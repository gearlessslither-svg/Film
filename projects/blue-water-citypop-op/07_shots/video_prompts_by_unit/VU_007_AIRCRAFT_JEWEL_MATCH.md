# VU_007_AIRCRAFT_JEWEL_MATCH - 飞机蓝天到 Blue Water 天空倒影 match cut

- Unit type: `transition_pair`
- Time range: 00:44-00:48
- Source: script-first director design
- Whitebox required: `false`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_023` (图1 / outgoing_aircraft_sky): 飞机上升，天空运动拉向蓝色。
- 图2 = `OP_SHOT_024` (图2 / incoming_jewel_reflection): Blue Water 反射天空，承接飞机蓝天。

## 剧本镜头意图 / Script Intent

剧本用飞机上升后的天空蓝转入 Blue Water 宝石里的天空倒影，为潜入海洋做颜色桥。

## 帧间关系 / Frame Relationships

这是剧本声明的转场单位。图2 的开头必须承接图1 的结束状态；转场关系比单张画面更重要。

Intra-unit transition edges:
- `TE_009_AIRCRAFT_TO_JEWEL` `match_cut`: sky blue and cloud reflection -> same blue inside Blue Water jewel。写法：图2/OP_SHOT_024 开头必须像图1的天空被装进宝石反射里。

Incoming transition edges to respect:
- `TE_008_GROUP_TO_AIRCRAFT` from `OP_SHOT_022`: OP_SHOT_023 的上升感承接奔跑段的前进动能。

Outgoing transition setup:
- `TE_010_JEWEL_TO_DEEP_SEA` to `OP_SHOT_025`: 当前 unit 结尾要准备 jewel cyan/sky blue -> deep ocean blue around Nautilus。

## 镜头计划 / Camera Plan

- Camera movement: aircraft climbs into blue; cut/match into jewel reflection with same sky color and light angle
- Framing: wide aircraft sky to macro jewel
- Lens: wide sky to macro lens
- Screen direction / axis: upward energy continues as reflected light expands
- Focus: infinity sky to macro jewel facets
- Lighting: sky blue and white cloud reflection

## AIGC Video Prompt

Use the ordered images exactly as listed above. The script, not the images alone, defines whether this is one take, montage, insert, or transition. Preserve character identity, costume, prop design, screen direction, camera axis, lighting continuity, and the OP rhythm. Do not add text, logo, subtitle, watermark, modern objects, or random readable markings.
Generate the transition so the incoming image begins by inheriting the outgoing image color/motion/object state. The transition is mandatory, not optional decoration.

## Negative / Failure Conditions

- 如果图2看不出承接飞机天空，match cut 失败；如果图2变成普通珠宝静物，失败。
