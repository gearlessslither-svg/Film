# Pipeline Hub GUI Scope / Pipeline Hub 总控台范围

`pipeline-hub` 是本地 AIGC 影视流程总控台。当前版本已经提供最小可用 GUI 和后端 API，用同一套项目结构、脚手架脚本、验证脚本和分析脚本驱动项目。
`pipeline-hub` is the local control hub for the AIGC film pipeline. The current version ships a minimal usable GUI and a backend API that drive projects with one shared project structure, scaffolding scripts, validation scripts, and analysis scripts.

## Run / 启动

```powershell
python apps/pipeline-hub/server.py --host 127.0.0.1 --port 8787
```

打开 / Open:

```text
http://127.0.0.1:8787
```

## First Screen / 首屏

总控台打开后应直接进入项目工作台，而不是展示介绍页。
On open, the hub goes straight to the project workspace rather than an intro page.

核心入口 / Core entry points:

- 新建项目 / New project
- 打开现有项目 / Open an existing project
- 导入旧项目文件夹 / Import an old project folder
- 预览剧本、故事文档、图片、视频、音频和 3D/Blender 资源 / Preview scripts, story docs, images, video, audio, and 3D/Blender assets
- 分析当前项目 / Analyze the current project
- 检查项目结构 / Check project structure
- 查看阶段进度 / View stage progress
- 进入镜头生产 / Enter shot production

## Minimum Useful Version / 最小可用版本

第一版 GUI 已覆盖这些事 / The first GUI version already covers:

1. 调用 `scripts/create_aigc_project.py` 创建新项目。/ Create a project via `scripts/create_aigc_project.py`.
2. 读取 `projects/<slug>/project.yaml` 显示阶段进度。/ Read `projects/<slug>/project.yaml` to show stage progress.
3. 读取和编辑 `assets_link_map.md`，把旧项目素材映射到标准阶段目录。/ Read and edit `assets_link_map.md` to map old assets into standard stage folders.
4. 打开每个阶段文件夹，并显示该阶段的必需文件是否存在。/ Open each stage folder and show whether its required files exist.
5. 读取 `07_shots/shot_list.csv`，显示镜头列表和状态。/ Read `07_shots/shot_list.csv` and show the shot list and status.
6. 调用 `scripts/validate_aigc_project.py` 运行结构检查，提示缺失目录、缺失清单、大文件 Git LFS 风险、`.rar` 风险。/ Run `scripts/validate_aigc_project.py` for the structure check, flagging missing dirs, missing manifests, large-file Git LFS risk, and `.rar` risk.
7. 调用 `scripts/analyze_aigc_project.py` 运行项目资产与审美体检，并打开 `10_qa/reports/project_audit_latest.md`。/ Run `scripts/analyze_aigc_project.py` for the asset/aesthetic review and open `10_qa/reports/project_audit_latest.md`.
8. 读取 `projects/<slug>/` 和 `resource_root`，显示文档阅读器、视觉画廊、视频/音频预览和资源清单。/ Read `projects/<slug>/` and `resource_root` to show the doc reader, visual gallery, video/audio preview, and resource list.

## API Contract / API 约定

- `GET /api/projects`: 列出项目。/ List projects.
- `POST /api/projects`: 创建项目。/ Create a project.
- `GET /api/projects/<slug>`: 读取项目详情、阶段状态、镜头表、验证结果和分析报告。/ Read project detail, stage status, shot table, validation, and analysis report.
- `GET /api/projects/<slug>/asset?origin=<project|resource>&path=<path>`: 在安全根目录内读取预览资源。/ Read a preview asset within the safe root.
- `POST /api/projects/<slug>/validate`: 运行结构检查。/ Run the structure check.
- `POST /api/projects/<slug>/analyze`: 运行项目资产与审美体检。/ Run the asset/aesthetic review.
- `POST /api/projects/<slug>/autofill`: 运行受控自治补全，补齐安全本地产物，并按配置排队或执行 Codex/image2/Blender/plugin 适配器任务。/ Run controlled autofill for safe local artifacts and queue/execute Codex/image2/Blender/plugin adapter tasks per config.
- `POST /api/projects/<slug>/links`: 更新旧项目目录和资源目录映射。/ Update the old-project and resource directory mapping.

## Analyze Current Project Button / "分析当前项目"按钮

按钮行为 / Button behavior:

```powershell
python scripts/analyze_aigc_project.py projects/<project-slug> --sample-size 24 --print-json
```

输出 / Output:

- 机器可读摘要: 命令行 JSON。/ Machine-readable summary: stdout JSON.
- 人类可读报告: `projects/<project-slug>/10_qa/reports/project_audit_latest.md`。/ Human-readable report at that path.
- AI 审片入口: 使用 `$aigc-film-project-auditor` 读取报告并结合电影审美 Rubric 生成导演建议。/ AI review entry: `$aigc-film-project-auditor` reads the report and applies a cinematic rubric to produce director notes.

## Autofill Button / "自治补全"按钮

按钮行为 / Button behavior:

```powershell
python scripts/autofill_aigc_project.py projects/<project-slug> --max-rounds 3 --sample-size 24 --print-json
```

自治补全会循环执行 analyze -> fill -> analyze，直到确定性审计达到 `pass` 或达到轮次预算。默认只写安全本地产物：缺失文档、CSV、索引、提示词草稿、任务队列、配置、QA 记录和运行报告。Codex、image2、Blender 或 plugin install 只有在 `00_admin/autofill_config.yaml` 里启用，并且 GUI/API 请求允许时才会执行。
Autofill loops analyze -> fill -> analyze until the deterministic audit reaches `pass` or the round budget is hit. By default it only writes safe local artifacts: missing docs, CSVs, indexes, prompt drafts, task queues, configs, QA records, and run reports. Codex, image2, Blender, or plugin install only run when enabled in `00_admin/autofill_config.yaml` and allowed by the GUI/API request.

输出 / Output:

- 机器摘要: 命令行 JSON。/ Machine summary: stdout JSON.
- 运行报告: `projects/<project-slug>/10_qa/autofill_runs/autofill_latest.md`。/ Run report at that path.
- 适配器任务提示词: `projects/<project-slug>/10_qa/autofill_runs/<run-id>/tasks/`。/ Adapter task prompts under that folder.
- 项目日志记录: `00_admin/project_log.md`。/ Logged into `00_admin/project_log.md`.

## Coin Slot Sample Seed / 投币口样板种子

投币口样板可通过脚本重建 12 镜头标准批次 / The Coin Slot sample can rebuild a 12-shot standard batch:

```powershell
python scripts/seed_coin_slot_sample_project.py --force
python scripts/analyze_aigc_project.py projects/coin-slot --sample-size 24
```

脚本会把链接资源库中的代表性 panels/prompts/stage maps 转成标准项目内的 story、lookdev、asset bible、previs、shots、generation、edit、QA 和 delivery 索引。
The script turns representative panels/prompts/stage maps from the linked resource library into standard in-project indexes for story, lookdev, asset bible, previs, shots, generation, edit, QA, and delivery.

## Later Modules / 后续模块

- Intake Analyzer: 分析导演输入、截图、视频和参考图。/ Analyze director input, screenshots, video, and references.
- Direction Board: 展示故事方向、美术方向、风格预览和导演确认状态。/ Show story/art directions, style tests, and approval status.
- Asset Bible Manager: 管理角色、场景、道具、颜色、光照和连续性锁定。/ Manage characters, scenes, props, color, light, and continuity locks.
- Previs Builder: 管理 Blender 白模、相机、控制层和空间关系 QA。/ Manage Blender whiteboxes, cameras, control layers, and spatial QA.
- Shot Factory: 批量生成关键帧、图片提示词、视频提示词和模型任务。/ Batch-generate keyframes, image prompts, video prompts, and model jobs.
- QA Console: 汇总角色一致性、空间一致性、白模匹配、交付完整性。/ Aggregate character consistency, spatial consistency, whitebox match, and delivery completeness.

## Implementation Note / 实现说明

GUI 应调用脚本或共享库，不要重新实现另一套项目结构规则。项目目录契约以 `docs/PROJECT_STRUCTURE.md` 和 `scripts/create_aigc_project.py` 为准。
The GUI should call the scripts or a shared library, not reimplement another set of project-structure rules. The directory contract is defined by `docs/PROJECT_STRUCTURE.md` and `scripts/create_aigc_project.py`.
