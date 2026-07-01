# 25 - VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT - Nautilus光带变化

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:57.00-00:58.50`
- Shot intent: 水下光带/潜艇剪影变化。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT/reference_clip/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `r5_adaptive_generated` | `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_057000ms_03` | 00:57.00 | adaptive_middle | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT/keyframes/01_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_057000ms_03.png` |
| `official_keyframe` | `OP_SHOT_028` | 00:58.50 | 图3 / undersea_shadow | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT/keyframes/02_OP_SHOT_028.png` |
| `r7_generated_candidate` | `R7_CAND_025_start_057030ms` | 00:57.03 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_025_start_057030ms.png` |
| `r7_generated_candidate` | `R7_CAND_025_middle_057750ms` | 00:57.75 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_025_middle_057750ms.png` |
| `r7_generated_candidate` | `R7_CAND_025_end_058470ms` | 00:58.47 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_025_end_058470ms.png` |
| `asset_lock:props_vehicles_symbols` | `nautilus` |  | official_prop_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_025_start_057030ms` | 00:57.03 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_025_start_057030ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT/candidate_reference_frames/R7_CAND_025_start_057030ms.jpg` |
| `R7_CAND_025_middle_057750ms` | 00:57.75 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_025_middle_057750ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT/candidate_reference_frames/R7_CAND_025_middle_057750ms.jpg` |
| `R7_CAND_025_end_058470ms` | 00:58.47 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_025_end_058470ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT/candidate_reference_frames/R7_CAND_025_end_058470ms.jpg` |

## Active Asset Locks

- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT`.
Time range: `00:57.00-00:58.50`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: 水下光带/潜艇剪影变化。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
