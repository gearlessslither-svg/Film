# 33 — VU_REF003_R7_033_SPLASH_PEAK — 水花爆发峰值

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_033_SPLASH_PEAK/reference_clip/VU_REF003_R7_033_SPLASH_PEAK_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_038` (01:18.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_033_SPLASH_PEAK/keyframes/01_OP_SHOT_038.png`
- 图2: `R5_VU_REF003_019_WATER_SPLASH_TRANSITION_078500ms_01` (01:18.50, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_033_SPLASH_PEAK/keyframes/02_R5_VU_REF003_019_WATER_SPLASH_TRANSITION_078500ms_01.png`
- 图3: `OP_SHOT_039` (01:19.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_033_SPLASH_PEAK/keyframes/03_OP_SHOT_039.png`
3. Active asset locks:
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_water_burst_transition.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_033_start_077816ms` (start, 01:17.82, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_033_SPLASH_PEAK/candidate_reference_frames/R7_CAND_033_start_077816ms.jpg`
- `R7_CAND_033_end_079174ms` (end, 01:19.17, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_033_SPLASH_PEAK/candidate_reference_frames/R7_CAND_033_end_079174ms.jpg`
- `R7_CAND_033_middle_078495ms` (middle, 01:18.50, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_033_SPLASH_PEAK/candidate_reference_frames/R7_CAND_033_middle_078495ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_033_SPLASH_PEAK.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_033_SPLASH_PEAK`.
Time range: `01:17.79-01:19.20`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: 水花爆发峰值与天空转场。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
