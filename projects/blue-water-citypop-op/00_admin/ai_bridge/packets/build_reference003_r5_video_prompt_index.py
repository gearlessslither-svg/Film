#!/usr/bin/env python3
"""Build a human-friendly prompt index for Reference-003 R5 video packages."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = PROJECT_ROOT / "08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701"
REPORT_PATH = (
    PROJECT_ROOT
    / "10_qa/reports/reference003_r5_video_segment_all_units01_21_generation_ready_20260701.json"
)
ASSET_LOCKS_PATH = PROJECT_ROOT / "05_asset_bible/setting_chapters/reference003_asset_locks_v1.json"
INDEX_ROOT = PACKAGE_ROOT / "_PROMPT_INDEX"
PROMPT_ONLY_ROOT = INDEX_ROOT / "PROMPT_ONLY"
GLOBAL_LOCK_ROOT = PACKAGE_ROOT / "_global_asset_locks"


ACTIVE_LOCK_PATTERNS = [
    ("characters", "nadia", [r"\bnadia\b"]),
    ("characters", "jean", [r"\bjean\b"]),
    ("characters", "marie", [r"\bmarie\b"]),
    ("characters", "king", [r"\bking\b"]),
    ("characters", "grandis", [r"\bgrandis\b", r"\btrio\b"]),
    ("characters", "sanson", [r"\bsanson\b", r"\btrio\b"]),
    ("characters", "hanson", [r"\bhanson\b", r"\btrio\b"]),
    ("characters", "nemo", [r"\bnemo\b", r"\bcaptain\b"]),
    ("props_vehicles_symbols", "blue_water_pendant", [r"blue water", r"\bjewel\b", r"\bpendant\b", r"\bnadia\b"]),
    ("props_vehicles_symbols", "white_bird", [r"white bird", r"\bbird\b"]),
    ("props_vehicles_symbols", "jean_aircraft", [r"\baircraft\b", r"\bplane\b", r"flying machine"]),
    ("props_vehicles_symbols", "grandis_vehicle", [r"grandis vehicle", r"\bvehicle\b"]),
    ("props_vehicles_symbols", "nautilus", [r"\bnautilus\b", r"\bsubmarine\b", r"\bundersea\b"]),
    ("props_vehicles_symbols", "blue_grid_geometry", [r"blue grid", r"night city", r"\bgeometry\b"]),
    ("props_vehicles_symbols", "water_burst_transition", [r"water splash", r"water burst", r"\bsplash\b"]),
]

UNIT_ACTIVE_LOCKS = {
    "VU_REF003_001_BLACK_CLOUD_FADEIN": [],
    "VU_REF003_002_WHITE_BIRD_SKY": [("props_vehicles_symbols", "white_bird")],
    "VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS": [("props_vehicles_symbols", "white_bird")],
    "VU_REF003_004_AIRCRAFT_BRIEF_REVEAL": [("props_vehicles_symbols", "jean_aircraft")],
    "VU_REF003_005_MAIN_TITLE_SAFE_HOLD": [],
    "VU_REF003_006_SUN_FLARE_TO_NADIA": [
        ("characters", "nadia"),
        ("props_vehicles_symbols", "blue_water_pendant"),
    ],
    "VU_REF003_007_NADIA_PROFILE_ENTRY": [
        ("characters", "nadia"),
        ("props_vehicles_symbols", "blue_water_pendant"),
    ],
    "VU_REF003_008_JEAN_INTRO": [("characters", "jean")],
    "VU_REF003_009_MARIE_KING_MEADOW": [
        ("characters", "marie"),
        ("characters", "king"),
    ],
    "VU_REF003_010_GRANDIS_TRIO_INTRO": [
        ("characters", "grandis"),
        ("characters", "sanson"),
        ("characters", "hanson"),
    ],
    "VU_REF003_011_RUNNING_MONTAGE": [
        ("characters", "nadia"),
        ("characters", "jean"),
        ("characters", "marie"),
        ("characters", "king"),
        ("props_vehicles_symbols", "blue_water_pendant"),
    ],
    "VU_REF003_012_GRANDIS_VEHICLE_ACTION": [
        ("characters", "grandis"),
        ("characters", "sanson"),
        ("characters", "hanson"),
        ("props_vehicles_symbols", "grandis_vehicle"),
    ],
    "VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS": [
        ("props_vehicles_symbols", "nautilus"),
    ],
    "VU_REF003_014_NIGHT_CITY_BLUE_GRID": [
        ("props_vehicles_symbols", "blue_grid_geometry"),
    ],
    "VU_REF003_015_NIGHT_AIRCRAFT_PASS": [
        ("props_vehicles_symbols", "jean_aircraft"),
    ],
    "VU_REF003_016_NEMO_SUNSET_PROFILE": [("characters", "nemo")],
    "VU_REF003_017_NADIA_SOLEMN_CLOSE": [
        ("characters", "nadia"),
        ("props_vehicles_symbols", "blue_water_pendant"),
    ],
    "VU_REF003_018_BLUE_WATER_SYMBOL": [
        ("props_vehicles_symbols", "blue_water_pendant"),
    ],
    "VU_REF003_019_WATER_SPLASH_TRANSITION": [
        ("props_vehicles_symbols", "water_burst_transition"),
    ],
    "VU_REF003_020_FINAL_SKY_SAFE_HOLD": [],
    "VU_REF003_021_BLACK_TAIL": [],
}


def rel(path: Path) -> str:
    return path.relative_to(PROJECT_ROOT).as_posix()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def extract_brief_prompt(brief_text: str) -> str:
    marker = "## Existing Unit Prompt"
    idx = brief_text.find(marker)
    if idx >= 0:
        prompt_text = brief_text[idx + len(marker) :].strip()
        for stop_marker in ("\n## R5 Expanded Notes", "\n## Reject Conditions"):
            stop_idx = prompt_text.find(stop_marker)
            if stop_idx >= 0:
                prompt_text = prompt_text[:stop_idx].strip()
        return prompt_text
    return brief_text.strip()


def safe_name(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]+", "_", text).strip("_")


def load_anchor_text(job: dict[str, Any]) -> tuple[list[dict[str, Any]], str]:
    anchors_path = PROJECT_ROOT / job["job_dir"] / "ordered_keyframe_anchors.json"
    anchors = read_json(anchors_path) if anchors_path.exists() else []
    pieces: list[str] = []
    for anchor in anchors:
        pieces.extend(
            str(anchor.get(key, ""))
            for key in ("item_id", "role", "beat", "difference_reason", "source_path")
        )
    return anchors, " ".join(pieces)


def select_active_locks(
    job: dict[str, Any],
    prompt_text: str,
    anchor_text: str,
    asset_locks: dict[str, Any],
) -> list[dict[str, Any]]:
    explicit_locks = UNIT_ACTIVE_LOCKS.get(job["unit_id"])
    if explicit_locks is not None:
        return [
            build_lock_record(group, asset_id, asset_locks)
            for group, asset_id in explicit_locks
        ]
    haystack = f"{job['unit_id']} {job.get('title', '')} {prompt_text} {anchor_text}".lower()
    selected: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for group, asset_id, patterns in ACTIVE_LOCK_PATTERNS:
        if any(re.search(pattern, haystack, re.IGNORECASE) for pattern in patterns):
            key = (group, asset_id)
            if key in seen:
                continue
            seen.add(key)
            selected.append(build_lock_record(group, asset_id, asset_locks))
    return selected


def build_lock_record(group: str, asset_id: str, asset_locks: dict[str, Any]) -> dict[str, Any]:
    lock = asset_locks.get(group, {}).get(asset_id, {})
    global_path = ""
    source_path = lock.get("lock_path") or ""
    if source_path:
        src = PROJECT_ROOT / source_path
        suffix = src.suffix or ".png"
        global_path = rel(GLOBAL_LOCK_ROOT / f"{group}_{asset_id}{suffix}")
    return {
        "group": group,
        "asset_id": asset_id,
        "status": lock.get("status", ""),
        "source_path": source_path,
        "global_lock_path": global_path,
    }


def copy_global_locks(asset_locks: dict[str, Any]) -> list[dict[str, Any]]:
    if GLOBAL_LOCK_ROOT.exists():
        shutil.rmtree(GLOBAL_LOCK_ROOT)
    GLOBAL_LOCK_ROOT.mkdir(parents=True, exist_ok=True)
    copied: list[dict[str, Any]] = []
    for group in ("characters", "props_vehicles_symbols"):
        for asset_id, lock in asset_locks.get(group, {}).items():
            source_path = lock.get("lock_path") if isinstance(lock, dict) else ""
            output_path = ""
            exists = False
            if source_path:
                src = PROJECT_ROOT / source_path
                suffix = src.suffix or ".png"
                dst = GLOBAL_LOCK_ROOT / f"{group}_{asset_id}{suffix}"
                if src.exists():
                    shutil.copy2(src, dst)
                output_path = rel(dst)
                exists = dst.exists()
            copied.append(
                {
                    "group": group,
                    "asset_id": asset_id,
                    "status": lock.get("status", "") if isinstance(lock, dict) else "",
                    "source_path": source_path or "",
                    "global_lock_path": output_path,
                    "exists": exists,
                }
            )
    (GLOBAL_LOCK_ROOT / "asset_locks_manifest.json").write_text(
        json.dumps(copied, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return copied


def format_active_lock_lines(active_locks: list[dict[str, Any]]) -> str:
    if not active_locks:
        return "- none for this unit; rely on reference clip + ordered keyframes + no-text rules."
    lines = []
    for lock in active_locks:
        path = lock.get("global_lock_path") or lock.get("source_path") or ""
        lines.append(f"- `{lock['asset_id']}` ({lock.get('status', '')}): `{path}`")
    return "\n".join(lines)


def format_anchor_lines(anchors: list[dict[str, Any]]) -> str:
    if not anchors:
        return "- none"
    lines = []
    for anchor in anchors:
        lines.append(
            f"- 图{anchor['order']}: `{anchor['item_id']}` ({anchor.get('timecode', '')}) "
            f"`{anchor.get('packaged_path', '')}`"
        )
    return "\n".join(lines)


def build_prompt_only(job: dict[str, Any], prompt_text: str, anchors: list[dict[str, Any]], active_locks: list[dict[str, Any]]) -> str:
    return f"""# {job['order']:02d} — {job['unit_id']} — {job.get('title', '')}

## Upload These

1. Reference video: `{job['reference_clip']['path']}`
2. Ordered keyframes:
{format_anchor_lines(anchors)}
3. Active asset locks:
{format_active_lock_lines(active_locks)}

## Save Result To

`{job['expected_video_output_path']}`

## Prompt To Use

{prompt_text.strip()}
"""


def main() -> None:
    report = read_json(REPORT_PATH)
    asset_locks = read_json(ASSET_LOCKS_PATH)
    INDEX_ROOT.mkdir(parents=True, exist_ok=True)
    if PROMPT_ONLY_ROOT.exists():
        shutil.rmtree(PROMPT_ONLY_ROOT)
    PROMPT_ONLY_ROOT.mkdir(parents=True, exist_ok=True)
    copied_locks = copy_global_locks(asset_locks)

    index_rows: list[str] = []
    json_rows: list[dict[str, Any]] = []
    for job in report["jobs"]:
        brief_path = PROJECT_ROOT / job["generation_brief"]
        brief_text = brief_path.read_text(encoding="utf-8")
        prompt_text = extract_brief_prompt(brief_text)
        anchors, anchor_text = load_anchor_text(job)
        active_locks = select_active_locks(job, prompt_text, anchor_text, asset_locks)
        prompt_file = PROMPT_ONLY_ROOT / f"{job['order']:02d}_{safe_name(job['unit_id'])}.md"
        prompt_file.write_text(
            build_prompt_only(job, prompt_text, anchors, active_locks), encoding="utf-8"
        )
        active_lock_path = PROJECT_ROOT / job["job_dir"] / "active_asset_locks.json"
        active_lock_path.write_text(
            json.dumps(active_locks, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        index_rows.append(
            f"| {job['order']:02d} | `{job['unit_id']}` | {job.get('title', '')} | "
            f"`{job['reference_clip']['path']}` | `{rel(prompt_file)}` | "
            f"{', '.join(lock['asset_id'] for lock in active_locks) or 'none'} |"
        )
        json_rows.append(
            {
                "order": job["order"],
                "unit_id": job["unit_id"],
                "title": job.get("title", ""),
                "time_range": job.get("time_range", ""),
                "reference_clip": job["reference_clip"]["path"],
                "prompt_only_path": rel(prompt_file),
                "full_generation_brief": job["generation_brief"],
                "ordered_keyframe_contact_sheet": job["ordered_keyframe_contact_sheet"],
                "expected_video_output_path": job["expected_video_output_path"],
                "active_asset_locks": active_locks,
            }
        )

    index_md = f"""# Reference-003 R5 Video Prompt Index

Use this folder as the human-facing entry point for external AIGC video generation.

## Which Prompt File To Use

- Best human entry: `_PROMPT_INDEX/PROMPT_ONLY/<ORDER>_<UNIT>.md`
- Full machine/QA packet: each unit's `AIGC_VIDEO_GENERATION_BRIEF.md`
- Original unit prompt source: `07_shots/video_prompts_by_unit/<UNIT>.md`

For the AIGC website, upload the unit reference clip, the ordered keyframes, and only
the active asset locks listed in the prompt-only file. The old per-unit `asset_locks/`
folders are intentionally redundant legacy/full-self-contained packaging.

## Global Asset Locks

- One shared folder: `{rel(GLOBAL_LOCK_ROOT)}`
- Manifest: `{rel(GLOBAL_LOCK_ROOT / 'asset_locks_manifest.json')}`
- Copied lock records: {len(copied_locks)}

## Unit Index

| # | Unit | Title | Reference Clip | Prompt-Only File | Active Locks |
|---:|---|---|---|---|---|
{chr(10).join(index_rows)}
"""
    (INDEX_ROOT / "AIGC_VIDEO_PROMPT_INDEX.md").write_text(index_md, encoding="utf-8")
    (INDEX_ROOT / "AIGC_VIDEO_PROMPT_INDEX.json").write_text(
        json.dumps(json_rows, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (PACKAGE_ROOT / "README_USE_THIS_FIRST.md").write_text(
        index_md.replace("# Reference-003 R5 Video Prompt Index", "# Use This First — Reference-003 R5 Video Packages"),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "status": "prompt_index_ready",
                "unit_count": len(json_rows),
                "index_md": rel(INDEX_ROOT / "AIGC_VIDEO_PROMPT_INDEX.md"),
                "index_json": rel(INDEX_ROOT / "AIGC_VIDEO_PROMPT_INDEX.json"),
                "prompt_only_dir": rel(PROMPT_ONLY_ROOT),
                "global_asset_locks": rel(GLOBAL_LOCK_ROOT),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
