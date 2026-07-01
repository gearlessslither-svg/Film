# 20 — VU_REF003_R7_020_VEHICLE_PREP_FLASH — 车辆动作预备闪帧

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_020_VEHICLE_PREP_FLASH/reference_clip/VU_REF003_R7_020_VEHICLE_PREP_FLASH_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_024` (00:49.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_020_VEHICLE_PREP_FLASH/keyframes/01_OP_SHOT_024.png`
### Newly Generated P1 Anchors (promoted pure-image assets)

- `R7_CAND_020_start_048704ms` (start, 00:48.70): `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_020_start_048704ms.png`

3. Active asset locks:
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_hanson.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_grandis_vehicle.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_020_start_048704ms` (start, 00:48.70, P1_generate_next_small_batch): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_020_VEHICLE_PREP_FLASH/candidate_reference_frames/R7_CAND_020_start_048704ms.jpg`
- `R7_CAND_020_end_049645ms` (end, 00:49.64, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_020_VEHICLE_PREP_FLASH/candidate_reference_frames/R7_CAND_020_end_049645ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_020_VEHICLE_PREP_FLASH.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_020_VEHICLE_PREP_FLASH`.
Time range: `00:48.67-00:49.67`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: 车辆动作前的短暂准备/闪帧。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
