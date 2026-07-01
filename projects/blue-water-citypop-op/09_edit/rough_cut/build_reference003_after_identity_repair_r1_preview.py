#!/usr/bin/env python3
"""Build Reference-003 preview after identity repair R1.

This preview is assembled from the current idea_board output paths. It does not
use proxy substitutions; OP_SHOT_024, OP_SHOT_025, and OP_SHOT_034 should already
point at the R1 replacement images before this script runs.
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Any

from PIL import Image


PROJECT_ROOT = Path(__file__).resolve().parents[2]
BOARD_PATH = PROJECT_ROOT / "03_story/idea_board/idea_board.json"
SOURCE_AUDIO_VIDEO = PROJECT_ROOT / "01_intake/references/reference-003-full-op-2160p.mp4"
OUT_DIR = PROJECT_ROOT / "09_edit/rough_cut/after_identity_repair_r1"
FRAMES_DIR = OUT_DIR / "frames_1920x824_jpg"
CONCAT_PATH = OUT_DIR / "reference003_after_identity_repair_r1_concat.txt"
REPORT_JSON = OUT_DIR / "reference003_after_identity_repair_r1_manifest.json"
REPORT_MD = OUT_DIR / "reference003_after_identity_repair_r1_manifest.md"
OUTPUT_MP4 = (
    PROJECT_ROOT
    / "09_edit/rough_cut/reference003_after_identity_repair_r1_1080p_with_music_20260630.mp4"
)
FFMPEG = Path("/Applications/Bitwig Studio.app/Contents/MacOS/ffmpeg")
END_TOTAL_SEC = 84.437333

REQUIRED_R1_OUTPUTS = {
    "OP_SHOT_024": "08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/outputs/OP_SHOT_024_VEHICLE_LOCK_R1.png",
    "OP_SHOT_025": "08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/outputs/OP_SHOT_025_R1.png",
    "OP_SHOT_034": "08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/outputs/OP_SHOT_034_R1.png",
}


def rel(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def parse_time(value: str) -> float:
    minutes, seconds = value.split(":")
    return int(minutes) * 60 + float(seconds)


def extract_reference_time(row: dict[str, Any]) -> float:
    text = f"{row.get('image_prompt') or ''}\n{row.get('video_prompt') or ''}"
    match = re.search(r"Reference source:.*? at ([0-9]{2}:[0-9]{2}(?:\.[0-9]+)?)", text)
    if not match:
        raise ValueError(f"Missing reference time for {row.get('item_id')}")
    return parse_time(match.group(1))


def load_rows() -> list[dict[str, Any]]:
    rows = json.loads(BOARD_PATH.read_text())["rows"]
    items: list[dict[str, Any]] = []
    for row in rows:
        if row.get("status") != "generated_reference003_qa_pass":
            continue
        output_path = row.get("output_path")
        if not output_path:
            continue
        source = PROJECT_ROOT / output_path
        if not source.exists():
            continue
        item = dict(row)
        item["reference_time_sec"] = extract_reference_time(row)
        item["source_path_abs"] = source
        items.append(item)
    return sorted(items, key=lambda item: item["reference_time_sec"])


def verify_r1_outputs(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_item = {row["item_id"]: row for row in rows}
    verified = []
    for item_id, expected in REQUIRED_R1_OUTPUTS.items():
        actual = by_item.get(item_id, {}).get("output_path", "")
        if actual != expected:
            raise SystemExit(
                f"{item_id} is not using R1 output. expected={expected} actual={actual}"
            )
        verified.append({"item_id": item_id, "output_path": actual})
    return verified


def fit_to_1920x824(image: Image.Image) -> Image.Image:
    return image.convert("RGB").resize((1920, 824), Image.Resampling.LANCZOS)


def build_frames(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if FRAMES_DIR.exists():
        for existing in FRAMES_DIR.glob("*.jpg"):
            existing.unlink()
    FRAMES_DIR.mkdir(parents=True, exist_ok=True)
    concat_lines: list[str] = []
    manifest_rows: list[dict[str, Any]] = []

    for index, row in enumerate(rows, start=1):
        source = row["source_path_abs"]
        frame = fit_to_1920x824(Image.open(source))
        frame_path = FRAMES_DIR / f"{index:03d}_{row['item_id']}.jpg"
        frame.save(frame_path, quality=96, subsampling=0, optimize=True)
        next_time = rows[index]["reference_time_sec"] if index < len(rows) else END_TOTAL_SEC
        duration = max(0.1, next_time - row["reference_time_sec"])
        concat_lines.append(f"file '{frame_path.as_posix()}'\n")
        concat_lines.append(f"duration {duration:.6f}\n")
        manifest_rows.append(
            {
                "order": index,
                "item_id": row["item_id"],
                "duration_sec": round(duration, 6),
                "source_path": rel(source),
                "frame_path": rel(frame_path),
            }
        )

    last_frame = FRAMES_DIR / f"{len(rows):03d}_{rows[-1]['item_id']}.jpg"
    concat_lines.append(f"file '{last_frame.as_posix()}'\n")
    CONCAT_PATH.write_text("".join(concat_lines))
    return manifest_rows


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, capture_output=True, text=True)


def encode_video() -> dict[str, Any]:
    command = [
        str(FFMPEG),
        "-y",
        "-safe",
        "0",
        "-f",
        "concat",
        "-i",
        str(CONCAT_PATH),
        "-i",
        str(SOURCE_AUDIO_VIDEO),
        "-map",
        "0:v:0",
        "-map",
        "1:a:0",
        "-vf",
        "fps=24,format=yuv420p,pad=1920:1080:0:128:black",
        "-c:v",
        "mpeg4",
        "-q:v",
        "1",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-shortest",
        "-movflags",
        "+faststart",
        str(OUTPUT_MP4),
    ]
    proc = run(command)
    decode = run([str(FFMPEG), "-v", "error", "-i", str(OUTPUT_MP4), "-f", "null", "-"]) if OUTPUT_MP4.exists() else None
    return {
        "command": command,
        "returncode": proc.returncode,
        "stderr_tail": "\n".join((proc.stderr or "").splitlines()[-16:]),
        "output_path": rel(OUTPUT_MP4),
        "output_exists": OUTPUT_MP4.exists(),
        "output_size_bytes": OUTPUT_MP4.stat().st_size if OUTPUT_MP4.exists() else 0,
        "decode_ok": bool(decode and decode.returncode == 0),
        "decode_stderr_tail": "\n".join((decode.stderr or "").splitlines()[-16:]) if decode else "",
    }


def write_reports(rows: list[dict[str, Any]], r1_outputs: list[dict[str, Any]], encode: dict[str, Any]) -> None:
    report = {
        "schema_version": "reference003_after_identity_repair_r1_preview_manifest",
        "project_slug": "blue-water-citypop-op",
        "created_at": "2026-06-30",
        "status": "decode_ok" if encode["decode_ok"] else "needs_review",
        "boundary": "Preview/workprint assembled from current R1-repaired keyframes. Not final AIGC motion-video rough cut.",
        "output_mp4": encode["output_path"],
        "frame_count": len(rows),
        "r1_outputs_verified": r1_outputs,
        "frames": rows,
        "encode": encode,
    }
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# Reference-003 Preview After Identity Repair R1",
        "",
        f"- Status: `{report['status']}`",
        f"- Output: `{report['output_mp4']}`",
        "- Boundary: preview/workprint only; final AIGC video segments still require external generation.",
        "",
        "## R1 Outputs Verified",
        "",
        "| Item | Output |",
        "|---|---|",
    ]
    for item in r1_outputs:
        lines.append(f"| `{item['item_id']}` | `{item['output_path']}` |")
    REPORT_MD.write_text("\n".join(lines) + "\n")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = load_rows()
    if len(rows) != 42:
        raise SystemExit(f"Expected 42 generated rows, found {len(rows)}")
    r1_outputs = verify_r1_outputs(rows)
    manifest_rows = build_frames(rows)
    encode = encode_video()
    write_reports(manifest_rows, r1_outputs, encode)
    print(
        json.dumps(
            {
                "status": "decode_ok" if encode["decode_ok"] else "needs_review",
                "output_mp4": encode["output_path"],
                "output_size_bytes": encode["output_size_bytes"],
                "frame_count": len(manifest_rows),
                "r1_outputs_verified": r1_outputs,
                "report_json": rel(REPORT_JSON),
                "report_md": rel(REPORT_MD),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if encode["decode_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
