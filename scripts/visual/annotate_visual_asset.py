#!/usr/bin/env python3
"""Create annotated working copies from pure visual assets.

This script never edits the pure image. It opens the pure image, adds a
right-side metadata panel, and writes an annotated copy for review.
"""

from __future__ import annotations

import argparse
import csv
import os
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def load_font(size: int) -> ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
        r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\arial.ttf",
    ]
    for candidate in candidates:
        if os.path.exists(candidate):
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default()


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, font: ImageFont.ImageFont, fill: str, width: int, line_gap: int = 5) -> int:
    x, y = xy
    # Rough width estimate works across fallback fonts.
    wrap_chars = max(12, width // max(8, font.size if hasattr(font, "size") else 14))
    for raw_line in str(text).splitlines() or [""]:
        for line in textwrap.wrap(raw_line, width=wrap_chars, break_long_words=False) or [""]:
            draw.text((x, y), line, font=font, fill=fill)
            bbox = draw.textbbox((x, y), line, font=font)
            y += (bbox[3] - bbox[1]) + line_gap
    return y


def annotate_one(project_root: Path, row: dict[str, str], panel_width: int = 520) -> bool:
    pure_path = project_root / row["pure_path"]
    annotated_path = project_root / row["annotated_path"]
    if not pure_path.exists():
        return False

    image = Image.open(pure_path).convert("RGB")
    w, h = image.size
    out = Image.new("RGB", (w + panel_width, h), (18, 18, 18))
    out.paste(image, (0, 0))
    draw = ImageDraw.Draw(out)

    title_font = load_font(24)
    label_font = load_font(16)
    body_font = load_font(15)

    x = w + 24
    y = 24
    draw.text((x, y), row.get("asset_id", pure_path.stem), font=title_font, fill="#ffffff")
    y += 38

    fields = [
        ("画幅", "aspect_ratio"),
        ("景别", "shot_size"),
        ("主体位置", "subject_position"),
        ("主体动作", "subject_action"),
        ("运动方向", "motion_direction"),
        ("镜头运动", "camera_movement"),
        ("前/中/背景", "foreground_midground_background"),
        ("光线", "lighting"),
        ("首帧", "start_frame"),
        ("尾帧", "end_frame"),
        ("中间帧", "needs_middle_frame"),
        ("生成风险", "generation_risk"),
        ("修正方案", "fix_plan"),
        ("隐藏剪辑", "hidden_cut_transition"),
    ]
    for label, key in fields:
        value = row.get(key, "")
        if not value:
            continue
        draw.text((x, y), label, font=label_font, fill="#8fd3ff")
        y += 22
        y = draw_wrapped(draw, (x, y), value, body_font, "#eeeeee", panel_width - 48)
        y += 8
        if y > h - 40:
            draw.text((x, h - 28), "...", font=body_font, fill="#eeeeee")
            break

    annotated_path.parent.mkdir(parents=True, exist_ok=True)
    out.save(annotated_path)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Create annotated working versions from pure images and metadata.")
    parser.add_argument("--project-root", default=".", help="Path to 01_AIGC project root")
    parser.add_argument("--metadata", default="exports/micro_storyboard_annotation_metadata.csv", help="Annotation metadata CSV")
    parser.add_argument("--asset-id", help="Only annotate one asset_id")
    parser.add_argument("--panel-width", type=int, default=520)
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    metadata_path = project_root / args.metadata
    if not metadata_path.exists():
        raise FileNotFoundError(metadata_path)

    attempted = 0
    created = 0
    missing: list[str] = []
    with metadata_path.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if args.asset_id and row.get("asset_id") != args.asset_id:
                continue
            attempted += 1
            if annotate_one(project_root, row, panel_width=args.panel_width):
                created += 1
            else:
                missing.append(row.get("pure_path", ""))

    print(f"attempted={attempted} created={created} missing={len(missing)}")
    for item in missing[:20]:
        print(f"missing: {item}")
    if len(missing) > 20:
        print(f"... and {len(missing) - 20} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
