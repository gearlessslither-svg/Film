#!/usr/bin/env python3
import csv
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path


def read_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def add(rows, check, value, status, notes=""):
    rows.append({
        "check": check,
        "value": str(value),
        "status": status,
        "notes": notes,
    })


def exists(root, rel):
    return (root / rel).exists()


def fmt_mtime(timestamp):
    if not timestamp:
        return ""
    return datetime.fromtimestamp(timestamp).isoformat(timespec="seconds")


def latest_existing_mtime(paths):
    mtimes = [p.stat().st_mtime for p in paths if p.exists()]
    return max(mtimes) if mtimes else 0


def oldest_existing_mtime(paths):
    mtimes = [p.stat().st_mtime for p in paths if p.exists()]
    return min(mtimes) if mtimes else 0


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
    aigc = root / "01_AIGC"
    exports = aigc / "exports"
    report = []

    required_files = [
        "TASK_LOG.md",
        "README.md",
        "01_AIGC/19_micro_storyboard_188_panels.csv",
        "01_AIGC/exports/real_image_generation_queue.csv",
        "01_AIGC/exports/micro_storyboard_pure_image_prompts.csv",
        "01_AIGC/exports/visual_asset_qa_checklist.csv",
        "01_AIGC/exports/visual_asset_dual_version_plan.csv",
        "01_AIGC/exports/final_delivery_validation_v002.csv",
        "01_AIGC/tools/build_final_storyboard_panels.py",
        "01_AIGC/tools/build_final_storyboard_video.py",
        "01_AIGC/tools/validate_final_delivery.py",
        "01_AIGC/35_full_pipeline_operating_manual_v1.md",
        "01_AIGC/36_runtime_resilience_and_keepawake_v1.md",
        "scripts/keep-codex-awake.ps1",
    ]
    missing_required = [p for p in required_files if not exists(root, p)]
    add(report, "required_files", len(required_files) - len(missing_required),
        "pass" if not missing_required else "fail",
        "missing=" + ";".join(missing_required) if missing_required else "")

    panels_path = aigc / "19_micro_storyboard_188_panels.csv"
    panels = read_csv(panels_path) if panels_path.exists() else []
    add(report, "micro_storyboard_rows", len(panels),
        "pass" if len(panels) == 188 else "fail")
    if panels:
        panel_ids = [r.get("panel_id", "") for r in panels]
        duplicate_ids = sorted([k for k, v in Counter(panel_ids).items() if v > 1])
        add(report, "micro_storyboard_duplicate_ids", len(duplicate_ids),
            "pass" if not duplicate_ids else "fail",
            ";".join(duplicate_ids[:20]))
        clip_counts = Counter(r.get("clip", "") for r in panels)
        expected_clips = {f"{i:02d}" for i in range(1, 21)}
        missing_clips = sorted(expected_clips - set(clip_counts.keys()))
        add(report, "micro_storyboard_clip_coverage", len(clip_counts),
            "pass" if not missing_clips else "fail",
            "missing=" + ";".join(missing_clips) if missing_clips else json.dumps(dict(sorted(clip_counts.items())), ensure_ascii=False))

    prompt_path = exports / "micro_storyboard_pure_image_prompts.csv"
    prompts = read_csv(prompt_path) if prompt_path.exists() else []
    add(report, "pure_prompt_rows", len(prompts),
        "pass" if len(prompts) == 188 else "fail")
    if prompts:
        prompt_ids = {r.get("panel_id", "") for r in prompts}
        panel_ids = {r.get("panel_id", "") for r in panels}
        missing_prompts = sorted(panel_ids - prompt_ids)
        add(report, "pure_prompt_panel_coverage", len(prompt_ids & panel_ids),
            "pass" if not missing_prompts and len(prompt_ids & panel_ids) == 188 else "fail",
            "missing=" + ";".join(missing_prompts[:20]) if missing_prompts else "")
        max_questions = max((r.get("pure_prompt", "").count("?") for r in prompts), default=0)
        add(report, "pure_prompt_question_marks", max_questions,
            "pass" if max_questions == 0 else "fail")
        missing_whitebox_refs = []
        for r in prompts:
            wb = r.get("whitebox_reference_path", "").strip()
            if wb and not (aigc / wb).exists() and not (root / wb).exists() and not Path(wb).exists():
                missing_whitebox_refs.append(r.get("panel_id", ""))
        add(report, "pure_prompt_whitebox_refs", len(prompts) - len(missing_whitebox_refs),
            "pass" if not missing_whitebox_refs else "fail",
            "missing_panel_refs=" + ";".join(missing_whitebox_refs[:20]) if missing_whitebox_refs else "")

    queue_path = exports / "real_image_generation_queue.csv"
    queue = read_csv(queue_path) if queue_path.exists() else []
    add(report, "real_image_queue_rows", len(queue),
        "pass" if len(queue) == 188 else "fail")
    if queue:
        statuses = Counter(r.get("status", "") for r in queue)
        add(report, "real_image_queue_status_counts", json.dumps(dict(sorted(statuses.items())), ensure_ascii=False),
            "pass")
        bad_paths = []
        for r in queue:
            status = r.get("status", "")
            pure_path = r.get("pure_path", "") or r.get("planned_path", "")
            if status.startswith("generated") and pure_path and not (aigc / pure_path).exists() and not (root / pure_path).exists():
                bad_paths.append(r.get("panel_id", ""))
        add(report, "generated_real_image_files_exist", len(queue) - len(bad_paths),
            "pass" if not bad_paths else "fail",
            "missing=" + ";".join(bad_paths[:20]) if bad_paths else "")
        next_queued = next((r.get("panel_id", "") for r in queue if r.get("status", "") == "queued"), "")
        add(report, "next_queued_panel", next_queued or "none",
            "pass" if next_queued else "warn")

        generated_asset_paths = []
        for r in queue:
            if not r.get("status", "").startswith("generated"):
                continue
            for key in ("pure_path", "annotated_path"):
                rel = r.get(key, "").strip()
                if rel:
                    generated_asset_paths.append(aigc / rel)
        latest_generated_mtime = latest_existing_mtime(generated_asset_paths + [queue_path])
        task_log_mtime = (root / "TASK_LOG.md").stat().st_mtime if (root / "TASK_LOG.md").exists() else 0
        add(
            report,
            "task_log_freshness",
            fmt_mtime(task_log_mtime),
            "pass" if task_log_mtime >= latest_generated_mtime else "warn",
            f"latest_generated_or_queue={fmt_mtime(latest_generated_mtime)}",
        )

    final_validation_path = exports / "final_delivery_validation_v002.csv"
    final_validation = read_csv(final_validation_path) if final_validation_path.exists() else []
    failed_final = [r for r in final_validation if r.get("status") != "pass"]
    add(report, "final_delivery_validation", len(final_validation),
        "pass" if final_validation and not failed_final else "fail",
        "failed=" + ";".join(r.get("check", "") for r in failed_final) if failed_final else "")

    video = aigc / "exports/final_video/coin_slot_final_storyboard_video_v002.mp4"
    audio = aigc / "audio/mix/coin_slot_audio_clean_v002.wav"
    package = aigc / "exports/coin_slot_final_storyboard_audio_video_v002_review_package.zip"
    add(report, "final_video_exists", video.exists(), "pass" if video.exists() else "fail")
    add(report, "clean_audio_exists", audio.exists(), "pass" if audio.exists() else "fail")
    add(report, "review_package_exists", package.exists(), "pass" if package.exists() else "fail")
    if queue:
        final_outputs = [video, final_validation_path, package]
        oldest_final_mtime = oldest_existing_mtime(final_outputs)
        latest_generated_mtime = latest_existing_mtime(
            [aigc / r.get("pure_path", "") for r in queue if r.get("status", "").startswith("generated")]
            + [aigc / r.get("annotated_path", "") for r in queue if r.get("status", "").startswith("generated")]
            + [queue_path]
        )
        add(
            report,
            "final_delivery_freshness",
            fmt_mtime(oldest_final_mtime),
            "pass" if oldest_final_mtime and oldest_final_mtime >= latest_generated_mtime else "warn",
            f"latest_generated_or_queue={fmt_mtime(latest_generated_mtime)}; rebuild final panels/video/package when warn",
        )

    status = "pass" if all(r["status"] in {"pass", "warn"} for r in report) else "fail"
    report_path = exports / "pipeline_state_validation.csv"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["check", "value", "status", "notes"])
        writer.writeheader()
        writer.writerows(report)

    print(f"pipeline_status={status}")
    print(f"report={report_path}")
    for row in report:
        print(f"{row['status']}: {row['check']} = {row['value']} {row['notes']}")
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
