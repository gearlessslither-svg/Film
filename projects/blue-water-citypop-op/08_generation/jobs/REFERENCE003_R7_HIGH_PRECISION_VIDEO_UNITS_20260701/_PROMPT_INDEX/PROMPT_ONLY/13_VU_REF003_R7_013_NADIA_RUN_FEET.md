# 13 — VU_REF003_R7_013_NADIA_RUN_FEET — Nadia奔跑脚步

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_013_NADIA_RUN_FEET/reference_clip/VU_REF003_R7_013_NADIA_RUN_FEET_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_017` (00:38.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_013_NADIA_RUN_FEET/keyframes/01_OP_SHOT_017.png`
- 图2: `OP_SHOT_018` (00:39.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_013_NADIA_RUN_FEET/keyframes/02_OP_SHOT_018.png`
### Newly Generated P1 Anchors (promoted pure-image assets)

- `R7_CAND_013_middle_038811ms` (middle, 00:38.81): `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_013_middle_038811ms.png`

3. Active asset locks:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_013_start_038151ms` (start, 00:38.15, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_013_NADIA_RUN_FEET/candidate_reference_frames/R7_CAND_013_start_038151ms.jpg`
- `R7_CAND_013_end_039470ms` (end, 00:39.47, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_013_NADIA_RUN_FEET/candidate_reference_frames/R7_CAND_013_end_039470ms.jpg`
- `R7_CAND_013_middle_038811ms` (middle, 00:38.81, P1_generate_next_small_batch): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_013_NADIA_RUN_FEET/candidate_reference_frames/R7_CAND_013_middle_038811ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_013_NADIA_RUN_FEET.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_013_NADIA_RUN_FEET`.
Time range: `00:38.12-00:39.50`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Nadia 奔跑脚步/身体节拍，不生成性感化身体强调。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
