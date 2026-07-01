#!/usr/bin/env python3
"""Promote dense reference frames into real R2 keyframe asset slots.

R1 increased reference-frame density but kept the final preview at 42 assets.
R2 corrects that workflow: selected dense frames become pending generated image
assets with stable IDs, prompts, planned output paths, and preview ordering.
"""

from __future__ import annotations

import json
import re
import shutil
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[3]
BOARD_PATH = PROJECT_ROOT / "03_story/idea_board/idea_board.json"
DENSE_MANIFEST_PATH = (
    PROJECT_ROOT / "01_intake/analysis/reference003_dense_repair_frames_20260630/manifest.json"
)
ASSET_LOCKS_PATH = PROJECT_ROOT / "05_asset_bible/setting_chapters/reference003_asset_locks_v1.json"
SETTING_CHAPTER_PATH = PROJECT_ROOT / "05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md"
JOB_DIR = PROJECT_ROOT / "08_generation/jobs/REFERENCE003_EXPANDED_KEYFRAMES_R2_20260630"
EXPANDED_DIR = PROJECT_ROOT / "03_story/expanded_keyframes"
EXPANDED_MANIFEST = EXPANDED_DIR / "reference003_expanded_keyframes_r2_20260630.json"
EXPANDED_MD = EXPANDED_DIR / "reference003_expanded_keyframes_r2_20260630.md"
TZ = timezone(timedelta(hours=8))
EPSILON_SEC = 0.02


def rel(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def parse_time(value: str) -> float:
    minutes, seconds = value.split(":")
    return int(minutes) * 60 + float(seconds)


def extract_reference_time(row: dict[str, Any]) -> float:
    text = f"{row.get('image_prompt') or ''}\n{row.get('video_prompt') or ''}"
    match = re.search(r"Reference source:.*? at ([0-9]{2}:[0-9]{2}(?:\.[0-9]+)?)", text)
    if not match:
        raise ValueError(f"Missing reference time for {row.get('item_id')}")
    return parse_time(match.group(1))


def slug_time(seconds: float) -> str:
    return f"{int(round(seconds * 1000)):06d}ms"


def load_board_rows() -> list[dict[str, Any]]:
    rows = json.loads(BOARD_PATH.read_text())["rows"]
    assets: list[dict[str, Any]] = []
    for row in rows:
        if row.get("status") != "generated_reference003_qa_pass":
            continue
        output_path = row.get("output_path")
        if not output_path:
            continue
        path = PROJECT_ROOT / output_path
        if not path.exists():
            continue
        asset = dict(row)
        asset["time_sec"] = extract_reference_time(row)
        assets.append(asset)
    return sorted(assets, key=lambda item: item["time_sec"])


def lock_summary() -> str:
    locks = json.loads(ASSET_LOCKS_PATH.read_text())
    lines = []
    for group_name in ("characters", "props_vehicles_symbols"):
        group = locks.get(group_name, {})
        for asset_id, lock in group.items():
            if not isinstance(lock, dict):
                continue
            path = lock.get("lock_path")
            status = lock.get("status", "")
            if path:
                lines.append(f"- `{asset_id}` ({status}): `{path}`")
            else:
                lines.append(f"- `{asset_id}` ({status})")
    return "\n".join(lines)


def copy_ref(src_rel: str, dst_name: str) -> str:
    refs_dir = JOB_DIR / "refs/expanded_selected"
    refs_dir.mkdir(parents=True, exist_ok=True)
    src = PROJECT_ROOT / src_rel
    dst = refs_dir / dst_name
    shutil.copy2(src, dst)
    return rel(dst)


def generation_prompt(parent: dict[str, Any], new_id: str, ref_path: str, time_sec: float) -> str:
    return "\n".join(
        [
            f"# {new_id} R2 expanded keyframe generation prompt",
            "",
            "Use case: photorealistic-natural",
            "Asset type: Reference-003 expanded real keyframe asset",
            f"Parent shot: `{parent['item_id']}`",
            f"Reference time: `{time_sec:.3f}` seconds",
            f"Dense reference frame: `{ref_path}`",
            f"Setting chapter: `{rel(SETTING_CHAPTER_PATH)}`",
            f"Asset locks: `{rel(ASSET_LOCKS_PATH)}`",
            "",
            "## Primary Request",
            "",
            "Generate a new 21:9 live-action keyframe asset for this exact dense reference moment. "
            "Use the dense reference frame for pose, camera angle, timing, motion phase, and scene layout only. "
            "Use the asset locks for all recurring faces, costumes, props, vehicles, locations, and symbols.",
            "",
            "## Parent Shot Context",
            "",
            parent.get("frame_description")
            or parent.get("beat")
            or parent.get("image_prompt", "")[:600],
            "",
            "## Lock Summary",
            "",
            lock_summary(),
            "",
            "## Rejection Conditions",
            "",
            "- Do not copy anime art, subtitles, lyrics, credits, source text, logos, or watermarks.",
            "- Do not redesign recurring faces, costumes, props, vehicles, animals, locations, or symbols.",
            "- Nadia must match OP_SHOT_011_v2 whenever visible.",
            "- Grandis vehicle/action craft must match the R1 OP_SHOT_024 vehicle lock whenever visible.",
            "- Minors must remain age-appropriate and non-sexualized.",
            "- Output must be a real generated image asset, not a reference placeholder.",
            "",
            "## Output",
            "",
            "- 1915x821 or higher, 21:9, clean image only.",
            f"- Planned output path: `08_generation/jobs/REFERENCE003_EXPANDED_KEYFRAMES_R2_20260630/outputs/{new_id}.png`",
            "",
        ]
    )


def main() -> int:
    now = datetime.now(TZ).isoformat(timespec="seconds")
    JOB_DIR.mkdir(parents=True, exist_ok=True)
    (JOB_DIR / "prompts").mkdir(parents=True, exist_ok=True)
    (JOB_DIR / "outputs").mkdir(parents=True, exist_ok=True)
    EXPANDED_DIR.mkdir(parents=True, exist_ok=True)

    base_rows = load_board_rows()
    by_item = {row["item_id"]: row for row in base_rows}
    dense = json.loads(DENSE_MANIFEST_PATH.read_text())

    assets: list[dict[str, Any]] = []
    for row in base_rows:
        assets.append(
            {
                "asset_id": row["item_id"],
                "asset_type": "existing_generated_keyframe",
                "parent_item_id": row["item_id"],
                "time_sec": round(row["time_sec"], 3),
                "status": "generated",
                "output_path": row["output_path"],
                "source": "idea_board",
            }
        )

    skipped_duplicates = []
    created_new = []
    existing_times = [(row["item_id"], row["time_sec"]) for row in base_rows]
    for target in dense.get("targets", []):
        parent_id = target["item_id"]
        parent = by_item.get(parent_id)
        if not parent:
            continue
        for selected in target.get("selected_frames", []):
            time_sec = float(selected["time_sec"])
            duplicate = [
                item_id
                for item_id, existing_time in existing_times
                if abs(time_sec - existing_time) <= EPSILON_SEC
            ]
            if duplicate:
                skipped_duplicates.append(
                    {
                        "parent_item_id": parent_id,
                        "time_sec": round(time_sec, 3),
                        "matches_existing": duplicate[0],
                        "selected_path": selected["selected_path"],
                    }
                )
                continue
            new_id = f"{parent_id}_R2_{slug_time(time_sec)}"
            ref_path = copy_ref(selected["selected_path"], f"{new_id}_ref.jpg")
            prompt_path = JOB_DIR / "prompts" / f"{new_id}_generation_prompt.md"
            prompt_path.write_text(generation_prompt(parent, new_id, ref_path, time_sec))
            planned_output = f"08_generation/jobs/REFERENCE003_EXPANDED_KEYFRAMES_R2_20260630/outputs/{new_id}.png"
            asset = {
                "asset_id": new_id,
                "asset_type": "new_expanded_keyframe",
                "parent_item_id": parent_id,
                "time_sec": round(time_sec, 3),
                "status": "pending_generation",
                "dense_reference_frame": ref_path,
                "prompt_path": rel(prompt_path),
                "planned_output_path": planned_output,
                "output_path": "",
                "select_reason": selected.get("select_reason", ""),
                "source": "dense_reference_promoted_to_asset_slot",
            }
            assets.append(asset)
            created_new.append(asset)

    assets = sorted(assets, key=lambda item: (item["time_sec"], item["asset_id"]))
    manifest = {
        "schema_version": "reference003_expanded_keyframes_r2_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": now,
        "status": "pending_new_image_generation",
        "rule": "Final preview must use this expanded asset list after pending_generation assets receive generated output_path values.",
        "base_existing_asset_count": len(base_rows),
        "dense_selected_count": sum(len(t.get("selected_frames", [])) for t in dense.get("targets", [])),
        "new_asset_slots_count": len(created_new),
        "skipped_duplicate_selected_frames_count": len(skipped_duplicates),
        "expanded_total_asset_count_after_generation": len(base_rows) + len(created_new),
        "setting_chapter": rel(SETTING_CHAPTER_PATH),
        "asset_locks": rel(ASSET_LOCKS_PATH),
        "source_dense_manifest": rel(DENSE_MANIFEST_PATH),
        "job_dir": rel(JOB_DIR),
        "assets": assets,
        "new_asset_slots": created_new,
        "skipped_duplicate_selected_frames": skipped_duplicates,
    }
    EXPANDED_MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    (JOB_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

    lines = [
        "# Reference-003 Expanded Keyframes R2",
        "",
        f"- Created: `{now}`",
        "- Status: `pending_new_image_generation`",
        f"- Existing generated assets: `{len(base_rows)}`",
        f"- Dense selected frames: `{manifest['dense_selected_count']}`",
        f"- New asset slots to generate: `{len(created_new)}`",
        f"- Expanded total after generation: `{manifest['expanded_total_asset_count_after_generation']}`",
        f"- Skipped duplicate selected frames: `{len(skipped_duplicates)}`",
        "",
        "## Rule",
        "",
        "The next preview video must read this expanded asset list after all `pending_generation` slots have real generated `output_path` values.",
        "",
        "## New Asset Slots",
        "",
        "| Asset | Parent | Time | Prompt | Planned output |",
        "|---|---|---:|---|---|",
    ]
    for asset in created_new:
        lines.append(
            f"| `{asset['asset_id']}` | `{asset['parent_item_id']}` | {asset['time_sec']:.3f} | `{asset['prompt_path']}` | `{asset['planned_output_path']}` |"
        )
    EXPANDED_MD.write_text("\n".join(lines) + "\n")
    (JOB_DIR / "README.md").write_text("\n".join(lines) + "\n")

    print(
        json.dumps(
            {
                "status": manifest["status"],
                "existing_assets": len(base_rows),
                "dense_selected_frames": manifest["dense_selected_count"],
                "new_asset_slots": len(created_new),
                "expanded_total_after_generation": manifest["expanded_total_asset_count_after_generation"],
                "expanded_manifest": rel(EXPANDED_MANIFEST),
                "job_manifest": rel(JOB_DIR / "manifest.json"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
