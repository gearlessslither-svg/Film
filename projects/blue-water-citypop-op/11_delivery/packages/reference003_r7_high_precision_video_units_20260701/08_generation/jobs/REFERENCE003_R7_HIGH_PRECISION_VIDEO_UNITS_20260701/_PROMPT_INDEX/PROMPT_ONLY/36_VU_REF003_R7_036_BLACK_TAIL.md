# 36 — VU_REF003_R7_036_BLACK_TAIL — 黑场尾帧

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_036_BLACK_TAIL/reference_clip/VU_REF003_R7_036_BLACK_TAIL_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_042` (01:23.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_036_BLACK_TAIL/keyframes/01_OP_SHOT_042.png`
3. Active asset locks:
- none

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_036_start_083614ms` (start, 01:23.61, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_036_BLACK_TAIL/candidate_reference_frames/R7_CAND_036_start_083614ms.jpg`
- `R7_CAND_036_end_084388ms` (end, 01:24.39, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_036_BLACK_TAIL/candidate_reference_frames/R7_CAND_036_end_084388ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_036_BLACK_TAIL.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_036_BLACK_TAIL`.
Time range: `01:23.58-01:24.42`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: 黑场尾帧。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
