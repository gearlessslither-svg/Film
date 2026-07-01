#!/usr/bin/env python3
"""Rebuild the Reference-003 roughcut and transition audit.

This script does not generate video. It checks the expected 21 segment paths,
probes/decode-checks any existing MP4s, preserves transition review status when
present, and rewrites the roughcut audit JSON/MD.
"""

from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
REPORT_DIR = PROJECT_ROOT / "10_qa/reports"
ROUGH_DIR = PROJECT_ROOT / "09_edit/rough_cut"
FFMPEG = Path("/Applications/Bitwig Studio.app/Contents/MacOS/ffmpeg")
REFERENCE_DURATION_SEC = 84.437333
EXPECTED_ROUGHCUT = ROUGH_DIR / "reference003_full_op_roughcut_20260630.mp4"


def rel(path: str | Path) -> str:
    path = Path(path)
    if path.is_absolute():
        return str(path.relative_to(PROJECT_ROOT))
    return str(path)


def read_json(rel_path: str) -> Any:
    return json.loads((PROJECT_ROOT / rel_path).read_text())


def parse_duration(line: str) -> float | None:
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", line)
    if not match:
        return None
    hours = int(match.group(1))
    minutes = int(match.group(2))
    seconds = float(match.group(3))
    return hours * 3600 + minutes * 60 + seconds


def probe_video(path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "path": rel(path),
        "exists": path.exists(),
        "decode_ok": False,
        "duration_sec": None,
        "duration_line": "",
        "probe_error": "",
    }
    if not path.exists():
        result["probe_error"] = "missing"
        return result
    if not FFMPEG.exists():
        result["probe_error"] = f"ffmpeg not found: {FFMPEG}"
        return result

    decode = subprocess.run(
        [str(FFMPEG), "-v", "error", "-i", str(path), "-f", "null", "-"],
        capture_output=True,
        text=True,
    )
    result["decode_ok"] = decode.returncode == 0
    if decode.returncode != 0:
        result["probe_error"] = (decode.stderr or decode.stdout or "").strip()

    info = subprocess.run(
        [str(FFMPEG), "-hide_banner", "-i", str(path)],
        capture_output=True,
        text=True,
    )
    for line in (info.stderr or info.stdout or "").splitlines():
        if "Duration:" in line:
            result["duration_line"] = line.strip()
            result["duration_sec"] = parse_duration(line)
            break
    return result


def prior_transition_reviews() -> dict[str, dict[str, Any]]:
    reviews: dict[str, dict[str, Any]] = {}
    for candidate in [
        ROUGH_DIR / "reference003_roughcut_transition_audit_template.json",
        REPORT_DIR / "reference003_roughcut_transition_audit_template_20260630.json",
    ]:
        if not candidate.exists():
            continue
        try:
            data = json.loads(candidate.read_text())
        except json.JSONDecodeError:
            continue
        for edge in data.get("transition_edges", []):
            edge_id = edge.get("edge_id")
            if not edge_id:
                continue
            reviews[edge_id] = {
                "review_status": edge.get("review_status", "pending"),
                "reviewed_at": edge.get("reviewed_at", ""),
                "reviewer": edge.get("reviewer", ""),
                "evidence_path": edge.get("evidence_path", ""),
                "review_notes": edge.get("review_notes", ""),
            }
    return reviews


def build_audit(now: str) -> dict[str, Any]:
    segment_packet = read_json(
        "00_admin/ai_bridge/packets/20260630_reference003_video_segment_execution.json"
    )
    transition_edges = read_json("07_shots/transition_edges.json")["edges"]
    preserved_reviews = prior_transition_reviews()

    segments = []
    for unit in segment_packet["units"]:
        path = PROJECT_ROOT / unit["expected_video_output_path"]
        probe = probe_video(path)
        segments.append(
            {
                "slot": unit["order"],
                "unit_id": unit["unit_id"],
                "time_range": unit["time_range"],
                "expected_video_output_path": unit["expected_video_output_path"],
                "source_gate_now": unit["generation_gate"],
                "blocking_keyframes": unit.get("blocking_keyframes", []),
                "exists": probe["exists"],
                "decode_status": "pass" if probe["decode_ok"] else "pending_or_fail",
                "duration_sec": probe["duration_sec"],
                "duration_line": probe["duration_line"],
                "probe_error": probe["probe_error"],
                "qa_status": "pending",
            }
        )

    roughcut_probe = probe_video(EXPECTED_ROUGHCUT)
    duration_delta = None
    if roughcut_probe["duration_sec"] is not None:
        duration_delta = round(roughcut_probe["duration_sec"] - REFERENCE_DURATION_SEC, 3)

    transition_rows = []
    for edge in transition_edges:
        edge_id = edge["edge_id"]
        review = preserved_reviews.get(edge_id, {})
        transition_rows.append(
            {
                "edge_id": edge_id,
                "from": edge.get("from", ""),
                "to": edge.get("to", ""),
                "from_unit": edge.get("from_unit", ""),
                "to_unit": edge.get("to_unit", ""),
                "transition_type": edge.get("transition_type", ""),
                "visual_bridge": edge.get("visual_bridge", ""),
                "review_status": review.get("review_status", "pending"),
                "reviewed_at": review.get("reviewed_at", ""),
                "reviewer": review.get("reviewer", ""),
                "evidence_path": review.get("evidence_path", ""),
                "review_notes": review.get("review_notes", ""),
            }
        )

    segment_decode_pass = sum(1 for segment in segments if segment["decode_status"] == "pass")
    segment_exists = sum(1 for segment in segments if segment["exists"])
    transitions_reviewed = sum(
        1 for edge in transition_rows if edge["review_status"] in {"pass", "reviewed"}
    )
    roughcut_decode_ok = roughcut_probe["decode_ok"]
    duration_match = (
        duration_delta is not None and abs(duration_delta) <= 1.0
    )
    all_pass = (
        segment_decode_pass == 21
        and transitions_reviewed == 41
        and roughcut_decode_ok
        and duration_match
    )
    status = "roughcut_audit_pass" if all_pass else "template_waiting_for_video_segments"

    return {
        "schema_version": "reference003_roughcut_transition_audit_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": now,
        "status": status,
        "source_reference": "reference-003-full-op-2160p",
        "expected_duration_sec": REFERENCE_DURATION_SEC,
        "summary": {
            "segments_total": 21,
            "segments_existing": segment_exists,
            "segments_decode_pass": segment_decode_pass,
            "transition_edges_total": 41,
            "transition_edges_reviewed": transitions_reviewed,
            "roughcut_path": rel(EXPECTED_ROUGHCUT),
            "roughcut_exists": roughcut_probe["exists"],
            "roughcut_decode_ok": roughcut_decode_ok,
            "roughcut_duration_sec": roughcut_probe["duration_sec"],
            "roughcut_duration_delta_sec": duration_delta,
            "roughcut_duration_match_within_1s": duration_match,
        },
        "segments": segments,
        "transition_edges": transition_rows,
        "roughcut_probe": roughcut_probe,
        "final_gates": [
            {
                "gate": "segments_21_decode_pass",
                "status": "pass" if segment_decode_pass == 21 else "pending",
                "evidence": f"{segment_decode_pass}/21 segment files decode pass",
            },
            {
                "gate": "transition_edges_41_reviewed",
                "status": "pass" if transitions_reviewed == 41 else "pending",
                "evidence": f"{transitions_reviewed}/41 transition edges reviewed",
            },
            {
                "gate": "roughcut_full_decode",
                "status": "pass" if roughcut_decode_ok else "pending",
                "evidence": roughcut_probe["path"],
            },
            {
                "gate": "duration_match",
                "status": "pass" if duration_match else "pending",
                "evidence": f"delta={duration_delta}",
            },
            {
                "gate": "no_text_logo_safety",
                "status": "manual_review_required",
                "evidence": "requires human visual QA on generated segments and roughcut",
            },
        ],
        "rebuild_script": rel(Path(__file__)),
    }


def write_outputs(audit: dict[str, Any]) -> None:
    for path in [
        ROUGH_DIR / "reference003_roughcut_transition_audit_template.json",
        REPORT_DIR / "reference003_roughcut_transition_audit_template_20260630.json",
    ]:
        path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

    md: list[str] = [
        "# Reference-003 Roughcut and Transition Audit",
        "",
        f"- Rebuilt: `{audit['created_at']}`",
        f"- Status: `{audit['status']}`",
        f"- Expected reference duration: `{audit['expected_duration_sec']}` seconds",
        "",
        "## Summary",
        "",
    ]
    for key, value in audit["summary"].items():
        md.append(f"- `{key}`: `{value}`")
    md.extend(
        [
            "",
            "## Segment Assembly Order",
            "",
            "| Slot | Unit | Time | Expected segment | Exists | Decode | Duration |",
            "|---:|---|---|---|---|---|---:|",
        ]
    )
    for segment in audit["segments"]:
        md.append(
            f"| {segment['slot']} | `{segment['unit_id']}` | {segment['time_range']} | "
            f"`{segment['expected_video_output_path']}` | {segment['exists']} | "
            f"`{segment['decode_status']}` | {segment['duration_sec']} |"
        )
    md.extend(
        [
            "",
            "## Transition Review Matrix",
            "",
            "| Edge | From | To | Type | Bridge | Status | Reviewer | Evidence | Notes |",
            "|---|---|---|---|---|---|---|---|---|",
        ]
    )
    for edge in audit["transition_edges"]:
        bridge = str(edge["visual_bridge"]).replace("|", "/")
        notes = str(edge.get("review_notes", "")).replace("|", "/")
        md.append(
            f"| `{edge['edge_id']}` | `{edge['from']}` | `{edge['to']}` | "
            f"`{edge['transition_type']}` | {bridge} | `{edge['review_status']}` | "
            f"{edge.get('reviewer', '')} | `{edge.get('evidence_path', '')}` | {notes} |"
        )
    md.extend(["", "## Final Gates", ""])
    for gate in audit["final_gates"]:
        mark = "[x]" if gate["status"] == "pass" else "[ ]"
        md.append(f"- {mark} `{gate['gate']}` — {gate['status']}; {gate['evidence']}")
    md.extend(
        [
            "",
            "## Boundary",
            "",
            "This audit is evidence only for files that exist and decode. Text/logo safety remains a visual QA gate and cannot be proven by this script alone.",
        ]
    )
    for path in [
        ROUGH_DIR / "reference003_roughcut_transition_audit_template.md",
        REPORT_DIR / "reference003_roughcut_transition_audit_template_20260630.md",
    ]:
        path.write_text("\n".join(md) + "\n")


def main() -> int:
    now = datetime.now(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    audit = build_audit(now)
    write_outputs(audit)
    print(
        json.dumps(
            {
                "status": audit["status"],
                "summary": audit["summary"],
                "report": rel(
                    REPORT_DIR / "reference003_roughcut_transition_audit_template_20260630.md"
                ),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
