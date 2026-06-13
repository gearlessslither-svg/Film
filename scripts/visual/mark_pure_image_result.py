#!/usr/bin/env python3
"""Mark one generated pure image in queue, QA, and dual-version tables."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path

from PIL import Image


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str] | None = None) -> None:
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def image_ok(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, "missing"
    try:
        with Image.open(path) as img:
            w, h = img.size
        if w < 1200 or h < 675:
            return False, f"small_dimensions_{w}x{h}"
        ratio = w / h
        if abs(ratio - (16 / 9)) > 0.03:
            return False, f"bad_aspect_{w}x{h}"
        return True, f"{w}x{h}"
    except Exception as exc:
        return False, f"open_failed_{exc}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--asset-id", required=True)
    parser.add_argument("--status", choices=["passed", "needs_regeneration"], default="passed")
    parser.add_argument("--issue", default="")
    parser.add_argument("--root-cause", default="")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    queue_path = root / "exports/real_image_generation_queue.csv"
    qa_path = root / "exports/visual_asset_qa_checklist.csv"
    dual_path = root / "exports/visual_asset_dual_version_plan.csv"
    issue_path = root / "exports/visual_asset_issue_log.csv"

    queue = read_csv(queue_path)
    qa = read_csv(qa_path)
    dual = read_csv(dual_path)
    issues = read_csv(issue_path) if issue_path.exists() else []
    panels_path = root / "19_micro_storyboard_188_panels.csv"
    panel_map = {r["panel_id"]: r for r in read_csv(panels_path)} if panels_path.exists() else {}

    queue_row = next((r for r in queue if r["panel_id"] == args.asset_id), None)
    if not queue_row:
        raise SystemExit(f"missing queue asset {args.asset_id}")
    pure_path = root / queue_row["pure_path"]
    annotated_path = root / queue_row["annotated_path"]
    ok, detail = image_ok(pure_path)
    passed = args.status == "passed" and ok and annotated_path.exists()

    queue_row["status"] = "generated_passed_qa" if passed else "generated_needs_regeneration"
    queue_row["notes"] = (
        f"pure generated and QA passed; image={detail}; annotated_exists={annotated_path.exists()}"
        if passed
        else f"pure generated but needs regeneration/review; image={detail}; issue={args.issue}"
    )

    for row in qa:
        if row.get("asset_id") == args.asset_id:
            row["pure_exists"] = "yes" if pure_path.exists() else "no"
            row["no_text_or_labels"] = "yes" if passed else "review"
            is_environment = panel_map.get(args.asset_id, {}).get("character_focus") == "环境"
            row["identity_ok"] = "not_applicable_environment" if is_environment else ("yes" if passed else "review")
            row["space_ok"] = "yes" if passed else "review"
            row["lighting_ok"] = "yes" if passed else "review"
            row["whitebox_ok"] = "yes" if passed else "review"
            row["overall_status"] = "pass" if passed else "needs_regeneration"
            row["issue_summary"] = "" if passed else args.issue
            row["root_cause"] = "" if passed else args.root_cause
            row["replacement_needed"] = "no" if passed else "yes"
            row["replacement_path"] = "" if passed else row.get("pure_path", "")
            break

    for row in dual:
        if row.get("asset_id") == args.asset_id:
            row["status"] = "pure_and_annotated_ready" if passed else "pure_needs_regeneration"
            break

    if not passed:
        issue_id = f"VIS_ISSUE_{len(issues)+1:03d}"
        issues.append(
            {
                "issue_id": issue_id,
                "asset_id": args.asset_id,
                "detected_time": datetime.now().isoformat(timespec="seconds"),
                "issue_type": "pure_image_qa",
                "symptom": args.issue or detail,
                "root_cause": args.root_cause,
                "fix_action": "regenerate from clean prompt and whitebox reference",
                "old_path": queue_row["pure_path"],
                "new_path": "",
                "status": "open",
            }
        )

    write_csv(queue_path, queue)
    write_csv(qa_path, qa)
    write_csv(dual_path, dual)
    if issues:
        write_csv(
            issue_path,
            issues,
            [
                "issue_id",
                "asset_id",
                "detected_time",
                "issue_type",
                "symptom",
                "root_cause",
                "fix_action",
                "old_path",
                "new_path",
                "status",
            ],
        )

    print(f"asset_id={args.asset_id}")
    print(f"passed={passed}")
    print(f"image_detail={detail}")
    print(f"queue_status={queue_row['status']}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
