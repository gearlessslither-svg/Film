# 02 — VU_REF003_002_WHITE_BIRD_SKY — 白鸟入画与蓝天滑翔

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/reference_clip/VU_REF003_002_WHITE_BIRD_SKY_reference.mp4`
2. Ordered keyframes:
- 图1: `OP_SHOT_003` (00:02.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/keyframes/01_OP_SHOT_003.png`
- 图2: `R5_VU_REF003_002_WHITE_BIRD_SKY_003500ms_02` (00:03.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/keyframes/02_R5_VU_REF003_002_WHITE_BIRD_SKY_003500ms_02.png`
- 图3: `OP_SHOT_004` (00:05.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/keyframes/03_OP_SHOT_004.png`
- 图4: `R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01` (00:07.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_002_WHITE_BIRD_SKY/keyframes/04_R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01.png`
3. Active asset locks:
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/props_vehicles_symbols_white_bird.png`

## Save Result To

`08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_002_WHITE_BIRD_SKY.mp4`

## Prompt To Use

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
