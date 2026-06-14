# 投币口 / 02_Normal_Shooting 差异补充计划 v1

## 核心判断

本项目不再全量制作正常拍摄版视觉资产。实拍版只作为 AIGC 版的“差异补充”和“镜头想法保留库”。

原因：

- 用户几乎不会真的实拍。
- AIGC 版是主生产路径。
- 实拍版有价值的部分，是那些 AIGC 容易阉割、但真人摄影/现场调度可能更有力量的镜头。

## 实拍版只保留这些内容

| 类型 | 是否保留 | 说明 |
|---|---|---|
| 20 镜完整重跑 | 不保留 | 由 AIGC micro storyboard 负责 |
| 场景完整设定图 | 不保留 | 用 AIGC 场景设定即可 |
| 人物全量重设定 | 不保留 | 以 AIGC 人物设计 v2 为准 |
| AIGC 难实现但实拍更强的镜头 | 保留 | 只生成 delta reference |
| 现场调度、低成本替代、道具建议 | 保留 | 文档级别即可 |
| 声音现场策略 | 保留 | 可补充环境声/foley 思路 |

## 候选 Delta 镜头

| ID | 对应 AIGC 范围 | 实拍差异价值 | 是否建议生成参考图 |
|---|---|---|---|
| NS_DELTA_001 | Clip 02 / 三兄弟靠近 | 真实儿童走路节奏和身高差，AIGC 容易变成同款队列 | yes |
| NS_DELTA_002 | Clip 03 / 游戏厅入口 | 脏门帘擦镜、CRT 光吞掉孩子，实拍会更自然 | yes |
| NS_DELTA_003 | Clip 05 / 街霸胜利 | 手、按钮、屏幕、脸部红光的连续反应，AIGC 容易乱 | yes |
| NS_DELTA_004 | Clip 10 / 围住哥哥 | 身体挤压和空间变窄，实拍调度比 AIGC 稳 | yes |
| NS_DELTA_005 | Clip 11 / 石块失手 | 前景遮挡冲击瞬间，实拍可更克制 | yes |
| NS_DELTA_006 | Clip 13-14 / 废楼走廊 | 真实长走廊回声和低机位奔跑，实拍质感强 | optional |
| NS_DELTA_007 | Clip 17 / 听筒特写 | 手和旧电话材质，AIGC 容易手变形 | yes |

## 输出目录

- `02_Normal_Shooting/delta_references/NS_DELTA_001_v001.png`
- `02_Normal_Shooting/delta_references/NS_DELTA_002_v001.png`
- ...

这些图只作为参考，不进入 AIGC 视频生成母版，不需要 annotated 双版本。

## 检查口径

- 实拍 delta 图只保留“和 AIGC 不同且有价值”的摄影/调度想法。
- 不用为实拍版重做全片。
- 如果某个 delta 镜头能直接改善 AIGC 提示词或白模机位，再把它反哺到 `01_AIGC`，而不是开一条独立实拍资产线。
