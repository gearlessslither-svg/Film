#!/usr/bin/env python3
"""Run the Reference-003 full pipeline gate audit.

This script does not generate images or videos. It reruns the idempotent status
rebuilders, project validation, and completion audit, then writes one compact
summary that shows which gates still block completion.
"""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
REPORT_DIR = PROJECT_ROOT / "10_qa/reports"
VALIDATOR = Path("/Users/jaychoupp/Story/Film/scripts/validate_aigc_project.py")


COMMANDS = [
    {
        "name": "project_validation",
        "cmd": ["python3", str(VALIDATOR), str(PROJECT_ROOT)],
    },
    {
        "name": "keyframe_status_previs_rebuild",
        "cmd": [
            "python3",
            str(
                PROJECT_ROOT
                / "10_qa/reference_match/REFERENCE003_OFFICIAL_KEYFRAME_STATUS_20260630/rebuild_reference003_keyframe_status_previs.py"
            ),
        ],
    },
    {
        "name": "video_unit_readiness_rebuild",
        "cmd": [
            "python3",
            str(
                PROJECT_ROOT
                / "08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/rebuild_reference003_video_unit_readiness.py"
            ),
        ],
    },
    {
        "name": "roughcut_assembly_readiness",
        "cmd": [
            "python3",
            str(PROJECT_ROOT / "09_edit/rough_cut/assemble_reference003_roughcut_from_segments.py"),
            "--check-only",
            "--print-json",
        ],
    },
    {
        "name": "roughcut_transition_audit_rebuild",
        "cmd": [
            "python3",
            str(PROJECT_ROOT / "09_edit/rough_cut/rebuild_reference003_roughcut_transition_audit.py"),
        ],
    },
    {
        "name": "no_text_logo_safety_review_refresh",
        "cmd": [
            "python3",
            str(PROJECT_ROOT / "10_qa/reports/update_reference003_no_text_logo_safety_review.py"),
            "--refresh",
            "--print-json",
        ],
    },
    {
        "name": "completion_audit_rebuild",
        "cmd": [
            "python3",
            str(PROJECT_ROOT / "10_qa/reports/rebuild_reference003_completion_audit.py"),
        ],
    },
]


def rel(path: Path | str) -> str:
    path = Path(path)
    if path.is_absolute():
        return str(path.relative_to(PROJECT_ROOT))
    return str(path)


def run_command(spec: dict[str, Any]) -> dict[str, Any]:
    proc = subprocess.run(spec["cmd"], capture_output=True, text=True)
    output = ((proc.stdout or "") + (proc.stderr or "")).strip()
    lines = output.splitlines()
    return {
        "name": spec["name"],
        "command": " ".join(spec["cmd"]),
        "returncode": proc.returncode,
        "ok": proc.returncode == 0,
        "output_tail": "\n".join(lines[-20:]),
    }


def read_json(rel_path: str) -> dict[str, Any]:
    return json.loads((PROJECT_ROOT / rel_path).read_text())


def build_summary(now: str, command_results: list[dict[str, Any]]) -> dict[str, Any]:
    keyframe = read_json(
        "10_qa/reference_match/REFERENCE003_OFFICIAL_KEYFRAME_STATUS_20260630/manifest.json"
    )
    video_unit = read_json("08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/manifest.json")
    roughcut = read_json("09_edit/rough_cut/reference003_roughcut_transition_audit_template.json")
    safety = read_json("10_qa/reports/reference003_no_text_logo_safety_review_20260630.json")
    completion = read_json("10_qa/reports/reference003_completion_audit_template_20260630.json")

    gates = completion.get("required_evidence", [])
    passed = [gate for gate in gates if gate.get("status") == "pass"]
    pending = [gate for gate in gates if gate.get("status") != "pass"]
    blocking = [
        {
            "gate": gate.get("gate"),
            "current": gate.get("current"),
            "evidence": gate.get("evidence"),
        }
        for gate in pending
    ]
    status = "complete" if completion.get("completion_proven") else "not_complete"
    all_commands_ok = all(result["ok"] for result in command_results)
    return {
        "schema_version": "reference003_full_pipeline_gate_audit_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": now,
        "status": status,
        "completion_proven": bool(completion.get("completion_proven")),
        "all_commands_ok": all_commands_ok,
        "command_results": command_results,
        "summary": {
            "keyframes_official_generated": keyframe.get("counts", {}).get(
                "official_generated_keyframes", 0
            ),
            "keyframes_pending": keyframe.get("counts", {}).get("pending_keyframes", 0),
            "video_units_ready": video_unit.get("summary", {}).get(
                "video_units_ready_for_generation", 0
            ),
            "video_units_blocked": video_unit.get("summary", {}).get(
                "video_units_blocked_until_keyframes_complete", 0
            ),
            "segments_decode_pass": roughcut.get("summary", {}).get("segments_decode_pass", 0),
            "transition_edges_reviewed": roughcut.get("summary", {}).get(
                "transition_edges_reviewed", 0
            ),
            "roughcut_decode_ok": roughcut.get("summary", {}).get("roughcut_decode_ok", False),
            "no_text_logo_safety_pass": safety.get("summary", {}).get(
                "completion_gate_pass", False
            ),
            "completion_gates_passed": len(passed),
            "completion_gates_total": len(gates),
        },
        "blocking_gates": blocking,
        "evidence_files": {
            "keyframe_status_manifest": "10_qa/reference_match/REFERENCE003_OFFICIAL_KEYFRAME_STATUS_20260630/manifest.json",
            "video_unit_readiness_manifest": "08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/manifest.json",
            "roughcut_assembly_report": "10_qa/reports/reference003_roughcut_assembly_20260630.json",
            "roughcut_transition_audit": "09_edit/rough_cut/reference003_roughcut_transition_audit_template.json",
            "no_text_logo_safety_review": "10_qa/reports/reference003_no_text_logo_safety_review_20260630.json",
            "completion_audit": "10_qa/reports/reference003_completion_audit_template_20260630.json",
        },
        "boundary": "This audit proves the current gate state only; it cannot replace missing image/video generation or manual visual safety review.",
        "rebuild_script": rel(Path(__file__)),
    }


def write_reports(audit: dict[str, Any]) -> None:
    json_path = REPORT_DIR / "reference003_full_pipeline_gate_audit_20260630.json"
    md_path = REPORT_DIR / "reference003_full_pipeline_gate_audit_20260630.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

    md = [
        "# Reference-003 Full Pipeline Gate Audit",
        "",
        f"- Rebuilt: `{audit['created_at']}`",
        f"- Status: `{audit['status']}`",
        f"- Completion proven: `{audit['completion_proven']}`",
        f"- Commands OK: `{audit['all_commands_ok']}`",
        "",
        "## Summary",
        "",
    ]
    for key, value in audit["summary"].items():
        md.append(f"- `{key}`: `{value}`")
    md.extend(["", "## Blocking Gates", ""])
    if audit["blocking_gates"]:
        for gate in audit["blocking_gates"]:
            md.append(
                f"- `{gate['gate']}` — current: {gate['current']}; evidence: `{gate['evidence']}`"
            )
    else:
        md.append("- None")
    md.extend(["", "## Commands", ""])
    for result in audit["command_results"]:
        md.append(f"- `{result['name']}` — ok={result['ok']} returncode={result['returncode']}")
    md.extend(["", "## Evidence Files", ""])
    for key, value in audit["evidence_files"].items():
        md.append(f"- `{key}`: `{value}`")
    md.extend(["", "## Boundary", "", audit["boundary"]])
    md_path.write_text("\n".join(md) + "\n")


def main() -> int:
    now = datetime.now(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    results = [run_command(spec) for spec in COMMANDS]
    audit = build_summary(now, results)
    write_reports(audit)
    print(
        json.dumps(
            {
                "status": audit["status"],
                "completion_proven": audit["completion_proven"],
                "all_commands_ok": audit["all_commands_ok"],
                "summary": audit["summary"],
                "blocking_gates": [gate["gate"] for gate in audit["blocking_gates"]],
                "report": "10_qa/reports/reference003_full_pipeline_gate_audit_20260630.md",
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if audit["all_commands_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
