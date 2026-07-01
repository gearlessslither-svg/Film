# 23 — VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY — Nautilus海底入场

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY/reference_clip/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_026` (00:52.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY/keyframes/01_OP_SHOT_026.png`
- 图2: `OP_SHOT_027` (00:55.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY/keyframes/02_OP_SHOT_027.png`
3. Active asset locks:
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_023_start_052457ms` (start, 00:52.46, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY/candidate_reference_frames/R7_CAND_023_start_052457ms.jpg`
- `R7_CAND_023_end_054970ms` (end, 00:54.97, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY/candidate_reference_frames/R7_CAND_023_end_054970ms.jpg`
- `R7_CAND_023_middle_053713ms` (middle, 00:53.71, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY/candidate_reference_frames/R7_CAND_023_middle_053713ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_023_NAUTILUS_UNDERSEA_ENTRY`.
Time range: `00:52.43-00:55.00`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Nautilus 海底入场，水下光束与潜艇比例锁定。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
