# AIGC Project Folder Contract / AIGC 项目文件夹规范

本文档定义总控台、Skill、脚本和人工导演共同遵守的项目文件夹格式。目标是让每个 AIGC 影视项目都能按同一套阶段归拢资产、记录决策、批量产出，并且可以被 GUI 工具稳定读取。
This document defines the project folder contract shared by the control hub, the Skill, the scripts, and human directors. The goal is that every AIGC film project organizes assets, records decisions, and produces output along the same set of stages, and can be read reliably by the GUI tools.

## Core Rule / 核心规则

一个项目等于 `projects/<project-slug>/` 下的一个大文件夹。
A project is one top-level folder under `projects/<project-slug>/`.

例如"投币口"样板项目为 / For example, the *Coin Slot* sample project is:

```text
projects/coin-slot/
```

项目显示名可以是中文，例如 `投币口`；项目目录名使用稳定英文 slug，例如 `coin-slot`。这样既方便导演阅读，也方便 Git、脚本、GUI 和外部模型调用。
The display name can be Chinese (e.g. `投币口`); the directory name uses a stable English slug (e.g. `coin-slot`). This stays readable for directors while remaining friendly to Git, scripts, the GUI, and external model calls.

## Create A New Project / 新建项目

```powershell
python scripts/create_aigc_project.py --name "新项目名" --slug new-project
```

如果项目名没有英文 slug，可以手动指定 `--slug`。脚本会创建标准目录、`project.yaml`、导演简报、模型配置、镜头表、资源映射表和阶段占位文件。
If the name has no English slug, pass `--slug` manually. The script creates the standard directories, `project.yaml`, the director brief, model config, shot list, resource map, and stage placeholder files.

创建后可以运行结构检查 / After creating, run a structure check:

```powershell
python scripts/validate_aigc_project.py projects/new-project
```

用于归拢旧项目时，可以额外登记源目录和资源目录 / When folding in an old project, you can also register its source and resource roots:

```powershell
python scripts/create_aigc_project.py `
  --name "投币口" `
  --slug coin-slot `
  --source-root "E:\视觉\投币口" `
  --resource-root "resources/examples/coin-slot"
```

## Standard Folder Layout / 标准目录结构

```text
00_admin/        项目控制、导演意图、模型配置、流程日志 / control, intent, model config, process log
01_intake/       点子、截图、视频、参考图、AI 分析 / ideas, screenshots, video, references, AI analysis
02_direction/    创意方向方案、审批记录、最终方向 / direction options, approvals, final direction
03_story/        大纲、剧本、场次、节拍、台词 / outline, script, scenes, beats, dialogue
04_lookdev/      风格预览、色彩、光照、美术参考 / style tests, color, light, art references
05_asset_bible/  人设、场景、道具、连续性锁定 / characters, scenes, props, continuity locks
06_previs/       白模、机位、控制层、空间关系 QA / whitebox, cameras, control layers, spatial QA
07_shots/        镜头表、关键帧、图片提示词、视频提示词 / shot list, keyframes, image/video prompts
08_generation/   批量生成任务、图片/视频输出、废片 / batch jobs, image/video output, rejects
09_edit/         粗剪、音频、字幕、调色 / rough cut, audio, subtitles, grading
10_qa/           QA 报告、修复队列、一致性检查 / QA reports, fix queue, consistency checks
11_delivery/     最终导出、交付包、交付清单 / final exports, delivery packages, checklist
```

## Files The GUI Should Read / GUI 需要读取的文件

- `project.yaml`: 项目元数据、阶段顺序、当前状态、模型策略、资产策略。
  - Project metadata, stage order, current status, model policy, asset policy.
- `00_admin/director_brief.md`: 导演最初输入、保留项、可探索项、禁止方向。
  - The director's initial input, must-keeps, things to explore, forbidden directions.
- `00_admin/model_config.yaml`: 本地模型和远程模型的双保险路由，不写入密钥。
  - Dual-fallback routing for local and remote models; no secrets stored.
- `00_admin/project_log.md`: 每次方向确认、阶段推进、模型切换、重要返工都记录在这里。
  - Every direction approval, stage advance, model switch, and major rework is logged here.
- `assets_link_map.md`: 旧工程、大素材、LFS 归档和当前项目目录的映射关系。
  - Mapping between old projects, large assets, LFS archives, and the current project directory.
- `07_shots/shot_list.csv`: 镜头级生产表，后续可驱动 Blender、图片模型、视频模型和 QA 工具。
  - Shot-level production table that can drive Blender, image models, video models, and QA tools.
- `10_qa/reports/project_audit_latest.md`: 一键项目分析报告，覆盖阶段资产、抽样结果、缺失项、审美风险和下一批建议。
  - One-click project analysis report covering stage assets, sampling results, gaps, aesthetic risks, and next-batch suggestions.

## Stage Gates / 阶段门禁

1. `01_intake` 必须先完成输入归档和 AI 分析，才能进入方向提案。
   - `01_intake` must finish input archiving and AI analysis before direction proposals.
2. `02_direction` 必须有导演确认记录，才能批量产出故事和美术前置资源。
   - `02_direction` needs a recorded director approval before mass-producing story and art pre-assets.
3. `05_asset_bible` 必须锁定角色、场景、道具、色彩和连续性规则，才能进入大规模镜头生成。
   - `05_asset_bible` must lock characters, scenes, props, color, and continuity rules before large-scale shot generation.
4. `06_previs` 需要输出白模、镜头机位和控制层；如果白模不够精致，要进入 `10_qa/fix_queue/`，不能直接跳过。
   - `06_previs` must produce whitebox, cameras, and control layers; weak whiteboxes go to `10_qa/fix_queue/`, never skipped.
5. `07_shots` 的每个镜头必须有关键帧路径、提示词路径、空间关系说明和状态字段。
   - Every shot in `07_shots` needs a keyframe path, prompt path, spatial note, and status field.
6. `08_generation` 的输出需要保留任务记录，废片进入 `rejects/`，避免反复踩同一个问题。
   - `08_generation` output keeps job records; rejects go to `rejects/` so the same mistakes are not repeated.
7. `11_delivery` 只放最终可交付内容和交付清单。
   - `11_delivery` holds only final deliverables and the delivery checklist.

## Asset Policy / 资产策略

- `.rar` 不进入 Git。
  - `.rar` never enters Git.
- 图片、视频、音频、Blender、PSD、EXR、FBX、GLB 等生产素材通过 Git LFS 管理。
  - Production media (images, video, audio, Blender, PSD, EXR, FBX, GLB) is managed via Git LFS.
- 从旧工程引用的大文件优先登记在 `assets_link_map.md`，避免为了样板项目重复复制素材。
  - Large files referenced from old projects are registered in `assets_link_map.md` to avoid duplicating media for the sample.
- 如果某个素材是当前项目的正式资产，可以放入对应阶段目录；如果只是历史参考，可以保留在 `resources/examples/<slug>/media/` 或外部源目录。
  - Formal assets of the current project go in the matching stage folder; historical references stay in `resources/examples/<slug>/media/` or an external source directory.

## GUI Hub Behavior / 总控台行为

总控台至少应提供这些项目级功能 / The hub should provide at least these project-level features:

- 创建新项目: 输入项目名和 slug，调用 `scripts/create_aigc_project.py`。
  - Create a project: enter name and slug, calling `scripts/create_aigc_project.py`.
- 导入旧项目: 选择旧文件夹，写入 `assets_link_map.md`，按阶段建议归拢。
  - Import an old project: pick the old folder, write `assets_link_map.md`, and suggest a stage layout.
- 阶段面板: 每个阶段只显示本阶段目录、必需文件、待确认项和 QA 状态。
  - Stage panels: each stage shows only its directory, required files, pending approvals, and QA status.
- 模型路由: 从 `00_admin/model_config.yaml` 读取本地/远程模型配置，记录 fallback 原因。
  - Model routing: read local/remote model config from `00_admin/model_config.yaml` and record fallback reasons.
- 镜头生产: 读取 `07_shots/shot_list.csv`，批量生成关键帧、提示词、视频任务和 QA 队列。
  - Shot production: read `07_shots/shot_list.csv` and batch-generate keyframes, prompts, video jobs, and QA queues.
- 项目健康检查: 检查缺失目录、缺失清单、未确认阶段、未入 LFS 的大文件和 `.rar` 风险。
  - Project health check: detect missing directories, missing manifests, unconfirmed stages, large non-LFS files, and `.rar` risk.
- 项目资产与审美体检: 调用 `scripts/analyze_aigc_project.py`，抽样检查当前项目和链接资源，输出缺失项与电影制作建议。
  - Asset and aesthetic review: call `scripts/analyze_aigc_project.py` to sample the project and linked resources and output gaps plus filmmaking suggestions.
- 自治补全: 调用 `scripts/autofill_aigc_project.py`，循环分析并补齐缺失的安全本地产物；Codex、image2、Blender 和插件安装通过 `00_admin/autofill_config.yaml` 作为显式适配器接入。
  - Autonomous fill: call `scripts/autofill_aigc_project.py` to loop analyze-and-fill for safe local artifacts; Codex, image2, Blender, and plugin installs plug in as explicit adapters via `00_admin/autofill_config.yaml`.

当前可先调用 `scripts/validate_aigc_project.py` 完成最小结构检查，后续再扩展更细的镜头、模型和资产 QA。
For now, run `scripts/validate_aigc_project.py` for the minimal structure check, then extend finer shot/model/asset QA later.

当前可调用 `scripts/analyze_aigc_project.py projects/<slug>` 输出 `10_qa/reports/project_audit_latest.md`，再由 `$aigc-film-project-auditor` Skill 进行导演级审美和工业流程建议。
Run `scripts/analyze_aigc_project.py projects/<slug>` to produce `10_qa/reports/project_audit_latest.md`, then let the `$aigc-film-project-auditor` skill give director-level aesthetic and pipeline advice.

当前也可调用 `scripts/autofill_aigc_project.py projects/<slug> --max-rounds 3` 输出 `10_qa/autofill_runs/autofill_latest.md`。默认模式只写可审计的文档、CSV、索引和任务队列；外部生成、Blender 执行和插件安装必须在项目配置中启用并由运行参数允许。
Run `scripts/autofill_aigc_project.py projects/<slug> --max-rounds 3` to produce `10_qa/autofill_runs/autofill_latest.md`. The default mode only writes auditable docs, CSVs, indexes, and task queues; external generation, Blender execution, and plugin installs must be enabled in project config and allowed by run flags.

## Run The Local Hub / 启动本地总控台

```powershell
python apps/pipeline-hub/server.py --host 127.0.0.1 --port 8787
```

本地打开 `http://127.0.0.1:8787` 后，可以直接对 `projects/coin-slot/` 执行验证、分析、资源链接和报告查看。
Open `http://127.0.0.1:8787` locally to validate, analyze, link resources, and view reports for `projects/coin-slot/` directly.
