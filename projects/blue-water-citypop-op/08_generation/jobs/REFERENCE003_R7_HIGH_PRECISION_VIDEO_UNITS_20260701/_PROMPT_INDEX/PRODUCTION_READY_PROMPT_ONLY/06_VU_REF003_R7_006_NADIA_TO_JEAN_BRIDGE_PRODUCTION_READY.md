# 06 - VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE - Nadia到Jean过渡

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:26.82-00:28.86`
- Shot intent: Nadia 段落向 Jean 入场切换，避免混淆人物归属。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/reference_clip/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_011` | 00:27.00 | 图2 / Nadia_close | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/keyframes/01_OP_SHOT_011.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_007_NADIA_PROFILE_ENTRY_027500ms_01` | 00:27.50 | adaptive_primary | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/keyframes/02_R5_VU_REF003_007_NADIA_PROFILE_ENTRY_027500ms_01.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_008_JEAN_INTRO_028500ms_02` | 00:28.50 | adaptive_middle | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/keyframes/03_R5_VU_REF003_008_JEAN_INTRO_028500ms_02.png` |
| `official_keyframe` | `OP_SHOT_012` | 00:29.00 | 图1 / Jean_hat_face | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/keyframes/04_OP_SHOT_012.png` |
| `r7_generated_candidate` | `R7_CAND_006_start_026848ms` | 00:26.85 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_006_start_026848ms.png` |
| `r7_generated_candidate` | `R7_CAND_006_middle_027840ms` | 00:27.84 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_006_middle_027840ms.png` |
| `r7_generated_candidate` | `R7_CAND_006_end_028832ms` | 00:28.83 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_006_end_028832ms.png` |
| `asset_lock:characters` | `nadia` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png` |
| `asset_lock:characters` | `jean` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png` |
| `asset_lock:props_vehicles_symbols` | `blue_water_pendant` |  | official_prop_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_006_start_026848ms` | 00:26.85 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_006_start_026848ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/candidate_reference_frames/R7_CAND_006_start_026848ms.jpg` |
| `R7_CAND_006_middle_027840ms` | 00:27.84 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_006_middle_027840ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/candidate_reference_frames/R7_CAND_006_middle_027840ms.jpg` |
| `R7_CAND_006_end_028832ms` | 00:28.83 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_006_end_028832ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/candidate_reference_frames/R7_CAND_006_end_028832ms.jpg` |

## Active Asset Locks

- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png`
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE`.
Time range: `00:26.82-00:28.86`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Nadia 段落向 Jean 入场切换，避免混淆人物归属。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
