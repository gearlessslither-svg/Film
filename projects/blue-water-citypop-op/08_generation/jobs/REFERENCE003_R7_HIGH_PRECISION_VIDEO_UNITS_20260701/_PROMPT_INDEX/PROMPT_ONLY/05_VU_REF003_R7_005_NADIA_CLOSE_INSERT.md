# 05 — VU_REF003_R7_005_NADIA_CLOSE_INSERT — Nadia近景插入

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_005_NADIA_CLOSE_INSERT/reference_clip/VU_REF003_R7_005_NADIA_CLOSE_INSERT_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_011` (00:27.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_005_NADIA_CLOSE_INSERT/keyframes/01_OP_SHOT_011.png`
### Newly Generated P1 Anchors (promoted pure-image assets)

- `R7_CAND_005_start_025931ms` (start, 00:25.93): `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_005_start_025931ms.png`

3. Active asset locks:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_005_start_025931ms` (start, 00:25.93, P1_generate_next_small_batch): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_005_NADIA_CLOSE_INSERT/candidate_reference_frames/R7_CAND_005_start_025931ms.jpg`
- `R7_CAND_005_end_026788ms` (end, 00:26.79, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_005_NADIA_CLOSE_INSERT/candidate_reference_frames/R7_CAND_005_end_026788ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_005_NADIA_CLOSE_INSERT.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_005_NADIA_CLOSE_INSERT`.
Time range: `00:25.90-00:26.82`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Nadia 从侧脸进入更近的人物状态。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
