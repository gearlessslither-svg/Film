#!/usr/bin/env python3
"""Assemble the Reference-003 roughcut from the 21 generated segment MP4s.

This script is intentionally idempotent. Before all expected segment files
exist and decode, it only writes a readiness report. Once the 21 segments are
ready, it assembles the visual roughcut in official roughcut_slot order,
decode-checks the result, and refreshes the roughcut/transition audit.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ROUGH_DIR = PROJECT_ROOT / "09_edit/rough_cut"
REPORT_DIR = PROJECT_ROOT / "10_qa/reports"
PACKET_PATH = PROJECT_ROOT / "00_admin/ai_bridge/packets/20260630_reference003_video_segment_execution.json"
AUDIT_SCRIPT = ROUGH_DIR / "rebuild_reference003_roughcut_transition_audit.py"
DEFAULT_FFMPEG = Path("/Applications/Bitwig Studio.app/Contents/MacOS/ffmpeg")
REFERENCE_DURATION_SEC = 84.437333
EXPECTED_ROUGHCUT = ROUGH_DIR / "reference003_full_op_roughcut_20260630.mp4"


def rel(path: str | Path) -> str:
    path = Path(path)
    if path.is_absolute():
        return str(path.relative_to(PROJECT_ROOT))
    return str(path)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_duration(line: str) -> float | None:
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", line)
    if not match:
        return None
    hours = int(match.group(1))
    minutes = int(match.group(2))
    seconds = float(match.group(3))
    return hours * 3600 + minutes * 60 + seconds


def probe_video(ffmpeg: Path, path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "path": rel(path),
        "exists": path.exists(),
        "decode_ok": False,
        "duration_sec": None,
        "duration_line": "",
        "error": "",
    }
    if not path.exists():
        result["error"] = "missing"
        return result
    if not ffmpeg.is_file():
        result["error"] = f"ffmpeg not found: {ffmpeg}"
        return result

    decode = subprocess.run(
        [str(ffmpeg), "-v", "error", "-i", str(path), "-f", "null", "-"],
        capture_output=True,
        text=True,
    )
    result["decode_ok"] = decode.returncode == 0
    if decode.returncode != 0:
        result["error"] = (decode.stderr or decode.stdout or "").strip()[-2000:]

    info = subprocess.run(
        [str(ffmpeg), "-hide_banner", "-i", str(path)],
        capture_output=True,
        text=True,
    )
    for line in (info.stderr or info.stdout or "").splitlines():
        if "Duration:" in line:
            result["duration_line"] = line.strip()
            result["duration_sec"] = parse_duration(line)
            break
    return result


def load_segments(ffmpeg: Path) -> list[dict[str, Any]]:
    packet = read_json(PACKET_PATH)
    segments: list[dict[str, Any]] = []
    for unit in sorted(packet["units"], key=lambda row: int(row["roughcut_slot"])):
        path = PROJECT_ROOT / unit["expected_video_output_path"]
        probe = probe_video(ffmpeg, path)
        segments.append(
            {
                "slot": int(unit["roughcut_slot"]),
                "unit_id": unit["unit_id"],
                "title": unit["title"],
                "time_range": unit["time_range"],
                "expected_video_output_path": unit["expected_video_output_path"],
                "generation_gate": unit["generation_gate"],
                "blocking_keyframes": unit.get("blocking_keyframes", []),
                "probe": probe,
            }
        )
    return segments


def build_filter(segment_count: int, fps: str, width: int, height: int) -> str:
    chains = []
    labels = []
    for index in range(segment_count):
        label = f"v{index}"
        chains.append(
            f"[{index}:v]fps={fps},"
            f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
            f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,"
            f"setsar=1,format=yuv420p[{label}]"
        )
        labels.append(f"[{label}]")
    chains.append("".join(labels) + f"concat=n={segment_count}:v=1:a=0[vout]")
    return ";".join(chains)


def run_assembly(
    ffmpeg: Path,
    segments: list[dict[str, Any]],
    output_path: Path,
    fps: str,
    width: int,
    height: int,
) -> dict[str, Any]:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    common: list[str] = [str(ffmpeg), "-y"]
    for segment in segments:
        common.extend(["-i", str(PROJECT_ROOT / segment["expected_video_output_path"])])
    common.extend(
        [
            "-filter_complex",
            build_filter(len(segments), fps, width, height),
            "-map",
            "[vout]",
            "-an",
            "-pix_fmt",
            "yuv420p",
            "-movflags",
            "+faststart",
        ]
    )

    encoder_attempts = [
        ["-c:v", "h264_videotoolbox", "-b:v", "12000k"],
        ["-c:v", "libx264", "-preset", "medium", "-crf", "18"],
        ["-c:v", "mpeg4", "-q:v", "2"],
    ]
    errors: list[str] = []
    for encoder in encoder_attempts:
        command = common + encoder + [str(output_path)]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            return {
                "ok": True,
                "encoder": " ".join(encoder),
                "command": " ".join(command),
                "error": "",
            }
        errors.append((result.stderr or result.stdout or "").strip()[-2000:])

    return {
        "ok": False,
        "encoder": "",
        "command": " ".join(common + encoder_attempts[-1] + [str(output_path)]),
        "error": "\n--- encoder attempt failed ---\n".join(errors),
    }


def refresh_transition_audit() -> dict[str, Any]:
    result = subprocess.run(
        ["python3", str(AUDIT_SCRIPT)],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
    )
    output = ((result.stdout or "") + (result.stderr or "")).strip()
    return {
        "ok": result.returncode == 0,
        "returncode": result.returncode,
        "output_tail": "\n".join(output.splitlines()[-20:]),
    }


def build_report(
    now: str,
    ffmpeg: Path,
    segments: list[dict[str, Any]],
    assembly: dict[str, Any] | None,
    roughcut_probe: dict[str, Any],
    transition_audit: dict[str, Any] | None,
    check_only: bool,
) -> dict[str, Any]:
    missing = [segment for segment in segments if not segment["probe"]["exists"]]
    failed_decode = [
        segment
        for segment in segments
        if segment["probe"]["exists"] and not segment["probe"]["decode_ok"]
    ]
    ready = not missing and not failed_decode
    duration_delta = None
    if roughcut_probe["duration_sec"] is not None:
        duration_delta = round(roughcut_probe["duration_sec"] - REFERENCE_DURATION_SEC, 3)
    duration_match = duration_delta is not None and abs(duration_delta) <= 1.0

    if not ready:
        status = "waiting_for_segments"
    elif check_only:
        status = "segments_ready_check_only"
    elif roughcut_probe["decode_ok"] and duration_match:
        status = "roughcut_assembled_decode_pass"
    elif roughcut_probe["decode_ok"]:
        status = "roughcut_assembled_decode_pass_duration_pending"
    else:
        status = "roughcut_assembly_failed_or_decode_failed"

    return {
        "schema_version": "reference003_roughcut_assembly_v1",
        "project_slug": "blue-water-citypop-op",
        "created_at": now,
        "status": status,
        "source_packet": rel(PACKET_PATH),
        "ffmpeg": str(ffmpeg),
        "expected_roughcut": rel(EXPECTED_ROUGHCUT),
        "expected_reference_duration_sec": REFERENCE_DURATION_SEC,
        "check_only": check_only,
        "summary": {
            "segments_total": len(segments),
            "segments_existing": sum(1 for segment in segments if segment["probe"]["exists"]),
            "segments_decode_pass": sum(
                1 for segment in segments if segment["probe"]["decode_ok"]
            ),
            "missing_segments": len(missing),
            "failed_decode_segments": len(failed_decode),
            "ready_for_assembly": ready,
            "roughcut_exists": roughcut_probe["exists"],
            "roughcut_decode_ok": roughcut_probe["decode_ok"],
            "roughcut_duration_sec": roughcut_probe["duration_sec"],
            "roughcut_duration_delta_sec": duration_delta,
            "roughcut_duration_match_within_1s": duration_match,
        },
        "segments": segments,
        "assembly": assembly,
        "roughcut_probe": roughcut_probe,
        "transition_audit_refresh": transition_audit,
        "next_action": (
            "Generate/copy the missing segment MP4s to their expected paths."
            if not ready
            else "Review transition edges and run completion audit."
        ),
        "rebuild_script": rel(Path(__file__)),
    }


def write_reports(report: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ROUGH_DIR.mkdir(parents=True, exist_ok=True)
    json_paths = [
        ROUGH_DIR / "reference003_roughcut_assembly_20260630.json",
        REPORT_DIR / "reference003_roughcut_assembly_20260630.json",
    ]
    for path in json_paths:
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = [
        "# Reference-003 Roughcut Assembly",
        "",
        f"- Rebuilt: `{report['created_at']}`",
        f"- Status: `{report['status']}`",
        f"- Expected roughcut: `{report['expected_roughcut']}`",
        "",
        "## Summary",
        "",
    ]
    for key, value in report["summary"].items():
        md.append(f"- `{key}`: `{value}`")
    md.extend(
        [
            "",
            "## Segment Readiness",
            "",
            "| Slot | Unit | Expected path | Exists | Decode | Duration |",
            "|---:|---|---|---|---|---:|",
        ]
    )
    for segment in report["segments"]:
        probe = segment["probe"]
        md.append(
            f"| {segment['slot']} | `{segment['unit_id']}` | "
            f"`{segment['expected_video_output_path']}` | {probe['exists']} | "
            f"{probe['decode_ok']} | {probe['duration_sec']} |"
        )
    md.extend(["", "## Next Action", "", report["next_action"]])
    md_paths = [
        ROUGH_DIR / "reference003_roughcut_assembly_20260630.md",
        REPORT_DIR / "reference003_roughcut_assembly_20260630.md",
    ]
    for path in md_paths:
        path.write_text("\n".join(md) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Assemble the Reference-003 roughcut from generated segment MP4s."
    )
    parser.add_argument("--check-only", action="store_true", help="Only write readiness report.")
    parser.add_argument("--ffmpeg", default=str(DEFAULT_FFMPEG), help="ffmpeg executable")
    parser.add_argument("--fps", default="24000/1001", help="Output frame rate")
    parser.add_argument("--width", type=int, default=1440, help="Output width")
    parser.add_argument("--height", type=int, default=1080, help="Output height")
    parser.add_argument("--print-json", action="store_true", help="Print compact JSON summary")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    now = datetime.now(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()
    ffmpeg = Path(args.ffmpeg)
    segments = load_segments(ffmpeg)
    ready = all(segment["probe"]["exists"] and segment["probe"]["decode_ok"] for segment in segments)

    assembly = None
    transition_audit = None
    if ready and not args.check_only:
        assembly = run_assembly(ffmpeg, segments, EXPECTED_ROUGHCUT, args.fps, args.width, args.height)
        transition_audit = refresh_transition_audit()

    roughcut_probe = probe_video(ffmpeg, EXPECTED_ROUGHCUT)
    report = build_report(
        now=now,
        ffmpeg=ffmpeg,
        segments=segments,
        assembly=assembly,
        roughcut_probe=roughcut_probe,
        transition_audit=transition_audit,
        check_only=args.check_only,
    )
    write_reports(report)

    compact = {
        "status": report["status"],
        "summary": report["summary"],
        "report": "10_qa/reports/reference003_roughcut_assembly_20260630.md",
    }
    if args.print_json:
        print(json.dumps(compact, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(compact, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
