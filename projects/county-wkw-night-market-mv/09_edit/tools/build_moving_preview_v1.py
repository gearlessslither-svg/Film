#!/usr/bin/env python3
"""Build a local moving preview from V1 keyframes.

This is an edit preview, not a replacement for external image-to-video clips.
It adds subtle pan/zoom motion and an original scratch music bed.
"""

from __future__ import annotations

import csv
import math
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
    ("KF001", "0-5s", "Night-market entry", "KF001_night_market_entry.png", 5.0, 1.00, 1.045, -0.10, 0.02),
    ("KF002", "5-10s", "Boy LED awning", "KF002_boy_led_awning.png", 5.0, 1.02, 1.06, 0.08, -0.02),
    ("KF003", "10-15s", "Girl game booth", "KF003_girl_game_booth.png", 5.0, 1.00, 1.055, -0.06, 0.01),
    ("KF004", "15-20s", "Beer-stall crossing", "KF004_beer_stall_crossing.png", 5.0, 1.02, 1.06, 0.10, 0.00),
    ("KF005", "20-25s", "Motorcycle start", "KF005_motorcycle_start.png", 5.0, 1.03, 1.08, -0.04, 0.02),
    ("KF006", "25-31s", "Alley ride", "KF006_alley_ride.png", 6.0, 1.02, 1.07, 0.12, 0.00),
    ("KF007", "31-37s", "Repair reflection", "KF007_repair_reflection.png", 6.0, 1.00, 1.05, -0.10, 0.00),
    ("KF008", "37-43s", "Girl rain curtain", "KF008_girl_rain_curtain.png", 6.0, 1.01, 1.06, 0.06, -0.01),
    ("KF009", "43-50s", "Wholesale standoff", "KF009_wholesale_standoff.png", 7.0, 1.00, 1.035, 0.00, 0.00),
    ("KF010", "50-55s", "Memory details", "KF010_memory_details.png", 5.0, 1.05, 1.10, -0.08, 0.03),
    ("KF011", "55-61s", "Ride out", "KF011_ride_out.png", 6.0, 1.00, 1.045, 0.12, 0.00),
    ("KF012", "61-67s", "Field road", "KF012_field_road.png", 6.0, 1.00, 1.035, -0.06, 0.00),
    ("KF013", "67-72s", "Girl departure", "KF013_girl_departure.png", 5.0, 1.00, 1.04, 0.04, 0.00),
    ("KF014", "72-75s", "Boy stops", "KF014_boy_stops.png", 3.0, 1.00, 1.025, 0.00, 0.00),
]


def ease(x: float) -> float:
    return x * x * (3.0 - 2.0 * x)


def cover_resize(image: Image.Image, scale: float) -> Image.Image:
    target_w = math.ceil(W * scale)
    target_h = math.ceil(H * scale)
    iw, ih = image.size
    factor = max(target_w / iw, target_h / ih)
    resized = image.resize((math.ceil(iw * factor), math.ceil(ih * factor)), Image.Resampling.LANCZOS)
    return resized


def render_frame(base: Image.Image, progress: float, z0: float, z1: float, pan_x: float, pan_y: float) -> Image.Image:
    e = ease(progress)
    scale = z0 + (z1 - z0) * e
    img = cover_resize(base, scale)
    max_x = max(0, img.width - W)
    max_y = max(0, img.height - H)
    cx = max_x / 2 + pan_x * max_x * (e - 0.5)
    cy = max_y / 2 + pan_y * max_y * (e - 0.5)
    left = int(min(max(cx, 0), max_x))
    top = int(min(max(cy, 0), max_y))
    frame = img.crop((left, top, left + W, top + H))
    if progress < 0.8:
        strength = progress / 0.8
    else:
        strength = (1.0 - progress) / 0.2
    strength = max(0.0, min(1.0, strength))
    if strength > 0:
        glow = frame.filter(ImageFilter.GaussianBlur(radius=0.35))
        frame = Image.blend(frame, glow, 0.04 * strength)
    return ImageEnhance.Contrast(frame).enhance(1.03)


def write_timing(out_dir: Path) -> None:
    with (out_dir / "moving_preview_timing.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["item_id", "time_range", "beat", "source_keyframe", "duration_sec"])
        for item_id, time_range, beat, name, duration, *_ in ITEMS:
            writer.writerow([item_id, time_range, beat, name, f"{duration:.2f}"])


def note(freq: float, t: float, phase: float = 0.0) -> float:
    return math.sin(2.0 * math.pi * freq * t + phase)


def env_pulse(local: float, length: float, attack: float = 0.01, release: float = 0.12) -> float:
    if local < 0 or local > length:
        return 0.0
    a = min(1.0, local / max(attack, 1e-6))
    r = min(1.0, (length - local) / max(release, 1e-6))
    return max(0.0, min(a, r))


def generate_scratch_music(path: Path, duration: float) -> None:
    bpm = 86.0
    beat = 60.0 / bpm
    chords = [
        (55.00, 65.41, 82.41, 110.00),  # A minor color
        (43.65, 65.41, 87.31, 130.81),  # F major color
        (32.70, 65.41, 98.00, 130.81),  # C major color
        (49.00, 61.74, 98.00, 146.83),  # G color
    ]
    total = int(duration * SR)
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(SR)
        for n in range(total):
            t = n / SR
            section = min(3, int(t // 18.75))
            chord = chords[(int(t // (beat * 8)) + section) % len(chords)]
            bar_pos = t % (beat * 4)
            beat_pos = t % beat
            fade_in = min(1.0, t / 9.0)
            fade_out = min(1.0, max(0.0, (duration - t) / 8.0))
            level = fade_in * fade_out

            pad = 0.0
            for idx, f in enumerate(chord):
                pad += note(f, t, phase=idx * 0.7) * 0.055
                pad += note(f * 2.0, t, phase=idx * 0.33) * 0.018
            lfo = 0.75 + 0.25 * note(0.08, t)
            pad *= lfo

            bass_freq = chord[0]
            bass_env = env_pulse(beat_pos, beat * 0.85, attack=0.012, release=0.24)
            bass = note(bass_freq, t) * 0.16 * bass_env

            kick = 0.0
            snare = 0.0
            hat = 0.0
            if t > 14.0 and t < 63.5:
                kick = math.sin(2 * math.pi * (70 - 32 * min(1.0, beat_pos / 0.18)) * beat_pos) * env_pulse(beat_pos, 0.22, 0.003, 0.16) * 0.22
                snare_pos = (t - beat * 2) % (beat * 4)
                snare = (math.sin(2 * math.pi * 180 * t) + math.sin(2 * math.pi * 265 * t)) * env_pulse(snare_pos, 0.18, 0.004, 0.10) * 0.045
                hat_pos = t % (beat / 2)
                hat = math.sin(2 * math.pi * 6400 * t) * env_pulse(hat_pos, 0.035, 0.001, 0.025) * 0.018

            field = note(330.0 + 8 * note(0.03, t), t) * 0.012
            sample_l = (pad + bass + kick + snare + hat + field) * level
            sample_r = (pad * 0.94 + bass + kick + snare * 0.9 - hat + field * 1.2) * level
            sample_l = max(-0.95, min(0.95, sample_l))
            sample_r = max(-0.95, min(0.95, sample_r))
            wav.writeframes(struct.pack("<hh", int(sample_l * 32767), int(sample_r * 32767)))


def build_video(root: Path, out_dir: Path) -> None:
    keyframes = root / "08_generation/jobs/keyframes_v1/outputs"
    audio = out_dir / "scratch_music_v1_original.wav"
    video = out_dir / "county_wkw_moving_preview_v1_with_scratch_music.mp4"
    duration = sum(item[4] for item in ITEMS)
    generate_scratch_music(audio, duration)

    cmd = [
        str(FFMPEG),
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-f",
        "rawvideo",
        "-pix_fmt",
        "rgb24",
        "-s",
        f"{W}x{H}",
        "-r",
        str(FPS),
        "-i",
        "-",
        "-i",
        str(audio),
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-crf",
        "18",
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-shortest",
        "-movflags",
        "+faststart",
        str(video),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    assert proc.stdin is not None
    for item_id, _time_range, _beat, name, duration, z0, z1, pan_x, pan_y in ITEMS:
        base = Image.open(keyframes / name).convert("RGB")
        frame_count = round(duration * FPS)
        for idx in range(frame_count):
            progress = idx / max(1, frame_count - 1)
            frame = render_frame(base, progress, z0, z1, pan_x, pan_y)
            proc.stdin.write(frame.tobytes())
    proc.stdin.close()
    ret = proc.wait()
    if ret != 0:
        raise RuntimeError(f"ffmpeg failed with code {ret}")


def main() -> int:
    out_dir = ROOT / "09_edit/animatics/moving_preview_v1"
    out_dir.mkdir(parents=True, exist_ok=True)
    write_timing(out_dir)
    build_video(ROOT, out_dir)
    print(out_dir / "county_wkw_moving_preview_v1_with_scratch_music.mp4")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
