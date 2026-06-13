#!/usr/bin/env python3
"""Build guide WAV assets and a rough full-length mix from CSV manifests."""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy import signal


SR = 48_000


def parse_time(value: str) -> float:
    value = str(value).strip()
    if not value:
        return 0.0
    parts = value.split(":")
    if len(parts) == 2:
        return int(parts[0]) * 60 + float(parts[1])
    return float(value)


def db_to_amp(db: str) -> float:
    try:
        return 10 ** (float(db) / 20)
    except Exception:
        return 1.0


def soft_noise(seconds: float, seed: int, amp: float = 0.08) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = max(1, int(seconds * SR))
    data = rng.normal(0.0, amp, n)
    b, a = signal.butter(2, 0.08)
    return signal.lfilter(b, a, data)


def tone(seconds: float, freq: float, amp: float = 0.1) -> np.ndarray:
    n = max(1, int(seconds * SR))
    t = np.arange(n) / SR
    return amp * np.sin(2 * np.pi * freq * t)


def envelope(data: np.ndarray, attack: float = 0.01, release: float = 0.05) -> np.ndarray:
    n = len(data)
    env = np.ones(n)
    a = min(n, int(attack * SR))
    r = min(n, int(release * SR))
    if a > 0:
        env[:a] = np.linspace(0, 1, a)
    if r > 0:
        env[-r:] = np.linspace(1, 0, r)
    return data * env


def synth_asset(event_id: str, category: str, seconds: float, description: str = "") -> np.ndarray:
    seconds = max(0.2, seconds)
    seed = sum(ord(c) for c in event_id + category + description)
    lower = f"{event_id} {category} {description}".lower()

    if "amb" in event_id.lower() or category == "ambience":
        base = soft_noise(seconds, seed, 0.05)
        hum = tone(seconds, 50 + (seed % 30), 0.025)
        if "arcade" in lower or "crt" in lower:
            hum += tone(seconds, 1560, 0.015)
        return np.clip(base + hum, -1, 1)

    if category == "music" or event_id.lower().startswith("mus"):
        base = tone(seconds, 110 + (seed % 70), 0.07)
        base += tone(seconds, 220 + (seed % 120), 0.035)
        return envelope(base, 0.4, 0.8)

    if "foley" in event_id.lower() or category == "foley":
        n = int(seconds * SR)
        data = np.zeros(n)
        step_count = max(2, int(seconds * 2.2))
        rng = np.random.default_rng(seed)
        for i in range(step_count):
            pos = int((i + 0.35 + rng.uniform(-0.08, 0.08)) / step_count * n)
            length = int(0.055 * SR)
            burst = rng.normal(0, 0.18, length)
            burst = envelope(burst, 0.005, 0.04)
            end = min(n, pos + length)
            data[pos:end] += burst[: end - pos]
        return np.clip(data, -1, 1)

    # Hard SFX / transition placeholder: short pulsed tones plus filtered noise.
    n = int(seconds * SR)
    t = np.arange(n) / SR
    freq = 180 + (seed % 900)
    data = 0.10 * np.sin(2 * np.pi * freq * t)
    if "coin" in lower or "insert" in lower or "win" in lower:
        data += 0.08 * np.sign(np.sin(2 * np.pi * 880 * t))
    data += soft_noise(seconds, seed + 7, 0.025)
    return envelope(np.clip(data, -1, 1), 0.01, 0.15)


def read_audio(path: Path) -> tuple[np.ndarray, int]:
    data, sr = sf.read(path, always_2d=True)
    if data.shape[1] == 1:
        data = np.repeat(data, 2, axis=1)
    return data.astype(np.float32), int(sr)


def resample_to_sr(data: np.ndarray, sr: int) -> np.ndarray:
    if sr == SR:
        return data
    gcd = math.gcd(sr, SR)
    up = SR // gcd
    down = sr // gcd
    return signal.resample_poly(data, up, down, axis=0).astype(np.float32)


def write_mono(path: Path, data: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(path, data.astype(np.float32), SR)


def ensure_cue_assets(project_root: Path, force: bool = False) -> int:
    cue_path = project_root / "exports/sound_music_cue_sheet.csv"
    made = 0
    with cue_path.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            out = project_root / row["wav_name"]
            if out.exists() and not force:
                continue
            seconds = max(0.2, parse_time(row["time_end"]) - parse_time(row["time_start"]))
            data = synth_asset(row["cue_id"], row["category"], seconds, row.get("sonic_description", ""))
            write_mono(out, data)
            made += 1
    return made


def mix(project_root: Path, out_name: str) -> Path:
    manifest = project_root / "exports/audio_assembly_manifest.csv"
    with manifest.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    total = max(parse_time(r["end_time"]) for r in rows) + 1.0
    mixbuf = np.zeros((int(total * SR), 2), dtype=np.float32)

    for row in rows:
        start = parse_time(row["start_time"])
        end = parse_time(row["end_time"])
        wav = project_root / row["wav_name"]
        if not wav.exists():
            seconds = max(0.2, end - start)
            data = synth_asset(row["event_id"], row["track"], seconds, row.get("processing", ""))
            write_mono(wav, data)
        data, sr = read_audio(wav)
        data = resample_to_sr(data, sr)
        gain = db_to_amp(row.get("gain_db", "0"))
        data *= gain
        offset = int(start * SR)
        length = min(len(data), len(mixbuf) - offset)
        if length <= 0:
            continue
        mixbuf[offset : offset + length] += data[:length]

    peak = float(np.max(np.abs(mixbuf))) if mixbuf.size else 0.0
    if peak > 0.95:
        mixbuf = mixbuf / peak * 0.95
    out = project_root / out_name
    out.parent.mkdir(parents=True, exist_ok=True)
    sf.write(out, mixbuf, SR)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--force-cues", action="store_true")
    parser.add_argument("--out", default="audio/mix/coin_slot_audio_guide_v001.wav")
    args = parser.parse_args()
    project_root = Path(args.project_root).resolve()
    made = ensure_cue_assets(project_root, force=args.force_cues)
    out = mix(project_root, args.out)
    print(f"cue_assets_generated={made}")
    print(f"mix={out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
