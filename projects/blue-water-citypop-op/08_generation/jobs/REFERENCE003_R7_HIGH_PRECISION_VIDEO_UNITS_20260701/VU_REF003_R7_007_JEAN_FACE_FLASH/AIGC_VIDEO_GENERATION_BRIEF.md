# 07 — VU_REF003_R7_007_JEAN_FACE_FLASH — Jean帽子正脸短插

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_007_JEAN_FACE_FLASH/reference_clip/VU_REF003_R7_007_JEAN_FACE_FLASH_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_012` (00:29.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_007_JEAN_FACE_FLASH/keyframes/01_OP_SHOT_012.png`
3. Active asset locks:
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_007_start_028892ms` (start, 00:28.89, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_007_JEAN_FACE_FLASH/candidate_reference_frames/R7_CAND_007_start_028892ms.jpg`
- `R7_CAND_007_end_029458ms` (end, 00:29.46, P1_generate_next_small_batch): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_007_JEAN_FACE_FLASH/candidate_reference_frames/R7_CAND_007_end_029458ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_007_JEAN_FACE_FLASH.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_007_JEAN_FACE_FLASH`.
Time range: `00:28.86-00:29.49`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Jean 正脸/帽子短促亮相，单独约束 Jean 身份。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
