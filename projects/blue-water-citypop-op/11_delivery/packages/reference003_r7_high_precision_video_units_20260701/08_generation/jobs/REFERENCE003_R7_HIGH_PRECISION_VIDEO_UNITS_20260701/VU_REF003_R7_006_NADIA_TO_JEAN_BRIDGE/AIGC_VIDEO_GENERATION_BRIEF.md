# 06 — VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE — Nadia到Jean过渡

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/reference_clip/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_011` (00:27.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/keyframes/01_OP_SHOT_011.png`
- 图2: `R5_VU_REF003_007_NADIA_PROFILE_ENTRY_027500ms_01` (00:27.50, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/keyframes/02_R5_VU_REF003_007_NADIA_PROFILE_ENTRY_027500ms_01.png`
- 图3: `R5_VU_REF003_008_JEAN_INTRO_028500ms_02` (00:28.50, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/keyframes/03_R5_VU_REF003_008_JEAN_INTRO_028500ms_02.png`
- 图4: `OP_SHOT_012` (00:29.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/keyframes/04_OP_SHOT_012.png`
3. Active asset locks:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png`
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_006_start_026848ms` (start, 00:26.85, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/candidate_reference_frames/R7_CAND_006_start_026848ms.jpg`
- `R7_CAND_006_end_028832ms` (end, 00:28.83, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/candidate_reference_frames/R7_CAND_006_end_028832ms.jpg`
- `R7_CAND_006_middle_027840ms` (middle, 00:27.84, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE/candidate_reference_frames/R7_CAND_006_middle_027840ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE`.
Time range: `00:26.82-00:28.86`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Nadia 段落向 Jean 入场切换，避免混淆人物归属。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
