# 13 — VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS — Nautilus 海底光束段

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/reference_clip/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_reference.mp4`
2. Ordered keyframes:
- 图1: `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_052000ms_01` (00:52.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/keyframes/01_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_052000ms_01.png`
- 图2: `OP_SHOT_026` (00:52.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/keyframes/02_OP_SHOT_026.png`
- 图3: `OP_SHOT_027` (00:55.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/keyframes/03_OP_SHOT_027.png`
- 图4: `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_057000ms_03` (00:57.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/keyframes/04_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_057000ms_03.png`
- 图5: `OP_SHOT_028` (00:58.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/keyframes/05_OP_SHOT_028.png`
- 图6: `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_060500ms_02` (01:00.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/keyframes/06_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_060500ms_02.png`
3. Active asset locks:
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png`

## Save Result To

`08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS.mp4`

## Prompt To Use

# VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS - Nautilus 海底光束段

- Unit type: `undersea_submarine_sequence`
- Time range: 00:52.00-01:01.00
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `true`

## Ordered Input Images

- 图1 = `OP_SHOT_026` (图1 / undersea_start, 00:52.50): Deep blue underwater light shafts with Nautilus silhouette entering, no credits.
- 图2 = `OP_SHOT_027` (图2 / undersea_pass, 00:55.00): Nautilus passes under shimmering surface light, large but graceful.
- 图3 = `OP_SHOT_028` (图3 / undersea_shadow, 00:58.50): Submarine silhouette deepens in blue water with moving light bands, no text.

## Script Intent

Nautilus 在水下光束中通过，原片有职员表；生成版保留海底运动和光线，去掉文字。

## Frame Relationships

潜艇空间连续和比例重要，文字全部替换为干净水下空间。

Incoming: TE_REF003_025_025_TO_026  
Intra: TE_REF003_026_026_TO_027, TE_REF003_027_027_TO_028  
Outgoing: TE_REF003_028_028_TO_029

## Camera Plan

- Movement: slow underwater tracking pass under shafts of light
- Framing: submarine silhouette and hull moving through deep blue water
- Lens: wide underwater lens
- Screen Direction: submarine crosses consistently
- Focus: submarine scale, water shafts, silhouette
- Lighting: blue underwater shafts

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
