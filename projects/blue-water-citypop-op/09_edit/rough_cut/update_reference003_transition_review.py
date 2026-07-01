#!/usr/bin/env python3
"""Record Reference-003 transition review evidence.

Use this after generated segments or the roughcut have been visually reviewed.
It never marks transitions complete automatically; each pass/needs_fix status
must be supplied explicitly or imported from a reviewed CSV.
"""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ROUGH_DIR = PROJECT_ROOT / "09_edit/rough_cut"
REPORT_DIR = PROJECT_ROOT / "10_qa/reports"
AUDIT_JSON = ROUGH_DIR / "reference003_roughcut_transition_audit_template.json"
REPORT_JSON = REPORT_DIR / "reference003_roughcut_transition_audit_template_20260630.json"
REBUILD_SCRIPT = ROUGH_DIR / "rebuild_reference003_roughcut_transition_audit.py"
DEFAULT_CSV = ROUGH_DIR / "reference003_transition_review_checklist_20260630.csv"
ALLOWED_STATUS = {"pending", "pass", "reviewed", "needs_fix"}


def rel(path: str | Path) -> str:
    path = Path(path)
    if path.is_absolute():
        return str(path.relative_to(PROJECT_ROOT))
    return str(path)


def now_iso() -> str:
    return datetime.now(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()


def run_rebuild() -> None:
    result = subprocess.run(
        ["python3", str(REBUILD_SCRIPT)],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit((result.stderr or result.stdout or "rebuild failed").strip())


def load_audit() -> dict[str, Any]:
    if not AUDIT_JSON.exists():
        run_rebuild()
    return json.loads(AUDIT_JSON.read_text(encoding="utf-8"))


def write_audit(audit: dict[str, Any]) -> None:
    for path in [AUDIT_JSON, REPORT_JSON]:
        path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def edge_map(audit: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {edge["edge_id"]: edge for edge in audit.get("transition_edges", [])}


def summarize(audit: dict[str, Any]) -> dict[str, Any]:
    counts: dict[str, int] = {}
    for edge in audit.get("transition_edges", []):
        status = edge.get("review_status", "pending")
        counts[status] = counts.get(status, 0) + 1
    reviewed = sum(counts.get(status, 0) for status in ["pass", "reviewed"])
    return {
        "status": audit.get("status"),
        "transition_edges_total": len(audit.get("transition_edges", [])),
        "transition_edges_reviewed": reviewed,
        "counts": counts,
    }


def export_csv(audit: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "edge_id",
        "from",
        "to",
        "from_unit",
        "to_unit",
        "transition_type",
        "visual_bridge",
        "review_status",
        "reviewed_at",
        "reviewer",
        "evidence_path",
        "review_notes",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for edge in audit.get("transition_edges", []):
            writer.writerow({field: edge.get(field, "") for field in fields})


def import_csv(audit: dict[str, Any], path: Path) -> int:
    existing = edge_map(audit)
    updated = 0
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            edge_id = row.get("edge_id", "").strip()
            status = row.get("review_status", "").strip()
            if not edge_id or edge_id not in existing:
                continue
            if status not in ALLOWED_STATUS:
                raise SystemExit(f"Invalid review_status for {edge_id}: {status}")
            edge = existing[edge_id]
            for field in ["review_status", "reviewed_at", "reviewer", "evidence_path", "review_notes"]:
                value = row.get(field, "").strip()
                if field == "reviewed_at" and status in {"pass", "reviewed", "needs_fix"} and not value:
                    value = now_iso()
                edge[field] = value
            updated += 1
    return updated


def update_one(
    audit: dict[str, Any],
    edge_id: str,
    status: str,
    reviewer: str,
    evidence_path: str,
    notes: str,
) -> None:
    if status not in ALLOWED_STATUS:
        raise SystemExit(f"Invalid review_status: {status}")
    existing = edge_map(audit)
    if edge_id not in existing:
        raise SystemExit(f"Unknown edge_id: {edge_id}")
    edge = existing[edge_id]
    edge["review_status"] = status
    edge["reviewed_at"] = now_iso() if status in {"pass", "reviewed", "needs_fix"} else ""
    edge["reviewer"] = reviewer
    edge["evidence_path"] = evidence_path
    edge["review_notes"] = notes


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Record Reference-003 transition review evidence.")
    parser.add_argument("--list", action="store_true", help="Print compact transition status summary.")
    parser.add_argument("--export-csv", nargs="?", const=str(DEFAULT_CSV), help="Export review checklist CSV.")
    parser.add_argument("--import-csv", help="Import reviewed statuses from a CSV.")
    parser.add_argument("--apply", action="store_true", help="Required when changing audit state.")
    parser.add_argument("--edge", help="Transition edge id to update.")
    parser.add_argument("--status", choices=sorted(ALLOWED_STATUS), help="Review status for --edge.")
    parser.add_argument("--reviewer", default="", help="Reviewer name or initials.")
    parser.add_argument("--evidence-path", default="", help="Path to segment/roughcut evidence.")
    parser.add_argument("--notes", default="", help="Short review notes.")
    parser.add_argument("--print-json", action="store_true", help="Print JSON summary.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    audit = load_audit()
    changed = False
    csv_exported = ""
    imported_count = 0

    if args.import_csv:
        if not args.apply:
            raise SystemExit("--apply is required with --import-csv")
        imported_count = import_csv(audit, Path(args.import_csv))
        changed = True

    if args.edge or args.status:
        if not (args.edge and args.status):
            raise SystemExit("--edge and --status must be used together")
        if not args.apply:
            raise SystemExit("--apply is required when updating a transition")
        update_one(audit, args.edge, args.status, args.reviewer, args.evidence_path, args.notes)
        changed = True

    if changed:
        write_audit(audit)
        run_rebuild()
        audit = load_audit()

    if args.export_csv is not None:
        export_path = Path(args.export_csv)
        if not export_path.is_absolute():
            export_path = PROJECT_ROOT / export_path
        export_csv(audit, export_path)
        csv_exported = rel(export_path)

    summary = summarize(audit)
    result = {
        "changed": changed,
        "imported_count": imported_count,
        "csv_exported": csv_exported,
        "summary": summary,
        "audit_json": rel(AUDIT_JSON),
        "report_json": rel(REPORT_JSON),
    }
    if args.print_json or args.list or csv_exported or changed:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
