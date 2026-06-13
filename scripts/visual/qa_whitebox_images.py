#!/usr/bin/env python3
"""Automatic QA for whitebox renders.

The check has two jobs:
1. Verify that every render is a healthy image: present, readable, 16:9,
   exposed, and not obviously blocked by a flat wall or foreground object.
2. Detect repeated or near-repeated renders. A whitebox can be technically
   valid but useless if many panels share the same effective camera.

Human review is still required for axis, story intent, and spatial continuity.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import math
import re
from pathlib import Path
from typing import Any

from PIL import Image, ImageChops, ImageStat


SIMILARITY_FIELDS = [
    "similarity_ok",
    "similarity_cluster",
    "similarity_reference",
    "similarity_score",
    "composition_reuse_ok",
    "composition_reuse_reason",
]


def bool_status(value: bool) -> str:
    return "pass" if value else "fail"


def ensure_fields(fieldnames: list[str], rows: list[dict[str, str]], fields: list[str]) -> list[str]:
    updated = list(fieldnames)
    for field in fields:
        if field not in updated:
            updated.append(field)
            for row in rows:
                row[field] = ""
    return updated


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def image_metrics(path: Path) -> dict[str, Any]:
    image = Image.open(path).convert("L")
    width, height = image.size
    stat = ImageStat.Stat(image)
    mean = float(stat.mean[0])
    stddev = float(stat.stddev[0])
    extrema = image.getextrema()

    # Center-crop metric catches cameras buried inside a flat wall or a giant
    # foreground object. It is not a semantic occlusion detector.
    cx0 = int(width * 0.35)
    cy0 = int(height * 0.30)
    cx1 = int(width * 0.65)
    cy1 = int(height * 0.70)
    center = image.crop((cx0, cy0, cx1, cy1))
    center_stat = ImageStat.Stat(center)
    center_mean = float(center_stat.mean[0])
    center_stddev = float(center_stat.stddev[0])

    hist = image.histogram()
    total = sum(hist) or 1
    dark_ratio = sum(hist[:16]) / total
    bright_ratio = sum(hist[240:]) / total

    return {
        "width": width,
        "height": height,
        "aspect": width / height if height else math.inf,
        "mean": mean,
        "stddev": stddev,
        "min": extrema[0],
        "max": extrema[1],
        "center_mean": center_mean,
        "center_stddev": center_stddev,
        "dark_ratio": dark_ratio,
        "bright_ratio": bright_ratio,
    }


def evaluate(metrics: dict[str, Any]) -> dict[str, str]:
    aspect_ok = abs(metrics["aspect"] - (16 / 9)) < 0.03
    exposure_ok = (
        20 <= metrics["mean"] <= 235
        and metrics["stddev"] >= 8
        and metrics["dark_ratio"] < 0.85
        and metrics["bright_ratio"] < 0.85
    )
    center_visible = metrics["center_stddev"] >= 5 and 15 <= metrics["center_mean"] <= 240
    auto_image_ok = aspect_ok and exposure_ok and center_visible
    return {
        "auto_image_ok": bool_status(auto_image_ok),
        "aspect_ok": bool_status(aspect_ok),
        "exposure_ok": bool_status(exposure_ok),
        "subject_visible": "review" if center_visible else "fail",
        "occlusion_ok": "review" if center_visible else "fail",
    }


def issue_type(row: dict[str, str], metrics: dict[str, Any] | None) -> str:
    if row.get("auto_file_ok") == "fail":
        return "missing_file"
    if metrics is None:
        return "unreadable"
    if row.get("aspect_ok") == "fail":
        return "wrong_aspect"
    if row.get("exposure_ok") == "fail":
        return "blank_or_flat"
    if row.get("subject_visible") == "fail" or row.get("occlusion_ok") == "fail":
        return "blocked_subject"
    return ""


def strip_auto_notes(notes: str) -> str:
    return re.sub(r"\s*auto_metrics width=.*$", "", notes or "").strip()


def tiny_image(path: Path) -> Image.Image:
    return Image.open(path).convert("L").resize((64, 36), Image.Resampling.BILINEAR)


def tiny_color_image(path: Path) -> Image.Image:
    return Image.open(path).convert("RGB").resize((64, 36), Image.Resampling.BILINEAR)


def dhash(image: Image.Image) -> str:
    small = image.resize((9, 8), Image.Resampling.BILINEAR)
    px = list(small.getdata())
    bits = []
    for y in range(8):
        for x in range(8):
            bits.append("1" if px[y * 9 + x] > px[y * 9 + x + 1] else "0")
    return "".join(bits)


def hamming(a: str, b: str) -> int:
    return sum(x != y for x, y in zip(a, b, strict=True))


def mean_absolute_difference(a: Image.Image, b: Image.Image) -> float:
    return float(ImageStat.Stat(ImageChops.difference(a, b)).mean[0])


def color_mean_absolute_difference(a: Image.Image, b: Image.Image) -> float:
    diff = ImageChops.difference(a, b)
    stat = ImageStat.Stat(diff)
    return float(sum(stat.mean[:3]) / 3)


def story_foreground_mask(image: Image.Image) -> list[int]:
    result = []
    for red, green, blue in image.getdata():
        high = max(red, green, blue)
        low = min(red, green, blue)
        saturation = high - low
        is_colored_proxy = saturation >= 22
        is_deep_story_proxy = high <= 58 and low <= 48
        result.append(1 if is_colored_proxy or is_deep_story_proxy else 0)
    return result


def foreground_difference(a: list[int], b: list[int]) -> float:
    if not a:
        return 0.0
    return sum(left != right for left, right in zip(a, b, strict=True)) / len(a)


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.parent[rb] = ra


def near_duplicate(
    a: dict[str, Any],
    b: dict[str, Any],
    mad_threshold: float,
    dhash_threshold: int,
) -> tuple[bool, float, int, float, float]:
    score_mad = mean_absolute_difference(a["_tiny"], b["_tiny"])
    score_hash = hamming(a["_dhash"], b["_dhash"])
    score_color = color_mean_absolute_difference(a["_tiny_color"], b["_tiny_color"])
    score_foreground = foreground_difference(a["_foreground_mask"], b["_foreground_mask"])
    base_close = score_mad <= mad_threshold or score_hash <= dhash_threshold
    # Gray whole-frame metrics are dominated by walls, floors, and corridors.
    # A whitebox is only treated as repeated when the story-colored foreground
    # blocking is also effectively unchanged.
    story_close = score_color <= 4.0 and score_foreground <= 0.025
    return base_close and story_close, score_mad, score_hash, score_color, score_foreground


def row_text(row: dict[str, Any]) -> str:
    return " ".join(
        str(row.get(key, ""))
        for key in ("character_blocking", "layout_focus", "pose_or_path")
    )


def has_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


SMALL_REUSE_TERMS = (
    "微", "轻", "固定", "locked-off", "fixed", "几乎静止", "不移动", "保持",
    "停", "悬停", "慢慢", "小步", "一拍", "闪", "光", "扫描线", "像素",
    "电话线", "听筒", "手", "指尖", "按钮", "屏幕", "CRT", "UI", "WIN",
    "INSERT", "idle", "特写", "呼吸", "嘴", "眼", "红领巾", "书包边缘",
)

HARD_CHANGE_TERMS = (
    "跑", "逃", "追", "堵住", "围", "挤", "起身", "甩", "队形", "转身",
    "横向", "擦镜", "离开", "走进", "走向", "向深处", "出场", "入场",
)

SMALL_OBJECT_TERMS = (
    "手", "指尖", "听筒", "电话线", "扫描线", "光", "眼", "嘴", "红领巾",
    "书包边缘", "按钮", "屏幕", "CRT", "UI", "WIN", "INSERT", "像素", "特写",
)


def micro_displacement_prompt(row: dict[str, Any]) -> str:
    subject = str(row.get("character_blocking", "")).strip()
    focus = str(row.get("layout_focus", "")).strip()
    pose = str(row.get("pose_or_path", "")).strip()
    pieces = []
    if subject:
        pieces.append(f"subject={subject}")
    if pose:
        pieces.append(f"micro_movement={pose}")
    if focus:
        pieces.append(f"story_focus={focus}")
    pieces.append("keep the shared whitebox composition and environment anchors unchanged")
    pieces.append("only change the stated micro movement, expression, prop state, light cue, or UI state")
    return "; ".join(pieces)


def composition_reuse_decision(row: dict[str, Any]) -> tuple[bool, str, str]:
    """Decide whether a near-duplicate composition can be intentional.

    Allowed reuse means the composition can stay stable and the prompt should
    carry the change through micro-expression, prop movement, light, texture,
    or UI state. It still requires human review; it is not a final pass.
    """
    text = row_text(row)
    scene = str(row.get("scene_id", ""))
    source = str(row.get("source_camera", ""))

    if has_any(text, HARD_CHANGE_TERMS) and not has_any(text, SMALL_OBJECT_TERMS):
        return False, "large blocking or screen-position change requires a distinct whitebox", ""

    if scene == "SCN_PHONE" and has_any(text, SMALL_REUSE_TERMS):
        return True, "phone-booth micro action/light/electronicization can reuse the same whitebox", micro_displacement_prompt(row)
    if scene == "SCN_8BIT" and has_any(text, ("WIN", "INSERT", "UI", "idle", "像素", "闪烁")):
        return True, "8-bit locked side-view or UI hold can reuse the same whitebox", micro_displacement_prompt(row)
    if source in {"CAM_PHONE_02_APPROACH_CLOSE", "CAM_PHONE_03_RECEIVER_INSERT"} and has_any(text, SMALL_OBJECT_TERMS):
        return True, "close insert movement stays under 10 percent of frame and can share whitebox", micro_displacement_prompt(row)
    if has_any(text, ("固定", "locked-off", "fixed", "几乎静止", "不移动", "保持")) and has_any(text, SMALL_REUSE_TERMS):
        return True, "intentional hold or fixed insert can share whitebox", micro_displacement_prompt(row)

    return False, "near-duplicate lacks an allowed small-displacement rationale", ""


def apply_similarity_qa(
    project_root: Path,
    rows: list[dict[str, str]],
    similarity_report_path: Path,
    mad_threshold: float,
    dhash_threshold: int,
) -> tuple[int, int]:
    """Fail repeated whiteboxes that hide a missing panel-specific design pass."""
    items: list[dict[str, Any]] = []
    for idx, row in enumerate(rows):
        row["similarity_ok"] = "not_checked"
        row["similarity_cluster"] = ""
        row["similarity_reference"] = ""
        row["similarity_score"] = ""
        row["composition_reuse_ok"] = "not_checked"
        row["composition_reuse_reason"] = ""
        if row.get("auto_file_ok") != "pass" or row.get("auto_image_ok") != "pass":
            continue
        image_path = project_root / row["planned_whitebox_path"]
        if not image_path.exists():
            continue
        tiny = tiny_image(image_path)
        tiny_color = tiny_color_image(image_path)
        items.append({
            **row,
            "_row_index": idx,
            "_tiny": tiny,
            "_tiny_color": tiny_color,
            "_foreground_mask": story_foreground_mask(tiny_color),
            "_dhash": dhash(tiny),
        })

    for item in items:
        rows[item["_row_index"]]["similarity_ok"] = "pass"

    uf = UnionFind(len(items))
    pair_scores: dict[tuple[int, int], tuple[float, int, float, float]] = {}
    adjacent_pairs: set[tuple[int, int]] = set()

    for i, j in itertools.combinations(range(len(items)), 2):
        if items[i].get("scene_id") != items[j].get("scene_id"):
            continue
        is_duplicate, score_mad, score_hash, score_color, score_foreground = near_duplicate(
            items[i], items[j], mad_threshold, dhash_threshold
        )
        if not is_duplicate:
            continue
        uf.union(i, j)
        pair_scores[(i, j)] = (score_mad, score_hash, score_color, score_foreground)
        row_gap = abs(int(items[i]["_row_index"]) - int(items[j]["_row_index"]))
        if row_gap == 1 and items[i].get("batch") == items[j].get("batch"):
            adjacent_pairs.add((i, j))

    clusters: dict[int, list[int]] = {}
    for idx in range(len(items)):
        clusters.setdefault(uf.find(idx), []).append(idx)
    large_clusters = [cluster for cluster in clusters.values() if len(cluster) >= 3]
    large_clusters.sort(key=len, reverse=True)

    duplicate_rows: list[dict[str, str]] = []
    flagged_indices: set[int] = set()
    hard_clusters = 0
    for cluster_number, cluster in enumerate(large_clusters, start=1):
        cluster_id = f"DUP{cluster_number:03d}"
        reference = str(items[cluster[0]].get("panel_id", ""))
        decisions = [composition_reuse_decision(items[idx]) for idx in cluster]
        cluster_allowed = all(decision[0] for decision in decisions)
        if not cluster_allowed:
            hard_clusters += 1
        for idx in cluster:
            item = items[idx]
            row_index = int(item["_row_index"])
            row = rows[row_index]
            row["similarity_cluster"] = cluster_id
            row["similarity_reference"] = reference
            row["similarity_score"] = f"cluster_size={len(cluster)}"
            allowed, reason, prompt_delta = composition_reuse_decision(item)
            if cluster_allowed:
                row["similarity_ok"] = "composition_reuse_review"
                row["composition_reuse_ok"] = "review"
                row["composition_reuse_reason"] = reason
                row["fix_action"] = (
                    f"Use shared whitebox {reference}; generate this as a separate pure image with prompt delta: {prompt_delta}"
                )
                row["notes"] = (
                    f"{row.get('notes', '')} composition_reuse {cluster_id} size={len(cluster)} "
                    f"ref={reference}; {reason}"
                ).strip()
            else:
                flagged_indices.add(row_index)
                row["similarity_ok"] = "fail"
                row["composition_reuse_ok"] = "fail" if not allowed else "review"
                row["composition_reuse_reason"] = reason
                row["panel_specific_ok"] = "fail"
                row["qa_status"] = "fail"
                row["issue_type"] = "near_duplicate_whitebox"
                row["fix_action"] = (
                    "Root cause: repeated source camera with only tiny offsets and no valid small-displacement rationale. "
                    "Create a panel-specific camera/blocking pass, or explicitly reclassify as composition reuse with a reason."
                )
                row["notes"] = f"{row.get('notes', '')} similarity {cluster_id} size={len(cluster)} ref={reference}".strip()
            duplicate_rows.append(
                {
                    "duplicate_cluster": cluster_id,
                    "cluster_size": str(len(cluster)),
                    "panel_id": row.get("panel_id", ""),
                    "batch": row.get("batch", ""),
                    "scene_id": row.get("scene_id", ""),
                    "source_camera": row.get("source_camera", ""),
                    "whitebox_id": row.get("whitebox_id", ""),
                    "reference_panel": reference,
                    "severity": "composition_reuse_review" if cluster_allowed else "fail",
                    "recommended_action": row.get("fix_action") or "Reuse this composition only with explicit prompt keywords and human review.",
                    "planned_whitebox_path": row.get("planned_whitebox_path", ""),
                    "composition_reuse_reason": reason,
                    "prompt_delta": prompt_delta,
                }
            )

    for i, j in adjacent_pairs:
        for idx, other_idx in ((i, j), (j, i)):
            item = items[idx]
            row_index = int(item["_row_index"])
            if row_index in flagged_indices:
                continue
            other = items[other_idx]
            score_mad, score_hash, score_color, score_foreground = pair_scores.get(
                tuple(sorted((idx, other_idx))), (0.0, 0, 0.0, 0.0)
            )
            row = rows[row_index]
            row["similarity_cluster"] = "ADJACENT"
            row["similarity_reference"] = str(other.get("panel_id", ""))
            row["similarity_score"] = (
                f"mad={score_mad:.2f};dhash={score_hash};"
                f"color={score_color:.2f};fg={score_foreground:.3f}"
            )
            allowed, reason, prompt_delta = composition_reuse_decision(row)
            if allowed:
                row["similarity_ok"] = "composition_reuse_review"
                row["composition_reuse_ok"] = "review"
                row["composition_reuse_reason"] = reason
                row["fix_action"] = (
                    f"Use shared adjacent whitebox {other.get('panel_id')}; generate this as a separate pure image "
                    f"with prompt delta: {prompt_delta}"
                )
            else:
                row["similarity_ok"] = "fail"
                row["composition_reuse_ok"] = "fail"
                row["composition_reuse_reason"] = reason
                row["adjacent_continuity_ok"] = "fail"
                row["panel_specific_ok"] = "fail"
                row["qa_status"] = "fail"
                row["issue_type"] = "adjacent_near_duplicate_whitebox"
                row["fix_action"] = "Adjacent panels are visually too similar; make the whitebox encode a real beat, camera, blocking, or hold rationale."
            row["notes"] = (
                f"{row.get('notes', '')} adjacent_similarity ref={other.get('panel_id')} "
                f"mad={score_mad:.2f} dh={score_hash} color={score_color:.2f} fg={score_foreground:.3f}"
            ).strip()

    report_fields = [
        "duplicate_cluster",
        "cluster_size",
        "panel_id",
        "batch",
        "scene_id",
        "source_camera",
        "whitebox_id",
        "reference_panel",
        "severity",
        "recommended_action",
        "planned_whitebox_path",
        "composition_reuse_reason",
        "prompt_delta",
    ]
    write_csv(similarity_report_path, duplicate_rows, report_fields)
    return hard_clusters, len(flagged_indices)


def run(
    project_root: Path,
    checklist_path: Path,
    out_path: Path | None,
    similarity_report_path: Path,
    mad_threshold: float,
    dhash_threshold: int,
) -> tuple[int, int, int, int, int]:
    with checklist_path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fieldnames = list(rows[0].keys()) if rows else []
    fieldnames = ensure_fields(fieldnames, rows, SIMILARITY_FIELDS)

    missing = 0
    for row in rows:
        row["issue_type"] = ""
        row["fix_action"] = ""
        row["similarity_ok"] = "not_checked"
        row["similarity_cluster"] = ""
        row["similarity_reference"] = ""
        row["similarity_score"] = ""
        image_path = project_root / row["planned_whitebox_path"]
        metrics: dict[str, Any] | None = None
        if not image_path.exists():
            row["auto_file_ok"] = "fail"
            row["auto_image_ok"] = "fail"
            row["qa_status"] = "fail"
            row["issue_type"] = "missing_file"
            row["fix_action"] = "Render this whitebox before pure image generation."
            missing += 1
            continue

        row["auto_file_ok"] = "pass"
        try:
            metrics = image_metrics(image_path)
            result = evaluate(metrics)
            row.update(result)
            if result["auto_image_ok"] == "pass":
                row["qa_status"] = "auto_pass_needs_human_review"
            else:
                row["qa_status"] = "fail"
                row["issue_type"] = issue_type(row, metrics)
                row["fix_action"] = "Adjust camera/render and rerun whitebox QA."
            base_notes = strip_auto_notes(row.get("notes", ""))
            metrics_note = (
                f"auto_metrics width={metrics['width']} height={metrics['height']} "
                f"mean={metrics['mean']:.1f} std={metrics['stddev']:.1f} "
                f"center_std={metrics['center_stddev']:.1f}"
            )
            row["notes"] = f"{base_notes} {metrics_note}".strip() if base_notes else metrics_note
        except Exception as exc:  # noqa: BLE001 - report bad image and continue.
            row["auto_image_ok"] = "fail"
            row["qa_status"] = "fail"
            row["issue_type"] = "unreadable"
            row["fix_action"] = "Re-render or replace unreadable whitebox image."
            row["notes"] = f"{row.get('notes','')} unreadable: {exc}".strip()

    similarity_clusters, similarity_flagged = apply_similarity_qa(
        project_root,
        rows,
        similarity_report_path,
        mad_threshold,
        dhash_threshold,
    )

    target = out_path or checklist_path
    write_csv(target, rows, fieldnames)

    passed = sum(1 for row in rows if row.get("qa_status") == "auto_pass_needs_human_review")
    failed = sum(1 for row in rows if row.get("qa_status") == "fail")
    return passed, failed, missing, similarity_clusters, similarity_flagged


def main() -> int:
    parser = argparse.ArgumentParser(description="Run automatic QA on whitebox renders.")
    parser.add_argument("--project-root", default=".", help="Path to 01_AIGC project root")
    parser.add_argument("--checklist", default="exports/whitebox_qa_checklist.csv")
    parser.add_argument("--out", help="Optional output CSV path. Defaults to updating checklist in place.")
    parser.add_argument("--similarity-report", default="exports/whitebox_similarity_report.csv")
    parser.add_argument("--mad-threshold", type=float, default=3.5)
    parser.add_argument("--dhash-threshold", type=int, default=3)
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    checklist_path = project_root / args.checklist
    out_path = project_root / args.out if args.out else None
    similarity_report_path = project_root / args.similarity_report

    passed, failed, missing, similarity_clusters, similarity_flagged = run(
        project_root,
        checklist_path,
        out_path,
        similarity_report_path,
        args.mad_threshold,
        args.dhash_threshold,
    )
    print(
        f"auto_pass_needs_human_review={passed} failed={failed} missing={missing} "
        f"similarity_clusters={similarity_clusters} similarity_flagged={similarity_flagged}"
    )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
