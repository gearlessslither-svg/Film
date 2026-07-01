# VU_001_CLOUD_PRELUDE - 云层静默开场

- Unit type: `single_shot`
- Time range: 00:00-00:02
- Source: script-first director design
- Whitebox required: `false`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_001` (single_frame): 云层静默开场，纯天空建立呼吸。

## 剧本镜头意图 / Script Intent

剧本要求第一眼不是宝石或人物，而是安静云层，为白鸟入画保留呼吸。

## 帧间关系 / Frame Relationships

作为全片第一个静止呼吸镜头；不要提前出现人物、宝石、文字或飞机。

Outgoing transition setup:
- `TE_001_CLOUD_TO_BIRD` to `OP_SHOT_002`: 当前 unit 结尾要准备 quiet cloud plate -> sudden white bird wing crossing same blue sky。

## 镜头计划 / Camera Plan

- Camera movement: locked wide sky plate with very slow cloud drift
- Framing: wide 21:9 cloud plate
- Lens: wide anamorphic, deep focus
- Screen direction / axis: none yet
- Focus: infinity clouds
- Lighting: clean blue daylight

## AIGC Video Prompt

Use the ordered images exactly as listed above. The script, not the images alone, defines whether this is one take, montage, insert, or transition. Preserve character identity, costume, prop design, screen direction, camera axis, lighting continuity, and the OP rhythm. Do not add text, logo, subtitle, watermark, modern objects, or random readable markings.
Generate with continuity appropriate to the unit type; if cuts occur, they must preserve the scripted spatial, color, and motion bridge.

## Negative / Failure Conditions

- 如果去掉下一镜白鸟，本镜仍应是纯开场呼吸；如果出现人物或标题字则失败。
