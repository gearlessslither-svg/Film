#!/usr/bin/env python3
"""Apply generated Reference-003 Batch05-07 keyframes after fresh-window QA.

Default mode is a dry run. Use --apply only after the selected batch output
files exist and have passed visual QA.
"""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

try:
    from PIL import Image
except ImportError:  # pragma: no cover - fallback for lean environments
    Image = None


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PACKET = PROJECT_ROOT / "00_admin/ai_bridge/packets/20260630_reference003_next_window_batch05_07_execution.json"
BOARD_PATH = PROJECT_ROOT / "03_story/idea_board/idea_board.json"
SHOT_LIST_PATH = PROJECT_ROOT / "07_shots/shot_list.csv"
REPORT_DIR = PROJECT_ROOT / "10_qa/reports"


def rel(path: Path | str) -> str:
    path = Path(path)
    if path.is_absolute():
        return str(path.relative_to(PROJECT_ROOT))
    return str(path)


def load_packet() -> dict[str, Any]:
    return json.loads(PACKET.read_text())


def batch_label(job_id: str) -> str:
    for label in ("05", "06", "07"):
        if f"BATCH{label}" in job_id:
            return label
    raise ValueError(f"Cannot derive batch label from {job_id}")


def selected_batches(packet: dict[str, Any], selection: str) -> list[dict[str, Any]]:
    batches = packet["batch_sequence"]
    if selection == "all":
        return batches
    want = selection.zfill(2)
    return [batch for batch in batches if batch_label(batch["job_id"]) == want]


def probe_image(path: Path) -> dict[str, Any]:
    result = {
        "exists": path.exists(),
        "readable": False,
        "width": None,
        "height": None,
        "error": "",
    }
    if not path.exists():
        result["error"] = "missing"
        return result
    if Image is None:
        result["readable"] = True
        result["error"] = "PIL unavailable; existence checked only"
        return result
    try:
        with Image.open(path) as image:
            image.verify()
        with Image.open(path) as image:
            result["width"] = image.width
            result["height"] = image.height
            result["readable"] = True
    except Exception as exc:  # noqa: BLE001 - report image QA problem
        result["error"] = str(exc)
    return result


def collect_items(batches: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for batch in batches:
        label = batch_label(batch["job_id"])
        for item in batch["items"]:
            output_path = item["expected_output_path"]
            probe = probe_image(PROJECT_ROOT / output_path)
            rows.append(
                {
                    "batch": label,
                    "job_id": batch["job_id"],
                    "item_id": item["item_id"],
                    "timecode": item.get("timecode", ""),
                    "video_unit_id": item.get("video_unit_id", ""),
                    "reference_frame": item.get("reference_frame", ""),
                    "generation_prompt_file": item.get("generation_prompt_file", ""),
                    "expected_output_path": output_path,
                    "exists": probe["exists"],
                    "readable": probe["readable"],
                    "width": probe["width"],
                    "height": probe["height"],
                    "probe_error": probe["error"],
                    "ready_to_apply": probe["exists"] and probe["readable"],
                }
            )
    return rows


def read_shot_list() -> tuple[list[dict[str, str]], list[str]]:
    with SHOT_LIST_PATH.open(newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader), list(reader.fieldnames or [])


def write_shot_list(rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with SHOT_LIST_PATH.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def update_board_and_shot_list(items: list[dict[str, Any]], now: str) -> dict[str, Any]:
    board = json.loads(BOARD_PATH.read_text())
    board_by_id = {row["item_id"]: row for row in board["rows"]}
    shot_rows, fieldnames = read_shot_list()
    shot_by_id = {row["shot_id"]: row for row in shot_rows}
    updated_board: list[str] = []
    updated_shot_list: list[str] = []

    for item in items:
        item_id = item["item_id"]
        board_row = board_by_id.get(item_id)
        if board_row is None:
            raise KeyError(f"Missing board row: {item_id}")
        board_row["status"] = "generated_reference003_qa_pass"
        board_row["output_path"] = item["expected_output_path"]
        board_row["output_notes"] = (
            f"reference-003 official keyframe QA pass via Batch{item['batch']} post-generation apply helper"
        )
        board_row["output_attached_at"] = now
        versions = board_row.setdefault("versions", [])
        if isinstance(versions, list):
            versions.append(
                {
                    "version_id": f"reference003_batch{item['batch']}_postgen_{now}",
                    "output_path": item["expected_output_path"],
                    "status": "generated_reference003_qa_pass",
                    "note": "Recorded by apply_reference003_batch05_07_keyframes.py",
                }
            )
        updated_board.append(item_id)

        shot_row = shot_by_id.get(item_id)
        if shot_row is None:
            raise KeyError(f"Missing shot_list row: {item_id}")
        shot_row["status"] = "generated_reference003_qa_pass"
        updated_shot_list.append(item_id)

    BOARD_PATH.write_text(json.dumps(board, ensure_ascii=False, indent=2) + "\n")
    write_shot_list(shot_rows, fieldnames)
    return {"board": updated_board, "shot_list": updated_shot_list}


def write_batch_reports(
    batches: list[dict[str, Any]],
    items: list[dict[str, Any]],
    now: str,
    applied: bool,
) -> list[str]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    written: list[str] = []
    by_batch: dict[str, list[dict[str, Any]]] = {}
    for item in items:
        by_batch.setdefault(item["batch"], []).append(item)

    for batch in batches:
        label = batch_label(batch["job_id"])
        rows = by_batch.get(label, [])
        pass_count = sum(1 for row in rows if row["ready_to_apply"])
        status = "qa_done_6_pass" if pass_count == len(rows) == 6 and applied else "ready_outputs_detected" if pass_count == len(rows) == 6 else "pending_outputs"
        report = {
            "schema_version": "reference003_batch_keyframe_postgen_apply_v1",
            "project_slug": "blue-water-citypop-op",
            "created_at": now,
            "batch": f"Batch{label}",
            "job_id": batch["job_id"],
            "status": status,
            "applied_to_board_and_shot_list": applied,
            "pass_count": pass_count,
            "total": len(rows),
            "items": rows,
            "boundary": "This helper verifies files and records status only after visual QA has been performed by the operator.",
        }
        json_path = REPORT_DIR / f"reference003_qa_batch{label}_keyframes_20260630.json"
        md_path = REPORT_DIR / f"reference003_qa_batch{label}_keyframes_20260630.md"
        json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")

        md = [
            f"# Reference-003 Batch{label} Keyframe QA",
            "",
            f"- Created: `{now}`",
            f"- Job: `{batch['job_id']}`",
            f"- Status: `{status}`",
            f"- Applied to board/shot_list: `{applied}`",
            f"- Outputs ready: {pass_count}/{len(rows)}",
            "",
            "| Item | Timecode | Output | Exists | Readable | Size |",
            "|---|---:|---|---|---|---|",
        ]
        for row in rows:
            size = (
                f"{row['width']}x{row['height']}"
                if row["width"] and row["height"]
                else "-"
            )
            md.append(
                f"| `{row['item_id']}` | {row['timecode']} | `{row['expected_output_path']}` | {row['exists']} | {row['readable']} | {size} |"
            )
        md.extend(
            [
                "",
                "## Boundary",
                "",
                "Use this report as status evidence only after visual QA confirms composition, no-text/no-logo safety, and age-appropriate character handling.",
            ]
        )
        md_path.write_text("\n".join(md) + "\n")
        written.extend([rel(json_path), rel(md_path)])

        manifest_path = PROJECT_ROOT / batch["manifest"]
        manifest = json.loads(manifest_path.read_text())
        manifest["status"] = "qa_done_6_pass" if applied and pass_count == len(rows) == 6 else manifest.get("status", "refs_prepared_no_generation_in_warn_window")
        manifest["post_generation_apply"] = {
            "applied": applied,
            "applied_at": now if applied else "",
            "pass_count": pass_count,
            "total": len(rows),
            "report_json": rel(json_path),
            "report_md": rel(md_path),
        }
        if applied and pass_count == len(rows) == 6:
            for manifest_item in manifest.get("items", []):
                match = next((row for row in rows if row["item_id"] == manifest_item["item_id"]), None)
                if match:
                    manifest_item["output_path"] = match["expected_output_path"]
                    manifest_item["qa_status"] = "pass"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return written


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", choices=["05", "06", "07", "all"], default="all")
    parser.add_argument("--apply", action="store_true", help="Update board and shot_list after outputs are present and QA passed.")
    parser.add_argument("--allow-partial", action="store_true", help="Allow applying only ready outputs from selected batches.")
    args = parser.parse_args()

    now = datetime.now(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()
    packet = load_packet()
    batches = selected_batches(packet, args.batch)
    if not batches:
        raise SystemExit(f"No batches selected for {args.batch}")
    items = collect_items(batches)
    ready = [item for item in items if item["ready_to_apply"]]
    missing = [item for item in items if not item["ready_to_apply"]]

    applied = False
    updates: dict[str, Any] = {"board": [], "shot_list": []}
    if args.apply:
        if missing and not args.allow_partial:
            print(
                json.dumps(
                    {
                        "status": "not_applied_missing_outputs",
                        "selected_batch": args.batch,
                        "ready": len(ready),
                        "missing": [item["item_id"] for item in missing],
                        "hint": "Generate missing outputs first, or rerun with --allow-partial after visual QA.",
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
            return 2
        updates = update_board_and_shot_list(ready, now)
        applied = True

    written_reports = write_batch_reports(batches, items, now, applied)
    print(
        json.dumps(
            {
                "status": "applied" if applied else "dry_run",
                "selected_batch": args.batch,
                "selected_items": len(items),
                "ready_outputs": len(ready),
                "missing_or_unreadable_outputs": [
                    {
                        "item_id": item["item_id"],
                        "expected_output_path": item["expected_output_path"],
                        "error": item["probe_error"],
                    }
                    for item in missing
                ],
                "updates": updates,
                "reports": written_reports,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
