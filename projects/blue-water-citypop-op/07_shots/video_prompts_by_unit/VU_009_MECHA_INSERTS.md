# VU_009_MECHA_INSERTS - 机械色块与推进插入

- Unit type: `insert_montage`
- Time range: 00:53-00:57
- Source: script-first director design
- Whitebox required: `false`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_027` (图1 / color_block_insert): 红黄蓝机械色块插入。
- 图2 = `OP_SHOT_028` (图2 / propulsion_energy_insert): 机械推进与能量插入。

## 剧本镜头意图 / Script Intent

在 Nautilus/海底段中插入机械红黄蓝色块和推进能量，增强节奏。

## 帧间关系 / Frame Relationships

这是剧本声明的 montage。AIGC 必须保留硬切/拍点节奏，不要把多个角色或地点平滑成同一个连续空间。

Incoming transition edges to respect:
- `TE_011_SUB_TO_MECHA` from `OP_SHOT_026`: OP_SHOT_027 是潜艇内部/结构细节插入，不是新机器空间。

Outgoing transition setup:
- `TE_012_MECHA_TO_CITY` to `OP_SHOT_029`: 当前 unit 结尾要准备 mechanical energy glow -> distant undersea city lights。

## 镜头计划 / Camera Plan

- Camera movement: fast mechanical insert cuts; tiny push or vibration on machinery
- Framing: extreme mechanical close-ups
- Lens: macro/close industrial lens
- Screen direction / axis: not geographic; energy flow and color rhythm carry continuity
- Focus: rivets, vents, piston/fins, steam
- Lighting: deep blue shadows with red/yellow/blue highlights

## AIGC Video Prompt

Use the ordered images exactly as listed above. The script, not the images alone, defines whether this is one take, montage, insert, or transition. Preserve character identity, costume, prop design, screen direction, camera axis, lighting continuity, and the OP rhythm. Do not add text, logo, subtitle, watermark, modern objects, or random readable markings.
Generate as beat-synced cuts or separate video clips according to the listed image order. Do not interpolate all images into one impossible continuous space; continuity is rhythm, identity, color, and screen direction.

## Negative / Failure Conditions

- 如果看起来像另一个现代机器广告而不是 Nautilus 段落的一部分则失败。
