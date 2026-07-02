#!/usr/bin/env python3
import argparse
import os
import shutil
import subprocess
from pathlib import Path


def find_blender(explicit=None):
    if explicit:
        return explicit
    if os.environ.get("BLENDER_BIN"):
        return os.environ["BLENDER_BIN"]
    path_bin = shutil.which("blender")
    if path_bin:
        return path_bin
    mac_bin = "/Applications/Blender.app/Contents/MacOS/Blender"
    if Path(mac_bin).exists():
        return mac_bin
    return None


def main():
    parser = argparse.ArgumentParser(description="Run a Blender Python script in background mode.")
    parser.add_argument("--script", required=True, help="Blender Python script.")
    parser.add_argument("--blender", help="Explicit Blender executable.")
    parser.add_argument("--cwd", help="Working directory.")
    parser.add_argument("script_args", nargs=argparse.REMAINDER, help="Arguments after -- passed to the Blender script.")
    args = parser.parse_args()

    blender = find_blender(args.blender)
    if not blender:
        raise SystemExit("Blender not found. Set BLENDER_BIN or install Blender.")
    script = Path(args.script).expanduser().resolve()
    if not script.exists():
        raise SystemExit(f"Script not found: {script}")

    cmd = [blender, "--background", "--python", str(script)]
    if args.script_args:
        extra = args.script_args
        if extra and extra[0] == "--":
            extra = extra[1:]
        cmd += ["--", *extra]
    print(" ".join(cmd))
    raise SystemExit(subprocess.run(cmd, cwd=args.cwd).returncode)


if __name__ == "__main__":
    main()
