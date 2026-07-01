# VU_011_SUBMARINE_CREW_MONTAGE - Nautilus 船员与主角严肃 montage

- Unit type: `montage_sequence`
- Time range: 01:01-01:09
- Source: script-first director design
- Whitebox required: `false`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_031` (图1 / Nemo_portrait): Nemo 船长冷色近景。
- 图2 = `OP_SHOT_032` (图2 / Electra_bridge): Electra 与舰桥控制台。
- 图3 = `OP_SHOT_033` (图3 / Nadia_serious): Nadia 正面凝望，Blue Water 在喉间。
- 图4 = `OP_SHOT_034` (图4 / Nadia_Jean_pair): Nadia 与 Jean 肩并肩看向未来。

## 剧本镜头意图 / Script Intent

从海底城市进入人物精神段：Nemo、Electra、Nadia、Nadia/Jean 关系。

## 帧间关系 / Frame Relationships

这是剧本声明的 montage。AIGC 必须保留硬切/拍点节奏，不要把多个角色或地点平滑成同一个连续空间。

Incoming transition edges to respect:
- `TE_013_CITY_TO_CREW` from `OP_SHOT_030`: OP_SHOT_031 的舰桥冷蓝光承接海底城市蓝光。

Outgoing transition setup:
- `TE_014_PAIR_TO_JEWEL` to `OP_SHOT_035`: 当前 unit 结尾要准备 Nadia/Jean shared horizon -> Blue Water icon。

## 镜头计划 / Camera Plan

- Camera movement: measured portrait cuts: slow push on Nemo, slight slide on Electra controls, jewel-light hold on Nadia, calm two-shot horizon hold
- Framing: portrait montage ending in two-shot
- Lens: portrait/medium lenses, shallow but readable depth
- Screen direction / axis: not one-take; emotional direction moves from authority to partnership
- Focus: faces and Blue Water
- Lighting: cool bridge blue, then sky/sea blue for pair

## AIGC Video Prompt

Use the ordered images exactly as listed above. The script, not the images alone, defines whether this is one take, montage, insert, or transition. Preserve character identity, costume, prop design, screen direction, camera axis, lighting continuity, and the OP rhythm. Do not add text, logo, subtitle, watermark, modern objects, or random readable markings.
Generate as beat-synced cuts or separate video clips according to the listed image order. Do not interpolate all images into one impossible continuous space; continuity is rhythm, identity, color, and screen direction.

## Negative / Failure Conditions

- 如果提示词把舰桥和海边强行接成一个空间则失败；如果 Nadia 在图3/图4变脸则失败。
