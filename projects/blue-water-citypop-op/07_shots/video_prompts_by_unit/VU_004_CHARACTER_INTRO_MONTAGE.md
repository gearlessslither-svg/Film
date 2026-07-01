# VU_004_CHARACTER_INTRO_MONTAGE - 角色介绍继续段（reference-002 后续占位）

- Unit type: `montage_sequence`
- Time range: 00:23-00:26 (provisional after reference-002 boundary)
- Source: reference-002-opening bounded local analysis
- Whitebox required: `false`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_008` (图1 / character_card_Jean): Jean 少年发明家近景。
- 图2 = `OP_SHOT_009` (图2 / character_card_King_Marie): King 与 Marie 的明亮角色一闪。
- 图3 = `OP_SHOT_010` (图3 / character_card_Grandis_trio): Grandis 三人组姿态介绍。
- 图4 = `OP_SHOT_011` (图4 / character_card_Nemo_Electra): Nemo 与 Electra 的舰桥冷色介绍。
- 图5 = `OP_SHOT_012` (图5 / character_card_Gargoyle): Gargoyle 敌影红蓝一闪。
- 图6 = `OP_SHOT_013` (图6 / jewel_insert_transition_out): Blue Water 宝石手部特写，蓝光脉冲。

## 剧本镜头意图 / Script Intent

reference-002 只覆盖到 Nadia 入场；OP_SHOT_008-013 暂保留为后续角色介绍占位，等待完整参考继续校准。

## 帧间关系 / Frame Relationships

该段目前只是 reference-002 之后的保留占位；不能再把 Nadia/Jean 等角色提前塞进 00:12-00:21。

Incoming edges: TE_REF002_007_NADIA_TO_CHARACTER_CONTINUE  
Intra-unit edges: none  
Outgoing edges: TE_006_JEWEL_TO_RUN

## 镜头计划 / Camera Plan

- Movement: provisional hard beat cuts after Nadia has entered; do not move these cards before 00:23 without more reference evidence
- Framing: mostly close-up or medium character cards ending on macro jewel
- Lens: portrait lenses for characters, macro for jewel
- Screen Direction: not continuous; continuity comes from rhythm and color design
- Focus: subject-specific focus pulls
- Lighting: sky daylight for surface characters, cool blue for Nautilus, red-blue for threat, jewel cyan for transition out

## AIGC Video Prompt

Use the ordered images exactly as listed above. Follow the reference-002 timing for this unit and preserve the scripted function over any previous generated still. Do not generate readable title text, logo, subtitles, watermark, random letters, or direct animation screenshot copying. Keep motion, sky direction, scale, and light transitions consistent with the listed transition edges.

## Generation Requirements

- 必须按剧本镜头单位生成，不允许把关键帧当成互不相关的单图。
- 多图单位必须在提示词中显式写出：图1、图2、图3...的角色和顺序。
- 一镜到底单位必须说明起点、中点、终点、摄影机运动、屏幕方向和禁止硬切。
- Montage 单位必须说明硬切节奏，禁止误写成连续摄影。
- 转场边必须写入 incoming prompt 或 unit prompt，图2开头要承接图1的结束状态。

## Negative / Failure Conditions

- 如果提示词要求同一镜头连续穿过所有人物则失败；如果图7不作为奔跑段触发器则失败。
