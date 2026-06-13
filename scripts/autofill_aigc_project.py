#!/usr/bin/env python3
"""Autofill missing AIGC film project assets with a controlled local agent.

The agent is deliberately conservative by default:
- it fills missing/weak text, CSV, index, queue, and QA artifacts locally;
- it records image2, Blender, Codex, and plugin-install work as adapter tasks;
- it only runs external commands when explicitly enabled by CLI and config.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from analyze_aigc_project import STAGE_EXPECTATIONS, analyze_stages, get_manifest_project_value, read_manifest, shot_list_stats

try:
    import yaml
except Exception:  # pragma: no cover - YAML is optional for command-line use.
    yaml = None


REPO_ROOT = Path(__file__).resolve().parents[1]
AUTOFILL_CONFIG_REL = Path("00_admin/autofill_config.yaml")
AUTOFILL_RUNS_REL = Path("10_qa/autofill_runs")
AUTOFILL_TASKS_REL = Path("10_qa/autofill_tasks")
AUTOFILL_LATEST_REL = AUTOFILL_RUNS_REL / "autofill_latest.md"
PROJECT_LOG_REL = Path("00_admin/project_log.md")

STANDARD_SHOT_COLUMNS = [
    "shot_id",
    "sequence",
    "story_beat",
    "duration_sec",
    "aspect_ratio",
    "location",
    "character_stage_lock",
    "start_frame",
    "end_frame",
    "camera",
    "action",
    "lighting",
    "continuity_lock",
    "prompt_path",
    "status",
]

DEFAULT_AUTOFILL_CONFIG = {
    "schema_version": 1,
    "autofill": {
        "max_rounds": 3,
        "stop_when_audit_status": "pass",
        "allow_external_tools": False,
        "allow_plugin_install": False,
        "require_external_completion": False,
        "timeout_seconds": 1800,
        "adapters": {
            "codex": {"enabled": False, "command": []},
            "image2": {"enabled": False, "command": []},
            "blender": {"enabled": False, "command": []},
            "plugin_installer": {"enabled": False, "command": []},
        },
    },
}

AUTOFILL_CONFIG_TEXT = """schema_version: 1
autofill:
  max_rounds: 3
  stop_when_audit_status: "pass"
  allow_external_tools: false
  allow_plugin_install: false
  require_external_completion: false
  timeout_seconds: 1800
  adapters:
    codex:
      enabled: false
      command: []
    image2:
      enabled: false
      command: []
    blender:
      enabled: false
      command: []
    plugin_installer:
      enabled: false
      command: []

# Adapter command placeholders:
# - {prompt_path}: task prompt file
# - {output_dir}: target output directory
# - {project_path}: project root
# - {run_dir}: current autofill run directory
#
# Example:
# image2:
#   enabled: true
#   command: ["python", "tools/image2_batch.py", "--prompt-file", "{prompt_path}", "--output-dir", "{output_dir}"]
"""

EXTERNAL_ADAPTER_BY_CHECK = {
    "analysis": "codex",
    "options": "codex",
    "outlines": "codex",
    "scripts": "codex",
    "beats": "codex",
    "styleframes": "image2",
    "references": "codex",
    "characters": "image2",
    "character_stage_locks": "codex",
    "locations": "image2",
    "props": "image2",
    "continuity": "codex",
    "blender": "blender",
    "renders": "blender",
    "control_layers": "blender",
    "keyframes": "image2",
    "image_outputs": "image2",
    "video_outputs": "image2",
    "rough_cut": "codex",
    "audio": "codex",
    "color": "codex",
}


@dataclass
class Gap:
    stage: str
    check_id: str
    rel_path: str
    note: str
    present: bool
    meaningful: bool


@dataclass
class Change:
    action: str
    path: str
    note: str


@dataclass
class ExternalTask:
    adapter: str
    stage: str
    check_id: str
    prompt_path: Path
    output_dir: Path
    status: str = "pending"
    returncode: int | None = None
    log_path: Path | None = None
    note: str = ""


@dataclass
class RoundResult:
    index: int
    gaps_before: int
    changes: list[Change] = field(default_factory=list)
    external_tasks: list[ExternalTask] = field(default_factory=list)


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def safe_name(value: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9_-]+", "-", value).strip("-").lower()
    return text or "task"


def relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root)).replace("\\", "/")
    except ValueError:
        return str(path)


def load_config(project_path: Path) -> dict[str, Any]:
    config_path = project_path / AUTOFILL_CONFIG_REL
    config = DEFAULT_AUTOFILL_CONFIG
    if config_path.exists() and yaml is not None:
        loaded = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        if isinstance(loaded, dict):
            config = deep_merge(config, loaded)

    adapters = config.setdefault("autofill", {}).setdefault("adapters", {})
    env_map = {
        "codex": "AIGC_AUTOFILL_CODEX_CMD",
        "image2": "AIGC_AUTOFILL_IMAGE2_CMD",
        "blender": "AIGC_AUTOFILL_BLENDER_CMD",
        "plugin_installer": "AIGC_AUTOFILL_PLUGIN_INSTALL_CMD",
    }
    for adapter, env_name in env_map.items():
        raw = os.environ.get(env_name, "").strip()
        if not raw:
            continue
        entry = adapters.setdefault(adapter, {})
        entry["enabled"] = True
        try:
            parsed = json.loads(raw)
            entry["command"] = parsed if isinstance(parsed, list) else [str(parsed)]
        except json.JSONDecodeError:
            entry["command"] = raw.split()
    return config


def ensure_autofill_config(project_path: Path, *, dry_run: bool) -> list[Change]:
    path = project_path / AUTOFILL_CONFIG_REL
    if path.exists():
        return []
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(AUTOFILL_CONFIG_TEXT, encoding="utf-8", newline="\n")
    return [Change("create", relative(path, project_path), "Created local autofill adapter config.")]


def project_identity(project_path: Path) -> tuple[str, str]:
    manifest = read_manifest(project_path)
    name = get_manifest_project_value(manifest, "name") or project_path.name
    slug = get_manifest_project_value(manifest, "slug") or project_path.name
    return name, slug


def collect_gaps(project_path: Path) -> list[Gap]:
    rows = analyze_stages(project_path)
    expectations = {
        (stage_id, check_id): (rel_path, note)
        for stage_id, checks in STAGE_EXPECTATIONS.items()
        for check_id, rel_path, note in checks
    }
    gaps: list[Gap] = []
    for row in rows:
        stage = str(row["stage"])
        for check in row.get("checks", []):
            if check.get("present") and check.get("meaningful"):
                continue
            check_id = str(check.get("id", ""))
            rel_path, note = expectations.get((stage, check_id), ("", str(check.get("note", ""))))
            gaps.append(
                Gap(
                    stage=stage,
                    check_id=check_id,
                    rel_path=rel_path,
                    note=note,
                    present=bool(check.get("present")),
                    meaningful=bool(check.get("meaningful")),
                )
            )
    return gaps


def read_shot_rows(project_path: Path) -> list[dict[str, str]]:
    shot_list = project_path / "07_shots/shot_list.csv"
    if not shot_list.exists():
        return []
    with shot_list.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def default_shot_rows(project_name: str) -> list[dict[str, str]]:
    beats = [
        ("S001", "Opening pressure", "The world and main tension become readable."),
        ("S002", "First decision", "A character chooses a direction under pressure."),
        ("S003", "Complication", "The plan collides with a physical or emotional obstacle."),
        ("S004", "Reversal", "The audience learns the situation is not what it seemed."),
        ("S005", "Payoff", "The core visual promise resolves in one strong image."),
        ("S006", "Afterimage", "A quiet final beat leaves memory and tone."),
    ]
    rows = []
    for index, (shot_id, beat, action) in enumerate(beats, start=1):
        rows.append(
            {
                "shot_id": shot_id,
                "sequence": f"SEQ{index:02d}",
                "story_beat": beat,
                "duration_sec": "4.0",
                "aspect_ratio": "16:9",
                "location": "TBD production space",
                "character_stage_lock": f"STAGE_{index:02d}",
                "start_frame": f"{project_name} provisional start frame {index}",
                "end_frame": f"{project_name} provisional end frame {index}",
                "camera": "story-motivated medium shot, locked screen direction",
                "action": action,
                "lighting": "motivated key light, readable silhouette, controlled contrast",
                "continuity_lock": "Preserve geography, eyeline, wardrobe state, prop state, and emotional state.",
                "prompt_path": f"07_shots/prompts/{shot_id}.md",
                "status": "autofill_draft",
            }
        )
    return rows


def write_shot_list(project_path: Path, project_name: str, *, dry_run: bool) -> list[Change]:
    path = project_path / "07_shots/shot_list.csv"
    rows = read_shot_rows(project_path)
    if rows:
        return []
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=STANDARD_SHOT_COLUMNS)
            writer.writeheader()
            writer.writerows(default_shot_rows(project_name))
    return [Change("write", relative(path, project_path), "Created provisional shot list rows.")]


def prompt_text(project_name: str, row: dict[str, str], *, video: bool) -> str:
    shot_id = row.get("shot_id", "S000")
    mode = "Video generation prompt" if video else "Image generation prompt"
    movement = "Camera movement should be restrained and physically motivated." if video else "Single production keyframe."
    return f"""# {mode} - {shot_id}

Project: {project_name}
Status: autofill draft; replace after director review.

## Story Function
- Beat: {row.get("story_beat", "TBD")}
- Action: {row.get("action", "TBD")}

## Visual Prompt
Create a cinematic frame with clear subject hierarchy, readable silhouette, foreground/midground/background separation, stable screen direction, and continuity with `{row.get("character_stage_lock", "TBD")}`.

## Camera And Space
- Camera: {row.get("camera", "TBD")}
- Location: {row.get("location", "TBD")}
- Continuity: {row.get("continuity_lock", "TBD")}

## Lighting
{row.get("lighting", "Motivated lighting with controlled contrast.")}

## Motion
{movement}

## Negative Constraints
Avoid generic stock framing, drifting character identity, impossible camera geography, inconsistent wardrobe, extra limbs, unreadable hands, smeared faces, broken props, and unmotivated lighting.
"""


def write_prompt_files(project_path: Path, project_name: str, *, dry_run: bool) -> list[Change]:
    changes: list[Change] = []
    rows = read_shot_rows(project_path) or default_shot_rows(project_name)
    for row in rows:
        shot_id = row.get("shot_id", "").strip() or "S000"
        for folder, is_video in [("07_shots/prompts", False), ("07_shots/video_prompts", True)]:
            path = project_path / folder / f"{shot_id}.md"
            if path.exists() and path.stat().st_size > 80:
                continue
            if not dry_run:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(prompt_text(project_name, row, video=is_video), encoding="utf-8", newline="\n")
            changes.append(Change("write", relative(path, project_path), "Created shot-level prompt draft."))
    return changes


def location_summary(project_path: Path) -> str:
    rows = read_shot_rows(project_path)
    counts: dict[str, int] = {}
    for row in rows:
        location = (row.get("location") or "TBD").strip() or "TBD"
        counts[location] = counts.get(location, 0) + 1
    if not counts:
        return "- TBD production space"
    return "\n".join(f"- {location}: {count} shots" for location, count in sorted(counts.items()))


def beat_summary(project_path: Path) -> str:
    rows = read_shot_rows(project_path)
    if not rows:
        return "- Opening pressure\n- Complication\n- Payoff"
    lines = []
    for row in rows[:12]:
        lines.append(f"- {row.get('shot_id', 'S000')}: {row.get('story_beat', 'TBD')} | {row.get('action', 'TBD')}")
    return "\n".join(lines)


def write_if_missing(path: Path, text: str, note: str, project_path: Path, *, dry_run: bool) -> list[Change]:
    if path.exists() and path.stat().st_size > 160:
        return []
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
    return [Change("write", relative(path, project_path), note)]


def recommendation_asset_texts(project_path: Path, project_name: str) -> list[tuple[Path, str, str]]:
    manifest = read_manifest(project_path)
    resource_root = get_manifest_project_value(manifest, "resource_root") or "(not linked)"
    source_root = get_manifest_project_value(manifest, "source_root") or "(not linked)"
    generated = now_iso()
    locations = location_summary(project_path)
    beats = beat_summary(project_path)
    return [
        (
            project_path / "01_intake/analysis/coin_slot_resource_evidence_map.md",
            f"""# Resource Evidence Map

Project: {project_name}
Generated at: {generated}
Status: autofill recommendation asset

## Linked Roots

- Source root: `{source_root}`
- Resource root: `{resource_root}`

## Stage Evidence Map

| Stage | Evidence Source | Production Use | Keep As Link Or Copy |
| --- | --- | --- | --- |
| `01_intake/source_inputs` | Director notes, screenshots, rough media, original folders | Raw intent and provenance | Link unless final source is small text |
| `01_intake/references` | External visual references and sample material | Mood, era, texture, composition checks | Link or copy curated thumbnails |
| `03_story` | Beat sheets, scripts, micro-storyboard tables | Story state and continuity decisions | Copy final text tables |
| `04_lookdev` | Character references, contact sheets, style tests | Look bible and palette rules | Copy final approved stills via LFS |
| `06_previs` | Blender files, whitebox renders, camera manifests | Spatial lock, camera lock, control layers | Copy approved manifests; LFS for media |
| `07_shots` | Shot CSV, prompts, keyframe indexes | Batch image/video task driver | Copy current production tables |
| `08_generation` | Image/video outputs and reject logs | QA loop and rerun evidence | LFS for approved media, text logs in Git |

## Current Shot Locations

{locations}

## Rule

If a file is used as an input for generation, record where it came from, whether it is authoritative, and which shot or story stage depends on it.
""",
            "Filled P1 linked-resource evidence mapping.",
        ),
        (
            project_path / "04_lookdev/references/coin_slot_look_bible_v001.md",
            f"""# Coin Slot Look Bible V001

Project: {project_name}
Generated at: {generated}
Status: autofill recommendation asset

## Visual Thesis

The film should feel like a pressured childhood memory colliding with arcade machinery: CRT glow, coin-slot metal, damp exterior air, shallow pockets of safety, and sudden pockets of threat.

## Color Script

| Story Zone | Dominant Color Logic | Contrast Role |
| --- | --- | --- |
| Compound / threshold | cold gray-green, dirty cyan, weak practicals | establishes pressure and surveillance |
| Arcade interior | CRT cyan, cabinet red, sodium spill, black recesses | seduction, confusion, fractured attention |
| Alley / exit | desaturated blue-green, concrete gray, small warm practicals | danger, isolation, aftermath |

## Lighting Rules

- Use motivated practical light: CRT screens, arcade signs, doorway spill, phone glow, street lamps.
- Keep faces readable but never glossy; use soft falloff and dirty ambient bounce.
- Silhouette should carry story pressure: protectors wider, younger brother smaller, threat group more angular.
- Avoid beauty lighting unless it is deliberately ironic or memory-like.

## Material And Texture

- Metal: worn coin-slot edges, scratched chrome, oily fingerprints.
- Plastic: aged arcade buttons, cloudy cabinet plexi, chipped colored surfaces.
- Fabric: school-age layers, washed cotton, dust, scuffs, sweat at late-stage stress points.
- Ground: concrete, damp patches, flattened trash, fluorescent reflection.

## Forbidden Looks

- Clean cyberpunk neon, glossy music-video contrast, generic streetwear catalog poses.
- Characters changing age, face shape, wardrobe state, dirt state, or relative height across adjacent shots.
- Unmotivated rim light, empty bokeh backgrounds, wide shots without readable blocking.

## Shot Beat Reference

{beats}
""",
            "Filled P1 reusable look bible.",
        ),
        (
            project_path / "06_previs/qa/coin_slot_blocking_readability_upgrade_plan.md",
            f"""# Blocking Readability Upgrade Plan

Project: {project_name}
Generated at: {generated}
Status: autofill recommendation asset

## Goal

Raise whitebox/previs usefulness from rough spatial reminder to image-generation control source. The next Blender pass should make scale, eyeline, occlusion, camera height, and foreground/midground/background readable at thumbnail size.

## Required Checks

| Check | Acceptance Criteria |
| --- | --- |
| Scale | child/adult height relation is clear in every shared frame |
| Screen direction | exits, threats, and movement preserve left/right continuity |
| Camera height | low, child-height, eye-level, and high-angle shots are explicitly labeled |
| Lens logic | wide, normal, and compressed views are not mixed accidentally |
| Occlusion | doorframes, cabinets, bodies, and foreground objects support story pressure |
| Depth | each key shot has clear foreground, midground, and background planes |
| Action readability | preparation, action, result, and reaction frames are separated |

## Current Location Coverage

{locations}

## Next Blender Tasks

- Add simple human-scale stand-ins with distinct silhouettes for each character group.
- Add camera markers named by `shot_id`.
- Export one clean whitebox render and one annotated review render per key shot.
- Export depth, line, normal, or segmentation layers only after camera and blocking are approved.
- Add a QA contact sheet before using the renders in image generation.
""",
            "Filled P1 whitebox/blocking upgrade plan.",
        ),
        (
            project_path / "09_edit/audio/coin_slot_sound_edit_intent_map.md",
            f"""# Sound And Edit Intent Map

Project: {project_name}
Generated at: {generated}
Status: autofill recommendation asset

## Principle

Sound is part of visual continuity. Each story beat needs an intended sound perspective before final image/video generation, so prompts can preserve distance, tension, silence, and motion rhythm.

## Beat-Level Sound Intent

| Beat Type | Sound Perspective | Edit Rhythm |
| --- | --- | --- |
| Threshold / approach | muffled arcade walla, distant cabinet tones, shoe scuff | hold slightly too long before entry |
| Discovery / coin-slot focus | close mechanical click, finger scrape, CRT hum | cut on attention shift rather than action completion |
| Threat arrival | offscreen voices first, then body presence | shorten shot duration, preserve reaction frames |
| Escape / alley | breathing, concrete footsteps, reduced music | alternate motion with stillness |
| Afterimage | sparse room tone, one unresolved machine tone | allow silence to carry the final image |

## Shot Beat Reference

{beats}

## QA Notes

- Dialogue, Foley, ambience, and music should be tracked by shot or story stage.
- Silence is a design asset and should be marked in the rough cut plan.
- If a generated video changes motion speed, update sound intent before regenerating the next batch.
""",
            "Filled P2 sound/edit intent map.",
        ),
    ]


def fill_recommendation_assets(project_path: Path, project_name: str, *, dry_run: bool) -> list[Change]:
    changes: list[Change] = []
    for path, text, note in recommendation_asset_texts(project_path, project_name):
        changes.extend(write_if_missing(path, text, note, project_path, dry_run=dry_run))
    return changes


def directory_index_text(project_name: str, gap: Gap) -> str:
    return f"""# Autofill Index - {gap.stage}/{gap.check_id}

Project: {project_name}
Generated at: {now_iso()}
Status: provisional scaffold; replace or expand with reviewed production evidence.

## Why This Exists
The analyzer found this project area missing or too weak: `{gap.rel_path}`.

## Minimum Contents To Lock
- A concrete production decision, not only a placeholder.
- Evidence source: director input, AI analysis, reference file, whitebox render, prompt batch, QA result, or approval note.
- Continuity constraints that future image/video generation must preserve.
- Known risks and what should be reviewed next.

## Next Production Task
Use this index as a landing page, then add the real files for `{gap.check_id}` in this folder.
"""


def file_draft_text(project_name: str, gap: Gap) -> str:
    title = gap.check_id.replace("_", " ").title()
    return f"""# {title}

Project: {project_name}
Generated at: {now_iso()}
Status: autofill draft; director review required.

## Current Best Fill
- The project needs a concrete artifact for `{gap.stage}/{gap.check_id}`.
- This draft exists to remove structural blockage and give Codex or another specialist tool enough context to continue.

## Production Decisions
- Define the story purpose, visual purpose, continuity lock, and acceptance criteria for this asset.
- Keep all future image/video prompts tied to these decisions.

## Evidence To Add
- Source input or reference path:
- Model or tool used:
- Approval or rejection note:
- QA result:

## Next Action
Replace this draft with a stronger project-specific version or send it to the matching external adapter.
"""


def write_file_gap(project_path: Path, project_name: str, gap: Gap, *, dry_run: bool) -> list[Change]:
    target = project_path / gap.rel_path
    if target.name == "shot_list.csv":
        return write_shot_list(project_path, project_name, dry_run=dry_run)

    text = file_draft_text(project_name, gap)
    existed = target.exists()
    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        if existed:
            existing = target.read_text(encoding="utf-8", errors="ignore")
            marker = "<!-- AUTOFILL_DRAFT -->"
            if marker in existing:
                before, _, _ = existing.partition(marker)
                target.write_text(before.rstrip() + "\n\n" + marker + "\n" + text, encoding="utf-8", newline="\n")
            else:
                target.write_text(existing.rstrip() + "\n\n" + marker + "\n" + text, encoding="utf-8", newline="\n")
        else:
            target.write_text(text, encoding="utf-8", newline="\n")
    action = "append" if existed else "write"
    return [Change(action, relative(target, project_path), "Filled missing or weak required file.")]


def write_directory_gap(project_path: Path, project_name: str, gap: Gap, *, dry_run: bool) -> list[Change]:
    target = project_path / gap.rel_path
    index_name = f"autofill_{safe_name(gap.check_id)}_index.md"
    index_path = target / index_name
    if not dry_run:
        target.mkdir(parents=True, exist_ok=True)
        index_path.write_text(directory_index_text(project_name, gap), encoding="utf-8", newline="\n")
    return [Change("write", relative(index_path, project_path), "Created required stage index artifact.")]


def apply_internal_gap(project_path: Path, project_name: str, gap: Gap, *, dry_run: bool) -> list[Change]:
    if gap.check_id in {"prompts", "video_prompts"}:
        return write_prompt_files(project_path, project_name, dry_run=dry_run)
    target = project_path / gap.rel_path
    if target.suffix:
        return write_file_gap(project_path, project_name, gap, dry_run=dry_run)
    return write_directory_gap(project_path, project_name, gap, dry_run=dry_run)


def external_prompt(project_name: str, gap: Gap) -> str:
    adapter = EXTERNAL_ADAPTER_BY_CHECK.get(gap.check_id, "codex")
    return f"""# External Autofill Task

Project: {project_name}
Stage: {gap.stage}
Check: {gap.check_id}
Target path: {gap.rel_path}
Recommended adapter: {adapter}
Generated at: {now_iso()}

## Problem
The project analyzer found this area missing or too weak for stable AIGC film production.

## Requested Output
Create or improve the production artifact for `{gap.rel_path}`. The output must be usable by the pipeline, not only illustrative.

## Quality Bar
- Make the artifact specific to this project.
- Preserve story-stage continuity, character identity, spatial geography, lens logic, motivated light, and color strategy.
- Include enough metadata for QA: source inputs, model/tool, settings, prompt, negative constraints, output path, and review status.

## Tool-Specific Notes
- Codex: write structured docs, tables, prompts, fix queues, and decision logs.
- image2: produce styleframes, keyframes, character/location/prop visual references, or image batches.
- Blender: produce whitebox scene updates, camera manifests, renders, and control-layer exports.
- plugin_installer: install only the plugin needed to execute a listed adapter command and record evidence.
"""


def build_external_tasks(project_path: Path, project_name: str, gaps: list[Gap], run_dir: Path, *, dry_run: bool) -> list[ExternalTask]:
    tasks: list[ExternalTask] = []
    seen: set[tuple[str, str, str]] = set()
    task_dir = run_dir / "tasks"
    for gap in gaps:
        adapter = EXTERNAL_ADAPTER_BY_CHECK.get(gap.check_id)
        if adapter is None:
            continue
        key = (adapter, gap.stage, gap.check_id)
        if key in seen:
            continue
        seen.add(key)
        prompt_path = task_dir / f"{adapter}_{gap.stage}_{safe_name(gap.check_id)}.md"
        output_dir = project_path / gap.rel_path
        if (project_path / gap.rel_path).suffix:
            output_dir = (project_path / gap.rel_path).parent
        if not dry_run:
            prompt_path.parent.mkdir(parents=True, exist_ok=True)
            prompt_path.write_text(external_prompt(project_name, gap), encoding="utf-8", newline="\n")
            output_dir.mkdir(parents=True, exist_ok=True)
        tasks.append(ExternalTask(adapter=adapter, stage=gap.stage, check_id=gap.check_id, prompt_path=prompt_path, output_dir=output_dir))
    return tasks


def adapter_config(config: dict[str, Any], adapter: str) -> dict[str, Any]:
    return dict(config.get("autofill", {}).get("adapters", {}).get(adapter, {}))


def render_command_args(command: list[Any], task: ExternalTask, project_path: Path, run_dir: Path) -> list[str]:
    values = {
        "prompt_path": str(task.prompt_path),
        "output_dir": str(task.output_dir),
        "project_path": str(project_path),
        "run_dir": str(run_dir),
    }
    return [str(part).format(**values) for part in command]


def run_external_task(
    task: ExternalTask,
    *,
    config: dict[str, Any],
    project_path: Path,
    run_dir: Path,
    allow_external: bool,
    allow_plugin_install: bool,
    timeout_seconds: int,
    dry_run: bool,
) -> ExternalTask:
    if dry_run:
        task.status = "dry_run"
        task.note = "External task not executed in dry-run mode."
        return task

    if task.adapter == "plugin_installer" and not allow_plugin_install:
        task.status = "blocked"
        task.note = "Plugin installation is disabled."
        return task
    if task.adapter != "plugin_installer" and not allow_external:
        task.status = "pending"
        task.note = "External tools are disabled for this run."
        return task

    entry = adapter_config(config, task.adapter)
    command = entry.get("command") or []
    if not entry.get("enabled") or not command:
        task.status = "pending"
        task.note = f"Adapter `{task.adapter}` has no enabled command."
        return task

    args = render_command_args(list(command), task, project_path, run_dir)
    log_path = run_dir / "logs" / f"{task.adapter}_{task.stage}_{safe_name(task.check_id)}.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    completed = subprocess.run(
        args,
        cwd=REPO_ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        timeout=timeout_seconds,
        check=False,
    )
    log_path.write_text(
        "COMMAND\n" + json.dumps(args, ensure_ascii=False, indent=2) + "\n\nSTDOUT\n" + completed.stdout + "\n\nSTDERR\n" + completed.stderr,
        encoding="utf-8",
        newline="\n",
    )
    task.returncode = completed.returncode
    task.log_path = log_path
    task.status = "done" if completed.returncode == 0 else "failed"
    task.note = "External command executed."
    return task


def run_analyzer(project_path: Path, sample_size: int, include_source_root: bool) -> dict[str, Any]:
    args = [
        sys.executable,
        "scripts/analyze_aigc_project.py",
        str(project_path),
        "--sample-size",
        str(sample_size),
        "--print-json",
    ]
    if include_source_root:
        args.append("--include-source-root")
    completed = subprocess.run(
        args,
        cwd=REPO_ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )
    text = completed.stdout.strip()
    payload: dict[str, Any] = {}
    if text:
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            payload = json.loads(text[start : end + 1])
    payload["returncode"] = completed.returncode
    payload["stderr"] = completed.stderr
    return payload


def append_project_log(project_path: Path, status: str, report_path: Path, *, dry_run: bool) -> None:
    if dry_run:
        return
    log_path = project_path / PROJECT_LOG_REL
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        log_path.write_text(
            "# Project Log\n\n| Date | Stage | Decision / Change | Owner | Evidence |\n| --- | --- | --- | --- | --- |\n",
            encoding="utf-8",
            newline="\n",
        )
    date = datetime.now().strftime("%Y-%m-%d")
    evidence = relative(report_path, project_path)
    line = f"| {date} | 10_qa | Autofill run completed with status `{status}`. | AI | {evidence} |\n"
    with log_path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(line)


def write_autofill_report(
    project_path: Path,
    run_dir: Path,
    *,
    project_name: str,
    project_slug: str,
    rounds: list[RoundResult],
    final_scan: dict[str, Any],
    completion_status: str,
    dry_run: bool,
    allow_external: bool,
    allow_plugin_install: bool,
) -> Path:
    report_path = run_dir / "autofill_report.md"
    latest_path = project_path / AUTOFILL_LATEST_REL
    all_changes = [change for round_result in rounds for change in round_result.changes]
    all_tasks = [task for round_result in rounds for task in round_result.external_tasks]
    pending_external_count = sum(1 for task in all_tasks if task.status == "pending")

    def changes_table() -> str:
        if not all_changes:
            return "| Action | Path | Note |\n| --- | --- | --- |\n| - | - | No local content changes were needed. |\n"
        lines = ["| Action | Path | Note |", "| --- | --- | --- |"]
        for change in all_changes:
            lines.append(f"| {change.action} | `{change.path}` | {change.note} |")
        return "\n".join(lines) + "\n"

    def tasks_table() -> str:
        if not all_tasks:
            return "| Adapter | Stage | Check | Status | Prompt | Output |\n| --- | --- | --- | --- | --- | --- |\n| - | - | - | - | No external tasks were required. | - |\n"
        lines = ["| Adapter | Stage | Check | Status | Prompt | Output |", "| --- | --- | --- | --- | --- | --- |"]
        for task in all_tasks:
            prompt = relative(task.prompt_path, project_path)
            output = relative(task.output_dir, project_path)
            lines.append(f"| {task.adapter} | {task.stage} | {task.check_id} | {task.status} | `{prompt}` | `{output}` |")
        return "\n".join(lines) + "\n"

    text = f"""# Autofill Run Report

Generated at: {now_iso()}

## Summary

- Project: {project_name} (`{project_slug}`)
- Project path: `{project_path}`
- Completion status: **{completion_status}**
- Final audit status: **{final_scan.get("status", "unknown")}**
- Final shot rows: {final_scan.get("shot_rows", 0)}
- Local changes: {len(all_changes)}
- External tasks: {len(all_tasks)}
- Pending external tasks: {pending_external_count}
- Dry run: {str(dry_run).lower()}
- External tools allowed: {str(allow_external).lower()}
- Plugin install allowed: {str(allow_plugin_install).lower()}

## Rounds

| Round | Gaps before | Local changes | External tasks |
| --- | --- | --- | --- |
{chr(10).join(f"| {item.index} | {item.gaps_before} | {len(item.changes)} | {len(item.external_tasks)} |" for item in rounds)}

## Local Changes

{changes_table()}

## External Adapter Tasks

{tasks_table()}

## Interpretation

- `ready_for_director_review` means the deterministic analyzer reports `pass`.
- Pending external tasks mean richer media generation or specialized tool work is available but was not executed in this run.
- To execute adapters, enable them in `{AUTOFILL_CONFIG_REL}` and run with `--allow-external`; plugin installation also requires `--allow-plugin-install`.
"""
    if not dry_run:
        run_dir.mkdir(parents=True, exist_ok=True)
        report_path.write_text(text, encoding="utf-8", newline="\n")
        latest_path.parent.mkdir(parents=True, exist_ok=True)
        latest_path.write_text(text, encoding="utf-8", newline="\n")
    return latest_path


def completion_status(final_scan: dict[str, Any], rounds: list[RoundResult], require_external_completion: bool) -> str:
    audit_status = final_scan.get("status", "unknown")
    tasks = [task for round_result in rounds for task in round_result.external_tasks]
    pending_or_failed = [task for task in tasks if task.status not in {"done", "dry_run"}]
    if audit_status != "pass":
        return "needs_more_work"
    if require_external_completion and pending_or_failed:
        return "structural_pass_external_pending"
    return "ready_for_director_review"


def autofill_project(args: argparse.Namespace) -> dict[str, Any]:
    project_path = Path(args.project_path).expanduser().resolve()
    if not project_path.exists():
        raise FileNotFoundError(f"Project folder does not exist: {project_path}")

    project_name, project_slug = project_identity(project_path)
    run_id = datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = project_path / AUTOFILL_RUNS_REL / run_id
    config_changes = ensure_autofill_config(project_path, dry_run=args.dry_run)
    config = load_config(project_path)
    autofill_config = config.get("autofill", {})
    max_rounds = args.max_rounds or int(autofill_config.get("max_rounds", 3) or 3)
    timeout_seconds = int(autofill_config.get("timeout_seconds", 1800) or 1800)
    allow_external = bool(args.allow_external or autofill_config.get("allow_external_tools", False))
    allow_plugin_install = bool(args.allow_plugin_install or autofill_config.get("allow_plugin_install", False))
    require_external_completion = bool(args.require_external_complete or autofill_config.get("require_external_completion", False))

    rounds: list[RoundResult] = []
    if config_changes:
        rounds.append(RoundResult(index=0, gaps_before=0, changes=config_changes))

    for round_index in range(1, max_rounds + 1):
        gaps = collect_gaps(project_path)
        round_result = RoundResult(index=round_index, gaps_before=len(gaps))
        if int(shot_list_stats(project_path).get("rows", 0) or 0) == 0:
            round_result.changes.extend(write_shot_list(project_path, project_name, dry_run=args.dry_run))
        if not gaps:
            round_result.changes.extend(fill_recommendation_assets(project_path, project_name, dry_run=args.dry_run))
            rounds.append(round_result)
            break

        for gap in gaps:
            round_result.changes.extend(apply_internal_gap(project_path, project_name, gap, dry_run=args.dry_run))

        external_tasks = build_external_tasks(project_path, project_name, gaps, run_dir, dry_run=args.dry_run)
        for task in external_tasks:
            round_result.external_tasks.append(
                run_external_task(
                    task,
                    config=config,
                    project_path=project_path,
                    run_dir=run_dir,
                    allow_external=allow_external,
                    allow_plugin_install=allow_plugin_install,
                    timeout_seconds=timeout_seconds,
                    dry_run=args.dry_run,
                )
            )

        rounds.append(round_result)
        if not round_result.changes and not external_tasks:
            break

    final_scan = run_analyzer(project_path, args.sample_size, args.include_source_root)
    status = completion_status(final_scan, rounds, require_external_completion)
    report_path = write_autofill_report(
        project_path,
        run_dir,
        project_name=project_name,
        project_slug=project_slug,
        rounds=rounds,
        final_scan=final_scan,
        completion_status=status,
        dry_run=args.dry_run,
        allow_external=allow_external,
        allow_plugin_install=allow_plugin_install,
    )
    append_project_log(project_path, status, report_path, dry_run=args.dry_run)

    all_changes = [change for round_result in rounds for change in round_result.changes]
    all_tasks = [task for round_result in rounds for task in round_result.external_tasks]
    result = {
        "status": status,
        "audit_status": final_scan.get("status", "unknown"),
        "project_path": str(project_path),
        "report_path": str(report_path),
        "rounds": len(rounds),
        "changed_count": len(all_changes),
        "external_task_count": len(all_tasks),
        "pending_external_count": sum(1 for task in all_tasks if task.status == "pending"),
        "failed_external_count": sum(1 for task in all_tasks if task.status == "failed"),
        "shot_rows": final_scan.get("shot_rows", 0),
    }
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Autofill missing AIGC film project assets.")
    parser.add_argument("project_path", help="Path to projects/<slug>")
    parser.add_argument("--max-rounds", type=int, default=0, help="Maximum autofill rounds. Default reads config or 3.")
    parser.add_argument("--sample-size", type=int, default=24, help="Analyzer sample size after autofill.")
    parser.add_argument("--include-source-root", action="store_true", help="Also scan source_root during final analysis.")
    parser.add_argument("--allow-external", action="store_true", help="Allow enabled Codex/image2/Blender adapter commands to run.")
    parser.add_argument("--allow-plugin-install", action="store_true", help="Allow enabled plugin installer adapter commands to run.")
    parser.add_argument("--require-external-complete", action="store_true", help="Do not sign off while external adapter tasks are pending.")
    parser.add_argument("--dry-run", action="store_true", help="Plan changes without writing files or running external tools.")
    parser.add_argument("--print-json", action="store_true", help="Print machine-readable summary.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    result = autofill_project(args)
    if args.print_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Autofill status: {result['status']}")
        print(f"Report: {result['report_path']}")
    return 0 if result["status"] in {"ready_for_director_review", "structural_pass_external_pending"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
