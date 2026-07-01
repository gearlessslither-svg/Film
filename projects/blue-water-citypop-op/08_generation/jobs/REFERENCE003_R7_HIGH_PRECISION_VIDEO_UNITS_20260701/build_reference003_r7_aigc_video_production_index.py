#!/usr/bin/env python3
"""Build production-ready per-unit AIGC video material indexes."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from typing import Any


JOB_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = JOB_DIR.parents[2]
PROMPT_INDEX_DIR = JOB_DIR / "_PROMPT_INDEX"
PRODUCTION_PROMPT_DIR = PROMPT_INDEX_DIR / "PRODUCTION_READY_PROMPT_ONLY"
PROMOTED_JOB_DIR = PROJECT_ROOT / "08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701"
QUEUE_PATH = PROMOTED_JOB_DIR / "reference003_r7_candidate_image_generation_queue.json"
PREVIEW_MP4 = (
    "09_edit/rough_cut/"
    "reference003_r7_generated_candidate_animatic_1080p_with_music_20260701.mp4"
)
PREVIEW_MANIFEST = (
    "09_edit/rough_cut/r7_generated_candidate_preview/"
    "reference003_r7_generated_candidate_preview_manifest.json"
)


def rel(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def exists(rel_path: str) -> bool:
    return (PROJECT_ROOT / rel_path).exists()


def timecode(seconds: float | int | None) -> str:
    if seconds is None:
        return "00:00.00"
    total = float(seconds)
    minutes = int(total // 60)
    secs = total - minutes * 60
    return f"{minutes:02d}:{secs:05.2f}"


def unit_time_range(unit: dict[str, Any]) -> str:
    start = unit.get("start")
    end = unit.get("end")
    if isinstance(start, dict):
        start_tc = start.get("timecode") or timecode(start.get("sec"))
    else:
        start_tc = timecode(start)
    if isinstance(end, dict):
        end_tc = end.get("timecode") or timecode(end.get("sec"))
    else:
        end_tc = timecode(end)
    return f"{start_tc}-{end_tc}"


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_unit_manifests() -> list[dict[str, Any]]:
    manifests = []
    for path in sorted(JOB_DIR.glob("VU_REF003_R7_*/manifest.json")):
        data = read_json(path)
        data["_manifest_path"] = rel(path)
        data["_unit_dir"] = rel(path.parent)
        manifests.append(data)
    return sorted(manifests, key=lambda item: item["unit"]["order"])


def load_candidates_by_unit() -> dict[str, list[dict[str, Any]]]:
    queue = read_json(QUEUE_PATH)
    by_unit: dict[str, list[dict[str, Any]]] = {}
    for item in queue.get("items", []):
        unit_id = item.get("parent_video_unit_id")
        generated_path = item.get("generated_output_path") or item.get("planned_output_path")
        if not unit_id or not generated_path:
            continue
        row = {
            "asset_id": item.get("asset_id"),
            "role": item.get("role", ""),
            "source_time_sec": item.get("source_time_sec"),
            "source_timecode": item.get("source_timecode", ""),
            "priority": item.get("priority", ""),
            "status": item.get("status", ""),
            "unit_title": item.get("unit_title", ""),
            "difference_reason": item.get("difference_reason", ""),
            "reference_frame_path": item.get("reference_frame_path", ""),
            "generated_output_path": generated_path,
            "image_prompt": item.get("image_prompt", ""),
            "exists": exists(generated_path),
        }
        by_unit.setdefault(unit_id, []).append(row)
    for rows in by_unit.values():
        rows.sort(key=lambda row: (row.get("source_time_sec") or 0, row.get("asset_id") or ""))
    return by_unit


def upload_image_rows(unit_manifest: dict[str, Any], r7_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for anchor in unit_manifest.get("ordered_generated_anchors", []):
        path = anchor.get("packaged_path") or anchor.get("source_path")
        rows.append(
            {
                "kind": anchor.get("kind", "anchor"),
                "id": anchor.get("item_id", ""),
                "timecode": anchor.get("timecode", ""),
                "role": anchor.get("role", ""),
                "path": path,
                "exists": exists(path) if path else False,
            }
        )
    for item in r7_rows:
        rows.append(
            {
                "kind": "r7_generated_candidate",
                "id": item.get("asset_id", ""),
                "timecode": item.get("source_timecode", ""),
                "role": item.get("role", ""),
                "path": item.get("generated_output_path", ""),
                "exists": item.get("exists", False),
            }
        )
    for lock in unit_manifest.get("active_asset_locks", []):
        path = lock.get("global_lock_path") or lock.get("source_path")
        rows.append(
            {
                "kind": f"asset_lock:{lock.get('group', '')}",
                "id": lock.get("asset_id", ""),
                "timecode": "",
                "role": lock.get("status", ""),
                "path": path,
                "exists": exists(path) if path else False,
            }
        )
    return rows


def prompt_doc_name(unit: dict[str, Any]) -> str:
    return f"{unit['order']:02d}_{unit['unit_id']}_PRODUCTION_READY.md"


def write_unit_prompt(unit_manifest: dict[str, Any], r7_rows: list[dict[str, Any]], now: str) -> str:
    unit = unit_manifest["unit"]
    reference_clip = unit_manifest["reference_clip"]["path"]
    expected_output = unit_manifest["expected_video_output_path"]
    all_images = upload_image_rows(unit_manifest, r7_rows)
    prompt_path = PRODUCTION_PROMPT_DIR / prompt_doc_name(unit)

    lines = [
        f"# {unit['order']:02d} - {unit['unit_id']} - {unit['title']}",
        "",
        f"- Created: {now}",
        "- Status: production-ready AIGC video input pack",
        f"- Time range: `{unit_time_range(unit)}`",
        f"- Shot intent: {unit.get('intent', '')}",
        "",
        "## Upload These",
        "",
        f"1. Reference video: `{reference_clip}`",
        "2. All image inputs below, in the listed order.",
        "3. This prompt document.",
        "",
        "## All Image Inputs",
        "",
        "| Kind | ID | Time | Role | Path |",
        "|---|---|---:|---|---|",
    ]
    for row in all_images:
        lines.append(
            f"| `{row['kind']}` | `{row['id']}` | {row['timecode']} | "
            f"{row['role']} | `{row['path']}` |"
        )

    if r7_rows:
        lines += [
            "",
            "## R7 Generated Candidate Anchors",
            "",
            "These are now pure generated image assets, not screenshot-only placeholders.",
            "",
            "| Asset | Time | Role | Generated image | Source reference frame |",
            "|---|---:|---|---|---|",
        ]
        for item in r7_rows:
            lines.append(
                f"| `{item['asset_id']}` | {item['source_timecode']} | {item['role']} | "
                f"`{item['generated_output_path']}` | `{item['reference_frame_path']}` |"
            )

    locks = unit_manifest.get("active_asset_locks", [])
    lines += [
        "",
        "## Active Asset Locks",
        "",
    ]
    if locks:
        for lock in locks:
            path = lock.get("global_lock_path") or lock.get("source_path", "")
            lines.append(f"- `{lock.get('asset_id')}` ({lock.get('status')}): `{path}`")
    else:
        lines.append("- none")

    lines += [
        "",
        "## Save Result To",
        "",
        f"`{expected_output}`",
        "",
        "## Prompt To Use",
        "",
        f"Generate a clean live-action remake segment for `{unit['unit_id']}`.",
        f"Time range: `{unit_time_range(unit)}`.",
        "",
        "Use the reference video clip as the primary source for timing, camera motion,",
        "screen direction, and edit rhythm. Use every image listed above as the visual",
        "world for identity, props, vehicle shapes, scene geometry, color, and continuity.",
        "The R7 generated candidate anchors are pure generated assets and should be",
        "treated as current image inputs.",
        "",
        f"Shot intent: {unit.get('intent', '')}",
        "",
        "Preserve active locks exactly when visible. Keep minors age-appropriate and",
        "non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,",
        "broadcaster marks, logos, watermarks, and random glyphs with clean no-text",
        "composition. Keep keyframes in timeline order.",
        "",
        "Reject if this segment absorbs a neighboring flash, drops a listed image input,",
        "invents readable text, redesigns visible locked assets, or turns a montage/short",
        "insert into a false continuous one-take.",
        "",
    ]
    prompt_path.write_text("\n".join(lines), encoding="utf-8")
    return rel(prompt_path)


def write_unit_readme(unit_manifest: dict[str, Any], prompt_path: str, r7_rows: list[dict[str, Any]], now: str) -> str:
    unit = unit_manifest["unit"]
    reference_clip = unit_manifest["reference_clip"]["path"]
    expected_output = unit_manifest["expected_video_output_path"]
    path = PROJECT_ROOT / unit_manifest["_unit_dir"] / "AIGC_VIDEO_PRODUCTION_READY.md"
    lines = [
        f"# {unit['unit_id']} Production Ready",
        "",
        f"- Created: {now}",
        f"- Reference clip: `{reference_clip}`",
        f"- Prompt document: `{prompt_path}`",
        f"- Expected returned MP4: `{expected_output}`",
        f"- Ordered anchors in this unit: {len(unit_manifest.get('ordered_generated_anchors', []))}",
        f"- R7 generated candidate images in this unit: {len(r7_rows)}",
        f"- Active locks: {len(unit_manifest.get('active_asset_locks', []))}",
        "",
        "Use the prompt document as the operator-facing upload checklist.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    return rel(path)


def write_indexes(rows: list[dict[str, Any]], now: str) -> None:
    json_path = PROMPT_INDEX_DIR / "AIGC_VIDEO_PRODUCTION_PACKAGE_INDEX.json"
    md_path = PROMPT_INDEX_DIR / "AIGC_VIDEO_PRODUCTION_PACKAGE_INDEX.md"
    package = {
        "created_at": now,
        "status": "production_ready",
        "project_slug": PROJECT_ROOT.name,
        "preview_mp4": PREVIEW_MP4,
        "preview_manifest": PREVIEW_MANIFEST,
        "unit_count": len(rows),
        "reference_clip_count": sum(1 for row in rows if row["reference_clip_exists"]),
        "production_prompt_count": sum(1 for row in rows if row["production_prompt_exists"]),
        "ordered_anchor_image_count": sum(row["ordered_anchor_count"] for row in rows),
        "r7_generated_candidate_image_count": sum(row["r7_generated_candidate_count"] for row in rows),
        "active_lock_image_count": sum(row["active_lock_count"] for row in rows),
        "units": rows,
    }
    json_path.write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Reference-003 R7 AIGC Video Production Package Index",
        "",
        f"- Created: {now}",
        "- Status: production-ready",
        f"- Full generated-candidate preview MP4: `{PREVIEW_MP4}`",
        f"- Preview manifest: `{PREVIEW_MANIFEST}`",
        f"- Units: {package['unit_count']}/36",
        f"- Reference clips: {package['reference_clip_count']}/36",
        f"- Production prompt docs: {package['production_prompt_count']}/36",
        f"- Ordered anchor images: {package['ordered_anchor_image_count']}",
        f"- R7 generated candidate images: {package['r7_generated_candidate_image_count']}",
        f"- Active lock images referenced: {package['active_lock_image_count']}",
        "",
        "## Per-Unit Materials",
        "",
        "| # | Unit | Reference clip | Production prompt | Anchors | R7 images | Locks | Expected MP4 |",
        "|---:|---|---|---|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['order']} | `{row['unit_id']}` | `{row['reference_clip']}` | "
            f"`{row['production_prompt']}` | {row['ordered_anchor_count']} | "
            f"{row['r7_generated_candidate_count']} | {row['active_lock_count']} | "
            f"`{row['expected_video_output_path']}` |"
        )
    lines += [
        "",
        "## Operator Note",
        "",
        "For each unit, upload the reference clip, every image listed in the production prompt,",
        "and that production prompt document. Generated segment MP4s should be returned to",
        "`08_generation/outputs/video/reference003_r7_high_precision_segments/` using the",
        "unit id as the filename.",
        "",
    ]
    md_path.write_text("\n".join(lines), encoding="utf-8")


def build(allow_partial: bool) -> dict[str, Any]:
    now = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).isoformat(timespec="seconds")
    PRODUCTION_PROMPT_DIR.mkdir(parents=True, exist_ok=True)
    units = load_unit_manifests()
    candidates_by_unit = load_candidates_by_unit()
    rows: list[dict[str, Any]] = []
    missing: list[str] = []

    for manifest in units:
        unit = manifest["unit"]
        unit_id = unit["unit_id"]
        r7_rows = candidates_by_unit.get(unit_id, [])
        prompt_path = write_unit_prompt(manifest, r7_rows, now)
        readme_path = write_unit_readme(manifest, prompt_path, r7_rows, now)
        manifest["production_prompt"] = prompt_path
        manifest["production_ready_readme"] = readme_path
        manifest["r7_generated_candidate_images"] = r7_rows
        Path(PROJECT_ROOT / manifest["_manifest_path"]).write_text(
            json.dumps({k: v for k, v in manifest.items() if not k.startswith("_")}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

        ref_clip = manifest["reference_clip"]["path"]
        prompt_exists = exists(prompt_path)
        ref_exists = exists(ref_clip)
        if not ref_exists:
            missing.append(ref_clip)
        if not prompt_exists:
            missing.append(prompt_path)
        for row in upload_image_rows(manifest, r7_rows):
            if not row.get("exists"):
                missing.append(row.get("path", ""))

        rows.append(
            {
                "order": unit["order"],
                "unit_id": unit_id,
                "title": unit["title"],
                "time_range": unit_time_range(unit),
                "reference_clip": ref_clip,
                "reference_clip_exists": ref_exists,
                "production_prompt": prompt_path,
                "production_prompt_exists": prompt_exists,
                "production_ready_readme": readme_path,
                "ordered_anchor_count": len(manifest.get("ordered_generated_anchors", [])),
                "r7_generated_candidate_count": len(r7_rows),
                "active_lock_count": len(manifest.get("active_asset_locks", [])),
                "expected_video_output_path": manifest["expected_video_output_path"],
            }
        )

    write_indexes(rows, now)
    status = "production_ready" if not missing else "missing_materials"
    if missing and not allow_partial:
        raise SystemExit(json.dumps({"status": status, "missing": missing[:40]}, ensure_ascii=False, indent=2))
    return {
        "status": status,
        "unit_count": len(rows),
        "reference_clip_count": sum(1 for row in rows if row["reference_clip_exists"]),
        "production_prompt_count": sum(1 for row in rows if row["production_prompt_exists"]),
        "ordered_anchor_image_count": sum(row["ordered_anchor_count"] for row in rows),
        "r7_generated_candidate_image_count": sum(row["r7_generated_candidate_count"] for row in rows),
        "active_lock_image_count": sum(row["active_lock_count"] for row in rows),
        "missing_count": len(missing),
        "index_md": rel(PROMPT_INDEX_DIR / "AIGC_VIDEO_PRODUCTION_PACKAGE_INDEX.md"),
        "index_json": rel(PROMPT_INDEX_DIR / "AIGC_VIDEO_PRODUCTION_PACKAGE_INDEX.json"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-partial", action="store_true")
    args = parser.parse_args()
    print(json.dumps(build(args.allow_partial), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
