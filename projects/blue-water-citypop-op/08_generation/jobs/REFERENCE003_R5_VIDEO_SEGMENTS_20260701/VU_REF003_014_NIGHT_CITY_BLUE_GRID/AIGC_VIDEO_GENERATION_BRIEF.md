# AIGC Video Generation Brief — VU_REF003_014_NIGHT_CITY_BLUE_GRID — R5 Expanded Package

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_014_NIGHT_CITY_BLUE_GRID_reference.mp4`
- Ordered keyframe anchors: 3 total = 2 official + 1 R5 adaptive generated
- 图1 = `OP_SHOT_029` (official_keyframe, 01:01.50, 图1 / night_city_reveal): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/keyframes/01_OP_SHOT_029.png`
  - function: 夜城初现
- 图2 = `R5_VU_REF003_014_NIGHT_CITY_BLUE_GRID_062500ms_01` (r5_adaptive_generated, 01:02.50, adaptive_primary): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/keyframes/02_R5_VU_REF003_014_NIGHT_CITY_BLUE_GRID_062500ms_01.png`
  - function: 夜城与蓝色地面图案: large timeline gap between existing anchors; visually different from nearest existing anchor
- 图3 = `OP_SHOT_030` (official_keyframe, 01:03.50, 图2 / glowing_blue_grid): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/keyframes/03_OP_SHOT_030.png`
  - function: 蓝色地面图案
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_014_NIGHT_CITY_BLUE_GRID.mp4`

## How To Feed This To The AIGC Video Site

Use the reference clip as the primary timing/camera/motion guide. Use the ordered
keyframe anchors as visual identity, scene, prop, and transition-state locks.
The generated segment should follow the reference clip's motion and duration,
but use the generated keyframes as the remake's visual world.

If the chosen AIGC site cannot accept all ordered images, keep the first and last anchors, then prioritize R5 adaptive anchors and turning-point official anchors. Do not reorder the remaining images.

## Primary Direction

Generate a clean live-action remake segment for `VU_REF003_014_NIGHT_CITY_BLUE_GRID`. Preserve
the reference-003 OP timing, shot function, screen direction, and edit rhythm.
Replace all readable original text, credits, lyrics, subtitles, broadcaster
marks, logos, and watermarks with clean no-text composition.

Use the setting chapter and packaged asset locks as hard identity, prop,
vehicle, animal, symbol, location, and scene-continuity constraints. The AIGC
model must not redesign visible characters, props, vehicles, or recurring
environments.

## Unit Metadata

- Title: 夜城与蓝色地面图案
- Time range: `01:01.50-01:04.50`
- Whitebox required: `True`
- Roughcut slot: `14`
- Package type: `reference003_r5_expanded_video_segment`

## Transition Context

- `TE_REF003_028_028_TO_029`: Nautilus 深蓝剪影 -> 夜城初现 | OP_SHOT_029 begins from the reference-003 timing after OP_SHOT_028: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_029_029_TO_030`: 夜城初现 -> 蓝色地面图案 | OP_SHOT_030 begins from the reference-003 timing after OP_SHOT_029: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_030_030_TO_031`: 蓝色地面图案 -> 夜航飞行器 | OP_SHOT_031 begins from the reference-003 timing after OP_SHOT_030: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

# VU_REF003_014_NIGHT_CITY_BLUE_GRID - 夜城与蓝色地面图案

- Unit type: `night_city_symbolic_reveal`
- Time range: 01:01.50-01:04.50
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `true`

## Ordered Input Images

- 图1 = `OP_SHOT_029` (图1 / night_city_reveal, 01:01.50): Dark night city under hovering craft lights, blue tones and mysterious scale.
- 图2 = `OP_SHOT_030` (图2 / glowing_blue_grid, 01:03.50): Glowing blue geometric grid or diagram across the ground with city lights beyond, no readable symbols.

## Script Intent

夜色城市、蓝色几何地面和空中机械形成神秘科技段。

## Frame Relationships

蓝色图案可抽象但不能生成可读文字。

Incoming: TE_REF003_028_028_TO_029  
Intra: TE_REF003_029_029_TO_030  
Outgoing: TE_REF003_030_030_TO_031

## Camera Plan

- Movement: slow reveal from dark aircraft/sky to glowing blue grid and city lights
- Framing: wide night city with luminous ground diagram
- Lens: wide night lens
- Screen Direction: vertical scale from craft to city grid
- Focus: blue grid/city relation
- Lighting: night blue and warm city lights

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

## R5 Expanded Notes

- This package includes R5 adaptive generated frames when they exist for this unit.
- R5 frames are not raw screenshots; they are generated pure-image assets with output paths.
- Keep the ordered images in timeline order. Do not skip a R5 frame that carries a unique transition, action, prop, or identity state unless the video site image limit forces triage.

## Reject Conditions

- Any readable text, title, credit, lyric, subtitle, NHK/broadcaster mark, logo,
  watermark, or random symbol appears.
- The generated segment ignores the reference clip's timing or screen direction.
- Keyframe anchors are reordered, skipped, or replaced with unrelated imagery.
- Nadia does not match the `OP_SHOT_011_v2` official face lock whenever visible.
- Any visible character face/costume/age identity, prop, vehicle, animal, symbol,
  or recurring scene structure drifts from the packaged locks.
- Minor characters are aged up, sexualized, or dressed immodestly.
- The MP4 cannot complete-decode.
