# 01 — VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG — 开场长段A：黑场云层到白鸟入画

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/reference_clip/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_001` (00:00.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/keyframes/01_OP_SHOT_001.png`
- 图2: `OP_SHOT_002` (00:01.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/keyframes/02_OP_SHOT_002.png`
- 图3: `OP_SHOT_003` (00:02.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/keyframes/03_OP_SHOT_003.png`
- 图4: `R5_VU_REF003_002_WHITE_BIRD_SKY_003500ms_02` (00:03.50, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/keyframes/04_R5_VU_REF003_002_WHITE_BIRD_SKY_003500ms_02.png`
- 图5: `OP_SHOT_004` (00:05.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/keyframes/05_OP_SHOT_004.png`
- 图6: `R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01` (00:07.00, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/keyframes/06_R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01.png`
3. Active asset locks:
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_white_bird.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_001_start_000030ms` (start, 00:00.03, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/candidate_reference_frames/R7_CAND_001_start_000030ms.jpg`
- `R7_CAND_001_end_006970ms` (end, 00:06.97, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/candidate_reference_frames/R7_CAND_001_end_006970ms.jpg`
- `R7_CAND_001_middle_003500ms` (middle, 00:03.50, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/candidate_reference_frames/R7_CAND_001_middle_003500ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG`.
Time range: `00:00.00-00:07.00`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: 连续天空开场，黑场/云层/白鸟作为一个长运动短语处理。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
