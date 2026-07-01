# 30 - VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL - Nadia庄重到宝石

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `01:11.36-01:14.07`
- Shot intent: Nadia 庄重正面过渡到 Blue Water 象征。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL/reference_clip/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_034` | 01:12.00 | 图1 / Nadia_solemn_front | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL/keyframes/01_OP_SHOT_034.png` |
| `official_keyframe` | `OP_SHOT_035` | 01:13.50 | 图1 / Blue_Water_jewel_symbol | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL/keyframes/02_OP_SHOT_035.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_018_BLUE_WATER_SYMBOL_074000ms_01` | 01:14.00 | adaptive_primary | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL/keyframes/03_R5_VU_REF003_018_BLUE_WATER_SYMBOL_074000ms_01.png` |
| `r7_generated_candidate` | `R7_CAND_030_start_071393ms` | 01:11.39 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_030_start_071393ms.png` |
| `r7_generated_candidate` | `R7_CAND_030_middle_072718ms` | 01:12.72 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_030_middle_072718ms.png` |
| `r7_generated_candidate` | `R7_CAND_030_end_074044ms` | 01:14.04 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_030_end_074044ms.png` |
| `asset_lock:characters` | `nadia` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png` |
| `asset_lock:props_vehicles_symbols` | `blue_water_pendant` |  | official_prop_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_030_start_071393ms` | 01:11.39 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_030_start_071393ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL/candidate_reference_frames/R7_CAND_030_start_071393ms.jpg` |
| `R7_CAND_030_middle_072718ms` | 01:12.72 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_030_middle_072718ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL/candidate_reference_frames/R7_CAND_030_middle_072718ms.jpg` |
| `R7_CAND_030_end_074044ms` | 01:14.04 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_030_end_074044ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL/candidate_reference_frames/R7_CAND_030_end_074044ms.jpg` |

## Active Asset Locks

- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL`.
Time range: `01:11.36-01:14.07`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Nadia 庄重正面过渡到 Blue Water 象征。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
