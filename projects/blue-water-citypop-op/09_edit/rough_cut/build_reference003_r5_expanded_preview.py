#!/usr/bin/env python3
"""Build Reference-003 R5 expanded keyframe animatic.

This preview is assembled from the 42 official generated keyframes plus the
21 R5 generated adaptive frame-promotion assets. It is a PPT-style animatic
with source audio, not final external AIGC motion-video output.
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
R5_MANIFEST_PATH = (
    PROJECT_ROOT
    / "08_generation/jobs/REFERENCE003_ADAPTIVE_FRAME_PROMOTION_R5_20260630/manifest.json"
)
SOURCE_AUDIO_VIDEO = PROJECT_ROOT / "01_intake/references/reference-003-full-op-2160p.mp4"
OUT_DIR = PROJECT_ROOT / "09_edit/rough_cut/r5_expanded_preview"
FRAMES_DIR = OUT_DIR / "frames_1920x824_jpg"
CONCAT_PATH = OUT_DIR / "reference003_r5_expanded_preview_concat.txt"
REPORT_JSON = OUT_DIR / "reference003_r5_expanded_preview_manifest.json"
REPORT_MD = OUT_DIR / "reference003_r5_expanded_preview_manifest.md"
OUTPUT_MP4 = (
    PROJECT_ROOT
    / "09_edit/rough_cut/reference003_r5_expanded_63frame_animatic_1080p_with_music_20260630.mp4"
)
FFMPEG = Path("/Applications/Bitwig Studio.app/Contents/MacOS/ffmpeg")
END_TOTAL_SEC = 84.437333


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


def load_official_rows() -> list[dict[str, Any]]:
    rows = json.loads(BOARD_PATH.read_text(encoding="utf-8"))["rows"]
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
        item = {
            "item_id": row["item_id"],
            "kind": "official_keyframe",
            "reference_time_sec": extract_reference_time(row),
            "source_path_abs": source,
            "source_path": output_path,
            "video_unit_id": row.get("video_unit_id"),
        }
        items.append(item)
    return items


def load_r5_rows() -> list[dict[str, Any]]:
    manifest = json.loads(R5_MANIFEST_PATH.read_text(encoding="utf-8"))
    items: list[dict[str, Any]] = []
    for row in manifest.get("items", []):
        if row.get("status") != "generated_pending_director_review":
            continue
        output_path = row.get("output_path") or row.get("planned_output_path")
        if not output_path:
            continue
        source = PROJECT_ROOT / output_path
        if not source.exists():
            continue
        item = {
            "item_id": row["asset_id"],
            "kind": "r5_adaptive_generated",
            "reference_time_sec": float(row["source_time_sec"]),
            "source_path_abs": source,
            "source_path": output_path,
            "video_unit_id": row.get("parent_video_unit_id"),
            "difference_reason": row.get("difference_reason"),
        }
        items.append(item)
    return items


def fit_to_1920x824(image: Image.Image) -> Image.Image:
    return image.convert("RGB").resize((1920, 824), Image.Resampling.LANCZOS)


def build_frames(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    FRAMES_DIR.mkdir(parents=True, exist_ok=True)
    for existing in FRAMES_DIR.glob("*.jpg"):
        existing.unlink()

    concat_lines: list[str] = []
    manifest_rows: list[dict[str, Any]] = []
    for index, row in enumerate(rows, start=1):
        frame = fit_to_1920x824(Image.open(row["source_path_abs"]))
        safe_id = re.sub(r"[^A-Za-z0-9_]+", "_", row["item_id"])
        frame_path = FRAMES_DIR / f"{index:03d}_{safe_id}.jpg"
        frame.save(frame_path, quality=96, subsampling=0, optimize=True)
        next_time = rows[index]["reference_time_sec"] if index < len(rows) else END_TOTAL_SEC
        duration = max(0.1, next_time - row["reference_time_sec"])
        concat_lines.append(f"file '{frame_path.as_posix()}'\n")
        concat_lines.append(f"duration {duration:.6f}\n")
        manifest_rows.append(
            {
                "order": index,
                "item_id": row["item_id"],
                "kind": row["kind"],
                "reference_time_sec": round(row["reference_time_sec"], 6),
                "duration_sec": round(duration, 6),
                "source_path": row["source_path"],
                "frame_path": rel(frame_path),
                "video_unit_id": row.get("video_unit_id"),
                "difference_reason": row.get("difference_reason"),
            }
        )

    last = FRAMES_DIR / f"{len(rows):03d}_{re.sub(r'[^A-Za-z0-9_]+', '_', rows[-1]['item_id'])}.jpg"
    concat_lines.append(f"file '{last.as_posix()}'\n")
    CONCAT_PATH.write_text("".join(concat_lines), encoding="utf-8")
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
    decode = (
        run([str(FFMPEG), "-v", "error", "-i", str(OUTPUT_MP4), "-f", "null", "-"])
        if OUTPUT_MP4.exists()
        else None
    )
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


def write_reports(rows: list[dict[str, Any]], encode: dict[str, Any]) -> None:
    official_count = sum(1 for row in rows if row["kind"] == "official_keyframe")
    r5_count = sum(1 for row in rows if row["kind"] == "r5_adaptive_generated")
    report = {
        "schema_version": "reference003_r5_expanded_preview_manifest_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": "2026-06-30",
        "status": "decode_ok" if encode["decode_ok"] else "needs_review",
        "boundary": "PPT-style expanded keyframe animatic only. Not final external AIGC motion-video rough cut.",
        "output_mp4": encode["output_path"],
        "frame_count": len(rows),
        "official_keyframe_count": official_count,
        "r5_adaptive_generated_count": r5_count,
        "frames": rows,
        "encode": encode,
    }
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Reference-003 R5 Expanded Preview",
        "",
        f"- Status: `{report['status']}`",
        f"- Output: `{report['output_mp4']}`",
        f"- Frame count: {len(rows)} = {official_count} official + {r5_count} R5 adaptive generated",
        "- Boundary: PPT-style keyframe animatic with source audio; final AIGC motion segments still require external generation.",
        "",
        "## R5 Assets Included",
        "",
        "| Order | Time | Asset | Video unit |",
        "|---:|---:|---|---|",
    ]
    for row in rows:
        if row["kind"] == "r5_adaptive_generated":
            lines.append(
                f"| {row['order']} | {row['reference_time_sec']:.2f}s | `{row['item_id']}` | `{row.get('video_unit_id') or ''}` |"
            )
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    if not FFMPEG.exists():
        raise SystemExit(f"Missing ffmpeg: {FFMPEG}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = load_official_rows() + load_r5_rows()
    rows = sorted(rows, key=lambda row: (row["reference_time_sec"], row["kind"] != "official_keyframe", row["item_id"]))
    official_count = sum(1 for row in rows if row["kind"] == "official_keyframe")
    r5_count = sum(1 for row in rows if row["kind"] == "r5_adaptive_generated")
    if official_count != 42:
        raise SystemExit(f"Expected 42 official keyframes, found {official_count}")
    if r5_count != 21:
        raise SystemExit(f"Expected 21 R5 generated assets, found {r5_count}")
    manifest_rows = build_frames(rows)
    encode = encode_video()
    write_reports(manifest_rows, encode)
    print(
        json.dumps(
            {
                "status": "decode_ok" if encode["decode_ok"] else "needs_review",
                "output_mp4": encode["output_path"],
                "output_size_bytes": encode["output_size_bytes"],
                "frame_count": len(manifest_rows),
                "official_keyframe_count": official_count,
                "r5_adaptive_generated_count": r5_count,
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
