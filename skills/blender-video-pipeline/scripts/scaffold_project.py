#!/usr/bin/env python3
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Create a standard Blender video project package.")
    parser.add_argument("--root", required=True, help="Parent directory for the package.")
    parser.add_argument("--slug", required=True, help="Project or shot slug.")
    parser.add_argument("--aspect", default="9:16", help="Aspect ratio, e.g. 9:16 or 16:9.")
    parser.add_argument("--duration", default="10s")
    parser.add_argument("--fps", default="24")
    parser.add_argument("--purpose", default="motion reference")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve() / args.slug
    for sub in [
        "inputs",
        "blender",
        "renders/frames",
        "renders/samples",
        "outputs",
        "docs",
    ]:
        (root / sub).mkdir(parents=True, exist_ok=True)

    brief = root / "docs" / "render_brief.md"
    if not brief.exists():
        brief.write_text(
            "\n".join(
                [
                    f"# {args.slug} Render Brief",
                    "",
                    f"- Aspect: {args.aspect}",
                    f"- Duration: {args.duration}",
                    f"- FPS: {args.fps}",
                    f"- Purpose: {args.purpose}",
                    "- Inputs: describe keyframes, references, audio, and source clips.",
                    "- Camera: describe start, path, and final reveal.",
                    "- Motion beats: describe frame/time ranges.",
                    "- Output: describe MP4/ProRes/GIF needs.",
                    "- QA notes: record sample-frame and final checks.",
                    "",
                ]
            ),
            encoding="utf-8",
        )

    print(root)


if __name__ == "__main__":
    main()
