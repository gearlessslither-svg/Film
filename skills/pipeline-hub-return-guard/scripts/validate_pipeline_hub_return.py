#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def fail(message, errors):
    errors.append(message)


def main():
    if len(sys.argv) != 2:
        print("usage: validate_pipeline_hub_return.py <project-root>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).expanduser().resolve()
    board_path = root / "03_story" / "idea_board" / "idea_board.json"
    if not board_path.is_file():
        print(json.dumps({"ok": False, "errors": [f"missing board: {board_path}"]}, ensure_ascii=False))
        return 1
    try:
        board = json.loads(board_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "errors": [f"invalid board: {exc}"]}, ensure_ascii=False))
        return 1

    errors = []
    acts = board.get("acts", [])
    rows = board.get("rows", [])
    if not isinstance(acts, list) or not acts:
        fail("acts is empty", errors)
        acts = []
    if not isinstance(rows, list) or not rows:
        fail("rows is empty", errors)
        rows = []
    act_ids = {str(a.get("act_id", "")).strip() for a in acts if isinstance(a, dict)}
    card_uids, item_ids, missing_paths = set(), set(), []
    prompt_count = version_count = 0

    def check_path(raw, label):
        value = str(raw or "").strip()
        if not value:
            fail(f"{label}: empty output_path", errors)
            return
        path = Path(value)
        if path.is_absolute() or ".." in path.parts:
            fail(f"{label}: output_path must be project-relative: {value}", errors)
            return
        if not (root / path).is_file():
            missing_paths.append(value)

    for index, row in enumerate(rows, 1):
        if not isinstance(row, dict):
            fail(f"row {index}: not an object", errors)
            continue
        item_id = str(row.get("item_id", "")).strip()
        card_uid = str(row.get("card_uid", "")).strip()
        label = item_id or f"row {index}"
        if not item_id or item_id in item_ids:
            fail(f"{label}: missing or duplicate item_id", errors)
        item_ids.add(item_id)
        if not card_uid or card_uid in card_uids:
            fail(f"{label}: missing or duplicate card_uid", errors)
        card_uids.add(card_uid)
        act_id = str(row.get("act_id", "")).strip()
        if not act_id or act_id not in act_ids:
            fail(f"{label}: undeclared act_id {act_id!r}", errors)
        if not str(row.get("scene_id", "")).strip():
            fail(f"{label}: empty scene_id", errors)
        if str(row.get("video_prompt", "")).strip():
            prompt_count += 1
        else:
            fail(f"{label}: empty video_prompt", errors)
        check_path(row.get("output_path"), label)
        versions = row.get("versions", [])
        if not isinstance(versions, list) or not versions:
            fail(f"{label}: no versions", errors)
            continue
        for version in versions:
            if not isinstance(version, dict):
                fail(f"{label}: invalid version", errors)
                continue
            version_count += 1
            check_path(version.get("output_path"), f"{label}/{version.get('version_id', 'version')}")

    if missing_paths:
        fail(f"missing image paths: {len(set(missing_paths))}", errors)
    result = {
        "ok": not errors,
        "act_count": len(acts),
        "card_count": len(rows),
        "version_count": version_count,
        "video_prompt_coverage": f"{prompt_count}/{len(rows)}",
        "missing_path_count": len(set(missing_paths)),
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
