#!/usr/bin/env python3
"""Rebuild the Reference-003 completion audit from current evidence."""

from __future__ import annotations

import csv
import json
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
REPORT_DIR = PROJECT_ROOT / "10_qa/reports"
PROJECT_VALIDATOR = Path("/Users/jaychoupp/Story/Film/scripts/validate_aigc_project.py")
SOURCE_VIDEO = PROJECT_ROOT / "01_intake/references/reference-003-full-op-2160p.mp4"


def read_json(rel_path: str) -> Any:
    return json.loads((PROJECT_ROOT / rel_path).read_text())


def rel(path: Path | str) -> str:
    path = Path(path)
    if path.is_absolute():
        return str(path.relative_to(PROJECT_ROOT))
    return str(path)


def run_project_validation() -> dict[str, Any]:
    proc = subprocess.run(
        ["python3", str(PROJECT_VALIDATOR), str(PROJECT_ROOT)],
        capture_output=True,
        text=True,
    )
    output = (proc.stdout or "") + (proc.stderr or "")
    return {
        "command": f"python3 {PROJECT_VALIDATOR} {PROJECT_ROOT}",
        "returncode": proc.returncode,
        "project_status_pass": "project_status=pass" in output,
        "output": output.strip(),
    }


def board_status() -> dict[str, Any]:
    board = read_json("03_story/idea_board/idea_board.json")
    counts: dict[str, int] = {}
    missing_outputs: list[str] = []
    for row in board["rows"]:
        status = row.get("status", "unknown")
        counts[status] = counts.get(status, 0) + 1
        output = row.get("output_path", "")
        if status == "generated_reference003_qa_pass":
            if not output or not (PROJECT_ROOT / output).exists():
                missing_outputs.append(row["item_id"])
    with (PROJECT_ROOT / "07_shots/shot_list.csv").open(newline="") as handle:
        shot_rows = list(csv.DictReader(handle))
    shot_counts: dict[str, int] = {}
    for row in shot_rows:
        status = row.get("status", "unknown")
        shot_counts[status] = shot_counts.get(status, 0) + 1
    return {
        "board_rows": len(board["rows"]),
        "board_status_counts": counts,
        "shot_list_rows": len(shot_rows),
        "shot_list_status_counts": shot_counts,
        "missing_outputs_for_passed_keyframes": missing_outputs,
        "all_42_keyframes_pass": counts.get("generated_reference003_qa_pass", 0) == 42
        and not missing_outputs
        and shot_counts.get("generated_reference003_qa_pass", 0) == 42,
    }


def load_optional_json(rel_path: str) -> dict[str, Any]:
    path = PROJECT_ROOT / rel_path
    if not path.exists():
        return {"missing": True}
    return json.loads(path.read_text())


def gate(name: str, expected: str, passed: bool, evidence: str, current: str) -> dict[str, Any]:
    return {
        "gate": name,
        "expected": expected,
        "status": "pass" if passed else "pending",
        "current": current,
        "evidence": evidence,
    }


def build_audit(now: str) -> dict[str, Any]:
    validation = run_project_validation()
    board = board_status()
    keyframe_status = load_optional_json(
        "10_qa/reference_match/REFERENCE003_OFFICIAL_KEYFRAME_STATUS_20260630/manifest.json"
    )
    video_unit = load_optional_json(
        "08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/manifest.json"
    )
    video_segment = load_optional_json(
        "00_admin/ai_bridge/packets/20260630_reference003_video_segment_execution.json"
    )
    roughcut = load_optional_json(
        "09_edit/rough_cut/reference003_roughcut_transition_audit_template.json"
    )
    safety_review = load_optional_json(
        "10_qa/reports/reference003_no_text_logo_safety_review_20260630.json"
    )

    keyframe_counts = keyframe_status.get("counts", {})
    video_summary = video_unit.get("summary", {})
    rough_summary = roughcut.get("summary", {})
    safety_summary = safety_review.get("summary", {})

    source_ingested = SOURCE_VIDEO.exists()
    project_pass = validation["project_status_pass"]
    keyframes_pass = board["all_42_keyframes_pass"]
    keyframe_previs_decode = keyframe_status.get("encode_validation", {}).get("decode_ok") is True
    video_stage_prepared = video_segment.get("schema_version") == "reference003_video_segment_execution_v1"
    video_units_ready = (
        video_summary.get("video_units_ready_for_generation") == 21
        and video_summary.get("video_units_blocked_until_keyframes_complete") == 0
    )
    video_segments_pass = rough_summary.get("segments_decode_pass") == 21
    transitions_reviewed = rough_summary.get("transition_edges_reviewed") == 41
    roughcut_decode = rough_summary.get("roughcut_decode_ok") is True
    duration_match = rough_summary.get("roughcut_duration_match_within_1s") is True
    text_logo_review = safety_summary.get("completion_gate_pass") is True

    gates = [
        gate(
            "source_video_ingested",
            "reference-003-full-op-2160p copied into project",
            source_ingested,
            rel(SOURCE_VIDEO),
            "pass" if source_ingested else "missing",
        ),
        gate(
            "project_validation",
            "validate_aigc_project.py returns project_status=pass",
            project_pass,
            validation["command"],
            "pass" if project_pass else "fail",
        ),
        gate(
            "keyframes_42_qa_pass",
            "42/42 board and shot_list rows are generated_reference003_qa_pass and output files exist",
            keyframes_pass,
            "03_story/idea_board/idea_board.json + 07_shots/shot_list.csv",
            f"board={board['board_status_counts']}; shot_list={board['shot_list_status_counts']}; missing={board['missing_outputs_for_passed_keyframes']}",
        ),
        gate(
            "keyframe_status_previs",
            "keyframe status manifest exists and status MP4 decodes",
            keyframe_previs_decode,
            "10_qa/reference_match/REFERENCE003_OFFICIAL_KEYFRAME_STATUS_20260630/manifest.json",
            f"{keyframe_counts.get('official_generated_keyframes', 0)}/42 official; decode={keyframe_previs_decode}",
        ),
        gate(
            "video_stage_execution_prepared",
            "video segment execution packet exists",
            video_stage_prepared,
            "00_admin/ai_bridge/packets/20260630_reference003_video_segment_execution.json",
            video_segment.get("status", "missing"),
        ),
        gate(
            "video_units_21_ready",
            "21/21 video units are ready after keyframes complete",
            video_units_ready,
            "08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/manifest.json",
            f"{video_summary.get('video_units_ready_for_generation', 0)}/21 ready; {video_summary.get('video_units_blocked_until_keyframes_complete', 0)} blocked",
        ),
        gate(
            "video_units_21_generated",
            "21/21 VU_REF003 segment MP4s exist and decode",
            video_segments_pass,
            "09_edit/rough_cut/reference003_roughcut_transition_audit_template.json",
            f"{rough_summary.get('segments_decode_pass', 0)}/21 decode pass",
        ),
        gate(
            "transition_edges_41_reviewed",
            "41/41 transition edges reviewed",
            transitions_reviewed,
            "09_edit/rough_cut/reference003_roughcut_transition_audit_template.json",
            f"{rough_summary.get('transition_edges_reviewed', 0)}/41 reviewed",
        ),
        gate(
            "roughcut_full_decode",
            "full OP roughcut MP4 complete-decodes",
            roughcut_decode,
            rough_summary.get("roughcut_path", "missing"),
            f"decode={roughcut_decode}",
        ),
        gate(
            "duration_match",
            "roughcut duration close to 84.437333 seconds",
            duration_match,
            rough_summary.get("roughcut_path", "missing"),
            f"duration={rough_summary.get('roughcut_duration_sec')}; delta={rough_summary.get('roughcut_duration_delta_sec')}",
        ),
        gate(
            "no_text_logo_safety",
            "manual visual QA confirms no generated readable text/logo/subtitle/watermark/random symbols",
            text_logo_review,
            "10_qa/reports/reference003_no_text_logo_safety_review_20260630.json",
            f"{safety_summary.get('items_effective_pass', 0)}/64 effective pass; gate={safety_summary.get('completion_gate_pass', False)}",
        ),
    ]
    complete = all(item["status"] == "pass" for item in gates)
    return {
        "schema_version": "reference003_completion_audit_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": now,
        "last_updated": now,
        "status": "complete" if complete else "template_not_complete",
        "source_reference": "reference-003-full-op-2160p",
        "completion_proven": complete,
        "required_evidence": gates,
        "supporting_evidence": {
            "project_validation": validation,
            "board_status": board,
            "keyframe_status_manifest": "10_qa/reference_match/REFERENCE003_OFFICIAL_KEYFRAME_STATUS_20260630/manifest.json",
            "video_unit_readiness_manifest": "08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/manifest.json",
            "video_segment_execution_packet": "00_admin/ai_bridge/packets/20260630_reference003_video_segment_execution.json",
            "roughcut_transition_audit": "09_edit/rough_cut/reference003_roughcut_transition_audit_template.json",
            "no_text_logo_safety_review": "10_qa/reports/reference003_no_text_logo_safety_review_20260630.json",
        },
        "not_complete_reason": ""
        if complete
        else "Remaining keyframes, video segments, transition review, roughcut decode/duration, or manual no-text safety evidence is incomplete.",
        "rebuild_script": rel(Path(__file__)),
    }


def write_outputs(audit: dict[str, Any]) -> None:
    json_path = REPORT_DIR / "reference003_completion_audit_template_20260630.json"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

    md = [
        "# Reference-003 Completion Audit",
        "",
        f"- Rebuilt: `{audit['last_updated']}`",
        f"- Status: `{audit['status']}`",
        f"- Completion proven: `{audit['completion_proven']}`",
        "- This is the authoritative evidence checklist for calling the full OP remake complete.",
        "",
        "## Completion Gates",
        "",
    ]
    for item in audit["required_evidence"]:
        mark = "[x]" if item["status"] == "pass" else "[ ]"
        md.append(
            f"- {mark} `{item['gate']}` — {item['status']}; current: {item['current']}; evidence: `{item['evidence']}`"
        )
    md.extend(
        [
            "",
            "## Current Boundary",
            "",
            audit["not_complete_reason"] or "All gates passed.",
            "",
            "## Rebuild Command",
            "",
            "`python3 10_qa/reports/rebuild_reference003_completion_audit.py`",
        ]
    )
    (REPORT_DIR / "reference003_completion_audit_template_20260630.md").write_text(
        "\n".join(md) + "\n"
    )


def main() -> int:
    now = datetime.now(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()
    audit = build_audit(now)
    write_outputs(audit)
    print(
        json.dumps(
            {
                "status": audit["status"],
                "completion_proven": audit["completion_proven"],
                "passed_gates": sum(
                    1 for item in audit["required_evidence"] if item["status"] == "pass"
                ),
                "total_gates": len(audit["required_evidence"]),
                "not_complete_reason": audit["not_complete_reason"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
