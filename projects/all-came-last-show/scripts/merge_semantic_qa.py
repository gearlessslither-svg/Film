#!/usr/bin/env python3
"""Merge the three batch semantic reviews and enforce exact 42-frame coverage."""

from __future__ import annotations

import json
from pathlib import Path


def expected_items() -> list[str]:
    items = [f"SH{index:02d}" for index in range(1, 28)]
    items += ["SH28_KF01", "SH28_KF02"]
    items += [f"SH{index:02d}" for index in range(29, 35)]
    items += ["SH35_KF01", "SH35_KF02", "SH35_KF03", "SH36", "SH37", "SH38_KF01", "SH38_KF02"]
    return items


def records_from(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = payload if isinstance(payload, list) else payload.get("records", payload.get("items", []))
    if not isinstance(records, list):
        raise ValueError(f"{path}: records must be a list")
    return [row for row in records if isinstance(row, dict)]


def main() -> int:
    project = Path(__file__).resolve().parents[1]
    qa = project / "08_generation/jobs/final_frames_v2/qa"
    sources = [
        qa / "batch_SH01_SH13_semantic.json",
        qa / "batch_SH14_SH26_semantic.json",
        qa / "batch_SH27_SH38_semantic.json",
    ]
    records: list[dict] = []
    for source in sources:
        if not source.is_file():
            raise ValueError(f"missing batch semantic report: {source}")
        records.extend(records_from(source))
    by_id: dict[str, dict] = {}
    duplicates: list[str] = []
    for record in records:
        item_id = str(record.get("item_id", ""))
        if not item_id:
            raise ValueError("semantic QA record missing item_id")
        if item_id in by_id:
            duplicates.append(item_id)
        by_id[item_id] = record
    expected = expected_items()
    missing = [item for item in expected if item not in by_id]
    extra = sorted(set(by_id) - set(expected))
    if duplicates or missing or extra:
        raise ValueError(f"semantic coverage mismatch; duplicates={duplicates}, missing={missing}, extra={extra}")
    ordered = [by_id[item] for item in expected]
    non_pass = [row["item_id"] for row in ordered if row.get("status") != "pass"]
    result = {
        "ok": not non_pass,
        "count": len(ordered),
        "counts": {
            "pass": sum(row.get("status") == "pass" for row in ordered),
            "fail": len(non_pass),
        },
        "non_pass": non_pass,
        "sources": [str(source) for source in sources],
        "records": ordered,
    }
    output = qa / "final_semantic_qa.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": result["ok"], "count": result["count"], "non_pass": non_pass, "output": str(output)}, ensure_ascii=False))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
