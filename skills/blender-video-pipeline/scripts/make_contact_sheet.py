#!/usr/bin/env python3
import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw


def pick_frames(files, count):
    if len(files) <= count:
        return files
    indexes = [round(i * (len(files) - 1) / (count - 1)) for i in range(count)]
    return [files[i] for i in indexes]


def main():
    parser = argparse.ArgumentParser(description="Create a QA contact sheet from rendered frames.")
    parser.add_argument("--frames-dir", required=True)
    parser.add_argument("--glob", default="frame_*.png")
    parser.add_argument("--output", required=True)
    parser.add_argument("--count", type=int, default=12)
    parser.add_argument("--thumb-width", type=int, default=240)
    args = parser.parse_args()

    frames_dir = Path(args.frames_dir).expanduser().resolve()
    files = sorted(frames_dir.glob(args.glob))
    if not files:
        raise SystemExit(f"No frames found in {frames_dir} matching {args.glob}")

    selected = pick_frames(files, max(2, args.count))
    thumbs = []
    for path in selected:
        img = Image.open(path).convert("RGB")
        scale = args.thumb_width / img.width
        thumb = img.resize((args.thumb_width, max(1, int(img.height * scale))), Image.Resampling.LANCZOS)
        thumbs.append((path, thumb))

    cols = min(4, len(thumbs))
    rows = math.ceil(len(thumbs) / cols)
    label_h = 28
    cell_w = args.thumb_width
    cell_h = max(t.height for _, t in thumbs) + label_h
    sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), (18, 18, 18))
    draw = ImageDraw.Draw(sheet)

    for i, (path, thumb) in enumerate(thumbs):
        x = (i % cols) * cell_w
        y = (i // cols) * cell_h
        sheet.paste(thumb, (x, y))
        draw.text((x + 8, y + thumb.height + 6), path.name, fill=(235, 205, 150))

    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)
    print(f"Contact sheet: {output}")


if __name__ == "__main__":
    main()
