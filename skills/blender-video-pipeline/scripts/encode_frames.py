#!/usr/bin/env python3
import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def find_ffmpeg(explicit=None):
    if explicit:
        return explicit
    system = shutil.which("ffmpeg")
    if system:
        return system
    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def main():
    parser = argparse.ArgumentParser(description="Encode an image sequence to video.")
    parser.add_argument("--frames-dir", required=True, help="Directory containing frames.")
    parser.add_argument("--pattern", default="frame_%04d.png", help="FFmpeg input pattern, e.g. frame_%04d.png.")
    parser.add_argument("--start-number", type=int, default=1, help="First frame number.")
    parser.add_argument("--fps", type=float, default=24, help="Frames per second.")
    parser.add_argument("--output", required=True, help="Output video path.")
    parser.add_argument("--ffmpeg", help="Explicit FFmpeg executable.")
    parser.add_argument("--crf", type=int, default=18, help="H.264 quality, lower is better.")
    parser.add_argument("--preset", default="slow", help="FFmpeg x264 preset.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite output if it exists.")
    args = parser.parse_args()

    frames_dir = Path(args.frames_dir).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    if not frames_dir.exists():
        raise SystemExit(f"Missing frames directory: {frames_dir}")
    first = frames_dir / (args.pattern.replace("%04d", f"{args.start_number:04d}").replace("%05d", f"{args.start_number:05d}"))
    if "%" not in args.pattern and not first.exists():
        raise SystemExit(f"Input pattern must contain a printf frame number token or point to an existing file: {args.pattern}")
    if "%" in args.pattern and not first.exists():
        raise SystemExit(f"First frame not found: {first}")

    ffmpeg = find_ffmpeg(args.ffmpeg)
    if not ffmpeg:
        raise SystemExit("No FFmpeg found. Run bootstrap_video_env.py and retry with that venv's Python.")

    output.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        ffmpeg,
        "-y" if args.overwrite else "-n",
        "-framerate",
        str(args.fps),
        "-start_number",
        str(args.start_number),
        "-i",
        str(frames_dir / args.pattern),
        "-vf",
        "scale=trunc(iw/2)*2:trunc(ih/2)*2,format=yuv420p",
        "-c:v",
        "libx264",
        "-preset",
        args.preset,
        "-crf",
        str(args.crf),
        "-movflags",
        "+faststart",
        str(output),
    ]
    print(" ".join(cmd))
    result = subprocess.run(cmd)
    if result.returncode != 0:
        sys.exit(result.returncode)
    print(f"Encoded: {output}")


if __name__ == "__main__":
    main()
