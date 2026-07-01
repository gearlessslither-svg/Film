#!/usr/bin/env python3
"""Preflight the Reference-003 Batch05-07 fresh-window generation handoff.

This script does not generate images. It checks that the remaining 18 official
keyframes are still exactly the next work, that reference frames/prompts exist,
that expected output paths are known, and that the project validator still
passes before a fresh window starts Batch05-07 generation.
"""

from __future__ import annotations

import csv
import json
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[3]
REPORT_DIR = PROJECT_ROOT / "10_qa/reports"
QUEUE_JSON = PROJECT_ROOT / "00_admin/ai_bridge/packets/20260630_reference003_remaining_keyframe_generation_queue.json"
NEXT_PACKET_JSON = PROJECT_ROOT / "00_admin/ai_bridge/packets/20260630_reference003_next_window_batch05_07_execution.json"
HANDOFF_LATEST = PROJECT_ROOT / "00_admin/handoff/HANDOFF_LATEST.md"
START_HERE = PROJECT_ROOT / "00_admin/handoff/NEXT_WINDOW_START_HERE_REFERENCE003_20260630.md"
VALIDATOR = Path("/Users/jaychoupp/Story/Film/scripts/validate_aigc_project.py")
EXPECTED_ITEMS = [f"OP_SHOT_{idx:03d}" for idx in range(25, 43)]
EXPECTED_BATCHES = {"05": 6, "06": 6, "07": 6}


def rel(path: str | Path) -> str:
    path = Path(path)
    if path.is_absolute():
        return str(path.relative_to(PROJECT_ROOT))
    return str(path)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def now_iso() -> str:
    return datetime.now(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()


def run_validator() -> dict[str, Any]:
    proc = subprocess.run(
        ["python3", str(VALIDATOR), str(PROJECT_ROOT)],
        capture_output=True,
        text=True,
    )
    output = ((proc.stdout or "") + (proc.stderr or "")).strip()
    return {
        "command": f"python3 {VALIDATOR} {PROJECT_ROOT}",
        "returncode": proc.returncode,
        "project_status_pass": "project_status=pass" in output,
        "output_tail": "\n".join(output.splitlines()[-20:]),
    }


def load_board_status() -> dict[str, Any]:
    board = read_json(PROJECT_ROOT / "03_story/idea_board/idea_board.json")
    board_by_id = {row["item_id"]: row for row in board["rows"]}
    board_counts: dict[str, int] = {}
    for row in board["rows"]:
        status = row.get("status", "unknown")
        board_counts[status] = board_counts.get(status, 0) + 1

    with (PROJECT_ROOT / "07_shots/shot_list.csv").open(
        "r", encoding="utf-8-sig", newline=""
    ) as handle:
        shot_rows = list(csv.DictReader(handle))
    shot_by_id = {row["shot_id"]: row for row in shot_rows}
    shot_counts: dict[str, int] = {}
    for row in shot_rows:
        status = row.get("status", "unknown")
        shot_counts[status] = shot_counts.get(status, 0) + 1

    remaining = []
    for item_id in EXPECTED_ITEMS:
        board_row = board_by_id.get(item_id, {})
        shot_row = shot_by_id.get(item_id, {})
        remaining.append(
            {
                "item_id": item_id,
                "board_status": board_row.get("status", "missing"),
                "shot_list_status": shot_row.get("status", "missing"),
                "board_output_path": board_row.get("output_path", ""),
                "shot_prompt_path": shot_row.get("prompt_path", ""),
            }
        )

    return {
        "board_rows": len(board["rows"]),
        "shot_list_rows": len(shot_rows),
        "board_status_counts": board_counts,
        "shot_list_status_counts": shot_counts,
        "remaining_items": remaining,
    }


def file_check(rel_path: str) -> dict[str, Any]:
    path = PROJECT_ROOT / rel_path
    return {
        "path": rel_path,
        "exists": path.is_file(),
        "size_bytes": path.stat().st_size if path.is_file() else 0,
    }


def inspect_queue() -> dict[str, Any]:
    queue = read_json(QUEUE_JSON)
    items = queue.get("items", [])
    by_batch: dict[str, int] = {}
    rows = []
    for expected_order, item in enumerate(items, start=1):
        batch = str(item.get("batch", ""))
        by_batch[batch] = by_batch.get(batch, 0) + 1
        prompt_file = item.get("generation_prompt_file", "")
        prompt_path = PROJECT_ROOT / prompt_file
        prompt_text = item.get("generation_prompt_text", "")
        prompt_file_text = prompt_path.read_text(encoding="utf-8") if prompt_path.is_file() else ""
        reference = file_check(item.get("reference_frame", ""))
        prompt = file_check(prompt_file)
        output = file_check(item.get("expected_output_path", ""))
        rows.append(
            {
                "queue_order": item.get("queue_order"),
                "expected_order": expected_order,
                "batch": batch,
                "item_id": item.get("item_id", ""),
                "timecode": item.get("timecode", ""),
                "video_unit_id": item.get("video_unit_id", ""),
                "status_now": item.get("status_now", ""),
                "reference": reference,
                "prompt": prompt,
                "prompt_chars_declared": item.get("generation_prompt_chars", 0),
                "prompt_chars_file": len(prompt_file_text),
                "prompt_text_present": bool(prompt_text.strip()),
                "prompt_text_matches_file": prompt_text.strip() == prompt_file_text.strip(),
                "output": output,
                "apply_command": item.get("post_generation_apply_command", ""),
            }
        )
    return {
        "schema_version": queue.get("schema_version", ""),
        "status": queue.get("status", ""),
        "items_total": len(items),
        "by_batch": by_batch,
        "items": rows,
    }


def build_preflight() -> dict[str, Any]:
    now = now_iso()
    queue = inspect_queue()
    board = load_board_status()
    validation = run_validator()
    next_packet = read_json(NEXT_PACKET_JSON)

    item_ids = [row["item_id"] for row in queue["items"]]
    expected_order_ok = item_ids == EXPECTED_ITEMS
    queue_order_ok = all(
        row["queue_order"] == row["expected_order"] for row in queue["items"]
    )
    batch_counts_ok = queue["by_batch"] == EXPECTED_BATCHES
    refs_ok = all(row["reference"]["exists"] and row["reference"]["size_bytes"] > 0 for row in queue["items"])
    prompts_ok = all(
        row["prompt"]["exists"]
        and row["prompt"]["size_bytes"] > 0
        and row["prompt_text_present"]
        and row["prompt_text_matches_file"]
        for row in queue["items"]
    )
    outputs_existing = [row for row in queue["items"] if row["output"]["exists"]]
    outputs_missing = [row for row in queue["items"] if not row["output"]["exists"]]
    remaining_status_ok = all(
        row["board_status"] == "prompt_ready_reference003"
        and row["shot_list_status"] == "prompt_ready_reference003"
        for row in board["remaining_items"]
    )
    counts_ok = (
        board["board_status_counts"].get("generated_reference003_qa_pass", 0) == 24
        and board["board_status_counts"].get("prompt_ready_reference003", 0) == 18
        and board["shot_list_status_counts"].get("generated_reference003_qa_pass", 0) == 24
        and board["shot_list_status_counts"].get("prompt_ready_reference003", 0) == 18
    )
    handoff_ok = HANDOFF_LATEST.is_file() and START_HERE.is_file()
    next_packet_ok = (
        next_packet.get("schema_version") == "reference003_next_window_batch05_07_execution_v1"
        and next_packet.get("status") == "ready_for_fresh_window_image_generation"
    )

    gates = [
        {"gate": "handoff_files_exist", "pass": handoff_ok, "current": str(handoff_ok)},
        {
            "gate": "project_validation",
            "pass": validation["project_status_pass"],
            "current": "project_status=pass" if validation["project_status_pass"] else "project_status=fail",
        },
        {"gate": "queue_has_18_items", "pass": queue["items_total"] == 18, "current": str(queue["items_total"])},
        {"gate": "queue_order_op_shot_025_to_042", "pass": expected_order_ok and queue_order_ok, "current": f"{item_ids[:1]}..{item_ids[-1:] if item_ids else []}"},
        {"gate": "batch_counts_6_each", "pass": batch_counts_ok, "current": str(queue["by_batch"])},
        {"gate": "reference_frames_exist", "pass": refs_ok, "current": f"{sum(1 for row in queue['items'] if row['reference']['exists'])}/18"},
        {"gate": "prompt_files_match_queue_text", "pass": prompts_ok, "current": f"{sum(1 for row in queue['items'] if row['prompt_text_matches_file'])}/18"},
        {"gate": "board_and_shot_list_at_24_18", "pass": counts_ok and remaining_status_ok, "current": f"board={board['board_status_counts']}; shot_list={board['shot_list_status_counts']}"},
        {"gate": "next_window_packet_ready", "pass": next_packet_ok, "current": next_packet.get("status", "missing")},
    ]

    if len(outputs_existing) == 0:
        status = "ready_for_fresh_window_generation"
        next_action = "Open a fresh window and generate OP_SHOT_025 through OP_SHOT_042 in queue_order."
    elif len(outputs_missing) == 0:
        status = "all_expected_outputs_present_ready_for_apply_review"
        next_action = "Run visual QA, then apply Batch05-07 outputs with apply_reference003_batch05_07_keyframes.py."
    else:
        status = "partial_outputs_present_review_before_continue"
        next_action = "Review existing outputs and continue only missing queue items; avoid duplicate generation."

    if not all(gate["pass"] for gate in gates):
        status = "preflight_blocked_check_gates"
        next_action = "Fix failed preflight gates before generating."

    return {
        "schema_version": "reference003_next_window_preflight_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": now,
        "status": status,
        "next_action": next_action,
        "fresh_window_required": True,
        "summary": {
            "queue_items": queue["items_total"],
            "expected_outputs_existing": len(outputs_existing),
            "expected_outputs_missing": len(outputs_missing),
            "board_status_counts": board["board_status_counts"],
            "shot_list_status_counts": board["shot_list_status_counts"],
            "project_validation_pass": validation["project_status_pass"],
        },
        "gates": gates,
        "queue": queue,
        "board": board,
        "project_validation": validation,
        "evidence_files": {
            "handoff_latest": rel(HANDOFF_LATEST),
            "start_here": rel(START_HERE),
            "queue_json": rel(QUEUE_JSON),
            "next_window_packet": rel(NEXT_PACKET_JSON),
            "apply_helper": "00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py",
        },
        "rebuild_script": rel(Path(__file__)),
    }


def write_outputs(preflight: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    json_path = REPORT_DIR / "reference003_next_window_preflight_20260630.json"
    md_path = REPORT_DIR / "reference003_next_window_preflight_20260630.md"
    json_path.write_text(json.dumps(preflight, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = [
        "# Reference-003 Next Window Preflight",
        "",
        f"- Rebuilt: `{preflight['created_at']}`",
        f"- Status: `{preflight['status']}`",
        f"- Fresh window required: `{preflight['fresh_window_required']}`",
        f"- Next action: {preflight['next_action']}",
        "",
        "## Summary",
        "",
    ]
    for key, value in preflight["summary"].items():
        md.append(f"- `{key}`: `{value}`")
    md.extend(["", "## Gates", ""])
    for gate in preflight["gates"]:
        mark = "[x]" if gate["pass"] else "[ ]"
        md.append(f"- {mark} `{gate['gate']}` — {gate['current']}")
    md.extend(
        [
            "",
            "## Queue",
            "",
            "| # | Batch | Item | Reference | Prompt | Output exists |",
            "|---:|---|---|---|---|---|",
        ]
    )
    for row in preflight["queue"]["items"]:
        md.append(
            f"| {row['queue_order']} | {row['batch']} | `{row['item_id']}` | "
            f"{row['reference']['exists']} | {row['prompt']['exists']} | {row['output']['exists']} |"
        )
    md.extend(["", "## Evidence Files", ""])
    for key, value in preflight["evidence_files"].items():
        md.append(f"- `{key}`: `{value}`")
    md_path.write_text("\n".join(md) + "\n", encoding="utf-8")


def main() -> int:
    preflight = build_preflight()
    write_outputs(preflight)
    print(
        json.dumps(
            {
                "status": preflight["status"],
                "summary": preflight["summary"],
                "failed_gates": [gate["gate"] for gate in preflight["gates"] if not gate["pass"]],
                "report": "10_qa/reports/reference003_next_window_preflight_20260630.md",
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if all(gate["pass"] for gate in preflight["gates"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
