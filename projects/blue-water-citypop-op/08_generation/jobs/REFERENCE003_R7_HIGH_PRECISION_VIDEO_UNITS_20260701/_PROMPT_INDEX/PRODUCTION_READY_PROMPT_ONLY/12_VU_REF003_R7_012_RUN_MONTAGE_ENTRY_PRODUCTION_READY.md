# 12 - VU_REF003_R7_012_RUN_MONTAGE_ENTRY - 奔跑Montage入场

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:37.20-00:38.12`
- Shot intent: 奔跑 montage 入场短切。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_012_RUN_MONTAGE_ENTRY/reference_clip/VU_REF003_R7_012_RUN_MONTAGE_ENTRY_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_016` | 00:37.00 | 图2 / Grandis_trio_close | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_012_RUN_MONTAGE_ENTRY/keyframes/01_OP_SHOT_016.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_010_GRANDIS_TRIO_INTRO_037500ms_02` | 00:37.50 | adaptive_middle | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_012_RUN_MONTAGE_ENTRY/keyframes/02_R5_VU_REF003_010_GRANDIS_TRIO_INTRO_037500ms_02.png` |
| `official_keyframe` | `OP_SHOT_017` | 00:38.00 | 图1 / Nadia_run_feet | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_012_RUN_MONTAGE_ENTRY/keyframes/03_OP_SHOT_017.png` |
| `r7_generated_candidate` | `R7_CAND_012_start_037234ms` | 00:37.23 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_012_start_037234ms.png` |
| `r7_generated_candidate` | `R7_CAND_012_end_038091ms` | 00:38.09 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_012_end_038091ms.png` |
| `asset_lock:characters` | `nadia` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_012_start_037234ms` | 00:37.23 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_012_start_037234ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_012_RUN_MONTAGE_ENTRY/candidate_reference_frames/R7_CAND_012_start_037234ms.jpg` |
| `R7_CAND_012_end_038091ms` | 00:38.09 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_012_end_038091ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_012_RUN_MONTAGE_ENTRY/candidate_reference_frames/R7_CAND_012_end_038091ms.jpg` |

## Active Asset Locks

- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_012_RUN_MONTAGE_ENTRY.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_012_RUN_MONTAGE_ENTRY`.
Time range: `00:37.20-00:38.12`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: 奔跑 montage 入场短切。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
