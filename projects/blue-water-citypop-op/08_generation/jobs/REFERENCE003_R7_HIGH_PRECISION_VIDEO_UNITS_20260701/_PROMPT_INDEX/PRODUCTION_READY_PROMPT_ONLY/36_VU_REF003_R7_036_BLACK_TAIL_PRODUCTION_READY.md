# 36 - VU_REF003_R7_036_BLACK_TAIL - 黑场尾帧

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `01:23.58-01:24.42`
- Shot intent: 黑场尾帧。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_036_BLACK_TAIL/reference_clip/VU_REF003_R7_036_BLACK_TAIL_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_042` | 01:23.50 | 图1 / black_tail | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_036_BLACK_TAIL/keyframes/01_OP_SHOT_042.png` |
| `r7_generated_candidate` | `R7_CAND_036_start_083614ms` | 01:23.61 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_036_start_083614ms.png` |
| `r7_generated_candidate` | `R7_CAND_036_end_084388ms` | 01:24.39 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_036_end_084388ms.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_036_start_083614ms` | 01:23.61 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_036_start_083614ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_036_BLACK_TAIL/candidate_reference_frames/R7_CAND_036_start_083614ms.jpg` |
| `R7_CAND_036_end_084388ms` | 01:24.39 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_036_end_084388ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_036_BLACK_TAIL/candidate_reference_frames/R7_CAND_036_end_084388ms.jpg` |

## Active Asset Locks

- none

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_036_BLACK_TAIL.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_036_BLACK_TAIL`.
Time range: `01:23.58-01:24.42`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: 黑场尾帧。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
