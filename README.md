# Coin Slot AIGC Toolkit / 投币口 AIGC 工具箱

> 中文在前，English follows each section. 每一节都是「中文 + English」双语。

这个独立仓库整理自 `E:\视觉\投币口` 项目，把目前沉淀出的可复用工作拆成四类。
This standalone repo is organized from the `E:\视觉\投币口` project and splits the reusable work into four categories.

- `skills/aigc-film-pipeline/`：Codex skill，用来指导 AIGC 短片从故事阶段、白模、pure 图、音频、animatic 到最终校验的生产流程。
  - The Codex skill that drives an AIGC short film through story stages, whitebox, pure images, audio, animatic, and final validation.
- `scripts/`：可执行工具，包括流水线校验、白模 QA、联系表、分镜面板、音频 guide、animatic、最终交付校验和 Windows keep-awake。
  - Executable tools: pipeline validation, whitebox QA, contact sheets, storyboard panels, audio guide, animatic, final-delivery validation, and a Windows keep-awake helper.
- `docs/`：面向人和 AI agent 的分类索引，说明每类产出放在哪里、怎么使用。
  - Human- and agent-facing index that explains where each kind of output lives and how to use it.
- `resources/examples/coin-slot/`：来自《投币口》的案例资源，包含项目文档、CSV 表格、流程索引、小型 Blender 白模示例，以及通过 Git LFS 管理的图片、音频、视频和项目内 `.zip` 交付包；`.rar` 备份包不纳入仓库。
  - Case-study assets from *Coin Slot*: project docs, CSV tables, process index, a small Blender whitebox sample, plus images/audio/video and in-project `.zip` deliverables tracked via Git LFS. `.rar` backups are excluded.
- `resources/examples/coin-slot/configs/` 和 `docs/new-project-copy-pack/`：从本地 `NEW_PROJECT_COPY_PACK_v1` 合入的跨项目模板、门禁规则和启动手册。
  - Cross-project templates, gate rules, and startup manuals merged in from the local `NEW_PROJECT_COPY_PACK_v1`.
- `resources/examples/coin-slot/local-story-20260613/`：本地 Story 与远端主线冲突的 CSV 快照；主线 CSV 保持远端版本，快照用于追溯本地 v002/v003 生成计划。
  - A CSV snapshot where the local Story conflicted with the remote mainline; the mainline CSV stays on the remote version and the snapshot is kept to trace the local v002/v003 generation plan.

## Repository Layout / 仓库结构

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

## Use As A Codex Plugin / 作为 Codex 插件使用

这个仓库已经带有 `.codex-plugin/plugin.json`。安装或分享时，使用插件目录 `coin-slot-aigc-toolkit` 作为根目录即可。
The repo already ships `.codex-plugin/plugin.json`. When installing or sharing, use the plugin directory `coin-slot-aigc-toolkit` as the root.

常用提示 / Common prompt:

```text
Use $aigc-film-pipeline to continue this AIGC film project from its TASK_LOG, CSV tables, and validation state.
```

## Tool Dependencies / 工具依赖

Python 脚本主要依赖（安装方式如下）：
The Python scripts mainly depend on the following (install with):

```powershell
python -m pip install -r requirements.txt
```

部分脚本需要项目素材存在，例如图片、音频或视频；`resources/examples/coin-slot/csv/` 只提供表格样例，不包含完整媒体交付物。
Some scripts require project media (images, audio, video) to be present; `resources/examples/coin-slot/csv/` only ships table samples, not full media deliverables.

## Merge Notes / 合并说明

- 2026-06-13 从本地 `Story/投币口` 补入 arcade lookdev、camera whiteboxes、15s long-take 设计、三兄弟参考锁、B01 v002/v003 候选图、rejected 记录和 arcade 专用工具脚本。
  - 2026-06-13: merged from local `Story/投币口` the arcade lookdev, camera whiteboxes, 15s long-take design, three-brother reference locks, B01 v002/v003 candidates, rejected records, and arcade-specific tool scripts.
- 远端已有的最终 183 张 real panel 交付主线未被本地旧表覆盖；本地冲突 CSV 保存在 `resources/examples/coin-slot/local-story-20260613/csv/`。
  - The remote mainline of 183 final real-panel deliverables was not overwritten by the older local tables; the conflicting local CSVs are kept in `resources/examples/coin-slot/local-story-20260613/csv/`.
- 本地 `NEW_PROJECT_COPY_PACK_v1` 已按新仓库组织方式拆入 `resources/examples/coin-slot/configs/` 与 `resources/examples/coin-slot/docs/new-project-copy-pack/`。
  - The local `NEW_PROJECT_COPY_PACK_v1` was reorganized into `resources/examples/coin-slot/configs/` and `resources/examples/coin-slot/docs/new-project-copy-pack/`.

## Common Commands / 常用命令

```powershell
python scripts/validate_pipeline_state.py <project-root>
python scripts/visual/qa_whitebox_images.py --project-root <project-root>\01_AIGC
python scripts/visual/make_contact_sheet.py --project-root <project-root>\01_AIGC
python scripts/visual/mark_pure_image_result.py --project-root <project-root>\01_AIGC --asset-id MSB001 --status passed
python scripts/visual/build_storyboard_animatic.py --project-root <project-root>\01_AIGC
python scripts/visual/validate_final_delivery.py --project-root <project-root>\01_AIGC
```

## Remote / 远端

远端仓库 / Remote repository:

[gearlessslither-svg/Film](https://github.com/gearlessslither-svg/Film.git)

如果要把最终分镜图、音频、视频也纳入版本管理，建议单独启用 Git LFS，并先确认远端仓库的容量限制。
If you want final storyboard images, audio, and video under version control too, enable Git LFS separately and check the remote repository's storage limits first.

## Git LFS Media / Git LFS 媒体

媒体归档位于 `resources/examples/coin-slot/media/`，按原项目相对路径保存。
Media archives live under `resources/examples/coin-slot/media/`, preserving the original project-relative paths.

当前 LFS 追踪类型 / Currently LFS-tracked types:

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
`.rar` is not tracked and not pushed.

## 预览图说明 / About Image Previews

很多媒体文件通过 Git LFS 管理。如果只克隆了仓库但没有运行 `git lfs pull`，这些图片在本地只是文本指针，Pipeline Hub 会显示「未下载 / not downloaded」占位块。
Many media files are managed by Git LFS. If you cloned the repo but did not run `git lfs pull`, those images are only text pointers locally, and Pipeline Hub shows a "not downloaded" placeholder.

恢复真实图片 / To restore the real images:

```bash
# 需要联网；若使用代理/VPN，先确保代理端口可用
# Requires network; if you use a proxy/VPN, make sure the proxy port is reachable first
git lfs pull
```

对于《投币口》案例，Pipeline Hub 会自动用本地 `投币口/01_AIGC/` 里已存在的原图回退显示，无需联网即可看到这部分图。
For the *Coin Slot* case study, Pipeline Hub automatically falls back to the originals already present in the local `投币口/01_AIGC/`, so those images display without any network.
