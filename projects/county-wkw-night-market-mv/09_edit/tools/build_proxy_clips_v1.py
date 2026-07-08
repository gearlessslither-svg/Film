#!/usr/bin/env python3
"""Build local proxy clips for VP001-VP014.

Each proxy clip uses one keyframe with subtle local motion and ambience/SFX only.
The final proxy MV adds scratch music separately, so clip audio remains music-free.
"""

from __future__ import annotations

import csv
import math
import random
import struct
import subprocess
import wave
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter


ROOT = Path("/Users/jaychoupp/Story/Film/projects/county-wkw-night-market-mv")
FFMPEG = Path("/Users/jaychoupp/Library/Application Support/bilibili/ffmpeg/ffmpeg")
W, H = 1920, 824
FPS = 24
SR = 44100


ITEMS = [
    ("VP001", "KF001", "Night-market entry", "KF001_night_market_entry.png", 5.0, "rain_market_engine", 1.00, 1.045, -0.10, 0.02),
    ("VP002", "KF002", "Boy LED awning", "KF002_boy_led_awning.png", 5.0, "engine_neon_tarp", 1.02, 1.06, 0.08, -0.02),
    ("VP003", "KF003", "Girl game booth", "KF003_girl_game_booth.png", 5.0, "bulbs_crowd_steps", 1.00, 1.055, -0.06, 0.01),
    ("VP004", "KF004", "Beer-stall crossing", "KF004_beer_stall_crossing.png", 5.0, "barbecue_stools_crowd", 1.02, 1.06, 0.10, 0.00),
    ("VP005", "KF005", "Motorcycle start", "KF005_motorcycle_start.png", 5.0, "motorcycle_start_rain", 1.03, 1.08, -0.04, 0.02),
    ("VP006", "KF006", "Alley ride", "KF006_alley_ride.png", 6.0, "low_engine_wet_tires", 1.02, 1.07, 0.12, 0.00),
    ("VP007", "KF007", "Repair reflection", "KF007_repair_reflection.png", 6.0, "engine_off_tools_neon", 1.00, 1.05, -0.10, 0.00),
    ("VP008", "KF008", "Girl rain curtain", "KF008_girl_rain_curtain.png", 6.0, "tarp_drips_steps", 1.01, 1.06, 0.06, -0.01),
    ("VP009", "KF009", "Wholesale standoff", "KF009_wholesale_standoff.png", 7.0, "pre_dawn_truck_hum", 1.00, 1.035, 0.00, 0.00),
    ("VP010", "KF010", "Memory details", "KF010_memory_details.png", 5.0, "macro_drips_tarp_ticks", 1.05, 1.10, -0.08, 0.03),
    ("VP011", "KF011", "Ride out", "KF011_ride_out.png", 6.0, "ride_out_wind", 1.00, 1.045, 0.12, 0.00),
    ("VP012", "KF012", "Field road", "KF012_field_road.png", 6.0, "field_insects_wind", 1.00, 1.035, -0.06, 0.00),
    ("VP013", "KF013", "Girl departure", "KF013_girl_departure.png", 5.0, "distant_steps_insects", 1.00, 1.04, 0.04, 0.00),
    ("VP014", "KF014", "Boy stops", "KF014_boy_stops.png", 3.0, "field_wind_cooling", 1.00, 1.025, 0.00, 0.00),
]


def ease(x: float) -> float:
    return x * x * (3.0 - 2.0 * x)


def cover_resize(image: Image.Image, scale: float) -> Image.Image:
    target_w = math.ceil(W * scale)
    target_h = math.ceil(H * scale)
    iw, ih = image.size
    factor = max(target_w / iw, target_h / ih)
    return image.resize((math.ceil(iw * factor), math.ceil(ih * factor)), Image.Resampling.LANCZOS)


def render_frame(base: Image.Image, progress: float, z0: float, z1: float, pan_x: float, pan_y: float) -> Image.Image:
    e = ease(progress)
    img = cover_resize(base, z0 + (z1 - z0) * e)
    max_x = max(0, img.width - W)
    max_y = max(0, img.height - H)
    left = int(min(max(max_x / 2 + pan_x * max_x * (e - 0.5), 0), max_x))
    top = int(min(max(max_y / 2 + pan_y * max_y * (e - 0.5), 0), max_y))
    frame = img.crop((left, top, left + W, top + H))
    glow = frame.filter(ImageFilter.GaussianBlur(radius=0.25))
    return ImageEnhance.Contrast(Image.blend(frame, glow, 0.035)).enhance(1.025)


def tone(freq: float, t: float, phase: float = 0.0) -> float:
    return math.sin(2.0 * math.pi * freq * t + phase)


def pulse(local: float, length: float, attack: float = 0.01, release: float = 0.12) -> float:
    if local < 0.0 or local > length:
        return 0.0
    return max(0.0, min(local / attack, (length - local) / release, 1.0))


def noise(rng: random.Random) -> float:
    return rng.uniform(-1.0, 1.0)


def ambience_sample(kind: str, t: float, duration: float, rng: random.Random) -> tuple[float, float]:
    fade = min(1.0, t / 0.25, (duration - t) / 0.25)
    rain = noise(rng) * 0.020
    neon = tone(118.0, t) * 0.012 + tone(236.0, t) * 0.006
    crowd = (tone(92.0, t, 0.4) + tone(141.0, t, 1.1) + tone(211.0, t, 2.0)) * 0.012
    wind = (noise(rng) * 0.010 + tone(0.21, t) * 0.020)
    insects = (tone(3200.0 + 90.0 * tone(0.7, t), t) + tone(4100.0, t, 0.5)) * 0.006
    engine = (tone(46.0 + 2.0 * tone(1.7, t), t) + tone(92.0, t, 0.2) * 0.35) * 0.055
    tire = noise(rng) * 0.014 + tone(28.0, t) * 0.008
    drip_phase = t % 0.83
    drips = tone(880.0, t) * pulse(drip_phase, 0.055, 0.002, 0.035) * 0.055
    tools_phase = t % 1.9
    tools = tone(1300.0, t) * pulse(tools_phase, 0.045, 0.002, 0.026) * 0.030
    steps_phase = t % 0.72
    steps = noise(rng) * pulse(steps_phase, 0.08, 0.004, 0.05) * 0.045
    truck = tone(37.0, t) * 0.020 if 1.5 < t < duration - 1.0 else 0.0
    barbecue = noise(rng) * 0.014 + tone(2500.0, t) * pulse(t % 0.21, 0.035, 0.001, 0.025) * 0.020
    start_hit = tone(62.0, t) * pulse(t, 0.8, 0.004, 0.45) * 0.20
    cooling = tone(1040.0, t) * pulse(t % 1.25, 0.030, 0.001, 0.020) * 0.018

    mix = rain * 0.6
    if kind in {"rain_market_engine", "engine_neon_tarp"}:
        mix += engine + neon + crowd * 0.8 + drips
    elif kind == "bulbs_crowd_steps":
        mix += neon * 0.8 + crowd + steps + drips
    elif kind == "barbecue_stools_crowd":
        mix += barbecue + crowd + steps * 0.8 + drips
    elif kind == "motorcycle_start_rain":
        mix += start_hit + engine * 0.7 + drips + neon
    elif kind == "low_engine_wet_tires":
        mix += engine + tire + neon * 0.5
    elif kind == "engine_off_tools_neon":
        mix += engine * max(0.0, 1.0 - t / 2.0) + tools + neon + wind * 0.5
    elif kind == "tarp_drips_steps":
        mix += drips * 1.5 + steps + neon * 0.5 + crowd * 0.35
    elif kind == "pre_dawn_truck_hum":
        mix += truck + wind + neon * 0.25 + drips * 0.4
    elif kind == "macro_drips_tarp_ticks":
        mix += drips * 1.8 + tools * 0.4 + cooling
    elif kind == "ride_out_wind":
        mix += engine * 0.8 + tire + wind + truck * 0.4
    elif kind == "field_insects_wind":
        mix += insects + wind + cooling
    elif kind == "distant_steps_insects":
        mix += insects + wind + steps * 0.5 + truck * 0.4
    elif kind == "field_wind_cooling":
        mix += insects + wind + cooling
    else:
        mix += wind
    mix *= fade
    return max(-0.95, min(0.95, mix)), max(-0.95, min(0.95, mix * 0.92 + tone(0.11, t) * 0.004))


def write_wav(path: Path, kind: str, duration: float, seed: int) -> None:
    rng = random.Random(seed)
    total = int(duration * SR)
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(SR)
        for n in range(total):
            t = n / SR
            left, right = ambience_sample(kind, t, duration, rng)
            wav.writeframes(struct.pack("<hh", int(left * 32767), int(right * 32767)))


def build_clip(item: tuple, index: int, out_dir: Path) -> Path:
    vp_id, kf_id, beat, filename, duration, ambience, z0, z1, pan_x, pan_y = item
    keyframes = ROOT / "08_generation/jobs/keyframes_v1/outputs"
    audio_path = out_dir / "audio" / f"{vp_id}_{kf_id}_ambience_only.wav"
    clip_path = out_dir / "outputs" / f"{vp_id}_{kf_id}_local_proxy_clip.mp4"
    audio_path.parent.mkdir(parents=True, exist_ok=True)
    clip_path.parent.mkdir(parents=True, exist_ok=True)
    write_wav(audio_path, ambience, duration, 7000 + index)
    cmd = [
        str(FFMPEG), "-y", "-hide_banner", "-loglevel", "error",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-i", str(audio_path),
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(clip_path),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    assert proc.stdin is not None
    base = Image.open(keyframes / filename).convert("RGB")
    frame_count = round(duration * FPS)
    for idx in range(frame_count):
        frame = render_frame(base, idx / max(1, frame_count - 1), z0, z1, pan_x, pan_y)
        proc.stdin.write(frame.tobytes())
    proc.stdin.close()
    ret = proc.wait()
    if ret:
        raise RuntimeError(f"ffmpeg failed for {vp_id} with {ret}")
    return clip_path


def write_manifest(out_dir: Path, clips: list[Path]) -> None:
    with (out_dir / "local_proxy_clips_timing.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["vp_id", "kf_id", "beat", "source_keyframe", "duration_sec", "clip_path", "audio_rule"])
        for item, clip in zip(ITEMS, clips):
            vp_id, kf_id, beat, filename, duration, *_ = item
            writer.writerow([vp_id, kf_id, beat, filename, f"{duration:.2f}", clip.relative_to(ROOT), "ambience/SFX only; no music/BGM/soundtrack"])
    with (out_dir / "ffmpeg_concat_clips.txt").open("w", encoding="utf-8") as f:
        for clip in clips:
            f.write(f"file '{clip}'\n")


def main() -> int:
    out_dir = ROOT / "09_edit/proxy_clips/local_proxy_clips_v1"
    out_dir.mkdir(parents=True, exist_ok=True)
    clips = [build_clip(item, idx, out_dir) for idx, item in enumerate(ITEMS, start=1)]
    write_manifest(out_dir, clips)
    print("clips", len(clips))
    print(out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
