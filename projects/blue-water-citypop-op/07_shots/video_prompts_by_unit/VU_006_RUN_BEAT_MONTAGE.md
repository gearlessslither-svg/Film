# VU_006_RUN_BEAT_MONTAGE - 奔跑四拍表情 montage

- Unit type: `montage_sequence`
- Time range: 00:36-00:44
- Source: script-first director design
- Whitebox required: `false`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_019` (图1 / beat_1_Nadia_close): Nadia 奔跑近景，四拍第一拍。
- 图2 = `OP_SHOT_020` (图2 / beat_2_Jean_close): Jean 奔跑近景，四拍第二拍。
- 图3 = `OP_SHOT_021` (图3 / beat_3_King_Marie_close): King/Marie 奔跑近景，四拍第三拍。
- 图4 = `OP_SHOT_022` (图4 / beat_4_group_wide): 全员宽景，四拍归拢。

## 剧本镜头意图 / Script Intent

剧本要求四拍切换：Nadia、Jean、King/Marie、全员；这是音乐剪辑，不是一镜到底。

## 帧间关系 / Frame Relationships

这是剧本声明的 montage。AIGC 必须保留硬切/拍点节奏，不要把多个角色或地点平滑成同一个连续空间。

Incoming transition edges to respect:
- `TE_007_GROUP_RUN_TO_BEAT_MONTAGE` from `OP_SHOT_018`: OP_SHOT_019 是从全员宽景硬切进 Nadia 奔跑近景，保持同向速度和风。

Outgoing transition setup:
- `TE_008_GROUP_TO_AIRCRAFT` to `OP_SHOT_023`: 当前 unit 结尾要准备 group motion resolves -> aircraft climbs into sky。

## 镜头计划 / Camera Plan

- Camera movement: four hard beat cuts with same running direction; close-ups carry motion blur and wind, final wide resolves direction
- Framing: close-up, close-up, close-up, wide
- Lens: portrait telephoto for first three, wider lens for final group
- Screen direction / axis: left-to-right motion must remain consistent across cuts
- Focus: sharp eyes/faces in close-ups, group readable in wide
- Lighting: same daylight and sky-blue background

## AIGC Video Prompt

Use the ordered images exactly as listed above. The script, not the images alone, defines whether this is one take, montage, insert, or transition. Preserve character identity, costume, prop design, screen direction, camera axis, lighting continuity, and the OP rhythm. Do not add text, logo, subtitle, watermark, modern objects, or random readable markings.
Generate as beat-synced cuts or separate video clips according to the listed image order. Do not interpolate all images into one impossible continuous space; continuity is rhythm, identity, color, and screen direction.

## Negative / Failure Conditions

- 如果四拍之间没有硬切节奏则失败；如果任一近景把人物方向改成反向奔跑则失败。
