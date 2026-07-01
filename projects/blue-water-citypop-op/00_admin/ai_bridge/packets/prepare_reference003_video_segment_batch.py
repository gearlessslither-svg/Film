#!/usr/bin/env python3
"""Prepare Reference-003 video segment generation packages.

This script does not generate AIGC video. It packages the inputs required by a
video-capable AIGC tool: source reference clip, QA-pass keyframe anchors, unit
prompt text, expected output path, and QA checklist.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PACKET_PATH = (
    PROJECT_ROOT
    / "00_admin/ai_bridge/packets/20260630_reference003_video_segment_execution.json"
)
BOARD_PATH = PROJECT_ROOT / "03_story/idea_board/idea_board.json"
SOURCE_VIDEO = PROJECT_ROOT / "01_intake/references/reference-003-full-op-2160p.mp4"
SETTING_CHAPTER_PATH = (
    PROJECT_ROOT
    / "05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md"
)
ASSET_LOCKS_PATH = (
    PROJECT_ROOT
    / "05_asset_bible/setting_chapters/reference003_asset_locks_v1.json"
)
OUTPUT_ROOT = PROJECT_ROOT / "08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630"
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


def fmt_seconds(seconds: float) -> str:
    return f"{seconds:.3f}"


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
    return json.loads(PACKET_PATH.read_text())


def load_board_rows() -> dict[str, dict[str, Any]]:
    board = json.loads(BOARD_PATH.read_text())
    return {row["item_id"]: row for row in board.get("rows", [])}


def load_asset_locks() -> dict[str, Any]:
    if not ASSET_LOCKS_PATH.exists():
        return {}
    return json.loads(ASSET_LOCKS_PATH.read_text())


def refresh_units_from_board(units: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Patch stale packet keyframe statuses with current board output paths."""
    board_rows = load_board_rows()
    refreshed = json.loads(json.dumps(units))
    for unit in refreshed:
        blocking: list[str] = []
        for keyframe in unit.get("keyframes", []):
            board_row = board_rows.get(keyframe["item_id"], {})
            status = board_row.get("status") or keyframe.get("status", "")
            output_path = board_row.get("output_path") or keyframe.get("current_output_path") or keyframe.get("expected_output_path", "")
            keyframe["status"] = status
            keyframe["qa_pass"] = status == "generated_reference003_qa_pass" and bool(output_path)
            keyframe["current_output_path"] = output_path
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
        fmt_seconds(start_sec),
        "-i",
        str(SOURCE_VIDEO),
        "-t",
        fmt_seconds(end_sec - start_sec),
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
    return (PROJECT_ROOT / rel_path).read_text()


def copy_keyframes(unit: dict[str, Any], job_dir: Path) -> list[dict[str, Any]]:
    anchors_dir = job_dir / "keyframes"
    anchors_dir.mkdir(parents=True, exist_ok=True)
    anchors: list[dict[str, Any]] = []
    for index, keyframe in enumerate(unit.get("keyframes", []), start=1):
        src = PROJECT_ROOT / keyframe["current_output_path"]
        suffix = src.suffix or ".png"
        dst = anchors_dir / f"{index:02d}_{keyframe['item_id']}{suffix}"
        if src.exists():
            shutil.copy2(src, dst)
        anchors.append(
            {
                "order": index,
                "item_id": keyframe["item_id"],
                "timecode": keyframe.get("timecode", ""),
                "role": keyframe.get("role", ""),
                "beat": keyframe.get("beat", ""),
                "source_path": keyframe["current_output_path"],
                "packaged_path": rel(dst),
                "exists": dst.exists(),
            }
        )
    return anchors


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
            lines.append(
                f"- `{lock['asset_id']}` ({lock.get('status', '')}): `{path}`"
            )
        else:
            lines.append(
                f"- `{lock['asset_id']}` ({lock.get('status', '')}): no image lock yet; do not invent a clear new design."
            )
    return "\n".join(lines) if lines else "- No asset lock manifest found."


def build_aigc_prompt(
    unit: dict[str, Any],
    unit_prompt_text: str,
    packaged_locks: list[dict[str, Any]],
) -> str:
    keyframes = "\n".join(
        f"- {idx}. `{kf['item_id']}` at `{kf.get('timecode', '')}`: {kf.get('beat', '')}; "
        f"anchor image `{kf['current_output_path']}`"
        for idx, kf in enumerate(unit.get("keyframes", []), start=1)
    )
    edges = "\n".join(
        f"- `{edge.get('edge_id')}`: {edge.get('visual_bridge')} | {edge.get('incoming_instruction', '')}"
        for edge in unit.get("transition_edges", [])
    )
    return f"""# AIGC Video Generation Brief — {unit['unit_id']}

## Required Inputs

- Reference video clip: `reference_clip/{unit['unit_id']}_reference.mp4`
- Ordered keyframe anchors:
{keyframes}
- Setting chapter: `{rel(SETTING_CHAPTER_PATH)}`
- Asset lock manifest: `{rel(ASSET_LOCKS_PATH)}`
- Packaged identity/asset lock images:
{build_lock_lines(packaged_locks)}
- Expected output path: `{unit['expected_video_output_path']}`

## Primary Direction

Use the reference video clip as the primary source for timing, camera movement,
screen direction, composition function, and transition rhythm. Use the generated
keyframe anchors as the visual remake identity and start/end/mid-frame anchors.
Use the setting chapter and asset lock images as hard identity, prop, vehicle,
animal, symbol, location, and scene-continuity constraints. The AIGC model must
not redesign visible characters, props, vehicles, or recurring environments.

Generate a clean live-action remake segment for `{unit['unit_id']}`. Preserve
the reference-003 OP motion and duration while replacing all readable original
text, credits, lyrics, subtitles, broadcaster marks, logos, and watermarks with
clean no-text composition.

## Unit Metadata

- Title: {unit.get('title', '')}
- Time range: `{unit['time_range']}`
- Whitebox required: `{unit.get('whitebox_required', False)}`
- Roughcut slot: `{unit.get('roughcut_slot')}`

## Transition Context

{edges or "- none"}

## Existing Unit Prompt

{unit_prompt_text.strip()}

## Reject Conditions

- Any readable text, title, credit, lyric, subtitle, NHK/broadcaster mark, logo,
  watermark, or random symbol appears.
- The generated segment ignores the reference clip's timing or screen direction.
- Keyframe anchors are reordered, skipped, or replaced with unrelated imagery.
- Nadia does not match the `OP_SHOT_011_v2` official face lock.
- Any visible character face/costume/age identity, prop, vehicle, animal, symbol,
  or recurring scene structure drifts from the packaged locks.
- Minor characters are aged up, sexualized, or dressed immodestly.
- The MP4 cannot complete-decode.
"""


def write_job(unit: dict[str, Any], now: str, dry_run: bool) -> dict[str, Any]:
    unit_id = unit["unit_id"]
    job_dir = PROJECT_ROOT / unit["expected_video_job_dir"]
    job_dir.mkdir(parents=True, exist_ok=True)
    (PROJECT_ROOT / unit["expected_video_output_path"]).parent.mkdir(parents=True, exist_ok=True)

    reference_clip = job_dir / "reference_clip" / f"{unit_id}_reference.mp4"
    clip_result = {"attempted": False, "ok": False, "path": rel(reference_clip)}
    if not dry_run:
        clip_result = ffmpeg_extract_clip(unit, reference_clip)
        clip_result.update(validate_decode(reference_clip))

    anchors = copy_keyframes(unit, job_dir)
    asset_locks = load_asset_locks()
    packaged_locks = copy_asset_locks(job_dir, asset_locks)
    unit_prompt_text = read_text(unit["video_prompt_path"])
    generation_brief = build_aigc_prompt(unit, unit_prompt_text, packaged_locks)
    prompt_path = job_dir / "AIGC_VIDEO_GENERATION_BRIEF.md"
    prompt_path.write_text(generation_brief)

    qa_path = job_dir / "SEGMENT_QA_CHECKLIST.md"
    qa_path.write_text(
        "\n".join(
            [
                f"# Segment QA Checklist — {unit_id}",
                "",
                "- [ ] Reference clip was used for timing/camera/motion.",
                "- [ ] Ordered keyframe anchors were used in the listed order.",
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
        + "\n"
    )

    manifest = {
        "schema_version": "reference003_video_segment_generation_job_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": now,
        "status": "ready_for_external_aigc_video_generation"
        if clip_result.get("decode_ok")
        else "prepared_needs_reference_clip_check",
        "unit": unit,
        "setting_chapter": rel(SETTING_CHAPTER_PATH),
        "asset_lock_manifest": rel(ASSET_LOCKS_PATH),
        "packaged_asset_locks": packaged_locks,
        "reference_video_source": rel(SOURCE_VIDEO),
        "reference_clip": clip_result,
        "keyframe_anchors": anchors,
        "generation_brief": rel(prompt_path),
        "qa_checklist": rel(qa_path),
        "expected_video_output_path": unit["expected_video_output_path"],
        "boundary": "This package prepares inputs only; it does not claim that AIGC video has been generated.",
    }
    manifest_path = job_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return {
        "unit_id": unit_id,
        "job_dir": rel(job_dir),
        "reference_clip": clip_result,
        "keyframe_anchors": anchors,
        "generation_brief": rel(prompt_path),
        "qa_checklist": rel(qa_path),
        "expected_video_output_path": unit["expected_video_output_path"],
        "ready": bool(clip_result.get("decode_ok")) and all(anchor["exists"] for anchor in anchors),
    }


def default_batch_label(orders: list[int]) -> str:
    if not orders:
        return "empty"
    contiguous = orders == list(range(orders[0], orders[-1] + 1))
    if contiguous:
        return f"units{orders[0]:02d}_{orders[-1]:02d}"
    return "units_" + "_".join(f"{order:02d}" for order in orders)


def write_batch_report(
    now: str,
    jobs: list[dict[str, Any]],
    orders: list[int],
    batch_label: str,
) -> dict[str, Any]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "schema_version": "reference003_video_segment_generation_batch_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": now,
        "status": "ready_for_external_aigc_video_generation"
        if all(job["ready"] for job in jobs)
        else "needs_review",
        "orders": orders,
        "jobs": jobs,
        "next_action": (
            "Use each job's reference clip, keyframe anchors, and generation brief in a video-capable AIGC tool; "
            "save returned MP4s to expected_video_output_path, then run roughcut/audit scripts."
        ),
    }
    json_path = REPORT_DIR / f"reference003_video_segment_{batch_label}_generation_ready_20260630.json"
    md_path = REPORT_DIR / f"reference003_video_segment_{batch_label}_generation_ready_20260630.md"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")

    lines = [
        f"# Reference-003 Video Segment {batch_label} Generation Ready",
        "",
        f"- Created: `{now}`",
        f"- Status: `{report['status']}`",
        f"- Orders: `{orders}`",
        "",
        "## Jobs",
        "",
        "| Unit | Ready | Reference clip | Generation brief | Expected output |",
        "|---|---:|---|---|---|",
    ]
    for job in jobs:
        lines.append(
            f"| `{job['unit_id']}` | `{job['ready']}` | `{job['reference_clip']['path']}` | "
            f"`{job['generation_brief']}` | `{job['expected_video_output_path']}` |"
        )
    lines.extend(["", "## Boundary", "", report["next_action"]])
    md_path.write_text("\n".join(lines) + "\n")
    report["report_json"] = rel(json_path)
    report["report_md"] = rel(md_path)
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--orders", default="1-3", help="Unit orders, e.g. 1-3 or 1,2,5")
    parser.add_argument("--batch-label", default="", help="Stable report label; default derives from --orders")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    now = datetime.now(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()
    packet = load_packet()
    units = refresh_units_from_board(packet["units"])
    orders = parse_orders(args.orders, len(units))
    batch_label = args.batch_label.strip() or default_batch_label(orders)
    selected = [unit for unit in units if unit["order"] in orders]
    jobs = [write_job(unit, now, args.dry_run) for unit in selected]
    report = write_batch_report(now, jobs, orders, batch_label)
    print(
        json.dumps(
            {
                "status": report["status"],
                "orders": orders,
                "ready_jobs": sum(1 for job in jobs if job["ready"]),
                "total_jobs": len(jobs),
                "report_json": report["report_json"],
                "report_md": report["report_md"],
                "jobs": [
                    {
                        "unit_id": job["unit_id"],
                        "ready": job["ready"],
                        "reference_clip": job["reference_clip"]["path"],
                        "generation_brief": job["generation_brief"],
                        "expected_video_output_path": job["expected_video_output_path"],
                    }
                    for job in jobs
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if report["status"] == "ready_for_external_aigc_video_generation" else 1


if __name__ == "__main__":
    raise SystemExit(main())
