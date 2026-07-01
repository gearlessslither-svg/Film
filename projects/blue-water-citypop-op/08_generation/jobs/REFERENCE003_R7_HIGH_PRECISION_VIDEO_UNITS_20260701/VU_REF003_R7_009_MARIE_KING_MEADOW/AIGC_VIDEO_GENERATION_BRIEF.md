# 09 — VU_REF003_R7_009_MARIE_KING_MEADOW — Marie与King草地段

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_009_MARIE_KING_MEADOW/reference_clip/VU_REF003_R7_009_MARIE_KING_MEADOW_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_014` (00:34.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_009_MARIE_KING_MEADOW/keyframes/01_OP_SHOT_014.png`
3. Active asset locks:
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_king.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_009_start_031979ms` (start, 00:31.98, P1_generate_next_small_batch): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_009_MARIE_KING_MEADOW/candidate_reference_frames/R7_CAND_009_start_031979ms.jpg`
- `R7_CAND_009_end_033921ms` (end, 00:33.92, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_009_MARIE_KING_MEADOW/candidate_reference_frames/R7_CAND_009_end_033921ms.jpg`
- `R7_CAND_009_middle_032950ms` (middle, 00:32.95, P1_generate_next_small_batch): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_009_MARIE_KING_MEADOW/candidate_reference_frames/R7_CAND_009_middle_032950ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_009_MARIE_KING_MEADOW.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_009_MARIE_KING_MEADOW`.
Time range: `00:31.95-00:33.95`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Marie 与 King 草地亮相，儿童/动物锁定。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
