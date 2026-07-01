# 19 — VU_REF003_019_WATER_SPLASH_TRANSITION — 水花爆发转天空

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_019_WATER_SPLASH_TRANSITION/reference_clip/VU_REF003_019_WATER_SPLASH_TRANSITION_reference.mp4`
2. Ordered keyframes:
- 图1: `R5_VU_REF003_019_WATER_SPLASH_TRANSITION_077500ms_02` (01:17.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_019_WATER_SPLASH_TRANSITION/keyframes/01_R5_VU_REF003_019_WATER_SPLASH_TRANSITION_077500ms_02.png`
- 图2: `OP_SHOT_038` (01:18.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_019_WATER_SPLASH_TRANSITION/keyframes/02_OP_SHOT_038.png`
- 图3: `R5_VU_REF003_019_WATER_SPLASH_TRANSITION_078500ms_01` (01:18.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_019_WATER_SPLASH_TRANSITION/keyframes/03_R5_VU_REF003_019_WATER_SPLASH_TRANSITION_078500ms_01.png`
- 图4: `OP_SHOT_039` (01:19.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_019_WATER_SPLASH_TRANSITION/keyframes/04_OP_SHOT_039.png`
3. Active asset locks:
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/props_vehicles_symbols_water_burst_transition.png`

## Save Result To

`08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_019_WATER_SPLASH_TRANSITION.mp4`

## Prompt To Use

# VU_REF003_019_WATER_SPLASH_TRANSITION - 水花爆发转天空

- Unit type: `water_burst_transition`
- Time range: 01:17.50-01:19.50
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_038` (图1 / water_burst, 01:18.00): Bright water/ice-like burst fills frame with blue-white motion, no text.
- 图2 = `OP_SHOT_039` (图2 / splash_to_sky, 01:19.00): Water streaks clear into blue sky and white cloud fragments.

## Script Intent

水体/冰蓝爆发把画面带回天空终段。

## Frame Relationships

动态水花转场，禁止文字。

Incoming: TE_REF003_037_037_TO_038  
Intra: TE_REF003_038_038_TO_039  
Outgoing: TE_REF003_039_039_TO_040

## Camera Plan

- Movement: bursting water transition into sky
- Framing: water splash fills frame then opens to blue sky/cloud
- Lens: wide dynamic transition
- Screen Direction: upward energy
- Focus: water edge and sky reveal
- Lighting: bright blue/white

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
