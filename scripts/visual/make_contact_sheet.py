import argparse
import csv
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def read_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def load_font(size):
    for name in ("arial.ttf", "seguisym.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def make_sheet(rows, root, out_path, thumb_width=320, cols=4):
    font = load_font(18)
    small = load_font(13)
    label_h = 54
    gap = 12
    thumbs = []

    for row in rows:
        rel = row.get("planned_whitebox_path") or row.get("image_path")
        img_path = root / rel
        if img_path.exists():
            with Image.open(img_path) as img:
                img = img.convert("RGB")
                ratio = thumb_width / img.width
                thumb = img.resize((thumb_width, int(img.height * ratio)), Image.Resampling.LANCZOS)
        else:
            thumb = Image.new("RGB", (thumb_width, int(thumb_width * 9 / 16)), (40, 40, 40))
        thumbs.append((row, thumb))

    if not thumbs:
        return

    thumb_h = max(img.height for _, img in thumbs)
    cell_w = thumb_width
    cell_h = thumb_h + label_h
    rows_n = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cell_w + (cols + 1) * gap, rows_n * cell_h + (rows_n + 1) * gap), (245, 245, 245))
    draw = ImageDraw.Draw(sheet)

    for idx, (row, img) in enumerate(thumbs):
        c = idx % cols
        r = idx // cols
        x = gap + c * (cell_w + gap)
        y = gap + r * (cell_h + gap)
        sheet.paste(img, (x, y))
        label_y = y + thumb_h + 5
        status = row.get("qa_status", "")
        issue = row.get("issue_type", "")
        line1 = f"{row.get('panel_id', '')}  {row.get('whitebox_id', '')}"
        line2 = f"{row.get('batch', '')} {row.get('scene_id', '')} {status} {issue}".strip()
        draw.text((x + 4, label_y), line1[:44], fill=(10, 10, 10), font=font)
        draw.text((x + 4, label_y + 25), line2[:58], fill=(80, 20, 20) if status == "fail" else (50, 50, 50), font=small)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path, quality=92)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--csv", default="exports/whitebox_qa_checklist.csv")
    parser.add_argument("--out-dir", default="whitebox_contact_sheets_v2")
    parser.add_argument("--failed-only", action="store_true")
    parser.add_argument("--cols", type=int, default=4)
    args = parser.parse_args()

    root = Path(args.project_root)
    rows = read_csv(root / args.csv)
    if args.failed_only:
        rows = [row for row in rows if row.get("qa_status") == "fail"]
        make_sheet(rows, root, root / args.out_dir / "FAILED_contact_sheet.jpg", cols=args.cols)
        print(f"wrote={len(rows)} failed-only")
        return

    batches = sorted({row.get("batch", "NO_BATCH") for row in rows})
    total = 0
    for batch in batches:
        batch_rows = [row for row in rows if row.get("batch", "NO_BATCH") == batch]
        make_sheet(batch_rows, root, root / args.out_dir / f"{batch}_contact_sheet.jpg", cols=args.cols)
        total += len(batch_rows)
    print(f"wrote={total} rows into {len(batches)} batch sheets")


if __name__ == "__main__":
    main()
