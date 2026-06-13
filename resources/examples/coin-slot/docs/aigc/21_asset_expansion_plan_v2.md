# 投币口 / 01_AIGC 资产扩展计划 v2

## 为什么要扩展

旧版资产适合展示方向，但不适合 5-6 分钟 AIGC 成片生产。现在的问题不是只缺几张图，而是缺一套能让人物、动作、空间和剪辑连续的图像资产网。

## 新资产目录

| 目录 | 用途 | 状态 |
|---|---|---|
| `character_design_v2/` | 新人物设定图、三视图、表情、姿态、关系图 | planned |
| `micro_storyboard_panels/` | MSB001-MSB188 微分镜图 | planned |
| `micro_storyboard_contact_sheets/` | 每批微分镜联系表 | planned |
| `micro_keyframes_v2/` | 从 188 张中选出的精修关键帧 | planned |
| `whitebox_renders_v2/` | 补充动作路径和中间构图白模 | planned |

## 资产数量

| 类型 | 计划数量 | 说明 | 对应表 |
|---|---:|---|---|
| 人物设计 v2 | 32 | 7 人 x 正面/三视图/表情/姿态 + 4 张关系/像素转换 | `exports/character_design_v2_asset_plan.csv` |
| 微分镜 panels | 188 | MSB001-MSB188，每张可生成单图 | `exports/micro_storyboard_asset_plan.csv` |
| 微分镜图像提示词 | 188 | 每张 panel 的完整正向/负向提示词 | `exports/micro_storyboard_image_prompts.csv` |
| 精修关键帧候选 | 34 | 从微分镜中标记为 keyframe 的候选图 | `19_micro_storyboard_188_panels.csv` |
| Start frame 候选 | 15 | 可作为视频生成单元首帧 | `19_micro_storyboard_188_panels.csv` |
| End frame 候选 | 20 | 可作为视频生成单元尾帧 | `19_micro_storyboard_188_panels.csv` |

## 生产优先级

1. 先做人物设计 v2：如果七个人仍然不可识别，禁止继续生成 188 张微分镜。
2. 再做 B01-B03：验证三兄弟、游戏厅、彬子和堵路关系。
3. 再做 B05：电话亭段动作少，适合检测小川是否稳定。
4. 最后做 B04 和 B06：暴力、逃跑、电子化、8-bit 都是高风险段。

## 文件命名规则

- 人物：`character_design_v2/CHR_BRO_B_protagonist_expression_grid_v001.png`
- 微分镜：`micro_storyboard_panels/B04/MSB096_11_手碰到石块.png`
- 联系表：`micro_storyboard_contact_sheets/B04_contact_sheet_v001.png`
- 精修关键帧：`micro_keyframes_v2/MKF096_stone_touch_v001.png`
- 白模补充：`whitebox_renders_v2/CAM_ALLEY_STONE_HAND_INSERT.png`

## 停止条件

出现以下任一情况必须返工，不继续跑视频：

- 阿磊、小川、小满只靠身高区别，脸和姿态不可区分。
- 彬子、高杆、大海、小齐变成同一类坏孩子。
- 小川在石块段像主动复仇。
- 小路空间不再连接游戏机房和废楼。
- 电话亭像科幻设备，不像现实错误物。
- 8-bit 段丢失废楼、电话亭和小川服装色块。
