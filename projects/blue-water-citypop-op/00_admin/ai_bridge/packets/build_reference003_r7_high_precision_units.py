#!/usr/bin/env python3
"""Build Reference-003 R7 high-precision video-unit packages and frame candidates."""

from __future__ import annotations

import csv
import json
import math
import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import cv2
from PIL import Image, ImageDraw, ImageFont


PROJECT_ROOT = Path(__file__).resolve().parents[3]
SOURCE_VIDEO = PROJECT_ROOT / "01_intake/references/reference-003-full-op-2160p.mp4"
R5_REPORT = PROJECT_ROOT / "10_qa/reports/reference003_r5_video_segment_all_units01_21_generation_ready_20260701.json"
R6_BOUNDARY_REPORT = PROJECT_ROOT / "01_intake/analysis/reference003_frame_boundary_refine_r6_20260701/reference003_frame_boundary_refine_r6_20260701.json"
SETTING_CHAPTER = PROJECT_ROOT / "05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md"
ASSET_LOCKS = PROJECT_ROOT / "05_asset_bible/setting_chapters/reference003_asset_locks_v1.json"
PACKAGE_ROOT = PROJECT_ROOT / "08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701"
CANDIDATE_ROOT = PROJECT_ROOT / "08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701"
ANALYSIS_ROOT = PROJECT_ROOT / "01_intake/analysis/reference003_r7_high_precision_units_20260701"
EXPECTED_VIDEO_ROOT = PROJECT_ROOT / "08_generation/outputs/video/reference003_r7_high_precision_segments"
REPORT_DIR = PROJECT_ROOT / "10_qa/reports"
FFMPEG = Path("/Applications/Bitwig Studio.app/Contents/MacOS/ffmpeg")


@dataclass(frozen=True)
class R7Unit:
    order: int
    unit_id: str
    title: str
    start: float
    end: float
    intent: str
    active_locks: tuple[tuple[str, str], ...]
    mode: str = "high_precision_segment"


R7_UNITS = [
    R7Unit(1, "VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG", "开场长段A：黑场云层到白鸟入画", 0.0, 7.0, "连续天空开场，黑场/云层/白鸟作为一个长运动短语处理。", (("props_vehicles_symbols", "white_bird"),), "long_opening"),
    R7Unit(2, "VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG", "开场长段B：白鸟云层到飞行器闪现", 7.0, 16.5, "保留白鸟/云层长运动，并精准抓住 00:14.72 飞行器一闪。", (("props_vehicles_symbols", "white_bird"), ("props_vehicles_symbols", "jean_aircraft")), "long_opening_flash"),
    R7Unit(3, "VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA", "开场长段C：标题安全位到日光转Nadia", 16.5, 24.8, "无字标题安全位、日光耀斑和 Nadia 首次显影作为开场收束。", (("characters", "nadia"), ("props_vehicles_symbols", "blue_water_pendant")), "long_opening"),
    R7Unit(4, "VU_REF003_R7_004_NADIA_PROFILE_CONTINUE", "Nadia侧脸延续", 24.8, 25.901, "Nadia 首次亮相后的侧脸延续，不并入 Jean。", (("characters", "nadia"), ("props_vehicles_symbols", "blue_water_pendant"))),
    R7Unit(5, "VU_REF003_R7_005_NADIA_CLOSE_INSERT", "Nadia近景插入", 25.901, 26.818, "Nadia 从侧脸进入更近的人物状态。", (("characters", "nadia"), ("props_vehicles_symbols", "blue_water_pendant"))),
    R7Unit(6, "VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE", "Nadia到Jean过渡", 26.818, 28.862, "Nadia 段落向 Jean 入场切换，避免混淆人物归属。", (("characters", "nadia"), ("characters", "jean"), ("props_vehicles_symbols", "blue_water_pendant"))),
    R7Unit(7, "VU_REF003_R7_007_JEAN_FACE_FLASH", "Jean帽子正脸短插", 28.862, 29.488, "Jean 正脸/帽子短促亮相，单独约束 Jean 身份。", (("characters", "jean"),)),
    R7Unit(8, "VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE", "Jean到Marie草地过渡", 29.488, 31.949, "Jean 段落过渡到 Marie/King 草地段。", (("characters", "jean"), ("characters", "marie"), ("characters", "king"))),
    R7Unit(9, "VU_REF003_R7_009_MARIE_KING_MEADOW", "Marie与King草地段", 31.949, 33.951, "Marie 与 King 草地亮相，儿童/动物锁定。", (("characters", "marie"), ("characters", "king"))),
    R7Unit(10, "VU_REF003_R7_010_GRANDIS_TRIO_WIDE", "Grandis三人组广角", 33.951, 35.953, "Grandis 三人组广角亮相。", (("characters", "grandis"), ("characters", "sanson"), ("characters", "hanson"))),
    R7Unit(11, "VU_REF003_R7_011_GRANDIS_TRIO_CLOSE", "Grandis三人组近景", 35.953, 37.204, "Grandis 三人组近景/表演状态，不能和前一广角混成同一镜。", (("characters", "grandis"), ("characters", "sanson"), ("characters", "hanson"))),
    R7Unit(12, "VU_REF003_R7_012_RUN_MONTAGE_ENTRY", "奔跑Montage入场", 37.204, 38.121, "奔跑 montage 入场短切。", (("characters", "nadia"),)),
    R7Unit(13, "VU_REF003_R7_013_NADIA_RUN_FEET", "Nadia奔跑脚步", 38.121, 39.5, "Nadia 奔跑脚步/身体节拍，不生成性感化身体强调。", (("characters", "nadia"), ("props_vehicles_symbols", "blue_water_pendant"))),
    R7Unit(14, "VU_REF003_R7_014_NADIA_RUN_FRONT", "Nadia正面奔跑", 39.5, 41.5, "Nadia 正面奔跑节拍。", (("characters", "nadia"), ("props_vehicles_symbols", "blue_water_pendant"))),
    R7Unit(15, "VU_REF003_R7_015_JEAN_RUN", "Jean奔跑", 41.5, 43.5, "Jean 独立奔跑节拍。", (("characters", "jean"),)),
    R7Unit(16, "VU_REF003_R7_016_MARIE_KING_RUN", "Marie与King奔跑", 43.5, 45.5, "Marie/King 独立奔跑节拍。", (("characters", "marie"), ("characters", "king"))),
    R7Unit(17, "VU_REF003_R7_017_GROUP_RUN", "群像奔跑", 45.5, 47.422, "全员奔跑群像节拍，必须用多角色锁图。", (("characters", "nadia"), ("characters", "jean"), ("characters", "marie"), ("characters", "king"), ("props_vehicles_symbols", "blue_water_pendant"))),
    R7Unit(18, "VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER", "奔跑到动作插入簇", 47.422, 48.173, "Jean反应/动作桥接短簇，避免被吞进奔跑长段。", (("characters", "jean"), ("characters", "grandis"), ("characters", "sanson"), ("characters", "hanson"))),
    R7Unit(19, "VU_REF003_R7_019_GRANDIS_ACTION_INSERT", "Grandis动作短插", 48.173, 48.674, "Grandis 阵营动作一闪短插。", (("characters", "grandis"), ("characters", "sanson"), ("characters", "hanson"))),
    R7Unit(20, "VU_REF003_R7_020_VEHICLE_PREP_FLASH", "车辆动作预备闪帧", 48.674, 49.675, "车辆动作前的短暂准备/闪帧。", (("characters", "grandis"), ("characters", "sanson"), ("characters", "hanson"), ("props_vehicles_symbols", "grandis_vehicle"))),
    R7Unit(21, "VU_REF003_R7_021_VEHICLE_ARC", "车辆飞行动作", 49.675, 50.676, "复古车辆/飞行器弧线动作。", (("props_vehicles_symbols", "grandis_vehicle"),)),
    R7Unit(22, "VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA", "群像到海底过渡", 50.676, 52.427, "群像 tableau 过渡进入 Nautilus 海底段。", (("characters", "nadia"), ("characters", "jean"), ("characters", "marie"), ("characters", "king"), ("props_vehicles_symbols", "nautilus"))),
    R7Unit(23, "VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY", "Nautilus海底入场", 52.427, 55.0, "Nautilus 海底入场，水下光束与潜艇比例锁定。", (("props_vehicles_symbols", "nautilus"),)),
    R7Unit(24, "VU_REF003_R7_024_NAUTILUS_PASS", "Nautilus水下通过", 55.0, 57.0, "潜艇水下通过中段。", (("props_vehicles_symbols", "nautilus"),)),
    R7Unit(25, "VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT", "Nautilus光带变化", 57.0, 58.5, "水下光带/潜艇剪影变化。", (("props_vehicles_symbols", "nautilus"),)),
    R7Unit(26, "VU_REF003_R7_026_NAUTILUS_EXIT", "Nautilus海底尾段", 58.5, 61.436, "Nautilus 海底尾段，不生成原片职员表文字。", (("props_vehicles_symbols", "nautilus"),)),
    R7Unit(27, "VU_REF003_R7_027_NIGHT_CITY_GRID", "夜城蓝网格", 61.436, 64.94, "夜城与蓝色地面/几何图案。", (("props_vehicles_symbols", "blue_grid_geometry"),)),
    R7Unit(28, "VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS", "夜航飞行器短切", 64.94, 66.024, "夜航飞行器短切。", (("props_vehicles_symbols", "jean_aircraft"),)),
    R7Unit(29, "VU_REF003_R7_029_NEMO_SUNSET_PROFILE", "Nemo夕景肖像长段", 66.024, 71.363, "Nemo 船长夕景肖像长段，首尾/中间关键帧承载连续运动。", (("characters", "nemo"),), "slow_hold"),
    R7Unit(30, "VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL", "Nadia庄重到宝石", 71.363, 74.074, "Nadia 庄重正面过渡到 Blue Water 象征。", (("characters", "nadia"), ("props_vehicles_symbols", "blue_water_pendant"))),
    R7Unit(31, "VU_REF003_R7_031_BLUE_WATER_BLOOM", "Blue Water蓝色绽放", 74.074, 76.451, "Blue Water 象征蓝色绽放/水下纹理。", (("props_vehicles_symbols", "blue_water_pendant"),)),
    R7Unit(32, "VU_REF003_R7_032_UNDERWATER_TO_SPLASH", "水下纹理到水花", 76.451, 77.786, "水下纹理进入水花爆发。", (("props_vehicles_symbols", "water_burst_transition"),)),
    R7Unit(33, "VU_REF003_R7_033_SPLASH_PEAK", "水花爆发峰值", 77.786, 79.204, "水花爆发峰值与天空转场。", (("props_vehicles_symbols", "water_burst_transition"),)),
    R7Unit(34, "VU_REF003_R7_034_FINAL_SKY_TRANSITION", "最终天空转场", 79.204, 80.789, "水花后转入最终无字天空。", ()),
    R7Unit(35, "VU_REF003_R7_035_FINAL_SKY_HOLD", "最终天空Hold", 80.789, 83.584, "最终无字天空 hold。", ()),
    R7Unit(36, "VU_REF003_R7_036_BLACK_TAIL", "黑场尾帧", 83.584, 84.418, "黑场尾帧。", ()),
]


def rel(path: Path | str) -> str:
    p = Path(path)
    return p.relative_to(PROJECT_ROOT).as_posix() if p.is_absolute() else p.as_posix()


def tc(seconds: float) -> str:
    minutes = int(seconds // 60)
    sec = seconds - minutes * 60
    return f"{minutes:02d}:{sec:05.2f}"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def safe(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]+", "_", text).strip("_")


def load_generated_anchors() -> list[dict[str, Any]]:
    report = read_json(R5_REPORT)
    anchors: list[dict[str, Any]] = []
    for job in report["jobs"]:
        for anchor in read_json(PROJECT_ROOT / job["job_dir"] / "ordered_keyframe_anchors.json"):
            a = dict(anchor)
            a["source_unit_id"] = job["unit_id"]
            anchors.append(a)
    anchors.sort(key=lambda item: (float(item["time_sec"]), item["item_id"]))
    return anchors


def load_asset_locks() -> list[dict[str, Any]]:
    data = read_json(ASSET_LOCKS)
    out_root = PACKAGE_ROOT / "_global_asset_locks"
    if out_root.exists():
        shutil.rmtree(out_root)
    out_root.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    for group in ("characters", "props_vehicles_symbols"):
        for asset_id, lock in data.get(group, {}).items():
            src_rel = lock.get("lock_path") or ""
            dst_rel = ""
            exists = False
            if src_rel:
                src = PROJECT_ROOT / src_rel
                dst = out_root / f"{group}_{asset_id}{src.suffix or '.png'}"
                if src.exists():
                    shutil.copy2(src, dst)
                dst_rel = rel(dst)
                exists = dst.exists()
            rows.append(
                {
                    "group": group,
                    "asset_id": asset_id,
                    "status": lock.get("status", ""),
                    "source_path": src_rel,
                    "global_lock_path": dst_rel,
                    "exists": exists,
                }
            )
    (out_root / "asset_locks_manifest.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return rows


def active_lock_records(unit: R7Unit, all_locks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_key = {(row["group"], row["asset_id"]): row for row in all_locks}
    return [by_key[key] for key in unit.active_locks if key in by_key]


def anchors_for_unit(unit: R7Unit, anchors: list[dict[str, Any]]) -> list[dict[str, Any]]:
    # Include current generated assets inside the segment, plus very near boundary anchors.
    tolerance = 0.22
    selected = [
        a for a in anchors
        if unit.start - tolerance <= float(a["time_sec"]) <= unit.end + tolerance
    ]
    if not selected:
        midpoint = (unit.start + unit.end) / 2
        selected = sorted(anchors, key=lambda a: abs(float(a["time_sec"]) - midpoint))[:1]
    selected.sort(key=lambda a: (float(a["time_sec"]), a["item_id"]))
    return selected


def copy_anchors(unit: R7Unit, anchors: list[dict[str, Any]], job_dir: Path) -> list[dict[str, Any]]:
    key_dir = job_dir / "keyframes"
    if key_dir.exists():
        shutil.rmtree(key_dir)
    key_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    for idx, anchor in enumerate(anchors, start=1):
        src = PROJECT_ROOT / anchor["source_path"]
        dst = key_dir / f"{idx:02d}_{safe(anchor['item_id'])}{src.suffix or '.png'}"
        if src.exists():
            shutil.copy2(src, dst)
        row = dict(anchor)
        row["order"] = idx
        row["packaged_path"] = rel(dst)
        row["exists"] = dst.exists()
        rows.append(row)
    return rows


def clip(unit: R7Unit, out_path: Path) -> dict[str, Any]:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(FFMPEG), "-y", "-ss", f"{unit.start:.3f}", "-i", str(SOURCE_VIDEO),
        "-t", f"{unit.end - unit.start:.3f}", "-an", "-c:v", "mpeg4", "-q:v", "3", str(out_path),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    dec = subprocess.run([str(FFMPEG), "-v", "error", "-i", str(out_path), "-f", "null", "-"], capture_output=True, text=True)
    return {
        "path": rel(out_path),
        "start_sec": round(unit.start, 3),
        "end_sec": round(unit.end, 3),
        "duration_sec": round(unit.end - unit.start, 3),
        "ok": proc.returncode == 0 and out_path.exists() and out_path.stat().st_size > 0,
        "decode_ok": dec.returncode == 0,
        "stderr_tail": "\n".join((proc.stderr or dec.stderr or "").splitlines()[-8:]),
    }


def capture_frame(cap: cv2.VideoCapture, fps: float, seconds: float) -> Image.Image:
    frame_idx = max(0, int(round(seconds * fps)))
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
    ok, frame = cap.read()
    if not ok:
        raise RuntimeError(f"Failed to capture frame at {seconds:.3f}")
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return Image.fromarray(rgb)


def make_sheet(items: list[tuple[str, Path]], out_path: Path, cols: int = 5, thumb_w: int = 260) -> None:
    if not items:
        return
    font = ImageFont.load_default()
    gap = 10
    label_h = 46
    thumbs = []
    for label, path in items:
        with Image.open(path) as img:
            img = img.convert("RGB")
            h = int(thumb_w * img.height / img.width)
            thumbs.append((label, img.resize((thumb_w, h), Image.Resampling.LANCZOS)))
    max_h = max(img.height for _, img in thumbs)
    rows = math.ceil(len(thumbs) / cols)
    sheet = Image.new("RGB", (cols * thumb_w + (cols + 1) * gap, rows * (max_h + label_h) + (rows + 1) * gap), (242, 242, 238))
    draw = ImageDraw.Draw(sheet)
    for idx, (label, img) in enumerate(thumbs):
        c = idx % cols
        r = idx // cols
        x = gap + c * (thumb_w + gap)
        y = gap + r * (max_h + label_h + gap)
        sheet.paste(img, (x, y))
        draw.text((x + 4, y + max_h + 5), label[:48], fill=(20, 20, 20), font=font)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path, quality=92)


def capture_candidates(unit: R7Unit, packaged_anchors: list[dict[str, Any]], cap: cv2.VideoCapture, fps: float, job_dir: Path) -> list[dict[str, Any]]:
    cand_dir = job_dir / "candidate_reference_frames"
    cand_dir.mkdir(parents=True, exist_ok=True)
    anchor_times = [float(a["time_sec"]) for a in packaged_anchors]
    roles = [("start", unit.start + 0.03), ("end", unit.end - 0.03)]
    if unit.end - unit.start >= 1.15:
        roles.append(("middle", (unit.start + unit.end) / 2))
    candidates: list[dict[str, Any]] = []
    for role, t in roles:
        empty_or_safe_hold = not unit.active_locks and any(
            token in unit.unit_id
            for token in ("FINAL_SKY", "BLACK_TAIL")
        )
        if empty_or_safe_hold:
            priority = "P3_reference_video_or_already_handled"
        elif anchor_times and min(abs(t - a) for a in anchor_times) <= 0.38:
            priority = "P3_reference_video_or_already_handled"
        elif unit.mode in {"long_opening_flash", "high_precision_segment"} and (unit.end - unit.start) <= 1.6:
            priority = "P1_generate_next_small_batch"
        elif len(packaged_anchors) < 2:
            priority = "P1_generate_next_small_batch"
        else:
            priority = "P2_review_after_p1"
        asset_id = f"R7_CAND_{unit.order:03d}_{role}_{int(round(t * 1000)):06d}ms"
        path = cand_dir / f"{asset_id}.jpg"
        img = capture_frame(cap, fps, t)
        img.save(path, quality=94)
        candidates.append(
            {
                "asset_id": asset_id,
                "parent_video_unit_id": unit.unit_id,
                "role": role,
                "source_time_sec": round(t, 3),
                "source_timecode": tc(t),
                "reference_frame_path": rel(path),
                "priority": priority,
                "status": "candidate_reference_frame_needs_prompt_and_generation" if priority.startswith("P1") else "candidate_reference_frame_review",
                "difference_reason": f"{unit.title} {role} boundary/transition frame from R7 high-precision split.",
                "planned_output_path": rel(CANDIDATE_ROOT / "outputs" / f"{asset_id}.png"),
            }
        )
    return candidates


def prompt_text(unit: R7Unit, anchors: list[dict[str, Any]], candidates: list[dict[str, Any]], locks: list[dict[str, Any]]) -> str:
    anchor_lines = "\n".join(
        f"- 图{a['order']}: `{a['item_id']}` ({a.get('timecode', '')}, {a.get('kind', '')}) `{a['packaged_path']}`"
        for a in anchors
    ) or "- no generated anchors available; use candidate frames only for analysis and generate pure image anchors first."
    candidate_lines = "\n".join(
        f"- `{c['asset_id']}` ({c['role']}, {c['source_timecode']}, {c['priority']}): `{c['reference_frame_path']}`"
        for c in candidates
    )
    lock_lines = "\n".join(
        f"- `{lock['asset_id']}` ({lock.get('status', '')}): `{lock.get('global_lock_path', '')}`"
        for lock in locks
    ) or "- none"
    return f"""# {unit.order:02d} — {unit.unit_id} — {unit.title}

## Upload These

1. Reference video: `{PACKAGE_ROOT.relative_to(PROJECT_ROOT).as_posix()}/{unit.unit_id}/reference_clip/{unit.unit_id}_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
{anchor_lines}
3. Active asset locks:
{lock_lines}

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

{candidate_lines}

## Save Result To

`{EXPECTED_VIDEO_ROOT.relative_to(PROJECT_ROOT).as_posix()}/{unit.unit_id}.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `{unit.unit_id}`.
Time range: `{tc(unit.start)}-{tc(unit.end)}`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: {unit.intent}

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
"""


def image_generation_prompt(candidate: dict[str, Any], unit: R7Unit, locks: list[dict[str, Any]], nearest_anchors: list[dict[str, Any]]) -> str:
    lock_names = ", ".join(lock["asset_id"] for lock in locks) or "none"
    anchor_names = ", ".join(a["item_id"] for a in nearest_anchors[:3]) or "none"
    return (
        "21:9 anamorphic live-action keyframe, faithful high-end live-action remake of the reference-003 OP, "
        "pure image only, no readable text/logo/subtitle/watermark. "
        f"Use source frame `{candidate['reference_frame_path']}` at {candidate['source_timecode']} as composition/timing reference. "
        f"Video unit: {unit.unit_id} ({unit.title}). Shot intent: {unit.intent} "
        f"Preserve active locks when visible: {lock_names}. Nearest generated anchors for continuity: {anchor_names}. "
        "Do not copy anime line art; create a clean live-action remake frame. "
        "Negative prompt: readable text, title letters, lyrics, credits, broadcaster mark, subtitle, watermark, random symbols, distorted face or hands, changed identity, changed prop design, sexualized minor."
    )


def main() -> int:
    now = datetime.now(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()
    for root in (PACKAGE_ROOT, CANDIDATE_ROOT, ANALYSIS_ROOT):
        if root.exists():
            shutil.rmtree(root)
        root.mkdir(parents=True, exist_ok=True)
    EXPECTED_VIDEO_ROOT.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    all_anchors = load_generated_anchors()
    all_locks = load_asset_locks()
    cap = cv2.VideoCapture(str(SOURCE_VIDEO))
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open {SOURCE_VIDEO}")
    fps = float(cap.get(cv2.CAP_PROP_FPS) or 24000 / 1001)

    prompt_root = PACKAGE_ROOT / "_PROMPT_INDEX" / "PROMPT_ONLY"
    prompt_root.mkdir(parents=True, exist_ok=True)
    candidate_rows: list[dict[str, Any]] = []
    jobs: list[dict[str, Any]] = []
    index_rows: list[str] = []
    csv_rows: list[dict[str, Any]] = []

    for unit in R7_UNITS:
        job_dir = PACKAGE_ROOT / unit.unit_id
        job_dir.mkdir(parents=True, exist_ok=True)
        generated = anchors_for_unit(unit, all_anchors)
        packaged = copy_anchors(unit, generated, job_dir)
        (job_dir / "ordered_keyframe_anchors.json").write_text(json.dumps(packaged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        make_sheet([(f"{a.get('timecode', '')} {a['item_id']}", PROJECT_ROOT / a["packaged_path"]) for a in packaged], job_dir / "ordered_keyframe_contact_sheet.jpg", cols=4, thumb_w=280)
        candidates = capture_candidates(unit, packaged, cap, fps, job_dir)
        locks = active_lock_records(unit, all_locks)
        (job_dir / "candidate_reference_frames.json").write_text(json.dumps(candidates, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (job_dir / "active_asset_locks.json").write_text(json.dumps(locks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        clip_result = clip(unit, job_dir / "reference_clip" / f"{unit.unit_id}_reference.mp4")
        prompt = prompt_text(unit, packaged, candidates, locks)
        prompt_path = prompt_root / f"{unit.order:02d}_{unit.unit_id}.md"
        prompt_path.write_text(prompt, encoding="utf-8")
        (job_dir / "AIGC_VIDEO_GENERATION_BRIEF.md").write_text(prompt, encoding="utf-8")
        manifest = {
            "schema_version": "reference003_r7_high_precision_video_unit_package_v1",
            "created_at": now,
            "status": "ready_for_external_aigc_video_generation" if clip_result["decode_ok"] and all(a["exists"] for a in packaged) else "needs_review",
            "unit": unit.__dict__,
            "reference_clip": clip_result,
            "ordered_generated_anchors": packaged,
            "candidate_reference_frames": candidates,
            "active_asset_locks": locks,
            "prompt_only": rel(prompt_path),
            "expected_video_output_path": rel(EXPECTED_VIDEO_ROOT / f"{unit.unit_id}.mp4"),
        }
        (job_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        ready = manifest["status"] == "ready_for_external_aigc_video_generation"
        jobs.append(
            {
                "order": unit.order,
                "unit_id": unit.unit_id,
                "title": unit.title,
                "time_range": f"{tc(unit.start)}-{tc(unit.end)}",
                "duration_sec": round(unit.end - unit.start, 3),
                "job_dir": rel(job_dir),
                "ready": ready,
                "generated_anchor_count": len(packaged),
                "r5_anchor_count": sum(1 for a in packaged if a.get("kind") == "r5_adaptive_generated"),
                "candidate_frame_count": len(candidates),
                "p1_candidate_count": sum(1 for c in candidates if c["priority"].startswith("P1")),
                "active_locks": [lock["asset_id"] for lock in locks],
                "reference_clip": clip_result,
                "prompt_only": rel(prompt_path),
                "expected_video_output_path": rel(EXPECTED_VIDEO_ROOT / f"{unit.unit_id}.mp4"),
            }
        )
        index_rows.append(
            f"| {unit.order:02d} | `{unit.unit_id}` | {unit.title} | `{tc(unit.start)}-{tc(unit.end)}` | {len(packaged)} | "
            f"{sum(1 for c in candidates if c['priority'].startswith('P1'))} | `{rel(prompt_path)}` |"
        )
        csv_rows.append(
            {
                "order": unit.order,
                "unit_id": unit.unit_id,
                "title": unit.title,
                "time_range": f"{tc(unit.start)}-{tc(unit.end)}",
                "generated_anchor_count": len(packaged),
                "p1_candidate_count": sum(1 for c in candidates if c["priority"].startswith("P1")),
                "prompt_only": rel(prompt_path),
            }
        )
        for cand in candidates:
            row = dict(cand)
            row["image_prompt"] = image_generation_prompt(cand, unit, locks, packaged)
            row["unit_title"] = unit.title
            candidate_rows.append(row)

    cap.release()

    index_md = PACKAGE_ROOT / "_PROMPT_INDEX" / "AIGC_VIDEO_PROMPT_INDEX.md"
    index_md.write_text(
        "\n".join(
            [
                "# Reference-003 R7 High-Precision Video Prompt Index",
                "",
                "R7 uses source-FPS boundary detection + PySceneDetect cross-checks and current generated anchors.",
                "Each prompt-only file lists current official/R5 generated images explicitly; old unit prompt text is not the source of truth.",
                "",
                f"- Setting chapter: `{rel(SETTING_CHAPTER)}`",
                f"- Boundary source: `{rel(R6_BOUNDARY_REPORT)}`",
                f"- Package root: `{rel(PACKAGE_ROOT)}`",
                "",
                "| # | Unit | Title | Time Range | Generated Anchors | P1 Candidates | Prompt |",
                "|---:|---|---|---|---:|---:|---|",
                *index_rows,
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    (PACKAGE_ROOT / "_PROMPT_INDEX" / "AIGC_VIDEO_PROMPT_INDEX.json").write_text(json.dumps(jobs, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    shutil.copy2(index_md, PACKAGE_ROOT / "README_USE_THIS_FIRST.md")
    (PACKAGE_ROOT / "manifest.json").write_text(json.dumps({"schema_version": "reference003_r7_high_precision_package_root_v1", "created_at": now, "jobs": jobs}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    candidate_rows.sort(key=lambda c: (0 if c["priority"].startswith("P1") else 1, c["source_time_sec"], c["asset_id"]))
    p1_rows = [row for row in candidate_rows if row["priority"].startswith("P1")]
    p2_rows = [row for row in candidate_rows if row["priority"].startswith("P2")]
    p3_rows = [row for row in candidate_rows if row["priority"].startswith("P3")]
    CANDIDATE_ROOT.joinpath("outputs").mkdir(parents=True, exist_ok=True)
    queue_json = CANDIDATE_ROOT / "reference003_r7_candidate_image_generation_queue.json"
    queue_json.write_text(json.dumps({"created_at": now, "status": "analysis_ready_candidates_not_generated", "p1_count": len(p1_rows), "p2_count": len(p2_rows), "p3_count": len(p3_rows), "items": candidate_rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    p1_sheet_items = [(f"{row['source_timecode']} {row['asset_id']}", PROJECT_ROOT / row["reference_frame_path"]) for row in p1_rows]
    p1_sheet = CANDIDATE_ROOT / "reference003_r7_p1_candidate_contact_sheet.jpg"
    make_sheet(p1_sheet_items, p1_sheet, cols=5, thumb_w=250)
    queue_md = CANDIDATE_ROOT / "reference003_r7_candidate_image_generation_queue.md"
    queue_md.write_text(
        "\n".join(
            [
                "# Reference-003 R7 Candidate Image Generation Queue",
                "",
                "- Status: `analysis_ready_candidates_not_generated`",
                f"- P1: {len(p1_rows)}",
                f"- P2: {len(p2_rows)}",
                f"- P3: {len(p3_rows)}",
                f"- P1 contact sheet: `{rel(p1_sheet)}`",
                "",
                "## P1 Items",
                "",
                "| time | candidate | unit | reason | planned output |",
                "|---:|---|---|---|---|",
                *[
                    f"| {row['source_timecode']} | `{row['asset_id']}` | `{row['parent_video_unit_id']}` | {row['difference_reason']} | `{row['planned_output_path']}` |"
                    for row in p1_rows
                ],
                "",
                "Candidates are screenshots, not final assets. Generate pure images first, then update output paths and rebuild the preview.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    with (ANALYSIS_ROOT / "reference003_r7_high_precision_units.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys()))
        writer.writeheader()
        writer.writerows(csv_rows)

    report = {
        "schema_version": "reference003_r7_high_precision_video_units_report_v1",
        "created_at": now,
        "status": "ready_for_external_aigc_video_generation_with_candidate_queue",
        "unit_count": len(jobs),
        "ready_jobs": sum(1 for job in jobs if job["ready"]),
        "total_generated_anchors": sum(job["generated_anchor_count"] for job in jobs),
        "total_r5_anchors": sum(job["r5_anchor_count"] for job in jobs),
        "total_candidate_frames": len(candidate_rows),
        "p1_candidate_count": len(p1_rows),
        "p2_candidate_count": len(p2_rows),
        "p3_candidate_count": len(p3_rows),
        "package_root": rel(PACKAGE_ROOT),
        "prompt_index": rel(index_md),
        "candidate_queue_json": rel(queue_json),
        "candidate_queue_md": rel(queue_md),
        "p1_contact_sheet": rel(p1_sheet),
        "jobs": jobs,
    }
    report_json = REPORT_DIR / "reference003_r7_high_precision_video_units_20260701.json"
    report_md = REPORT_DIR / "reference003_r7_high_precision_video_units_20260701.md"
    report["report_json"] = rel(report_json)
    report["report_md"] = rel(report_md)
    report_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report_md.write_text(
        "\n".join(
            [
                "# Reference-003 R7 High-Precision Video Units",
                "",
                f"- Status: `{report['status']}`",
                f"- Units: {report['ready_jobs']}/{report['unit_count']} ready",
                f"- Generated anchors in prompts: {report['total_generated_anchors']} total, including {report['total_r5_anchors']} R5 anchors",
                f"- Candidate screenshots: {report['total_candidate_frames']} total; P1 {report['p1_candidate_count']}, P2 {report['p2_candidate_count']}, P3 {report['p3_candidate_count']}",
                f"- Prompt index: `{report['prompt_index']}`",
                f"- Candidate queue: `{report['candidate_queue_md']}`",
                "",
                "| # | Unit | Time | Anchors | R5 | P1 | Prompt |",
                "|---:|---|---|---:|---:|---:|---|",
                *[
                    f"| {job['order']:02d} | `{job['unit_id']}` | `{job['time_range']}` | {job['generated_anchor_count']} | {job['r5_anchor_count']} | {job['p1_candidate_count']} | `{job['prompt_only']}` |"
                    for job in jobs
                ],
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(json.dumps({
        "status": report["status"],
        "unit_count": report["unit_count"],
        "ready_jobs": report["ready_jobs"],
        "generated_anchors": report["total_generated_anchors"],
        "r5_anchors": report["total_r5_anchors"],
        "p1_candidates": report["p1_candidate_count"],
        "package_root": report["package_root"],
        "prompt_index": report["prompt_index"],
        "candidate_queue": report["candidate_queue_md"],
        "report_md": report["report_md"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
