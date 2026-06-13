# Coin Slot AIGC Toolkit

这个独立仓库整理自 `E:\视觉\投币口` 项目，把目前沉淀出的可复用工作拆成三类：

- `skills/aigc-film-pipeline/`：Codex skill，用来指导 AIGC 短片从故事阶段、白模、pure 图、音频、animatic 到最终校验的生产流程。
- `scripts/`：可执行工具，包括流水线校验、白模 QA、联系表、分镜面板、音频 guide、animatic、最终交付校验和 Windows keep-awake。
- `resources/examples/coin-slot/`：来自《投币口》的轻量案例资源，主要是 CSV 表格、流程索引和一个小型 Blender 白模示例；大型图片、音频、视频、压缩包没有纳入仓库。

## Repository Layout

```text
.codex-plugin/plugin.json
skills/aigc-film-pipeline/
scripts/
  validate_pipeline_state.py
  keep-codex-awake.ps1
  visual/
  blender/
resources/examples/coin-slot/
  csv/
  blender/
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

## Common Commands

```powershell
python scripts/validate_pipeline_state.py <project-root>
python scripts/visual/qa_whitebox_images.py --project-root <project-root>\01_AIGC
python scripts/visual/make_contact_sheet.py --project-root <project-root>\01_AIGC
python scripts/visual/mark_pure_image_result.py --project-root <project-root>\01_AIGC --asset-id MSB001 --status passed
python scripts/visual/build_storyboard_animatic.py --project-root <project-root>\01_AIGC
python scripts/visual/validate_final_delivery.py --project-root <project-root>\01_AIGC
```

## Push To A Remote

本地 git 仓库可以直接推到一个空的远端仓库：

```powershell
git remote add origin <repo-url>
git push -u origin main
```

如果要把最终分镜图、音频、视频也纳入版本管理，建议单独启用 Git LFS，并先确认远端仓库的容量限制。
