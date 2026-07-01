# 10 - VU_REF003_R7_010_GRANDIS_TRIO_WIDE - Grandis三人组广角

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:33.95-00:35.95`
- Shot intent: Grandis 三人组广角亮相。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_010_GRANDIS_TRIO_WIDE/reference_clip/VU_REF003_R7_010_GRANDIS_TRIO_WIDE_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_014` | 00:34.00 | 图2 / Marie_King_close | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_010_GRANDIS_TRIO_WIDE/keyframes/01_OP_SHOT_014.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_010_GRANDIS_TRIO_INTRO_034500ms_01` | 00:34.50 | adaptive_primary | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_010_GRANDIS_TRIO_WIDE/keyframes/02_R5_VU_REF003_010_GRANDIS_TRIO_INTRO_034500ms_01.png` |
| `official_keyframe` | `OP_SHOT_015` | 00:35.50 | 图1 / Grandis_trio_wide | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_010_GRANDIS_TRIO_WIDE/keyframes/03_OP_SHOT_015.png` |
| `r7_generated_candidate` | `R7_CAND_010_start_033981ms` | 00:33.98 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_010_start_033981ms.png` |
| `r7_generated_candidate` | `R7_CAND_010_middle_034952ms` | 00:34.95 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_010_middle_034952ms.png` |
| `r7_generated_candidate` | `R7_CAND_010_end_035923ms` | 00:35.92 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_010_end_035923ms.png` |
| `asset_lock:characters` | `grandis` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_grandis.png` |
| `asset_lock:characters` | `sanson` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_sanson.png` |
| `asset_lock:characters` | `hanson` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_hanson.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_010_start_033981ms` | 00:33.98 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_010_start_033981ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_010_GRANDIS_TRIO_WIDE/candidate_reference_frames/R7_CAND_010_start_033981ms.jpg` |
| `R7_CAND_010_middle_034952ms` | 00:34.95 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_010_middle_034952ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_010_GRANDIS_TRIO_WIDE/candidate_reference_frames/R7_CAND_010_middle_034952ms.jpg` |
| `R7_CAND_010_end_035923ms` | 00:35.92 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_010_end_035923ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_010_GRANDIS_TRIO_WIDE/candidate_reference_frames/R7_CAND_010_end_035923ms.jpg` |

## Active Asset Locks

- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_hanson.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_010_GRANDIS_TRIO_WIDE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_010_GRANDIS_TRIO_WIDE`.
Time range: `00:33.95-00:35.95`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Grandis 三人组广角亮相。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
