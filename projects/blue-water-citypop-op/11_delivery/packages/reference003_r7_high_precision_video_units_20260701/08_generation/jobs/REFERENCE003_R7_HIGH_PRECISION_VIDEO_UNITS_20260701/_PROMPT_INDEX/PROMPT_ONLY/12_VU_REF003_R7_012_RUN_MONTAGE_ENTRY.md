# 12 — VU_REF003_R7_012_RUN_MONTAGE_ENTRY — 奔跑Montage入场

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_012_RUN_MONTAGE_ENTRY/reference_clip/VU_REF003_R7_012_RUN_MONTAGE_ENTRY_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_016` (00:37.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_012_RUN_MONTAGE_ENTRY/keyframes/01_OP_SHOT_016.png`
- 图2: `R5_VU_REF003_010_GRANDIS_TRIO_INTRO_037500ms_02` (00:37.50, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_012_RUN_MONTAGE_ENTRY/keyframes/02_R5_VU_REF003_010_GRANDIS_TRIO_INTRO_037500ms_02.png`
- 图3: `OP_SHOT_017` (00:38.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_012_RUN_MONTAGE_ENTRY/keyframes/03_OP_SHOT_017.png`
3. Active asset locks:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_012_start_037234ms` (start, 00:37.23, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_012_RUN_MONTAGE_ENTRY/candidate_reference_frames/R7_CAND_012_start_037234ms.jpg`
- `R7_CAND_012_end_038091ms` (end, 00:38.09, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_012_RUN_MONTAGE_ENTRY/candidate_reference_frames/R7_CAND_012_end_038091ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_012_RUN_MONTAGE_ENTRY.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_012_RUN_MONTAGE_ENTRY`.
Time range: `00:37.20-00:38.12`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: 奔跑 montage 入场短切。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
