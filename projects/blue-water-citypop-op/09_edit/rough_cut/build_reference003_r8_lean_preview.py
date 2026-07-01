#!/usr/bin/env python3
"""Build Reference-003 R8 lean QA-recovery animatic.

R8 intentionally excludes all R7 generated candidates from the timeline. The
R7 images remain available as a reference pool, but the previous 161-frame
preview proved that automatically inserting every candidate creates timing,
identity, and style failures.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw


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
OUT_DIR = PROJECT_ROOT / "09_edit/rough_cut/r8_lean_preview"
FRAMES_DIR = OUT_DIR / "frames_1920x824_jpg"
CONCAT_PATH = OUT_DIR / "reference003_r8_lean_preview_concat.txt"
REPORT_JSON = OUT_DIR / "reference003_r8_lean_preview_manifest.json"
REPORT_MD = OUT_DIR / "reference003_r8_lean_preview_manifest.md"
CONTACT_SHEET = OUT_DIR / "reference003_r8_lean_preview_contact_sheet.jpg"
R7_SELECTION_JSON = PROJECT_ROOT / "10_qa/reports/reference003_r8_r7_candidate_selection_manifest.json"
R7_SELECTION_MD = PROJECT_ROOT / "10_qa/reports/reference003_r8_r7_candidate_selection_manifest.md"
OUTPUT_MP4 = (
    PROJECT_ROOT
    / "09_edit/rough_cut/"
    "reference003_r8_lean_63frame_animatic_1080p_with_music_20260701.mp4"
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


def write_r7_selection_manifest() -> dict[str, Any]:
    queue = json.loads(R7_QUEUE_PATH.read_text(encoding="utf-8"))
    rows = []
    for item in queue.get("items", []):
        rows.append(
            {
                "asset_id": item.get("asset_id"),
                "unit": item.get("parent_video_unit_id"),
                "unit_title": item.get("unit_title", ""),
                "time_sec": item.get("source_time_sec"),
                "timecode": item.get("source_timecode", ""),
                "role": item.get("role", ""),
                "priority": item.get("priority", ""),
                "generated_output_path": item.get("generated_output_path", ""),
                "r8_status": "reference_only_pending_director_reapproval",
                "r8_reason": "Excluded from R8 lean timeline after director reported timeline weighting, face flicker, and style drift in the 161-frame R7 preview.",
            }
        )
    report = {
        "created_at": dt.datetime.now().replace(microsecond=0).isoformat(),
        "status": "all_r7_candidates_reference_only_pending_reapproval",
        "r7_candidate_count": len(rows),
        "approved_timeline_anchor_count": 0,
        "items": rows,
    }
    R7_SELECTION_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Reference-003 R8 R7 Candidate Selection Manifest",
        "",
        f"- Status: `{report['status']}`",
        f"- R7 candidates: {len(rows)}",
        "- Approved R8 timeline anchors: 0",
        "- Reason: R7 candidate preview failed director QA; all R7 images are reference-only until individually reapproved.",
        "",
        "| Time | Asset | Unit | Role | Priority | R8 status |",
        "|---:|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['timecode']} | `{row['asset_id']}` | `{row['unit']}` | {row['role']} | "
            f"`{row['priority']}` | `{row['r8_status']}` |"
        )
    R7_SELECTION_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


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


def write_contact_sheet(manifest_rows: list[dict[str, Any]]) -> None:
    thumb_w, thumb_h, label_h = 320, 137, 38
    cols = 4
    rows = (len(manifest_rows) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), (24, 24, 24))
    draw = ImageDraw.Draw(sheet)
    for index, row in enumerate(manifest_rows):
        image = Image.open(PROJECT_ROOT / row["frame_path"]).convert("RGB")
        image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x = (index % cols) * thumb_w
        y = (index // cols) * (thumb_h + label_h)
        canvas = Image.new("RGB", (thumb_w, thumb_h), "black")
        canvas.paste(image, ((thumb_w - image.width) // 2, (thumb_h - image.height) // 2))
        sheet.paste(canvas, (x, y))
        label = f"{row['order']:03d} {row['item_id']}"
        draw.text((x + 6, y + thumb_h + 4), label[:44], fill=(235, 235, 235))
    CONTACT_SHEET.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(CONTACT_SHEET, quality=92)


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
    decode = run([str(ffmpeg), "-v", "error", "-i", str(OUTPUT_MP4), "-f", "null", "-"]) if OUTPUT_MP4.exists() else None
    return {
        "returncode": proc.returncode,
        "stderr_tail": "\n".join((proc.stderr or "").splitlines()[-16:]),
        "output_path": rel(OUTPUT_MP4),
        "output_exists": OUTPUT_MP4.exists(),
        "output_size_bytes": OUTPUT_MP4.stat().st_size if OUTPUT_MP4.exists() else 0,
        "decode_ok": bool(decode and decode.returncode == 0),
        "decode_stderr_tail": "\n".join((decode.stderr or "").splitlines()[-16:]) if decode else "",
    }


def write_reports(rows: list[dict[str, Any]], encode: dict[str, Any], r7_selection: dict[str, Any]) -> None:
    status = "qa_recovery_baseline_decode_ok" if encode["decode_ok"] else "qa_recovery_baseline_needs_review"
    report = {
        "schema_version": "reference003_r8_lean_preview_manifest_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": dt.datetime.now().replace(microsecond=0).isoformat(),
        "status": status,
        "boundary": "R8 lean QA-recovery baseline. Uses only official + R5 anchors. R7 generated candidates are reference-only pending reapproval.",
        "output_mp4": encode["output_path"],
        "contact_sheet": rel(CONTACT_SHEET),
        "frame_count": len(rows),
        "official_keyframe_count": sum(1 for row in rows if row["kind"] == "official_keyframe"),
        "r5_adaptive_generated_count": sum(1 for row in rows if row["kind"] == "r5_adaptive_generated"),
        "r7_timeline_anchor_count": 0,
        "r7_reference_only_count": r7_selection["r7_candidate_count"],
        "r7_selection_manifest": rel(R7_SELECTION_JSON),
        "frames": rows,
        "encode": encode,
    }
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Reference-003 R8 Lean Preview",
        "",
        f"- Status: `{status}`",
        f"- Output: `{report['output_mp4']}`",
        f"- Contact sheet: `{report['contact_sheet']}`",
        f"- Frame count: {report['frame_count']}",
        f"- Official keyframes: {report['official_keyframe_count']}",
        f"- R5 adaptive generated: {report['r5_adaptive_generated_count']}",
        "- R7 timeline anchors: 0",
        f"- R7 reference-only candidates: {report['r7_reference_only_count']}",
        f"- R7 selection manifest: `{report['r7_selection_manifest']}`",
        "",
        "## Boundary",
        "",
        "This is a QA-recovery baseline after the 161-frame R7 generated-candidate preview failed director review. It intentionally removes all R7 candidate frames from the timeline to restore timing and style stability before reapproving any R7 anchors.",
        "",
        "## Frames",
        "",
        "| # | Time | Kind | ID | Source |",
        "|---:|---:|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['order']} | {row['reference_time_sec']:.2f}s | `{row['kind']}` | "
            f"`{row['item_id']}` | `{row['source_path']}` |"
        )
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    official_rows = load_official_rows()
    r5_rows = load_r5_rows()
    if len(official_rows) != EXPECTED_OFFICIAL:
        raise SystemExit(f"Expected {EXPECTED_OFFICIAL} official keyframes, found {len(official_rows)}")
    if len(r5_rows) != EXPECTED_R5:
        raise SystemExit(f"Expected {EXPECTED_R5} R5 generated assets, found {len(r5_rows)}")
    r7_selection = write_r7_selection_manifest()
    rows = sorted(official_rows + r5_rows, key=lambda row: (row["reference_time_sec"], row["kind_order"], row["item_id"]))
    manifest_rows = build_frames(rows)
    write_contact_sheet(manifest_rows)
    encode = encode_video(find_ffmpeg())
    write_reports(manifest_rows, encode, r7_selection)
    print(
        json.dumps(
            {
                "status": "decode_ok" if encode["decode_ok"] else "needs_review",
                "output_mp4": rel(OUTPUT_MP4),
                "frame_count": len(manifest_rows),
                "official_keyframe_count": len(official_rows),
                "r5_adaptive_generated_count": len(r5_rows),
                "r7_timeline_anchor_count": 0,
                "r7_reference_only_count": r7_selection["r7_candidate_count"],
                "report_json": rel(REPORT_JSON),
                "report_md": rel(REPORT_MD),
                "contact_sheet": rel(CONTACT_SHEET),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if encode["decode_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
