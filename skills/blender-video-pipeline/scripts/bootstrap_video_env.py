#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path


DEFAULT_PACKAGES = [
    "pillow",
    "numpy",
    "imageio",
    "imageio-ffmpeg",
    "moviepy",
]


def main():
    parser = argparse.ArgumentParser(description="Create a local Python video environment for Blender post-production.")
    parser.add_argument("--venv", default=".venv-video", help="Virtual environment path.")
    parser.add_argument("--packages", nargs="*", default=DEFAULT_PACKAGES, help="Packages to install.")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without running them.")
    args = parser.parse_args()

    venv = Path(args.venv).expanduser().resolve()
    python_bin = venv / ("Scripts/python.exe" if sys.platform.startswith("win") else "bin/python")

    commands = [
        [sys.executable, "-m", "venv", str(venv)],
        [str(python_bin), "-m", "pip", "install", "--upgrade", "pip"],
        [str(python_bin), "-m", "pip", "install", *args.packages],
    ]

    for cmd in commands:
        print(" ".join(cmd))
        if not args.dry_run:
            subprocess.run(cmd, check=True)

    print(f"\nReady: {python_bin}")
    print("Check with:")
    print(f"{python_bin} ~/.codex/skills/blender-video-pipeline/scripts/check_env.py")


if __name__ == "__main__":
    main()
