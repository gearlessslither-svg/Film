#!/usr/bin/env python3
"""Rebuild Reference-003 video unit readiness from current project state."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[3]
JOB_DIR = Path(__file__).resolve().parent
REPORT_DIR = PROJECT_ROOT / "10_qa/reports"


def read_json(rel_path: str) -> Any:
    return json.loads((PROJECT_ROOT / rel_path).read_text())


def rel(path: Path | str) -> str:
    path = Path(path)
    if path.is_absolute():
        return str(path.relative_to(PROJECT_ROOT))
    return str(path)


def read_shot_list() -> dict[str, dict[str, str]]:
    with (PROJECT_ROOT / "07_shots/shot_list.csv").open(newline="") as handle:
        return {row["shot_id"]: row for row in csv.DictReader(handle)}


def collect_pending_generation_meta() -> dict[str, dict[str, str]]:
    meta: dict[str, dict[str, str]] = {}
    for manifest_path in sorted(
        (PROJECT_ROOT / "08_generation/jobs").glob(
            "REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH*_READY/manifest.json"
        )
    ):
        data = json.loads(manifest_path.read_text())
        job_id = data.get("job_id", manifest_path.parent.name)
        for item in data.get("items", []):
            item_id = item["item_id"]
            meta[item_id] = {
                "ready_job_id": job_id,
                "ready_manifest_path": rel(manifest_path),
                "reference_frame": item.get("reference_frame", ""),
                "generation_prompt_file": item.get("prompt_file", ""),
                "expected_output_path": f"08_generation/jobs/{job_id}/outputs/{item_id}.png",
                "label": item.get("label")
                or item.get("title")
                or item.get("description", ""),
            }
    return meta


def collect_rows(now: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    video_units = read_json("07_shots/video_units.json")["units"]
    edges = read_json("07_shots/transition_edges.json")["edges"]
    board = read_json("03_story/idea_board/idea_board.json")
    board_rows = {row["item_id"]: row for row in board["rows"]}
    shot_index = read_shot_list()
    pending_meta = collect_pending_generation_meta()

    status_counts: dict[str, int] = {}
    for row in board["rows"]:
        status = row.get("status", "unknown")
        status_counts[status] = status_counts.get(status, 0) + 1

    def keyframe_status(item_id: str, unit: dict[str, Any], kf: dict[str, Any]) -> dict[str, Any]:
        board_row = board_rows.get(item_id, {})
        shot = shot_index.get(item_id, {})
        pending = pending_meta.get(item_id, {})
        status = board_row.get("status") or shot.get("status") or "unknown"
        output_path = (
            board_row.get("output_path", "")
            if status == "generated_reference003_qa_pass"
            else ""
        )
        output_exists = bool(output_path) and (PROJECT_ROOT / output_path).exists()
        qa_pass = status == "generated_reference003_qa_pass" and output_exists
        return {
            "item_id": item_id,
            "status": status,
            "qa_pass": qa_pass,
            "current_output_path": output_path,
            "output_exists": output_exists,
            "expected_output_path": output_path
            or pending.get("expected_output_path")
            or f"08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/keyframe_placeholders/{item_id}.png",
            "shot_prompt_path": shot.get("prompt_path") or f"07_shots/prompts/{item_id}.md",
            "shot_video_prompt_path": f"07_shots/video_prompts/{item_id}.md",
            "unit_prompt_path": shot.get("unit_prompt_path") or f"07_shots/video_prompts_by_unit/{unit['unit_id']}.md",
            "reference_frame": pending.get("reference_frame", ""),
            "ready_job_id": pending.get("ready_job_id", ""),
            "generation_prompt_file": pending.get("generation_prompt_file", ""),
            "timecode": kf.get("timecode", ""),
            "beat": board_row.get("beat") or shot.get("story_beat") or kf.get("beat", ""),
            "role": shot.get("keyframe_role") or kf.get("role", ""),
        }

    units: list[dict[str, Any]] = []
    for index, unit in enumerate(video_units, 1):
        keyframes = [
            keyframe_status(kf["item_id"], unit, kf)
            for kf in unit.get("keyframes", [])
        ]
        blocking = [kf["item_id"] for kf in keyframes if not kf["qa_pass"]]
        ready = bool(keyframes) and not blocking
        units.append(
            {
                "order": index,
                "unit_id": unit["unit_id"],
                "title": unit.get("title", ""),
                "time_range": unit.get("time_range", ""),
                "unit_type": unit.get("unit_type", ""),
                "stage": "ready_for_video_generation"
                if ready
                else "blocked_until_keyframes_complete",
                "blocking_keyframes": blocking,
                "video_prompt_path": f"07_shots/video_prompts_by_unit/{unit['unit_id']}.md",
                "expected_video_output_path": f"08_generation/outputs/video/reference003_segments/{unit['unit_id']}.mp4",
                "expected_video_job_dir": f"08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/{unit['unit_id']}",
                "roughcut_slot": index,
                "whitebox_required": bool(unit.get("whitebox_required")),
                "keyframes": keyframes,
                "incoming_edges": unit.get("incoming_edges", []),
                "outgoing_edges": unit.get("outgoing_edges", []),
                "intra_unit_edges": unit.get("intra_unit_edges", []),
                "qa_focus": [
                    "preserve reference-003 timing and composition function",
                    "keep remake clean: no readable text, logo, subtitles, watermark, or random symbols",
                    "use only reference-003 QA-passed keyframes as visual anchors",
                    "preserve unit order and transition edges",
                    "keep Nadia and all minors age-appropriate and non-sexualized whenever visible",
                ],
                "blocker_summary": ", ".join(blocking),
            }
        )

    summary = {
        "video_units_total": len(units),
        "video_units_ready_for_generation": sum(
            1 for unit in units if unit["stage"] == "ready_for_video_generation"
        ),
        "video_units_blocked_until_keyframes_complete": sum(
            1
            for unit in units
            if unit["stage"] == "blocked_until_keyframes_complete"
        ),
        "keyframes_total": len(board["rows"]),
        "keyframes_generated_reference003_qa_pass": status_counts.get(
            "generated_reference003_qa_pass", 0
        ),
        "keyframes_prompt_ready_reference003": status_counts.get(
            "prompt_ready_reference003", 0
        ),
        "transition_edges_total": len(edges),
        "missing_outputs_for_passed_keyframes": [
            kf["item_id"]
            for unit in units
            for kf in unit["keyframes"]
            if kf["status"] == "generated_reference003_qa_pass"
            and not kf["output_exists"]
        ],
    }
    return units, summary


def write_outputs(now: str, units: list[dict[str, Any]], summary: dict[str, Any]) -> dict[str, Any]:
    status = (
        "all_video_units_ready_for_generation"
        if summary["video_units_ready_for_generation"] == summary["video_units_total"]
        and not summary["missing_outputs_for_passed_keyframes"]
        else "partial_ready_waiting_for_remaining_keyframes"
    )
    manifest = {
        "schema_version": "reference003_video_unit_readiness_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": now,
        "source_reference": "reference-003-full-op-2160p",
        "source_video_project_copy": "01_intake/references/reference-003-full-op-2160p.mp4",
        "status": status,
        "relay_note": "This package is readiness prep only; image/video generation should run from a fresh window when needed.",
        "summary": summary,
        "hard_gates_before_video_generation": [
            "All 42 OP_SHOT keyframes must be generated_reference003_qa_pass and have existing output files before full unit generation starts.",
            "Do not use superseded reference-002 assets or OP_KEYFRAMES_20260629_REMAKE_V3 pending output paths as official anchors.",
            "Use reference-003-full-op-2160p timing and section contact sheets for unit QA.",
            "Keep all text/logo/title/credit/subtitle areas clean in generated video.",
        ],
        "units": units,
        "rebuild_script": rel(Path(__file__)),
    }
    (JOB_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    )
    (REPORT_DIR / "reference003_video_unit_generation_ready_20260630.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    )

    with (JOB_DIR / "video_unit_readiness.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "order",
                "unit_id",
                "time_range",
                "title",
                "stage",
                "keyframes",
                "blocking_keyframes",
                "expected_video_output_path",
            ],
        )
        writer.writeheader()
        for unit in units:
            writer.writerow(
                {
                    "order": unit["order"],
                    "unit_id": unit["unit_id"],
                    "time_range": unit["time_range"],
                    "title": unit["title"],
                    "stage": unit["stage"],
                    "keyframes": " ".join(kf["item_id"] for kf in unit["keyframes"]),
                    "blocking_keyframes": " ".join(unit["blocking_keyframes"]),
                    "expected_video_output_path": unit["expected_video_output_path"],
                }
            )

    md = [
        "# Reference-003 Video Unit Generation Readiness",
        "",
        f"- Project: `blue-water-citypop-op`",
        f"- Rebuilt: `{now}`",
        "- Source reference: `reference-003-full-op-2160p`",
        "- Purpose: prepare and verify the video-stage handoff after keyframes.",
        "",
        "## Current Gate",
        "",
        f"- Keyframes: {summary['keyframes_generated_reference003_qa_pass']}/42 official reference-003 QA pass; {summary['keyframes_prompt_ready_reference003']} still prompt-ready.",
        f"- Video units: {summary['video_units_ready_for_generation']}/21 have all required keyframes QA-passed; {summary['video_units_blocked_until_keyframes_complete']}/21 are blocked until remaining keyframes finish.",
        f"- Transition edges: {summary['transition_edges_total']} declared and must be preserved in order.",
        "",
        "Do not start full video generation until all 42 keyframes are `generated_reference003_qa_pass` and this script reports 21/21 units ready.",
        "",
        "## Unit Readiness",
        "",
        "| # | Unit | Time | Status | Keyframes | Blockers |",
        "|---:|---|---|---|---|---|",
    ]
    for unit in units:
        keyframes = ", ".join(kf["item_id"] for kf in unit["keyframes"])
        blockers = ", ".join(unit["blocking_keyframes"]) or "-"
        md.append(
            f"| {unit['order']} | `{unit['unit_id']}` | {unit['time_range']} | `{unit['stage']}` | {keyframes} | {blockers} |"
        )
    md.extend(
        [
            "",
            "## Rebuild Command",
            "",
            "`python3 08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/rebuild_reference003_video_unit_readiness.py`",
            "",
            "## Files",
            "",
            "- Machine manifest: `08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/manifest.json`",
            "- Scan table: `08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/video_unit_readiness.csv`",
            "- QA checklist: `08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/qa/VIDEO_UNIT_QA_CHECKLIST.md`",
            "- Rebuild script: `08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/rebuild_reference003_video_unit_readiness.py`",
        ]
    )
    (JOB_DIR / "README.md").write_text("\n".join(md) + "\n")
    (REPORT_DIR / "reference003_video_unit_generation_ready_20260630.md").write_text(
        "\n".join(md) + "\n"
    )
    return manifest


def main() -> int:
    now = datetime.now(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    units, summary = collect_rows(now)
    manifest = write_outputs(now, units, summary)
    print(
        json.dumps(
            {
                "status": manifest["status"],
                "summary": manifest["summary"],
                "manifest": rel(JOB_DIR / "manifest.json"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
