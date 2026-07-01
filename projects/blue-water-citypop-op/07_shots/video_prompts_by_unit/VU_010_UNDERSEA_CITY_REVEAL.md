# VU_010_UNDERSEA_CITY_REVEAL - 海底都市点亮到全景

- Unit type: `continuous_reveal`
- Time range: 00:57-01:01
- Source: script-first director design
- Whitebox required: `true`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_029` (图1 / first_lights): 海底都市初光逐点亮起。
- 图2 = `OP_SHOT_030` (图2 / wide_city_reveal): 海底都市全景发光。

## 剧本镜头意图 / Script Intent

剧本要求远处海底都市先有光点，再展开为完整神秘城市。

## 帧间关系 / Frame Relationships

图2是图1的扩展，不是新地点；灯光密度、深海色和城市方向必须承接。

Incoming transition edges to respect:
- `TE_012_MECHA_TO_CITY` from `OP_SHOT_028`: OP_SHOT_029 的城市初光承接 OP_SHOT_028 的能量光。

Outgoing transition setup:
- `TE_013_CITY_TO_CREW` to `OP_SHOT_031`: 当前 unit 结尾要准备 undersea cyan city -> Nautilus bridge blue instruments。

## 镜头计划 / Camera Plan

- Camera movement: slow forward drift or crane-like underwater glide; lights awaken from scattered points to full panorama
- Framing: distant reveal to wide 21:9 city panorama
- Lens: wide underwater lens with depth haze
- Screen direction / axis: forward/downward drift, no jump to unrelated city
- Focus: distant lights becoming architecture
- Lighting: cyan/blue lights bloom gradually in black water

## AIGC Video Prompt

Use the ordered images exactly as listed above. The script, not the images alone, defines whether this is one take, montage, insert, or transition. Preserve character identity, costume, prop design, screen direction, camera axis, lighting continuity, and the OP rhythm. Do not add text, logo, subtitle, watermark, modern objects, or random readable markings.
Generate with continuity appropriate to the unit type; if cuts occur, they must preserve the scripted spatial, color, and motion bridge.

## Negative / Failure Conditions

- 如果图2不是图1的空间扩展则失败；如果突然出现文字、现代城市或陆地天空则失败。
