# 14 — VU_REF003_R7_014_NADIA_RUN_FRONT — Nadia正面奔跑

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_014_NADIA_RUN_FRONT/reference_clip/VU_REF003_R7_014_NADIA_RUN_FRONT_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_018` (00:39.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_014_NADIA_RUN_FRONT/keyframes/01_OP_SHOT_018.png`
- 图2: `OP_SHOT_019` (00:41.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_014_NADIA_RUN_FRONT/keyframes/02_OP_SHOT_019.png`
3. Active asset locks:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_014_start_039530ms` (start, 00:39.53, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_014_NADIA_RUN_FRONT/candidate_reference_frames/R7_CAND_014_start_039530ms.jpg`
- `R7_CAND_014_end_041470ms` (end, 00:41.47, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_014_NADIA_RUN_FRONT/candidate_reference_frames/R7_CAND_014_end_041470ms.jpg`
- `R7_CAND_014_middle_040500ms` (middle, 00:40.50, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_014_NADIA_RUN_FRONT/candidate_reference_frames/R7_CAND_014_middle_040500ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_014_NADIA_RUN_FRONT.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_014_NADIA_RUN_FRONT`.
Time range: `00:39.50-00:41.50`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Nadia 正面奔跑节拍。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
