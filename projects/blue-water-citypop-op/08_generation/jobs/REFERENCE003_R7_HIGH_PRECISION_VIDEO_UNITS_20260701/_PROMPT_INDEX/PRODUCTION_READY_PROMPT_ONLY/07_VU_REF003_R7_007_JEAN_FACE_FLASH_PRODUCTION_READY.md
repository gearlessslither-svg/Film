# 07 - VU_REF003_R7_007_JEAN_FACE_FLASH - Jean帽子正脸短插

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:28.86-00:29.49`
- Shot intent: Jean 正脸/帽子短促亮相，单独约束 Jean 身份。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_007_JEAN_FACE_FLASH/reference_clip/VU_REF003_R7_007_JEAN_FACE_FLASH_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_012` | 00:29.00 | 图1 / Jean_hat_face | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_007_JEAN_FACE_FLASH/keyframes/01_OP_SHOT_012.png` |
| `r7_generated_candidate` | `R7_CAND_007_start_028892ms` | 00:28.89 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_007_start_028892ms.png` |
| `r7_generated_candidate` | `R7_CAND_007_end_029458ms` | 00:29.46 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_007_end_029458ms.png` |
| `asset_lock:characters` | `jean` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_007_start_028892ms` | 00:28.89 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_007_start_028892ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_007_JEAN_FACE_FLASH/candidate_reference_frames/R7_CAND_007_start_028892ms.jpg` |
| `R7_CAND_007_end_029458ms` | 00:29.46 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_007_end_029458ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_007_JEAN_FACE_FLASH/candidate_reference_frames/R7_CAND_007_end_029458ms.jpg` |

## Active Asset Locks

- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_007_JEAN_FACE_FLASH.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_007_JEAN_FACE_FLASH`.
Time range: `00:28.86-00:29.49`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Jean 正脸/帽子短促亮相，单独约束 Jean 身份。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
