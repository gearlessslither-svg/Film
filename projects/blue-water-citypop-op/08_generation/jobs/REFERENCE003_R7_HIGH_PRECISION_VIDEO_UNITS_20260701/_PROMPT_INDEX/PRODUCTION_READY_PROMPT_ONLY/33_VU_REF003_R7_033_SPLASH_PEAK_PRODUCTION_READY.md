# 33 - VU_REF003_R7_033_SPLASH_PEAK - 水花爆发峰值

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `01:17.79-01:19.20`
- Shot intent: 水花爆发峰值与天空转场。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_033_SPLASH_PEAK/reference_clip/VU_REF003_R7_033_SPLASH_PEAK_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_038` | 01:18.00 | 图1 / water_burst | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_033_SPLASH_PEAK/keyframes/01_OP_SHOT_038.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_019_WATER_SPLASH_TRANSITION_078500ms_01` | 01:18.50 | adaptive_primary | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_033_SPLASH_PEAK/keyframes/02_R5_VU_REF003_019_WATER_SPLASH_TRANSITION_078500ms_01.png` |
| `official_keyframe` | `OP_SHOT_039` | 01:19.00 | 图2 / splash_to_sky | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_033_SPLASH_PEAK/keyframes/03_OP_SHOT_039.png` |
| `r7_generated_candidate` | `R7_CAND_033_start_077816ms` | 01:17.82 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_033_start_077816ms.png` |
| `r7_generated_candidate` | `R7_CAND_033_middle_078495ms` | 01:18.50 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_033_middle_078495ms.png` |
| `r7_generated_candidate` | `R7_CAND_033_end_079174ms` | 01:19.17 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_033_end_079174ms.png` |
| `asset_lock:props_vehicles_symbols` | `water_burst_transition` |  | official_transition_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_water_burst_transition.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_033_start_077816ms` | 01:17.82 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_033_start_077816ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_033_SPLASH_PEAK/candidate_reference_frames/R7_CAND_033_start_077816ms.jpg` |
| `R7_CAND_033_middle_078495ms` | 01:18.50 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_033_middle_078495ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_033_SPLASH_PEAK/candidate_reference_frames/R7_CAND_033_middle_078495ms.jpg` |
| `R7_CAND_033_end_079174ms` | 01:19.17 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_033_end_079174ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_033_SPLASH_PEAK/candidate_reference_frames/R7_CAND_033_end_079174ms.jpg` |

## Active Asset Locks

- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_water_burst_transition.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_033_SPLASH_PEAK.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_033_SPLASH_PEAK`.
Time range: `01:17.79-01:19.20`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: 水花爆发峰值与天空转场。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
