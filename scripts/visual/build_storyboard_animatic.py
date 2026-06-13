#!/usr/bin/env python3
"""Build a timed storyboard animatic from pure images or whitebox fallbacks."""

from __future__ import annotations

import argparse
import csv
import subprocess
from pathlib import Path

import cv2
import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import soundfile as sf


W, H = 1280, 720


def parse_time(value: str) -> float:
    value = str(value).strip()
    if not value:
        return 0.0
    minutes, seconds = value.split(":")
    return int(minutes) * 60 + float(seconds)


def fit_image(path: Path) -> Image.Image:
    image = Image.open(path).convert("RGB")
    iw, ih = image.size
    scale = min(W / iw, H / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    image = image.resize((nw, nh), Image.LANCZOS)
    canvas = Image.new("RGB", (W, H), (10, 10, 10))
    canvas.paste(image, ((W - nw) // 2, (H - nh) // 2))
    return canvas


def load_font(size: int) -> ImageFont.ImageFont:
    for path in [r"C:\Windows\Fonts\msyh.ttc", r"C:\Windows\Fonts\simhei.ttf", r"C:\Windows\Fonts\arial.ttf"]:
        if Path(path).exists():
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


def overlay(image: Image.Image, row: dict[str, str], source_kind: str) -> Image.Image:
    out = image.copy()
    draw = ImageDraw.Draw(out, "RGBA")
    font = load_font(20)
    small = load_font(16)
    draw.rectangle((0, 0, W, 58), fill=(0, 0, 0, 150))
    title = f"{row['panel_id']}  Clip {row['clip']}  {row['approx_time']}  {source_kind}"
    draw.text((18, 12), title, font=font, fill=(255, 255, 255, 235))
    draw.text((18, 36), f"{row.get('beat','')} | {row.get('shot_size','')}", font=small, fill=(220, 220, 220, 220))
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--fps", type=float, default=12.0)
    parser.add_argument("--audio", default="audio/mix/coin_slot_audio_guide_v001.wav")
    parser.add_argument("--out-dir", default="exports/animatic")
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    out_dir = project_root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    with (project_root / "19_micro_storyboard_188_panels.csv").open("r", encoding="utf-8-sig", newline="") as f:
        panels = list(csv.DictReader(f))
    with (project_root / "exports/panel_stage_state_map.csv").open("r", encoding="utf-8-sig", newline="") as f:
        stage = {r["panel_id"]: r for r in csv.DictReader(f)}

    audio_path = project_root / args.audio
    audio_duration = 350.0
    if audio_path.exists():
        info = sf.info(audio_path)
        audio_duration = info.frames / info.samplerate

    timing_rows = []
    starts = [parse_time(r["approx_time"]) for r in panels]
    for idx, row in enumerate(panels):
        start = starts[idx]
        end = starts[idx + 1] if idx + 1 < len(starts) else audio_duration
        end = max(start + 0.35, end)
        pure = project_root / "visual_assets/pure/micro_storyboard" / f"B{int(row['clip'])//4+1:02d}" / f"{row['panel_id']}_v001.png"
        # Use the planned pure path when available in the prompt table.
        pure_path = None
        if (project_root / "exports/micro_storyboard_pure_image_prompts.csv").exists():
            pass
        prompt_pure = project_root / f"visual_assets/pure/micro_storyboard/{stage[row['panel_id']]['whitebox_reference_path'].split('/')[1] if stage[row['panel_id']]['whitebox_reference_path'] else 'B01'}"
        planned_pure = None
        # Direct known pure layout from manifest.
        for batch in ["B01", "B02", "B03", "B04", "B05", "B06"]:
            candidate = project_root / f"visual_assets/pure/micro_storyboard/{batch}/{row['panel_id']}_v001.png"
            if candidate.exists():
                planned_pure = candidate
                break
        if planned_pure:
            source = planned_pure
            source_kind = "REAL"
        else:
            source = project_root / stage[row["panel_id"]]["whitebox_reference_path"]
            source_kind = "WHITEBOX"
        timing_rows.append({
            "panel_id": row["panel_id"],
            "clip": row["clip"],
            "start": f"{start:.2f}",
            "end": f"{end:.2f}",
            "duration": f"{end - start:.2f}",
            "source_kind": source_kind,
            "source_path": str(source.relative_to(project_root)).replace("\\", "/"),
        })

    timing_path = out_dir / "animatic_panel_timing.csv"
    with timing_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(timing_rows[0].keys()))
        writer.writeheader()
        writer.writerows(timing_rows)

    silent = out_dir / "coin_slot_storyboard_animatic_v001_silent.mp4"
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(silent), fourcc, args.fps, (W, H))
    if not writer.isOpened():
        raise RuntimeError("Could not open OpenCV VideoWriter")

    for row, timing in zip(panels, timing_rows):
        source = project_root / timing["source_path"]
        frame = overlay(fit_image(source), row, timing["source_kind"])
        arr = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
        frames = max(1, round(float(timing["duration"]) * args.fps))
        for _ in range(frames):
            writer.write(arr)
    writer.release()

    final = out_dir / "coin_slot_storyboard_animatic_v001.mp4"
    if audio_path.exists():
        ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
        cmd = [
            ffmpeg,
            "-y",
            "-i",
            str(silent),
            "-i",
            str(audio_path),
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-shortest",
            str(final),
        ]
        result = subprocess.run(cmd, capture_output=True)
        if result.returncode != 0:
            print(result.stderr.decode("utf-8", errors="replace"))
            print(f"silent_video={silent}")
            print(f"audio={audio_path}")
            return 1
        print(f"video={final}")
    else:
        print(f"silent_video={silent}")
    print(f"timing={timing_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
