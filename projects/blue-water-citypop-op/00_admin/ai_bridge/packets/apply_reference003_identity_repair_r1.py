#!/usr/bin/env python3
"""Apply Reference-003 identity repair R1 outputs to board and asset locks."""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from PIL import Image


PROJECT_ROOT = Path(__file__).resolve().parents[3]
BOARD_PATH = PROJECT_ROOT / "03_story/idea_board/idea_board.json"
ASSET_LOCKS_PATH = PROJECT_ROOT / "05_asset_bible/setting_chapters/reference003_asset_locks_v1.json"
JOB_MANIFEST_PATH = PROJECT_ROOT / "08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/manifest.json"
REPORT_JSON = PROJECT_ROOT / "10_qa/reports/reference003_identity_repair_r1_application_20260630.json"
REPORT_MD = PROJECT_ROOT / "10_qa/reports/reference003_identity_repair_r1_application_20260630.md"
TZ = timezone(timedelta(hours=8))


REPLACEMENTS = {
    "OP_SHOT_024": {
        "output_path": "08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/outputs/OP_SHOT_024_VEHICLE_LOCK_R1.png",
        "decision": "R1 Grandis vehicle/action craft lock generated from dense OP24 reference frames; use as new vehicle/action craft continuity source.",
        "status": "generated_reference003_identity_repair_r1_pass",
    },
    "OP_SHOT_025": {
        "output_path": "08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/outputs/OP_SHOT_025_R1.png",
        "decision": "R1 hard replacement for director-rejected large group portrait; uses locked character identities and new Grandis vehicle craft lock.",
        "status": "generated_reference003_identity_repair_r1_pass",
    },
    "OP_SHOT_034": {
        "output_path": "08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/outputs/OP_SHOT_034_R1.png",
        "decision": "R1 hard replacement for director-rejected sea-background Nadia; uses OP_SHOT_011_v2 as Nadia face lock.",
        "status": "generated_reference003_identity_repair_r1_pass",
    },
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def image_size(rel_path: str) -> str:
    path = PROJECT_ROOT / rel_path
    with Image.open(path) as image:
        width, height = image.size
    return f"{width}x{height}"


def apply_board(now: str) -> list[dict[str, Any]]:
    board = load_json(BOARD_PATH)
    applied: list[dict[str, Any]] = []
    rows = board.get("rows", [])
    for item_id, replacement in REPLACEMENTS.items():
        row = next((candidate for candidate in rows if candidate.get("item_id") == item_id), None)
        if row is None:
            raise RuntimeError(f"Missing idea_board row: {item_id}")
        old_path = row.get("output_path", "")
        row["output_path"] = replacement["output_path"]
        row["output_attached_at"] = now
        row["output_notes"] = replacement["decision"]
        row["notes"] = replacement["decision"]
        row["revision_note"] = "REFERENCE003_IDENTITY_REPAIR_R1 applied after director rejected OP_SHOT_025 and OP_SHOT_034; video assembly waits until image QA."
        versions = row.setdefault("versions", [])
        versions.append(
            {
                "version_id": f"reference003_identity_repair_r1_{now}",
                "output_path": replacement["output_path"],
                "status": replacement["status"],
                "note": replacement["decision"],
                "supersedes_path": old_path,
                "created_at": now,
                "packet_id": "REFERENCE003_IDENTITY_REPAIR_R1_20260630",
            }
        )
        applied.append(
            {
                "item_id": item_id,
                "old_output_path": old_path,
                "new_output_path": replacement["output_path"],
                "status_kept_for_pipeline": row.get("status"),
                "repair_status": replacement["status"],
                "size": image_size(replacement["output_path"]),
            }
        )
    write_json(BOARD_PATH, board)
    return applied


def apply_asset_locks(now: str) -> dict[str, Any]:
    asset_locks = load_json(ASSET_LOCKS_PATH)
    props = asset_locks.setdefault("props_vehicles_symbols", {})
    props["grandis_vehicle"] = {
        "status": "official_prop_lock",
        "lock_path": REPLACEMENTS["OP_SHOT_024"]["output_path"],
        "director_note": "R1 Grandis vehicle/action craft lock replaces the rejected OP_SHOT_025 vehicle/group reference.",
        "updated_at": now,
    }
    asset_locks["latest_repair_outputs"] = {
        item_id: {
            "status": data["status"],
            "output_path": data["output_path"],
            "decision": data["decision"],
        }
        for item_id, data in REPLACEMENTS.items()
    }
    write_json(ASSET_LOCKS_PATH, asset_locks)
    return asset_locks["latest_repair_outputs"]


def update_job_manifest(applied: list[dict[str, Any]], now: str) -> None:
    manifest = load_json(JOB_MANIFEST_PATH)
    manifest["status"] = "hard_replacements_applied_to_board"
    manifest["applied_at"] = now
    manifest["applied_outputs"] = applied
    write_json(JOB_MANIFEST_PATH, manifest)


def write_report(applied: list[dict[str, Any]], asset_updates: dict[str, Any], now: str) -> None:
    report = {
        "schema_version": "reference003_identity_repair_r1_application_v1",
        "project_slug": "blue-water-citypop-op",
        "applied_at": now,
        "status": "hard_replacements_applied",
        "board": str(BOARD_PATH.relative_to(PROJECT_ROOT)),
        "asset_locks": str(ASSET_LOCKS_PATH.relative_to(PROJECT_ROOT)),
        "applied": applied,
        "asset_updates": asset_updates,
        "remaining_before_video": [
            "Run identity QA on OP_SHOT_018, OP_SHOT_019, OP_SHOT_020, OP_SHOT_023, OP_SHOT_032, OP_SHOT_033.",
            "Only assemble a new preview video after the image replacement pass is accepted.",
        ],
    }
    write_json(REPORT_JSON, report)
    lines = [
        "# Reference-003 Identity Repair R1 Application",
        "",
        f"- Applied at: `{now}`",
        "- Status: `hard_replacements_applied`",
        "",
        "| Item | New output | Size | Note |",
        "|---|---|---:|---|",
    ]
    for row in applied:
        lines.append(
            f"| `{row['item_id']}` | `{row['new_output_path']}` | {row['size']} | {REPLACEMENTS[row['item_id']]['decision']} |"
        )
    lines.extend(
        [
            "",
            "## Remaining Before Video",
            "",
            "- QA or regenerate high-risk continuity frames: `OP_SHOT_018`, `OP_SHOT_019`, `OP_SHOT_020`, `OP_SHOT_023`, `OP_SHOT_032`, `OP_SHOT_033`.",
            "- Assemble preview video only after this image pass is accepted.",
        ]
    )
    REPORT_MD.write_text("\n".join(lines) + "\n")


def main() -> int:
    now = datetime.now(TZ).isoformat(timespec="seconds")
    applied = apply_board(now)
    asset_updates = apply_asset_locks(now)
    update_job_manifest(applied, now)
    write_report(applied, asset_updates, now)
    print(
        json.dumps(
            {
                "status": "hard_replacements_applied",
                "applied": applied,
                "report_json": str(REPORT_JSON.relative_to(PROJECT_ROOT)),
                "report_md": str(REPORT_MD.relative_to(PROJECT_ROOT)),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
