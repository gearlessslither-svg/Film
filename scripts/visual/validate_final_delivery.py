#!/usr/bin/env python3
"""Validate final storyboard/audio/video delivery artifacts."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

import cv2
import soundfile as sf
from PIL import Image


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["check", "value", "status", "notes"])
        writer.writeheader()
        writer.writerows(rows)


def ok(condition: bool) -> str:
    return "pass" if condition else "fail"


def default_project_root() -> Path:
    bundled_layout_root = Path(__file__).resolve().parents[1]
    if (bundled_layout_root / "exports" / "panel_stage_state_map.csv").exists():
        return bundled_layout_root
    return Path.cwd().resolve()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate final storyboard, audio, and video delivery artifacts."
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=default_project_root(),
        help="Path to the 01_AIGC project root. Defaults to the current directory for standalone use.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.project_root.resolve()
    rows: list[dict[str, str]] = []

    stage_rows = read_csv(root / "exports/panel_stage_state_map.csv")
    prompt_rows = read_csv(root / "exports/micro_storyboard_pure_image_prompts.csv")
    queue_rows = read_csv(root / "exports/real_image_generation_queue.csv")
    manifest = read_csv(root / "exports/final_storyboard/final_storyboard_panel_manifest_v002.csv")
    qa_rows = read_csv(root / "exports/final_storyboard/final_storyboard_qa_v002.csv")
    timing_rows = read_csv(root / "exports/final_video/coin_slot_final_storyboard_video_v002_timing.csv")

    rows.append({"check": "stage_rows", "value": str(len(stage_rows)), "status": ok(len(stage_rows) == 188), "notes": ""})
    rows.append({"check": "prompt_rows", "value": str(len(prompt_rows)), "status": ok(len(prompt_rows) == 188), "notes": ""})
    rows.append({"check": "queue_rows", "value": str(len(queue_rows)), "status": ok(len(queue_rows) == 188), "notes": ""})
    max_q = max(r["pure_prompt"].count("?") for r in prompt_rows)
    rows.append({"check": "max_prompt_question_marks", "value": str(max_q), "status": ok(max_q == 0), "notes": ""})
    missing_whitebox = sum(1 for r in stage_rows if not (root / r["whitebox_reference_path"]).exists())
    rows.append({"check": "missing_whitebox", "value": str(missing_whitebox), "status": ok(missing_whitebox == 0), "notes": ""})

    source_counts = Counter(r["source_kind"] for r in manifest)
    rows.append({"check": "final_panel_manifest_rows", "value": str(len(manifest)), "status": ok(len(manifest) == 188), "notes": dict(source_counts).__repr__()})
    qa_pass = sum(1 for r in qa_rows if r["qa_status"] == "pass")
    rows.append({"check": "final_panel_qa_pass", "value": str(qa_pass), "status": ok(qa_pass == 188), "notes": ""})
    bad_dims = 0
    for row in manifest:
        path = root / row["final_panel_path"]
        if not path.exists():
            bad_dims += 1
            continue
        with Image.open(path) as img:
            if img.size != (1280, 720):
                bad_dims += 1
    rows.append({"check": "final_panel_dimensions_bad", "value": str(bad_dims), "status": ok(bad_dims == 0), "notes": "expected 1280x720"})

    contact_sheets = list((root / "final_storyboard_contact_sheets").glob("*_final_storyboard_contact_sheet_v002.jpg"))
    rows.append({"check": "contact_sheets", "value": str(len(contact_sheets)), "status": ok(len(contact_sheets) == 6), "notes": ""})

    audio = root / "audio/mix/coin_slot_audio_clean_v002.wav"
    info = sf.info(audio)
    audio_duration = info.frames / info.samplerate
    rows.append({"check": "audio_duration_sec", "value": f"{audio_duration:.3f}", "status": ok(abs(audio_duration - 351.0) < 0.02), "notes": "clean v002"})

    video = root / "exports/final_video/coin_slot_final_storyboard_video_v002.mp4"
    cap = cv2.VideoCapture(str(video))
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    video_duration = frames / fps if fps else 0.0
    rows.append({"check": "video_duration_sec", "value": f"{video_duration:.3f}", "status": ok(abs(video_duration - 351.0) < 0.05), "notes": f"frames={int(frames)} fps={fps:.3f}"})
    rows.append({"check": "timing_rows", "value": str(len(timing_rows)), "status": ok(len(timing_rows) == 188), "notes": ""})
    timing_total = sum(float(r["duration"]) for r in timing_rows)
    rows.append({"check": "timing_total_sec", "value": f"{timing_total:.3f}", "status": ok(abs(timing_total - 351.0) < 0.02), "notes": ""})

    out = root / "exports/final_delivery_validation_v002.csv"
    write_csv(out, rows)
    failed = [r for r in rows if r["status"] != "pass"]
    print(f"validation={out}")
    print(f"checks={len(rows)} failed={len(failed)}")
    for row in rows:
        print(f"{row['status']} {row['check']}={row['value']} {row['notes']}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
