#!/usr/bin/env python3
"""Assemble final MV from returned external image-to-video clips.

Expected inputs:
  09_edit/external_clips/external_i2v_clips_v1/VP001_KF001_external_i2v.mp4
  ...
  09_edit/external_clips/external_i2v_clips_v1/VP014_KF014_external_i2v.mp4
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import subprocess
import zipfile
from datetime import datetime
from pathlib import Path


ROOT = Path("/Users/jaychoupp/Story/Film/projects/county-wkw-night-market-mv")
FFMPEG = Path("/Users/jaychoupp/Library/Application Support/bilibili/ffmpeg/ffmpeg")
CLIP_DIR = ROOT / "09_edit/external_clips/external_i2v_clips_v1"
OUT_DIR = ROOT / "11_delivery/final_external_mv_v1"
PACKAGE_DIR = ROOT / "11_delivery/packages/final_external_mv_v1"
MUSIC = ROOT / "09_edit/animatics/moving_preview_v1/scratch_music_v1_original.wav"

ITEMS = [
    ("VP001", "KF001"),
    ("VP002", "KF002"),
    ("VP003", "KF003"),
    ("VP004", "KF004"),
    ("VP005", "KF005"),
    ("VP006", "KF006"),
    ("VP007", "KF007"),
    ("VP008", "KF008"),
    ("VP009", "KF009"),
    ("VP010", "KF010"),
    ("VP011", "KF011"),
    ("VP012", "KF012"),
    ("VP013", "KF013"),
    ("VP014", "KF014"),
]


def expected_path(vp: str, kf: str) -> Path:
    return CLIP_DIR / f"{vp}_{kf}_external_i2v.mp4"


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def probe(path: Path) -> tuple[bool, str]:
    result = run([str(FFMPEG), "-hide_banner", "-i", str(path), "-f", "null", "-"])
    text = (result.stderr or "") + (result.stdout or "")
    return result.returncode == 0, text


def check_inputs() -> tuple[list[Path], list[str]]:
    clips = []
    issues = []
    for vp, kf in ITEMS:
        path = expected_path(vp, kf)
        if not path.exists():
            issues.append(f"missing {path.relative_to(ROOT)}")
            continue
        ok, info = probe(path)
        if not ok:
            issues.append(f"unreadable {path.relative_to(ROOT)}")
        if "Audio:" not in info:
            issues.append(f"no_audio_stream {path.relative_to(ROOT)}")
        clips.append(path)
    return clips, issues


def write_tracking(clips: list[Path], issues: list[str]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with (OUT_DIR / "external_clip_check.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["vp_id", "kf_id", "expected_clip", "exists", "status"])
        issues_text = "\n".join(issues)
        for vp, kf in ITEMS:
            path = expected_path(vp, kf)
            status = "missing"
            if path.exists():
                status = "issue" if str(path.relative_to(ROOT)) in issues_text else "ready"
            writer.writerow([vp, kf, str(path.relative_to(ROOT)), path.exists(), status])


def concat_clips(clips: list[Path]) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    concat = OUT_DIR / "external_concat.txt"
    with concat.open("w", encoding="utf-8") as f:
        for clip in clips:
            f.write(f"file '{clip}'\n")
    ambience = OUT_DIR / "county_wkw_external_mv_v1_ambience_only.mp4"
    cmd = [
        str(FFMPEG),
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(concat),
        "-c",
        "copy",
        str(ambience),
    ]
    subprocess.run(cmd, check=True)
    return ambience


def mix_music(ambience: Path) -> Path:
    final = OUT_DIR / "county_wkw_external_mv_v1_with_scratch_music.mp4"
    cmd = [
        str(FFMPEG),
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(ambience),
        "-i",
        str(MUSIC),
        "-filter_complex",
        "[0:a]volume=0.55[a0];[1:a]volume=0.75[a1];[a0][a1]amix=inputs=2:duration=shortest:dropout_transition=0[a]",
        "-map",
        "0:v:0",
        "-map",
        "[a]",
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-shortest",
        "-movflags",
        "+faststart",
        str(final),
    ]
    subprocess.run(cmd, check=True)
    return final


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_final_docs(clips: list[Path], ambience: Path, final: Path) -> list[Path]:
    manifest = OUT_DIR / "MANIFEST.md"
    qa = OUT_DIR / "QA.md"
    checksums = OUT_DIR / "checksums_sha256.csv"
    generated_at = datetime.now().isoformat(timespec="seconds")

    manifest.write_text(
        f"""# Final External MV V1 Manifest

Project: `county-wkw-night-market-mv`
Generated: {generated_at}
Source clips: 14 returned external image-to-video clips

## Main Files

- Ambience-only external MV: `{ambience.name}`
- External MV with scratch music: `{final.name}`
- Clip intake check: `external_clip_check.csv`
- QA: `QA.md`
- Checksums: `checksums_sha256.csv`

## Audio Rule

Each returned image-to-video clip is expected to contain ambience / sound effects only, with no music, no BGM, and no soundtrack. Scratch music is mixed only in the final edit file.

## Source Package

The upload source is `11_delivery/packages/external_i2v_upload_v1/county_wkw_external_i2v_upload_v1.zip`.
""",
        encoding="utf-8",
    )

    qa.write_text(
        f"""# Final External MV V1 QA

Project: `county-wkw-night-market-mv`
QA time: {generated_at}

## Input Check

- Expected external clips: 14
- Clips present and probed: {len(clips)}
- Missing clips at assembly time: 0
- Assembly source order: VP001-KF001 through VP014-KF014

## Output Check

- Ambience-only file exists: {ambience.exists()}
- Scratch-music file exists: {final.exists()}
- Ambience-only bytes: {ambience.stat().st_size if ambience.exists() else 0}
- Scratch-music bytes: {final.stat().st_size if final.exists() else 0}

## Notes

This QA only proves file presence, readability of source clips during intake, and successful assembly/mix. Director review is still required for motion quality, identity continuity, and final music choice.
""",
        encoding="utf-8",
    )

    checksum_targets = [
        ambience,
        final,
        OUT_DIR / "external_clip_check.csv",
        manifest,
        qa,
    ]
    with checksums.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["path", "sha256", "bytes"])
        for path in checksum_targets:
            writer.writerow([path.relative_to(ROOT), sha256(path), path.stat().st_size])

    return [manifest, qa, checksums]


def package_final_external(ambience: Path, final: Path, docs: list[Path]) -> Path:
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    package = PACKAGE_DIR / "county_wkw_final_external_mv_v1.zip"
    members = [
        ambience,
        final,
        OUT_DIR / "external_clip_check.csv",
        OUT_DIR / "external_concat.txt",
        *docs,
    ]
    with zipfile.ZipFile(package, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in members:
            archive.write(path, arcname=str(path.relative_to(ROOT)))
    return package


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()

    clips, issues = check_inputs()
    write_tracking(clips, issues)
    if issues:
        print("external_clip_status=incomplete")
        for issue in issues:
            print(issue)
        return 2
    print("external_clip_status=ready")
    if args.check_only:
        return 0
    ambience = concat_clips(clips)
    final = mix_music(ambience)
    docs = write_final_docs(clips, ambience, final)
    package = package_final_external(ambience, final, docs)
    print(f"ambience_only={ambience}")
    print(f"with_scratch_music={final}")
    print(f"package={package}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
