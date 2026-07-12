#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


IMAGE_MARKERS = (
    "[STYLE_FINGERPRINT]",
    "[NARRATIVE_TIME]",
    "[CHARACTER_STATE_LOCK]",
    "[STATE_TRANSITION_RULE]",
)
VIDEO_MARKERS = (
    "[STYLE_FINGERPRINT]",
    "[STYLE_INHERITANCE_HARD_LOCK]",
    "[STYLE_NEGATIVE]",
    "[NARRATIVE_TIME]",
    "[CHARACTER_STATE_LOCK]",
    "[STATE_TRANSITION_RULE]",
    "[DURATION]",
    "[DURATION_RATIONALE]",
    "[TIMELINE]",
    "[CONTINUITY_LOCKS]",
    "[NEGATIVE]",
    "[AUDIO]",
)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("board")
    ap.add_argument("--project-root")
    args = ap.parse_args()
    board_path = Path(args.board).expanduser().resolve()
    board = json.loads(board_path.read_text(encoding="utf-8"))
    project_root = Path(args.project_root).expanduser().resolve() if args.project_root else board_path.parents[2]
    ledger_rel = str(board.get("character_state_ledger", "") or "")
    errors: list[str] = []
    if not ledger_rel:
        errors.append("board missing character_state_ledger")
        ledger = {}
    else:
        ledger_path = project_root / ledger_rel
        if not ledger_path.is_file():
            errors.append(f"ledger path missing: {ledger_rel}")
            ledger = {}
        else:
            ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    states = ledger.get("character_states", {}) if isinstance(ledger, dict) else {}
    bindings = ledger.get("shot_bindings", {}) if isinstance(ledger, dict) else {}
    rows = [r for r in board.get("rows", []) if isinstance(r, dict)]
    for row in rows:
        item = str(row.get("item_id", "") or "<missing-item-id>")
        phase = str(row.get("timeline_phase", "") or "")
        ids = row.get("character_state_ids", [])
        transition = str(row.get("state_transition_rule", "") or "")
        if not phase:
            errors.append(f"{item}: missing timeline_phase")
        if not isinstance(ids, list) or not ids:
            errors.append(f"{item}: missing character_state_ids")
            ids = []
        for state_id in ids:
            if state_id not in states:
                errors.append(f"{item}: unknown state id {state_id}")
        if not transition:
            errors.append(f"{item}: missing state_transition_rule")
        binding = bindings.get(item, {}) if isinstance(bindings, dict) else {}
        if binding and (binding.get("timeline_phase") != phase or binding.get("character_state_ids") != ids):
            errors.append(f"{item}: board/ledger state binding mismatch")
        image_prompt = str(row.get("image_prompt", "") or "")
        video_prompt = str(row.get("video_prompt", "") or "")
        for marker in IMAGE_MARKERS:
            if marker not in image_prompt:
                errors.append(f"{item}: image prompt missing {marker}")
        for marker in VIDEO_MARKERS:
            if marker not in video_prompt:
                errors.append(f"{item}: video prompt missing {marker}")
        for state_id in ids:
            if state_id not in image_prompt or state_id not in video_prompt:
                errors.append(f"{item}: prompts do not name bound state {state_id}")
        for version in row.get("versions", []):
            if not isinstance(version, dict):
                continue
            vid = str(version.get("version_id", "") or "version")
            if version.get("timeline_phase") != phase or version.get("character_state_ids") != ids:
                errors.append(f"{item}/{vid}: version state differs from card state")
            vp = str(version.get("video_prompt", "") or "")
            for marker in VIDEO_MARKERS:
                if marker not in vp:
                    errors.append(f"{item}/{vid}: version video prompt missing {marker}")
        group = str(row.get("multi_keyframe_shot_id", "") or "")
        if group:
            order = row.get("keyframe_order")
            sheet = str(row.get("storyboard_sheet_path", "") or "")
            if not isinstance(order, int) or order < 1:
                errors.append(f"{item}: invalid keyframe_order")
            if not sheet or not (project_root / sheet).is_file():
                errors.append(f"{item}: storyboard sheet missing: {sheet}")
            for marker in ("[SHOT_ID]", "[KEYFRAME_SEQUENCE]", "[TRANSITIONS]", "[STORYBOARD_SHEET]"):
                if marker not in video_prompt:
                    errors.append(f"{item}: multi-keyframe prompt missing {marker}")
    report = {
        "ok": not errors,
        "rows": len(rows),
        "versions": sum(len(r.get("versions", [])) for r in rows),
        "states": len(states),
        "errors": errors,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
