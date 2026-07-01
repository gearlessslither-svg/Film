# 16 - VU_REF003_R7_016_MARIE_KING_RUN - Marie与King奔跑

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:43.50-00:45.50`
- Shot intent: Marie/King 独立奔跑节拍。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_016_MARIE_KING_RUN/reference_clip/VU_REF003_R7_016_MARIE_KING_RUN_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_020` | 00:43.50 | 图4 / Marie_run | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_016_MARIE_KING_RUN/keyframes/01_OP_SHOT_020.png` |
| `official_keyframe` | `OP_SHOT_021` | 00:45.50 | 图5 / group_run | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_016_MARIE_KING_RUN/keyframes/02_OP_SHOT_021.png` |
| `r7_generated_candidate` | `R7_CAND_016_start_043530ms` | 00:43.53 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_016_start_043530ms.png` |
| `r7_generated_candidate` | `R7_CAND_016_middle_044500ms` | 00:44.50 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_016_middle_044500ms.png` |
| `r7_generated_candidate` | `R7_CAND_016_end_045470ms` | 00:45.47 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_016_end_045470ms.png` |
| `asset_lock:characters` | `marie` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_marie.png` |
| `asset_lock:characters` | `king` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_king.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_016_start_043530ms` | 00:43.53 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_016_start_043530ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_016_MARIE_KING_RUN/candidate_reference_frames/R7_CAND_016_start_043530ms.jpg` |
| `R7_CAND_016_middle_044500ms` | 00:44.50 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_016_middle_044500ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_016_MARIE_KING_RUN/candidate_reference_frames/R7_CAND_016_middle_044500ms.jpg` |
| `R7_CAND_016_end_045470ms` | 00:45.47 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_016_end_045470ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_016_MARIE_KING_RUN/candidate_reference_frames/R7_CAND_016_end_045470ms.jpg` |

## Active Asset Locks

- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_king.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_016_MARIE_KING_RUN.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_016_MARIE_KING_RUN`.
Time range: `00:43.50-00:45.50`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Marie/King 独立奔跑节拍。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
