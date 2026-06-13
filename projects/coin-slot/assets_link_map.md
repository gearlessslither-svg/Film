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

## Large asset rule

- `.rar` 不进入 Git。
- 图片、视频、音频、Blender、压缩包等生产素材如需入库，必须走 Git LFS。
- 如果只是引用旧素材，优先在这里登记路径，避免重复复制大文件。
