# 11 - VU_REF003_R7_011_GRANDIS_TRIO_CLOSE - Grandis三人组近景

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:35.95-00:37.20`
- Shot intent: Grandis 三人组近景/表演状态，不能和前一广角混成同一镜。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_011_GRANDIS_TRIO_CLOSE/reference_clip/VU_REF003_R7_011_GRANDIS_TRIO_CLOSE_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_016` | 00:37.00 | 图2 / Grandis_trio_close | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_011_GRANDIS_TRIO_CLOSE/keyframes/01_OP_SHOT_016.png` |
| `r7_generated_candidate` | `R7_CAND_011_start_035983ms` | 00:35.98 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_011_start_035983ms.png` |
| `r7_generated_candidate` | `R7_CAND_011_middle_036579ms` | 00:36.58 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_011_middle_036579ms.png` |
| `r7_generated_candidate` | `R7_CAND_011_end_037174ms` | 00:37.17 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_011_end_037174ms.png` |
| `asset_lock:characters` | `grandis` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_grandis.png` |
| `asset_lock:characters` | `sanson` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_sanson.png` |
| `asset_lock:characters` | `hanson` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_hanson.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_011_start_035983ms` | 00:35.98 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_011_start_035983ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_011_GRANDIS_TRIO_CLOSE/candidate_reference_frames/R7_CAND_011_start_035983ms.jpg` |
| `R7_CAND_011_middle_036579ms` | 00:36.58 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_011_middle_036579ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_011_GRANDIS_TRIO_CLOSE/candidate_reference_frames/R7_CAND_011_middle_036579ms.jpg` |
| `R7_CAND_011_end_037174ms` | 00:37.17 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_011_end_037174ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_011_GRANDIS_TRIO_CLOSE/candidate_reference_frames/R7_CAND_011_end_037174ms.jpg` |

## Active Asset Locks

- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_hanson.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_011_GRANDIS_TRIO_CLOSE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_011_GRANDIS_TRIO_CLOSE`.
Time range: `00:35.95-00:37.20`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Grandis 三人组近景/表演状态，不能和前一广角混成同一镜。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
