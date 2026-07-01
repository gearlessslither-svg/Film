# 31 - VU_REF003_R7_031_BLUE_WATER_BLOOM - Blue Water蓝色绽放

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `01:14.07-01:16.45`
- Shot intent: Blue Water 象征蓝色绽放/水下纹理。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_031_BLUE_WATER_BLOOM/reference_clip/VU_REF003_R7_031_BLUE_WATER_BLOOM_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `r5_adaptive_generated` | `R5_VU_REF003_018_BLUE_WATER_SYMBOL_074000ms_01` | 01:14.00 | adaptive_primary | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_031_BLUE_WATER_BLOOM/keyframes/01_R5_VU_REF003_018_BLUE_WATER_SYMBOL_074000ms_01.png` |
| `official_keyframe` | `OP_SHOT_036` | 01:15.00 | 图2 / blue_symbol_bloom | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_031_BLUE_WATER_BLOOM/keyframes/02_OP_SHOT_036.png` |
| `official_keyframe` | `OP_SHOT_037` | 01:16.50 | 图3 / underwater_texture | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_031_BLUE_WATER_BLOOM/keyframes/03_OP_SHOT_037.png` |
| `r7_generated_candidate` | `R7_CAND_031_start_074104ms` | 01:14.10 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_031_start_074104ms.png` |
| `r7_generated_candidate` | `R7_CAND_031_middle_075262ms` | 01:15.26 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_031_middle_075262ms.png` |
| `r7_generated_candidate` | `R7_CAND_031_end_076421ms` | 01:16.42 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_031_end_076421ms.png` |
| `asset_lock:props_vehicles_symbols` | `blue_water_pendant` |  | official_prop_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_031_start_074104ms` | 01:14.10 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_031_start_074104ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_031_BLUE_WATER_BLOOM/candidate_reference_frames/R7_CAND_031_start_074104ms.jpg` |
| `R7_CAND_031_middle_075262ms` | 01:15.26 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_031_middle_075262ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_031_BLUE_WATER_BLOOM/candidate_reference_frames/R7_CAND_031_middle_075262ms.jpg` |
| `R7_CAND_031_end_076421ms` | 01:16.42 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_031_end_076421ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_031_BLUE_WATER_BLOOM/candidate_reference_frames/R7_CAND_031_end_076421ms.jpg` |

## Active Asset Locks

- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_031_BLUE_WATER_BLOOM.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_031_BLUE_WATER_BLOOM`.
Time range: `01:14.07-01:16.45`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Blue Water 象征蓝色绽放/水下纹理。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
