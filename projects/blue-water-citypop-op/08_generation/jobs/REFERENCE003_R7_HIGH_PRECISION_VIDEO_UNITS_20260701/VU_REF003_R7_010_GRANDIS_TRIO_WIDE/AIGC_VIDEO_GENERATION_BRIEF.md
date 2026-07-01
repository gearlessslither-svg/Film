# 10 — VU_REF003_R7_010_GRANDIS_TRIO_WIDE — Grandis三人组广角

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_010_GRANDIS_TRIO_WIDE/reference_clip/VU_REF003_R7_010_GRANDIS_TRIO_WIDE_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_014` (00:34.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_010_GRANDIS_TRIO_WIDE/keyframes/01_OP_SHOT_014.png`
- 图2: `R5_VU_REF003_010_GRANDIS_TRIO_INTRO_034500ms_01` (00:34.50, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_010_GRANDIS_TRIO_WIDE/keyframes/02_R5_VU_REF003_010_GRANDIS_TRIO_INTRO_034500ms_01.png`
- 图3: `OP_SHOT_015` (00:35.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_010_GRANDIS_TRIO_WIDE/keyframes/03_OP_SHOT_015.png`
3. Active asset locks:
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_hanson.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_010_start_033981ms` (start, 00:33.98, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_010_GRANDIS_TRIO_WIDE/candidate_reference_frames/R7_CAND_010_start_033981ms.jpg`
- `R7_CAND_010_end_035923ms` (end, 00:35.92, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_010_GRANDIS_TRIO_WIDE/candidate_reference_frames/R7_CAND_010_end_035923ms.jpg`
- `R7_CAND_010_middle_034952ms` (middle, 00:34.95, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_010_GRANDIS_TRIO_WIDE/candidate_reference_frames/R7_CAND_010_middle_034952ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_010_GRANDIS_TRIO_WIDE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_010_GRANDIS_TRIO_WIDE`.
Time range: `00:33.95-00:35.95`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Grandis 三人组广角亮相。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
