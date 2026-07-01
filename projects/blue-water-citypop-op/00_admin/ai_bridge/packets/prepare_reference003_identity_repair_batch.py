#!/usr/bin/env python3
"""Prepare dense reference frames and image-repair prompts for Reference-003.

This script stops before video assembly. It creates a repair-first image batch:
1. Extract dense candidates around identity/prop-risk moments.
2. Select sharp/motion-representative frames.
3. Package current locks, reject rules, and per-shot AIGC image prompts.
"""

from __future__ import annotations

import json
import math
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageStat


PROJECT_ROOT = Path(__file__).resolve().parents[3]
SOURCE_VIDEO = PROJECT_ROOT / "01_intake/references/reference-003-full-op-2160p.mp4"
BOARD_PATH = PROJECT_ROOT / "03_story/idea_board/idea_board.json"
SETTING_CHAPTER_PATH = PROJECT_ROOT / "05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md"
ASSET_LOCKS_PATH = PROJECT_ROOT / "05_asset_bible/setting_chapters/reference003_asset_locks_v1.json"
ANALYSIS_DIR = PROJECT_ROOT / "01_intake/analysis/reference003_dense_repair_frames_20260630"
JOB_DIR = PROJECT_ROOT / "08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630"
FFMPEG = Path("/Applications/Bitwig Studio.app/Contents/MacOS/ffmpeg")
FPS = 8
TZ = timezone(timedelta(hours=8))


@dataclass(frozen=True)
class RepairTarget:
    item_id: str
    label: str
    center_sec: float
    start_sec: float
    end_sec: float
    action: str
    priority: int
    hard_replace: bool
    locks: tuple[str, ...]
    notes: str


TARGETS = [
    RepairTarget(
        "OP_SHOT_018",
        "Nadia running front identity continuity",
        39.50,
        38.75,
        40.25,
        "regenerate_if_face_drift_after_dense_reference_review",
        4,
        False,
        ("nadia", "blue_water_pendant"),
        "Use OP_SHOT_011_v2 as Nadia face lock; preserve running pose only from video.",
    ),
    RepairTarget(
        "OP_SHOT_019",
        "Jean running identity continuity",
        41.50,
        40.75,
        42.25,
        "regenerate_if_face_or_costume_drift_after_dense_reference_review",
        5,
        False,
        ("jean",),
        "Use OP_SHOT_012 as Jean lock; preserve cap, glasses, jacket, bow tie.",
    ),
    RepairTarget(
        "OP_SHOT_020",
        "Marie and King running identity continuity",
        43.50,
        42.75,
        44.50,
        "regenerate_if_marie_or_king_drift_after_dense_reference_review",
        5,
        False,
        ("marie", "king"),
        "Use OP_SHOT_014 as Marie/King lock; preserve child-safe age and King scarf.",
    ),
    RepairTarget(
        "OP_SHOT_021",
        "Accepted group-running energy reference",
        45.50,
        44.75,
        46.50,
        "keep_as_workprint_reference_and_use_for_group_energy",
        9,
        False,
        ("nadia", "jean", "marie", "king", "grandis", "sanson", "hanson"),
        "Director accepted current OP_SHOT_021_v2 for workprint use.",
    ),
    RepairTarget(
        "OP_SHOT_023",
        "Grandis trio action identity continuity",
        48.00,
        47.25,
        48.75,
        "regenerate_or_retouch_with_grandis_trio_locks",
        3,
        False,
        ("grandis", "sanson", "hanson"),
        "Use OP_SHOT_016_v2 as trio lock; do not redesign faces during action.",
    ),
    RepairTarget(
        "OP_SHOT_024",
        "Grandis vehicle/action craft design lock",
        49.50,
        48.85,
        50.35,
        "create_new_grandis_vehicle_action_craft_lock",
        2,
        True,
        ("grandis", "sanson", "hanson"),
        "Create a new vehicle/action craft lock. Do not use rejected OP_SHOT_025.",
    ),
    RepairTarget(
        "OP_SHOT_025",
        "Rejected group lineup and vehicle tableau",
        51.50,
        50.70,
        52.40,
        "hard_replace_rebuild_locked_group_tableau",
        1,
        True,
        ("nadia", "jean", "marie", "king", "grandis", "sanson", "hanson", "blue_water_pendant"),
        "Director rejected current OP_SHOT_025 as the worst group image; rebuild from locks.",
    ),
    RepairTarget(
        "OP_SHOT_032",
        "Nemo sunset identity lock",
        66.50,
        65.75,
        67.40,
        "regenerate_if_nemo_drift_after_dense_reference_review",
        6,
        False,
        ("nemo",),
        "Use OP_SHOT_032 as current Nemo lock; preserve uniform, cap, stern adult face.",
    ),
    RepairTarget(
        "OP_SHOT_033",
        "Nemo sunset continuation",
        69.50,
        68.75,
        70.40,
        "regenerate_if_nemo_continuity_drift_after_dense_reference_review",
        6,
        False,
        ("nemo",),
        "Match OP_SHOT_032 exactly; only angle/lighting may change.",
    ),
    RepairTarget(
        "OP_SHOT_034",
        "Rejected Nadia solemn front close-up",
        72.00,
        71.20,
        72.90,
        "hard_replace_with_nadia_face_lock",
        1,
        True,
        ("nadia", "blue_water_pendant"),
        "Director rejected current OP_SHOT_034; Nadia must match OP_SHOT_011_v2.",
    ),
]


PROMPT_PRIMARY = {
    "OP_SHOT_018": "21:9 live-action remake keyframe of Nadia running toward camera in bright sky light, dynamic but age-appropriate, face matching the official Nadia lock exactly.",
    "OP_SHOT_019": "21:9 live-action remake keyframe of Jean running in the montage, energetic boy inventor, face and costume matching the official Jean lock exactly.",
    "OP_SHOT_020": "21:9 live-action remake keyframe of Marie and King running in open daylight, child-safe, cheerful movement, identities matching their first approved lock.",
    "OP_SHOT_021": "21:9 live-action group-running reference keyframe, keep current accepted energy; use only as continuity support unless a later QA pass requires a rerender.",
    "OP_SHOT_023": "21:9 live-action action keyframe of Grandis, Sanson, and Hanson in a fast bridge/action beat, faces and costumes matching their official trio lock.",
    "OP_SHOT_024": "21:9 live-action action keyframe establishing a new Grandis vehicle/action craft lock in sky/cloud spray, readable silhouette, consistent retro adventure engineering.",
    "OP_SHOT_025": "21:9 live-action locked group tableau replacing the rejected large group portrait: all seven recurring characters arranged together with correct faces, costumes, scale, and Grandis vehicle/action craft continuity.",
    "OP_SHOT_032": "21:9 live-action Nemo sunset profile keyframe, stern adult captain, uniform and cap locked, same actor identity as official Nemo lock.",
    "OP_SHOT_033": "21:9 live-action Nemo sunset continuation keyframe, same actor identity as OP_SHOT_032, only angle and sunset lighting shift.",
    "OP_SHOT_034": "21:9 live-action solemn front close-up of Nadia in cool symbolic blue light, face matching OP_SHOT_011_v2 exactly, Blue Water pendant readable, no sea-background face drift.",
}


def rel(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def timecode(seconds: float) -> str:
    mins = int(seconds // 60)
    secs = seconds - mins * 60
    return f"{mins:02d}:{secs:05.2f}"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def current_rows() -> dict[str, dict[str, Any]]:
    rows = load_json(BOARD_PATH)["rows"]
    return {row["item_id"]: row for row in rows if row.get("item_id")}


def asset_lock_paths(asset_locks: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for group_name in ("characters", "props_vehicles_symbols"):
        group = asset_locks.get(group_name, {})
        if not isinstance(group, dict):
            continue
        for asset_id, data in group.items():
            if isinstance(data, dict) and data.get("lock_path"):
                result[asset_id] = data["lock_path"]
    return result


def ensure_clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def extract_candidates(target: RepairTarget) -> list[Path]:
    out_dir = ANALYSIS_DIR / "candidates" / target.item_id
    ensure_clean_dir(out_dir)
    duration = target.end_sec - target.start_sec
    pattern = out_dir / f"{target.item_id}_cand_%04d.jpg"
    command = [
        str(FFMPEG),
        "-y",
        "-ss",
        f"{target.start_sec:.3f}",
        "-t",
        f"{duration:.3f}",
        "-i",
        str(SOURCE_VIDEO),
        "-vf",
        f"fps={FPS},scale=1915:-2",
        "-q:v",
        "2",
        str(pattern),
    ]
    proc = subprocess.run(command, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr)
    return sorted(out_dir.glob("*.jpg"))


def sharpness(image: Image.Image) -> float:
    gray = image.convert("L").resize((320, 138))
    edges = gray.filter(ImageFilter.FIND_EDGES)
    return float(ImageStat.Stat(edges).stddev[0])


def mean_delta(image: Image.Image, previous: Image.Image | None) -> float:
    if previous is None:
        return 0.0
    a = image.convert("L").resize((320, 138))
    b = previous.convert("L").resize((320, 138))
    diff = ImageChops.difference(a, b)
    return float(ImageStat.Stat(diff).mean[0])


def analyze_candidates(target: RepairTarget, paths: list[Path]) -> list[dict[str, Any]]:
    metrics: list[dict[str, Any]] = []
    previous: Image.Image | None = None
    for index, path in enumerate(paths):
        image = Image.open(path)
        t = target.start_sec + index / FPS
        row = {
            "index": index + 1,
            "time_sec": round(t, 3),
            "timecode": timecode(t),
            "path": rel(path),
            "sharpness": round(sharpness(image), 4),
            "delta": round(mean_delta(image, previous), 4),
            "center_distance": round(abs(t - target.center_sec), 4),
        }
        metrics.append(row)
        previous = image.copy()
    return metrics


def select_metrics(target: RepairTarget, metrics: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not metrics:
        return []
    selected: dict[int, dict[str, Any]] = {}

    def add(reason: str, row: dict[str, Any]) -> None:
        copy = dict(row)
        copy["select_reason"] = reason
        selected[copy["index"]] = copy

    add("center_time", min(metrics, key=lambda row: row["center_distance"]))
    for row in sorted(metrics, key=lambda row: row["sharpness"], reverse=True)[:2]:
        add("sharp_detail", row)
    for row in sorted(metrics, key=lambda row: row["delta"], reverse=True)[:2]:
        add("motion_change", row)
    add("window_start", metrics[0])
    add("window_end", metrics[-1])

    ordered = sorted(selected.values(), key=lambda row: row["time_sec"])
    if len(ordered) > 6:
        keep = [ordered[0], ordered[-1]]
        middle = sorted(ordered[1:-1], key=lambda row: (row["select_reason"] != "center_time", -row["sharpness"]))[:4]
        ordered = sorted(keep + middle, key=lambda row: row["time_sec"])
    for order, row in enumerate(ordered, start=1):
        src = PROJECT_ROOT / row["path"]
        dst_dir = ANALYSIS_DIR / "selected" / target.item_id
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst = dst_dir / f"{target.item_id}_sel_{order:02d}_{int(row['time_sec'] * 1000):06d}ms.jpg"
        shutil.copy2(src, dst)
        row["selected_order"] = order
        row["selected_path"] = rel(dst)
    return ordered


def make_sheet(rows: list[dict[str, Any]], out_path: Path, title: str, columns: int = 3) -> None:
    thumbs: list[tuple[Image.Image, dict[str, Any]]] = []
    for row in rows:
        path = PROJECT_ROOT / row["selected_path"]
        img = Image.open(path).convert("RGB")
        img.thumbnail((420, 180), Image.Resampling.LANCZOS)
        thumbs.append((img, row))

    cell_w, cell_h = 440, 245
    rows_count = max(1, math.ceil(len(thumbs) / columns))
    sheet = Image.new("RGB", (columns * cell_w, rows_count * cell_h + 54), (16, 20, 24))
    draw = ImageDraw.Draw(sheet)
    draw.text((12, 14), title, fill=(235, 240, 245))
    for idx, (img, row) in enumerate(thumbs):
        x = (idx % columns) * cell_w + 10
        y = (idx // columns) * cell_h + 54
        sheet.paste(img, (x, y))
        label = f"{row.get('item_id', '')} {row['timecode']} {row['select_reason']}"
        draw.text((x, y + img.height + 8), label, fill=(230, 235, 240))
        metric = f"sharp {row['sharpness']:.1f} delta {row['delta']:.1f}"
        draw.text((x, y + img.height + 28), metric, fill=(170, 180, 190))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path, quality=92)


def copy_locks(asset_locks: dict[str, Any]) -> list[dict[str, Any]]:
    lock_dir = JOB_DIR / "asset_locks"
    ensure_clean_dir(lock_dir)
    packaged: list[dict[str, Any]] = []
    for asset_id, source_rel in asset_lock_paths(asset_locks).items():
        src = PROJECT_ROOT / source_rel
        dst = lock_dir / f"{asset_id}{src.suffix or '.png'}"
        if src.exists():
            shutil.copy2(src, dst)
        packaged.append(
            {
                "asset_id": asset_id,
                "source_path": source_rel,
                "packaged_path": rel(dst),
                "exists": dst.exists(),
            }
        )
    return packaged


def copy_selected_refs(selected_by_item: dict[str, list[dict[str, Any]]]) -> None:
    refs_dir = JOB_DIR / "refs/dense_selected"
    ensure_clean_dir(refs_dir)
    for item_id, rows in selected_by_item.items():
        item_dir = refs_dir / item_id
        item_dir.mkdir(parents=True, exist_ok=True)
        for row in rows:
            src = PROJECT_ROOT / row["selected_path"]
            shutil.copy2(src, item_dir / src.name)


def prompt_for_target(target: RepairTarget, row: dict[str, Any], locks: dict[str, str]) -> str:
    current = row.get("output_path", "")
    selected_paths = [
        f"refs/dense_selected/{target.item_id}/{Path(sel['selected_path']).name}"
        for sel in row["selected_refs"]
    ]
    lock_lines = []
    for lock_id in target.locks:
        lock_path = locks.get(lock_id)
        if lock_path:
            lock_lines.append(f"- `{lock_id}`: `asset_locks/{lock_id}{Path(lock_path).suffix or '.png'}`")
        else:
            lock_lines.append(f"- `{lock_id}`: pending new lock; do not invent from rejected OP_SHOT_025")
    reject = [
        "Do not use the rejected OP_SHOT_025 image as a character, group, or vehicle lock.",
        "Do not use the rejected OP_SHOT_034 face as a Nadia lock.",
        "No readable text, credits, lyrics, subtitles, logo, watermark, or random symbols.",
        "Minors must remain age-appropriate and non-sexualized.",
        "No character face swaps, costume redesigns, prop redesigns, or scene drift.",
    ]
    if target.item_id == "OP_SHOT_021":
        reject.append("This item is already accepted for workprint; only rerender if a later identity QA explicitly fails it.")
    return "\n".join(
        [
            f"# {target.item_id} identity/detail repair prompt",
            "",
            "Use case: photorealistic-natural",
            f"Asset type: official replacement keyframe candidate for Reference-003, `{target.item_id}`",
            f"Priority: {target.priority}",
            f"Action: `{target.action}`",
            f"Hard replace: `{target.hard_replace}`",
            "",
            "## Primary Request",
            "",
            PROMPT_PRIMARY[target.item_id],
            "",
            "## Dense Video Reference Frames",
            "",
            "Use these for timing, body pose, camera angle, motion beat, and scene layout only:",
            *[f"- `{path}`" for path in selected_paths],
            "",
            "## Locked Assets",
            "",
            "Use these as the source of truth for identity, costumes, props, and continuity:",
            *lock_lines,
            "",
            "## Current Output To Replace Or QA",
            "",
            f"- Current board image: `{current}`",
            f"- Director/QA note: {target.notes}",
            "",
            "## Rejection Conditions",
            "",
            *[f"- {line}" for line in reject],
            "",
            "## Output Requirements",
            "",
            "- 21:9 image, 1915x821 or higher, pure image only.",
            "- Preserve the reference-video shot function while remaking it as a clean live-action/keyframe image.",
            "- Make the frame usable as an AIGC video anchor, not a poster or marketing still.",
            "",
        ]
    )


def write_job(
    targets: list[RepairTarget],
    rows_by_item: dict[str, dict[str, Any]],
    selected_by_item: dict[str, list[dict[str, Any]]],
    lock_package: list[dict[str, Any]],
    asset_locks: dict[str, Any],
    combined_sheet: Path,
) -> None:
    prompts_dir = JOB_DIR / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    locks = asset_lock_paths(asset_locks)
    items: list[dict[str, Any]] = []
    pack_lines = [
        "# Reference-003 Identity Repair R1 Prompt Pack",
        "",
        "Generate/replace images before any further video assembly.",
        "",
    ]
    for target in targets:
        row = dict(rows_by_item[target.item_id])
        row["selected_refs"] = selected_by_item[target.item_id]
        prompt = prompt_for_target(target, row, locks)
        prompt_path = prompts_dir / f"{target.item_id}_identity_repair_prompt.md"
        prompt_path.write_text(prompt)
        pack_lines.extend([f"## {target.item_id}", "", prompt])
        items.append(
            {
                "item_id": target.item_id,
                "priority": target.priority,
                "label": target.label,
                "hard_replace": target.hard_replace,
                "action": target.action,
                "current_output_path": row.get("output_path"),
                "prompt_path": rel(prompt_path),
                "selected_reference_frames": selected_by_item[target.item_id],
                "locks": list(target.locks),
                "notes": target.notes,
            }
        )
    (prompts_dir / "BATCH_identity_repair_R1_prompt_pack.md").write_text("\n".join(pack_lines))
    manifest = {
        "schema_version": "reference003_identity_repair_r1",
        "project_slug": "blue-water-citypop-op",
        "created_at": datetime.now(TZ).isoformat(timespec="seconds"),
        "status": "ready_for_image_generation",
        "boundary": "Image repair and dense reference package only. Do not assemble final video until replacement images pass identity/asset QA.",
        "setting_chapter": rel(SETTING_CHAPTER_PATH),
        "asset_lock_manifest": rel(ASSET_LOCKS_PATH),
        "dense_reference_manifest": rel(ANALYSIS_DIR / "manifest.json"),
        "combined_dense_reference_sheet": rel(combined_sheet),
        "packaged_asset_locks": lock_package,
        "items": items,
    }
    (JOB_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    readme = [
        "# Reference-003 Identity Repair R1",
        "",
        "This batch comes before any new video assembly.",
        "",
        "## Required Order",
        "",
        "1. Generate hard replacements first: `OP_SHOT_025`, `OP_SHOT_034`, and the `OP_SHOT_024` vehicle/action craft lock.",
        "2. QA the high-risk continuity frames: `OP_SHOT_018`, `OP_SHOT_019`, `OP_SHOT_020`, `OP_SHOT_023`, `OP_SHOT_032`, `OP_SHOT_033`.",
        "3. Update the board outputs only after identity/asset continuity passes.",
        "4. Assemble preview video last.",
        "",
        f"- Dense reference sheet: `{rel(combined_sheet)}`",
        f"- Prompt pack: `{rel(prompts_dir / 'BATCH_identity_repair_R1_prompt_pack.md')}`",
    ]
    (JOB_DIR / "README.md").write_text("\n".join(readme) + "\n")


def main() -> int:
    if not SOURCE_VIDEO.exists():
        raise SystemExit(f"Missing source video: {SOURCE_VIDEO}")
    if not FFMPEG.exists():
        raise SystemExit(f"Missing ffmpeg: {FFMPEG}")
    ensure_clean_dir(ANALYSIS_DIR)
    ensure_clean_dir(JOB_DIR)
    rows_by_item = current_rows()
    asset_locks = load_json(ASSET_LOCKS_PATH)

    selected_by_item: dict[str, list[dict[str, Any]]] = {}
    target_reports: list[dict[str, Any]] = []
    combined_rows: list[dict[str, Any]] = []
    for target in TARGETS:
        candidates = extract_candidates(target)
        metrics = analyze_candidates(target, candidates)
        selected = select_metrics(target, metrics)
        for row in selected:
            row["item_id"] = target.item_id
        selected_by_item[target.item_id] = selected
        combined_rows.extend(selected)
        sheet = ANALYSIS_DIR / "sheets" / f"{target.item_id}_dense_selected_sheet.jpg"
        make_sheet(selected, sheet, f"{target.item_id} dense selected frames", columns=3)
        target_reports.append(
            {
                "item_id": target.item_id,
                "label": target.label,
                "priority": target.priority,
                "hard_replace": target.hard_replace,
                "window_sec": [target.start_sec, target.end_sec],
                "center_sec": target.center_sec,
                "candidate_count": len(candidates),
                "selected_count": len(selected),
                "selected_sheet": rel(sheet),
                "selected_frames": selected,
                "action": target.action,
                "notes": target.notes,
            }
        )

    combined_sheet = ANALYSIS_DIR / "reference003_identity_repair_dense_selected_sheet.jpg"
    make_sheet(combined_rows, combined_sheet, "Reference-003 identity repair dense selected frames", columns=4)
    manifest = {
        "schema_version": "reference003_dense_repair_frames_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": datetime.now(TZ).isoformat(timespec="seconds"),
        "source_video": rel(SOURCE_VIDEO),
        "fps": FPS,
        "selection_strategy": [
            "center_time",
            "top_sharp_detail",
            "top_motion_change",
            "window_start",
            "window_end",
        ],
        "combined_sheet": rel(combined_sheet),
        "targets": target_reports,
    }
    (ANALYSIS_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    md_lines = [
        "# Reference-003 Dense Repair Frames",
        "",
        f"- Created: `{manifest['created_at']}`",
        f"- Source video: `{manifest['source_video']}`",
        f"- Candidate fps: `{FPS}`",
        f"- Combined sheet: `{manifest['combined_sheet']}`",
        "",
        "| Item | Priority | Hard replace | Candidates | Selected | Action |",
        "|---|---:|---|---:|---:|---|",
    ]
    for report in target_reports:
        md_lines.append(
            f"| `{report['item_id']}` | {report['priority']} | `{report['hard_replace']}` | {report['candidate_count']} | {report['selected_count']} | `{report['action']}` |"
        )
    (ANALYSIS_DIR / "README.md").write_text("\n".join(md_lines) + "\n")

    lock_package = copy_locks(asset_locks)
    copy_selected_refs(selected_by_item)
    write_job(TARGETS, rows_by_item, selected_by_item, lock_package, asset_locks, combined_sheet)
    print(
        json.dumps(
            {
                "status": "ready_for_image_generation",
                "targets": len(TARGETS),
                "dense_reference_manifest": rel(ANALYSIS_DIR / "manifest.json"),
                "combined_sheet": rel(combined_sheet),
                "job_manifest": rel(JOB_DIR / "manifest.json"),
                "prompt_pack": rel(JOB_DIR / "prompts/BATCH_identity_repair_R1_prompt_pack.md"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
