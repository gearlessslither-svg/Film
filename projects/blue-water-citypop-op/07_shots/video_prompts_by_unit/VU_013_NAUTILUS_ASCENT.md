# VU_013_NAUTILUS_ASCENT - Nautilus 加速上升

- Unit type: `single_shot_with_transition_out`
- Time range: 01:13-01:15
- Source: script-first director design
- Whitebox required: `true`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_037` (图1 / submarine_ascent): Nautilus 加速上升破蓝。

## 剧本镜头意图 / Script Intent

敌人威胁后切回 Nautilus 行动，推动出水段。

## 帧间关系 / Frame Relationships

这是剧本声明的转场单位。图2 的开头必须承接图1 的结束状态；转场关系比单张画面更重要。

Incoming transition edges to respect:
- `TE_016_THREAT_TO_ASCENT` from `OP_SHOT_036`: OP_SHOT_037 用行动回应威胁，水压和速度必须上来。

Outgoing transition setup:
- `TE_017_ASCENT_TO_SURFACE` to `OP_SHOT_038`: 当前 unit 结尾要准备 submarine rising -> camera POV rising toward water surface。

## 镜头计划 / Camera Plan

- Camera movement: track with submarine hull as it rises through pressure and light
- Framing: dynamic three-quarter submarine action
- Lens: wide underwater tracking lens
- Screen direction / axis: upward and forward momentum
- Focus: hull, bubbles, light beams
- Lighting: deep blue brightening toward surface

## AIGC Video Prompt

Use the ordered images exactly as listed above. The script, not the images alone, defines whether this is one take, montage, insert, or transition. Preserve character identity, costume, prop design, screen direction, camera axis, lighting continuity, and the OP rhythm. Do not add text, logo, subtitle, watermark, modern objects, or random readable markings.
Generate the transition so the incoming image begins by inheriting the outgoing image color/motion/object state. The transition is mandatory, not optional decoration.

## Negative / Failure Conditions

- 如果潜艇不向上或不制造水压动能，下一段出水无法成立。
