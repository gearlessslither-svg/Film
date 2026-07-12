#!/usr/bin/env python3
"""Select AIGC film project-memory lessons."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "references" / "lesson-index.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--area", help="Filter by workflow_area")
    parser.add_argument("--project", help="Filter by project_slug")
    parser.add_argument("--status", help="Filter by status")
    parser.add_argument("--hard", action="store_true", help="Show hard rules only")
    args = parser.parse_args()

    data = json.loads(INDEX.read_text(encoding="utf-8"))
    lessons = data.get("lessons", [])
    if args.area:
        lessons = [row for row in lessons if row.get("workflow_area") == args.area]
    if args.project:
        lessons = [row for row in lessons if row.get("project_slug") == args.project]
    if args.status:
        lessons = [row for row in lessons if row.get("status") == args.status]
    if args.hard:
        lessons = [row for row in lessons if row.get("hard_rule") is True and row.get("status") == "active"]

    print(f"lesson_count={len(lessons)}")
    for row in lessons:
        hard = " HARD" if row.get("hard_rule") else ""
        print(f"- {row['lesson_id']} [{row.get('status')}/{row.get('reliability')}{hard}]")
        print(f"  {row.get('claim', '')}")
        print(f"  Do: {row.get('recommendation', '')}")


if __name__ == "__main__":
    main()
