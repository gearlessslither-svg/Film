#!/usr/bin/env python3
"""Validate completion state for county-wkw-night-market-mv.

This script is intentionally local-only. It checks the project files that make
the MV package reviewable, then writes compact CSV/JSON audit outputs.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
import zipfile
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "10_qa/completion_state_v1.json"
OUT_CSV = ROOT / "10_qa/completion_state_v1.csv"

ITEMS = [f"VP{i:03d}_KF{i:03d}" for i in range(1, 15)]


@dataclass
class Check:
    category: str
    name: str
    expected: str
    observed: str
    status: str
    details: str = ""


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def add(checks: list[Check], category: str, name: str, expected: str, observed: str, status: str, details: str = "") -> None:
    checks.append(Check(category, name, expected, observed, status, details))


def count_files(path: Path, pattern: str) -> int:
    return len(sorted(path.glob(pattern))) if path.exists() else 0


def check_required_files(checks: list[Check]) -> None:
    files = [
        "README.md",
        "01_intake/PROJECT_BRIEF.md",
        "02_direction/TOPIC_SELECTION_GATE.md",
        "03_story/outlines/STORY_SPINE.md",
        "04_lookdev/STYLE_BIBLE.md",
        "04_lookdev/LOOKDEV_MOOD_FRAMES_V1.md",
        "07_shots/SHOT_PLAN_DIRECTOR_SEMANTIC_V1.md",
        "07_shots/KEYFRAME_QUEUE_V1.md",
        "08_generation/jobs/video_prompts_v1/PROMPTS.md",
        "09_edit/EDIT_GUIDE_V1.md",
        "10_qa/PROJECT_COMPLETION_AUDIT_V1.md",
        "00_admin/handoff/HANDOFF_LATEST.md",
        "11_delivery/final_decision_gate_v1/FINAL_DECISION_GATE.md",
        "11_delivery/final_decision_gate_v1/PROXY_FINAL_ACCEPTANCE_TEMPLATE.md",
        "11_delivery/final_decision_gate_v1/finalize_proxy_acceptance.py",
    ]
    missing = [name for name in files if not (ROOT / name).exists()]
    add(
        checks,
        "core",
        "required_text_files",
        f"{len(files)} files",
        f"{len(files) - len(missing)} present",
        "pass" if not missing else "fail",
        "; ".join(missing),
    )


def check_asset_counts(checks: list[Check]) -> None:
    targets = [
        ("lookdev_moodframes", "08_generation/jobs/lookdev_moodframes_v1/outputs", "*.png", 8),
        ("hardlock_candidates", "08_generation/jobs/hardlocks_v1/outputs", "*.png", 4),
        ("formal_keyframes", "08_generation/jobs/keyframes_v1/outputs", "*.png", 14),
        ("local_proxy_clips", "09_edit/proxy_clips/local_proxy_clips_v1/outputs", "*.mp4", 14),
        ("local_proxy_ambience_wavs", "09_edit/proxy_clips/local_proxy_clips_v1/audio", "*.wav", 14),
    ]
    for name, folder, pattern, expected in targets:
        observed = count_files(ROOT / folder, pattern)
        add(
            checks,
            "assets",
            name,
            str(expected),
            str(observed),
            "pass" if observed == expected else "fail",
            folder,
        )


def check_prompts(checks: list[Check]) -> None:
    prompt_path = ROOT / "08_generation/jobs/video_prompts_v1/PROMPTS.md"
    text = prompt_path.read_text(encoding="utf-8") if prompt_path.exists() else ""
    sections = re.findall(r"^## VP\d{3}\b", text, flags=re.MULTILINE)
    cn = text.count("中文视频提示词")
    en = text.count("English video prompt")
    source_refs = re.findall(r"Source: `08_generation/jobs/keyframes_v1/outputs/KF\d{3}_[^`]+\.png`", text)

    split_sections = re.split(r"^## VP\d{3}\b.*$", text, flags=re.MULTILINE)[1:]
    audio_ok = 0
    for section in split_sections:
        lower = section.lower()
        if "不要音乐" in section and "no music" in lower and "no bgm" in lower and "no soundtrack" in lower:
            audio_ok += 1

    status = "pass" if (len(sections), cn, en, len(source_refs), audio_ok) == (14, 14, 14, 14, 14) else "fail"
    add(
        checks,
        "prompts",
        "bilingual_video_prompts_and_audio_rule",
        "14 VP sections, CN/EN prompts, source refs, no-music rule",
        f"sections={len(sections)}, cn={cn}, en={en}, sources={len(source_refs)}, audio_rule={audio_ok}",
        status,
        rel(prompt_path),
    )


def check_video_outputs(checks: list[Check]) -> None:
    files = [
        "09_edit/animatics/static_animatic_v1/county_wkw_static_animatic_v1_silent.mp4",
        "09_edit/animatics/moving_preview_v1/county_wkw_moving_preview_v1_with_scratch_music.mp4",
        "09_edit/animatics/moving_preview_v1/scratch_music_v1_original.wav",
        "11_delivery/final_proxy_mv_v1/county_wkw_proxy_mv_v1_ambience_only.mp4",
        "11_delivery/final_proxy_mv_v1/county_wkw_proxy_mv_v1_with_scratch_music.mp4",
        "11_delivery/final_proxy_candidate_v1/poster_frame_v1.png",
    ]
    missing = [name for name in files if not (ROOT / name).exists()]
    add(
        checks,
        "video",
        "required_local_video_outputs",
        f"{len(files)} files",
        f"{len(files) - len(missing)} present",
        "pass" if not missing else "fail",
        "; ".join(missing),
    )


def check_zip_packages(checks: list[Check]) -> None:
    packages = [
        "11_delivery/packages/static_review_v1/county_wkw_static_review_v1.zip",
        "11_delivery/packages/moving_preview_v1/county_wkw_moving_preview_v1.zip",
        "11_delivery/packages/proxy_mv_v1/county_wkw_proxy_mv_v1.zip",
        "11_delivery/packages/external_i2v_upload_v1/county_wkw_external_i2v_upload_v1.zip",
        "11_delivery/packages/final_proxy_candidate_v1/county_wkw_final_proxy_candidate_v1.zip",
        "11_delivery/packages/final_decision_gate_v1/county_wkw_final_decision_gate_v1.zip",
    ]
    issues = []
    for name in packages:
        path = ROOT / name
        if not path.exists():
            issues.append(f"missing {name}")
            continue
        try:
            with zipfile.ZipFile(path) as archive:
                bad = archive.testzip()
            if bad:
                issues.append(f"bad member {name}:{bad}")
        except zipfile.BadZipFile:
            issues.append(f"bad zip {name}")
    add(
        checks,
        "packages",
        "zip_integrity",
        f"{len(packages)} valid zip packages",
        f"{len(packages) - len(issues)} ok",
        "pass" if not issues else "fail",
        "; ".join(issues),
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check_candidate_checksums(checks: list[Check]) -> None:
    csv_path = ROOT / "11_delivery/final_proxy_candidate_v1/checksums_sha256.csv"
    if not csv_path.exists():
        add(checks, "packages", "final_proxy_candidate_checksums", "checksum csv", "missing", "fail")
        return

    issues = []
    rows = 0
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            rows += 1
            path = ROOT / row["path"]
            if not path.exists():
                issues.append(f"missing {row['path']}")
                continue
            actual_bytes = path.stat().st_size
            actual_hash = sha256(path)
            if str(actual_bytes) != row["bytes"] or actual_hash != row["sha256"]:
                issues.append(f"mismatch {row['path']}")

    add(
        checks,
        "packages",
        "final_proxy_candidate_checksums",
        "all checksum rows match current files",
        f"{rows} rows checked",
        "pass" if not issues else "fail",
        "; ".join(issues),
    )


def check_external_upload_and_intake(checks: list[Check]) -> None:
    units = ROOT / "11_delivery/packages/external_i2v_upload_v1/units"
    unit_dirs = sorted([path for path in units.glob("VP???_KF???") if path.is_dir()]) if units.exists() else []
    prompt_files = sorted(units.glob("VP???_KF???/VP???_KF???_prompt.md")) if units.exists() else []
    source_frames = sorted(units.glob("VP???_KF???/VP???_KF???_source_keyframe.png")) if units.exists() else []
    upload_status = "pass" if (len(unit_dirs), len(prompt_files), len(source_frames)) == (14, 14, 14) else "fail"
    add(
        checks,
        "external_i2v",
        "upload_units",
        "14 units, 14 prompts, 14 source keyframes",
        f"units={len(unit_dirs)}, prompts={len(prompt_files)}, source_keyframes={len(source_frames)}",
        upload_status,
        rel(units),
    )

    intake = ROOT / "09_edit/external_clips/external_i2v_clips_v1"
    expected = [intake / f"{item}_external_i2v.mp4" for item in ITEMS]
    present = [path for path in expected if path.exists()]
    missing = [rel(path) for path in expected if not path.exists()]
    status = "pass" if len(present) == 14 else "pending"
    add(
        checks,
        "external_i2v",
        "returned_external_clips",
        "14 returned external I2V clips",
        f"{len(present)} present, {len(missing)} missing",
        status,
        "; ".join(missing[:5]) + ("; ..." if len(missing) > 5 else ""),
    )

    final_external = [
        ROOT / "11_delivery/final_external_mv_v1/county_wkw_external_mv_v1_ambience_only.mp4",
        ROOT / "11_delivery/final_external_mv_v1/county_wkw_external_mv_v1_with_scratch_music.mp4",
    ]
    present_final = [path for path in final_external if path.exists()]
    add(
        checks,
        "external_i2v",
        "final_external_mv_outputs",
        "2 assembled external-MV files",
        f"{len(present_final)} present",
        "pass" if len(present_final) == 2 else "pending",
        "; ".join(rel(path) for path in final_external if not path.exists()),
    )

    package = ROOT / "11_delivery/packages/final_external_mv_v1/county_wkw_final_external_mv_v1.zip"
    package_status = "pending"
    package_details = rel(package)
    if len(present_final) == 2:
        if not package.exists():
            package_status = "fail"
            package_details = f"missing {rel(package)}"
        else:
            try:
                with zipfile.ZipFile(package) as archive:
                    bad = archive.testzip()
                package_status = "pass" if bad is None else "fail"
                package_details = "" if bad is None else f"bad member {bad}"
            except zipfile.BadZipFile:
                package_status = "fail"
                package_details = f"bad zip {rel(package)}"
    add(
        checks,
        "external_i2v",
        "final_external_mv_package",
        "assembled final external-MV zip package",
        "present" if package.exists() else "missing",
        package_status,
        package_details,
    )


def check_director_acceptance(checks: list[Check]) -> str:
    note = ROOT / "11_delivery/final_proxy_candidate_v1/DIRECTOR_ACCEPTANCE_NOTE.md"
    text = note.read_text(encoding="utf-8") if note.exists() else ""
    match = re.search(r"^Status:\s*(.+?)\s*$", text, flags=re.MULTILINE | re.IGNORECASE)
    status_text = match.group(1).strip() if match else "unknown"
    accepted = status_text.lower().startswith("accepted")
    add(
        checks,
        "director_gate",
        "proxy_style_acceptance",
        "Status: accepted, if proxy style is final",
        f"Status: {status_text}",
        "pass" if accepted else "pending",
        rel(note),
    )
    return "accepted" if accepted else "pending"


def derive_overall(checks: list[Check], director_status: str) -> dict[str, str]:
    hard_failures = [check for check in checks if check.status == "fail"]
    external_ready = all(
        check.status == "pass"
        for check in checks
        if check.name in {"returned_external_clips", "final_external_mv_outputs", "final_external_mv_package"}
    )
    proxy_ready = not hard_failures and director_status == "accepted"
    package_ready = not hard_failures

    if proxy_ready:
        status = "complete_proxy_final"
        next_action = "Package can be treated as final proxy-style delivery."
    elif external_ready and package_ready:
        status = "complete_external_final"
        next_action = "External image-to-video MV files are assembled and ready for final delivery QA."
    elif hard_failures:
        status = "needs_repair"
        next_action = "Repair failed checks before director acceptance or final delivery."
    else:
        status = "pending_director_or_external_i2v"
        next_action = "Either accept proxy style as final, or return 14 external I2V clips and assemble the final external MV."

    return {
        "overall_status": status,
        "blocking_failures": str(len(hard_failures)),
        "director_acceptance": director_status,
        "next_action": next_action,
    }


def write_outputs(checks: list[Check], summary: dict[str, str]) -> None:
    OUT_JSON.write_text(
        json.dumps(
            {
                "project": "county-wkw-night-market-mv",
                "generated_at": datetime.now().isoformat(timespec="seconds"),
                "summary": summary,
                "checks": [asdict(check) for check in checks],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["category", "name", "expected", "observed", "status", "details"])
        writer.writeheader()
        for check in checks:
            writer.writerow(asdict(check))


def main() -> int:
    checks: list[Check] = []
    check_required_files(checks)
    check_asset_counts(checks)
    check_prompts(checks)
    check_video_outputs(checks)
    check_zip_packages(checks)
    check_candidate_checksums(checks)
    check_external_upload_and_intake(checks)
    director_status = check_director_acceptance(checks)
    summary = derive_overall(checks, director_status)
    write_outputs(checks, summary)

    print(f"overall_status={summary['overall_status']}")
    print(f"blocking_failures={summary['blocking_failures']}")
    print(f"director_acceptance={summary['director_acceptance']}")
    print(f"wrote={rel(OUT_JSON)}")
    print(f"wrote={rel(OUT_CSV)}")
    return 1 if summary["overall_status"] == "needs_repair" else 0


if __name__ == "__main__":
    raise SystemExit(main())
