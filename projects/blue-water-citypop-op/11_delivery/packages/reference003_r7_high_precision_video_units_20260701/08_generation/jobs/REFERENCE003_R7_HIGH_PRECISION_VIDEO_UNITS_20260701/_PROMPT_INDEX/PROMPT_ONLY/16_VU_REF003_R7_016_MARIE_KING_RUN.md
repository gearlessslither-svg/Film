# 16 — VU_REF003_R7_016_MARIE_KING_RUN — Marie与King奔跑

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_016_MARIE_KING_RUN/reference_clip/VU_REF003_R7_016_MARIE_KING_RUN_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_020` (00:43.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_016_MARIE_KING_RUN/keyframes/01_OP_SHOT_020.png`
- 图2: `OP_SHOT_021` (00:45.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_016_MARIE_KING_RUN/keyframes/02_OP_SHOT_021.png`
3. Active asset locks:
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_king.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_016_start_043530ms` (start, 00:43.53, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_016_MARIE_KING_RUN/candidate_reference_frames/R7_CAND_016_start_043530ms.jpg`
- `R7_CAND_016_end_045470ms` (end, 00:45.47, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_016_MARIE_KING_RUN/candidate_reference_frames/R7_CAND_016_end_045470ms.jpg`
- `R7_CAND_016_middle_044500ms` (middle, 00:44.50, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_016_MARIE_KING_RUN/candidate_reference_frames/R7_CAND_016_middle_044500ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_016_MARIE_KING_RUN.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_016_MARIE_KING_RUN`.
Time range: `00:43.50-00:45.50`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Marie/King 独立奔跑节拍。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
