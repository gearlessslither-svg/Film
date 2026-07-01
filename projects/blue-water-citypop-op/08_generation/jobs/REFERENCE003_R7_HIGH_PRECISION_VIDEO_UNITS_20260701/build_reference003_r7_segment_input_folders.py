#!/usr/bin/env python3
"""Build self-contained per-segment input folders for external AIGC video generation."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any


JOB_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = JOB_DIR.parents[2]
QUEUE_PATH = (
    PROJECT_ROOT
    / "08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/"
    "reference003_r7_candidate_image_generation_queue.json"
)
OUTPUT_ROOT = (
    PROJECT_ROOT
    / "11_delivery/packages/reference003_r7_aigc_video_segment_input_folders_20260701"
)
LEAN_OUTPUT_ROOT = (
    PROJECT_ROOT
    / "11_delivery/packages/reference003_r8_lean_aigc_video_segment_input_folders_20260701"
)
REGULAR_MIN2S_OUTPUT_ROOT = (
    PROJECT_ROOT
    / "11_delivery/packages/reference003_r8_lean_regular_reference_materials_min2s_20260702"
)
SHORT_UNDER2S_OUTPUT_ROOT = (
    PROJECT_ROOT
    / "11_delivery/packages/reference003_r8_lean_short_reference_materials_under2s_20260702"
)
FFMPEG_CANDIDATES = [
    Path("/Users/jaychoupp/Library/Application Support/bilibili/ffmpeg/ffmpeg"),
    Path("/opt/homebrew/bin/ffmpeg"),
    Path("/usr/local/bin/ffmpeg"),
]
MIN_REFERENCE_MATERIAL_SECONDS = 2.05


def rel(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def timecode(seconds: float | int | None) -> str:
    if seconds is None:
        return "00:00.00"
    total = float(seconds)
    minutes = int(total // 60)
    secs = total - minutes * 60
    return f"{minutes:02d}:{secs:05.2f}"


def parse_timecode(value: str | None) -> float:
    if not value:
        return 0.0
    text = str(value)
    if ":" not in text:
        try:
            return float(text)
        except ValueError:
            return 0.0
    minutes, seconds = text.split(":", 1)
    try:
        return int(minutes) * 60 + float(seconds)
    except ValueError:
        return 0.0


def unit_time_range(unit: dict[str, Any]) -> str:
    return f"{timecode(unit.get('start'))}-{timecode(unit.get('end'))}"


def ensure_clean_dir(path: Path, clean: bool) -> None:
    if clean and path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def materialize(src: Path, dst: Path) -> None:
    """Create a real file entry at dst, using a hardlink when possible."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() or dst.is_symlink():
        dst.unlink()
    try:
        os.link(src, dst)
    except OSError:
        shutil.copy2(src, dst)


def find_ffmpeg() -> Path:
    for candidate in FFMPEG_CANDIDATES:
        if candidate.exists():
            return candidate
    resolved = shutil.which("ffmpeg")
    if resolved:
        return Path(resolved)
    raise RuntimeError("ffmpeg not found; cannot build upload-compatible reference clips")


def probe_duration_seconds(src: Path) -> float | None:
    ffmpeg = find_ffmpeg()
    result = subprocess.run(
        [str(ffmpeg), "-hide_banner", "-i", str(src)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", result.stderr)
    if not match:
        return None
    hours, minutes, seconds = match.groups()
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


def transcode_reference_clip(src: Path, dst: Path, pad_short_to_min: bool) -> dict[str, Any]:
    """Write a website-friendly H.264/AAC MP4; optionally hold the last frame to >=2s."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() or dst.is_symlink():
        dst.unlink()
    ffmpeg = find_ffmpeg()
    source_duration = probe_duration_seconds(src)
    pad_seconds = 0.0
    if pad_short_to_min and source_duration is not None and source_duration < MIN_REFERENCE_MATERIAL_SECONDS:
        pad_seconds = MIN_REFERENCE_MATERIAL_SECONDS - source_duration
    vf = "scale=trunc(iw/2)*2:trunc(ih/2)*2,format=yuv420p"
    if pad_seconds > 0:
        vf += f",tpad=stop_mode=clone:stop_duration={pad_seconds:.3f}"
    cmd = [
        str(ffmpeg),
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(src),
        "-f",
        "lavfi",
        "-i",
        "anullsrc=channel_layout=stereo:sample_rate=48000",
        "-map",
        "0:v:0",
        "-map",
        "1:a:0",
        "-vf",
        vf,
        "-r",
        "24000/1001",
        "-c:v",
        "libx264",
        "-profile:v",
        "high",
        "-level",
        "4.1",
        "-preset",
        "veryfast",
        "-crf",
        "18",
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-shortest",
        "-movflags",
        "+faststart",
        "-map_metadata",
        "-1",
        str(dst),
    ]
    subprocess.run(cmd, check=True)
    output_duration = probe_duration_seconds(dst)
    return {
        "source_duration_seconds": source_duration,
        "output_duration_seconds": output_duration,
        "minimum_reference_material_seconds": 2.0,
        "encoding_floor_seconds": MIN_REFERENCE_MATERIAL_SECONDS,
        "padded_last_frame_seconds": round(pad_seconds, 3),
    }


def safe_name(index: int, unit_id: str) -> str:
    return f"{index:02d}_{unit_id}"


def fmt_seconds(value: float | int | None) -> str:
    if value is None:
        return "unknown"
    return f"{float(value):.2f}"


def load_units() -> list[dict[str, Any]]:
    units = []
    for manifest_path in sorted(JOB_DIR.glob("VU_REF003_R7_*/manifest.json")):
        manifest = read_json(manifest_path)
        manifest["_manifest_path"] = manifest_path
        manifest["_unit_dir"] = manifest_path.parent
        units.append(manifest)
    return sorted(units, key=lambda item: item["unit"]["order"])


def reference_source_path(unit_manifest: dict[str, Any]) -> Path:
    return PROJECT_ROOT / unit_manifest["reference_clip"]["path"]


def is_short_reference_material(unit_manifest: dict[str, Any]) -> bool:
    duration = unit_manifest["unit"].get("end", 0) - unit_manifest["unit"].get("start", 0)
    return float(duration) < 2.0


def load_candidates_by_unit() -> dict[str, list[dict[str, Any]]]:
    queue = read_json(QUEUE_PATH)
    by_unit: dict[str, list[dict[str, Any]]] = {}
    for item in queue.get("items", []):
        unit_id = item.get("parent_video_unit_id")
        if not unit_id:
            continue
        generated_path = item.get("generated_output_path") or item.get("planned_output_path")
        item = dict(item)
        item["_generated_path"] = generated_path
        by_unit.setdefault(unit_id, []).append(item)
    for rows in by_unit.values():
        rows.sort(key=lambda item: (float(item.get("source_time_sec") or 0), item.get("asset_id") or ""))
    return by_unit


def copy_reference_clip(
    unit_manifest: dict[str, Any],
    unit_dir: Path,
    short_material_package: bool,
) -> dict[str, Any]:
    ref = unit_manifest["reference_clip"]["path"]
    src = reference_source_path(unit_manifest)
    if short_material_package:
        original_dst = (
            unit_dir
            / "00_original_independent_reference_clip"
            / f"{src.stem}_independent_original_duration_h264_aac.mp4"
        )
        original_info = transcode_reference_clip(src, original_dst, pad_short_to_min=False)
        dst = (
            unit_dir
            / "01_reference_clip_same_shot_hold_min2s_optional"
            / f"{src.stem}_same_shot_hold_min2s_h264_aac.mp4"
        )
        transcode_info = transcode_reference_clip(src, dst, pad_short_to_min=True)
        return {
            "source": ref,
            "local": dst.relative_to(unit_dir).as_posix(),
            "original_independent_local": original_dst.relative_to(unit_dir).as_posix(),
            "exists": dst.exists(),
            "original_independent_exists": original_dst.exists(),
            "encoding": "H.264 video + silent AAC audio, yuv420p, faststart, metadata stripped",
            "reference_material_rule": "short_under_2s_packaged_separately; no adjacent shots spliced",
            "short_material_handling": "optional same-shot last-frame hold to satisfy 2s upload floor",
            "original_independent_duration_seconds": original_info.get("output_duration_seconds"),
            "original_encoding_note": "source split clips were MP4 container with mpeg4/mp4v video and no audio",
            **transcode_info,
        }

    dst = unit_dir / "01_reference_clip" / f"{src.stem}_upload_h264_aac.mp4"
    transcode_info = transcode_reference_clip(src, dst, pad_short_to_min=False)
    result = {
        "source": ref,
        "local": dst.relative_to(unit_dir).as_posix(),
        "exists": dst.exists(),
        "encoding": "H.264 video + silent AAC audio, yuv420p, faststart, metadata stripped",
        "reference_material_rule": "regular_upload_only_if_original_independent_reference_is_2s_or_longer",
        "original_encoding_note": "source split clips were MP4 container with mpeg4/mp4v video and no audio",
        **transcode_info,
    }
    return result


def anchor_sort_key(anchor: dict[str, Any]) -> tuple[float, str]:
    return (parse_timecode(anchor.get("timecode")), anchor.get("item_id") or "")


def anchor_row(anchor: dict[str, Any], dst: Path, unit_dir: Path) -> dict[str, Any]:
    source_rel = anchor.get("packaged_path") or anchor.get("source_path")
    return {
        "kind": anchor.get("kind", "anchor"),
        "id": anchor.get("item_id", ""),
        "timecode": anchor.get("timecode", ""),
        "role": anchor.get("role", ""),
        "source": source_rel,
        "local": dst.relative_to(unit_dir).as_posix(),
        "exists": dst.exists(),
    }


def copy_ordered_anchors(
    unit_manifest: dict[str, Any],
    unit_dir: Path,
    upload_official_keyframes: bool,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    upload_rows = []
    official_reference_rows = []
    anchors = sorted(unit_manifest.get("ordered_generated_anchors", []), key=anchor_sort_key)
    upload_index = 1
    official_reference_index = 1
    for anchor in anchors:
        source_rel = anchor.get("packaged_path") or anchor.get("source_path")
        if not source_rel:
            continue
        src = PROJECT_ROOT / source_rel
        suffix = src.suffix or ".png"
        kind = anchor.get("kind", "anchor")
        item_id = anchor.get("item_id", f"anchor_{upload_index:02d}")
        is_official = kind == "official_keyframe"
        if is_official and not upload_official_keyframes:
            dst = (
                unit_dir
                / "06_official_original_keyframes_reference_only"
                / f"{official_reference_index:02d}_{kind}_{item_id}{suffix}"
            )
            official_reference_index += 1
            materialize(src, dst)
            row = anchor_row(anchor, dst, unit_dir)
            row["r8_status"] = "reference_only_not_for_default_upload"
            official_reference_rows.append(row)
            continue
        kind = anchor.get("kind", "anchor")
        dst = unit_dir / "02_keyframes_for_upload" / f"{upload_index:02d}_{kind}_{item_id}{suffix}"
        upload_index += 1
        materialize(src, dst)
        upload_rows.append(anchor_row(anchor, dst, unit_dir))
    return upload_rows, official_reference_rows


def copy_r7_candidates(candidates: list[dict[str, Any]], unit_dir: Path, start_index: int) -> list[dict[str, Any]]:
    rows = []
    for offset, item in enumerate(candidates, start_index):
        generated_rel = item.get("_generated_path")
        if not generated_rel:
            continue
        src = PROJECT_ROOT / generated_rel
        suffix = src.suffix or ".png"
        asset_id = item.get("asset_id", f"r7_{offset:02d}")
        role = item.get("role", "")
        dst = unit_dir / "02_keyframes_for_upload" / f"{offset:02d}_r7_generated_{asset_id}{suffix}"
        materialize(src, dst)
        rows.append(
            {
                "kind": "r7_generated_candidate",
                "id": asset_id,
                "timecode": item.get("source_timecode", ""),
                "role": role,
                "priority": item.get("priority", ""),
                "status": item.get("status", ""),
                "source": generated_rel,
                "local": dst.relative_to(unit_dir).as_posix(),
                "exists": dst.exists(),
                "difference_reason": item.get("difference_reason", ""),
            }
        )
    return rows


def copy_r7_reference_only(candidates: list[dict[str, Any]], unit_dir: Path) -> list[dict[str, Any]]:
    rows = []
    for index, item in enumerate(candidates, 1):
        generated_rel = item.get("_generated_path")
        if not generated_rel:
            continue
        src = PROJECT_ROOT / generated_rel
        suffix = src.suffix or ".png"
        asset_id = item.get("asset_id", f"r7_{index:02d}")
        dst = unit_dir / "05_r7_generated_candidates_reference_only" / f"{index:02d}_{asset_id}{suffix}"
        materialize(src, dst)
        rows.append(
            {
                "kind": "r7_generated_candidate_reference_only",
                "id": asset_id,
                "timecode": item.get("source_timecode", ""),
                "role": item.get("role", ""),
                "priority": item.get("priority", ""),
                "source": generated_rel,
                "local": dst.relative_to(unit_dir).as_posix(),
                "exists": dst.exists(),
                "r8_status": "reference_only_pending_director_reapproval",
            }
        )
    return rows


def copy_source_reference_frames(candidates: list[dict[str, Any]], unit_dir: Path) -> list[dict[str, Any]]:
    rows = []
    for index, item in enumerate(candidates, 1):
        source_rel = item.get("reference_frame_path")
        if not source_rel:
            continue
        src = PROJECT_ROOT / source_rel
        suffix = src.suffix or ".jpg"
        asset_id = item.get("asset_id", f"source_{index:02d}")
        dst = unit_dir / "04_source_reference_frames_audit_only" / f"{index:02d}_{asset_id}{suffix}"
        materialize(src, dst)
        rows.append(
            {
                "id": asset_id,
                "timecode": item.get("source_timecode", ""),
                "role": item.get("role", ""),
                "source": source_rel,
                "local": dst.relative_to(unit_dir).as_posix(),
                "exists": dst.exists(),
            }
        )
    return rows


def copy_locks(unit_manifest: dict[str, Any], unit_dir: Path) -> list[dict[str, Any]]:
    rows = []
    for index, lock in enumerate(unit_manifest.get("active_asset_locks", []), 1):
        source_rel = lock.get("global_lock_path") or lock.get("source_path")
        if not source_rel:
            continue
        src = PROJECT_ROOT / source_rel
        suffix = src.suffix or ".png"
        asset_id = lock.get("asset_id", f"lock_{index:02d}")
        group = lock.get("group", "asset_lock")
        dst = unit_dir / "03_asset_locks_for_upload" / f"{index:02d}_{group}_{asset_id}{suffix}"
        materialize(src, dst)
        rows.append(
            {
                "group": group,
                "id": asset_id,
                "status": lock.get("status", ""),
                "source": source_rel,
                "local": dst.relative_to(unit_dir).as_posix(),
                "exists": dst.exists(),
            }
        )
    return rows


def write_prompt(
    unit_manifest: dict[str, Any],
    unit_dir: Path,
    reference_clip: dict[str, Any],
    keyframes: list[dict[str, Any]],
    locks: list[dict[str, Any]],
    source_frames: list[dict[str, Any]],
    r7_reference_only: list[dict[str, Any]],
    official_reference_only: list[dict[str, Any]],
    lean_approved: bool,
) -> str:
    unit = unit_manifest["unit"]
    expected_output = unit_manifest.get("expected_video_output_path", "")
    prompt_path = unit_dir / "AIGC_PROMPT.md"
    lines = [
        f"# {unit['order']:02d} - {unit['unit_id']} - {unit['title']}",
        "",
        "- Status: organized input folder; visual quality is not yet re-approved."
        if not lean_approved
        else "- Status: lean QA-recovery input folder; R7 candidates are reference-only.",
        f"- Time range: `{unit_time_range(unit)}`",
        f"- Shot intent: {unit.get('intent', '')}",
        "",
        "## Upload These",
        "",
        f"1. Reference video: `{reference_clip['local']}` (upload-compatible H.264/AAC MP4)",
        "2. Keyframes/images in `02_keyframes_for_upload/`.",
        "3. Asset locks in `03_asset_locks_for_upload/`, if any.",
        "4. This prompt document.",
        "",
    ]
    if reference_clip.get("original_independent_local"):
        lines += [
            "Short reference material note: this unit is under 2 seconds in the source timeline and is packaged separately.",
            f"- Original independent clip: `{reference_clip['original_independent_local']}`",
            f"- Optional upload workaround: `{reference_clip['local']}`",
            "- The optional workaround only holds this same shot's last frame; it does not splice neighboring shots.",
            "- Preserve the original shot content and do not merge this unit with adjacent units.",
            "",
        ]
    lines += [
        "## Keyframes / Images For Upload",
        "",
    ]
    if keyframes:
        lines += ["| # | Kind | ID | Time | Role | Local file |", "|---:|---|---|---:|---|---|"]
        for index, row in enumerate(keyframes, 1):
            lines.append(
                f"| {index} | `{row['kind']}` | `{row['id']}` | {row.get('timecode', '')} | "
                f"{row.get('role', '')} | `{row['local']}` |"
            )
    else:
        lines.append(
            "No target-style keyframe is approved for default upload in this unit. Use the reference clip, asset locks, and prompt; do not substitute original-style frames as visual style anchors."
        )

    lines += ["", "## Asset Locks", ""]
    if locks:
        for row in locks:
            lines.append(f"- `{row['id']}` ({row.get('status', '')}): `{row['local']}`")
    else:
        lines.append("- none")

    if r7_reference_only:
        lines += [
            "",
            "## R7 Generated Candidates, Reference Only",
            "",
            "These images are included for review/reference only and are not part of the default upload image set for this lean package.",
            "",
            "| ID | Time | Role | Local file |",
            "|---|---:|---|---|",
        ]
        for row in r7_reference_only:
            lines.append(f"| `{row['id']}` | {row.get('timecode', '')} | {row.get('role', '')} | `{row['local']}` |")

    if official_reference_only:
        lines += [
            "",
            "## Official Original Keyframes, Reference Only",
            "",
            "These original-style frames are included for timing/composition audit only. Do not upload them as target-style keyframes unless the director explicitly asks for that specific unit.",
            "",
            "| ID | Time | Role | Local file |",
            "|---|---:|---|---|",
        ]
        for row in official_reference_only:
            lines.append(f"| `{row['id']}` | {row.get('timecode', '')} | {row.get('role', '')} | `{row['local']}` |")

    lines += [
        "",
        "## Source Reference Frames",
        "",
        "These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.",
        "",
        "| ID | Time | Role | Local file |",
        "|---|---:|---|---|",
    ]
    for row in source_frames:
        lines.append(f"| `{row['id']}` | {row.get('timecode', '')} | {row.get('role', '')} | `{row['local']}` |")

    lines += [
        "",
        "## Save Result To",
        "",
        f"`{expected_output}`",
        "",
        "## Prompt To Use",
        "",
        f"Generate a clean live-action remake segment for `{unit['unit_id']}`.",
        f"Time range: `{unit_time_range(unit)}`.",
        "",
        "Use the reference video clip as the primary source for timing, camera movement,",
        "screen direction, shot duration, and edit rhythm. Use the listed keyframes/images",
        "as visual anchors for identity, props, vehicles, scene geometry, palette, and",
        "continuity. Preserve active asset locks exactly when visible.",
        "Shot content integrity has higher priority than the 2-second upload constraint:",
        "do not merge, splice, or borrow content from neighboring shots to satisfy duration.",
        "",
        f"Shot intent: {unit.get('intent', '')}",
        "",
        "No readable original title, credit, lyric, subtitle, broadcaster mark, logo,",
        "watermark, or random glyph. Keep minors age-appropriate and non-sexualized.",
        "Do not merge neighboring flashes or montage beats into a false single take.",
        "",
        "QA note: this folder is an organized material handoff. Some generated images may",
        "still need director review or replacement before final production approval.",
        "",
    ]
    if lean_approved:
        lines += [
            "Lean package note: R7 generated candidates are deliberately excluded from the",
            "default image upload set after the 161-frame R7 preview failed director QA.",
            "Only re-add an R7 image after director approval for this specific unit.",
            "",
        ]
    prompt_path.write_text("\n".join(lines), encoding="utf-8")
    return prompt_path.relative_to(unit_dir).as_posix()


def write_unit_readme(unit_manifest: dict[str, Any], unit_dir: Path, manifest: dict[str, Any]) -> None:
    unit = unit_manifest["unit"]
    lines = [
        f"# {unit['order']:02d} - {unit['unit_id']}",
        "",
        f"- Title: {unit['title']}",
        f"- Time range: `{unit_time_range(unit)}`",
        f"- Reference clip: `{manifest['reference_clip']['local']}`",
        f"- Original independent reference clip: `{manifest['reference_clip'].get('original_independent_local', 'same as reference clip')}`",
        f"- Prompt: `{manifest['prompt_doc']}`",
        f"- Keyframes/images for upload: {len(manifest['keyframes_for_upload'])}",
        f"- Asset locks: {len(manifest['asset_locks_for_upload'])}",
        f"- Source reference frames, audit only: {len(manifest['source_reference_frames_audit_only'])}",
        f"- R7 generated candidates, reference only: {len(manifest.get('r7_generated_candidates_reference_only', []))}",
        f"- Official original keyframes, reference only: {len(manifest.get('official_original_keyframes_reference_only', []))}",
        "",
        "Folder order:",
        "",
        "- `01_reference_clip/`: split reference video for this segment.",
        "- `00_original_independent_reference_clip/`: original-duration independent clip, present only for short-material units.",
        "- `01_reference_clip_same_shot_hold_min2s_optional/`: optional same-shot hold version, present only for short-material units.",
        "- `02_keyframes_for_upload/`: ordered target-style generated keyframe inputs only in lean packages.",
        "- `03_asset_locks_for_upload/`: identity/prop/scene locks for this segment.",
        "- `04_source_reference_frames_audit_only/`: original-video screenshots for audit only.",
        "- `05_r7_generated_candidates_reference_only/`: R7 generated images held out of the default upload set.",
        "- `06_official_original_keyframes_reference_only/`: official/original keyframes held out of the default upload set.",
        "- `AIGC_PROMPT.md`: this segment's AIGC video prompt and upload checklist.",
        "",
    ]
    (unit_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def build(
    clean: bool,
    output_root: Path,
    include_r7_upload: bool,
    units_override: list[dict[str, Any]] | None = None,
    short_material_package: bool = False,
    package_title: str | None = None,
) -> dict[str, Any]:
    now = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).isoformat(timespec="seconds")
    ensure_clean_dir(output_root, clean=clean)
    units = units_override if units_override is not None else load_units()
    candidates_by_unit = load_candidates_by_unit()
    unit_rows = []
    missing = []

    for unit_manifest in units:
        unit = unit_manifest["unit"]
        unit_id = unit["unit_id"]
        folder = output_root / safe_name(unit["order"], unit_id)
        ensure_clean_dir(folder, clean=clean)
        candidates = candidates_by_unit.get(unit_id, [])

        reference_clip = copy_reference_clip(unit_manifest, folder, short_material_package=short_material_package)
        ordered, official_reference_only = copy_ordered_anchors(
            unit_manifest,
            folder,
            upload_official_keyframes=include_r7_upload,
        )
        r7 = copy_r7_candidates(candidates, folder, start_index=len(ordered) + 1) if include_r7_upload else []
        r7_reference_only = copy_r7_reference_only(candidates, folder) if not include_r7_upload else []
        locks = copy_locks(unit_manifest, folder)
        source_frames = copy_source_reference_frames(candidates, folder)
        keyframes = ordered + r7
        prompt_doc = write_prompt(
            unit_manifest,
            folder,
            reference_clip,
            keyframes,
            locks,
            source_frames,
            r7_reference_only,
            official_reference_only,
            lean_approved=not include_r7_upload,
        )

        manifest = {
            "created_at": now,
            "status": "organized_input_folder_pending_visual_qa"
            if include_r7_upload
            else (
                "lean_short_under2s_reference_material_folder_pending_special_handling"
                if short_material_package
                else "lean_input_folder_r7_reference_only_pending_visual_qa"
            ),
            "unit": unit,
            "source_unit_manifest": rel(unit_manifest["_manifest_path"]),
            "reference_clip": reference_clip,
            "prompt_doc": prompt_doc,
            "keyframes_for_upload": keyframes,
            "asset_locks_for_upload": locks,
            "source_reference_frames_audit_only": source_frames,
            "r7_generated_candidates_reference_only": r7_reference_only,
            "official_original_keyframes_reference_only": official_reference_only,
            "expected_video_output_path": unit_manifest.get("expected_video_output_path", ""),
        }
        write_unit_readme(unit_manifest, folder, manifest)
        (folder / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        for section in [
            "reference_clip",
            "keyframes_for_upload",
            "asset_locks_for_upload",
            "source_reference_frames_audit_only",
            "r7_generated_candidates_reference_only",
            "official_original_keyframes_reference_only",
        ]:
            value = manifest[section]
            if isinstance(value, dict):
                rows = [value]
            else:
                rows = value
            for row in rows:
                if not row.get("exists"):
                    missing.append({"unit_id": unit_id, "section": section, "path": row.get("source")})

        unit_rows.append(
            {
                "order": unit["order"],
                "unit_id": unit_id,
                "title": unit["title"],
                "time_range": unit_time_range(unit),
                "folder": folder.relative_to(output_root).as_posix(),
                "reference_clip": reference_clip["local"],
                "original_independent_reference_clip": reference_clip.get("original_independent_local", ""),
                "source_duration_seconds": reference_clip.get("source_duration_seconds"),
                "output_duration_seconds": reference_clip.get("output_duration_seconds"),
                "padded_last_frame_seconds": reference_clip.get("padded_last_frame_seconds", 0),
                "is_short_reference_material": is_short_reference_material(unit_manifest),
                "prompt_doc": prompt_doc,
                "keyframe_count": len(keyframes),
                "asset_lock_count": len(locks),
                "source_reference_frame_count": len(source_frames),
                "r7_reference_only_count": len(r7_reference_only),
                "official_reference_only_count": len(official_reference_only),
                "expected_video_output_path": unit_manifest.get("expected_video_output_path", ""),
            }
        )

    package_manifest = {
        "created_at": now,
        "status": (
            "organized_input_folders_pending_visual_qa"
            if include_r7_upload
            else (
                "lean_short_under2s_reference_materials_pending_special_handling"
                if short_material_package
                else "lean_regular_reference_materials_min2s_ready_for_upload"
            )
        )
        if not missing
        else "missing_files",
        "package_root": rel(output_root),
        "include_r7_candidates_as_upload_images": include_r7_upload,
        "short_reference_material_package": short_material_package,
        "reference_material_policy": (
            "short materials are separated; optional min2s files use same-shot last-frame hold only"
            if short_material_package
            else "regular package contains only original independent reference materials that are 2s or longer"
        ),
        "unit_count": len(unit_rows),
        "short_reference_material_count": sum(1 for row in unit_rows if row["is_short_reference_material"]),
        "reference_clip_count": len(unit_rows),
        "prompt_doc_count": len(unit_rows),
        "keyframe_image_count": sum(row["keyframe_count"] for row in unit_rows),
        "asset_lock_image_count": sum(row["asset_lock_count"] for row in unit_rows),
        "source_reference_frame_count": sum(row["source_reference_frame_count"] for row in unit_rows),
        "r7_reference_only_image_count": sum(row["r7_reference_only_count"] for row in unit_rows),
        "official_original_keyframe_reference_only_count": sum(
            row["official_reference_only_count"] for row in unit_rows
        ),
        "missing_count": len(missing),
        "missing": missing,
        "units": unit_rows,
    }
    (output_root / "PACKAGE_MANIFEST.json").write_text(
        json.dumps(package_manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    lines = [
        package_title
        or (
            "# Reference-003 R7 AIGC Video Segment Input Folders"
            if include_r7_upload
            else "# Reference-003 R8 Lean AIGC Video Segment Input Folders"
        ),
        "",
        f"- Created: {now}",
        f"- Status: `{package_manifest['status']}`",
        f"- Unit folders: {len(unit_rows)}",
        f"- Short reference materials under 2s: {package_manifest['short_reference_material_count']}",
        f"- Reference clips: {package_manifest['reference_clip_count']}",
        f"- Prompt docs: {package_manifest['prompt_doc_count']}",
        f"- Keyframe/image inputs: {package_manifest['keyframe_image_count']}",
        f"- Asset lock images: {package_manifest['asset_lock_image_count']}",
        f"- Source reference frames, audit only: {package_manifest['source_reference_frame_count']}",
        f"- R7 generated candidates, reference only: {package_manifest['r7_reference_only_image_count']}",
        f"- Official original keyframes, reference only: {package_manifest['official_original_keyframe_reference_only_count']}",
        f"- Missing files: {package_manifest['missing_count']}",
        "",
        "## Important QA Boundary",
        "",
        "This package is organized first, per director request. It does not mean every generated image is visually approved.",
        "Use it as a clean folder handoff, then continue visual QA and repair decisions."
        if include_r7_upload
        else (
            "Short reference materials are packaged separately. Shot content integrity is higher priority than the 2-second upload constraint: do not merge, splice, or borrow neighboring shots."
            if short_material_package
            else "This regular package excludes source-independent reference clips shorter than 2 seconds. R7 generated candidates and official/original keyframes are held as reference-only."
        ),
        "",
        "## Folders",
        "",
        "| # | Unit | Time | Source seconds | Folder | Upload keyframes | Locks | R7 ref-only | Official ref-only | Prompt |",
        "|---:|---|---:|---:|---|---:|---:|---:|---:|---|",
    ]
    for row in unit_rows:
        lines.append(
            f"| {row['order']} | `{row['unit_id']}` | {row['time_range']} | "
            f"{fmt_seconds(row['source_duration_seconds'])} | "
            f"`{row['folder']}` | {row['keyframe_count']} | {row['asset_lock_count']} | "
            f"{row['r7_reference_only_count']} | {row['official_reference_only_count']} | `{row['prompt_doc']}` |"
        )
    lines.append("")
    (output_root / "README.md").write_text("\n".join(lines), encoding="utf-8")

    return package_manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-clean", action="store_true", help="Do not remove existing package folder before rebuilding.")
    parser.add_argument(
        "--lean-approved",
        action="store_true",
        help="Build R8 lean folders: exclude R7 generated candidates from upload images and keep them reference-only.",
    )
    parser.add_argument(
        "--split-min2s",
        action="store_true",
        help="Build two lean packages: regular >=2s reference materials and separate <2s short materials.",
    )
    args = parser.parse_args()
    if args.split_min2s:
        all_units = load_units()
        regular_units = [unit for unit in all_units if not is_short_reference_material(unit)]
        short_units = [unit for unit in all_units if is_short_reference_material(unit)]
        regular = build(
            clean=not args.no_clean,
            output_root=REGULAR_MIN2S_OUTPUT_ROOT,
            include_r7_upload=False,
            units_override=regular_units,
            short_material_package=False,
            package_title="# Reference-003 R8 Lean Regular Reference Materials Min2s",
        )
        short = build(
            clean=not args.no_clean,
            output_root=SHORT_UNDER2S_OUTPUT_ROOT,
            include_r7_upload=False,
            units_override=short_units,
            short_material_package=True,
            package_title="# Reference-003 R8 Lean Short Reference Materials Under 2s",
        )
        print(json.dumps({
            "regular_package_root": regular["package_root"],
            "regular_unit_count": regular["unit_count"],
            "regular_short_reference_material_count": regular["short_reference_material_count"],
            "short_package_root": short["package_root"],
            "short_unit_count": short["unit_count"],
            "short_reference_material_count": short["short_reference_material_count"],
            "missing_count": regular["missing_count"] + short["missing_count"],
        }, ensure_ascii=False, indent=2))
        return
    result = build(
        clean=not args.no_clean,
        output_root=LEAN_OUTPUT_ROOT if args.lean_approved else OUTPUT_ROOT,
        include_r7_upload=not args.lean_approved,
    )
    print(json.dumps({k: result[k] for k in [
        "status",
        "package_root",
        "include_r7_candidates_as_upload_images",
        "unit_count",
        "reference_clip_count",
        "prompt_doc_count",
        "keyframe_image_count",
        "asset_lock_image_count",
        "source_reference_frame_count",
        "r7_reference_only_image_count",
        "official_original_keyframe_reference_only_count",
        "missing_count",
    ]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
