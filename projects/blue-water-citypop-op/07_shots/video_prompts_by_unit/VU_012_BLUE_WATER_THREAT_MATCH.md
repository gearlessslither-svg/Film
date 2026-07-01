# VU_012_BLUE_WATER_THREAT_MATCH - Blue Water 蓝光到敌人红光威胁

- Unit type: `transition_pair`
- Time range: 01:09-01:13
- Source: script-first director design
- Whitebox required: `false`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_035` (图1 / blue_jewel_icon): Blue Water 标志性大特写。
- 图2 = `OP_SHOT_036` (图2 / red_threat_incoming): Gargoyle 红光威胁，蓝色被红色压迫。

## 剧本镜头意图 / Script Intent

用 Blue Water 图标后接 Gargoyle 威胁，形成蓝色希望被红色阴影压迫的对照。

## 帧间关系 / Frame Relationships

这是剧本声明的转场单位。图2 的开头必须承接图1 的结束状态；转场关系比单张画面更重要。

Intra-unit transition edges:
- `TE_015_JEWEL_TO_THREAT` `blue_to_red_strobe`: Blue Water cyan fills frame -> red-blue masked threat。写法：图2/OP_SHOT_036 的红光应像吞没图1蓝光一样出现。

Incoming transition edges to respect:
- `TE_014_PAIR_TO_JEWEL` from `OP_SHOT_034`: OP_SHOT_035 是从两人关系落到 Blue Water 象征，不是普通珠宝插图。

Outgoing transition setup:
- `TE_016_THREAT_TO_ASCENT` to `OP_SHOT_037`: 当前 unit 结尾要准备 red threat tension -> Nautilus acceleration in blue water。

## 镜头计划 / Camera Plan

- Camera movement: push into blue jewel until blue fills frame; red strobe cuts into masked threat and cold machinery
- Framing: macro jewel to masked villain portrait
- Lens: macro to portrait/close lens
- Screen direction / axis: color transition, not geographic continuity
- Focus: facets to mask/gloved hand
- Lighting: blue/cyan swallowed by hard red-blue threat light

## AIGC Video Prompt

Use the ordered images exactly as listed above. The script, not the images alone, defines whether this is one take, montage, insert, or transition. Preserve character identity, costume, prop design, screen direction, camera axis, lighting continuity, and the OP rhythm. Do not add text, logo, subtitle, watermark, modern objects, or random readable markings.
Generate the transition so the incoming image begins by inheriting the outgoing image color/motion/object state. The transition is mandatory, not optional decoration.

## Negative / Failure Conditions

- 如果图2没有承接蓝光被红色压迫的关系，则失败。
