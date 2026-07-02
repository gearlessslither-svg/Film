#!/usr/bin/env python3
import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def run_version(cmd):
    try:
        result = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=10)
        return result.returncode, result.stdout.splitlines()[:3]
    except Exception as exc:
        return None, [f"{type(exc).__name__}: {exc}"]


def module_status(name):
    spec = importlib.util.find_spec(name)
    if spec is None:
        return {"available": False}
    try:
        mod = __import__(name)
        return {"available": True, "version": getattr(mod, "__version__", "")}
    except Exception as exc:
        return {"available": True, "import_error": f"{type(exc).__name__}: {exc}"}


def find_blender():
    candidates = []
    env = os.environ.get("BLENDER_BIN")
    if env:
        candidates.append(env)
    path_bin = shutil.which("blender")
    if path_bin:
        candidates.append(path_bin)
    mac_bin = "/Applications/Blender.app/Contents/MacOS/Blender"
    if Path(mac_bin).exists():
        candidates.append(mac_bin)
    seen = []
    for item in candidates:
        if item not in seen:
            seen.append(item)
    found = []
    for item in seen:
        code, lines = run_version([item, "--version"])
        found.append({"path": item, "returncode": code, "version": lines})
    return found


def ffmpeg_status():
    status = {}
    ffmpeg = shutil.which("ffmpeg")
    status["system_ffmpeg"] = ffmpeg
    if ffmpeg:
        code, lines = run_version([ffmpeg, "-version"])
        status["system_ffmpeg_version"] = lines
    status["mac_avconvert"] = shutil.which("avconvert")
    try:
        import imageio_ffmpeg

        exe = imageio_ffmpeg.get_ffmpeg_exe()
        status["imageio_ffmpeg"] = exe
        code, lines = run_version([exe, "-version"])
        status["imageio_ffmpeg_version"] = lines
    except Exception as exc:
        status["imageio_ffmpeg"] = None
        status["imageio_ffmpeg_error"] = f"{type(exc).__name__}: {exc}"
    return status


def main():
    parser = argparse.ArgumentParser(description="Check Blender video pipeline environment.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of readable text.")
    args = parser.parse_args()

    data = {
        "python": sys.executable,
        "python_version": sys.version.split()[0],
        "blender": find_blender(),
        "modules": {name: module_status(name) for name in ["PIL", "numpy", "imageio", "imageio_ffmpeg", "moviepy", "cv2"]},
        "ffmpeg": ffmpeg_status(),
    }

    if args.json:
        print(json.dumps(data, indent=2))
        return

    print(f"Python: {data['python']} ({data['python_version']})")
    print("\nBlender:")
    if data["blender"]:
        for item in data["blender"]:
            print(f"  - {item['path']}")
            for line in item["version"]:
                print(f"    {line}")
    else:
        print("  - Not found. Set BLENDER_BIN or install Blender.")

    print("\nPython modules:")
    for name, item in data["modules"].items():
        if item.get("available"):
            suffix = f" {item.get('version')}" if item.get("version") else ""
            print(f"  - {name}: OK{suffix}")
        else:
            print(f"  - {name}: missing")

    print("\nVideo encoders:")
    print(f"  - system ffmpeg: {data['ffmpeg'].get('system_ffmpeg') or 'missing'}")
    print(f"  - imageio-ffmpeg: {data['ffmpeg'].get('imageio_ffmpeg') or 'missing'}")
    print(f"  - macOS avconvert: {data['ffmpeg'].get('mac_avconvert') or 'missing'}")

    if not data["ffmpeg"].get("system_ffmpeg") and not data["ffmpeg"].get("imageio_ffmpeg"):
        print("\nRecommended next step:")
        print("  python3 ~/.codex/skills/blender-video-pipeline/scripts/bootstrap_video_env.py --venv .venv-video")


if __name__ == "__main__":
    main()
