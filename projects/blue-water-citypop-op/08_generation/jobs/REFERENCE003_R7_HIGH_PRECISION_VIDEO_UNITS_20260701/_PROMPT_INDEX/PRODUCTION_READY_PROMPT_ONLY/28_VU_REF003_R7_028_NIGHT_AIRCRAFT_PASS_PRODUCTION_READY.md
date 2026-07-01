# 28 - VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS - 夜航飞行器短切

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `01:04.94-01:06.02`
- Shot intent: 夜航飞行器短切。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS/reference_clip/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `r5_adaptive_generated` | `R5_VU_REF003_015_NIGHT_AIRCRAFT_PASS_065000ms_01` | 01:05.00 | adaptive_primary | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS/keyframes/01_R5_VU_REF003_015_NIGHT_AIRCRAFT_PASS_065000ms_01.png` |
| `official_keyframe` | `OP_SHOT_031` | 01:05.50 | 图1 / night_aircraft_pass | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS/keyframes/02_OP_SHOT_031.png` |
| `r7_generated_candidate` | `R7_CAND_028_start_064970ms` | 01:04.97 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_028_start_064970ms.png` |
| `r7_generated_candidate` | `R7_CAND_028_end_065994ms` | 01:05.99 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_028_end_065994ms.png` |
| `asset_lock:props_vehicles_symbols` | `jean_aircraft` |  | official_prop_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_jean_aircraft.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_028_start_064970ms` | 01:04.97 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_028_start_064970ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS/candidate_reference_frames/R7_CAND_028_start_064970ms.jpg` |
| `R7_CAND_028_end_065994ms` | 01:05.99 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_028_end_065994ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS/candidate_reference_frames/R7_CAND_028_end_065994ms.jpg` |

## Active Asset Locks

- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_jean_aircraft.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS`.
Time range: `01:04.94-01:06.02`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: 夜航飞行器短切。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
