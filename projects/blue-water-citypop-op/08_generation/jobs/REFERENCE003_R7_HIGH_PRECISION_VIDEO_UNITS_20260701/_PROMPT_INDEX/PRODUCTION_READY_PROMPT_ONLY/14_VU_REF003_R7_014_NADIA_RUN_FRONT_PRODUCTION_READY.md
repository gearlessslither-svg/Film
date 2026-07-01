# 14 - VU_REF003_R7_014_NADIA_RUN_FRONT - Nadia正面奔跑

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:39.50-00:41.50`
- Shot intent: Nadia 正面奔跑节拍。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_014_NADIA_RUN_FRONT/reference_clip/VU_REF003_R7_014_NADIA_RUN_FRONT_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_018` | 00:39.50 | 图2 / Nadia_run_front | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_014_NADIA_RUN_FRONT/keyframes/01_OP_SHOT_018.png` |
| `official_keyframe` | `OP_SHOT_019` | 00:41.50 | 图3 / Jean_run | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_014_NADIA_RUN_FRONT/keyframes/02_OP_SHOT_019.png` |
| `r7_generated_candidate` | `R7_CAND_014_start_039530ms` | 00:39.53 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_014_start_039530ms.png` |
| `r7_generated_candidate` | `R7_CAND_014_middle_040500ms` | 00:40.50 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_014_middle_040500ms.png` |
| `r7_generated_candidate` | `R7_CAND_014_end_041470ms` | 00:41.47 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_014_end_041470ms.png` |
| `asset_lock:characters` | `nadia` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png` |
| `asset_lock:props_vehicles_symbols` | `blue_water_pendant` |  | official_prop_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_014_start_039530ms` | 00:39.53 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_014_start_039530ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_014_NADIA_RUN_FRONT/candidate_reference_frames/R7_CAND_014_start_039530ms.jpg` |
| `R7_CAND_014_middle_040500ms` | 00:40.50 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_014_middle_040500ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_014_NADIA_RUN_FRONT/candidate_reference_frames/R7_CAND_014_middle_040500ms.jpg` |
| `R7_CAND_014_end_041470ms` | 00:41.47 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_014_end_041470ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_014_NADIA_RUN_FRONT/candidate_reference_frames/R7_CAND_014_end_041470ms.jpg` |

## Active Asset Locks

- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_014_NADIA_RUN_FRONT.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_014_NADIA_RUN_FRONT`.
Time range: `00:39.50-00:41.50`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Nadia 正面奔跑节拍。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
