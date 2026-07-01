# 26 - VU_REF003_R7_026_NAUTILUS_EXIT - Nautilus海底尾段

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:58.50-01:01.44`
- Shot intent: Nautilus 海底尾段，不生成原片职员表文字。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_026_NAUTILUS_EXIT/reference_clip/VU_REF003_R7_026_NAUTILUS_EXIT_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_028` | 00:58.50 | 图3 / undersea_shadow | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_026_NAUTILUS_EXIT/keyframes/01_OP_SHOT_028.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_060500ms_02` | 01:00.50 | adaptive_middle | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_026_NAUTILUS_EXIT/keyframes/02_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_060500ms_02.png` |
| `official_keyframe` | `OP_SHOT_029` | 01:01.50 | 图1 / night_city_reveal | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_026_NAUTILUS_EXIT/keyframes/03_OP_SHOT_029.png` |
| `r7_generated_candidate` | `R7_CAND_026_start_058530ms` | 00:58.53 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_026_start_058530ms.png` |
| `r7_generated_candidate` | `R7_CAND_026_middle_059968ms` | 00:59.97 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_026_middle_059968ms.png` |
| `r7_generated_candidate` | `R7_CAND_026_end_061406ms` | 01:01.41 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_026_end_061406ms.png` |
| `asset_lock:props_vehicles_symbols` | `nautilus` |  | official_prop_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_026_start_058530ms` | 00:58.53 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_026_start_058530ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_026_NAUTILUS_EXIT/candidate_reference_frames/R7_CAND_026_start_058530ms.jpg` |
| `R7_CAND_026_middle_059968ms` | 00:59.97 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_026_middle_059968ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_026_NAUTILUS_EXIT/candidate_reference_frames/R7_CAND_026_middle_059968ms.jpg` |
| `R7_CAND_026_end_061406ms` | 01:01.41 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_026_end_061406ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_026_NAUTILUS_EXIT/candidate_reference_frames/R7_CAND_026_end_061406ms.jpg` |

## Active Asset Locks

- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_026_NAUTILUS_EXIT.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_026_NAUTILUS_EXIT`.
Time range: `00:58.50-01:01.44`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Nautilus 海底尾段，不生成原片职员表文字。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
