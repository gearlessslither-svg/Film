#!/usr/bin/env python3
"""Prepare Reference-003 R5 expanded video segment packages.

This script packages the 21 video units for external AIGC video generation using
the current 42 official generated keyframes plus the 21 generated R5 adaptive
frame-promotion assets. It does not generate final AIGC motion-video segments.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PACKET_PATH = (
    PROJECT_ROOT
    / "00_admin/ai_bridge/packets/20260630_reference003_video_segment_execution.json"
)
BOARD_PATH = PROJECT_ROOT / "03_story/idea_board/idea_board.json"
R5_MANIFEST_PATH = (
    PROJECT_ROOT
    / "08_generation/jobs/REFERENCE003_ADAPTIVE_FRAME_PROMOTION_R5_20260630/manifest.json"
)
SOURCE_VIDEO = PROJECT_ROOT / "01_intake/references/reference-003-full-op-2160p.mp4"
SETTING_CHAPTER_PATH = (
    PROJECT_ROOT / "05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md"
)
ASSET_LOCKS_PATH = (
    PROJECT_ROOT / "05_asset_bible/setting_chapters/reference003_asset_locks_v1.json"
)
OUTPUT_ROOT = PROJECT_ROOT / "08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701"
EXPECTED_VIDEO_ROOT = PROJECT_ROOT / "08_generation/outputs/video/reference003_r5_expanded_segments"
REPORT_DIR = PROJECT_ROOT / "10_qa/reports"
FFMPEG = Path("/Applications/Bitwig Studio.app/Contents/MacOS/ffmpeg")


def rel(path: Path | str) -> str:
    path = Path(path)
    if path.is_absolute():
        return str(path.relative_to(PROJECT_ROOT))
    return str(path)


def parse_timecode(value: str) -> float:
    value = value.strip()
    parts = value.split(":")
    if len(parts) == 2:
        return int(parts[0]) * 60 + float(parts[1])
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    raise ValueError(f"Unsupported timecode: {value}")


def timecode_from_seconds(seconds: float) -> str:
    minutes = int(seconds // 60)
    sec = seconds - minutes * 60
    return f"{minutes:02d}:{sec:05.2f}"


def parse_range(time_range: str) -> tuple[float, float]:
    start, end = [part.strip() for part in time_range.split("-", 1)]
    start_sec = parse_timecode(start)
    end_sec = parse_timecode(end)
    if end_sec <= start_sec:
        raise ValueError(f"Invalid time range: {time_range}")
    return start_sec, end_sec


def parse_orders(raw: str, total: int) -> list[int]:
    orders: set[int] = set()
    for chunk in raw.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        if "-" in chunk:
            a, b = [int(part) for part in chunk.split("-", 1)]
            orders.update(range(a, b + 1))
        else:
            orders.add(int(chunk))
    invalid = [order for order in sorted(orders) if order < 1 or order > total]
    if invalid:
        raise ValueError(f"Invalid unit order(s): {invalid}")
    return sorted(orders)


def load_packet() -> dict[str, Any]:
    return json.loads(PACKET_PATH.read_text(encoding="utf-8"))


def load_board_rows() -> dict[str, dict[str, Any]]:
    board = json.loads(BOARD_PATH.read_text(encoding="utf-8"))
    return {row["item_id"]: row for row in board.get("rows", [])}


def load_r5_rows() -> dict[str, list[dict[str, Any]]]:
    manifest = json.loads(R5_MANIFEST_PATH.read_text(encoding="utf-8"))
    by_unit: dict[str, list[dict[str, Any]]] = {}
    for row in manifest.get("items", []):
        if row.get("status") != "generated_pending_director_review":
            continue
        unit_id = row.get("parent_video_unit_id")
        output_path = row.get("output_path") or row.get("planned_output_path")
        if not unit_id or not output_path:
            continue
        source = PROJECT_ROOT / output_path
        if not source.exists():
            continue
        item = {
            "item_id": row["asset_id"],
            "kind": "r5_adaptive_generated",
            "time_sec": float(row["source_time_sec"]),
            "timecode": row.get("source_timecode") or timecode_from_seconds(float(row["source_time_sec"])),
            "role": row.get("keyframe_role", "adaptive_generated_anchor"),
            "beat": row.get("difference_reason", ""),
            "current_output_path": output_path,
            "qa_pass": True,
            "difference_reason": row.get("difference_reason", ""),
            "source_reference_frame": row.get("reference_frame_path", ""),
        }
        by_unit.setdefault(unit_id, []).append(item)
    for items in by_unit.values():
        items.sort(key=lambda item: (item["time_sec"], item["item_id"]))
    return by_unit


def load_asset_locks() -> dict[str, Any]:
    if not ASSET_LOCKS_PATH.exists():
        return {}
    return json.loads(ASSET_LOCKS_PATH.read_text(encoding="utf-8"))


def refresh_units_from_board(units: list[dict[str, Any]]) -> list[dict[str, Any]]:
    board_rows = load_board_rows()
    refreshed = json.loads(json.dumps(units))
    for unit in refreshed:
        blocking: list[str] = []
        unit_id = unit["unit_id"]
        unit["expected_video_job_dir"] = rel(OUTPUT_ROOT / unit_id)
        unit["expected_video_output_path"] = rel(EXPECTED_VIDEO_ROOT / f"{unit_id}.mp4")
        for keyframe in unit.get("keyframes", []):
            board_row = board_rows.get(keyframe["item_id"], {})
            status = board_row.get("status") or keyframe.get("status", "")
            output_path = (
                board_row.get("output_path")
                or keyframe.get("current_output_path")
                or keyframe.get("expected_output_path", "")
            )
            keyframe["kind"] = "official_keyframe"
            keyframe["status"] = status
            keyframe["qa_pass"] = status == "generated_reference003_qa_pass" and bool(output_path)
            keyframe["current_output_path"] = output_path
            keyframe["time_sec"] = parse_timecode(keyframe.get("timecode", "00:00.00"))
            if not keyframe["qa_pass"]:
                blocking.append(keyframe["item_id"])
        if blocking:
            unit["stage_now"] = "blocked_until_keyframes_complete"
            unit["blocking_keyframes"] = blocking
            unit["generation_gate"] = "blocked_until_keyframes_complete"
        else:
            unit["stage_now"] = "ready_for_video_generation"
            unit["blocking_keyframes"] = []
            unit["generation_gate"] = "ready"
    return refreshed


def ordered_unit_anchors(unit: dict[str, Any], r5_by_unit: dict[str, list[dict[str, Any]]]) -> list[dict[str, Any]]:
    anchors: list[dict[str, Any]] = []
    for keyframe in unit.get("keyframes", []):
        anchors.append(
            {
                "item_id": keyframe["item_id"],
                "kind": "official_keyframe",
                "time_sec": keyframe["time_sec"],
                "timecode": keyframe.get("timecode", timecode_from_seconds(keyframe["time_sec"])),
                "role": keyframe.get("role", ""),
                "beat": keyframe.get("beat", ""),
                "current_output_path": keyframe["current_output_path"],
                "qa_pass": keyframe.get("qa_pass", False),
                "difference_reason": "",
                "source_reference_frame": "",
            }
        )
    anchors.extend(r5_by_unit.get(unit["unit_id"], []))
    anchors.sort(key=lambda item: (item["time_sec"], item["kind"] != "official_keyframe", item["item_id"]))
    return anchors


def ffmpeg_extract_clip(unit: dict[str, Any], out_path: Path) -> dict[str, Any]:
    start_sec, end_sec = parse_range(unit["time_range"])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    result = {
        "attempted": False,
        "ok": False,
        "path": rel(out_path),
        "start_sec": round(start_sec, 3),
        "end_sec": round(end_sec, 3),
        "duration_sec": round(end_sec - start_sec, 3),
        "stderr_tail": "",
    }
    if not FFMPEG.exists():
        result["stderr_tail"] = f"ffmpeg not found: {FFMPEG}"
        return result
    if not SOURCE_VIDEO.exists():
        result["stderr_tail"] = f"source video not found: {SOURCE_VIDEO}"
        return result
    result["attempted"] = True
    command = [
        str(FFMPEG),
        "-y",
        "-ss",
        f"{start_sec:.3f}",
        "-i",
        str(SOURCE_VIDEO),
        "-t",
        f"{end_sec - start_sec:.3f}",
        "-an",
        "-c:v",
        "mpeg4",
        "-q:v",
        "3",
        str(out_path),
    ]
    proc = subprocess.run(command, capture_output=True, text=True)
    result["ok"] = proc.returncode == 0 and out_path.exists() and out_path.stat().st_size > 0
    result["stderr_tail"] = "\n".join((proc.stderr or "").splitlines()[-12:])
    return result


def validate_decode(path: Path) -> dict[str, Any]:
    result = {"decode_ok": False, "stderr_tail": ""}
    if not path.exists() or not FFMPEG.exists():
        result["stderr_tail"] = "missing file or ffmpeg"
        return result
    proc = subprocess.run(
        [str(FFMPEG), "-v", "error", "-i", str(path), "-f", "null", "-"],
        capture_output=True,
        text=True,
    )
    result["decode_ok"] = proc.returncode == 0
    result["stderr_tail"] = "\n".join((proc.stderr or "").splitlines()[-12:])
    return result


def read_text(rel_path: str) -> str:
    return (PROJECT_ROOT / rel_path).read_text(encoding="utf-8")


def copy_keyframes(anchors: list[dict[str, Any]], job_dir: Path) -> list[dict[str, Any]]:
    anchors_dir = job_dir / "keyframes"
    if anchors_dir.exists():
        shutil.rmtree(anchors_dir)
    anchors_dir.mkdir(parents=True, exist_ok=True)
    packaged: list[dict[str, Any]] = []
    for index, anchor in enumerate(anchors, start=1):
        src = PROJECT_ROOT / anchor["current_output_path"]
        suffix = src.suffix or ".png"
        safe_id = re.sub(r"[^A-Za-z0-9_]+", "_", anchor["item_id"])
        dst = anchors_dir / f"{index:02d}_{safe_id}{suffix}"
        if src.exists():
            shutil.copy2(src, dst)
        packaged.append(
            {
                "order": index,
                "item_id": anchor["item_id"],
                "kind": anchor["kind"],
                "time_sec": round(anchor["time_sec"], 3),
                "timecode": anchor.get("timecode", ""),
                "role": anchor.get("role", ""),
                "beat": anchor.get("beat", ""),
                "difference_reason": anchor.get("difference_reason", ""),
                "source_reference_frame": anchor.get("source_reference_frame", ""),
                "source_path": anchor["current_output_path"],
                "packaged_path": rel(dst),
                "exists": dst.exists(),
            }
        )
    return packaged


def copy_asset_locks(job_dir: Path, asset_locks: dict[str, Any]) -> list[dict[str, Any]]:
    locks_dir = job_dir / "asset_locks"
    if locks_dir.exists():
        shutil.rmtree(locks_dir)
    locks_dir.mkdir(parents=True, exist_ok=True)
    packaged: list[dict[str, Any]] = []
    for group_name in ("characters", "props_vehicles_symbols"):
        group = asset_locks.get(group_name, {})
        if not isinstance(group, dict):
            continue
        for asset_id, lock in group.items():
            if not isinstance(lock, dict):
                continue
            source_rel = lock.get("lock_path")
            if not source_rel:
                packaged.append(
                    {
                        "group": group_name,
                        "asset_id": asset_id,
                        "status": lock.get("status", ""),
                        "source_path": "",
                        "packaged_path": "",
                        "exists": False,
                    }
                )
                continue
            src = PROJECT_ROOT / source_rel
            suffix = src.suffix or ".png"
            dst = locks_dir / f"{group_name}_{asset_id}{suffix}"
            if src.exists():
                shutil.copy2(src, dst)
            packaged.append(
                {
                    "group": group_name,
                    "asset_id": asset_id,
                    "status": lock.get("status", ""),
                    "source_path": source_rel,
                    "packaged_path": rel(dst),
                    "exists": dst.exists(),
                }
            )
    return packaged


def build_lock_lines(packaged_locks: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    for lock in packaged_locks:
        path = lock.get("packaged_path") or lock.get("source_path") or ""
        if path:
            lines.append(f"- `{lock['asset_id']}` ({lock.get('status', '')}): `{path}`")
        else:
            lines.append(
                f"- `{lock['asset_id']}` ({lock.get('status', '')}): no image lock yet; do not invent a clear new design."
            )
    return "\n".join(lines) if lines else "- No asset lock manifest found."


def build_keyframe_lines(anchors: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    for anchor in anchors:
        label = f"图{anchor['order']}"
        reason = anchor.get("difference_reason") or anchor.get("beat") or ""
        lines.append(
            f"- {label} = `{anchor['item_id']}` ({anchor['kind']}, {anchor.get('timecode', '')}, "
            f"{anchor.get('role', '')}): `{anchor['packaged_path']}`"
        )
        if reason:
            lines.append(f"  - function: {reason}")
    return "\n".join(lines)


def build_transition_lines(unit: dict[str, Any]) -> str:
    lines = []
    for edge in unit.get("transition_edges", []):
        lines.append(
            f"- `{edge.get('edge_id')}`: {edge.get('visual_bridge')} | {edge.get('incoming_instruction', '')}"
        )
    return "\n".join(lines) if lines else "- none"


def build_aigc_prompt(
    unit: dict[str, Any],
    unit_prompt_text: str,
    packaged_locks: list[dict[str, Any]],
    anchors: list[dict[str, Any]],
) -> str:
    official_count = sum(1 for anchor in anchors if anchor["kind"] == "official_keyframe")
    r5_count = sum(1 for anchor in anchors if anchor["kind"] == "r5_adaptive_generated")
    image_limit_note = (
        "If the chosen AIGC site cannot accept all ordered images, keep the first and last anchors, "
        "then prioritize R5 adaptive anchors and turning-point official anchors. Do not reorder the remaining images."
    )
    return f"""# AIGC Video Generation Brief — {unit['unit_id']} — R5 Expanded Package

## Required Inputs

- Reference video clip: `reference_clip/{unit['unit_id']}_reference.mp4`
- Ordered keyframe anchors: {len(anchors)} total = {official_count} official + {r5_count} R5 adaptive generated
{build_keyframe_lines(anchors)}
- Setting chapter: `{rel(SETTING_CHAPTER_PATH)}`
- Asset lock manifest: `{rel(ASSET_LOCKS_PATH)}`
- Packaged identity/asset lock images:
{build_lock_lines(packaged_locks)}
- Expected output path: `{unit['expected_video_output_path']}`

## How To Feed This To The AIGC Video Site

Use the reference clip as the primary timing/camera/motion guide. Use the ordered
keyframe anchors as visual identity, scene, prop, and transition-state locks.
The generated segment should follow the reference clip's motion and duration,
but use the generated keyframes as the remake's visual world.

{image_limit_note}

## Primary Direction

Generate a clean live-action remake segment for `{unit['unit_id']}`. Preserve
the reference-003 OP timing, shot function, screen direction, and edit rhythm.
Replace all readable original text, credits, lyrics, subtitles, broadcaster
marks, logos, and watermarks with clean no-text composition.

Use the setting chapter and packaged asset locks as hard identity, prop,
vehicle, animal, symbol, location, and scene-continuity constraints. The AIGC
model must not redesign visible characters, props, vehicles, or recurring
environments.

## Unit Metadata

- Title: {unit.get('title', '')}
- Time range: `{unit['time_range']}`
- Whitebox required: `{unit.get('whitebox_required', False)}`
- Roughcut slot: `{unit.get('roughcut_slot')}`
- Package type: `reference003_r5_expanded_video_segment`

## Transition Context

{build_transition_lines(unit)}

## Existing Unit Prompt

{unit_prompt_text.strip()}

## R5 Expanded Notes

- This package includes R5 adaptive generated frames when they exist for this unit.
- R5 frames are not raw screenshots; they are generated pure-image assets with output paths.
- Keep the ordered images in timeline order. Do not skip a R5 frame that carries a unique transition, action, prop, or identity state unless the video site image limit forces triage.

## Reject Conditions

- Any readable text, title, credit, lyric, subtitle, NHK/broadcaster mark, logo,
  watermark, or random symbol appears.
- The generated segment ignores the reference clip's timing or screen direction.
- Keyframe anchors are reordered, skipped, or replaced with unrelated imagery.
- Nadia does not match the `OP_SHOT_011_v2` official face lock whenever visible.
- Any visible character face/costume/age identity, prop, vehicle, animal, symbol,
  or recurring scene structure drifts from the packaged locks.
- Minor characters are aged up, sexualized, or dressed immodestly.
- The MP4 cannot complete-decode.
"""


def make_contact_sheet(anchors: list[dict[str, Any]], out_path: Path) -> None:
    if not anchors:
        return
    font = ImageFont.load_default()
    thumb_w = 300
    label_h = 54
    gap = 12
    cols = min(4, max(1, len(anchors)))
    thumbs: list[tuple[dict[str, Any], Image.Image]] = []
    for anchor in anchors:
        img_path = PROJECT_ROOT / anchor["packaged_path"]
        with Image.open(img_path) as img:
            img = img.convert("RGB")
            thumb_h = int(thumb_w * img.height / img.width)
            thumb = img.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        thumbs.append((anchor, thumb))
    max_thumb_h = max(thumb.height for _, thumb in thumbs)
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new(
        "RGB",
        (cols * thumb_w + (cols + 1) * gap, rows * (max_thumb_h + label_h) + (rows + 1) * gap),
        (242, 242, 238),
    )
    draw = ImageDraw.Draw(sheet)
    for idx, (anchor, thumb) in enumerate(thumbs):
        c = idx % cols
        r = idx // cols
        x = gap + c * (thumb_w + gap)
        y = gap + r * (max_thumb_h + label_h + gap)
        sheet.paste(thumb, (x, y))
        label_y = y + max_thumb_h + 5
        draw.text((x + 4, label_y), f"{anchor['order']:02d} {anchor.get('timecode', '')} {anchor['kind']}", fill=(15, 15, 15), font=font)
        draw.text((x + 4, label_y + 24), anchor["item_id"][:44], fill=(60, 60, 60), font=font)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path, quality=92)


def write_qa_checklist(unit: dict[str, Any], qa_path: Path) -> None:
    qa_path.write_text(
        "\n".join(
            [
                f"# Segment QA Checklist — {unit['unit_id']} — R5 Expanded",
                "",
                "- [ ] Reference clip was used for timing/camera/motion.",
                "- [ ] Ordered keyframe anchors were used in listed order.",
                "- [ ] R5 adaptive anchors, if present, were used for their specific transition/action/identity function.",
                "- [ ] Setting chapter and packaged asset locks were used as hard identity/asset constraints.",
                "- [ ] Nadia matches the official `OP_SHOT_011_v2` face lock whenever visible.",
                "- [ ] Character faces, costumes, ages, props, vehicles, animals, symbols, and scene anchors do not drift.",
                "- [ ] Output contains no readable text, logo, subtitles, credits, lyrics, or watermark.",
                "- [ ] Character age/costume safety constraints are preserved.",
                "- [ ] Output MP4 exists at expected path.",
                "- [ ] Output MP4 complete-decodes.",
                "- [ ] Incoming/outgoing transition intent remains compatible.",
                "",
                f"Expected output: `{unit['expected_video_output_path']}`",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def write_job(
    unit: dict[str, Any],
    r5_by_unit: dict[str, list[dict[str, Any]]],
    now: str,
    dry_run: bool,
) -> dict[str, Any]:
    unit_id = unit["unit_id"]
    job_dir = OUTPUT_ROOT / unit_id
    if job_dir.exists() and not dry_run:
        shutil.rmtree(job_dir)
    job_dir.mkdir(parents=True, exist_ok=True)
    (PROJECT_ROOT / unit["expected_video_output_path"]).parent.mkdir(parents=True, exist_ok=True)

    reference_clip = job_dir / "reference_clip" / f"{unit_id}_reference.mp4"
    clip_result = {"attempted": False, "ok": False, "path": rel(reference_clip)}
    if not dry_run:
        clip_result = ffmpeg_extract_clip(unit, reference_clip)
        clip_result.update(validate_decode(reference_clip))

    anchors = ordered_unit_anchors(unit, r5_by_unit)
    packaged_anchors = copy_keyframes(anchors, job_dir)
    ordered_json = job_dir / "ordered_keyframe_anchors.json"
    ordered_json.write_text(json.dumps(packaged_anchors, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    contact_sheet = job_dir / "ordered_keyframe_contact_sheet.jpg"
    make_contact_sheet(packaged_anchors, contact_sheet)

    asset_locks = load_asset_locks()
    packaged_locks = copy_asset_locks(job_dir, asset_locks)
    unit_prompt_text = read_text(unit["video_prompt_path"])
    generation_brief = build_aigc_prompt(unit, unit_prompt_text, packaged_locks, packaged_anchors)
    prompt_path = job_dir / "AIGC_VIDEO_GENERATION_BRIEF.md"
    prompt_path.write_text(generation_brief, encoding="utf-8")

    qa_path = job_dir / "SEGMENT_QA_CHECKLIST.md"
    write_qa_checklist(unit, qa_path)

    r5_count = sum(1 for anchor in packaged_anchors if anchor["kind"] == "r5_adaptive_generated")
    manifest = {
        "schema_version": "reference003_r5_expanded_video_segment_package_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": now,
        "status": "ready_for_external_aigc_video_generation"
        if clip_result.get("decode_ok")
        else "prepared_needs_reference_clip_check",
        "unit": unit,
        "package_root": rel(job_dir),
        "package_type": "reference003_r5_expanded_video_segment",
        "setting_chapter": rel(SETTING_CHAPTER_PATH),
        "asset_lock_manifest": rel(ASSET_LOCKS_PATH),
        "packaged_asset_locks": packaged_locks,
        "reference_video_source": rel(SOURCE_VIDEO),
        "reference_clip": clip_result,
        "keyframe_anchor_count": len(packaged_anchors),
        "official_keyframe_anchor_count": len(packaged_anchors) - r5_count,
        "r5_adaptive_anchor_count": r5_count,
        "keyframe_anchors": packaged_anchors,
        "ordered_keyframe_anchors_json": rel(ordered_json),
        "ordered_keyframe_contact_sheet": rel(contact_sheet),
        "generation_brief": rel(prompt_path),
        "qa_checklist": rel(qa_path),
        "expected_video_output_path": unit["expected_video_output_path"],
        "boundary": "This package prepares inputs only; it does not claim that external AIGC video has been generated.",
    }
    manifest_path = job_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ready = bool(clip_result.get("decode_ok")) and all(anchor["exists"] for anchor in packaged_anchors)
    return {
        "unit_id": unit_id,
        "order": unit["order"],
        "title": unit.get("title", ""),
        "time_range": unit["time_range"],
        "job_dir": rel(job_dir),
        "reference_clip": clip_result,
        "keyframe_anchor_count": len(packaged_anchors),
        "official_keyframe_anchor_count": len(packaged_anchors) - r5_count,
        "r5_adaptive_anchor_count": r5_count,
        "ordered_keyframe_contact_sheet": rel(contact_sheet),
        "generation_brief": rel(prompt_path),
        "qa_checklist": rel(qa_path),
        "manifest": rel(manifest_path),
        "expected_video_output_path": unit["expected_video_output_path"],
        "ready": ready,
    }


def default_batch_label(orders: list[int]) -> str:
    if not orders:
        return "empty"
    contiguous = orders == list(range(orders[0], orders[-1] + 1))
    if contiguous:
        return f"units{orders[0]:02d}_{orders[-1]:02d}"
    return "units_" + "_".join(f"{order:02d}" for order in orders)


def write_batch_report(now: str, jobs: list[dict[str, Any]], orders: list[int], batch_label: str) -> dict[str, Any]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    status = "ready_for_external_aigc_video_generation" if all(job["ready"] for job in jobs) else "needs_review"
    report = {
        "schema_version": "reference003_r5_expanded_video_segment_batch_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": now,
        "status": status,
        "orders": orders,
        "package_root": rel(OUTPUT_ROOT),
        "jobs": jobs,
        "total_jobs": len(jobs),
        "ready_jobs": sum(1 for job in jobs if job["ready"]),
        "total_keyframe_anchors": sum(job["keyframe_anchor_count"] for job in jobs),
        "total_official_keyframe_anchors": sum(job["official_keyframe_anchor_count"] for job in jobs),
        "total_r5_adaptive_anchors": sum(job["r5_adaptive_anchor_count"] for job in jobs),
        "next_action": (
            "Use each job's reference clip, ordered keyframe anchors, and generation brief in a video-capable AIGC tool; "
            "save returned MP4s to expected_video_output_path, then run roughcut/audit scripts."
        ),
    }
    json_path = REPORT_DIR / f"reference003_r5_video_segment_{batch_label}_generation_ready_20260701.json"
    md_path = REPORT_DIR / f"reference003_r5_video_segment_{batch_label}_generation_ready_20260701.md"
    report["report_json"] = rel(json_path)
    report["report_md"] = rel(md_path)
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        f"# Reference-003 R5 Video Segment {batch_label} Generation Ready",
        "",
        f"- Created: `{now}`",
        f"- Status: `{status}`",
        f"- Package root: `{rel(OUTPUT_ROOT)}`",
        f"- Jobs: {report['ready_jobs']}/{report['total_jobs']} ready",
        f"- Anchors: {report['total_keyframe_anchors']} total = {report['total_official_keyframe_anchors']} official + {report['total_r5_adaptive_anchors']} R5 adaptive",
        "",
        "## Jobs",
        "",
        "| # | Unit | Ready | Anchors | R5 | Reference clip | Generation brief | Expected output |",
        "|---:|---|---:|---:|---:|---|---|---|",
    ]
    for job in jobs:
        lines.append(
            f"| {job['order']} | `{job['unit_id']}` | `{job['ready']}` | {job['keyframe_anchor_count']} | "
            f"{job['r5_adaptive_anchor_count']} | `{job['reference_clip']['path']}` | "
            f"`{job['generation_brief']}` | `{job['expected_video_output_path']}` |"
        )
    lines.extend(["", "## Boundary", "", report["next_action"]])
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    root_manifest = {
        "schema_version": "reference003_r5_expanded_video_segments_root_manifest_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": now,
        "status": status,
        "report_json": rel(json_path),
        "report_md": rel(md_path),
        "jobs": jobs,
    }
    (OUTPUT_ROOT / "manifest.json").write_text(json.dumps(root_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--orders", default="1-21", help="Unit orders, e.g. 1-3 or 1,2,5")
    parser.add_argument("--batch-label", default="", help="Stable report label; default derives from --orders")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    now = datetime.now(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()
    packet = load_packet()
    units = refresh_units_from_board(packet["units"])
    r5_by_unit = load_r5_rows()
    orders = parse_orders(args.orders, len(units))
    batch_label = args.batch_label.strip() or default_batch_label(orders)
    selected = [unit for unit in units if unit["order"] in orders]
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    EXPECTED_VIDEO_ROOT.mkdir(parents=True, exist_ok=True)
    jobs = [write_job(unit, r5_by_unit, now, args.dry_run) for unit in selected]
    report = write_batch_report(now, jobs, orders, batch_label)
    print(
        json.dumps(
            {
                "status": report["status"],
                "orders": orders,
                "package_root": report["package_root"],
                "ready_jobs": report["ready_jobs"],
                "total_jobs": report["total_jobs"],
                "total_keyframe_anchors": report["total_keyframe_anchors"],
                "total_r5_adaptive_anchors": report["total_r5_adaptive_anchors"],
                "report_json": report["report_json"],
                "report_md": report["report_md"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if report["status"] == "ready_for_external_aigc_video_generation" else 1


if __name__ == "__main__":
    raise SystemExit(main())
