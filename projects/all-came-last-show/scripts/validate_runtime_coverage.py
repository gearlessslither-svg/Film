#!/usr/bin/env python3
"""Validate that the idea board truly covers 120 seconds with 38 shots/42 sources."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


EXPECTED_MULTI = {"SH28": 2, "SH35": 3, "SH38": 2}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--require-images", action="store_true")
    args = parser.parse_args()
    project = Path(args.project_root).expanduser().resolve()
    board_path = project / "03_story/idea_board/idea_board.json"
    board = json.loads(board_path.read_text(encoding="utf-8"))
    rows = [row for row in board.get("rows", []) if isinstance(row, dict)]
    errors: list[str] = []
    if len(rows) != 42:
        errors.append(f"expected 42 keyframe rows, found {len(rows)}")
    item_ids = [str(row.get("item_id", "")) for row in rows]
    if len(set(item_ids)) != len(item_ids):
        errors.append("duplicate item_id in board")
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("shot_id", ""))].append(row)
        if args.require_images:
            path = project / str(row.get("selected_image_path", ""))
            if not path.is_file():
                errors.append(f"{row.get('item_id')}: selected image missing")
    if len(grouped) != 38:
        errors.append(f"expected 38 shots, found {len(grouped)}")
    shots = []
    for shot_id, shot_rows in grouped.items():
        starts = {row.get("timeline_start_seconds") for row in shot_rows}
        ends = {row.get("timeline_end_seconds") for row in shot_rows}
        durations = {row.get("duration_seconds") for row in shot_rows}
        if len(starts) != 1 or len(ends) != 1 or len(durations) != 1:
            errors.append(f"{shot_id}: keyframe rows disagree on timing")
            continue
        start, end, duration = starts.pop(), ends.pop(), durations.pop()
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            errors.append(f"{shot_id}: invalid timing")
            continue
        if abs((end - start) - duration) > 1e-6:
            errors.append(f"{shot_id}: duration does not equal end-start")
        expected_sources = EXPECTED_MULTI.get(shot_id, 1)
        if len(shot_rows) != expected_sources:
            errors.append(f"{shot_id}: expected {expected_sources} source images, found {len(shot_rows)}")
        if duration > 4 and len(shot_rows) == 1:
            errors.append(f"{shot_id}: unsupported single-source hold {duration}s")
        shots.append({"shot_id": shot_id, "start": start, "end": end, "duration": duration, "sources": len(shot_rows)})
    shots.sort(key=lambda shot: shot["start"])
    cursor = 0.0
    for shot in shots:
        if abs(shot["start"] - cursor) > 1e-6:
            errors.append(f"gap or overlap before {shot['shot_id']}: cursor={cursor}, start={shot['start']}")
        cursor = shot["end"]
    if abs(cursor - 120.0) > 1e-6:
        errors.append(f"timeline ends at {cursor}s, expected 120s")
    durations = [shot["duration"] for shot in shots]
    ordered = sorted(durations)
    median = (ordered[18] + ordered[19]) / 2 if len(ordered) == 38 else None
    result = {
        "ok": not errors,
        "runtime_seconds": cursor,
        "shot_count": len(shots),
        "keyframe_count": len(rows),
        "mean_shot_duration_seconds": round(sum(durations) / len(durations), 3) if durations else 0,
        "median_shot_duration_seconds": median,
        "longest_shot_seconds": max(durations) if durations else 0,
        "longest_single_source_hold_seconds": max((shot["duration"] for shot in shots if shot["sources"] == 1), default=0),
        "multi_keyframe_shots": {shot["shot_id"]: shot["sources"] for shot in shots if shot["sources"] > 1},
        "require_images": args.require_images,
        "errors": errors,
        "shots": shots,
    }
    output = project / "10_qa/runtime_coverage_qa.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("ok", "runtime_seconds", "shot_count", "keyframe_count", "mean_shot_duration_seconds", "median_shot_duration_seconds", "longest_single_source_hold_seconds", "errors")}, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
