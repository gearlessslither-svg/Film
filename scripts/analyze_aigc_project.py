#!/usr/bin/env python3
"""Analyze a standardized AIGC film project and write a missing-work report."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

from create_aigc_project import STAGES

try:
    import yaml
except Exception:  # pragma: no cover - fallback for minimal Python environments.
    yaml = None

try:
    from PIL import Image
except Exception:  # pragma: no cover - optional image metadata.
    Image = None


TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".csv",
    ".tsv",
    ".json",
    ".yaml",
    ".yml",
    ".srt",
}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".exr", ".psd", ".psb"}
VIDEO_EXTENSIONS = {".mp4", ".mov", ".avi", ".mkv", ".webm"}
AUDIO_EXTENSIONS = {".wav", ".mp3", ".flac", ".aif", ".aiff", ".ogg"}
THREE_D_EXTENSIONS = {".blend", ".fbx", ".obj", ".glb", ".gltf"}
ARCHIVE_EXTENSIONS = {".zip", ".7z", ".rar"}

IGNORED_PARTS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
PLACEHOLDER_FILENAMES = {".gitkeep"}

STAGE_EXPECTATIONS = {
    "00_admin": [
        ("director_brief", "00_admin/director_brief.md", "导演意图、保留项、禁止方向需要有真实内容。"),
        ("model_config", "00_admin/model_config.yaml", "需要配置本地/远程模型双保险策略。"),
        ("project_log", "00_admin/project_log.md", "需要记录阶段推进、模型切换和导演确认。"),
    ],
    "01_intake": [
        ("source_inputs", "01_intake/source_inputs", "需要归档导演原始输入：文字、截图、视频、参考图。"),
        ("references", "01_intake/references", "需要整理外部参考和可复用视觉依据。"),
        ("analysis", "01_intake/analysis", "需要有 AI 对输入材料的分析记录。"),
    ],
    "02_direction": [
        ("creative_brief", "02_direction/creative_brief.md", "需要最终创意方向、故事方向、美术方向和确认记录。"),
        ("options", "02_direction/options", "需要保留 2 到 4 个方向方案，便于导演选择。"),
        ("approvals", "02_direction/approvals", "需要方向确认证据，避免后续批量返工。"),
    ],
    "03_story": [
        ("outlines", "03_story/outlines", "需要故事大纲、结构、转折和情绪曲线。"),
        ("scripts", "03_story/scripts", "需要剧本、旁白、台词或无对白叙事说明。"),
        ("beats", "03_story/beats", "需要场次/节拍表，供分镜和声音同步。"),
    ],
    "04_lookdev": [
        ("styleframes", "04_lookdev/styleframes", "需要风格帧或关键画面预览。"),
        ("palettes", "04_lookdev/palettes", "需要色彩体系、材质关系和视觉对比策略。"),
        ("lighting", "04_lookdev/lighting", "需要光照逻辑、时间、空间和情绪规则。"),
        ("references", "04_lookdev/references", "需要可解释的美术/摄影/类型片参考。"),
    ],
    "05_asset_bible": [
        ("characters", "05_asset_bible/characters", "需要角色设定、脸型、服装、姿态和区分度。"),
        ("character_stage_locks", "05_asset_bible/character_stage_locks", "需要不同故事阶段的角色状态锁定。"),
        ("locations", "05_asset_bible/locations", "需要场景设定、空间关系和可拍摄区域。"),
        ("props", "05_asset_bible/props", "需要关键道具、使用状态和连续性规则。"),
        ("continuity", "05_asset_bible/continuity", "需要跨镜头连续性、禁错项和变体规则。"),
    ],
    "06_previs": [
        ("blender", "06_previs/blender", "需要白模、场景几何、角色站位和镜头约束。"),
        ("camera_manifests", "06_previs/camera_manifests", "需要镜头机位、焦段、运动和构图说明。"),
        ("renders", "06_previs/renders", "需要白模预览图，便于空间关系审核。"),
        ("control_layers", "06_previs/control_layers", "需要深度、线稿、法线、分割等生成控制层。"),
        ("qa", "06_previs/qa", "需要白模相似度、构图和空间还原 QA。"),
    ],
    "07_shots": [
        ("shot_list", "07_shots/shot_list.csv", "需要镜头级任务表，包含状态、空间、提示词和连续性字段。"),
        ("keyframes", "07_shots/keyframes", "需要关键分镜图或锁定帧。"),
        ("prompts", "07_shots/prompts", "需要图片生成提示词。"),
        ("video_prompts", "07_shots/video_prompts", "需要视频生成提示词和运动约束。"),
    ],
    "08_generation": [
        ("jobs", "08_generation/jobs", "需要生成批次、模型参数、失败原因和复跑策略。"),
        ("image_outputs", "08_generation/outputs/images", "需要图片输出或已归档链接。"),
        ("video_outputs", "08_generation/outputs/video", "需要视频输出或已归档链接。"),
        ("rejects", "08_generation/rejects", "需要保留废片原因，避免重复犯错。"),
    ],
    "09_edit": [
        ("rough_cut", "09_edit/rough_cut", "需要粗剪、animatic 或节奏样片。"),
        ("audio", "09_edit/audio", "需要对白、旁白、音效、环境声、音乐或临时声轨。"),
        ("subtitles", "09_edit/subtitles", "需要字幕或文字节奏稿。"),
        ("color", "09_edit/color", "需要调色参考、LUT 或色彩一致性说明。"),
    ],
    "10_qa": [
        ("reports", "10_qa/reports", "需要 QA 报告、审片记录和修复建议。"),
        ("fix_queue", "10_qa/fix_queue", "需要待修复项、优先级和责任阶段。"),
    ],
    "11_delivery": [
        ("exports", "11_delivery/exports", "需要最终导出文件或交付路径。"),
        ("packages", "11_delivery/packages", "需要交付包。"),
        ("manifests", "11_delivery/manifests", "需要交付清单、版本和素材来源。"),
    ],
}

HIGH_VALUE_FILENAMES = {
    "director_brief.md",
    "creative_brief.md",
    "project.yaml",
    "assets_link_map.md",
    "shot_list.csv",
    "project_log.md",
}


def category_for(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in TEXT_EXTENSIONS:
        return "text"
    if suffix in IMAGE_EXTENSIONS:
        return "image"
    if suffix in VIDEO_EXTENSIONS:
        return "video"
    if suffix in AUDIO_EXTENSIONS:
        return "audio"
    if suffix in THREE_D_EXTENSIONS:
        return "3d"
    if suffix in ARCHIVE_EXTENSIONS:
        return "archive"
    return "other"


def should_skip(path: Path) -> bool:
    if path.name in PLACEHOLDER_FILENAMES:
        return True
    if path.name.startswith("project_audit_") and path.suffix.lower() == ".md":
        return True
    return any(part in IGNORED_PARTS for part in path.parts)


def list_files(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(path for path in root.rglob("*") if path.is_file() and not should_skip(path))


def count_files_by_category(files: list[Path]) -> Counter[str]:
    return Counter(category_for(path) for path in files)


def relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root)).replace("\\", "/")
    except ValueError:
        return str(path)


def resolve_optional_path(value: str, *, project_path: Path, cwd: Path) -> Path | None:
    if not value or value.startswith("{{"):
        return None
    raw = Path(value)
    candidates = [raw] if raw.is_absolute() else [cwd / raw, project_path.parent.parent / raw, project_path / raw]
    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()
    return candidates[0].resolve()


def read_manifest(project_path: Path) -> dict[str, object]:
    manifest = project_path / "project.yaml"
    if not manifest.exists():
        return {}
    text = manifest.read_text(encoding="utf-8")
    if yaml is not None:
        data = yaml.safe_load(text)
        return data if isinstance(data, dict) else {}
    result: dict[str, object] = {}
    for line in text.splitlines():
        if line.strip().startswith(("name:", "slug:", "source_root:", "resource_root:")):
            key, _, value = line.partition(":")
            result[key.strip()] = value.strip().strip('"')
    return result


def get_manifest_project_value(manifest: dict[str, object], key: str) -> str:
    project = manifest.get("project")
    if isinstance(project, dict):
        value = project.get(key, "")
        return str(value) if value is not None else ""
    value = manifest.get(key, "")
    return str(value) if value is not None else ""


def meaningful_text_score(path: Path) -> int:
    if not path.exists() or category_for(path) != "text":
        return 0
    try:
        text = path.read_text(encoding="utf-8-sig", errors="ignore")
    except OSError:
        return 0
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped in {"-", "- [ ]", "| --- | --- | --- | --- | --- |"}:
            continue
        if stripped.startswith("#"):
            continue
        if "{{" in stripped and "}}" in stripped:
            continue
        lines.append(stripped)
    compact = re.sub(r"[\W_]+", "", "".join(lines), flags=re.UNICODE)
    return len(compact)


def has_meaningful_path(path: Path) -> bool:
    if path.is_file():
        if path.suffix.lower() in {".md", ".txt"}:
            return meaningful_text_score(path) >= 24
        return path.exists() and path.stat().st_size > 0
    if path.is_dir():
        return any(not should_skip(child) for child in path.rglob("*") if child.is_file())
    return False


def shot_list_stats(project_path: Path) -> dict[str, object]:
    shot_list = project_path / "07_shots" / "shot_list.csv"
    if not shot_list.exists():
        return {"exists": False, "rows": 0, "statuses": {}}
    with shot_list.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    statuses = Counter(row.get("status", "") or "(empty)" for row in rows)
    return {"exists": True, "rows": len(rows), "statuses": dict(statuses)}


def stage_for_relative(path: str) -> str:
    first = path.split("/", 1)[0]
    return first if first in STAGE_EXPECTATIONS else "external"


def find_root_for(path: Path, roots: list[Path], fallback: Path) -> Path:
    for root in roots:
        try:
            path.relative_to(root)
            return root
        except ValueError:
            continue
    return fallback


def choose_samples(
    project_files: list[Path],
    linked_files: list[Path],
    project_path: Path,
    linked_roots: list[Path],
    limit: int,
) -> list[dict[str, object]]:
    all_candidates: list[tuple[str, Path, Path]] = [("project", path, project_path) for path in project_files]
    all_candidates.extend(("linked", path, find_root_for(path, linked_roots, project_path)) for path in linked_files)

    def score(item: tuple[str, Path, Path]) -> tuple[int, str]:
        _, path, root = item
        relative_path = relative(path, root).lower()
        keyword_score = 0
        for keyword in (
            "final",
            "storyboard",
            "contact",
            "whitebox",
            "character",
            "stage",
            "prompt",
            "audio",
            "animatic",
            "manifest",
        ):
            if keyword in relative_path:
                keyword_score -= 1
        name_score = -10 if path.name in HIGH_VALUE_FILENAMES else 0
        origin_score = -2 if item[0] == "project" else 0
        return (name_score + origin_score + keyword_score, relative_path)

    by_category: dict[str, list[tuple[str, Path, Path]]] = {}
    for item in sorted(all_candidates, key=score):
        by_category.setdefault(category_for(item[1]), []).append(item)

    selected: list[tuple[str, Path, Path]] = []
    seen: set[Path] = set()

    for item in by_category.get("text", []):
        if item[1].name in HIGH_VALUE_FILENAMES and item[1] not in seen:
            selected.append(item)
            seen.add(item[1])
        if len(selected) >= min(limit, 8):
            break

    category_order = ["image", "video", "audio", "3d", "text", "archive", "other"]
    while len(selected) < limit:
        grew = False
        for category in category_order:
            for item in by_category.get(category, []):
                if item[1] not in seen:
                    selected.append(item)
                    seen.add(item[1])
                    grew = True
                    break
            if len(selected) >= limit:
                break
        if not grew:
            break

    rows = []
    for origin, path, root in selected:
        item = {
            "origin": origin,
            "path": relative(path, root),
            "category": category_for(path),
            "size_kb": round(path.stat().st_size / 1024, 1),
        }
        if Image is not None and category_for(path) == "image":
            try:
                with Image.open(path) as image:
                    item["dimensions"] = f"{image.width}x{image.height}"
            except Exception:
                item["dimensions"] = ""
        rows.append(item)
    return rows


def analyze_stages(project_path: Path) -> list[dict[str, object]]:
    rows = []
    for stage_id, description in STAGES:
        stage_root = project_path / stage_id
        files = list_files(stage_root)
        checks = []
        missing = []
        weak = []
        for check_id, rel_path, note in STAGE_EXPECTATIONS.get(stage_id, []):
            target = project_path / rel_path
            present = target.exists()
            meaningful = has_meaningful_path(target)
            checks.append({"id": check_id, "present": present, "meaningful": meaningful, "note": note})
            if not present:
                missing.append(check_id)
            elif not meaningful:
                weak.append(check_id)

        if missing:
            status = "fail"
        elif weak:
            status = "warn"
        else:
            status = "pass"

        rows.append(
            {
                "stage": stage_id,
                "description": description,
                "status": status,
                "file_count": len(files),
                "category_counts": dict(count_files_by_category(files)),
                "missing": missing,
                "weak": weak,
                "checks": checks,
            }
        )
    return rows


def build_recommendations(stage_rows: list[dict[str, object]], shot_stats: dict[str, object], linked_count: int) -> list[dict[str, str]]:
    recommendations: list[dict[str, str]] = []
    critical_before_batch = {"02_direction", "03_story", "04_lookdev", "05_asset_bible", "06_previs", "07_shots"}

    def add(priority: str, stage: str, problem: str, action: str) -> None:
        recommendations.append({"priority": priority, "stage": stage, "problem": problem, "action": action})

    for row in stage_rows:
        stage = str(row["stage"])
        missing = row["missing"]
        weak = row["weak"]
        if missing:
            add("P0" if stage in {"01_intake", "02_direction", "03_story", "05_asset_bible", "06_previs", "07_shots"} else "P1", stage, "缺少关键阶段资产: " + ", ".join(missing), "先补齐这些资产，再进入后续批量生成。")
        if weak:
            weak_notes = [
                str(check["note"])
                for check in row.get("checks", [])
                if check.get("id") in weak
            ][:4]
            priority = "P0" if stage in critical_before_batch else "P1"
            add(
                priority,
                stage,
                "存在模板化、空目录或内容不足的资产: " + ", ".join(weak),
                "；".join(weak_notes) if weak_notes else "补真实内容，并记录导演确认或 QA 证据。",
            )

    if int(shot_stats.get("rows", 0)) == 0:
        add("P0", "07_shots", "镜头表没有镜头行，无法驱动批量图像/视频生成。", "先建立 shot_id、story_beat、camera、action、lighting、prompt_path、status 等字段的镜头级任务。")

    if linked_count > 0:
        add("P1", "01_intake", "已有外部/样例资源被链接，但尚未完全归拢到标准阶段目录。", "按 assets_link_map.md 把旧资源分配到 intake、story、previs、shots、generation 的对应阶段，或保留链接并写清证据来源。")

    add("P1", "04_lookdev", "需要建立审美基准，不能只靠单张参考图推进。", "补一组风格帧、色彩脚本、光照逻辑、材质参考和禁止项，形成可复用 look bible。")
    add("P1", "06_previs", "白模精度会直接决定 AIGC 的空间稳定性。", "把关键场景做成更可读的 blocking：比例、站位、镜头高度、焦段、遮挡、前中后景都要可视化。")
    add("P2", "09_edit", "声音和剪辑节奏应尽早进入审美判断。", "为每个故事节拍建立声音意图、静默点、环境声、音效和音乐推进，而不是等画面完成后补。")

    priority_order = {"P0": 0, "P1": 1, "P2": 2}
    return sorted(recommendations, key=lambda item: (priority_order[item["priority"]], item["stage"], item["problem"]))


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        out.append("| " + " | ".join(str(value) for value in row) + " |")
    return "\n".join(out)


def format_counts(counts: Counter[str]) -> str:
    if not counts:
        return "-"
    return ", ".join(f"{key}: {value}" for key, value in sorted(counts.items()))


def build_report(
    *,
    project_path: Path,
    manifest: dict[str, object],
    stage_rows: list[dict[str, object]],
    project_files: list[Path],
    linked_roots: list[Path],
    linked_files: list[Path],
    samples: list[dict[str, object]],
    recommendations: list[dict[str, str]],
    shot_stats: dict[str, object],
    generated_at: str,
    sample_size: int,
) -> str:
    project_counts = count_files_by_category(project_files)
    linked_counts = count_files_by_category(linked_files)
    failed = sum(1 for row in stage_rows if row["status"] == "fail")
    warned = sum(1 for row in stage_rows if row["status"] == "warn")
    passed = sum(1 for row in stage_rows if row["status"] == "pass")
    readiness = round((passed + warned * 0.5) / max(len(stage_rows), 1) * 100)
    if any(item["priority"] == "P0" for item in recommendations) or failed:
        audit_status = "needs_work"
    elif warned:
        audit_status = "warn"
    else:
        audit_status = "pass"

    project_name = get_manifest_project_value(manifest, "name") or project_path.name
    project_slug = get_manifest_project_value(manifest, "slug") or project_path.name

    stage_table = markdown_table(
        ["Stage", "Status", "Files", "Missing", "Weak / Template"],
        [
            [
                row["stage"],
                row["status"],
                row["file_count"],
                ", ".join(row["missing"]) or "-",
                ", ".join(row["weak"]) or "-",
            ]
            for row in stage_rows
        ],
    )

    recommendation_table = markdown_table(
        ["Priority", "Stage", "Problem", "Suggested next action"],
        [[item["priority"], item["stage"], item["problem"], item["action"]] for item in recommendations],
    )

    sample_table = markdown_table(
        ["Origin", "Category", "Size KB", "Path"],
        [[item["origin"], item["category"], item["size_kb"], item["path"]] for item in samples],
    )

    linked_root_text = "\n".join(f"- {root}" for root in linked_roots) if linked_roots else "- (none)"

    ai_prompt = f"""Use $aigc-film-project-auditor to turn this scan into a director-facing audit.

Project: {project_name} (`{project_slug}`)
Project folder: {project_path}
Latest scan: 10_qa/reports/project_audit_latest.md

Focus the human report on:
- P0 missing work before batch generation.
- Whether the idea, story, lookdev, asset bible, previs, shot list, sound, and delivery plan are industrially ready.
- Aesthetic risks: weak visual hierarchy, unclear lens logic, unmotivated light, missing color script, generic character silhouettes, unstable spatial continuity, weak edit rhythm, and insufficient sound design.
- The smallest next batch that would make the project materially more stable.
"""

    return f"""# AIGC Project Audit Report

Generated at: {generated_at}

## Executive Summary

- Project: {project_name} (`{project_slug}`)
- Project path: `{project_path}`
- Audit status: **{audit_status}**
- Readiness score: **{readiness}%**
- Stage status: {passed} pass, {warned} warn, {failed} fail
- Project files scanned: {len(project_files)} ({format_counts(project_counts)})
- Linked resource files scanned: {len(linked_files)} ({format_counts(linked_counts)})
- Shot list rows: {shot_stats.get("rows", 0)}

This is a deterministic asset and workflow scan. It identifies structural gaps, template-only files, missing production evidence, and a representative sample for AI-assisted film/aesthetic review.

## Sampling Method

- Sample size limit: {sample_size}
- Priority order: project manifests, director/creative docs, shot tables, then representative text/image/video/audio/3D files.
- Placeholder files such as `.gitkeep` are ignored.
- Linked roots considered:
{linked_root_text}

## Stage Coverage

{stage_table}

## Priority Recommendations

{recommendation_table}

## Sampled Assets

{sample_table}

## Film And Aesthetic Review Checklist

Use the project files and sampled assets to judge:

- Premise: Is the core cinematic idea clear in one sentence, and is the emotional promise specific?
- Story engine: Are conflict, escalation, reversal, payoff, and audience memory designed rather than accidental?
- Visual hierarchy: Does each image have a clear subject, readable silhouette, foreground/midground/background, and motivated negative space?
- Cinematography: Are lens, camera height, movement, blocking, focus, and shot size chosen for story pressure?
- Lighting: Is light motivated by space, time, source, emotion, genre, and material response?
- Color: Is there a color script with contrast, progression, and scene-to-scene logic?
- Production design: Do characters, props, locations, materials, typography, and scale support the same world?
- Continuity: Are character state, wardrobe, dirt, damage, prop state, spatial geography, and screen direction locked per stage?
- Previs: Does the whitebox solve scale, occlusion, camera, staging, and image-model control layers?
- Editing: Is there rhythm across preparation, action, result, reaction, and transition frames?
- Sound: Are voice, silence, ambience, Foley, sound effects, and music designed as story assets?
- AIGC stability: Are prompts, negative constraints, references, control layers, and QA loops strong enough for batch generation?

## Suggested AI Follow-Up Prompt

```text
{ai_prompt.strip()}
```
"""


def analyze_project(args: argparse.Namespace) -> dict[str, object]:
    project_path = Path(args.project_path).expanduser().resolve()
    cwd = Path.cwd().resolve()
    manifest = read_manifest(project_path)

    project_files = list_files(project_path)

    linked_roots: list[Path] = []
    resource_root = resolve_optional_path(get_manifest_project_value(manifest, "resource_root"), project_path=project_path, cwd=cwd)
    if resource_root and resource_root.exists():
        linked_roots.append(resource_root)

    if args.include_source_root:
        source_root = resolve_optional_path(get_manifest_project_value(manifest, "source_root"), project_path=project_path, cwd=cwd)
        if source_root and source_root.exists():
            linked_roots.append(source_root)

    linked_files: list[Path] = []
    for root in linked_roots:
        linked_files.extend(list_files(root))

    stage_rows = analyze_stages(project_path)
    shot_stats = shot_list_stats(project_path)
    samples = choose_samples(project_files, linked_files, project_path, linked_roots, args.sample_size)
    recommendations = build_recommendations(stage_rows, shot_stats, len(linked_files))

    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    report = build_report(
        project_path=project_path,
        manifest=manifest,
        stage_rows=stage_rows,
        project_files=project_files,
        linked_roots=linked_roots,
        linked_files=linked_files,
        samples=samples,
        recommendations=recommendations,
        shot_stats=shot_stats,
        generated_at=generated_at,
        sample_size=args.sample_size,
    )

    output = Path(args.output) if args.output else project_path / "10_qa" / "reports" / "project_audit_latest.md"
    if not output.is_absolute():
        output = (cwd / output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8", newline="\n")

    if any(item["priority"] == "P0" for item in recommendations) or any(row["status"] == "fail" for row in stage_rows):
        status = "needs_work"
    elif any(row["status"] == "warn" for row in stage_rows):
        status = "warn"
    else:
        status = "pass"
    result = {
        "status": status,
        "project_path": str(project_path),
        "report_path": str(output),
        "project_file_count": len(project_files),
        "linked_file_count": len(linked_files),
        "shot_rows": shot_stats.get("rows", 0),
        "recommendation_count": len(recommendations),
    }
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze an AIGC film project and write a missing-work report.")
    parser.add_argument("project_path", help="Path to projects/<slug>")
    parser.add_argument("--sample-size", type=int, default=24, help="Maximum representative files listed in the report.")
    parser.add_argument("--output", help="Report output path. Default: <project>/10_qa/reports/project_audit_latest.md")
    parser.add_argument("--include-source-root", action="store_true", help="Also scan source_root from project.yaml. This can be large.")
    parser.add_argument("--fail-on-findings", action="store_true", help="Return exit code 1 when required project work is missing.")
    parser.add_argument("--print-json", action="store_true", help="Print machine-readable summary.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.sample_size < 1:
        print("ERROR: --sample-size must be >= 1", file=sys.stderr)
        return 1
    try:
        result = analyze_project(args)
    except Exception as exc:  # noqa: BLE001 - CLI should report any audit error cleanly.
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.print_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"project_audit_status={result['status']}")
        print(f"report={result['report_path']}")
        print(f"project_files={result['project_file_count']}")
        print(f"linked_files={result['linked_file_count']}")
        print(f"shot_rows={result['shot_rows']}")
        print(f"recommendations={result['recommendation_count']}")
    return 1 if args.fail_on_findings and result["status"] != "pass" else 0


if __name__ == "__main__":
    raise SystemExit(main())
