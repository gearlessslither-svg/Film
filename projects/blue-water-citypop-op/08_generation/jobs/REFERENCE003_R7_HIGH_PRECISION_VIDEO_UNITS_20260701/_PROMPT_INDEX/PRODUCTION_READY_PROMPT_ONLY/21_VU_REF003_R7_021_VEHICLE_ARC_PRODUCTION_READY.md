# 21 - VU_REF003_R7_021_VEHICLE_ARC - 车辆飞行动作

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:49.67-00:50.68`
- Shot intent: 复古车辆/飞行器弧线动作。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_021_VEHICLE_ARC/reference_clip/VU_REF003_R7_021_VEHICLE_ARC_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_024` | 00:49.50 | 图2 / vehicle_sky_action | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_021_VEHICLE_ARC/keyframes/01_OP_SHOT_024.png` |
| `r7_generated_candidate` | `R7_CAND_021_start_049705ms` | 00:49.70 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_021_start_049705ms.png` |
| `r7_generated_candidate` | `R7_CAND_021_end_050646ms` | 00:50.65 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_021_end_050646ms.png` |
| `asset_lock:props_vehicles_symbols` | `grandis_vehicle` |  | official_prop_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_grandis_vehicle.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_021_start_049705ms` | 00:49.70 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_021_start_049705ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_021_VEHICLE_ARC/candidate_reference_frames/R7_CAND_021_start_049705ms.jpg` |
| `R7_CAND_021_end_050646ms` | 00:50.65 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_021_end_050646ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_021_VEHICLE_ARC/candidate_reference_frames/R7_CAND_021_end_050646ms.jpg` |

## Active Asset Locks

- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_grandis_vehicle.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_021_VEHICLE_ARC.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_021_VEHICLE_ARC`.
Time range: `00:49.67-00:50.68`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: 复古车辆/飞行器弧线动作。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
