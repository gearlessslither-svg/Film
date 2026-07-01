# AIGC Video Generation Brief — VU_REF003_018_BLUE_WATER_SYMBOL

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_018_BLUE_WATER_SYMBOL_reference.mp4`
- Ordered keyframe anchors:
- 1. `OP_SHOT_035` at `01:13.50`: Blue Water 宝石象征; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_035.png`
- 2. `OP_SHOT_036` at `01:15.00`: 蓝色符号光; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_036.png`
- 3. `OP_SHOT_037` at `01:16.50`: 水下蓝色纹理; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_037.png`
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_segments/VU_REF003_018_BLUE_WATER_SYMBOL.mp4`

## Primary Direction

Use the reference video clip as the primary source for timing, camera movement,
screen direction, composition function, and transition rhythm. Use the generated
keyframe anchors as the visual remake identity and start/end/mid-frame anchors.
Use the setting chapter and asset lock images as hard identity, prop, vehicle,
animal, symbol, location, and scene-continuity constraints. The AIGC model must
not redesign visible characters, props, vehicles, or recurring environments.

Generate a clean live-action remake segment for `VU_REF003_018_BLUE_WATER_SYMBOL`. Preserve
the reference-003 OP motion and duration while replacing all readable original
text, credits, lyrics, subtitles, broadcaster marks, logos, and watermarks with
clean no-text composition.

## Unit Metadata

- Title: Blue Water 象征与水下纹理
- Time range: `01:13.50-01:17.00`
- Whitebox required: `False`
- Roughcut slot: `18`

## Transition Context

- `TE_REF003_034_034_TO_035`: Nadia 庄重正面 -> Blue Water 宝石象征 | OP_SHOT_035 begins from the reference-003 timing after OP_SHOT_034: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_035_035_TO_036`: Blue Water 宝石象征 -> 蓝色符号光 | OP_SHOT_036 begins from the reference-003 timing after OP_SHOT_035: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_036_036_TO_037`: 蓝色符号光 -> 水下蓝色纹理 | OP_SHOT_037 begins from the reference-003 timing after OP_SHOT_036: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_037_037_TO_038`: 水下蓝色纹理 -> 水花爆发 | OP_SHOT_038 begins from the reference-003 timing after OP_SHOT_037: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

# VU_REF003_018_BLUE_WATER_SYMBOL - Blue Water 象征与水下纹理

- Unit type: `symbolic_jewel_transition`
- Time range: 01:13.50-01:17.00
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_035` (图1 / Blue_Water_jewel_symbol, 01:13.50): Blue Water jewel/sapphire symbol over clean blue field, no text or marks.
- 图2 = `OP_SHOT_036` (图2 / blue_symbol_bloom, 01:15.00): Cyan-blue bloom or energy texture replaces original text overlay, jewel feeling preserved.
- 图3 = `OP_SHOT_037` (图3 / underwater_texture, 01:16.50): Underwater blue texture and light pattern, clean and text-free.

## Script Intent

Blue Water/宝石/水下纹理承担象征性转场，原片 NHK/文字必须替换。

## Frame Relationships

保留 Blue Water 象征，不生成 NHK 或文字。

Incoming: TE_REF003_034_034_TO_035  
Intra: TE_REF003_035_035_TO_036, TE_REF003_036_036_TO_037  
Outgoing: TE_REF003_037_037_TO_038

## Camera Plan

- Movement: jewel/symbol overlay dissolves into blue underwater texture
- Framing: macro jewel and abstract blue texture
- Lens: macro to wide texture
- Screen Direction: symbolic not geographic
- Focus: jewel facets and blue energy
- Lighting: cyan/blue glow

## AIGC Video Prompt

Generate this unit as a faithful live-action remake of the reference-003 OP timing. Use the ordered images as the only keyframe order for this unit. Preserve the reference shot function, motion role, screen direction, and character-entry timing. Replace all original readable titles, credits, lyrics, subtitles, and broadcaster marks with clean no-text composition.

## Generation Requirements

- Use reference-003-full-op-2160p as the timing and composition source.
- Replace original readable titles, credits, lyrics, subtitles, and NHK marks with clean no-text composition while preserving shot function.
- Do not generate literal anime screenshots; produce a faithful live-action remake keyframe/video plan.
- Preserve character age, costume color blocks, motion direction, and OP rhythm.

## Negative / Failure Conditions

- If readable text, logo, credits, lyrics, subtitle, or broadcaster mark appears, reject.
- If timing role or screen function no longer matches reference-003, reject.
- If a montage unit becomes a false continuous one-take, reject.

## Reject Conditions

- Any readable text, title, credit, lyric, subtitle, NHK/broadcaster mark, logo,
  watermark, or random symbol appears.
- The generated segment ignores the reference clip's timing or screen direction.
- Keyframe anchors are reordered, skipped, or replaced with unrelated imagery.
- Nadia does not match the `OP_SHOT_011_v2` official face lock.
- Any visible character face/costume/age identity, prop, vehicle, animal, symbol,
  or recurring scene structure drifts from the packaged locks.
- Minor characters are aged up, sexualized, or dressed immodestly.
- The MP4 cannot complete-decode.
