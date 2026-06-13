#!/usr/bin/env python3
"""Build final review storyboard panels and contact sheets.

This produces actual image deliverables for all 188 micro-storyboard panels.
Pure generated images are used when present; otherwise the validated panel-level
whitebox is used as the structural fallback and clearly marked in metadata.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


W, H = 1280, 720


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def load_font(size: int) -> ImageFont.ImageFont:
    for path in [
        r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\arial.ttf",
    ]:
        if Path(path).exists():
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


def fit_image(path: Path) -> Image.Image:
    image = Image.open(path).convert("RGB")
    iw, ih = image.size
    scale = min(W / iw, H / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    image = image.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (W, H), (10, 10, 10))
    canvas.paste(image, ((W - nw) // 2, (H - nh) // 2))
    return canvas


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> int:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int, max_lines: int) -> list[str]:
    text = " ".join(str(text).split())
    if not text:
        return []
    lines: list[str] = []
    current = ""
    for ch in text:
        trial = current + ch
        if current and text_width(draw, trial, font) > max_width:
            lines.append(current)
            current = ch
            if len(lines) == max_lines:
                break
        else:
            current = trial
    if len(lines) < max_lines and current:
        lines.append(current)
    if len(lines) == max_lines and text_width(draw, lines[-1], font) > max_width:
        while lines[-1] and text_width(draw, lines[-1] + "...", font) > max_width:
            lines[-1] = lines[-1][:-1]
        lines[-1] += "..."
    return lines


def source_for(root: Path, queue_row: dict[str, str]) -> tuple[Path, str, str]:
    pure = root / queue_row["pure_path"]
    if pure.exists():
        status = queue_row.get("status", "")
        kind = "REAL_DRAFT" if "review" in status or "regeneration" in status else "REAL"
        return pure, kind, status
    whitebox = root / queue_row["whitebox_reference_path"]
    return whitebox, "WHITEBOX_QA_PASS", "whitebox_fallback"


def draw_panel(
    source: Path,
    panel: dict[str, str],
    stage: dict[str, str],
    queue_row: dict[str, str],
    source_kind: str,
    source_status: str,
) -> Image.Image:
    image = fit_image(source)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay, "RGBA")
    title_font = load_font(24)
    font = load_font(19)
    small = load_font(16)

    draw.rectangle((0, 0, W, 82), fill=(0, 0, 0, 172))
    draw.rectangle((0, H - 112, W, H), fill=(0, 0, 0, 176))
    badge_color = (46, 138, 86, 220) if source_kind.startswith("REAL") else (150, 106, 38, 220)
    draw.rounded_rectangle((1020, 15, 1258, 54), radius=8, fill=badge_color)
    draw.text((1034, 22), source_kind[:24], font=font, fill=(255, 255, 255, 245))

    title = f"{panel['panel_id']} | Clip {panel['clip']} | {panel['approx_time']} | {stage['story_stage']}"
    draw.text((22, 12), title, font=title_font, fill=(255, 255, 255, 245))
    line2 = f"{panel['clip_title']} | {panel['shot_size']} | {panel['asset_type']} | {source_status}"
    draw.text((22, 46), line2[:100], font=small, fill=(225, 225, 225, 230))

    bottom_lines = [
        f"Beat: {panel['beat']}",
        f"Focus: {panel['image_prompt_focus']}",
        f"Blocking: {panel['pose_motion_note']}",
    ]
    y = H - 100
    for text in bottom_lines:
        for wrapped in wrap_text(draw, text, small, 1210, 1):
            draw.text((22, y), wrapped, font=small, fill=(245, 245, 245, 230))
            y += 26

    return Image.alpha_composite(image.convert("RGBA"), overlay).convert("RGB")


def make_contact_sheet(rows: list[dict[str, str]], root: Path, out_path: Path, cols: int = 4) -> None:
    thumb_w = 300
    thumb_h = int(thumb_w * 9 / 16)
    label_h = 44
    gap = 12
    font = load_font(16)
    small = load_font(13)
    sheet_rows = (len(rows) + cols - 1) // cols
    sheet = Image.new(
        "RGB",
        (cols * thumb_w + (cols + 1) * gap, sheet_rows * (thumb_h + label_h) + (sheet_rows + 1) * gap),
        (238, 238, 238),
    )
    draw = ImageDraw.Draw(sheet)
    for idx, row in enumerate(rows):
        src = root / row["final_panel_path"]
        with Image.open(src) as img:
            thumb = img.convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x = gap + (idx % cols) * (thumb_w + gap)
        y = gap + (idx // cols) * (thumb_h + label_h + gap)
        sheet.paste(thumb, (x, y))
        draw.text((x + 4, y + thumb_h + 4), f"{row['panel_id']} {row['source_kind']}", font=font, fill=(20, 20, 20))
        draw.text((x + 4, y + thumb_h + 25), f"{row['clip']} {row['story_stage']}", font=small, fill=(70, 70, 70))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path, quality=92)


def default_project_root() -> Path:
    bundled_layout_root = Path(__file__).resolve().parents[1]
    if (bundled_layout_root / "19_micro_storyboard_188_panels.csv").exists():
        return bundled_layout_root
    return Path.cwd().resolve()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build final review storyboard panels and contact sheets."
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=default_project_root(),
        help="Path to the 01_AIGC project root. Defaults to the current directory for standalone use.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.project_root.resolve()
    panels = read_csv(root / "19_micro_storyboard_188_panels.csv")
    stage_map = {r["panel_id"]: r for r in read_csv(root / "exports/panel_stage_state_map.csv")}
    queue = {r["panel_id"]: r for r in read_csv(root / "exports/real_image_generation_queue.csv")}
    prompts = {r["panel_id"]: r for r in read_csv(root / "exports/micro_storyboard_pure_image_prompts.csv")}

    manifest_rows: list[dict[str, str]] = []
    qa_rows: list[dict[str, str]] = []
    out_base = root / "final_storyboard_panels"

    for panel in panels:
        panel_id = panel["panel_id"]
        queue_row = queue[panel_id]
        stage = stage_map[panel_id]
        source, source_kind, source_status = source_for(root, queue_row)
        batch = queue_row["batch"]
        out_rel = f"final_storyboard_panels/{batch}/{panel_id}_final_storyboard_v002.jpg"
        out_path = root / out_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        image = draw_panel(source, panel, stage, queue_row, source_kind, source_status)
        image.save(out_path, quality=92)

        manifest_rows.append(
            {
                "panel_id": panel_id,
                "batch": batch,
                "clip": panel["clip"],
                "approx_time": panel["approx_time"],
                "story_stage": stage["story_stage"],
                "source_kind": source_kind,
                "source_status": source_status,
                "source_path": source.relative_to(root).as_posix(),
                "final_panel_path": out_rel,
            }
        )
        qa_rows.append(
            {
                "panel_id": panel_id,
                "final_panel_path": out_rel,
                "exists": "yes" if out_path.exists() else "no",
                "dimensions_ok": "yes" if image.size == (W, H) else "no",
                "source_exists": "yes" if source.exists() else "no",
                "whitebox_exists": "yes" if (root / queue_row["whitebox_reference_path"]).exists() else "no",
                "prompt_question_marks": str(prompts[panel_id]["pure_prompt"].count("?")),
                "source_kind": source_kind,
                "qa_status": "pass" if out_path.exists() and image.size == (W, H) and source.exists() else "fail",
            }
        )

    manifest_path = root / "exports/final_storyboard/final_storyboard_panel_manifest_v002.csv"
    qa_path = root / "exports/final_storyboard/final_storyboard_qa_v002.csv"
    write_csv(
        manifest_path,
        [
            "panel_id",
            "batch",
            "clip",
            "approx_time",
            "story_stage",
            "source_kind",
            "source_status",
            "source_path",
            "final_panel_path",
        ],
        manifest_rows,
    )
    write_csv(
        qa_path,
        [
            "panel_id",
            "final_panel_path",
            "exists",
            "dimensions_ok",
            "source_exists",
            "whitebox_exists",
            "prompt_question_marks",
            "source_kind",
            "qa_status",
        ],
        qa_rows,
    )

    for batch in sorted({r["batch"] for r in manifest_rows}):
        batch_rows = [r for r in manifest_rows if r["batch"] == batch]
        make_contact_sheet(batch_rows, root, root / "final_storyboard_contact_sheets" / f"{batch}_final_storyboard_contact_sheet_v002.jpg")

    print(f"final_panels={len(manifest_rows)}")
    print(f"qa_pass={sum(1 for r in qa_rows if r['qa_status'] == 'pass')}")
    print(f"source_counts={dict(Counter(r['source_kind'] for r in manifest_rows))}")
    print(f"manifest={manifest_path}")
    print(f"qa={qa_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
