# 35 - VU_REF003_R7_035_FINAL_SKY_HOLD - 最终天空Hold

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `01:20.79-01:23.58`
- Shot intent: 最终无字天空 hold。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_035_FINAL_SKY_HOLD/reference_clip/VU_REF003_R7_035_FINAL_SKY_HOLD_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_041` | 01:22.00 | 图2 / final_sun_hold | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_035_FINAL_SKY_HOLD/keyframes/01_OP_SHOT_041.png` |
| `official_keyframe` | `OP_SHOT_042` | 01:23.50 | 图1 / black_tail | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_035_FINAL_SKY_HOLD/keyframes/02_OP_SHOT_042.png` |
| `r7_generated_candidate` | `R7_CAND_035_start_080819ms` | 01:20.82 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_035_start_080819ms.png` |
| `r7_generated_candidate` | `R7_CAND_035_middle_082186ms` | 01:22.19 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_035_middle_082186ms.png` |
| `r7_generated_candidate` | `R7_CAND_035_end_083554ms` | 01:23.55 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_035_end_083554ms.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_035_start_080819ms` | 01:20.82 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_035_start_080819ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_035_FINAL_SKY_HOLD/candidate_reference_frames/R7_CAND_035_start_080819ms.jpg` |
| `R7_CAND_035_middle_082186ms` | 01:22.19 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_035_middle_082186ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_035_FINAL_SKY_HOLD/candidate_reference_frames/R7_CAND_035_middle_082186ms.jpg` |
| `R7_CAND_035_end_083554ms` | 01:23.55 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_035_end_083554ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_035_FINAL_SKY_HOLD/candidate_reference_frames/R7_CAND_035_end_083554ms.jpg` |

## Active Asset Locks

- none

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_035_FINAL_SKY_HOLD.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_035_FINAL_SKY_HOLD`.
Time range: `01:20.79-01:23.58`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: 最终无字天空 hold。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
