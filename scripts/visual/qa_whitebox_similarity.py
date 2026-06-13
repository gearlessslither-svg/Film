#!/usr/bin/env python3
"""Detect repeated or near-repeated whitebox frames.

This is a semantic guardrail for storyboard whiteboxes. A render can pass file,
aspect, exposure, and center-visibility checks while still being useless because
several panels share the same effective camera. This script flags those clusters.
"""

from __future__ import annotations

import argparse
import csv
import itertools
from pathlib import Path

from PIL import Image, ImageChops, ImageStat


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def tiny_image(path: Path) -> Image.Image:
    return Image.open(path).convert("L").resize((64, 36), Image.Resampling.BILINEAR)


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


def mad(a: Image.Image, b: Image.Image) -> float:
    return float(ImageStat.Stat(ImageChops.difference(a, b)).mean[0])


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


def build_items(project_root: Path, rows: list[dict[str, str]]) -> list[dict[str, object]]:
    items: list[dict[str, object]] = []
    for row in rows:
        path = project_root / row["planned_whitebox_path"]
        if not path.exists():
            continue
        image = tiny_image(path)
        items.append({**row, "_image": image, "_dhash": dhash(image)})
    return items


def pair_is_near_duplicate(a: dict[str, object], b: dict[str, object], mad_threshold: float, dhash_threshold: int) -> tuple[bool, float, int]:
    score_mad = mad(a["_image"], b["_image"])  # type: ignore[arg-type]
    score_hash = hamming(str(a["_dhash"]), str(b["_dhash"]))
    return score_mad <= mad_threshold or score_hash <= dhash_threshold, score_mad, score_hash


def run(project_root: Path, checklist_path: Path, out_path: Path, mad_threshold: float, dhash_threshold: int) -> tuple[int, int, int]:
    rows = read_csv(checklist_path)
    items = build_items(project_root, rows)
    uf = UnionFind(len(items))
    pair_notes: dict[tuple[int, int], tuple[float, int]] = {}

    for i, j in itertools.combinations(range(len(items)), 2):
        if items[i].get("scene_id") != items[j].get("scene_id"):
            continue
        is_dup, score_mad, score_hash = pair_is_near_duplicate(items[i], items[j], mad_threshold, dhash_threshold)
        if is_dup:
            uf.union(i, j)
            pair_notes[(i, j)] = (score_mad, score_hash)

    clusters: dict[int, list[int]] = {}
    for i in range(len(items)):
        clusters.setdefault(uf.find(i), []).append(i)
    large_clusters = [cluster for cluster in clusters.values() if len(cluster) >= 3]
    large_clusters.sort(key=len, reverse=True)

    report_rows: list[dict[str, str]] = []
    for cluster_idx, cluster in enumerate(large_clusters, start=1):
        cluster_id = f"DUP{cluster_idx:03d}"
        first = cluster[0]
        for idx in cluster:
            row = items[idx]
            adjacent_flags = []
            for other in (idx - 1, idx + 1):
                if other < 0 or other >= len(items):
                    continue
                if items[other].get("batch") != row.get("batch"):
                    continue
                is_dup, score_mad, score_hash = pair_is_near_duplicate(row, items[other], mad_threshold, dhash_threshold)
                if is_dup:
                    adjacent_flags.append(f"{items[other].get('panel_id')} mad={score_mad:.2f} dh={score_hash}")
            report_rows.append(
                {
                    "duplicate_cluster": cluster_id,
                    "cluster_size": str(len(cluster)),
                    "panel_id": str(row.get("panel_id", "")),
                    "batch": str(row.get("batch", "")),
                    "scene_id": str(row.get("scene_id", "")),
                    "source_camera": str(row.get("source_camera", "")),
                    "whitebox_id": str(row.get("whitebox_id", "")),
                    "reference_panel": str(items[first].get("panel_id", "")),
                    "adjacent_near_duplicate": "; ".join(adjacent_flags),
                    "severity": "fail",
                    "recommended_action": "Create panel-specific camera/blocking or explicitly mark this as an intentional hold before pure image generation.",
                    "planned_whitebox_path": str(row.get("planned_whitebox_path", "")),
                }
            )

    fieldnames = [
        "duplicate_cluster",
        "cluster_size",
        "panel_id",
        "batch",
        "scene_id",
        "source_camera",
        "whitebox_id",
        "reference_panel",
        "adjacent_near_duplicate",
        "severity",
        "recommended_action",
        "planned_whitebox_path",
    ]
    write_csv(out_path, report_rows, fieldnames)
    return len(large_clusters), len(report_rows), len(items)


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect near-duplicate whitebox renders.")
    parser.add_argument("--project-root", default=".", help="Path to 01_AIGC project root")
    parser.add_argument("--checklist", default="exports/whitebox_qa_checklist.csv")
    parser.add_argument("--out", default="exports/whitebox_similarity_report.csv")
    parser.add_argument("--mad-threshold", type=float, default=3.5)
    parser.add_argument("--dhash-threshold", type=int, default=3)
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    clusters, flagged, total = run(
        project_root,
        project_root / args.checklist,
        project_root / args.out,
        args.mad_threshold,
        args.dhash_threshold,
    )
    print(f"similarity_clusters={clusters} flagged_frames={flagged} checked_frames={total}")
    return 1 if flagged else 0


if __name__ == "__main__":
    raise SystemExit(main())
