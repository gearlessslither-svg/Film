# VU_014_SURFACE_ONETAKE - 水下上浮到海天线一镜到底

- Unit type: `one_take_group`
- Time range: 01:15-01:21
- Source: script-first director design
- Whitebox required: `true`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_038` (图1 / underwater_upward_start): 水下仰视水面，镜头向上浮。
- 图2 = `OP_SHOT_039` (图2 / surface_break_midpoint): 破水瞬间，水滴与泡沫。
- 图3 = `OP_SHOT_040` (图3 / horizon_end): 海天线展开，镜头稳定。

## 剧本镜头意图 / Script Intent

剧本要求镜头从海中浮出：水下仰视、破水、海天线展开。

## 帧间关系 / Frame Relationships

这是剧本声明的一镜到底/准一镜到底单位。AIGC 必须把图1到最后一图理解为同一连续摄影机运动里的关键状态，不要硬切、不要跳轴、不要改换场地。

Incoming transition edges to respect:
- `TE_017_ASCENT_TO_SURFACE` from `OP_SHOT_037`: VU_014 图1/OP_SHOT_038 承接 OP_SHOT_037 的上升方向，改为水下 POV 向上浮。

Outgoing transition setup:
- `TE_018_HORIZON_TO_BIRD` to `OP_SHOT_041`: 当前 unit 结尾要准备 steady sea horizon -> white bird crosses same open sky。

## 镜头计划 / Camera Plan

- Camera movement: continuous upward camera rise through bubbles, break surface, droplets slide, stabilize on horizon
- Framing: underwater POV to waterline to wide horizon
- Lens: wide waterproof POV lens
- Screen direction / axis: vertical upward movement resolves into level horizon
- Focus: water surface shimmer, then foam/droplets, then distant horizon
- Lighting: blue underwater shifts to bright white sky and saturated ocean

## AIGC Video Prompt

Use the ordered images exactly as listed above. The script, not the images alone, defines whether this is one take, montage, insert, or transition. Preserve character identity, costume, prop design, screen direction, camera axis, lighting continuity, and the OP rhythm. Do not add text, logo, subtitle, watermark, modern objects, or random readable markings.
Generate one continuous shot moving through 图1 -> 图2 -> ... -> final image as key states. No visible cut inside the unit. Maintain a single camera path and continuous physical motion.

## Negative / Failure Conditions

- 如果没有连续上浮路径则失败；如果图2不是图1到图3之间的破水中点则失败。
