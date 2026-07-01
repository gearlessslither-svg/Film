# 28 — VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS — 夜航飞行器短切

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS/reference_clip/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `R5_VU_REF003_015_NIGHT_AIRCRAFT_PASS_065000ms_01` (01:05.00, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS/keyframes/01_R5_VU_REF003_015_NIGHT_AIRCRAFT_PASS_065000ms_01.png`
- 图2: `OP_SHOT_031` (01:05.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS/keyframes/02_OP_SHOT_031.png`
3. Active asset locks:
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_jean_aircraft.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_028_start_064970ms` (start, 01:04.97, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS/candidate_reference_frames/R7_CAND_028_start_064970ms.jpg`
- `R7_CAND_028_end_065994ms` (end, 01:05.99, P1_generate_next_small_batch): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS/candidate_reference_frames/R7_CAND_028_end_065994ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS`.
Time range: `01:04.94-01:06.02`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: 夜航飞行器短切。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
