# 24 - VU_REF003_R7_024_NAUTILUS_PASS - Nautilus水下通过

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:55.00-00:57.00`
- Shot intent: 潜艇水下通过中段。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_024_NAUTILUS_PASS/reference_clip/VU_REF003_R7_024_NAUTILUS_PASS_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_027` | 00:55.00 | 图2 / undersea_pass | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_024_NAUTILUS_PASS/keyframes/01_OP_SHOT_027.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_057000ms_03` | 00:57.00 | adaptive_middle | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_024_NAUTILUS_PASS/keyframes/02_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_057000ms_03.png` |
| `r7_generated_candidate` | `R7_CAND_024_start_055030ms` | 00:55.03 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_024_start_055030ms.png` |
| `r7_generated_candidate` | `R7_CAND_024_middle_056000ms` | 00:56.00 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_024_middle_056000ms.png` |
| `r7_generated_candidate` | `R7_CAND_024_end_056970ms` | 00:56.97 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_024_end_056970ms.png` |
| `asset_lock:props_vehicles_symbols` | `nautilus` |  | official_prop_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_024_start_055030ms` | 00:55.03 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_024_start_055030ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_024_NAUTILUS_PASS/candidate_reference_frames/R7_CAND_024_start_055030ms.jpg` |
| `R7_CAND_024_middle_056000ms` | 00:56.00 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_024_middle_056000ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_024_NAUTILUS_PASS/candidate_reference_frames/R7_CAND_024_middle_056000ms.jpg` |
| `R7_CAND_024_end_056970ms` | 00:56.97 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_024_end_056970ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_024_NAUTILUS_PASS/candidate_reference_frames/R7_CAND_024_end_056970ms.jpg` |

## Active Asset Locks

- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_024_NAUTILUS_PASS.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_024_NAUTILUS_PASS`.
Time range: `00:55.00-00:57.00`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: 潜艇水下通过中段。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
