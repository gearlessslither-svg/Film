# Coin Slot AIGC Toolkit

这个独立仓库整理自 `E:\视觉\投币口` 项目，把目前沉淀出的可复用工作拆成四类：

- `skills/aigc-film-pipeline/`：Codex skill，用来指导 AIGC 短片从故事阶段、白模、pure 图、音频、animatic 到最终校验的生产流程。
- `scripts/`：可执行工具，包括流水线校验、白模 QA、联系表、分镜面板、音频 guide、animatic、最终交付校验和 Windows keep-awake。
- `docs/`：面向人和 AI agent 的分类索引，说明每类产出放在哪里、怎么使用。
- `resources/examples/coin-slot/`：来自《投币口》的案例资源，包含项目文档、CSV 表格、流程索引、小型 Blender 白模示例，以及通过 Git LFS 管理的图片、音频、视频和项目内 `.zip` 交付包；`.rar` 备份包不纳入仓库。
- `resources/examples/coin-slot/configs/` 和 `docs/new-project-copy-pack/`：从本地 `NEW_PROJECT_COPY_PACK_v1` 合入的跨项目模板、门禁规则和启动手册。
- `resources/examples/coin-slot/local-story-20260613/`：本地 Story 与远端主线冲突的 CSV 快照；主线 CSV 保持远端版本，快照用于追溯本地 v002/v003 生成计划。

## Repository Layout

```text
.codex-plugin/plugin.json
docs/
skills/aigc-film-pipeline/
scripts/
  validate_pipeline_state.py
  keep-codex-awake.ps1
  visual/
  blender/
resources/examples/coin-slot/
  docs/
  configs/
  csv/
  blender/
  media/
  local-story-20260613/
  case-study-readme.md
```

## Use As A Codex Plugin

这个仓库已经带有 `.codex-plugin/plugin.json`。安装或分享时，使用插件目录 `coin-slot-aigc-toolkit` 作为根目录即可。

常用提示：

```text
Use $aigc-film-pipeline to continue this AIGC film project from its TASK_LOG, CSV tables, and validation state.
```

## Tool Dependencies

Python 脚本主要依赖：

```powershell
python -m pip install -r requirements.txt
```

部分脚本需要项目素材存在，例如图片、音频或视频；`resources/examples/coin-slot/csv/` 只提供表格样例，不包含完整媒体交付物。

## Merge Notes

- 2026-06-13 从本地 `Story/投币口` 补入 arcade lookdev、camera whiteboxes、15s long-take 设计、三兄弟参考锁、B01 v002/v003 候选图、rejected 记录和 arcade 专用工具脚本。
- 远端已有的最终 183 张 real panel 交付主线未被本地旧表覆盖；本地冲突 CSV 保存在 `resources/examples/coin-slot/local-story-20260613/csv/`。
- 本地 `NEW_PROJECT_COPY_PACK_v1` 已按新仓库组织方式拆入 `resources/examples/coin-slot/configs/` 与 `resources/examples/coin-slot/docs/new-project-copy-pack/`。

## Common Commands

```powershell
python scripts/validate_pipeline_state.py <project-root>
python scripts/visual/qa_whitebox_images.py --project-root <project-root>\01_AIGC
python scripts/visual/make_contact_sheet.py --project-root <project-root>\01_AIGC
python scripts/visual/mark_pure_image_result.py --project-root <project-root>\01_AIGC --asset-id MSB001 --status passed
python scripts/visual/build_storyboard_animatic.py --project-root <project-root>\01_AIGC
python scripts/visual/validate_final_delivery.py --project-root <project-root>\01_AIGC
```

## Remote

远端仓库：

[gearlessslither-svg/Film](https://github.com/gearlessslither-svg/Film.git)

如果要把最终分镜图、音频、视频也纳入版本管理，建议单独启用 Git LFS，并先确认远端仓库的容量限制。

## Git LFS Media

媒体归档位于 `resources/examples/coin-slot/media/`，按原项目相对路径保存。

当前 LFS 追踪类型：

```text
*.blend
*.zip
*.png
*.jpg
*.jpeg
*.wav
*.mp4
```

`.rar` 不追踪、不推送。
