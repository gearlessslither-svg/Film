#!/usr/bin/env python3
"""Build the production idea board from the three approved-format prompt packages."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SHOT_TIMES = {
    "SH01": (0, 4), "SH02": (4, 7), "SH03": (7, 10), "SH04": (10, 13),
    "SH05": (13, 16), "SH06": (16, 19), "SH07": (19, 21), "SH08": (21, 24),
    "SH09": (24, 28), "SH10": (28, 32), "SH11": (32, 35), "SH12": (35, 38),
    "SH13": (38, 42), "SH14": (42, 46), "SH15": (46, 50), "SH16": (50, 53),
    "SH17": (53, 56), "SH18": (56, 59), "SH19": (59, 62), "SH20": (62, 66),
    "SH21": (66, 69), "SH22": (69, 72), "SH23": (72, 75), "SH24": (75, 78),
    "SH25": (78, 81), "SH26": (81, 84), "SH27": (84, 88), "SH28": (88, 91),
    "SH29": (91, 94), "SH30": (94, 96), "SH31": (96, 99), "SH32": (99, 102),
    "SH33": (102, 104), "SH34": (104, 107), "SH35": (107, 112),
    "SH36": (112, 115), "SH37": (115, 117), "SH38": (117, 120),
}

PROMPT_PACKAGES = (
    "07_shots/prompt_packages_v2/SH01_SH13_PRODUCTION_PROMPTS.md",
    "07_shots/prompt_packages_v2/SH14_SH26_PRODUCTION_PROMPTS.md",
    "07_shots/prompt_packages_v2/SH27_SH38_PRODUCTION_PROMPTS.md",
)

SECTION_RE = re.compile(r"(?ms)^## (SH\d+)\b([^\n]*)\n(.*?)(?=^## SH\d+\b|\Z)")
HEADING_RE = re.compile(r"(?m)^###\s+(.+?)\s*$")
IMAGE_HEADING_RE = re.compile(r"^(?:AIGC\s+)?IMAGE PROMPT(?:\s*[—-]\s*([A-Z0-9_]+).*)?$")
VIDEO_HEADING_RE = re.compile(r"^AIGC IMAGE-TO-VIDEO PROMPT(?:\s*[—-]\s*([A-Z0-9_]+).*)?$")


def timecode(seconds: int) -> str:
    return f"{seconds // 60:02d}:{seconds % 60:02d}"


def act_for(shot_number: int) -> str:
    if shot_number <= 13:
        return "ACT01"
    if shot_number <= 30:
        return "ACT02"
    return "ACT03"


def clean_prompt_block(value: str) -> str:
    value = value.strip()
    if value.startswith("```text"):
        value = value[len("```text"):].lstrip("\r\n")
    elif value.startswith("```"):
        value = value[len("```"):].lstrip("\r\n")
    if value.endswith("```"):
        value = value[:-3].rstrip()
    if value.endswith("---"):
        value = value[:-3].rstrip()
    return value


def prompt_blocks(body: str) -> tuple[list[tuple[str | None, str]], list[tuple[str | None, str]]]:
    headings = list(HEADING_RE.finditer(body))
    images: list[tuple[str | None, str]] = []
    videos: list[tuple[str | None, str]] = []
    for index, heading in enumerate(headings):
        label = heading.group(1).strip()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
        content = clean_prompt_block(body[heading.end():end])
        image_match = IMAGE_HEADING_RE.fullmatch(label)
        video_match = VIDEO_HEADING_RE.fullmatch(label)
        if image_match:
            images.append((image_match.group(1), content))
        elif video_match:
            videos.append((video_match.group(1), content))
    return images, videos


def parse_packages(root: Path) -> dict[str, dict]:
    shots: dict[str, dict] = {}
    for rel in PROMPT_PACKAGES:
        path = root / rel
        text = path.read_text(encoding="utf-8")
        for shot_match in SECTION_RE.finditer(text):
            shot_id, heading_tail, body = shot_match.groups()
            image_blocks, video_blocks = prompt_blocks(body)
            if not image_blocks:
                raise ValueError(f"{shot_id}: no IMAGE PROMPT block in {rel}")
            if len(video_blocks) != 1:
                raise ValueError(f"{shot_id}: expected one VIDEO PROMPT block, found {len(video_blocks)}")
            items = []
            for explicit_id, image_prompt in image_blocks:
                if explicit_id:
                    item_id = explicit_id
                elif len(image_blocks) == 1:
                    item_id = shot_id
                else:
                    raise ValueError(f"{shot_id}: multi-keyframe image prompt lacks explicit keyframe id")
                items.append({"item_id": item_id, "image_prompt": image_prompt})
            title = heading_tail.lstrip("｜ |-").strip()
            shots[shot_id] = {
                "shot_id": shot_id,
                "title": title,
                "source_prompt_package": rel,
                "video_prompt": video_blocks[0][1],
                "items": items,
            }
    missing = sorted(set(SHOT_TIMES) - set(shots))
    extra = sorted(set(shots) - set(SHOT_TIMES))
    if missing or extra:
        raise ValueError(f"shot package mismatch; missing={missing}, extra={extra}")
    return shots


def build_board(root: Path) -> dict:
    ledger_rel = "05_asset_bible/CHARACTER_STATE_LEDGER_V2.json"
    ledger = json.loads((root / ledger_rel).read_text(encoding="utf-8"))
    bindings = ledger["shot_bindings"]
    shots = parse_packages(root)
    rows = []
    for shot_id in sorted(shots, key=lambda value: int(value[2:])):
        shot_number = int(shot_id[2:])
        start, end = SHOT_TIMES[shot_id]
        shot = shots[shot_id]
        for index, item in enumerate(shot["items"], 1):
            item_id = item["item_id"]
            binding = bindings.get(item_id)
            if not binding:
                raise ValueError(f"{item_id}: missing state binding")
            multi = len(shot["items"]) > 1
            selected_rel = f"08_generation/jobs/final_frames_v2/selected/{item_id}.png"
            selected_exists = (root / selected_rel).is_file()
            sheet_rel = (
                f"08_generation/jobs/final_frames_v2/storyboard_sheets/{shot_id}_NUMBERED_SHEET.png"
                if multi else ""
            )
            row = {
                "card_type": "storyboard",
                "card_uid": f"ALS-{item_id}",
                "item_id": item_id,
                "shot_id": shot_id,
                "act_id": act_for(shot_number),
                "title": shot["title"],
                "timeline_start_seconds": start,
                "timeline_end_seconds": end,
                "timeline_timecode": f"{timecode(start)}–{timecode(end)}",
                "duration_seconds": end - start,
                "timeline_phase": binding["timeline_phase"],
                "character_state_ids": binding["character_state_ids"],
                "state_transition_rule": binding["state_transition_rule"],
                "image_prompt": item["image_prompt"],
                "video_prompt": shot["video_prompt"],
                "source_prompt_package": shot["source_prompt_package"],
                "selected_image_path": selected_rel,
                "production_status": "selected_candidate" if selected_exists else "generation_pending",
                "director_approval_status": "pending",
                "versions": [
                    {
                        "version_id": "v2_production_candidate",
                        "timeline_phase": binding["timeline_phase"],
                        "character_state_ids": binding["character_state_ids"],
                        "video_prompt": shot["video_prompt"],
                        "image_path": selected_rel,
                        "status": "selected_candidate" if selected_exists else "generation_pending",
                    }
                ],
            }
            if multi:
                row.update({
                    "multi_keyframe_shot_id": shot_id,
                    "keyframe_order": index,
                    "keyframe_count": len(shot["items"]),
                    "storyboard_sheet_path": sheet_rel,
                })
            rows.append(row)
    if len(rows) != 42:
        raise ValueError(f"expected 42 keyframe rows, found {len(rows)}")
    return {
        "schema_version": "2.0",
        "project": "all-came-last-show",
        "active_branch": "DFT_MASTERPLAN_WILD_RETURN_V4",
        "runtime_seconds": 120,
        "shot_count": 38,
        "keyframe_count": 42,
        "frame_spec": {"aspect_ratio": "21:9", "width": 1915, "height": 821, "format": "PNG"},
        "character_state_ledger": ledger_rel,
        "prompt_packages": list(PROMPT_PACKAGES),
        "director_approval_status": "pending",
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--output", default="03_story/idea_board/idea_board.json")
    args = parser.parse_args()
    root = Path(args.project_root).expanduser().resolve()
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    board = build_board(root)
    output.write_text(json.dumps(board, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    selected = sum(row["production_status"] == "selected_candidate" for row in board["rows"])
    print(json.dumps({"ok": True, "rows": len(board["rows"]), "selected": selected, "output": str(output)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
