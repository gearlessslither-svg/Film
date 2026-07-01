# 30 — VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL — Nadia庄重到宝石

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL/reference_clip/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_034` (01:12.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL/keyframes/01_OP_SHOT_034.png`
- 图2: `OP_SHOT_035` (01:13.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL/keyframes/02_OP_SHOT_035.png`
- 图3: `R5_VU_REF003_018_BLUE_WATER_SYMBOL_074000ms_01` (01:14.00, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL/keyframes/03_R5_VU_REF003_018_BLUE_WATER_SYMBOL_074000ms_01.png`
3. Active asset locks:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_030_start_071393ms` (start, 01:11.39, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL/candidate_reference_frames/R7_CAND_030_start_071393ms.jpg`
- `R7_CAND_030_end_074044ms` (end, 01:14.04, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL/candidate_reference_frames/R7_CAND_030_end_074044ms.jpg`
- `R7_CAND_030_middle_072718ms` (middle, 01:12.72, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL/candidate_reference_frames/R7_CAND_030_middle_072718ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_030_NADIA_SOLEMN_TO_JEWEL`.
Time range: `01:11.36-01:14.07`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Nadia 庄重正面过渡到 Blue Water 象征。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
