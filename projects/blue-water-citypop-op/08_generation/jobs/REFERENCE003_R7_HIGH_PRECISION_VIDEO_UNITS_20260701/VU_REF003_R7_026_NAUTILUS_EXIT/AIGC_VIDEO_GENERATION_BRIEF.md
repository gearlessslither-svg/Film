# 26 — VU_REF003_R7_026_NAUTILUS_EXIT — Nautilus海底尾段

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_026_NAUTILUS_EXIT/reference_clip/VU_REF003_R7_026_NAUTILUS_EXIT_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_028` (00:58.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_026_NAUTILUS_EXIT/keyframes/01_OP_SHOT_028.png`
- 图2: `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_060500ms_02` (01:00.50, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_026_NAUTILUS_EXIT/keyframes/02_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_060500ms_02.png`
- 图3: `OP_SHOT_029` (01:01.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_026_NAUTILUS_EXIT/keyframes/03_OP_SHOT_029.png`
3. Active asset locks:
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_026_start_058530ms` (start, 00:58.53, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_026_NAUTILUS_EXIT/candidate_reference_frames/R7_CAND_026_start_058530ms.jpg`
- `R7_CAND_026_end_061406ms` (end, 01:01.41, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_026_NAUTILUS_EXIT/candidate_reference_frames/R7_CAND_026_end_061406ms.jpg`
- `R7_CAND_026_middle_059968ms` (middle, 00:59.97, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_026_NAUTILUS_EXIT/candidate_reference_frames/R7_CAND_026_middle_059968ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_026_NAUTILUS_EXIT.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_026_NAUTILUS_EXIT`.
Time range: `00:58.50-01:01.44`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Nautilus 海底尾段，不生成原片职员表文字。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
