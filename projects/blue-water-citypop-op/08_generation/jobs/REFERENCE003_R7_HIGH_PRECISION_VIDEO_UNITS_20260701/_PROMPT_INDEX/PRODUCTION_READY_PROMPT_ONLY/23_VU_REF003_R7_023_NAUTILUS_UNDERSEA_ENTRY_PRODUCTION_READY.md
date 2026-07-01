# 23 - VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY - Nautilus海底入场

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:52.43-00:55.00`
- Shot intent: Nautilus 海底入场，水下光束与潜艇比例锁定。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY/reference_clip/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_026` | 00:52.50 | 图1 / undersea_start | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY/keyframes/01_OP_SHOT_026.png` |
| `official_keyframe` | `OP_SHOT_027` | 00:55.00 | 图2 / undersea_pass | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY/keyframes/02_OP_SHOT_027.png` |
| `r7_generated_candidate` | `R7_CAND_023_start_052457ms` | 00:52.46 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_023_start_052457ms.png` |
| `r7_generated_candidate` | `R7_CAND_023_middle_053713ms` | 00:53.71 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_023_middle_053713ms.png` |
| `r7_generated_candidate` | `R7_CAND_023_end_054970ms` | 00:54.97 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_023_end_054970ms.png` |
| `asset_lock:props_vehicles_symbols` | `nautilus` |  | official_prop_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_023_start_052457ms` | 00:52.46 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_023_start_052457ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY/candidate_reference_frames/R7_CAND_023_start_052457ms.jpg` |
| `R7_CAND_023_middle_053713ms` | 00:53.71 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_023_middle_053713ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY/candidate_reference_frames/R7_CAND_023_middle_053713ms.jpg` |
| `R7_CAND_023_end_054970ms` | 00:54.97 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_023_end_054970ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY/candidate_reference_frames/R7_CAND_023_end_054970ms.jpg` |

## Active Asset Locks

- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY`.
Time range: `00:52.43-00:55.00`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Nautilus 海底入场，水下光束与潜艇比例锁定。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
