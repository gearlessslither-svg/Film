# VU_015_FINAL_BIRD_SKY_PAN - 白鸟回归到最终天空留白

- Unit type: `one_take_group`
- Time range: 01:21-01:30
- Source: script-first director design
- Whitebox required: `false`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_041` (图1 / bird_return_start): 白鸟回归，穿过海天线。
- 图2 = `OP_SHOT_042` (图2 / final_sky_hold): 最终蓝天留白，无字标志位。

## 剧本镜头意图 / Script Intent

剧本以白鸟回到海天线，并上摇到最终无字标志位留白。

## 帧间关系 / Frame Relationships

这是剧本声明的一镜到底/准一镜到底单位。AIGC 必须把图1到最后一图理解为同一连续摄影机运动里的关键状态，不要硬切、不要跳轴、不要改换场地。

Intra-unit transition edges:
- `TE_019_BIRD_TO_FINAL_SKY` `pan_to_title_safe_hold`: bird exits upward -> clean centered sky negative space。写法：图2/OP_SHOT_042 是图1白鸟上摇后的最终无字留白。

Incoming transition edges to respect:
- `TE_018_HORIZON_TO_BIRD` from `OP_SHOT_040`: OP_SHOT_041 必须从 OP_SHOT_040 的海天线中自然出现，呼应开场白鸟。

## 镜头计划 / Camera Plan

- Camera movement: gentle upward pan follows bird from horizon into open sky, then hold negative space
- Framing: wide horizon bird pass to clean sky title-safe frame
- Lens: wide sky/ocean lens
- Screen direction / axis: bird moves upward through frame; camera continues upward
- Focus: bird readable then sky/clouds
- Lighting: bright final daylight

## AIGC Video Prompt

Use the ordered images exactly as listed above. The script, not the images alone, defines whether this is one take, montage, insert, or transition. Preserve character identity, costume, prop design, screen direction, camera axis, lighting continuity, and the OP rhythm. Do not add text, logo, subtitle, watermark, modern objects, or random readable markings.
Generate one continuous shot moving through 图1 -> 图2 -> ... -> final image as key states. No visible cut inside the unit. Maintain a single camera path and continuous physical motion.

## Negative / Failure Conditions

- 如果图2不保留最终标志位留白则失败；如果生成文字则失败。
