#!/usr/bin/env python3
"""Build Reference-003 identity-locked workprint v2.

This is a clean preview/workprint, not a replacement for final AIGC keyframes.
It applies director feedback by replacing rejected frames with approved proxies:
OP_SHOT_025 uses OP_SHOT_021_v2 as a temporary group proxy, and OP_SHOT_034 uses
OP_SHOT_011_v2 as a Nadia face-lock proxy.
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Any

from PIL import Image, ImageEnhance


PROJECT_ROOT = Path(__file__).resolve().parents[2]
BOARD_PATH = PROJECT_ROOT / "03_story/idea_board/idea_board.json"
SOURCE_AUDIO_VIDEO = PROJECT_ROOT / "01_intake/references/reference-003-full-op-2160p.mp4"
OUT_DIR = PROJECT_ROOT / "09_edit/rough_cut/identity_workprint_v2"
FRAMES_DIR = OUT_DIR / "frames_1920x824_jpg"
CONCAT_PATH = OUT_DIR / "reference003_identity_workprint_v2_concat.txt"
REPORT_JSON = OUT_DIR / "reference003_identity_workprint_v2_manifest.json"
REPORT_MD = OUT_DIR / "reference003_identity_workprint_v2_manifest.md"
OUTPUT_MP4 = (
    PROJECT_ROOT
    / "09_edit/rough_cut/reference003_identity_locked_workprint_v2_1080p_with_music_20260630.mp4"
)
FFMPEG = Path("/Applications/Bitwig Studio.app/Contents/MacOS/ffmpeg")
END_TOTAL_SEC = 84.437333

SUBSTITUTIONS = {
    "OP_SHOT_025": {
        "source_item_id": "OP_SHOT_021",
        "reason": "director rejected OP_SHOT_025 large group portrait; use accepted OP_SHOT_021_v2 as temporary group proxy",
        "kind": "direct_proxy",
    },
    "OP_SHOT_034": {
        "source_item_id": "OP_SHOT_011",
        "reason": "director rejected OP_SHOT_034 blue/sea-background Nadia; use approved OP_SHOT_011_v2 face lock as temporary Nadia proxy",
        "kind": "nadia_blue_mood_proxy",
    },
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


def fit_to_1920x824(image: Image.Image) -> Image.Image:
    return image.convert("RGB").resize((1920, 824), Image.Resampling.LANCZOS)


def make_nadia_blue_proxy(image: Image.Image) -> Image.Image:
    base = fit_to_1920x824(image)
    base = ImageEnhance.Color(base).enhance(0.82)
    base = ImageEnhance.Brightness(base).enhance(0.9)
    base = ImageEnhance.Contrast(base).enhance(1.05)
    blue = Image.new("RGB", base.size, (8, 35, 72))
    return Image.blend(base, blue, 0.22)


def resolve_frame_source(
    row: dict[str, Any],
    by_item_id: dict[str, dict[str, Any]],
) -> tuple[Path, dict[str, str] | None]:
    item_id = row["item_id"]
    substitution = SUBSTITUTIONS.get(item_id)
    if not substitution:
        return row["source_path_abs"], None
    source_row = by_item_id[substitution["source_item_id"]]
    return source_row["source_path_abs"], {
        "item_id": item_id,
        "source_item_id": substitution["source_item_id"],
        "kind": substitution["kind"],
        "reason": substitution["reason"],
        "source_path": rel(source_row["source_path_abs"]),
    }


def build_frames(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    FRAMES_DIR.mkdir(parents=True, exist_ok=True)
    by_item_id = {row["item_id"]: row for row in rows}
    concat_lines: list[str] = []
    manifest_rows: list[dict[str, Any]] = []

    for index, row in enumerate(rows, start=1):
        source, substitution = resolve_frame_source(row, by_item_id)
        image = Image.open(source)
        if substitution and substitution["kind"] == "nadia_blue_mood_proxy":
            frame = make_nadia_blue_proxy(image)
        else:
            frame = fit_to_1920x824(image)

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
                "substitution": substitution,
            }
        )

    concat_lines.append(f"file '{(FRAMES_DIR / f'{len(rows):03d}_{rows[-1]['item_id']}.jpg').as_posix()}'\n")
    CONCAT_PATH.write_text("".join(concat_lines))
    return manifest_rows


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
    proc = subprocess.run(command, capture_output=True, text=True)
    decode = subprocess.run(
        [str(FFMPEG), "-v", "error", "-i", str(OUTPUT_MP4), "-f", "null", "-"],
        capture_output=True,
        text=True,
    ) if OUTPUT_MP4.exists() else None
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
    substitutions = [row["substitution"] for row in rows if row["substitution"]]
    report = {
        "schema_version": "reference003_identity_locked_workprint_v2_manifest",
        "project_slug": "blue-water-citypop-op",
        "created_at": "2026-06-30",
        "status": "decode_ok" if encode["decode_ok"] else "needs_review",
        "boundary": "Preview/workprint only. Substituted frames are proxies, not final AIGC-generated replacement keyframes.",
        "output_mp4": encode["output_path"],
        "frame_count": len(rows),
        "substitutions": substitutions,
        "frames": rows,
        "encode": encode,
    }
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# Reference-003 Identity-Locked Workprint v2",
        "",
        f"- Status: `{report['status']}`",
        f"- Output: `{report['output_mp4']}`",
        "- Boundary: preview/workprint only; substituted frames are proxies, not final AIGC regenerated keyframes.",
        "",
        "## Substitutions",
        "",
        "| Replaced item | Proxy source | Reason |",
        "|---|---|---|",
    ]
    for substitution in substitutions:
        lines.append(
            f"| `{substitution['item_id']}` | `{substitution['source_item_id']}` | {substitution['reason']} |"
        )
    REPORT_MD.write_text("\n".join(lines) + "\n")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = load_rows()
    if len(rows) != 42:
        raise SystemExit(f"Expected 42 generated rows, found {len(rows)}")
    manifest_rows = build_frames(rows)
    encode = encode_video()
    write_reports(manifest_rows, encode)
    print(json.dumps({
        "status": "decode_ok" if encode["decode_ok"] else "needs_review",
        "output_mp4": encode["output_path"],
        "output_size_bytes": encode["output_size_bytes"],
        "substitution_count": sum(1 for row in manifest_rows if row["substitution"]),
        "report_json": rel(REPORT_JSON),
        "report_md": rel(REPORT_MD),
    }, ensure_ascii=False, indent=2))
    return 0 if encode["decode_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

