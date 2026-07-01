# 25 — VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT — Nautilus光带变化

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT/reference_clip/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_057000ms_03` (00:57.00, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT/keyframes/01_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_057000ms_03.png`
- 图2: `OP_SHOT_028` (00:58.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT/keyframes/02_OP_SHOT_028.png`
### Newly Generated P1 Anchors (promoted pure-image assets)

- `R7_CAND_025_middle_057750ms` (middle, 00:57.75): `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_025_middle_057750ms.png`

3. Active asset locks:
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_025_start_057030ms` (start, 00:57.03, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT/candidate_reference_frames/R7_CAND_025_start_057030ms.jpg`
- `R7_CAND_025_end_058470ms` (end, 00:58.47, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT/candidate_reference_frames/R7_CAND_025_end_058470ms.jpg`
- `R7_CAND_025_middle_057750ms` (middle, 00:57.75, P1_generate_next_small_batch): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT/candidate_reference_frames/R7_CAND_025_middle_057750ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_025_NAUTILUS_LIGHT_SHIFT`.
Time range: `00:57.00-00:58.50`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: 水下光带/潜艇剪影变化。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
