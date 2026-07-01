# 24 — VU_REF003_R7_024_NAUTILUS_PASS — Nautilus水下通过

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_024_NAUTILUS_PASS/reference_clip/VU_REF003_R7_024_NAUTILUS_PASS_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_027` (00:55.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_024_NAUTILUS_PASS/keyframes/01_OP_SHOT_027.png`
- 图2: `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_057000ms_03` (00:57.00, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_024_NAUTILUS_PASS/keyframes/02_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_057000ms_03.png`
3. Active asset locks:
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_024_start_055030ms` (start, 00:55.03, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_024_NAUTILUS_PASS/candidate_reference_frames/R7_CAND_024_start_055030ms.jpg`
- `R7_CAND_024_end_056970ms` (end, 00:56.97, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_024_NAUTILUS_PASS/candidate_reference_frames/R7_CAND_024_end_056970ms.jpg`
- `R7_CAND_024_middle_056000ms` (middle, 00:56.00, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_024_NAUTILUS_PASS/candidate_reference_frames/R7_CAND_024_middle_056000ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_024_NAUTILUS_PASS.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_024_NAUTILUS_PASS`.
Time range: `00:55.00-00:57.00`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: 潜艇水下通过中段。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
