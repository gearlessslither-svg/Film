# 27 - VU_REF003_R7_027_NIGHT_CITY_GRID - 夜城蓝网格

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `01:01.44-01:04.94`
- Shot intent: 夜城与蓝色地面/几何图案。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/reference_clip/VU_REF003_R7_027_NIGHT_CITY_GRID_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_029` | 01:01.50 | 图1 / night_city_reveal | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/keyframes/01_OP_SHOT_029.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_014_NIGHT_CITY_BLUE_GRID_062500ms_01` | 01:02.50 | adaptive_primary | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/keyframes/02_R5_VU_REF003_014_NIGHT_CITY_BLUE_GRID_062500ms_01.png` |
| `official_keyframe` | `OP_SHOT_030` | 01:03.50 | 图2 / glowing_blue_grid | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/keyframes/03_OP_SHOT_030.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_015_NIGHT_AIRCRAFT_PASS_065000ms_01` | 01:05.00 | adaptive_primary | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/keyframes/04_R5_VU_REF003_015_NIGHT_AIRCRAFT_PASS_065000ms_01.png` |
| `r7_generated_candidate` | `R7_CAND_027_start_061466ms` | 01:01.47 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_027_start_061466ms.png` |
| `r7_generated_candidate` | `R7_CAND_027_middle_063188ms` | 01:03.19 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_027_middle_063188ms.png` |
| `r7_generated_candidate` | `R7_CAND_027_end_064910ms` | 01:04.91 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_027_end_064910ms.png` |
| `asset_lock:props_vehicles_symbols` | `blue_grid_geometry` |  | official_scene_symbol_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_grid_geometry.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_027_start_061466ms` | 01:01.47 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_027_start_061466ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/candidate_reference_frames/R7_CAND_027_start_061466ms.jpg` |
| `R7_CAND_027_middle_063188ms` | 01:03.19 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_027_middle_063188ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/candidate_reference_frames/R7_CAND_027_middle_063188ms.jpg` |
| `R7_CAND_027_end_064910ms` | 01:04.91 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_027_end_064910ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_027_NIGHT_CITY_GRID/candidate_reference_frames/R7_CAND_027_end_064910ms.jpg` |

## Active Asset Locks

- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_grid_geometry.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_027_NIGHT_CITY_GRID.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_027_NIGHT_CITY_GRID`.
Time range: `01:01.44-01:04.94`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: 夜城与蓝色地面/几何图案。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
