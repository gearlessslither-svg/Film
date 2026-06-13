# Director Aesthetic Review

Generated at: 2026-06-13T16:11:00+08:00

## Evidence Reviewed

- `10_qa/reports/project_audit_latest.md`
- `resources/examples/coin-slot/media/01_AIGC/final_storyboard_contact_sheets/B01_final_storyboard_contact_sheet_v002.jpg`
- `resources/examples/coin-slot/media/01_AIGC/final_storyboard_contact_sheets/B03_final_storyboard_contact_sheet_v002.jpg`

## Current Judgment

`投币口` 已经有可读的成片方向和大量历史产物：潮湿夜景、旧街机厅、蓝绿荧光、儿童角色组、窄巷空间、从入口到离开的节奏都比较统一。它适合作为样板，因为它同时暴露了两层问题：

- 视觉资产本身已经有一定完成度。
- 标准化项目目录需要把这些资产转化为阶段锁定文件、镜头任务表和可复用生产证据。

本轮已经完成 12 镜头样板批次迁移，并补齐生成、剪辑音频和交付索引。项目分析状态从 `needs_work` 提升到 `pass`，标准目录 12 个阶段全部有可读产物或索引。

## Strengths

- 美术气质稳定：潮湿墙面、旧门洞、街机光源、夜间反光地面形成统一世界。
- 光色方向明确：蓝绿机台光与暖色街灯有清晰对比，能支持悬疑、童年记忆和轻微危险感。
- 分镜颗粒度较细：contact sheet 已经拆出进入、观察、街机厅、退出、对峙等连续节拍。
- 角色组关系清楚：高个孩子、校服孩子、小孩的体量和站位能形成层级。
- 空间类型明确：门口、窄巷、街机厅三个主空间具有可识别的转换关系。

## Current Pipeline Status

| Area | Status | Note |
| --- | --- | --- |
| `00_admin` to `07_shots` | pass | 已有导演简报、方向、故事、lookdev、asset bible、previs 索引和 12 镜头任务。 |
| `10_qa` | pass | 已有项目分析报告和导演审美复盘。 |
| `08_generation` | pass | 已有 12-shot generation plan、输出索引和 reject log。 |
| `09_edit` | pass | 已有 rough cut timing、audio cue sheet、subtitle notes 和 color pass notes。 |
| `11_delivery` | pass | 已有 exports/packages/manifests 索引，链接到 LFS archive。 |

## Aesthetic Risks

- 画面气质统一，但如果继续生成，很容易变成“同一条湿巷的重复角度”。下一步需要明确镜头功能：观察、进入、发现、犹豫、对峙、离开，每类镜头要有不同 camera height、shot size 和 blocking。
- 儿童角色的服装和脸部需要 stage-specific lock。B01 和 B03 中角色组可读，但如果后续扩展镜头，校服、背包、发型、身高比例和表情阶段必须锁定。
- 街机厅蓝绿光是强记忆点，但需要继续沉淀为可复用 styleframes。当前已有色彩和灯光规则，下一步应将这些规则绑定到具体 keyframes。
- 白模精度仍是流程短板。投币口的空间依赖门洞、墙体、巷道纵深和前景遮挡；如果白模不够精细，图片模型会把空间关系重新发明一遍。
- 声音资产不能等最后补。街机厅的电流声、投币声、按钮声、脚步水声和远处环境声应该在分镜阶段就进入节奏设计。

## Next Useful Batch

12 镜头样板批次已经建立并通过结构/分析检查。下一批建议集中提高质量，而不是补目录：

1. 把 12 镜头对应的白模/control layer 从链接索引升级为项目内可直接读取的控制层。
2. 从 contact sheets 中拆出 3 到 6 张正式 styleframes，绑定到 lookdev 规则。
3. 把 audio cue sheet 扩成真实时间轴，并接入 animatic/review video。
4. 在 GUI 中增加 Shot Factory 面板，按 `shot_id` 批量打开 prompt、whitebox、keyframe 和 reject log。
5. 对同一 12 镜头跑一次真实模型复生成，比较新输出与历史样板的一致性。
