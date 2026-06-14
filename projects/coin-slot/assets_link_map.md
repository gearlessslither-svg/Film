# Asset Link Map

这个文件记录“项目文件夹”和外部旧资源之间的关系。总控台可以读取这里，把历史素材映射到当前项目阶段。

## Project

- Project name: 投币口
- Project slug: `coin-slot`
- Source root: E:\视觉\投币口
- Resource root: resources/examples/coin-slot

## Suggested mappings

| Current project area | External/source location | Notes |
| --- | --- | --- |
| `01_intake/source_inputs/` | E:\视觉\投币口 | 原始导演输入、旧工程资料、临时输入。 |
| `03_story/` | resources/examples/coin-slot/docs | 故事、分镜、制作文档。 |
| `06_previs/blender/` | resources/examples/coin-slot/blender | 白模、Blender 脚本、空间关系验证。 |
| `07_shots/` | resources/examples/coin-slot/csv | 镜头表、生成表、QA 表。 |
| `08_generation/outputs/` | resources/examples/coin-slot/media | 已归档的图片、视频、音频样例素材。 |
| `04_lookdev/` / `06_previs/scene_locks/` | resources/examples/coin-slot/media/01_AIGC/environment_lookdev | 本地 Story 补入的 SCN_ARCADE / SCN_COMPOUND lookdev、mother OBJ 和 camera whiteboxes。 |
| `07_shots/video_prompts/` | resources/examples/coin-slot/media/01_AIGC/long_take_design | 本地 Story 补入的 SCN_ARCADE opening 15s 长镜头设计、prompt pack、keyframe board 和测试图。 |
| cross-project templates | resources/examples/coin-slot/configs and resources/examples/coin-slot/docs/new-project-copy-pack | 本地 `NEW_PROJECT_COPY_PACK_v1` 的新项目模板、camera-subject 连续性和 skill 迭代治理。 |
| conflict snapshots | resources/examples/coin-slot/local-story-20260613 | 本地 CSV 与远端主线语义不同，保留为追溯快照，不覆盖主线。 |

## Large asset rule

- `.rar` 不进入 Git。
- 图片、视频、音频、Blender、压缩包等生产素材如需入库，必须走 Git LFS。
- 如果只是引用旧素材，优先在这里登记路径，避免重复复制大文件。
