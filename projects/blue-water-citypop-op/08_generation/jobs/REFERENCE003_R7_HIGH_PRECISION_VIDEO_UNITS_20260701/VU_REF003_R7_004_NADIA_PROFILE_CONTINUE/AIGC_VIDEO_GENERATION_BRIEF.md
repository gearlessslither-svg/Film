# 04 — VU_REF003_R7_004_NADIA_PROFILE_CONTINUE — Nadia侧脸延续

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_004_NADIA_PROFILE_CONTINUE/reference_clip/VU_REF003_R7_004_NADIA_PROFILE_CONTINUE_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_010` (00:24.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_004_NADIA_PROFILE_CONTINUE/keyframes/01_OP_SHOT_010.png`
3. Active asset locks:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_004_start_024830ms` (start, 00:24.83, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_004_NADIA_PROFILE_CONTINUE/candidate_reference_frames/R7_CAND_004_start_024830ms.jpg`
- `R7_CAND_004_end_025871ms` (end, 00:25.87, P1_generate_next_small_batch): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_004_NADIA_PROFILE_CONTINUE/candidate_reference_frames/R7_CAND_004_end_025871ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_004_NADIA_PROFILE_CONTINUE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_004_NADIA_PROFILE_CONTINUE`.
Time range: `00:24.80-00:25.90`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Nadia 首次亮相后的侧脸延续，不并入 Jean。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
