#!/usr/bin/env python3
"""Validate a standardized AIGC film project folder."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from create_aigc_project import DIRECTORIES, TEXT_TEMPLATES


SHOT_LIST_COLUMNS = [
    "shot_id",
    "sequence",
    "story_beat",
    "duration_sec",
    "aspect_ratio",
    "location",
    "character_stage_lock",
    "start_frame",
    "end_frame",
    "camera",
    "action",
    "lighting",
    "continuity_lock",
    "prompt_path",
    "status",
]


def add(result: list[dict[str, str]], check: str, status: str, notes: str = "") -> None:
    result.append({"check": check, "status": status, "notes": notes})


def validate_project(project_path: Path) -> list[dict[str, str]]:
    root = project_path.expanduser().resolve()
    result: list[dict[str, str]] = []

    add(result, "project_folder_exists", "pass" if root.exists() else "fail", str(root))
    if not root.exists():
        return result

    missing_dirs = [directory for directory in DIRECTORIES if not (root / directory).is_dir()]
    add(
        result,
        "required_directories",
        "pass" if not missing_dirs else "fail",
        ";".join(missing_dirs),
    )

    required_files = sorted(TEXT_TEMPLATES)
    missing_files = [file for file in required_files if not (root / file).is_file()]
    add(
        result,
        "required_files",
        "pass" if not missing_files else "fail",
        ";".join(missing_files),
    )

    rar_files = sorted(str(path.relative_to(root)) for path in root.rglob("*.rar"))
    add(result, "rar_exclusion", "pass" if not rar_files else "fail", ";".join(rar_files))

    shot_list = root / "07_shots" / "shot_list.csv"
    if shot_list.exists():
        with shot_list.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.reader(handle)
            header = next(reader, [])
        missing_columns = [column for column in SHOT_LIST_COLUMNS if column not in header]
        add(
            result,
            "shot_list_schema",
            "pass" if not missing_columns else "fail",
            "missing=" + ";".join(missing_columns) if missing_columns else "",
        )
    else:
        add(result, "shot_list_schema", "fail", "missing 07_shots/shot_list.csv")

    project_manifest = root / "project.yaml"
    manifest_text = project_manifest.read_text(encoding="utf-8") if project_manifest.exists() else ""
    add(
        result,
        "project_manifest_contract",
        "pass"
        if "gui_contract:" in manifest_text and "stage_order:" in manifest_text and "audit_report:" in manifest_text
        else "fail",
        "requires gui_contract, stage_order, and audit_report",
    )

    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate an AIGC project folder.")
    parser.add_argument("project_path", help="Path to projects/<slug>")
    parser.add_argument("--print-json", action="store_true", help="Print JSON result.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = validate_project(Path(args.project_path))
    failed = [row for row in result if row["status"] == "fail"]

    if args.print_json:
        print(json.dumps({"status": "fail" if failed else "pass", "checks": result}, ensure_ascii=False, indent=2))
    else:
        print(f"project_status={'fail' if failed else 'pass'}")
        for row in result:
            suffix = f" {row['notes']}" if row["notes"] else ""
            print(f"{row['status']}: {row['check']}{suffix}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
