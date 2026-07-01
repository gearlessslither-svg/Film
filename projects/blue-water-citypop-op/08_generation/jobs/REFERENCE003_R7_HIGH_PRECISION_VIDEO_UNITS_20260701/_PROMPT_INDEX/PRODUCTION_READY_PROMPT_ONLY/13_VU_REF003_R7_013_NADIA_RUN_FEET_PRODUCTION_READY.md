# 13 - VU_REF003_R7_013_NADIA_RUN_FEET - Nadia奔跑脚步

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:38.12-00:39.50`
- Shot intent: Nadia 奔跑脚步/身体节拍，不生成性感化身体强调。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_013_NADIA_RUN_FEET/reference_clip/VU_REF003_R7_013_NADIA_RUN_FEET_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_017` | 00:38.00 | 图1 / Nadia_run_feet | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_013_NADIA_RUN_FEET/keyframes/01_OP_SHOT_017.png` |
| `official_keyframe` | `OP_SHOT_018` | 00:39.50 | 图2 / Nadia_run_front | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_013_NADIA_RUN_FEET/keyframes/02_OP_SHOT_018.png` |
| `r7_generated_candidate` | `R7_CAND_013_start_038151ms` | 00:38.15 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_013_start_038151ms.png` |
| `r7_generated_candidate` | `R7_CAND_013_middle_038811ms` | 00:38.81 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_013_middle_038811ms.png` |
| `r7_generated_candidate` | `R7_CAND_013_end_039470ms` | 00:39.47 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_013_end_039470ms.png` |
| `asset_lock:characters` | `nadia` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png` |
| `asset_lock:props_vehicles_symbols` | `blue_water_pendant` |  | official_prop_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_013_start_038151ms` | 00:38.15 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_013_start_038151ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_013_NADIA_RUN_FEET/candidate_reference_frames/R7_CAND_013_start_038151ms.jpg` |
| `R7_CAND_013_middle_038811ms` | 00:38.81 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_013_middle_038811ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_013_NADIA_RUN_FEET/candidate_reference_frames/R7_CAND_013_middle_038811ms.jpg` |
| `R7_CAND_013_end_039470ms` | 00:39.47 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_013_end_039470ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_013_NADIA_RUN_FEET/candidate_reference_frames/R7_CAND_013_end_039470ms.jpg` |

## Active Asset Locks

- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_013_NADIA_RUN_FEET.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_013_NADIA_RUN_FEET`.
Time range: `00:38.12-00:39.50`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Nadia 奔跑脚步/身体节拍，不生成性感化身体强调。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
