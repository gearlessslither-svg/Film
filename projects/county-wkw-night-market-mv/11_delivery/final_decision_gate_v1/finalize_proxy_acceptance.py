#!/usr/bin/env python3
"""Finalize the proxy-style delivery after explicit director acceptance.

This script does not make the director decision. It only performs the mechanical
updates after the director has explicitly accepted proxy motion as final.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import zipfile
from datetime import date
from pathlib import Path


ROOT = Path("/Users/jaychoupp/Story/Film/projects/county-wkw-night-market-mv")
ACCEPTANCE_NOTE = ROOT / "11_delivery/final_proxy_candidate_v1/DIRECTOR_ACCEPTANCE_NOTE.md"
AUDIT = ROOT / "10_qa/PROJECT_COMPLETION_AUDIT_V1.md"
HANDOFF_LATEST = ROOT / "00_admin/handoff/HANDOFF_LATEST.md"
HANDOFF_DATED = ROOT / "00_admin/handoff/HANDOFF_2026-07-08.md"
README = ROOT / "README.md"
VALIDATOR = ROOT / "10_qa/validate_completion_state.py"
PROXY_ZIP = ROOT / "11_delivery/packages/final_proxy_candidate_v1/county_wkw_final_proxy_candidate_v1.zip"
DECISION_ZIP = ROOT / "11_delivery/packages/final_decision_gate_v1/county_wkw_final_decision_gate_v1.zip"
CHECKSUMS = ROOT / "11_delivery/final_proxy_candidate_v1/checksums_sha256.csv"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str, dry_run: bool) -> None:
    if dry_run:
        return
    path.write_text(text, encoding="utf-8")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def update_acceptance_note(audio_choice: str, director_note: str, decision_date: str, dry_run: bool) -> None:
    text = f"""# Director Acceptance Note

Project: `county-wkw-night-market-mv`
Candidate: `11_delivery/final_proxy_mv_v1/county_wkw_proxy_mv_v1_with_scratch_music.mp4`

## Current Decision

Status: accepted_proxy_final - {decision_date}

The director explicitly accepts the local proxy motion style as the final visual style for this MV.

Final audio choice: `{audio_choice}`

Director note: {director_note}

## Final Delivery Path

- Main proxy final with scratch music: `11_delivery/final_proxy_mv_v1/county_wkw_proxy_mv_v1_with_scratch_music.mp4`
- Ambience-only proxy final: `11_delivery/final_proxy_mv_v1/county_wkw_proxy_mv_v1_ambience_only.mp4`
- Final proxy candidate package: `11_delivery/packages/final_proxy_candidate_v1/county_wkw_final_proxy_candidate_v1.zip`

## External I2V Status

External image-to-video clips are no longer required for final delivery after this acceptance. The external upload package remains archived as an optional future upgrade path.
"""
    write(ACCEPTANCE_NOTE, text, dry_run)


def ensure_section(text: str, marker: str, section: str) -> str:
    if marker in text:
        before = text.split(marker, 1)[0].rstrip()
        return before + "\n\n" + section.strip() + "\n"
    return text.rstrip() + "\n\n" + section.strip() + "\n"


def update_audit(audio_choice: str, decision_date: str, dry_run: bool) -> None:
    text = read(AUDIT)
    text = text.replace(
        "Current status: static production package, local moving preview, 14 local proxy clips, and local proxy MV complete; final external-AIGC moving MV not complete.",
        "Current status: proxy-style final delivery accepted and packaged; external-AIGC moving MV remains archived as an optional upgrade path.",
    )
    text = text.replace(
        "The project now has the core creative, lookdev, locks, formal keyframes, video prompt package, edit guide, review package, a 75-second silent static animatic, a 75-second local moving preview with original scratch music, 14 ambience-only local proxy clips, a local proxy MV package, a complete external image-to-video upload/intake package, and a final proxy candidate package. It still needs returned external image-to-video clips, or explicit director acceptance of the proxy style, to become final.",
        "The project now has the core creative, lookdev, locks, formal keyframes, video prompt package, edit guide, review package, a 75-second silent static animatic, a 75-second local moving preview with original scratch music, 14 ambience-only local proxy clips, a local proxy MV package, a complete external image-to-video upload/intake package, and an accepted final proxy candidate package.",
    )
    section = f"""## Final Proxy Acceptance

Status: accepted proxy final  
Decision date: {decision_date}  
Final audio choice: `{audio_choice}`

Authoritative evidence:

- `11_delivery/final_proxy_candidate_v1/DIRECTOR_ACCEPTANCE_NOTE.md`
- `11_delivery/packages/final_proxy_candidate_v1/county_wkw_final_proxy_candidate_v1.zip`
- `10_qa/completion_state_v1.json`

External image-to-video clips are not required for the accepted proxy-style final delivery. They remain an optional future upgrade path only.
"""
    text = ensure_section(text, "## Not Yet Complete", section)
    write(AUDIT, text, dry_run)


def update_handoff_file(path: Path, audio_choice: str, decision_date: str, dry_run: bool) -> None:
    text = read(path)
    text = text.replace(
        "最新自检结果：`overall_status=pending_director_or_external_i2v`，`blocking_failures=0`，`director_acceptance=pending`。也就是说项目内部素材、提示词、包完整性、六个 zip 包和校验没有硬失败；最终完成只差导演签收 proxy 风格，或回收 14 段外部图生视频并组装外部 AIGC 正片。",
        f"最新自检结果：proxy 风格已被导演签收为最终交付路径，签收日期 {decision_date}，最终音频选择 `{audio_choice}`。外部图生视频回片不再是最终交付必需项，只作为未来升级路径保留。",
    )
    section = f"""
## Final Proxy Acceptance

- Status: accepted proxy final
- Decision date: {decision_date}
- Final audio choice: `{audio_choice}`
- Acceptance note: `11_delivery/final_proxy_candidate_v1/DIRECTOR_ACCEPTANCE_NOTE.md`
- Final package: `11_delivery/packages/final_proxy_candidate_v1/county_wkw_final_proxy_candidate_v1.zip`
"""
    text = ensure_section(text, "## 下一步 / NEXT", section + "\n## 下一步 / NEXT")
    write(path, text, dry_run)


def update_readme(audio_choice: str, decision_date: str, dry_run: bool) -> None:
    text = read(README)
    text = text.replace(
        "Latest validation: `overall_status=pending_director_or_external_i2v`, `blocking_failures=0`.",
        f"Latest validation: proxy-style final accepted on {decision_date}, final audio choice `{audio_choice}`.",
    )
    text = text.replace(
        "Next recommended step: review `11_delivery/final_decision_gate_v1/FINAL_DECISION_GATE.md`. Then either explicitly accept the proxy style as final, or use `external_i2v_upload_v1` to generate 14 external image-to-video clips and place the returned MP4 files in `09_edit/external_clips/external_i2v_clips_v1/`.",
        "Next recommended step: archive or publish the accepted final proxy package. External I2V remains optional for a future upgraded version.",
    )
    write(README, text, dry_run)


def rebuild_proxy_candidate_zip(dry_run: bool) -> None:
    checksum_paths = [
        "11_delivery/final_proxy_mv_v1/county_wkw_proxy_mv_v1_with_scratch_music.mp4",
        "11_delivery/final_proxy_mv_v1/county_wkw_proxy_mv_v1_ambience_only.mp4",
        "11_delivery/packages/proxy_mv_v1/county_wkw_proxy_mv_v1.zip",
        "11_delivery/final_proxy_candidate_v1/poster_frame_v1.png",
        "10_qa/PROJECT_COMPLETION_AUDIT_V1.md",
        "00_admin/handoff/HANDOFF_LATEST.md",
    ]
    if not dry_run:
        with CHECKSUMS.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["path", "sha256", "bytes"])
            for name in checksum_paths:
                path = ROOT / name
                writer.writerow([name, sha256(path), path.stat().st_size])

    members = [
        "11_delivery/final_proxy_mv_v1/county_wkw_proxy_mv_v1_with_scratch_music.mp4",
        "11_delivery/final_proxy_mv_v1/county_wkw_proxy_mv_v1_ambience_only.mp4",
        "11_delivery/final_proxy_candidate_v1/poster_frame_v1.png",
        "11_delivery/final_proxy_candidate_v1/checksums_sha256.csv",
        "11_delivery/final_proxy_candidate_v1/MANIFEST.md",
        "11_delivery/final_proxy_candidate_v1/QA.md",
        "11_delivery/final_proxy_candidate_v1/DIRECTOR_ACCEPTANCE_NOTE.md",
        "11_delivery/packages/external_i2v_upload_v1/MANIFEST.md",
        "10_qa/PROJECT_COMPLETION_AUDIT_V1.md",
        "00_admin/handoff/HANDOFF_LATEST.md",
    ]
    if not dry_run:
        with zipfile.ZipFile(PROXY_ZIP, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
            for name in members:
                archive.write(ROOT / name, arcname=name)


def rebuild_decision_gate_zip(dry_run: bool) -> None:
    members = [
        "11_delivery/final_decision_gate_v1/FINAL_DECISION_GATE.md",
        "11_delivery/final_decision_gate_v1/PROXY_FINAL_ACCEPTANCE_TEMPLATE.md",
        "11_delivery/final_decision_gate_v1/MANIFEST.md",
        "11_delivery/final_decision_gate_v1/finalize_proxy_acceptance.py",
        "11_delivery/packages/final_decision_gate_v1/MANIFEST.md",
        "10_qa/completion_state_v1.json",
        "10_qa/completion_state_v1.csv",
        "11_delivery/final_proxy_candidate_v1/DIRECTOR_ACCEPTANCE_NOTE.md",
        "11_delivery/packages/external_i2v_upload_v1/MANIFEST.md",
        "09_edit/external_clips/external_i2v_clips_v1/README.md",
    ]
    if not dry_run:
        with zipfile.ZipFile(DECISION_ZIP, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
            for name in members:
                archive.write(ROOT / name, arcname=name)


def run_validator(dry_run: bool) -> str:
    if dry_run:
        return "dry_run"
    subprocess.run(["python3", str(VALIDATOR)], cwd=ROOT, check=True)
    state = json.loads((ROOT / "10_qa/completion_state_v1.json").read_text(encoding="utf-8"))
    return state["summary"]["overall_status"]


def test_zip(path: Path, dry_run: bool) -> None:
    if dry_run:
        return
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
    if bad:
        raise SystemExit(f"zip validation failed for {path}: {bad}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--confirm-director-accepts-proxy-final", action="store_true", help="Required. Confirms the director explicitly accepts proxy motion as final.")
    parser.add_argument("--audio-choice", choices=["with_scratch_music", "ambience_only", "replace_music_later"], required=True)
    parser.add_argument("--director-note", default="Proxy-style final accepted by director.")
    parser.add_argument("--decision-date", default=date.today().isoformat())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.confirm_director_accepts_proxy_final:
        raise SystemExit("Refusing to finalize without --confirm-director-accepts-proxy-final")

    update_acceptance_note(args.audio_choice, args.director_note, args.decision_date, args.dry_run)
    update_audit(args.audio_choice, args.decision_date, args.dry_run)
    update_handoff_file(HANDOFF_LATEST, args.audio_choice, args.decision_date, args.dry_run)
    update_handoff_file(HANDOFF_DATED, args.audio_choice, args.decision_date, args.dry_run)
    update_readme(args.audio_choice, args.decision_date, args.dry_run)
    rebuild_proxy_candidate_zip(args.dry_run)
    status = run_validator(args.dry_run)
    rebuild_decision_gate_zip(args.dry_run)
    test_zip(PROXY_ZIP, args.dry_run)
    test_zip(DECISION_ZIP, args.dry_run)

    if not args.dry_run and status != "complete_proxy_final":
        raise SystemExit(f"Expected complete_proxy_final, got {status}")

    print(f"finalize_proxy_acceptance={'dry_run' if args.dry_run else 'complete'}")
    print(f"overall_status={status}")
    print(f"audio_choice={args.audio_choice}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
