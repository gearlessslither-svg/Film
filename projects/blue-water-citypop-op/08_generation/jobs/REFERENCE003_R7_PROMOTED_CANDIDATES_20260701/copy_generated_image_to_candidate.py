#!/usr/bin/env python3
"""Copy a generated image into an R7 candidate planned output path.

Usage:
  python copy_generated_image_to_candidate.py R7_CAND_006_end_028832ms --source /path/to/generated.png

If --source is omitted, the newest image under ~/.codex/generated_images is used.
The original generated image is left in place.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


JOB_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = JOB_DIR.parents[2]
QUEUE_PATH = JOB_DIR / "reference003_r7_candidate_image_generation_queue.json"
UPDATE_SCRIPT = JOB_DIR / "update_r7_promoted_candidate_manifests.py"
GENERATED_ROOT = Path.home() / ".codex/generated_images"
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}


def newest_generated_image() -> Path:
    candidates = [
        path
        for path in GENERATED_ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES
    ]
    if not candidates:
        raise SystemExit(f"No generated images found under {GENERATED_ROOT}")
    return max(candidates, key=lambda path: path.stat().st_mtime)


def load_candidate(asset_id: str) -> dict:
    queue = json.loads(QUEUE_PATH.read_text(encoding="utf-8"))
    for item in queue.get("items", []):
        if item.get("asset_id") == asset_id:
            return item
    raise SystemExit(f"Unknown asset_id: {asset_id}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("asset_id")
    parser.add_argument("--source", type=Path, help="Generated image to copy. Defaults to newest ~/.codex/generated_images image.")
    parser.add_argument("--no-refresh", action="store_true", help="Skip manifest refresh after copying.")
    args = parser.parse_args()

    item = load_candidate(args.asset_id)
    planned = item.get("planned_output_path")
    if not planned:
        raise SystemExit(f"Candidate has no planned_output_path: {args.asset_id}")

    source = args.source or newest_generated_image()
    if not source.exists():
        raise SystemExit(f"Missing source image: {source}")
    if source.suffix.lower() not in IMAGE_SUFFIXES:
        raise SystemExit(f"Unsupported image suffix: {source.suffix}")

    destination = PROJECT_ROOT / planned
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    print(f"copied {source} -> {destination}")

    if not args.no_refresh:
        subprocess.run(["python3", str(UPDATE_SCRIPT)], check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
