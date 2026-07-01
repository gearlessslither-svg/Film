#!/usr/bin/env python3
"""Refresh R7 promoted-candidate generated asset metadata.

Run this after copying newly generated candidate PNGs into the planned output
paths. The script updates generated_output_path fields in the queue and writes
per-priority manifests, contact sheets, anchor addenda, and the remaining P3
generation plan.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw


JOB_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = JOB_DIR.parents[2]
QUEUE_PATH = JOB_DIR / "reference003_r7_candidate_image_generation_queue.json"
PRIORITY_CONFIG = {
    "P1_generate_next_small_batch": {
        "slug": "p1",
        "label": "P1",
        "manifest_name": "reference003_r7_p1_generated_assets_manifest",
        "partial": False,
    },
    "P2_review_after_p1": {
        "slug": "p2",
        "label": "P2",
        "manifest_name": "reference003_r7_p2_generated_assets_manifest",
        "partial": False,
    },
    "P3_reference_video_or_already_handled": {
        "slug": "p3",
        "label": "P3",
        "manifest_name": "reference003_r7_p3_generated_assets_manifest",
        "partial": True,
    },
}


def rel(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def load_queue() -> dict[str, Any]:
    return json.loads(QUEUE_PATH.read_text(encoding="utf-8"))


def image_size(path: Path) -> tuple[int, int]:
    with Image.open(path) as image:
        return image.size


def sync_generated_fields(queue: dict[str, Any], now: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for priority, config in PRIORITY_CONFIG.items():
        generated = 0
        for item in queue.get("items", []):
            if item.get("priority") != priority:
                continue
            planned = item.get("planned_output_path")
            if not planned:
                continue
            path = PROJECT_ROOT / planned
            if not path.exists():
                continue
            width, height = image_size(path)
            generated += 1
            item["status"] = (
                "generated_asset_ready_pending_review"
                if config["partial"]
                else "generated_asset_ready"
            )
            item["generated_output_path"] = planned
            item["generated_width"] = width
            item["generated_height"] = height
            item["generated_manifest_path"] = rel(JOB_DIR / f"{config['manifest_name']}.json")
            item.setdefault("generated_at", now)
        counts[config["slug"]] = generated
        queue[f"{config['slug']}_generated_count"] = generated
    queue["updated_at"] = now
    p1_total = queue.get("p1_count", 0)
    p2_total = queue.get("p2_count", 0)
    p3_total = queue.get("p3_count", 0)
    if counts.get("p1") == p1_total and counts.get("p2") == p2_total and counts.get("p3") == p3_total:
        queue["status"] = "all_generated_assets_ready"
    elif counts.get("p1") == p1_total and counts.get("p2") == p2_total:
        queue["status"] = f"p3_partial_generated_{counts.get('p3', 0)}_of_{p3_total}"
    elif counts.get("p1") == p1_total:
        queue["status"] = f"p2_partial_generated_{counts.get('p2', 0)}_of_{p2_total}"
    else:
        queue["status"] = f"p1_partial_generated_{counts.get('p1', 0)}_of_{p1_total}"
    return counts


def generated_items(queue: dict[str, Any], priority: str) -> list[dict[str, Any]]:
    return [
        item
        for item in queue.get("items", [])
        if item.get("priority") == priority and item.get("generated_output_path")
    ]


def all_items(queue: dict[str, Any], priority: str) -> list[dict[str, Any]]:
    return [item for item in queue.get("items", []) if item.get("priority") == priority]


def manifest_rows(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for index, item in enumerate(items, 1):
        output_path = item["generated_output_path"]
        width, height = image_size(PROJECT_ROOT / output_path)
        rows.append(
            {
                "index": index,
                "asset_id": item["asset_id"],
                "unit": item.get("parent_video_unit_id"),
                "unit_title": item.get("unit_title", ""),
                "role": item.get("role", ""),
                "source_timecode": item.get("source_timecode", ""),
                "source_time_sec": item.get("source_time_sec"),
                "size": f"{width}x{height}",
                "ratio": round(width / height, 4) if height else None,
                "status": item.get("status", ""),
                "generated_output_path": output_path,
                "reference_frame_path": item.get("reference_frame_path", ""),
                "image_prompt": item.get("image_prompt", ""),
            }
        )
    return rows


def write_manifest(config: dict[str, Any], items: list[dict[str, Any]], total: int, now: str) -> None:
    rows = manifest_rows(items)
    complete = len(items) == total
    status = "generated_pending_director_review" if complete else "partial_generated_pending_director_review"
    suffix = "" if complete else "_partial"
    base = JOB_DIR / f"{config['manifest_name']}{suffix}"
    manifest = {
        "created_at": now,
        "status": status,
        "priority": config["label"],
        "ready": f"{len(items)}/{total}",
        "items": rows,
    }
    (base.with_suffix(".json")).write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = [
        f"# REFERENCE003 R7 {config['label']} Generated Assets Manifest"
        + (" (Partial)" if not complete else ""),
        "",
        f"- Created: {now}",
        f"- Status: `{status}`",
        f"- Ready: {len(items)}/{total}",
        "",
        "| # | Asset | Unit | Time | Role | Size | Ratio | Status | Generated output |",
        "|---:|---|---|---:|---|---|---:|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['index']} | `{row['asset_id']}` | `{row['unit']}` | "
            f"{row['source_timecode']} | {row['role']} | {row['size']} | "
            f"{row['ratio']} | `{row['status']}` | `{row['generated_output_path']}` |"
        )
    lines += [
        "",
        "## Notes",
        "",
        f"- {config['label']} candidate screenshots converted into pure generated image assets: {len(items)}/{total}.",
        "- Candidate screenshots remain audit references only; generated_output_path is the usable asset path.",
        "- Fit/pad generated anchors onto a common 21:9 canvas rather than stretching.",
    ]
    (base.with_suffix(".md")).write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_addendum(config: dict[str, Any], items: list[dict[str, Any]], total: int, now: str) -> None:
    complete = len(items) == total
    suffix = "" if complete else "_partial"
    path = JOB_DIR / f"reference003_r7_{config['slug']}_generated_anchor_addendum{suffix}.md"
    lines = [
        f"# REFERENCE003 R7 {config['label']} Generated Anchor Addendum"
        + (" (Partial)" if not complete else ""),
        "",
        f"- Created: {now}",
        f"- Generated assets: {len(items)}/{total}",
        "",
        "| Unit | Time | Asset | Generated image | Source screenshot |",
        "|---|---:|---|---|---|",
    ]
    for item in items:
        lines.append(
            f"| `{item.get('parent_video_unit_id')}` | {item.get('source_timecode', '')} | "
            f"`{item.get('asset_id')}` | `{item.get('generated_output_path')}` | "
            f"`{item.get('reference_frame_path', '')}` |"
        )
    lines += [
        "",
        "## Operational Notes",
        "",
        "- Generated image paths are pure-image assets pending director approval.",
        "- Candidate screenshots are not final assets.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_contact_sheet(config: dict[str, Any], items: list[dict[str, Any]], total: int) -> None:
    if not items:
        return
    complete = len(items) == total
    suffix = "" if complete else "_partial"
    path = JOB_DIR / f"reference003_r7_{config['slug']}_generated_assets_contact_sheet{suffix}.jpg"
    thumb_w, thumb_h, label_h = 360, 154, 52
    cols = 5 if len(items) >= 10 else 4
    rows = (len(items) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    for index, item in enumerate(items, 1):
        image = Image.open(PROJECT_ROOT / item["generated_output_path"]).convert("RGB")
        image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        cell_x = ((index - 1) % cols) * thumb_w
        cell_y = ((index - 1) // cols) * (thumb_h + label_h)
        sheet.paste(image, (cell_x + (thumb_w - image.width) // 2, cell_y))
        label = f"{index:02d} {item['asset_id']}\n{item.get('source_timecode', '')} {item.get('role', '')}"
        draw.text((cell_x + 6, cell_y + thumb_h + 4), label, fill=(0, 0, 0))
    sheet.save(path, quality=92)


def write_remaining_p3_plan(queue: dict[str, Any], now: str) -> None:
    remaining = [
        item
        for item in queue.get("items", [])
        if item.get("priority") == "P3_reference_video_or_already_handled"
        and not item.get("generated_output_path")
    ]
    path = JOB_DIR / "reference003_r7_p3_remaining_generation_plan.md"
    lines = [
        "# REFERENCE003 R7 P3 Remaining Generation Plan",
        "",
        f"- Created: {now}",
        f"- Remaining P3 assets: {len(remaining)}",
        "- Continue in order; do not regenerate P1, P2, or P3 items already carrying `generated_output_path`.",
        "- After completion, rerun this script and then run `09_edit/rough_cut/build_reference003_r7_generated_candidate_preview.py` without `--allow-partial`.",
        "",
    ]
    if remaining:
        first = remaining[0]
        lines += [
            "## Next Item",
            "",
            f"- Asset: `{first.get('asset_id')}`",
            f"- Time: `{first.get('source_timecode', '')}`",
            f"- Unit: `{first.get('parent_video_unit_id', '')}`",
            f"- Planned output: `{first.get('planned_output_path', '')}`",
            "",
        ]
    lines += [
        "## Remaining Items",
        "",
        "| # | Time | Asset | Unit | Role | Planned output |",
        "|---:|---:|---|---|---|---|",
    ]
    for index, item in enumerate(remaining, 1):
        lines.append(
            f"| {index} | {item.get('source_timecode', '')} | `{item.get('asset_id', '')}` | "
            f"`{item.get('parent_video_unit_id', '')}` | {item.get('role', '')} | "
            f"`{item.get('planned_output_path', '')}` |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_queue_summary_md(queue: dict[str, Any]) -> None:
    path = JOB_DIR / "reference003_r7_candidate_image_generation_queue.md"
    p1 = queue.get("p1_generated_count", 0)
    p2 = queue.get("p2_generated_count", 0)
    p3 = queue.get("p3_generated_count", 0)
    p1_total = queue.get("p1_count", 0)
    p2_total = queue.get("p2_count", 0)
    p3_total = queue.get("p3_count", 0)
    next_p3 = next(
        (
            item
            for item in queue.get("items", [])
            if item.get("priority") == "P3_reference_video_or_already_handled"
            and not item.get("generated_output_path")
        ),
        None,
    )
    lines = [
        "# Reference-003 R7 Candidate Image Generation Queue",
        "",
        f"- Status: `{queue.get('status')}`",
        f"- P1: {p1} generated / {p1_total}",
        f"- P2: {p2} generated / {p2_total}",
        f"- P3: {p3} generated / {p3_total}",
        "- P1 contact sheet: `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/reference003_r7_p1_generated_assets_contact_sheet.jpg`",
        "- P2 contact sheet: `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/reference003_r7_p2_generated_assets_contact_sheet.jpg`",
        "- P3 contact sheet: `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/reference003_r7_p3_generated_assets_contact_sheet"
        + ("_partial" if p3 < p3_total else "")
        + ".jpg`",
    ]
    if next_p3:
        lines.append(
            f"- Next P3 item: `{next_p3.get('asset_id')}` at `{next_p3.get('source_timecode')}`, "
            f"planned output `{next_p3.get('planned_output_path')}`"
        )
    lines += [
        "",
        "Candidates are screenshots, not final assets. Generated candidates carry `generated_output_path` in the JSON queue.",
        "Continue from the first P3 item without `generated_output_path`, then rerun `update_r7_promoted_candidate_manifests.py`.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true", help="Report current counts without writing files.")
    args = parser.parse_args()

    now = dt.datetime.now().replace(microsecond=0).isoformat()
    queue = load_queue()
    counts = sync_generated_fields(queue, now)
    if args.check_only:
        print(json.dumps({"status": queue.get("status"), "counts": counts}, ensure_ascii=False, indent=2))
        return 0

    for priority, config in PRIORITY_CONFIG.items():
        items = generated_items(queue, priority)
        total = len(all_items(queue, priority))
        write_manifest(config, items, total, now)
        write_addendum(config, items, total, now)
        write_contact_sheet(config, items, total)
    write_remaining_p3_plan(queue, now)
    write_queue_summary_md(queue)
    QUEUE_PATH.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": queue.get("status"), "counts": counts}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
