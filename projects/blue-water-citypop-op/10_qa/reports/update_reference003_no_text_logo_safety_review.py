#!/usr/bin/env python3
"""Build and update the Reference-003 no-text/logo safety review.

This records the manual visual QA gate for readable text, titles, credits,
lyrics, NHK/broadcaster marks, subtitles, watermarks, and random symbols. It
does not infer a pass from prompts or prior intent; every media item must be
explicitly reviewed after its file exists.
"""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
REPORT_DIR = PROJECT_ROOT / "10_qa/reports"
REVIEW_JSON = REPORT_DIR / "reference003_no_text_logo_safety_review_20260630.json"
REVIEW_MD = REPORT_DIR / "reference003_no_text_logo_safety_review_20260630.md"
REVIEW_CSV = REPORT_DIR / "reference003_no_text_logo_safety_review_checklist_20260630.csv"
ROUGH_CUT = PROJECT_ROOT / "09_edit/rough_cut/reference003_full_op_roughcut_20260630.mp4"
ALLOWED_STATUS = {"pending", "pass", "needs_fix"}


def rel(path: str | Path) -> str:
    path = Path(path)
    if path.is_absolute():
        return str(path.relative_to(PROJECT_ROOT))
    return str(path)


def now_iso() -> str:
    return datetime.now(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()


def read_json(rel_path: str) -> Any:
    return json.loads((PROJECT_ROOT / rel_path).read_text(encoding="utf-8"))


def prior_reviews() -> dict[str, dict[str, Any]]:
    if not REVIEW_JSON.exists():
        return {}
    try:
        payload = json.loads(REVIEW_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return {item["item_key"]: item for item in payload.get("items", []) if item.get("item_key")}


def prior_created_at(default: str) -> str:
    if not REVIEW_JSON.exists():
        return default
    try:
        payload = json.loads(REVIEW_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return default
    return payload.get("created_at", default)


def review_defaults(item_key: str, prior: dict[str, dict[str, Any]], exists: bool) -> dict[str, str]:
    old = prior.get(item_key, {})
    status = old.get("review_status", "pending")
    if not exists and status == "pass":
        status = "pending"
    return {
        "review_status": status,
        "reviewed_at": old.get("reviewed_at", ""),
        "reviewer": old.get("reviewer", ""),
        "evidence_path": old.get("evidence_path", ""),
        "review_notes": old.get("review_notes", ""),
    }


def build_items(prior: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []

    board = read_json("03_story/idea_board/idea_board.json")
    for row in board["rows"]:
        item_id = row["item_id"]
        media_path = row.get("output_path", "")
        source_status = row.get("status", "")
        exists = (
            source_status == "generated_reference003_qa_pass"
            and bool(media_path)
            and (PROJECT_ROOT / media_path).is_file()
        )
        item_key = f"keyframe:{item_id}"
        items.append(
            {
                "item_key": item_key,
                "scope": "keyframe",
                "item_id": item_id,
                "title": row.get("title", ""),
                "media_path": media_path,
                "media_exists": exists,
                "source_status": source_status,
                "required_check": "No readable text/title/credit/logo/subtitle/watermark/random symbols in generated keyframe.",
                **review_defaults(item_key, prior, exists),
            }
        )

    segment_packet = read_json("00_admin/ai_bridge/packets/20260630_reference003_video_segment_execution.json")
    for unit in segment_packet["units"]:
        unit_id = unit["unit_id"]
        media_path = unit["expected_video_output_path"]
        exists = (PROJECT_ROOT / media_path).is_file()
        item_key = f"segment:{unit_id}"
        items.append(
            {
                "item_key": item_key,
                "scope": "segment",
                "item_id": unit_id,
                "title": unit.get("title", ""),
                "media_path": media_path,
                "media_exists": exists,
                "source_status": unit.get("generation_gate", ""),
                "required_check": "No readable text/title/credit/logo/subtitle/watermark/random symbols throughout generated segment.",
                **review_defaults(item_key, prior, exists),
            }
        )

    roughcut_exists = ROUGH_CUT.is_file()
    item_key = "roughcut:reference003_full_op"
    items.append(
        {
            "item_key": item_key,
            "scope": "roughcut",
            "item_id": "reference003_full_op_roughcut_20260630",
            "title": "full OP roughcut",
            "media_path": rel(ROUGH_CUT),
            "media_exists": roughcut_exists,
            "source_status": "final_roughcut",
            "required_check": "Full assembled OP contains no generated readable text, title, credit, logo, subtitle, watermark, or random symbols.",
            **review_defaults(item_key, prior, roughcut_exists),
        }
    )
    return items


def summarize(items: list[dict[str, Any]]) -> dict[str, Any]:
    by_scope: dict[str, dict[str, int]] = {}
    counts: dict[str, int] = {}
    effective_pass = 0
    for item in items:
        scope = item["scope"]
        status = item.get("review_status", "pending")
        counts[status] = counts.get(status, 0) + 1
        bucket = by_scope.setdefault(scope, {"total": 0, "exists": 0, "pass": 0, "needs_fix": 0, "pending": 0})
        bucket["total"] += 1
        if item["media_exists"]:
            bucket["exists"] += 1
        if status == "pass" and item["media_exists"]:
            bucket["pass"] += 1
            effective_pass += 1
        elif status == "needs_fix":
            bucket["needs_fix"] += 1
        else:
            bucket["pending"] += 1

    keyframes = by_scope.get("keyframe", {})
    segments = by_scope.get("segment", {})
    roughcut = by_scope.get("roughcut", {})
    completion_gate_pass = (
        keyframes.get("pass") == 42
        and segments.get("pass") == 21
        and roughcut.get("pass") == 1
    )
    return {
        "items_total": len(items),
        "items_existing": sum(1 for item in items if item["media_exists"]),
        "items_effective_pass": effective_pass,
        "counts_by_status": counts,
        "by_scope": by_scope,
        "completion_gate_pass": completion_gate_pass,
    }


def build_review() -> dict[str, Any]:
    prior = prior_reviews()
    items = build_items(prior)
    now = now_iso()
    summary = summarize(items)
    return {
        "schema_version": "reference003_no_text_logo_safety_review_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": prior_created_at(now),
        "last_updated": now,
        "status": "pass" if summary["completion_gate_pass"] else "manual_review_pending",
        "source_reference": "reference-003-full-op-2160p",
        "review_scope": {
            "keyframes": 42,
            "segments": 21,
            "roughcut": 1,
            "total_items": 64,
        },
        "summary": summary,
        "items": items,
        "boundary": "A pass requires explicit manual review of all 42 keyframes, all 21 generated segments, and the final roughcut after files exist.",
        "rebuild_script": rel(Path(__file__)),
    }


def write_json_and_md(review: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REVIEW_JSON.write_text(json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = [
        "# Reference-003 No-Text/Logo Safety Review",
        "",
        f"- Rebuilt: `{review['last_updated']}`",
        f"- Status: `{review['status']}`",
        f"- Completion gate pass: `{review['summary']['completion_gate_pass']}`",
        "",
        "## Summary",
        "",
    ]
    for key, value in review["summary"].items():
        if key != "by_scope":
            md.append(f"- `{key}`: `{value}`")
    md.append(f"- `by_scope`: `{review['summary']['by_scope']}`")
    md.extend(
        [
            "",
            "## Review Items",
            "",
            "| Item | Scope | Media | Exists | Status | Reviewer | Evidence | Notes |",
            "|---|---|---|---|---|---|---|---|",
        ]
    )
    for item in review["items"]:
        notes = str(item.get("review_notes", "")).replace("|", "/")
        md.append(
            f"| `{item['item_key']}` | {item['scope']} | `{item['media_path']}` | "
            f"{item['media_exists']} | `{item['review_status']}` | "
            f"{item.get('reviewer', '')} | `{item.get('evidence_path', '')}` | {notes} |"
        )
    md.extend(["", "## Boundary", "", review["boundary"]])
    REVIEW_MD.write_text("\n".join(md) + "\n", encoding="utf-8")


def export_csv(review: dict[str, Any], path: Path) -> None:
    fields = [
        "item_key",
        "scope",
        "item_id",
        "title",
        "media_path",
        "media_exists",
        "source_status",
        "review_status",
        "reviewed_at",
        "reviewer",
        "evidence_path",
        "review_notes",
        "required_check",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for item in review["items"]:
            writer.writerow({field: item.get(field, "") for field in fields})


def import_csv(review: dict[str, Any], path: Path) -> int:
    by_key = {item["item_key"]: item for item in review["items"]}
    updated = 0
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            item_key = row.get("item_key", "").strip()
            status = row.get("review_status", "").strip()
            if not item_key or item_key not in by_key:
                continue
            if status not in ALLOWED_STATUS:
                raise SystemExit(f"Invalid review_status for {item_key}: {status}")
            item = by_key[item_key]
            for field in ["review_status", "reviewed_at", "reviewer", "evidence_path", "review_notes"]:
                value = row.get(field, "").strip()
                if field == "reviewed_at" and status in {"pass", "needs_fix"} and not value:
                    value = now_iso()
                item[field] = value
            updated += 1
    review["last_updated"] = now_iso()
    review["summary"] = summarize(review["items"])
    review["status"] = "pass" if review["summary"]["completion_gate_pass"] else "manual_review_pending"
    return updated


def update_one(
    review: dict[str, Any],
    item_key: str,
    status: str,
    reviewer: str,
    evidence_path: str,
    notes: str,
) -> None:
    if status not in ALLOWED_STATUS:
        raise SystemExit(f"Invalid review_status: {status}")
    by_key = {item["item_key"]: item for item in review["items"]}
    if item_key not in by_key:
        raise SystemExit(f"Unknown item_key: {item_key}")
    item = by_key[item_key]
    item["review_status"] = status
    item["reviewed_at"] = now_iso() if status in {"pass", "needs_fix"} else ""
    item["reviewer"] = reviewer
    item["evidence_path"] = evidence_path
    item["review_notes"] = notes
    review["last_updated"] = now_iso()
    review["summary"] = summarize(review["items"])
    review["status"] = "pass" if review["summary"]["completion_gate_pass"] else "manual_review_pending"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Update Reference-003 no-text/logo safety review.")
    parser.add_argument("--refresh", action="store_true", help="Refresh the review file from current media state.")
    parser.add_argument("--list", action="store_true", help="Print current summary.")
    parser.add_argument("--export-csv", nargs="?", const=str(REVIEW_CSV), help="Export checklist CSV.")
    parser.add_argument("--import-csv", help="Import reviewed statuses from CSV.")
    parser.add_argument("--apply", action="store_true", help="Required for updates/imports.")
    parser.add_argument("--item", help="Item key, e.g. keyframe:OP_SHOT_001 or roughcut:reference003_full_op.")
    parser.add_argument("--status", choices=sorted(ALLOWED_STATUS), help="Review status for --item.")
    parser.add_argument("--reviewer", default="", help="Reviewer name or initials.")
    parser.add_argument("--evidence-path", default="", help="Path to the reviewed evidence.")
    parser.add_argument("--notes", default="", help="Short review notes.")
    parser.add_argument("--print-json", action="store_true", help="Print compact JSON summary.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    review = build_review()
    changed = bool(args.refresh)
    imported_count = 0
    csv_exported = ""

    if args.import_csv:
        if not args.apply:
            raise SystemExit("--apply is required with --import-csv")
        imported_count = import_csv(review, Path(args.import_csv))
        changed = True

    if args.item or args.status:
        if not (args.item and args.status):
            raise SystemExit("--item and --status must be used together")
        if not args.apply:
            raise SystemExit("--apply is required when updating an item")
        update_one(review, args.item, args.status, args.reviewer, args.evidence_path, args.notes)
        changed = True

    if changed or not REVIEW_JSON.exists():
        write_json_and_md(review)

    if args.export_csv is not None:
        export_path = Path(args.export_csv)
        if not export_path.is_absolute():
            export_path = PROJECT_ROOT / export_path
        export_csv(review, export_path)
        csv_exported = rel(export_path)

    result = {
        "changed": changed,
        "imported_count": imported_count,
        "csv_exported": csv_exported,
        "status": review["status"],
        "summary": review["summary"],
        "review_json": rel(REVIEW_JSON),
        "review_md": rel(REVIEW_MD),
    }
    if args.print_json or args.list or csv_exported or changed:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
