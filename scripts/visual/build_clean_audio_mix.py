#!/usr/bin/env python3
"""Build a cleaner low-noise audio guide mix.

The first guide intentionally used procedural noise for ambience and foley.
This version keeps timing and story cues, but rebuilds non-voice assets with
mostly tonal/filtered material and lower beds so the animatic is easier to
review without broadband hiss.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy import signal


SR = 48_000


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def parse_time(value: str) -> float:
    value = str(value).strip()
    if not value:
        return 0.0
    parts = value.split(":")
    if len(parts) == 2:
        return int(parts[0]) * 60 + float(parts[1])
    return float(value)


def db_to_amp(db: float | str) -> float:
    text = str(db).strip().lower()
    if text.startswith("-inf"):
        return 0.0
    return 10 ** (float(text.split()[0]) / 20)


def parse_db(db: str, fallback: float = 0.0) -> float:
    text = str(db).strip().lower()
    if text.startswith("-inf"):
        return -120.0
    try:
        return float(text.split()[0])
    except Exception:
        return fallback


def env(data: np.ndarray, attack: float = 0.03, release: float = 0.08) -> np.ndarray:
    n = len(data)
    out = np.ones(n)
    a = min(n, int(attack * SR))
    r = min(n, int(release * SR))
    if a:
        out[:a] = np.linspace(0, 1, a)
    if r:
        out[-r:] = np.linspace(1, 0, r)
    if data.ndim == 2:
        out = out.reshape(-1, 1)
    return data * out


def sine(seconds: float, freq: float, amp: float, phase: float = 0.0) -> np.ndarray:
    n = max(1, int(seconds * SR))
    t = np.arange(n) / SR
    return amp * np.sin(2 * np.pi * freq * t + phase)


def square_soft(seconds: float, freq: float, amp: float) -> np.ndarray:
    data = np.tanh(2.4 * sine(seconds, freq, 1.0, 0.0))
    return amp * data


def butter_filter(data: np.ndarray, cutoff: float, btype: str, order: int = 3) -> np.ndarray:
    b, a = signal.butter(order, cutoff / (SR / 2), btype=btype)
    return signal.lfilter(b, a, data, axis=0).astype(np.float32)


def low_noise_air(seconds: float, seed: int, amp: float = 0.004, cutoff: float = 900.0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = max(1, int(seconds * SR))
    data = rng.normal(0.0, amp, n)
    data = butter_filter(data, cutoff, "lowpass", 2)
    return data[:, 0] if data.ndim == 2 else data


def click_train(seconds: float, seed: int, rate: float, amp: float, lowpass: float = 1300.0) -> np.ndarray:
    n = max(1, int(seconds * SR))
    data = np.zeros(n, dtype=np.float32)
    rng = np.random.default_rng(seed)
    count = max(1, int(seconds * rate))
    for idx in range(count):
        pos = int((idx + 0.35 + rng.uniform(-0.08, 0.08)) / count * n)
        length = min(n - pos, int(0.045 * SR))
        if length <= 0:
            continue
        burst = rng.normal(0, amp, length).astype(np.float32)
        burst = butter_filter(burst.reshape(-1, 1), lowpass, "lowpass", 2).reshape(-1)
        data[pos : pos + length] += env(burst, 0.002, 0.04)
    return data


def clean_synth(event_id: str, track: str, seconds: float, description: str = "") -> np.ndarray:
    seconds = max(0.2, seconds)
    seed = sum(ord(c) for c in event_id + track + description)
    lower = f"{event_id} {track} {description}".lower()

    if "sil" in event_id.lower() or track == "silence":
        return np.zeros(int(seconds * SR), dtype=np.float32)

    if track == "ambience" or event_id.lower().startswith("amb"):
        base_freq = 46 + seed % 34
        data = sine(seconds, base_freq, 0.010)
        data += sine(seconds, base_freq * 2.01, 0.004, 0.6)
        data += sine(seconds, 0.17 + (seed % 7) * 0.03, 0.002)
        if "arcade" in lower or "crt" in lower:
            data += sine(seconds, 1560, 0.004)
            data += square_soft(seconds, 7.5, 0.002)
        if "corridor" in lower or "phone" in lower:
            data += sine(seconds, 410, 0.003)
        data += low_noise_air(seconds, seed, 0.0018, 550.0)
        return env(np.clip(data, -1, 1), 0.4, 0.8)

    if track == "music" or event_id.lower().startswith("mus"):
        root = 82 + (seed % 30)
        data = sine(seconds, root, 0.030)
        data += sine(seconds, root * 1.5, 0.016, 0.4)
        data += sine(seconds, root * 2.0, 0.010, 1.2)
        if "8bit" in lower or "stage" in lower:
            pulse = (np.sin(2 * np.pi * 2.0 * np.arange(int(seconds * SR)) / SR) > 0).astype(np.float32)
            data += square_soft(seconds, 440 + (seed % 80), 0.010) * pulse
        return env(np.clip(data, -1, 1), 0.6, 1.2)

    if "foley" in event_id.lower() or track == "foley":
        return env(click_train(seconds, seed, 1.6 if "steps" in lower else 2.2, 0.055, 800.0), 0.01, 0.08)

    n = max(1, int(seconds * SR))
    t = np.arange(n) / SR
    data = np.zeros(n, dtype=np.float32)
    if "coin" in lower or "insert" in lower:
        data += env(sine(seconds, 1280, 0.050) + sine(seconds, 1920, 0.025), 0.002, 0.28)
    elif "ring" in lower or "phone" in lower:
        ring = sine(seconds, 920, 0.038) * (0.5 + 0.5 * np.sin(2 * np.pi * 5.0 * t))
        data += env(ring, 0.02, 0.2)
    elif "impact" in lower or "stone" in lower:
        thud = sine(seconds, 78, 0.075) + click_train(seconds, seed, 1.0, 0.045, 450.0)
        data += env(thud, 0.004, 0.22)
    elif "button" in lower or "arcade" in lower:
        data += click_train(seconds, seed, 7.0, 0.030, 1800.0)
        data += square_soft(seconds, 680, 0.008)
    elif "glitch" in lower or "scanline" in lower or "morph" in lower:
        sweep = signal.chirp(t, f0=180, f1=1800, t1=seconds, method="quadratic").astype(np.float32)
        data += env(0.040 * sweep + square_soft(seconds, 14.0, 0.012), 0.01, 0.35)
    else:
        data += env(sine(seconds, 260 + (seed % 500), 0.030), 0.01, 0.18)
    return butter_filter(np.clip(data, -1, 1).reshape(-1, 1), 7200, "lowpass", 3).reshape(-1)


def read_audio(path: Path) -> tuple[np.ndarray, int]:
    data, sr = sf.read(path, always_2d=True)
    if data.shape[1] == 1:
        data = np.repeat(data, 2, axis=1)
    return data.astype(np.float32), int(sr)


def resample_to_sr(data: np.ndarray, sr: int) -> np.ndarray:
    if sr == SR:
        return data.astype(np.float32)
    gcd = math.gcd(sr, SR)
    return signal.resample_poly(data, SR // gcd, sr // gcd, axis=0).astype(np.float32)


def clean_voice(data: np.ndarray) -> np.ndarray:
    data = butter_filter(data, 80, "highpass", 2)
    data = butter_filter(data, 9000, "lowpass", 4)
    peak = float(np.max(np.abs(data))) if data.size else 0.0
    if peak > 0.98:
        data = data / peak * 0.98
    return env(data, 0.006, 0.03).astype(np.float32)


def write_audio(path: Path, data: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(path, data.astype(np.float32), SR, subtype="PCM_16")


def clean_asset_path(original: str) -> str:
    parts = Path(original).parts
    if len(parts) >= 2 and parts[0] == "audio":
        return str(Path("audio_clean", *parts[1:])).replace("\\", "/")
    return str(Path("audio_clean", original)).replace("\\", "/")


def asset_for_row(root: Path, row: dict[str, str], force: bool = False) -> tuple[Path, str]:
    original = root / row["wav_name"]
    clean_rel = clean_asset_path(row["wav_name"])
    clean = root / clean_rel
    if clean.exists() and not force:
        return clean, clean_rel

    seconds = max(0.2, parse_time(row["end_time"]) - parse_time(row["start_time"]))
    track = row["track"]
    if track.startswith("voice") and original.exists():
        data, sr = read_audio(original)
        data = clean_voice(resample_to_sr(data, sr))
        write_audio(clean, data)
    else:
        mono = clean_synth(row["event_id"], track, seconds, row.get("processing", ""))
        write_audio(clean, np.repeat(mono.reshape(-1, 1), 2, axis=1))
    return clean, clean_rel


def high_frequency_ratio(data: np.ndarray, sr: int, threshold: float = 8000.0) -> float:
    mono = data.mean(axis=1) if data.ndim == 2 else data
    if len(mono) < 2048:
        return 0.0
    freqs, power = signal.welch(mono, fs=sr, nperseg=4096)
    total = float(np.sum(power)) + 1e-12
    high = float(np.sum(power[freqs >= threshold]))
    return high / total


def stats_for(path: Path) -> dict[str, str]:
    data, sr = read_audio(path)
    peak = float(np.max(np.abs(data))) if data.size else 0.0
    rms = float(np.sqrt(np.mean(data**2))) if data.size else 0.0
    crest = 20 * math.log10((peak + 1e-12) / (rms + 1e-12))
    return {
        "file": path.as_posix(),
        "duration_sec": f"{len(data) / sr:.3f}",
        "sample_rate": str(sr),
        "peak": f"{peak:.6f}",
        "rms": f"{rms:.6f}",
        "crest_db": f"{crest:.3f}",
        "hf_ratio_8k": f"{high_frequency_ratio(data, sr, 8000):.8f}",
        "hf_ratio_10k": f"{high_frequency_ratio(data, sr, 10000):.8f}",
    }


def mix(project_root: Path, out_rel: str, force_assets: bool = False) -> tuple[Path, list[dict[str, str]]]:
    rows = read_csv(project_root / "exports/audio_assembly_manifest.csv")
    total = max(parse_time(r["end_time"]) for r in rows) + 1.0
    mixbuf = np.zeros((int(total * SR), 2), dtype=np.float32)
    clean_manifest: list[dict[str, str]] = []

    track_trim_db = {
        "ambience": -8.0,
        "music": -4.0,
        "sfx": -2.5,
        "foley": -2.5,
        "voice_walla": -4.0,
        "voice_processed": -2.0,
        "voice_dialogue": 0.0,
    }

    for row in rows:
        clean_path, clean_rel = asset_for_row(project_root, row, force=force_assets)
        data, sr = read_audio(clean_path)
        data = resample_to_sr(data, sr)
        gain_db = parse_db(row.get("gain_db", "0")) + track_trim_db.get(row["track"], -1.0)
        data *= db_to_amp(gain_db)
        start = parse_time(row["start_time"])
        offset = int(start * SR)
        length = min(len(data), len(mixbuf) - offset)
        if length > 0:
            mixbuf[offset : offset + length] += data[:length]
        clean_row = dict(row)
        clean_row["clean_wav_name"] = clean_rel
        clean_row["clean_gain_db"] = f"{gain_db:.1f}"
        clean_manifest.append(clean_row)

    mixbuf = butter_filter(mixbuf, 35, "highpass", 2)
    mixbuf = butter_filter(mixbuf, 11500, "lowpass", 4)
    peak = float(np.max(np.abs(mixbuf))) if mixbuf.size else 0.0
    if peak > 0:
        ceiling = db_to_amp(-1.0)
        mixbuf = np.tanh(mixbuf / ceiling) * ceiling
    peak = float(np.max(np.abs(mixbuf))) if mixbuf.size else 0.0
    if peak > db_to_amp(-1.0):
        mixbuf = mixbuf / peak * db_to_amp(-1.0)
    out = project_root / out_rel
    write_audio(out, mixbuf)
    return out, clean_manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--out", default="audio/mix/coin_slot_audio_clean_v002.wav")
    parser.add_argument("--force-assets", action="store_true")
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    out, clean_manifest = mix(project_root, args.out, args.force_assets)

    manifest_path = project_root / "exports/audio_clean_assembly_manifest_v002.csv"
    fields = list(clean_manifest[0].keys())
    with manifest_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(clean_manifest)

    qa_rows = []
    old = project_root / "audio/mix/coin_slot_audio_guide_v001.wav"
    if old.exists():
        row = stats_for(old)
        row["version"] = "v001_noisy_guide"
        qa_rows.append(row)
    row = stats_for(out)
    row["version"] = "v002_clean_low_noise"
    qa_rows.append(row)

    qa_path = project_root / "exports/audio_clean_qa_v002.csv"
    with qa_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "version",
                "file",
                "duration_sec",
                "sample_rate",
                "peak",
                "rms",
                "crest_db",
                "hf_ratio_8k",
                "hf_ratio_10k",
            ],
        )
        writer.writeheader()
        writer.writerows(qa_rows)

    print(f"clean_mix={out}")
    print(f"clean_manifest={manifest_path}")
    print(f"audio_qa={qa_path}")
    for row in qa_rows:
        print(
            f"{row['version']} duration={row['duration_sec']} peak={row['peak']} "
            f"rms={row['rms']} hf8k={row['hf_ratio_8k']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
