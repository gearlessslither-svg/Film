# 08 - VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE - Jean到Marie草地过渡

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:29.49-00:31.95`
- Shot intent: Jean 段落过渡到 Marie/King 草地段。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE/reference_clip/VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `r5_adaptive_generated` | `R5_VU_REF003_008_JEAN_INTRO_030500ms_01` | 00:30.50 | adaptive_primary | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE/keyframes/01_R5_VU_REF003_008_JEAN_INTRO_030500ms_01.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_009_MARIE_KING_MEADOW_031000ms_01` | 00:31.00 | adaptive_primary | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE/keyframes/02_R5_VU_REF003_009_MARIE_KING_MEADOW_031000ms_01.png` |
| `official_keyframe` | `OP_SHOT_013` | 00:31.50 | 图1 / Marie_King_meadow | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE/keyframes/03_OP_SHOT_013.png` |
| `r7_generated_candidate` | `R7_CAND_008_start_029518ms` | 00:29.52 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_008_start_029518ms.png` |
| `r7_generated_candidate` | `R7_CAND_008_middle_030718ms` | 00:30.72 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_008_middle_030718ms.png` |
| `r7_generated_candidate` | `R7_CAND_008_end_031919ms` | 00:31.92 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_008_end_031919ms.png` |
| `asset_lock:characters` | `jean` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png` |
| `asset_lock:characters` | `marie` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_marie.png` |
| `asset_lock:characters` | `king` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_king.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_008_start_029518ms` | 00:29.52 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_008_start_029518ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE/candidate_reference_frames/R7_CAND_008_start_029518ms.jpg` |
| `R7_CAND_008_middle_030718ms` | 00:30.72 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_008_middle_030718ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE/candidate_reference_frames/R7_CAND_008_middle_030718ms.jpg` |
| `R7_CAND_008_end_031919ms` | 00:31.92 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_008_end_031919ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE/candidate_reference_frames/R7_CAND_008_end_031919ms.jpg` |

## Active Asset Locks

- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_king.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE`.
Time range: `00:29.49-00:31.95`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Jean 段落过渡到 Marie/King 草地段。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
