# VU_008_NAUTILUS_DIVE_CONTINUITY - Nautilus 下潜连续空间

- Unit type: `multi_shot_continuity`
- Time range: 00:48-00:53
- Source: script-first director design
- Whitebox required: `true`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_025` (图1 / wide_submarine_descends): Nautilus 初见下潜，深海大景。
- 图2 = `OP_SHOT_026` (图2 / side_profile_continues): Nautilus 侧影继续下潜，方向延续。

## 剧本镜头意图 / Script Intent

剧本从 Blue Water 蓝色进入深海，让 Nautilus 以重量感下潜并侧向通过。

## 帧间关系 / Frame Relationships

这是同空间连续，不一定一镜到底；图2必须承接图1的船体比例、水深、气泡方向和下潜方向。

Incoming transition edges to respect:
- `TE_010_JEWEL_TO_DEEP_SEA` from `OP_SHOT_024`: OP_SHOT_025 从宝石蓝扩展到深海蓝，像 Blue Water 的颜色把画面带入海底。

Outgoing transition setup:
- `TE_011_SUB_TO_MECHA` to `OP_SHOT_027`: 当前 unit 结尾要准备 submarine hull -> red/yellow/blue mechanical detail。

## 镜头计划 / Camera Plan

- Camera movement: wide descending reveal followed by lateral side tracking pass; can cut, but same underwater geography and vessel direction must remain
- Framing: wide three-quarter submarine to side profile
- Lens: wide underwater miniature/realistic lens
- Screen direction / axis: submarine moves left-to-right and downward; bubbles trail backward
- Focus: hull readable with depth haze
- Lighting: deep blue shafts, porthole glow

## AIGC Video Prompt

Use the ordered images exactly as listed above. The script, not the images alone, defines whether this is one take, montage, insert, or transition. Preserve character identity, costume, prop design, screen direction, camera axis, lighting continuity, and the OP rhythm. Do not add text, logo, subtitle, watermark, modern objects, or random readable markings.
Generate with continuity appropriate to the unit type; if cuts occur, they must preserve the scripted spatial, color, and motion bridge.

## Negative / Failure Conditions

- 如果图2的船方向、比例或水深和图1冲突则失败；如果变成新潜艇设计则失败。
