# 01 - VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG - 开场长段A：黑场云层到白鸟入画

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:00.00-00:07.00`
- Shot intent: 连续天空开场，黑场/云层/白鸟作为一个长运动短语处理。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/reference_clip/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_001` | 00:00.00 | 图1 / black_to_cloud_start | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/keyframes/01_OP_SHOT_001.png` |
| `official_keyframe` | `OP_SHOT_002` | 00:01.50 | 图2 / bright_cloud_sky_reveal | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/keyframes/02_OP_SHOT_002.png` |
| `official_keyframe` | `OP_SHOT_003` | 00:02.50 | 图1 / bird_entry | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/keyframes/03_OP_SHOT_003.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_002_WHITE_BIRD_SKY_003500ms_02` | 00:03.50 | adaptive_middle | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/keyframes/04_R5_VU_REF003_002_WHITE_BIRD_SKY_003500ms_02.png` |
| `official_keyframe` | `OP_SHOT_004` | 00:05.00 | 图2 / bird_glide | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/keyframes/05_OP_SHOT_004.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01` | 00:07.00 | adaptive_primary | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/keyframes/06_R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01.png` |
| `r7_generated_candidate` | `R7_CAND_001_start_000030ms` | 00:00.03 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_001_start_000030ms.png` |
| `r7_generated_candidate` | `R7_CAND_001_middle_003500ms` | 00:03.50 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_001_middle_003500ms.png` |
| `r7_generated_candidate` | `R7_CAND_001_end_006970ms` | 00:06.97 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_001_end_006970ms.png` |
| `asset_lock:props_vehicles_symbols` | `white_bird` |  | official_prop_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_white_bird.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_001_start_000030ms` | 00:00.03 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_001_start_000030ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/candidate_reference_frames/R7_CAND_001_start_000030ms.jpg` |
| `R7_CAND_001_middle_003500ms` | 00:03.50 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_001_middle_003500ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/candidate_reference_frames/R7_CAND_001_middle_003500ms.jpg` |
| `R7_CAND_001_end_006970ms` | 00:06.97 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_001_end_006970ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG/candidate_reference_frames/R7_CAND_001_end_006970ms.jpg` |

## Active Asset Locks

- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_white_bird.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG`.
Time range: `00:00.00-00:07.00`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: 连续天空开场，黑场/云层/白鸟作为一个长运动短语处理。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
