# 29 - VU_REF003_R7_029_NEMO_SUNSET_PROFILE - Nemo夕景肖像长段

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `01:06.02-01:11.36`
- Shot intent: Nemo 船长夕景肖像长段，首尾/中间关键帧承载连续运动。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_029_NEMO_SUNSET_PROFILE/reference_clip/VU_REF003_R7_029_NEMO_SUNSET_PROFILE_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_032` | 01:06.50 | 图1 / Nemo_profile_start | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_029_NEMO_SUNSET_PROFILE/keyframes/01_OP_SHOT_032.png` |
| `official_keyframe` | `OP_SHOT_033` | 01:09.50 | 图2 / Nemo_profile_hold | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_029_NEMO_SUNSET_PROFILE/keyframes/02_OP_SHOT_033.png` |
| `r7_generated_candidate` | `R7_CAND_029_start_066054ms` | 01:06.05 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_029_start_066054ms.png` |
| `r7_generated_candidate` | `R7_CAND_029_middle_068694ms` | 01:08.69 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_029_middle_068694ms.png` |
| `r7_generated_candidate` | `R7_CAND_029_end_071333ms` | 01:11.33 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_029_end_071333ms.png` |
| `asset_lock:characters` | `nemo` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nemo.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_029_start_066054ms` | 01:06.05 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_029_start_066054ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_029_NEMO_SUNSET_PROFILE/candidate_reference_frames/R7_CAND_029_start_066054ms.jpg` |
| `R7_CAND_029_middle_068694ms` | 01:08.69 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_029_middle_068694ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_029_NEMO_SUNSET_PROFILE/candidate_reference_frames/R7_CAND_029_middle_068694ms.jpg` |
| `R7_CAND_029_end_071333ms` | 01:11.33 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_029_end_071333ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_029_NEMO_SUNSET_PROFILE/candidate_reference_frames/R7_CAND_029_end_071333ms.jpg` |

## Active Asset Locks

- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nemo.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_029_NEMO_SUNSET_PROFILE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_029_NEMO_SUNSET_PROFILE`.
Time range: `01:06.02-01:11.36`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Nemo 船长夕景肖像长段，首尾/中间关键帧承载连续运动。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
