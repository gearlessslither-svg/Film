# Content Catalog / 内容索引

这个仓库按用途分为四类，避免工具、skill、案例文档和生成资料混在一起。
This repo is split into four categories by purpose, so tools, skills, case-study docs, and generated material do not get mixed together.

## Skills

- `skills/aigc-film-pipeline/SKILL.md`
  - Codex skill 主入口。/ Main entry of the Codex skill.
  - 负责继续、规划、QA 或打包 AIGC-first 短片项目。/ Continues, plans, QAs, or packages AIGC-first short film projects.
- `skills/aigc-film-pipeline/references/`
  - skill 按需读取的流程规则。/ Process rules the skill reads on demand.
  - 覆盖故事阶段连续性、人物相似度 QA、白模 QA、pure/annotated 双版本、音频规划、续跑恢复等。/ Covers story-stage continuity, character-similarity QA, whitebox QA, pure/annotated dual versions, audio planning, resume recovery, and more.

## Tools / 工具

- `scripts/validate_pipeline_state.py`
  - 项目状态和生产门禁校验。/ Validates project state and production gates.
- `scripts/visual/`
  - 白模 QA、相似度检测、联系表、pure 图结果标记、annotated 版本生成、最终分镜表重建、音频 guide、animatic、最终视频和交付校验。/ Whitebox QA, similarity detection, contact sheets, pure-image result marking, annotated version generation, final storyboard rebuild, audio guide, animatic, final video, and delivery validation.
  - Arcade 场景专用工具：mother OBJ 白模、camera whiteboxes、formal prompt pack、crowd/camera-subject 修正脚本。/ Arcade-scene specific tools: mother OBJ whitebox, camera whiteboxes, formal prompt pack, crowd/camera-subject fix scripts.
- `scripts/blender/`
  - Blender 白模生成与渲染工具。/ Blender whitebox generation and rendering tools.
- `scripts/keep-codex-awake.ps1`
  - Windows 长任务防睡眠辅助工具。/ Windows keep-awake helper for long-running tasks.

## Docs / 文档

- `README.md`
  - 仓库入口和常用命令。/ Repo entry and common commands.
- `docs/CONTENT_CATALOG.md`
  - 当前分类索引。/ This category index.
- `resources/examples/coin-slot/docs/project/`
  - 原项目总览和任务日志。/ Original project overview and task log.
- `resources/examples/coin-slot/docs/aigc/`
  - 《投币口》AIGC 全流程文档，从规则、视觉圣经、分镜、提示词、白模、音频、QA 到交付。/ The full *Coin Slot* AIGC pipeline docs: rules, visual bible, storyboard, prompts, whitebox, audio, QA, delivery.
  - 已补入镜头-主体逻辑规则 `34_camera_subject_logic_rules.md`。/ Added the camera-subject logic rules `34_camera_subject_logic_rules.md`.
- `resources/examples/coin-slot/docs/normal-shooting/`
  - 同一故事的常规拍摄版翻译文档。/ Conventional live-action shooting version of the same story.
- `resources/examples/coin-slot/docs/new-project-copy-pack/`
  - 从本地 `NEW_PROJECT_COPY_PACK_v1/docs/` 合入的跨项目启动手册、camera-subject 连续性规则和 skill 迭代治理文件。/ Cross-project startup manuals, camera-subject continuity rules, and skill-iteration governance merged from local `NEW_PROJECT_COPY_PACK_v1/docs/`.

## Resources / 资源

- `resources/examples/coin-slot/csv/`
  - 生产表样例：188 panel 表、stage map、pure image queue、音频 cue、白模 QA、视觉 QA、交付校验等。/ Production table samples: 188-panel table, stage map, pure image queue, audio cues, whitebox QA, visual QA, delivery validation, etc.
- `resources/examples/coin-slot/configs/`
  - 从本地 copy pack 合入的跨项目配置模板：manifest、continuity、section map、edit plan、asset integrity、audio/animatic、whitebox 和 QA 表。/ Cross-project config templates from the local copy pack: manifest, continuity, section map, edit plan, asset integrity, audio/animatic, whitebox, and QA tables.
- `resources/examples/coin-slot/blender/`
  - 小型白模工程和 camera manifest 示例。/ A small whitebox project and a camera manifest sample.
- `resources/examples/coin-slot/media/`
  - Git LFS 管理的图片、音频、视频、Blender 和项目内 `.zip` 交付包，保留原项目相对路径。/ Images, audio, video, Blender, and in-project `.zip` deliverables managed by Git LFS, preserving original project-relative paths.
- `resources/examples/coin-slot/local-story-20260613/`
  - 本地 Story 与远端主线发生语义冲突的 CSV 快照；用于追溯本地 v002/v003 计划，不覆盖当前主线。/ A CSV snapshot where the local Story semantically conflicted with the remote mainline; kept to trace the local v002/v003 plan, without overwriting the current mainline.
- `resources/RESOURCE_MAP.md`
  - 资源说明和大型媒体排除规则。/ Resource notes and large-media exclusion rules.

大型图片、音频、视频、`.zip` 交付包通过 Git LFS 管理；`.rar` 备份包不推送。
Large images, audio, video, and `.zip` deliverables are managed by Git LFS; `.rar` backups are not pushed.
