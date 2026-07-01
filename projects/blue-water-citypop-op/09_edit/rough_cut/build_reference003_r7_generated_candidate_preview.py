#!/usr/bin/env python3
"""Build Reference-003 R7 generated-candidate expanded animatic.

This preview is assembled from:
- 42 official generated keyframes
- 21 R5 adaptive generated assets
- R7 promoted candidate generated assets from the candidate queue

By default this script requires all 98 R7 promoted candidates to have real
generated_output_path values. Use --allow-partial only for an interim workprint.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
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
R7_QUEUE_PATH = (
    PROJECT_ROOT
    / "08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/"
    "reference003_r7_candidate_image_generation_queue.json"
)
SOURCE_AUDIO_VIDEO = PROJECT_ROOT / "01_intake/references/reference-003-full-op-2160p.mp4"
OUT_DIR = PROJECT_ROOT / "09_edit/rough_cut/r7_generated_candidate_preview"
FRAMES_DIR = OUT_DIR / "frames_1920x824_jpg"
CONCAT_PATH = OUT_DIR / "reference003_r7_generated_candidate_preview_concat.txt"
REPORT_JSON = OUT_DIR / "reference003_r7_generated_candidate_preview_manifest.json"
REPORT_MD = OUT_DIR / "reference003_r7_generated_candidate_preview_manifest.md"
OUTPUT_MP4 = (
    PROJECT_ROOT
    / "09_edit/rough_cut/"
    "reference003_r7_generated_candidate_animatic_1080p_with_music_20260701.mp4"
)
FFMPEG_CANDIDATES = [
    Path("/Applications/Bitwig Studio.app/Contents/MacOS/ffmpeg"),
    Path(shutil.which("ffmpeg") or ""),
]
END_TOTAL_SEC = 84.437333
TARGET_W = 1920
TARGET_H = 824
EXPECTED_OFFICIAL = 42
EXPECTED_R5 = 21
EXPECTED_R7 = 98


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
        items.append(
            {
                "item_id": row["item_id"],
                "kind": "official_keyframe",
                "kind_order": 0,
                "reference_time_sec": extract_reference_time(row),
                "source_path_abs": source,
                "source_path": output_path,
                "video_unit_id": row.get("video_unit_id"),
            }
        )
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
        items.append(
            {
                "item_id": row["asset_id"],
                "kind": "r5_adaptive_generated",
                "kind_order": 1,
                "reference_time_sec": float(row["source_time_sec"]),
                "source_path_abs": source,
                "source_path": output_path,
                "video_unit_id": row.get("parent_video_unit_id"),
                "difference_reason": row.get("difference_reason"),
            }
        )
    return items


def load_r7_rows(allow_partial: bool) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    queue = json.loads(R7_QUEUE_PATH.read_text(encoding="utf-8"))
    generated: list[dict[str, Any]] = []
    missing: list[dict[str, Any]] = []
    for row in queue.get("items", []):
        output_path = row.get("generated_output_path")
        if output_path and (PROJECT_ROOT / output_path).exists():
            generated.append(
                {
                    "item_id": row["asset_id"],
                    "kind": "r7_promoted_generated",
                    "kind_order": 2,
                    "priority": row.get("priority"),
                    "reference_time_sec": float(row["source_time_sec"]),
                    "source_timecode": row.get("source_timecode"),
                    "source_path_abs": PROJECT_ROOT / output_path,
                    "source_path": output_path,
                    "video_unit_id": row.get("parent_video_unit_id"),
                    "role": row.get("role"),
                    "difference_reason": row.get("difference_reason"),
                }
            )
        else:
            missing.append(row)
    if missing and not allow_partial:
        first = missing[0]
        raise SystemExit(
            "R7 candidate generation is incomplete: "
            f"{len(generated)}/{EXPECTED_R7} generated. "
            f"Next missing: {first.get('asset_id')} at {first.get('source_timecode')} "
            f"-> {first.get('planned_output_path')}. "
            "Run with --allow-partial only for an interim workprint."
        )
    return generated, missing, queue


def fit_pad_1920x824(image: Image.Image) -> Image.Image:
    image = image.convert("RGB")
    scale = min(TARGET_W / image.width, TARGET_H / image.height)
    new_w = max(1, round(image.width * scale))
    new_h = max(1, round(image.height * scale))
    resized = image.resize((new_w, new_h), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (TARGET_W, TARGET_H), "black")
    canvas.paste(resized, ((TARGET_W - new_w) // 2, (TARGET_H - new_h) // 2))
    return canvas


def build_frames(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    FRAMES_DIR.mkdir(parents=True, exist_ok=True)
    for existing in FRAMES_DIR.glob("*.jpg"):
        existing.unlink()

    concat_lines: list[str] = []
    manifest_rows: list[dict[str, Any]] = []
    for index, row in enumerate(rows, start=1):
        frame = fit_pad_1920x824(Image.open(row["source_path_abs"]))
        safe_id = re.sub(r"[^A-Za-z0-9_]+", "_", row["item_id"])
        frame_path = FRAMES_DIR / f"{index:03d}_{safe_id}.jpg"
        frame.save(frame_path, quality=96, subsampling=0, optimize=True)
        next_time = rows[index]["reference_time_sec"] if index < len(rows) else END_TOTAL_SEC
        duration = max(1 / 24, next_time - row["reference_time_sec"])
        concat_lines.append(f"file '{frame_path.as_posix()}'\n")
        concat_lines.append(f"duration {duration:.6f}\n")
        manifest_rows.append(
            {
                "order": index,
                "item_id": row["item_id"],
                "kind": row["kind"],
                "priority": row.get("priority"),
                "reference_time_sec": round(row["reference_time_sec"], 6),
                "duration_sec": round(duration, 6),
                "source_path": row["source_path"],
                "frame_path": rel(frame_path),
                "video_unit_id": row.get("video_unit_id"),
                "role": row.get("role"),
                "difference_reason": row.get("difference_reason"),
            }
        )

    last = FRAMES_DIR / f"{len(rows):03d}_{re.sub(r'[^A-Za-z0-9_]+', '_', rows[-1]['item_id'])}.jpg"
    concat_lines.append(f"file '{last.as_posix()}'\n")
    CONCAT_PATH.write_text("".join(concat_lines), encoding="utf-8")
    return manifest_rows


def find_ffmpeg() -> Path:
    for candidate in FFMPEG_CANDIDATES:
        if candidate and candidate.exists():
            return candidate
    raise SystemExit("Missing ffmpeg")


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, capture_output=True, text=True)


def encode_video(ffmpeg: Path) -> dict[str, Any]:
    command = [
        str(ffmpeg),
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
        run([str(ffmpeg), "-v", "error", "-i", str(OUTPUT_MP4), "-f", "null", "-"])
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


def write_reports(
    rows: list[dict[str, Any]],
    encode: dict[str, Any],
    queue: dict[str, Any],
    missing_r7: list[dict[str, Any]],
    allow_partial: bool,
) -> None:
    counts = {
        "official_keyframe_count": sum(1 for row in rows if row["kind"] == "official_keyframe"),
        "r5_adaptive_generated_count": sum(1 for row in rows if row["kind"] == "r5_adaptive_generated"),
        "r7_promoted_generated_count": sum(1 for row in rows if row["kind"] == "r7_promoted_generated"),
        "r7_missing_count": len(missing_r7),
    }
    status = "decode_ok"
    if missing_r7:
        status = "partial_decode_ok" if encode["decode_ok"] else "partial_needs_review"
    elif not encode["decode_ok"]:
        status = "needs_review"
    report = {
        "schema_version": "reference003_r7_generated_candidate_preview_manifest_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": dt.datetime.now().replace(microsecond=0).isoformat(),
        "status": status,
        "allow_partial": allow_partial,
        "boundary": "PPT-style expanded keyframe animatic only. Not final external AIGC motion-video rough cut.",
        "output_mp4": encode["output_path"],
        "frame_count": len(rows),
        **counts,
        "queue_status": queue.get("status"),
        "next_missing_r7": (
            {
                "asset_id": missing_r7[0].get("asset_id"),
                "source_timecode": missing_r7[0].get("source_timecode"),
                "planned_output_path": missing_r7[0].get("planned_output_path"),
            }
            if missing_r7
            else None
        ),
        "frames": rows,
        "encode": encode,
    }
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Reference-003 R7 Generated Candidate Preview",
        "",
        f"- Status: `{report['status']}`",
        f"- Output: `{report['output_mp4']}`",
        f"- Frame count: {len(rows)}",
        f"- Official keyframes: {counts['official_keyframe_count']}",
        f"- R5 adaptive generated: {counts['r5_adaptive_generated_count']}",
        f"- R7 promoted generated: {counts['r7_promoted_generated_count']}",
        f"- R7 missing: {counts['r7_missing_count']}",
        "- Boundary: PPT-style keyframe animatic with source audio; final AIGC motion segments still require external generation.",
        "",
    ]
    if missing_r7:
        first = missing_r7[0]
        lines.extend(
            [
                "## Next Missing R7 Candidate",
                "",
                f"- Asset: `{first.get('asset_id')}`",
                f"- Time: `{first.get('source_timecode')}`",
                f"- Planned output: `{first.get('planned_output_path')}`",
                "",
            ]
        )
    lines.extend(["## R7 Assets Included", "", "| Order | Time | Asset | Priority | Video unit |", "|---:|---:|---|---|---|"])
    for row in rows:
        if row["kind"] == "r7_promoted_generated":
            lines.append(
                f"| {row['order']} | {row['reference_time_sec']:.2f}s | `{row['item_id']}` | "
                f"`{row.get('priority') or ''}` | `{row.get('video_unit_id') or ''}` |"
            )
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-partial", action="store_true", help="Build an interim workprint before all R7 candidates are generated.")
    args = parser.parse_args()

    ffmpeg = find_ffmpeg()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    official_rows = load_official_rows()
    r5_rows = load_r5_rows()
    r7_rows, missing_r7, queue = load_r7_rows(args.allow_partial)
    if len(official_rows) != EXPECTED_OFFICIAL:
        raise SystemExit(f"Expected {EXPECTED_OFFICIAL} official keyframes, found {len(official_rows)}")
    if len(r5_rows) != EXPECTED_R5:
        raise SystemExit(f"Expected {EXPECTED_R5} R5 generated assets, found {len(r5_rows)}")
    rows = official_rows + r5_rows + r7_rows
    rows = sorted(rows, key=lambda row: (row["reference_time_sec"], row["kind_order"], row["item_id"]))
    manifest_rows = build_frames(rows)
    encode = encode_video(ffmpeg)
    write_reports(manifest_rows, encode, queue, missing_r7, args.allow_partial)
    print(
        json.dumps(
            {
                "status": "decode_ok" if encode["decode_ok"] else "needs_review",
                "allow_partial": args.allow_partial,
                "output_mp4": encode["output_path"],
                "output_size_bytes": encode["output_size_bytes"],
                "frame_count": len(manifest_rows),
                "official_keyframe_count": len(official_rows),
                "r5_adaptive_generated_count": len(r5_rows),
                "r7_promoted_generated_count": len(r7_rows),
                "r7_missing_count": len(missing_r7),
                "next_missing_r7": missing_r7[0].get("asset_id") if missing_r7 else None,
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
