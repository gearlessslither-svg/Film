# 29 — VU_REF003_R7_029_NEMO_SUNSET_PROFILE — Nemo夕景肖像长段

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_029_NEMO_SUNSET_PROFILE/reference_clip/VU_REF003_R7_029_NEMO_SUNSET_PROFILE_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_032` (01:06.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_029_NEMO_SUNSET_PROFILE/keyframes/01_OP_SHOT_032.png`
- 图2: `OP_SHOT_033` (01:09.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_029_NEMO_SUNSET_PROFILE/keyframes/02_OP_SHOT_033.png`
3. Active asset locks:
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nemo.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_029_start_066054ms` (start, 01:06.05, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_029_NEMO_SUNSET_PROFILE/candidate_reference_frames/R7_CAND_029_start_066054ms.jpg`
- `R7_CAND_029_end_071333ms` (end, 01:11.33, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_029_NEMO_SUNSET_PROFILE/candidate_reference_frames/R7_CAND_029_end_071333ms.jpg`
- `R7_CAND_029_middle_068694ms` (middle, 01:08.69, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_029_NEMO_SUNSET_PROFILE/candidate_reference_frames/R7_CAND_029_middle_068694ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_029_NEMO_SUNSET_PROFILE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_029_NEMO_SUNSET_PROFILE`.
Time range: `01:06.02-01:11.36`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Nemo 船长夕景肖像长段，首尾/中间关键帧承载连续运动。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
