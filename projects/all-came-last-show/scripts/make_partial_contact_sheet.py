#!/usr/bin/env python3
"""Build a chronological contact sheet from the currently selected candidates."""

from __future__ import annotations

from pathlib import Path

from package_delivery import make_contact_sheet


def sort_key(path: Path) -> tuple[int, int]:
    stem = path.stem
    shot = int(stem[2:4])
    keyframe = int(stem.rsplit("KF", 1)[1]) if "_KF" in stem else 0
    return shot, keyframe


def main() -> int:
    project = Path(__file__).resolve().parents[1]
    selected = project / "08_generation/jobs/final_frames_v2/selected"
    paths = sorted(selected.glob("*.png"), key=sort_key)
    output = project / "08_generation/jobs/final_frames_v2/storyboard_sheets/PARTIAL_CONTACT_SHEET.png"
    make_contact_sheet(paths, [path.stem for path in paths], output)
    print(f"{len(paths)} frames -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
