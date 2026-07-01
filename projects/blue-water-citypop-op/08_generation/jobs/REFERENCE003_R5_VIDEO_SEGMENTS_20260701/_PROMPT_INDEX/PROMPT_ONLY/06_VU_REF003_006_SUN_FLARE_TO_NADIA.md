# 06 — VU_REF003_006_SUN_FLARE_TO_NADIA — 太阳光转 Nadia

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_006_SUN_FLARE_TO_NADIA/reference_clip/VU_REF003_006_SUN_FLARE_TO_NADIA_reference.mp4`
2. Ordered keyframes:
- 图1: `OP_SHOT_009` (00:23.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_006_SUN_FLARE_TO_NADIA/keyframes/01_OP_SHOT_009.png`
- 图2: `R5_VU_REF003_006_SUN_FLARE_TO_NADIA_023500ms_01` (00:23.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_006_SUN_FLARE_TO_NADIA/keyframes/02_R5_VU_REF003_006_SUN_FLARE_TO_NADIA_023500ms_01.png`
3. Active asset locks:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/characters_nadia.png`
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Save Result To

`08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_006_SUN_FLARE_TO_NADIA.mp4`

## Prompt To Use

# VU_REF003_006_SUN_FLARE_TO_NADIA - 太阳光转 Nadia

- Unit type: `light_transition_insert`
- Time range: 00:22.50-00:23.50
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_009` (图1 / sun_flare_transition, 00:23.00): Bright sun flare over clean blue sky prepares the cut to Nadia.

## Script Intent

标题位后由蓝天和太阳光线转入 Nadia 入场。

## Frame Relationships

太阳光是进入人物段的切点，不要写入文字。

Incoming: TE_REF003_008_008_TO_009  
Intra: none  
Outgoing: TE_REF003_009_009_TO_010

## Camera Plan

- Movement: locked sky insert with sun bloom
- Framing: sky, cloud streaks, bright sun edge
- Lens: wide/tele sky insert with controlled flare
- Screen Direction: none; brightness drives cut
- Focus: sun bloom and sky streaks
- Lighting: strong daylight flare

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
