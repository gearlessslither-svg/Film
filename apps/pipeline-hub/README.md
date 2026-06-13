# Pipeline Hub GUI Scope

`pipeline-hub` 是本地 AIGC 影视流程总控台。当前版本已经提供最小可用 GUI 和后端 API，用同一套项目结构、脚手架脚本、验证脚本和分析脚本驱动项目。

## Run

```powershell
python apps/pipeline-hub/server.py --host 127.0.0.1 --port 8787
```

打开：

```text
http://127.0.0.1:8787
```

## First Screen

总控台打开后应直接进入项目工作台，而不是展示介绍页。

核心入口：

- 新建项目
- 打开现有项目
- 导入旧项目文件夹
- 预览剧本、故事文档、图片、视频、音频和 3D/Blender 资源
- 分析当前项目
- 检查项目结构
- 查看阶段进度
- 进入镜头生产

## Minimum Useful Version

第一版 GUI 已覆盖这些事：

1. 调用 `scripts/create_aigc_project.py` 创建新项目。
2. 读取 `projects/<slug>/project.yaml` 显示阶段进度。
3. 读取和编辑 `assets_link_map.md`，把旧项目素材映射到标准阶段目录。
4. 打开每个阶段文件夹，并显示该阶段的必需文件是否存在。
5. 读取 `07_shots/shot_list.csv`，显示镜头列表和状态。
6. 调用 `scripts/validate_aigc_project.py` 运行结构检查，提示缺失目录、缺失清单、大文件 Git LFS 风险、`.rar` 风险。
7. 调用 `scripts/analyze_aigc_project.py` 运行项目资产与审美体检，并打开 `10_qa/reports/project_audit_latest.md`。
8. 读取 `projects/<slug>/` 和 `resource_root`，显示文档阅读器、视觉画廊、视频/音频预览和资源清单。

## API Contract

- `GET /api/projects`: 列出项目。
- `POST /api/projects`: 创建项目。
- `GET /api/projects/<slug>`: 读取项目详情、阶段状态、镜头表、验证结果和分析报告。
- `GET /api/projects/<slug>/asset?origin=<project|resource>&path=<path>`: 在安全根目录内读取预览资源。
- `POST /api/projects/<slug>/validate`: 运行结构检查。
- `POST /api/projects/<slug>/analyze`: 运行项目资产与审美体检。
- `POST /api/projects/<slug>/autofill`: 运行受控自治补全，补齐安全本地产物，并按配置排队或执行 Codex/image2/Blender/plugin 适配器任务。
- `POST /api/projects/<slug>/links`: 更新旧项目目录和资源目录映射。

## Analyze Current Project Button

按钮行为：

```powershell
python scripts/analyze_aigc_project.py projects/<project-slug> --sample-size 24 --print-json
```

输出：

- 机器可读摘要: 命令行 JSON。
- 人类可读报告: `projects/<project-slug>/10_qa/reports/project_audit_latest.md`。
- AI 审片入口: 使用 `$aigc-film-project-auditor` 读取报告并结合电影审美 Rubric 生成导演建议。

## Autofill Button

按钮行为：

```powershell
python scripts/autofill_aigc_project.py projects/<project-slug> --max-rounds 3 --sample-size 24 --print-json
```

自治补全会循环执行 analyze -> fill -> analyze，直到确定性审计达到 `pass` 或达到轮次预算。默认只写安全本地产物：缺失文档、CSV、索引、提示词草稿、任务队列、配置、QA 记录和运行报告。Codex、image2、Blender 或 plugin install 只有在 `00_admin/autofill_config.yaml` 里启用，并且 GUI/API 请求允许时才会执行。

输出：

- 机器摘要: 命令行 JSON。
- 运行报告: `projects/<project-slug>/10_qa/autofill_runs/autofill_latest.md`。
- 适配器任务提示词: `projects/<project-slug>/10_qa/autofill_runs/<run-id>/tasks/`。
- 项目日志记录: `00_admin/project_log.md`。

## Coin Slot Sample Seed

投币口样板可通过脚本重建 12 镜头标准批次：

```powershell
python scripts/seed_coin_slot_sample_project.py --force
python scripts/analyze_aigc_project.py projects/coin-slot --sample-size 24
```

脚本会把链接资源库中的代表性 panels/prompts/stage maps 转成标准项目内的 story、lookdev、asset bible、previs、shots、generation、edit、QA 和 delivery 索引。

## Later Modules

- Intake Analyzer: 分析导演输入、截图、视频和参考图。
- Direction Board: 展示故事方向、美术方向、风格预览和导演确认状态。
- Asset Bible Manager: 管理角色、场景、道具、颜色、光照和连续性锁定。
- Previs Builder: 管理 Blender 白模、相机、控制层和空间关系 QA。
- Shot Factory: 批量生成关键帧、图片提示词、视频提示词和模型任务。
- QA Console: 汇总角色一致性、空间一致性、白模匹配、交付完整性。

## Implementation Note

GUI 应调用脚本或共享库，不要重新实现另一套项目结构规则。项目目录契约以 `docs/PROJECT_STRUCTURE.md` 和 `scripts/create_aigc_project.py` 为准。
