#!/usr/bin/env python3
"""Assemble the final paced storyboard video with clean audio."""

from __future__ import annotations

import argparse
import csv
import subprocess
from pathlib import Path

import cv2
import imageio_ffmpeg
import numpy as np
import soundfile as sf
from PIL import Image


W, H = 1280, 720


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def parse_time(value: str) -> float:
    value = str(value).strip()
    minutes, seconds = value.split(":")
    return int(minutes) * 60 + float(seconds)


def load_frame(path: Path) -> np.ndarray:
    image = Image.open(path).convert("RGB")
    if image.size != (W, H):
        image = image.resize((W, H), Image.Resampling.LANCZOS)
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--fps", type=float, default=12.0)
    parser.add_argument("--audio", default="audio/mix/coin_slot_audio_clean_v002.wav")
    parser.add_argument("--manifest", default="exports/final_storyboard/final_storyboard_panel_manifest_v002.csv")
    parser.add_argument("--out-dir", default="exports/final_video")
    parser.add_argument("--stem", default="coin_slot_final_storyboard_video_v002")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    out_dir = root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    panels = read_csv(root / "19_micro_storyboard_188_panels.csv")
    manifest = {r["panel_id"]: r for r in read_csv(root / args.manifest)}
    audio_path = root / args.audio
    audio_duration = 351.0
    if audio_path.exists():
        info = sf.info(audio_path)
        audio_duration = info.frames / info.samplerate

    starts = [parse_time(r["approx_time"]) for r in panels]
    timing_rows: list[dict[str, str]] = []
    for idx, panel in enumerate(panels):
        start = starts[idx]
        end = starts[idx + 1] if idx + 1 < len(starts) else audio_duration
        end = max(start + 0.35, end)
        m = manifest[panel["panel_id"]]
        timing_rows.append(
            {
                "panel_id": panel["panel_id"],
                "clip": panel["clip"],
                "start": f"{start:.2f}",
                "end": f"{end:.2f}",
                "duration": f"{end - start:.2f}",
                "source_kind": m["source_kind"],
                "final_panel_path": m["final_panel_path"],
            }
        )

    timing_path = out_dir / f"{args.stem}_timing.csv"
    write_csv(
        timing_path,
        ["panel_id", "clip", "start", "end", "duration", "source_kind", "final_panel_path"],
        timing_rows,
    )

    silent = out_dir / f"{args.stem}_silent.mp4"
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(silent), fourcc, args.fps, (W, H))
    if not writer.isOpened():
        raise RuntimeError("Could not open OpenCV VideoWriter")

    for timing in timing_rows:
        frame = load_frame(root / timing["final_panel_path"])
        frame_count = max(1, round(float(timing["duration"]) * args.fps))
        for _ in range(frame_count):
            writer.write(frame)
    writer.release()

    final = out_dir / f"{args.stem}.mp4"
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
            "-b:a",
            "192k",
            "-shortest",
            str(final),
        ]
        result = subprocess.run(cmd, capture_output=True)
        if result.returncode != 0:
            print(result.stderr.decode("utf-8", errors="replace"))
            return 1
        print(f"video={final}")
    else:
        print(f"silent_video={silent}")
    print(f"timing={timing_path}")
    print(f"silent_video={silent}")
    print(f"audio={audio_path}")
    print(f"duration={audio_duration:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
