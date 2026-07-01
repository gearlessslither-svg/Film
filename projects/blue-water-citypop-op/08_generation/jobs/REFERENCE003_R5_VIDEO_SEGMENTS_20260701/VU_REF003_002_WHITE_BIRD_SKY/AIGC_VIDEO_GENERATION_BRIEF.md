# AIGC Video Generation Brief — VU_REF003_002_WHITE_BIRD_SKY — R5 Expanded Package

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_002_WHITE_BIRD_SKY_reference.mp4`
- Ordered keyframe anchors: 4 total = 2 official + 2 R5 adaptive generated
- 图1 = `OP_SHOT_003` (official_keyframe, 00:02.50, 图1 / bird_entry): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/keyframes/01_OP_SHOT_003.png`
  - function: 白鸟首次入画
- 图2 = `R5_VU_REF003_002_WHITE_BIRD_SKY_003500ms_02` (r5_adaptive_generated, 00:03.50, adaptive_middle): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/keyframes/02_R5_VU_REF003_002_WHITE_BIRD_SKY_003500ms_02.png`
  - function: White bird glide changes screen position/scale within a long sky movement; useful middle/final action anchor without generating every frame.
- 图3 = `OP_SHOT_004` (official_keyframe, 00:05.00, 图2 / bird_glide): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/keyframes/03_OP_SHOT_004.png`
  - function: 白鸟滑翔延续
- 图4 = `R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01` (r5_adaptive_generated, 00:07.00, adaptive_primary): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/keyframes/04_R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01.png`
  - function: White bird glide changes screen position/scale within a long sky movement; useful middle/final action anchor without generating every frame.
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_002_WHITE_BIRD_SKY.mp4`

## How To Feed This To The AIGC Video Site

Use the reference clip as the primary timing/camera/motion guide. Use the ordered
keyframe anchors as visual identity, scene, prop, and transition-state locks.
The generated segment should follow the reference clip's motion and duration,
but use the generated keyframes as the remake's visual world.

If the chosen AIGC site cannot accept all ordered images, keep the first and last anchors, then prioritize R5 adaptive anchors and turning-point official anchors. Do not reorder the remaining images.

## Primary Direction

Generate a clean live-action remake segment for `VU_REF003_002_WHITE_BIRD_SKY`. Preserve
the reference-003 OP timing, shot function, screen direction, and edit rhythm.
Replace all readable original text, credits, lyrics, subtitles, broadcaster
marks, logos, and watermarks with clean no-text composition.

Use the setting chapter and packaged asset locks as hard identity, prop,
vehicle, animal, symbol, location, and scene-continuity constraints. The AIGC
model must not redesign visible characters, props, vehicles, or recurring
environments.

## Unit Metadata

- Title: 白鸟入画与蓝天滑翔
- Time range: `00:02.50-00:07.00`
- Whitebox required: `False`
- Roughcut slot: `2`
- Package type: `reference003_r5_expanded_video_segment`

## Transition Context

- `TE_REF003_002_002_TO_003`: 云层蓝天显现 -> 白鸟首次入画 | OP_SHOT_003 begins from the reference-003 timing after OP_SHOT_002: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_003_003_TO_004`: 白鸟首次入画 -> 白鸟滑翔延续 | OP_SHOT_004 begins from the reference-003 timing after OP_SHOT_003: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_004_004_TO_005`: 白鸟滑翔延续 -> 无字职员表安全位 | OP_SHOT_005 begins from the reference-003 timing after OP_SHOT_004: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

# VU_REF003_002_WHITE_BIRD_SKY - 白鸟入画与蓝天滑翔

- Unit type: `single_subject_motion_sequence`
- Time range: 00:02.50-00:07.00
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_003` (图1 / bird_entry, 00:02.50): White bird enters the blue sky after the cloud fade-in, wings open and readable.
- 图2 = `OP_SHOT_004` (图2 / bird_glide, 00:05.00): The same white bird glides farther through saturated blue sky, no aircraft.

## Script Intent

白鸟约 2.5 秒入画并在蓝天中持续滑翔，带出 OP 的第一条运动线。

## Frame Relationships

同一只白鸟连续运动；原片字幕区域在生成版变成干净天空。

Incoming: TE_REF003_002_002_TO_003  
Intra: TE_REF003_003_003_TO_004  
Outgoing: TE_REF003_004_004_TO_005

## Camera Plan

- Movement: locked/gentle follow on bird crossing blue sky
- Framing: wide blue sky with white bird medium to small scale
- Lens: wide anamorphic sky lens
- Screen Direction: bird glides consistently across frame
- Focus: bird silhouette against blue sky
- Lighting: clean daylight

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
