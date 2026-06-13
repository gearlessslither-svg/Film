#!/usr/bin/env python3
"""Create a standardized AIGC film project folder.

The script is intentionally dependency-free so a future GUI hub can call the
same project scaffold contract without needing a Python environment beyond the
standard library.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path


STAGES = [
    ("00_admin", "Project control, director intent, model routing, and logs"),
    ("01_intake", "Source ideas, reference media, screenshots, footage, and analysis"),
    ("02_direction", "Creative options, approvals, and final direction lock"),
    ("03_story", "Outline, script, beats, scene structure, and dialogue"),
    ("04_lookdev", "Styleframes, color, lighting, visual references, and preview tests"),
    ("05_asset_bible", "Characters, locations, props, continuity locks, and asset rules"),
    ("06_previs", "Whitebox, camera, control layers, spatial QA, and Blender work"),
    ("07_shots", "Shot list, keyframe prompts, video prompts, and shot-level manifests"),
    ("08_generation", "Image/video generation jobs, outputs, rejects, and iteration records"),
    ("09_edit", "Rough cut, audio, subtitles, color, and editorial assembly"),
    ("10_qa", "QA reports, fix queue, consistency checks, and acceptance notes"),
    ("11_delivery", "Final exports, packages, manifests, and delivery records"),
]


DIRECTORIES = [
    "00_admin",
    "01_intake/source_inputs",
    "01_intake/references",
    "01_intake/analysis",
    "02_direction/options",
    "02_direction/approvals",
    "03_story/outlines",
    "03_story/scripts",
    "03_story/beats",
    "04_lookdev/styleframes",
    "04_lookdev/palettes",
    "04_lookdev/lighting",
    "04_lookdev/references",
    "05_asset_bible/characters",
    "05_asset_bible/character_stage_locks",
    "05_asset_bible/locations",
    "05_asset_bible/props",
    "05_asset_bible/continuity",
    "06_previs/blender",
    "06_previs/camera_manifests",
    "06_previs/renders",
    "06_previs/control_layers/depth",
    "06_previs/control_layers/line",
    "06_previs/control_layers/normal",
    "06_previs/control_layers/segmentation",
    "06_previs/qa",
    "07_shots/keyframes",
    "07_shots/prompts",
    "07_shots/video_prompts",
    "08_generation/jobs",
    "08_generation/outputs/images",
    "08_generation/outputs/video",
    "08_generation/rejects",
    "09_edit/rough_cut",
    "09_edit/audio",
    "09_edit/subtitles",
    "09_edit/color",
    "10_qa/reports",
    "10_qa/fix_queue",
    "11_delivery/exports",
    "11_delivery/packages",
    "11_delivery/manifests",
]


TEXT_TEMPLATES = {
    "README.md": """# {{PROJECT_NAME}}

这是一个按工业化 AIGC 影视流程归拢的项目文件夹。

- 项目代号: `{{PROJECT_SLUG}}`
- 项目状态: active
- 当前阶段: `01_intake`
- 原始项目位置: {{SOURCE_ROOT_TEXT}}
- 外部/样例资源: {{RESOURCE_ROOT_TEXT}}

## 使用方式

1. 导演把点子、截图、视频、参考图放入 `01_intake/source_inputs/` 或 `01_intake/references/`。
2. AI 分析结果写入 `01_intake/analysis/`，并同步更新 `project.yaml` 的阶段状态。
3. 创意方向确认后，把故事、美术、角色、场景、道具、灯光等前置资源分别放入 `03_story/`、`04_lookdev/`、`05_asset_bible/`。
4. 白模、镜头机位、ControlNet/深度/线稿/法线/分割等控制层放入 `06_previs/`。
5. 关键分镜、图像提示词、视频提示词和镜头清单放入 `07_shots/`。
6. 点击“分析当前项目”或运行 `scripts/analyze_aigc_project.py`，在 `10_qa/reports/` 输出缺失项和审美风险报告。
7. 批量生成、剪辑、QA 和交付分别进入 `08_generation/` 到 `11_delivery/`。

## 总控台读取约定

- `project.yaml`: 项目元数据、阶段顺序、模型策略、资产策略。
- `assets_link_map.md`: 外部旧目录、LFS 资源、参考资料和大文件映射。
- `07_shots/shot_list.csv`: 镜头级任务表，后续可被 GUI、Blender、图片模型和视频模型共同读取。
- 每个阶段目录只放本阶段的“产物”和“决策证据”，临时缓存不进入 Git。
""",
    "project.yaml": """schema_version: 1
project:
  name: {{PROJECT_NAME_JSON}}
  slug: {{PROJECT_SLUG_JSON}}
  created_at: {{CREATED_AT_JSON}}
  status: "active"
  source_root: {{SOURCE_ROOT_JSON}}
  resource_root: {{RESOURCE_ROOT_JSON}}
pipeline:
  current_stage: "01_intake"
  stage_order:
{{STAGE_ORDER_YAML}}
models:
  config: "00_admin/model_config.yaml"
  fallback_policy: "local_first_remote_fallback"
storage:
  large_asset_policy: "Use Git LFS for production media; do not commit .rar archives."
  link_map: "assets_link_map.md"
gui_contract:
  project_manifest: "project.yaml"
  shot_table: "07_shots/shot_list.csv"
  director_brief: "00_admin/director_brief.md"
  project_log: "00_admin/project_log.md"
  audit_report: "10_qa/reports/project_audit_latest.md"
  autofill_report: "10_qa/autofill_runs/autofill_latest.md"
""",
    "00_admin/director_brief.md": """# Director Brief

## 核心点子

-

## 必须保留

-

## 可以探索

-

## 禁止方向

-

## 参考输入

- 文本:
- 图片:
- 视频:
- 其他:
""",
    "00_admin/model_config.yaml": """schema_version: 1
policy:
  routing: "local_first_remote_fallback"
  secrets_rule: "Do not commit API keys or private tokens."
local_models:
  text_analysis:
    provider: "local"
    endpoint: ""
    model: ""
  vision_analysis:
    provider: "local"
    endpoint: ""
    model: ""
remote_models:
  text_analysis:
    provider: ""
    model: ""
  image_generation:
    provider: ""
    model: ""
  video_generation:
    provider: ""
    model: ""
fallback:
  when_local_unavailable: "Use remote model after recording the reason in 00_admin/project_log.md."
  when_remote_unavailable: "Continue with local draft outputs and mark outputs as provisional."
""",
    "00_admin/autofill_config.yaml": """schema_version: 1
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
""",
    "00_admin/project_log.md": """# Project Log

| Date | Stage | Decision / Change | Owner | Evidence |
| --- | --- | --- | --- | --- |
| {{TODAY}} | 00_admin | Project scaffold created. | AI | project.yaml |
""",
    "02_direction/creative_brief.md": """# Creative Brief

## 最终方向

-

## 故事大纲

-

## 美术风格

-

## 角色 / 场景 / 道具优先级

-

## 确认记录

-
""",
    "07_shots/shot_list.csv": (
        "shot_id,sequence,story_beat,duration_sec,aspect_ratio,location,"
        "character_stage_lock,start_frame,end_frame,camera,action,lighting,"
        "continuity_lock,prompt_path,status\n"
    ),
    "assets_link_map.md": """# Asset Link Map

这个文件记录“项目文件夹”和外部旧资源之间的关系。总控台可以读取这里，把历史素材映射到当前项目阶段。

## Project

- Project name: {{PROJECT_NAME}}
- Project slug: `{{PROJECT_SLUG}}`
- Source root: {{SOURCE_ROOT_TEXT}}
- Resource root: {{RESOURCE_ROOT_TEXT}}

## Suggested mappings

| Current project area | External/source location | Notes |
| --- | --- | --- |
| `01_intake/source_inputs/` | {{SOURCE_ROOT_TEXT}} | 原始导演输入、旧工程资料、临时输入。 |
| `03_story/` | {{RESOURCE_ROOT_TEXT}}/docs | 故事、分镜、制作文档。 |
| `06_previs/blender/` | {{RESOURCE_ROOT_TEXT}}/blender | 白模、Blender 脚本、空间关系验证。 |
| `07_shots/` | {{RESOURCE_ROOT_TEXT}}/csv | 镜头表、生成表、QA 表。 |
| `08_generation/outputs/` | {{RESOURCE_ROOT_TEXT}}/media | 已归档的图片、视频、音频样例素材。 |

## Large asset rule

- `.rar` 不进入 Git。
- 图片、视频、音频、Blender、压缩包等生产素材如需入库，必须走 Git LFS。
- 如果只是引用旧素材，优先在这里登记路径，避免重复复制大文件。
""",
}


def json_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", name).strip("-").lower()
    slug = re.sub(r"-{2,}", "-", slug)
    if slug:
        return slug[:64].strip("-")
    return "project-" + datetime.now().strftime("%Y%m%d-%H%M%S")


def validate_slug(slug: str, *, allow_template: bool = False) -> None:
    if allow_template and slug == "_template":
        return
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", slug):
        raise ValueError(
            "Slug must use lowercase letters, numbers, and hyphens, "
            "and must start with a letter or number."
        )


def stage_order_yaml() -> str:
    lines = []
    for stage_id, description in STAGES:
        lines.append(f'    - id: "{stage_id}"')
        lines.append(f'      description: "{description}"')
    return "\n".join(lines)


def render_template(template: str, values: dict[str, str]) -> str:
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    return rendered


def write_text_if_missing(path: Path, text: str, *, force: bool) -> bool:
    if path.exists() and not force:
        return False
    if path.exists() and force:
        # Existing project data is user work. Force only fills missing files.
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def create_project(args: argparse.Namespace) -> dict[str, object]:
    root = Path(args.root).expanduser().resolve()

    if args.template:
        name = "{{PROJECT_NAME}}"
        slug = "_template"
        source_root = "{{SOURCE_ROOT}}"
        resource_root = "{{RESOURCE_ROOT}}"
        created_at = "{{CREATED_AT}}"
    else:
        if not args.name:
            raise ValueError("--name is required unless --template is used.")
        name = args.name.strip()
        slug = args.slug.strip() if args.slug else slugify(name)
        source_root = args.source_root.strip()
        resource_root = args.resource_root.strip()
        created_at = datetime.now().astimezone().isoformat(timespec="seconds")

    validate_slug(slug, allow_template=args.template)

    target = root / slug
    if target.exists() and not args.force:
        raise FileExistsError(
            f"Project already exists: {target}. Use --force to fill missing files."
        )

    target.mkdir(parents=True, exist_ok=True)

    for directory in DIRECTORIES:
        current = target / directory
        current.mkdir(parents=True, exist_ok=True)
        gitkeep = current / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.write_text("", encoding="utf-8")

    today = datetime.now().strftime("%Y-%m-%d")
    values = {
        "PROJECT_NAME": name,
        "PROJECT_SLUG": slug,
        "PROJECT_NAME_JSON": json_string(name),
        "PROJECT_SLUG_JSON": json_string(slug),
        "CREATED_AT_JSON": json_string(created_at),
        "SOURCE_ROOT_JSON": json_string(source_root),
        "RESOURCE_ROOT_JSON": json_string(resource_root),
        "SOURCE_ROOT_TEXT": source_root if source_root else "(not linked yet)",
        "RESOURCE_ROOT_TEXT": resource_root if resource_root else "(not linked yet)",
        "STAGE_ORDER_YAML": stage_order_yaml(),
        "TODAY": today,
    }

    written_files = []
    skipped_files = []
    for relative_path, template in TEXT_TEMPLATES.items():
        destination = target / relative_path
        rendered = render_template(template, values)
        if write_text_if_missing(destination, rendered, force=args.force):
            written_files.append(str(destination))
        else:
            skipped_files.append(str(destination))

    return {
        "project_path": str(target),
        "project_name": name,
        "project_slug": slug,
        "written_files": written_files,
        "skipped_existing_files": skipped_files,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create a standardized AIGC film project folder."
    )
    parser.add_argument("--name", help="Human-readable project name, e.g. 投币口")
    parser.add_argument(
        "--slug",
        help="Stable folder name. Use lowercase letters, numbers, and hyphens.",
    )
    parser.add_argument(
        "--root",
        default="projects",
        help="Project root directory. Default: projects",
    )
    parser.add_argument(
        "--source-root",
        default="",
        help="Existing source folder to record in assets_link_map.md.",
    )
    parser.add_argument(
        "--resource-root",
        default="",
        help="Existing curated resource folder to record in assets_link_map.md.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow target folder to exist and fill missing folders/files only.",
    )
    parser.add_argument(
        "--template",
        action="store_true",
        help="Create projects/_template with placeholder metadata.",
    )
    parser.add_argument(
        "--print-json",
        action="store_true",
        help="Print machine-readable JSON for GUI callers.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        result = create_project(args)
    except Exception as exc:  # noqa: BLE001 - CLI should report any setup error cleanly.
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.print_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Project path: {result['project_path']}")
        print(f"Project name: {result['project_name']}")
        print(f"Project slug: {result['project_slug']}")
        print(f"Written files: {len(result['written_files'])}")
        print(f"Existing files kept: {len(result['skipped_existing_files'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
