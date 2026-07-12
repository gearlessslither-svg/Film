#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

IMAGE_TAGS = [
    "[STYLE_FINGERPRINT]", "[SUBJECT_AND_ACTION]", "[CAMERA_AND_COMPOSITION]",
    "[LIGHTING]", "[SPACE_AND_CONTINUITY]", "[NEGATIVE]",
]
VIDEO_TAGS = [
    "[STYLE_FINGERPRINT]", "[STYLE_INHERITANCE_HARD_LOCK]", "[STYLE_NEGATIVE]",
    "[DURATION]", "[DURATION_RATIONALE]", "[TIMELINE]", "[CONTINUITY_LOCKS]",
    "[NEGATIVE]", "[AUDIO]",
]
DURATION_RE = re.compile(r"\[DURATION\]\s*([0-9]+(?:\.[0-9]+)?)s")
RANGE_RE = re.compile(r"(?m)^([0-9]+(?:\.[0-9]+)?)–([0-9]+(?:\.[0-9]+)?)s:\s*(.+)$")


def rows_from(payload):
    rows = payload.get("rows", []) if isinstance(payload, dict) else []
    return [row for row in rows if isinstance(row, dict)]


def main():
    if len(sys.argv) != 2:
        print("usage: validate_prompt_contract.py <board-or-manifest.json>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1]).expanduser().resolve()
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = rows_from(payload)
    errors = []
    for index, row in enumerate(rows, 1):
        item_id = str(row.get("item_id") or f"row-{index}")
        image_prompt = str(row.get("image_prompt") or "")
        video_prompt = str(row.get("video_prompt") or "")
        for tag in IMAGE_TAGS:
            if tag not in image_prompt:
                errors.append(f"{item_id}: image prompt missing {tag}")
        for tag in VIDEO_TAGS:
            if tag not in video_prompt:
                errors.append(f"{item_id}: video prompt missing {tag}")
        duration_match = DURATION_RE.search(video_prompt)
        ranges = [(float(a), float(b), text) for a, b, text in RANGE_RE.findall(video_prompt)]
        if not duration_match:
            continue
        duration = float(duration_match.group(1))
        if not ranges:
            errors.append(f"{item_id}: no time ranges")
            continue
        if abs(ranges[0][0]) > 1e-6:
            errors.append(f"{item_id}: timeline does not start at 0.0s")
        if abs(ranges[-1][1] - duration) > 1e-6:
            errors.append(f"{item_id}: timeline ends at {ranges[-1][1]}s, expected {duration}s")
        for number, (start, end, text) in enumerate(ranges):
            if end <= start:
                errors.append(f"{item_id}: invalid range {start}–{end}s")
            if number and abs(ranges[number - 1][1] - start) > 1e-6:
                errors.append(f"{item_id}: gap or overlap before {start}s")
            if "表演" not in text or "摄影" not in text:
                errors.append(f"{item_id}: {start}–{end}s must specify both performance and camera")
    result = {"ok": not errors, "rows": len(rows), "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
