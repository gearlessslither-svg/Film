# 34 - VU_REF003_R7_034_FINAL_SKY_TRANSITION - 最终天空转场

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `01:19.20-01:20.79`
- Shot intent: 水花后转入最终无字天空。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_034_FINAL_SKY_TRANSITION/reference_clip/VU_REF003_R7_034_FINAL_SKY_TRANSITION_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_039` | 01:19.00 | 图2 / splash_to_sky | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_034_FINAL_SKY_TRANSITION/keyframes/01_OP_SHOT_039.png` |
| `official_keyframe` | `OP_SHOT_040` | 01:20.00 | 图1 / final_sky_safe | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_034_FINAL_SKY_TRANSITION/keyframes/02_OP_SHOT_040.png` |
| `r7_generated_candidate` | `R7_CAND_034_start_079234ms` | 01:19.23 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_034_start_079234ms.png` |
| `r7_generated_candidate` | `R7_CAND_034_middle_079996ms` | 01:20.00 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_034_middle_079996ms.png` |
| `r7_generated_candidate` | `R7_CAND_034_end_080759ms` | 01:20.76 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_034_end_080759ms.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_034_start_079234ms` | 01:19.23 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_034_start_079234ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_034_FINAL_SKY_TRANSITION/candidate_reference_frames/R7_CAND_034_start_079234ms.jpg` |
| `R7_CAND_034_middle_079996ms` | 01:20.00 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_034_middle_079996ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_034_FINAL_SKY_TRANSITION/candidate_reference_frames/R7_CAND_034_middle_079996ms.jpg` |
| `R7_CAND_034_end_080759ms` | 01:20.76 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_034_end_080759ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_034_FINAL_SKY_TRANSITION/candidate_reference_frames/R7_CAND_034_end_080759ms.jpg` |

## Active Asset Locks

- none

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_034_FINAL_SKY_TRANSITION.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_034_FINAL_SKY_TRANSITION`.
Time range: `01:19.20-01:20.79`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: 水花后转入最终无字天空。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
