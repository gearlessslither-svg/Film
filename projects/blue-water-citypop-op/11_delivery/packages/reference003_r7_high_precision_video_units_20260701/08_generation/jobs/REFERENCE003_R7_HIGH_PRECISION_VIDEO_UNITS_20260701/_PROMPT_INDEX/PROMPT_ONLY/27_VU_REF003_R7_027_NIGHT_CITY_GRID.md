# 27 — VU_REF003_R7_027_NIGHT_CITY_GRID — 夜城蓝网格

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/reference_clip/VU_REF003_R7_027_NIGHT_CITY_GRID_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_029` (01:01.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/keyframes/01_OP_SHOT_029.png`
- 图2: `R5_VU_REF003_014_NIGHT_CITY_BLUE_GRID_062500ms_01` (01:02.50, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/keyframes/02_R5_VU_REF003_014_NIGHT_CITY_BLUE_GRID_062500ms_01.png`
- 图3: `OP_SHOT_030` (01:03.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/keyframes/03_OP_SHOT_030.png`
- 图4: `R5_VU_REF003_015_NIGHT_AIRCRAFT_PASS_065000ms_01` (01:05.00, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/keyframes/04_R5_VU_REF003_015_NIGHT_AIRCRAFT_PASS_065000ms_01.png`
3. Active asset locks:
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_grid_geometry.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_027_start_061466ms` (start, 01:01.47, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/candidate_reference_frames/R7_CAND_027_start_061466ms.jpg`
- `R7_CAND_027_end_064910ms` (end, 01:04.91, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/candidate_reference_frames/R7_CAND_027_end_064910ms.jpg`
- `R7_CAND_027_middle_063188ms` (middle, 01:03.19, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/candidate_reference_frames/R7_CAND_027_middle_063188ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_027_NIGHT_CITY_GRID.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_027_NIGHT_CITY_GRID`.
Time range: `01:01.44-01:04.94`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: 夜城与蓝色地面/几何图案。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
