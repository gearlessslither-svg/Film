# 02 — VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG — 开场长段B：白鸟云层到飞行器闪现

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG/reference_clip/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01` (00:07.00, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG/keyframes/01_R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01.png`
- 图2: `OP_SHOT_005` (00:07.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG/keyframes/02_OP_SHOT_005.png`
- 图3: `OP_SHOT_006` (00:11.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG/keyframes/03_OP_SHOT_006.png`
- 图4: `R5_VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS_014000ms_01` (00:14.00, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG/keyframes/04_R5_VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS_014000ms_01.png`
- 图5: `R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_014500ms_02` (00:14.50, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG/keyframes/05_R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_014500ms_02.png`
- 图6: `OP_SHOT_007` (00:15.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG/keyframes/06_OP_SHOT_007.png`
- 图7: `R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_016000ms_01` (00:16.00, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG/keyframes/07_R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_016000ms_01.png`
3. Active asset locks:
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_jean_aircraft.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_002_start_007030ms` (start, 00:07.03, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG/candidate_reference_frames/R7_CAND_002_start_007030ms.jpg`
- `R7_CAND_002_end_016470ms` (end, 00:16.47, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG/candidate_reference_frames/R7_CAND_002_end_016470ms.jpg`
- `R7_CAND_002_middle_011750ms` (middle, 00:11.75, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG/candidate_reference_frames/R7_CAND_002_middle_011750ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG`.
Time range: `00:07.00-00:16.50`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: 保留白鸟/云层长运动，并精准抓住 00:14.72 飞行器一闪。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
