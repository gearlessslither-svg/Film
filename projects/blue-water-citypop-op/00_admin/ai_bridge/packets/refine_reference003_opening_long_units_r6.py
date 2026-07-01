#!/usr/bin/env python3
"""Frame-level boundary audit and opening-long-unit repack for Reference-003."""

from __future__ import annotations

import csv
import json
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


PROJECT_ROOT = Path(__file__).resolve().parents[3]
SOURCE_VIDEO = PROJECT_ROOT / "01_intake/references/reference-003-full-op-2160p.mp4"
SOURCE_REPORT = (
    PROJECT_ROOT
    / "10_qa/reports/reference003_r5_video_segment_all_units01_21_generation_ready_20260701.json"
)
ASSET_LOCKS_PATH = PROJECT_ROOT / "05_asset_bible/setting_chapters/reference003_asset_locks_v1.json"
ANALYSIS_ROOT = PROJECT_ROOT / "01_intake/analysis/reference003_frame_boundary_refine_r6_20260701"
PACKAGE_ROOT = PROJECT_ROOT / "08_generation/jobs/REFERENCE003_R6_OPENING_LONG_UNITS_20260701"
EXPECTED_VIDEO_ROOT = PROJECT_ROOT / "08_generation/outputs/video/reference003_r6_opening_long_segments"
REPORT_DIR = PROJECT_ROOT / "10_qa/reports"
FFMPEG = Path("/Applications/Bitwig Studio.app/Contents/MacOS/ffmpeg")


OPENING_UNITS = [
    {
        "order": 1,
        "unit_id": "VU_REF003_OPENING_L01_CLOUD_BIRD_LONG",
        "title": "开场长镜头 A：黑场云层到白鸟入画",
        "time_range": "00:00.00-00:07.00",
        "intent": "把原 0-7 秒作为同一连续天空/白鸟开场，不再拆成黑场、云层、白鸟短段。",
        "anchor_ids": [
            "OP_SHOT_001",
            "OP_SHOT_002",
            "OP_SHOT_003",
            "R5_VU_REF003_002_WHITE_BIRD_SKY_003500ms_02",
            "OP_SHOT_004",
            "R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01",
        ],
        "active_locks": [("props_vehicles_symbols", "white_bird")],
        "motion": "fade from black into bright clouds, then continue into white-bird sky motion as one long, graceful opening move",
    },
    {
        "order": 2,
        "unit_id": "VU_REF003_OPENING_L02_BIRD_CLOUD_AIRCRAFT_LONG",
        "title": "开场长镜头 B：白鸟云层到飞行器短显",
        "time_range": "00:07.00-00:16.50",
        "intent": "保留白鸟/云层/飞行器的一体化运动，重点抓住一闪而过的飞行器，不把它丢到前后镜头里。",
        "anchor_ids": [
            "R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01",
            "OP_SHOT_005",
            "OP_SHOT_006",
            "R5_VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS_014000ms_01",
            "R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_014500ms_02",
            "OP_SHOT_007",
            "R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_016000ms_01",
        ],
        "active_locks": [
            ("props_vehicles_symbols", "white_bird"),
            ("props_vehicles_symbols", "jean_aircraft"),
        ],
        "motion": "continuous sky move with white bird/cloud composition, then a brief aircraft reveal treated as an insert inside the same long opening phrase",
    },
    {
        "order": 3,
        "unit_id": "VU_REF003_OPENING_L03_TITLE_FLARE_NADIA_LONG",
        "title": "开场长镜头 C：标题安全位到日光转 Nadia",
        "time_range": "00:16.50-00:24.80",
        "intent": "把主标题安全位、日光耀斑、Nadia 首次显影作为开场长镜头收束段，避免 1 秒转场被单独切碎。",
        "anchor_ids": [
            "R5_VU_REF003_005_MAIN_TITLE_SAFE_HOLD_017000ms_01",
            "OP_SHOT_008",
            "OP_SHOT_009",
            "R5_VU_REF003_006_SUN_FLARE_TO_NADIA_023500ms_01",
            "OP_SHOT_010",
        ],
        "active_locks": [
            ("characters", "nadia"),
            ("props_vehicles_symbols", "blue_water_pendant"),
        ],
        "motion": "hold the no-text title-safe sky space, bloom into sun flare, then bridge into Nadia's first profile reveal",
    },
]


def rel(path: Path | str) -> str:
    path = Path(path)
    if path.is_absolute():
        return path.relative_to(PROJECT_ROOT).as_posix()
    return path.as_posix()


def parse_timecode(value: str) -> float:
    parts = value.strip().split(":")
    if len(parts) == 2:
        return int(parts[0]) * 60 + float(parts[1])
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    raise ValueError(f"Unsupported timecode: {value}")


def parse_range(value: str) -> tuple[float, float]:
    start, end = [part.strip() for part in value.split("-", 1)]
    return parse_timecode(start), parse_timecode(end)


def timecode(seconds: float) -> str:
    minutes = int(seconds // 60)
    sec = seconds - minutes * 60
    return f"{minutes:02d}:{sec:05.2f}"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


@dataclass
class FrameMetric:
    frame: int
    time_sec: float
    gray_diff: float
    hist_diff: float
    edge_diff: float
    composite: float
    kind: str = ""


def robust_threshold(values: np.ndarray, sigma: float = 7.0, quantile: float = 0.985) -> float:
    median = float(np.median(values))
    mad = float(np.median(np.abs(values - median)))
    robust = median + sigma * max(mad, 1e-6)
    return max(robust, float(np.quantile(values, quantile)))


def make_sheet(items: list[tuple[str, Image.Image]], out_path: Path, cols: int = 5, thumb_w: int = 260) -> None:
    if not items:
        return
    font = ImageFont.load_default()
    gap = 10
    label_h = 42
    thumbs = []
    for label, img in items:
        img = img.convert("RGB")
        thumb_h = int(thumb_w * img.height / img.width)
        thumb = img.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        thumbs.append((label, thumb))
    max_h = max(t.height for _, t in thumbs)
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_w + (cols + 1) * gap, rows * (max_h + label_h) + (rows + 1) * gap), (242, 242, 238))
    draw = ImageDraw.Draw(sheet)
    for idx, (label, thumb) in enumerate(thumbs):
        c = idx % cols
        r = idx // cols
        x = gap + c * (thumb_w + gap)
        y = gap + r * (max_h + label_h + gap)
        sheet.paste(thumb, (x, y))
        draw.text((x + 4, y + max_h + 5), label[:42], fill=(20, 20, 20), font=font)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path, quality=92)


def analyze_frame_boundaries() -> dict[str, Any]:
    ANALYSIS_ROOT.mkdir(parents=True, exist_ok=True)
    cap = cv2.VideoCapture(str(SOURCE_VIDEO))
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open {SOURCE_VIDEO}")
    fps = float(cap.get(cv2.CAP_PROP_FPS) or 24000 / 1001)
    frames_gray: list[np.ndarray] = []
    frames_edge: list[np.ndarray] = []
    frames_hist: list[np.ndarray] = []
    frames_rgb_small: list[np.ndarray] = []

    while True:
        ok, frame = cap.read()
        if not ok:
            break
        small = cv2.resize(frame, (240, 180), interpolation=cv2.INTER_AREA)
        rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(gray, 60, 140)
        hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv], [0, 1], None, [24, 16], [0, 180, 0, 256])
        cv2.normalize(hist, hist)
        frames_rgb_small.append(rgb)
        frames_gray.append(gray)
        frames_edge.append(edge)
        frames_hist.append(hist)
    cap.release()

    metrics: list[FrameMetric] = []
    for i in range(1, len(frames_gray)):
        gray_diff = float(np.mean(cv2.absdiff(frames_gray[i], frames_gray[i - 1])) / 255.0)
        edge_diff = float(np.mean(cv2.absdiff(frames_edge[i], frames_edge[i - 1])) / 255.0)
        hist_diff = float(cv2.compareHist(frames_hist[i], frames_hist[i - 1], cv2.HISTCMP_BHATTACHARYYA))
        composite = 0.55 * gray_diff + 0.35 * hist_diff + 0.10 * edge_diff
        metrics.append(FrameMetric(i, i / fps, gray_diff, hist_diff, edge_diff, composite))

    values = np.array([m.composite for m in metrics], dtype=np.float32)
    hard_threshold = robust_threshold(values, sigma=7.0, quantile=0.985)
    flash_threshold = robust_threshold(values, sigma=5.5, quantile=0.975)
    low_threshold = float(np.median(values) + 2.5 * max(np.median(np.abs(values - np.median(values))), 1e-6))

    hard: list[FrameMetric] = []
    for m in metrics:
        if m.composite < hard_threshold:
            continue
        prev_score = metrics[m.frame - 2].composite if m.frame >= 2 else -1
        next_score = metrics[m.frame].composite if m.frame < len(metrics) else -1
        if m.composite >= prev_score and m.composite >= next_score:
            m.kind = "hard_boundary_candidate"
            hard.append(m)

    flashes: list[dict[str, Any]] = []
    for i in range(1, len(frames_gray) - 1):
        d_in = metrics[i - 1].composite
        d_out = metrics[i].composite
        bridge = float(np.mean(cv2.absdiff(frames_gray[i - 1], frames_gray[i + 1])) / 255.0)
        if d_in >= flash_threshold and d_out >= flash_threshold and bridge <= low_threshold:
            flashes.append(
                {
                    "kind": "single_frame_flash_candidate",
                    "frame": i,
                    "time_sec": round(i / fps, 3),
                    "timecode": timecode(i / fps),
                    "d_in": round(float(d_in), 5),
                    "d_out": round(float(d_out), 5),
                    "bridge_prev_next": round(bridge, 5),
                }
            )

    metrics_csv = ANALYSIS_ROOT / "reference003_frame_level_metrics.csv"
    with metrics_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["frame", "time_sec", "timecode", "gray_diff", "hist_diff", "edge_diff", "composite"],
        )
        writer.writeheader()
        for m in metrics:
            writer.writerow(
                {
                    "frame": m.frame,
                    "time_sec": round(m.time_sec, 3),
                    "timecode": timecode(m.time_sec),
                    "gray_diff": round(m.gray_diff, 6),
                    "hist_diff": round(m.hist_diff, 6),
                    "edge_diff": round(m.edge_diff, 6),
                    "composite": round(m.composite, 6),
                }
            )

    opening_items: list[tuple[str, Image.Image]] = []
    for frame_no in range(0, min(len(frames_rgb_small), int(fps * 25)), max(1, int(round(fps / 4)))):
        opening_items.append((f"{timecode(frame_no / fps)} f{frame_no}", Image.fromarray(frames_rgb_small[frame_no])))
    opening_sheet = ANALYSIS_ROOT / "opening_00_25_4fps_contact_sheet.jpg"
    make_sheet(opening_items, opening_sheet, cols=6, thumb_w=220)

    top = sorted(hard, key=lambda m: m.composite, reverse=True)[:60]
    candidate_items: list[tuple[str, Image.Image]] = []
    for m in top:
        for offset, tag in [(-1, "pre"), (0, "cut"), (1, "post")]:
            idx = max(0, min(len(frames_rgb_small) - 1, m.frame + offset))
            candidate_items.append((f"{tag} {timecode(idx / fps)} s{m.composite:.3f}", Image.fromarray(frames_rgb_small[idx])))
    candidate_sheet = ANALYSIS_ROOT / "top_boundary_candidate_triplets.jpg"
    make_sheet(candidate_items, candidate_sheet, cols=6, thumb_w=190)

    flash_items: list[tuple[str, Image.Image]] = []
    for item in flashes[:40]:
        i = item["frame"]
        for offset, tag in [(-1, "pre"), (0, "flash"), (1, "post")]:
            idx = max(0, min(len(frames_rgb_small) - 1, i + offset))
            flash_items.append((f"{tag} {timecode(idx / fps)}", Image.fromarray(frames_rgb_small[idx])))
    flash_sheet = ANALYSIS_ROOT / "single_frame_flash_candidate_triplets.jpg"
    make_sheet(flash_items, flash_sheet, cols=6, thumb_w=190)

    boundary_rows = [
        {
            "kind": m.kind,
            "frame": m.frame,
            "time_sec": round(m.time_sec, 3),
            "timecode": timecode(m.time_sec),
            "score": round(m.composite, 5),
        }
        for m in sorted(hard, key=lambda item: item.time_sec)
    ]
    report = {
        "schema_version": "reference003_frame_boundary_refine_r6_v1",
        "source_video": rel(SOURCE_VIDEO),
        "fps": fps,
        "frame_count": len(frames_gray),
        "duration_sec": round(len(frames_gray) / fps, 3),
        "method": "OpenCV full-frame scan at source frame rate; grayscale, HSV histogram, and edge deltas; robust hard-boundary and single-frame flash candidates.",
        "hard_threshold": round(float(hard_threshold), 6),
        "flash_threshold": round(float(flash_threshold), 6),
        "candidate_boundaries": boundary_rows,
        "single_frame_flash_candidates": flashes,
        "metrics_csv": rel(metrics_csv),
        "opening_0_25_contact_sheet": rel(opening_sheet),
        "top_boundary_candidate_sheet": rel(candidate_sheet),
        "single_frame_flash_candidate_sheet": rel(flash_sheet) if flash_items else "",
    }
    json_path = ANALYSIS_ROOT / "reference003_frame_boundary_refine_r6_20260701.json"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    opening_boundaries = [b for b in boundary_rows if b["time_sec"] <= 25.5]
    md_lines = [
        "# Reference-003 Frame Boundary Refine R6",
        "",
        f"- Source: `{rel(SOURCE_VIDEO)}`",
        f"- FPS scan: {fps:.3f}; frames: {len(frames_gray)}",
        f"- Opening sheet: `{rel(opening_sheet)}`",
        f"- Boundary triplets: `{rel(candidate_sheet)}`",
        f"- Flash triplets: `{rel(flash_sheet) if flash_items else 'none detected'}`",
        "",
        "## Opening 0-25s Candidate Boundaries",
        "",
        "| time | frame | score | kind |",
        "|---:|---:|---:|---|",
    ]
    for b in opening_boundaries:
        md_lines.append(f"| {b['timecode']} | {b['frame']} | {b['score']} | {b['kind']} |")
    md_lines.extend(
        [
            "",
            "## Packaging Decision",
            "",
            "The opening is repacked as three long AIGC units: 00:00-00:07, 00:07-00:16.50, and 00:16.50-00:24.80. These are generation chunks, not a claim that the reference has hard cuts at those exact times.",
            "",
            "## Precision Upgrade",
            "",
            "- Previous 2fps sampling can miss 1-3 frame inserts.",
            "- R6 scans every source frame at ~23.976fps and flags hard-boundary and single-frame flash candidates.",
            "- Candidate boundaries still require director/semantic review before becoming promoted image assets.",
        ]
    )
    md_path = ANALYSIS_ROOT / "reference003_frame_boundary_refine_r6_20260701.md"
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    report["report_json"] = rel(json_path)
    report["report_md"] = rel(md_path)
    return report


def load_existing_anchors() -> dict[str, dict[str, Any]]:
    report = read_json(SOURCE_REPORT)
    anchors: dict[str, dict[str, Any]] = {}
    for job in report["jobs"][:8]:
        for anchor in read_json(PROJECT_ROOT / job["job_dir"] / "ordered_keyframe_anchors.json"):
            anchors[anchor["item_id"]] = anchor
    return anchors


def copy_global_asset_locks() -> list[dict[str, Any]]:
    asset_locks = read_json(ASSET_LOCKS_PATH)
    dst_root = PACKAGE_ROOT / "_global_asset_locks"
    if dst_root.exists():
        shutil.rmtree(dst_root)
    dst_root.mkdir(parents=True, exist_ok=True)
    copied: list[dict[str, Any]] = []
    for group in ("characters", "props_vehicles_symbols"):
        for asset_id, lock in asset_locks.get(group, {}).items():
            source_path = lock.get("lock_path") or ""
            output_path = ""
            exists = False
            if source_path:
                src = PROJECT_ROOT / source_path
                dst = dst_root / f"{group}_{asset_id}{src.suffix or '.png'}"
                if src.exists():
                    shutil.copy2(src, dst)
                output_path = rel(dst)
                exists = dst.exists()
            copied.append(
                {
                    "group": group,
                    "asset_id": asset_id,
                    "status": lock.get("status", ""),
                    "source_path": source_path,
                    "global_lock_path": output_path,
                    "exists": exists,
                }
            )
    (dst_root / "asset_locks_manifest.json").write_text(json.dumps(copied, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return copied


def active_lock_records(active_locks: list[tuple[str, str]], all_locks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_key = {(row["group"], row["asset_id"]): row for row in all_locks}
    return [by_key[(group, asset_id)] for group, asset_id in active_locks if (group, asset_id) in by_key]


def extract_clip(start_sec: float, end_sec: float, out_path: Path) -> dict[str, Any]:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    command = [
        str(FFMPEG),
        "-y",
        "-ss",
        f"{start_sec:.3f}",
        "-i",
        str(SOURCE_VIDEO),
        "-t",
        f"{end_sec - start_sec:.3f}",
        "-an",
        "-c:v",
        "mpeg4",
        "-q:v",
        "3",
        str(out_path),
    ]
    proc = subprocess.run(command, capture_output=True, text=True)
    decode = subprocess.run([str(FFMPEG), "-v", "error", "-i", str(out_path), "-f", "null", "-"], capture_output=True, text=True)
    return {
        "path": rel(out_path),
        "start_sec": round(start_sec, 3),
        "end_sec": round(end_sec, 3),
        "duration_sec": round(end_sec - start_sec, 3),
        "ok": proc.returncode == 0 and out_path.exists() and out_path.stat().st_size > 0,
        "decode_ok": decode.returncode == 0,
        "stderr_tail": "\n".join((proc.stderr or decode.stderr or "").splitlines()[-8:]),
    }


def package_keyframes(unit: dict[str, Any], anchors_by_id: dict[str, dict[str, Any]], job_dir: Path) -> list[dict[str, Any]]:
    keyframe_dir = job_dir / "keyframes"
    if keyframe_dir.exists():
        shutil.rmtree(keyframe_dir)
    keyframe_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    for idx, anchor_id in enumerate(unit["anchor_ids"], start=1):
        anchor = anchors_by_id[anchor_id]
        src = PROJECT_ROOT / anchor["source_path"]
        dst = keyframe_dir / f"{idx:02d}_{anchor_id}{src.suffix or '.png'}"
        shutil.copy2(src, dst)
        row = dict(anchor)
        row["order"] = idx
        row["packaged_path"] = rel(dst)
        row["exists"] = dst.exists()
        rows.append(row)
    return rows


def build_prompt(unit: dict[str, Any], anchors: list[dict[str, Any]], locks: list[dict[str, Any]]) -> str:
    anchor_lines = "\n".join(
        f"- 图{a['order']}: `{a['item_id']}` ({a.get('timecode', '')}, {a.get('kind', '')}) `{a['packaged_path']}`"
        for a in anchors
    )
    lock_lines = "\n".join(
        f"- `{lock['asset_id']}` ({lock.get('status', '')}): `{lock.get('global_lock_path', '')}`"
        for lock in locks
    ) or "- none for this unit"
    return f"""# {unit['unit_id']} — {unit['title']}

## Upload These

1. Reference video: `reference_clip/{unit['unit_id']}_reference.mp4`
2. Ordered keyframes:
{anchor_lines}
3. Active asset locks:
{lock_lines}

## Prompt To Use

Generate a clean live-action remake video segment for `{unit['unit_id']}`.
Time range: `{unit['time_range']}`.

Reference-video priority: use the reference clip for timing, camera movement,
screen direction, and continuous motion. This is a long opening-generation chunk,
not a montage of unrelated stills.

Shot intent: {unit['intent']}

Motion direction: {unit['motion']}.

Use the ordered keyframes only in the listed timeline order. Preserve the no-text,
no-logo remake rule: replace all readable titles, credits, subtitles, lyrics,
broadcaster marks, and random symbols with clean sky/light/water composition.

Reject if the model invents readable text, moves keyframes out of order, drops the
brief aircraft/bird/Nadia transition beat when that beat is listed, or redesigns
visible locked assets.
"""


def package_opening_units(now: str, boundary_report: dict[str, Any]) -> dict[str, Any]:
    if PACKAGE_ROOT.exists():
        shutil.rmtree(PACKAGE_ROOT)
    PACKAGE_ROOT.mkdir(parents=True, exist_ok=True)
    EXPECTED_VIDEO_ROOT.mkdir(parents=True, exist_ok=True)
    prompt_root = PACKAGE_ROOT / "_PROMPT_INDEX" / "PROMPT_ONLY"
    prompt_root.mkdir(parents=True, exist_ok=True)
    all_locks = copy_global_asset_locks()
    anchors_by_id = load_existing_anchors()
    jobs: list[dict[str, Any]] = []
    index_rows: list[str] = []
    index_json: list[dict[str, Any]] = []
    for unit in OPENING_UNITS:
        job_dir = PACKAGE_ROOT / unit["unit_id"]
        job_dir.mkdir(parents=True, exist_ok=True)
        start_sec, end_sec = parse_range(unit["time_range"])
        clip_path = job_dir / "reference_clip" / f"{unit['unit_id']}_reference.mp4"
        clip = extract_clip(start_sec, end_sec, clip_path)
        anchors = package_keyframes(unit, anchors_by_id, job_dir)
        (job_dir / "ordered_keyframe_anchors.json").write_text(json.dumps(anchors, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        make_sheet(
            [(f"{a.get('timecode', '')} {a['item_id']}", Image.open(PROJECT_ROOT / a["packaged_path"])) for a in anchors],
            job_dir / "ordered_keyframe_contact_sheet.jpg",
            cols=4,
            thumb_w=280,
        )
        locks = active_lock_records(unit["active_locks"], all_locks)
        (job_dir / "active_asset_locks.json").write_text(json.dumps(locks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        prompt = build_prompt(unit, anchors, locks)
        prompt_path = prompt_root / f"{unit['order']:02d}_{unit['unit_id']}.md"
        prompt_path.write_text(prompt, encoding="utf-8")
        brief_path = job_dir / "AIGC_VIDEO_GENERATION_BRIEF.md"
        brief_path.write_text(prompt, encoding="utf-8")
        expected = EXPECTED_VIDEO_ROOT / f"{unit['unit_id']}.mp4"
        manifest = {
            "schema_version": "reference003_r6_opening_long_unit_package_v1",
            "created_at": now,
            "status": "ready_for_external_aigc_video_generation" if clip["decode_ok"] and all(a["exists"] for a in anchors) else "needs_review",
            "unit": unit,
            "reference_clip": clip,
            "keyframe_anchors": anchors,
            "active_asset_locks": locks,
            "prompt_only": rel(prompt_path),
            "generation_brief": rel(brief_path),
            "ordered_keyframe_contact_sheet": rel(job_dir / "ordered_keyframe_contact_sheet.jpg"),
            "expected_video_output_path": rel(expected),
            "boundary_refine_report": boundary_report["report_json"],
        }
        (job_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        job = {
            "order": unit["order"],
            "unit_id": unit["unit_id"],
            "title": unit["title"],
            "time_range": unit["time_range"],
            "job_dir": rel(job_dir),
            "reference_clip": clip,
            "keyframe_anchor_count": len(anchors),
            "active_locks": [lock["asset_id"] for lock in locks],
            "prompt_only": rel(prompt_path),
            "generation_brief": rel(brief_path),
            "expected_video_output_path": rel(expected),
            "ready": manifest["status"] == "ready_for_external_aigc_video_generation",
        }
        jobs.append(job)
        index_rows.append(
            f"| {unit['order']:02d} | `{unit['unit_id']}` | {unit['title']} | `{unit['time_range']}` | "
            f"`{clip['path']}` | `{rel(prompt_path)}` | {', '.join(job['active_locks']) or 'none'} |"
        )
        index_json.append(job)

    index_md = PACKAGE_ROOT / "_PROMPT_INDEX" / "AIGC_VIDEO_PROMPT_INDEX.md"
    index_md.write_text(
        "\n".join(
            [
                "# Reference-003 R6 Opening Long Units Prompt Index",
                "",
                "This package replaces the overly short opening units with three longer generation chunks.",
                "",
                f"- Boundary refine report: `{boundary_report['report_md']}`",
                f"- Global asset locks: `{rel(PACKAGE_ROOT / '_global_asset_locks')}`",
                "",
                "| # | Unit | Title | Time Range | Reference Clip | Prompt-Only File | Active Locks |",
                "|---:|---|---|---|---|---|---|",
                *index_rows,
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    (PACKAGE_ROOT / "_PROMPT_INDEX" / "AIGC_VIDEO_PROMPT_INDEX.json").write_text(json.dumps(index_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    shutil.copy2(index_md, PACKAGE_ROOT / "README_USE_THIS_FIRST.md")

    report = {
        "schema_version": "reference003_r6_opening_long_units_batch_v1",
        "created_at": now,
        "status": "ready_for_external_aigc_video_generation" if all(job["ready"] for job in jobs) else "needs_review",
        "package_root": rel(PACKAGE_ROOT),
        "jobs": jobs,
        "boundary_refine_report": boundary_report["report_json"],
        "opening_replacement_note": "Use these three long units as the refined opening replacement. Existing R5 21-unit package remains available for the rest of the video.",
    }
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    json_path = REPORT_DIR / "reference003_r6_opening_long_units_generation_ready_20260701.json"
    md_path = REPORT_DIR / "reference003_r6_opening_long_units_generation_ready_20260701.md"
    report["report_json"] = rel(json_path)
    report["report_md"] = rel(md_path)
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(
        "\n".join(
            [
                "# Reference-003 R6 Opening Long Units Generation Ready",
                "",
                f"- Status: `{report['status']}`",
                f"- Package root: `{report['package_root']}`",
                f"- Boundary refine report: `{report['boundary_refine_report']}`",
                "",
                "| # | Unit | Ready | Time Range | Anchors | Prompt |",
                "|---:|---|---:|---|---:|---|",
                *[
                    f"| {job['order']} | `{job['unit_id']}` | `{job['ready']}` | `{job['time_range']}` | {job['keyframe_anchor_count']} | `{job['prompt_only']}` |"
                    for job in jobs
                ],
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    (PACKAGE_ROOT / "manifest.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    now = datetime.now(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()
    boundary_report = analyze_frame_boundaries()
    package_report = package_opening_units(now, boundary_report)
    print(
        json.dumps(
            {
                "status": package_report["status"],
                "package_root": package_report["package_root"],
                "jobs": len(package_report["jobs"]),
                "boundary_report": boundary_report["report_md"],
                "report_md": package_report["report_md"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if package_report["status"] == "ready_for_external_aigc_video_generation" else 1


if __name__ == "__main__":
    raise SystemExit(main())
