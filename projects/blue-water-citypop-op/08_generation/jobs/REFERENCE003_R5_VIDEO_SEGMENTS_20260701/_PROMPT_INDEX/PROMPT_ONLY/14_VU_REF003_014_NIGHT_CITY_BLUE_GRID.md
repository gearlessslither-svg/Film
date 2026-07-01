# 14 — VU_REF003_014_NIGHT_CITY_BLUE_GRID — 夜城与蓝色地面图案

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/reference_clip/VU_REF003_014_NIGHT_CITY_BLUE_GRID_reference.mp4`
2. Ordered keyframes:
- 图1: `OP_SHOT_029` (01:01.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/keyframes/01_OP_SHOT_029.png`
- 图2: `R5_VU_REF003_014_NIGHT_CITY_BLUE_GRID_062500ms_01` (01:02.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/keyframes/02_R5_VU_REF003_014_NIGHT_CITY_BLUE_GRID_062500ms_01.png`
- 图3: `OP_SHOT_030` (01:03.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_014_NIGHT_CITY_BLUE_GRID/keyframes/03_OP_SHOT_030.png`
3. Active asset locks:
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/props_vehicles_symbols_blue_grid_geometry.png`

## Save Result To

`08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_014_NIGHT_CITY_BLUE_GRID.mp4`

## Prompt To Use

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
