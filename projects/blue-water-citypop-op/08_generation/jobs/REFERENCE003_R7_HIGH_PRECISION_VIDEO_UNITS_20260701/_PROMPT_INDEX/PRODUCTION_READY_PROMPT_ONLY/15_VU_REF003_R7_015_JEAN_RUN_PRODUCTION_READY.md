# 15 - VU_REF003_R7_015_JEAN_RUN - Jean奔跑

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:41.50-00:43.50`
- Shot intent: Jean 独立奔跑节拍。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_015_JEAN_RUN/reference_clip/VU_REF003_R7_015_JEAN_RUN_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_019` | 00:41.50 | 图3 / Jean_run | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_015_JEAN_RUN/keyframes/01_OP_SHOT_019.png` |
| `official_keyframe` | `OP_SHOT_020` | 00:43.50 | 图4 / Marie_run | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_015_JEAN_RUN/keyframes/02_OP_SHOT_020.png` |
| `r7_generated_candidate` | `R7_CAND_015_start_041530ms` | 00:41.53 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_015_start_041530ms.png` |
| `r7_generated_candidate` | `R7_CAND_015_middle_042500ms` | 00:42.50 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_015_middle_042500ms.png` |
| `r7_generated_candidate` | `R7_CAND_015_end_043470ms` | 00:43.47 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_015_end_043470ms.png` |
| `asset_lock:characters` | `jean` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_015_start_041530ms` | 00:41.53 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_015_start_041530ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_015_JEAN_RUN/candidate_reference_frames/R7_CAND_015_start_041530ms.jpg` |
| `R7_CAND_015_middle_042500ms` | 00:42.50 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_015_middle_042500ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_015_JEAN_RUN/candidate_reference_frames/R7_CAND_015_middle_042500ms.jpg` |
| `R7_CAND_015_end_043470ms` | 00:43.47 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_015_end_043470ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_015_JEAN_RUN/candidate_reference_frames/R7_CAND_015_end_043470ms.jpg` |

## Active Asset Locks

- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_015_JEAN_RUN.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_015_JEAN_RUN`.
Time range: `00:41.50-00:43.50`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Jean 独立奔跑节拍。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
