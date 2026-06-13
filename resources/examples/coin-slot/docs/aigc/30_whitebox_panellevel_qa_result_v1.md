# 投币口 / 01_AIGC panel-level 白模 QA 结果 v1

## 本轮结论

白模生产策略已从“少量 source camera 复用”升级为“188 张 MSB panel 默认各自一张白模”。本轮已完成 188/188 张白模重渲染，并通过自动 QA：

| 指标 | 结果 |
|---|---:|
| 计划白模 | 188 |
| 实际渲染 | 188 |
| skipped | 0 |
| missing | 0 |
| failed | 0 |
| similarity clusters | 0 |
| similarity flagged | 0 |

自动 QA 命令：

```powershell
python E:\视觉\投币口\01_AIGC\tools\qa_whitebox_images.py --project-root E:\视觉\投币口\01_AIGC
```

最终输出：

```text
auto_pass_needs_human_review=188 failed=0 missing=0 similarity_clusters=0 similarity_flagged=0
```

## 本轮修正的根因

之前重复白模的根因不是单张坏图，而是流程错误：多个 panel 复用同一个 source camera，只做轻微 deterministic offset，且静态白模没有编码人物 blocking、动作、道具状态、首尾帧差异。用户指出“大量重复图”后，本轮做了三层修正。

1. 生成规则：`whitebox_expansion_plan.csv` 从 169 required / 19 optional 改为 188 required。
2. Blender 生成：隐藏基础场景里的静态 `CHAR_` 人物锚点，改为每张 panel 渲染时按故事临时放置人物、道具、动作路径和特写结构。
3. QA 检测：相似度 QA 从灰度全图检测升级为“灰度 + dHash + RGB 色差 + story foreground mask”，避免把同一环境里的真实 blocking 差异误判成重复。

## 关键白模规则

- 白模必须服从分镜意图；白模不好就修白模，不改原分镜。
- 1 Blender unit 近似 1 米；人物高度和体量按 `29_whitebox_scale_and_blocking_bible_v1.md` 执行。
- 每张 MSB 默认独立白模。微小位移可共用构图逻辑，但仍要有独立白模、独立 pure 图和 prompt delta。
- 真实图片生成前必须先看对应白模；如果 pure 图跑偏，先回查白模是否不够精确。

## 主要输出

- `exports/whitebox_expansion_plan.csv`：188/188 required。
- `exports/whitebox_qa_checklist.csv`：188 行，全部自动通过，待人工导演视角复核。
- `exports/whitebox_similarity_report.csv`：无重复簇。
- `exports/whitebox_scale_anchor_table.csv`：人物/环境比例锚点。
- `whitebox_renders_v2/B01` 到 `B06`：188 张白模。
- `whitebox_contact_sheets_v2_panellevel_final`：6 张批次 contact sheets。

## 进入真实图片前的人眼复核重点

自动 QA 不能代替导演判断。进入 pure 图生产前，仍要人工扫以下重点：

- 小路段：三兄弟近/左侧，混混远/右侧，不翻轴。
- 石块段：石块从路边环境物逐步变成小川视线焦点。
- 逃跑段：小川朝废楼方向跑，后方人物留在原空间。
- 走廊/电话亭：电话亭固定远端，暖白光不漂移成科幻装置。
- 8-bit 段：横版 orthographic，主角左、敌人右。
