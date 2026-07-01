#!/usr/bin/env python3
"""Rebuild the Reference-003 keyframe status sheet and status animatic.

This is a QA/status helper only. It uses official generated output paths for
rows already marked generated_reference003_qa_pass, and dimmed reference
placeholders for rows that are still pending.
"""

from __future__ import annotations

import csv
import json
import math
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont, ImageOps


PROJECT_ROOT = Path(__file__).resolve().parents[3]
JOB_DIR = Path(__file__).resolve().parent
FRAMES_DIR = JOB_DIR / "animatic_frames"
FRAMES_JPG_DIR = JOB_DIR / "animatic_frames_jpg"
REPORT_DIR = PROJECT_ROOT / "10_qa/reports"
ROUGH_DIR = PROJECT_ROOT / "09_edit/rough_cut"
FFMPEG = Path("/Applications/Bitwig Studio.app/Contents/MacOS/ffmpeg")
END_TOTAL_SEC = 84.437333


def read_json(rel: str) -> Any:
    return json.loads((PROJECT_ROOT / rel).read_text())


def rel(path: Path | str) -> str:
    path = Path(path)
    if path.is_absolute():
        return str(path.relative_to(PROJECT_ROOT))
    return str(path)


def parse_tc(value: str) -> float:
    value = str(value).strip()
    if not value:
        return 0.0
    parts = value.split(":")
    if len(parts) == 2:
        return int(parts[0]) * 60 + float(parts[1])
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    raise ValueError(value)


def fmt_time(seconds: float) -> str:
    minutes = int(seconds // 60)
    sec = seconds - minutes * 60
    return f"{minutes:02d}:{sec:05.2f}"


def load_font(size: int) -> ImageFont.ImageFont:
    for candidate in [
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Unicode.ttf",
    ]:
        if Path(candidate).exists():
            try:
                return ImageFont.truetype(candidate, size=size)
            except OSError:
                pass
    return ImageFont.load_default()


F_MED = load_font(24)
F_SMALL = load_font(17)
F_TINY = load_font(14)


def image_info(image_rel: str) -> dict[str, Any]:
    if not image_rel:
        return {"exists": False, "width": None, "height": None}
    path = PROJECT_ROOT / image_rel
    if not path.exists():
        return {"exists": False, "width": None, "height": None}
    with Image.open(path) as image:
        return {"exists": True, "width": image.width, "height": image.height}


def collect_reference_meta() -> dict[str, dict[str, str]]:
    meta: dict[str, dict[str, str]] = {}
    manifests = sorted(
        (PROJECT_ROOT / "08_generation/jobs").glob(
            "REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630*/manifest.json"
        )
    )
    for manifest_path in manifests:
        data = json.loads(manifest_path.read_text())
        job_id = data.get("job_id", manifest_path.parent.name)
        for item in data.get("items", []):
            item_id = item["item_id"]
            meta[item_id] = {
                "reference_frame": item.get("reference_frame", ""),
                "generation_prompt_file": item.get("prompt_file", ""),
                "label": item.get("label")
                or item.get("title")
                or item.get("description", ""),
                "job_id": job_id,
                "job_status": data.get("status", ""),
            }
    return meta


def collect_rows(now: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    board = read_json("03_story/idea_board/idea_board.json")
    board_rows = {row["item_id"]: row for row in board["rows"]}
    with (PROJECT_ROOT / "07_shots/shot_list.csv").open(newline="") as handle:
        shot_rows = list(csv.DictReader(handle))
    shot_index = {row["shot_id"]: row for row in shot_rows}
    video_units = read_json("07_shots/video_units.json")["units"]
    reference_meta = collect_reference_meta()

    flat = []
    for unit in video_units:
        for keyframe in unit.get("keyframes", []):
            flat.append((unit, keyframe))

    starts = [parse_tc(keyframe.get("timecode", "")) for _, keyframe in flat]
    rows: list[dict[str, Any]] = []
    for index, (unit, keyframe) in enumerate(flat):
        item_id = keyframe["item_id"]
        board_row = board_rows.get(item_id, {})
        shot = shot_index.get(item_id, {})
        status = board_row.get("status") or shot.get("status") or "unknown"
        start = starts[index]
        end = starts[index + 1] if index + 1 < len(starts) else END_TOTAL_SEC
        end = max(start + 0.1, end)
        output_path = (
            board_row.get("output_path", "")
            if status == "generated_reference003_qa_pass"
            else ""
        )
        ref = reference_meta.get(item_id, {})
        ref_path = ref.get("reference_frame", "")
        out_info = image_info(output_path)
        ref_info = image_info(ref_path)
        official = status == "generated_reference003_qa_pass" and out_info["exists"]
        rows.append(
            {
                "order": index + 1,
                "item_id": item_id,
                "timecode": keyframe.get("timecode", ""),
                "start_sec": round(start, 3),
                "end_sec": round(end, 3),
                "duration_sec": round(end - start, 3),
                "video_unit_id": unit["unit_id"],
                "video_unit_title": unit.get("title", ""),
                "keyframe_role": keyframe.get("role", "")
                or shot.get("keyframe_role", ""),
                "beat": board_row.get("beat")
                or keyframe.get("beat", "")
                or shot.get("story_beat", ""),
                "status": status,
                "official_generated": official,
                "current_output_path": output_path,
                "output_exists": out_info["exists"],
                "output_width": out_info["width"],
                "output_height": out_info["height"],
                "reference_frame": ref_path,
                "reference_exists": ref_info["exists"],
                "reference_width": ref_info["width"],
                "reference_height": ref_info["height"],
                "source_for_status_animatic": output_path if official else ref_path,
                "source_kind": "official_generated_keyframe"
                if official
                else "reference_placeholder_pending_generation",
                "job_id": ref.get("job_id", ""),
                "job_status": ref.get("job_status", ""),
                "generation_prompt_file": ref.get("generation_prompt_file", ""),
            }
        )

    summary = {
        "total_keyframes": len(rows),
        "official_generated_keyframes": sum(
            1 for row in rows if row["official_generated"]
        ),
        "pending_keyframes": sum(1 for row in rows if not row["official_generated"]),
        "animatic_reference_duration_sec": END_TOTAL_SEC,
        "missing_generated_outputs_for_passed_rows": [
            row["item_id"]
            for row in rows
            if row["status"] == "generated_reference003_qa_pass"
            and not row["output_exists"]
        ],
        "missing_reference_frames": [
            row["item_id"] for row in rows if not row["reference_exists"]
        ],
    }
    return rows, summary


def fit_to_box(path: Path, box_w: int, box_h: int, bg=(18, 20, 24)) -> Image.Image:
    canvas = Image.new("RGB", (box_w, box_h), bg)
    if not path.exists():
        return canvas
    image = Image.open(path).convert("RGB")
    scale = min(box_w / image.width, box_h / image.height)
    new_size = (max(1, int(image.width * scale)), max(1, int(image.height * scale)))
    image = image.resize(new_size, Image.LANCZOS)
    canvas.paste(image, ((box_w - new_size[0]) // 2, (box_h - new_size[1]) // 2))
    return canvas


def write_inventory(rows: list[dict[str, Any]], now: str, summary: dict[str, Any]) -> None:
    csv_path = JOB_DIR / "reference003_official_keyframe_status_inventory.csv"
    json_path = JOB_DIR / "reference003_official_keyframe_status_inventory.json"
    with csv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    json_path.write_text(
        json.dumps(
            {
                "schema_version": "reference003_official_keyframe_status_inventory_v1",
                "project_slug": "blue-water-citypop-op",
                "created_at": now,
                "status": (
                    "complete_42_pass"
                    if summary["official_generated_keyframes"] == 42
                    else "partial_24_pass_18_pending"
                ),
                "source_reference": "reference-003-full-op-2160p",
                "summary": summary,
                "rows": rows,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n"
    )


def write_status_sheet(rows: list[dict[str, Any]], now: str) -> Path:
    tile_w, tile_h = 360, 270
    image_h = 205
    cols = 7
    rows_n = math.ceil(len(rows) / cols)
    official_count = sum(1 for row in rows if row["official_generated"])
    pending_count = len(rows) - official_count
    sheet = Image.new("RGB", (cols * tile_w, rows_n * tile_h + 80), (12, 14, 18))
    draw = ImageDraw.Draw(sheet, "RGBA")
    draw.rectangle((0, 0, sheet.width, 80), fill=(20, 24, 32, 255))
    draw.text(
        (24, 18),
        "Reference-003 Official Keyframe Status Sheet",
        font=F_MED,
        fill=(255, 255, 255, 245),
    )
    draw.text(
        (24, 48),
        f"{official_count}/42 official QA pass; {pending_count} pending. "
        f"QA/status sheet only, not final picture asset. Created {now}",
        font=F_SMALL,
        fill=(210, 220, 230, 230),
    )
    for index, row in enumerate(rows):
        x = (index % cols) * tile_w
        y = 80 + (index // cols) * tile_h
        bg = (23, 33, 28) if row["official_generated"] else (42, 31, 27)
        draw.rectangle(
            (x + 6, y + 6, x + tile_w - 6, y + tile_h - 6),
            fill=bg + (255,),
            outline=(80, 90, 100, 255),
            width=1,
        )
        source = PROJECT_ROOT / row["source_for_status_animatic"]
        image = fit_to_box(source, tile_w - 18, image_h, bg=(10, 10, 10))
        if not row["official_generated"]:
            image = ImageOps.grayscale(image).convert("RGB")
            overlay = Image.new("RGBA", image.size, (80, 40, 20, 85))
            image = Image.alpha_composite(image.convert("RGBA"), overlay).convert("RGB")
        sheet.paste(image, (x + 9, y + 9))
        label_y = y + image_h + 14
        status = "PASS" if row["official_generated"] else "PENDING"
        status_color = (
            (84, 220, 135, 255)
            if row["official_generated"]
            else (255, 172, 92, 255)
        )
        draw.rectangle((x + 9, y + 9, x + 94, y + 38), fill=(0, 0, 0, 155))
        draw.text((x + 17, y + 15), status, font=F_TINY, fill=status_color)
        draw.text(
            (x + 12, label_y),
            f"{row['order']:02d} {row['item_id']}  {row['timecode']}",
            font=F_SMALL,
            fill=(245, 245, 245, 245),
        )
        draw.text(
            (x + 12, label_y + 22),
            str(row["beat"])[:42],
            font=F_TINY,
            fill=(210, 215, 220, 220),
        )
        draw.text(
            (x + 12, label_y + 42),
            row["video_unit_id"][:42],
            font=F_TINY,
            fill=(170, 185, 200, 220),
        )
    sheet_path = JOB_DIR / "reference003_official_keyframe_status_sheet_42up.jpg"
    sheet.save(sheet_path, quality=92)
    return sheet_path


def write_animatic_frames(rows: list[dict[str, Any]]) -> None:
    width, height = 1280, 720
    FRAMES_DIR.mkdir(exist_ok=True)
    FRAMES_JPG_DIR.mkdir(exist_ok=True)
    for row in rows:
        frame = Image.new("RGB", (width, height), (10, 12, 16))
        source = PROJECT_ROOT / row["source_for_status_animatic"]
        if source.exists():
            image = Image.open(source).convert("RGB")
            if not row["official_generated"]:
                image = ImageOps.grayscale(image).convert("RGB")
                tint = Image.new("RGBA", image.size, (80, 42, 18, 80))
                image = Image.alpha_composite(image.convert("RGBA"), tint).convert("RGB")
            scale = min(width / image.width, (height - 88) / image.height)
            new_size = (
                max(1, int(image.width * scale)),
                max(1, int(image.height * scale)),
            )
            image = image.resize(new_size, Image.LANCZOS)
            frame.paste(
                image,
                ((width - new_size[0]) // 2, 64 + ((height - 88) - new_size[1]) // 2),
            )
        draw = ImageDraw.Draw(frame, "RGBA")
        bar = (12, 42, 25, 218) if row["official_generated"] else (76, 38, 16, 228)
        draw.rectangle((0, 0, width, 64), fill=bar)
        draw.rectangle((0, height - 54, width, height), fill=(0, 0, 0, 180))
        status = (
            "OFFICIAL KEYFRAME QA PASS"
            if row["official_generated"]
            else "PENDING OFFICIAL GENERATION - REFERENCE PLACEHOLDER ONLY"
        )
        draw.text(
            (24, 15),
            f"{row['item_id']}  {row['timecode']} to {fmt_time(row['end_sec'])}"
            f"  |  {status}",
            font=F_MED,
            fill=(255, 255, 255, 245),
        )
        draw.text(
            (24, height - 40),
            f"{row['video_unit_id']} | {row['beat']}",
            font=F_SMALL,
            fill=(230, 235, 240, 235),
        )
        stem = f"{row['order']:03d}_{row['item_id']}"
        frame.save(FRAMES_DIR / f"{stem}.png")
        frame.save(FRAMES_JPG_DIR / f"{stem}.jpg", quality=92)


def encode_animatic(rows: list[dict[str, Any]]) -> dict[str, Any]:
    ROUGH_DIR.mkdir(parents=True, exist_ok=True)
    concat_path = JOB_DIR / "reference003_keyframe_status_animatic_concat_jpg.txt"
    with concat_path.open("w") as handle:
        for row in rows:
            frame = FRAMES_JPG_DIR / f"{row['order']:03d}_{row['item_id']}.jpg"
            handle.write(f"file '{frame.as_posix()}'\n")
            handle.write(f"duration {float(row['duration_sec']):.3f}\n")
        last = rows[-1]
        frame = FRAMES_JPG_DIR / f"{last['order']:03d}_{last['item_id']}.jpg"
        handle.write(f"file '{frame.as_posix()}'\n")

    out = ROUGH_DIR / "reference003_keyframe_status_animatic_20260630.mp4"
    result = {
        "attempted": False,
        "ok": False,
        "decode_ok": False,
        "stderr_tail": "",
        "duration_line": "",
        "encoder": "Bitwig ffmpeg, concat JPEG frames, mpeg4 video",
    }
    if not FFMPEG.exists():
        result["stderr_tail"] = f"ffmpeg not found: {FFMPEG}"
        return result
    result["attempted"] = True
    command = [
        str(FFMPEG),
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(concat_path),
        "-vf",
        "fps=12,format=yuv420p",
        "-c:v",
        "mpeg4",
        str(out),
    ]
    proc = subprocess.run(command, capture_output=True, text=True)
    result["ok"] = proc.returncode == 0 and out.exists()
    result["stderr_tail"] = "\n".join((proc.stderr or "").splitlines()[-12:])
    if result["ok"]:
        dec = subprocess.run(
            [str(FFMPEG), "-v", "error", "-i", str(out), "-f", "null", "-"],
            capture_output=True,
            text=True,
        )
        result["decode_ok"] = dec.returncode == 0
        info = subprocess.run(
            [str(FFMPEG), "-hide_banner", "-i", str(out)],
            capture_output=True,
            text=True,
        )
        for line in (info.stderr or info.stdout or "").splitlines():
            if "Duration:" in line:
                result["duration_line"] = line.strip()
                break
    return result


def write_reports(
    now: str,
    rows: list[dict[str, Any]],
    summary: dict[str, Any],
    sheet_path: Path,
    encode: dict[str, Any],
) -> None:
    status = (
        "complete_status_previs_built"
        if summary["official_generated_keyframes"] == 42 and encode["decode_ok"]
        else "partial_status_previs_built"
    )
    manifest = {
        "schema_version": "reference003_keyframe_status_previs_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": now,
        "status": status,
        "source_reference": "reference-003-full-op-2160p",
        "purpose": (
            "QA/status overview only. It is not a final generated OP segment and "
            "pending frames are reference placeholders."
        ),
        "counts": {
            "total_keyframes": summary["total_keyframes"],
            "official_generated_keyframes": summary["official_generated_keyframes"],
            "pending_keyframes": summary["pending_keyframes"],
            "animatic_reference_duration_sec": END_TOTAL_SEC,
        },
        "outputs": {
            "inventory_csv": rel(JOB_DIR / "reference003_official_keyframe_status_inventory.csv"),
            "inventory_json": rel(JOB_DIR / "reference003_official_keyframe_status_inventory.json"),
            "status_sheet": rel(sheet_path),
            "animatic_concat": rel(JOB_DIR / "reference003_keyframe_status_animatic_concat_jpg.txt"),
            "animatic_frames_dir": rel(FRAMES_DIR),
            "animatic_frames_jpg_dir": rel(FRAMES_JPG_DIR),
            "status_animatic_mp4": rel(
                ROUGH_DIR / "reference003_keyframe_status_animatic_20260630.mp4"
            )
            if encode["ok"]
            else "",
            "rebuild_script": rel(Path(__file__)),
        },
        "encode_validation": encode,
        "next_gate": (
            "Generate OP_SHOT_025-042 in a fresh window, then rerun this script so "
            "all 42 frames are official_generated_keyframe."
        )
        if summary["official_generated_keyframes"] < 42
        else "Proceed to 21 VU_REF003 video unit generation and roughcut QA.",
    }
    (JOB_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    )
    (REPORT_DIR / "reference003_keyframe_status_previs_20260630.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    )

    md = [
        "# Reference-003 Keyframe Status Previs",
        "",
        f"- Created: `{now}`",
        "- Scope: QA/status overview only; not final OP video and not official shot output.",
        "- Source reference: `reference-003-full-op-2160p`",
        "",
        "## Result",
        "",
        f"- Official generated keyframes: {summary['official_generated_keyframes']}/42",
        f"- Pending official keyframes: {summary['pending_keyframes']}/42",
        f"- Status sheet: `{manifest['outputs']['status_sheet']}`",
    ]
    if encode["ok"]:
        md.extend(
            [
                f"- QA status animatic MP4: `{manifest['outputs']['status_animatic_mp4']}`",
                f"- MP4 decode validation: `{encode['decode_ok']}`",
            ]
        )
        if encode["duration_line"]:
            md.append(f"- MP4 duration probe: `{encode['duration_line']}`")
    else:
        md.append("- QA status animatic MP4: not encoded; inspect `manifest.json`.")
    md.extend(
        [
            "",
            "## Important Boundary",
            "",
            "Pending frames in the status animatic use dimmed reference placeholders. "
            "They are not generated remake assets and must be replaced by official "
            "`generated_reference003_qa_pass` outputs before video generation.",
            "",
            "## Files",
            "",
        ]
    )
    for key, value in manifest["outputs"].items():
        if value:
            md.append(f"- `{key}`: `{value}`")
    (REPORT_DIR / "reference003_keyframe_status_previs_20260630.md").write_text(
        "\n".join(md) + "\n"
    )


def main() -> int:
    now = datetime.now(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    rows, summary = collect_rows(now)
    write_inventory(rows, now, summary)
    sheet_path = write_status_sheet(rows, now)
    write_animatic_frames(rows)
    encode = encode_animatic(rows)
    write_reports(now, rows, summary, sheet_path, encode)
    print(
        json.dumps(
            {
                "status": "ok" if encode["decode_ok"] else "needs_review",
                "official_generated_keyframes": summary["official_generated_keyframes"],
                "pending_keyframes": summary["pending_keyframes"],
                "status_sheet": rel(sheet_path),
                "status_animatic_mp4": rel(
                    ROUGH_DIR / "reference003_keyframe_status_animatic_20260630.mp4"
                )
                if encode["ok"]
                else "",
                "decode_ok": encode["decode_ok"],
                "duration_line": encode["duration_line"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if encode["decode_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
