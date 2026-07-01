# 21 — VU_REF003_R7_021_VEHICLE_ARC — 车辆飞行动作

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_021_VEHICLE_ARC/reference_clip/VU_REF003_R7_021_VEHICLE_ARC_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_024` (00:49.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_021_VEHICLE_ARC/keyframes/01_OP_SHOT_024.png`
3. Active asset locks:
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_grandis_vehicle.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_021_start_049705ms` (start, 00:49.70, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_021_VEHICLE_ARC/candidate_reference_frames/R7_CAND_021_start_049705ms.jpg`
- `R7_CAND_021_end_050646ms` (end, 00:50.65, P1_generate_next_small_batch): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_021_VEHICLE_ARC/candidate_reference_frames/R7_CAND_021_end_050646ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_021_VEHICLE_ARC.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_021_VEHICLE_ARC`.
Time range: `00:49.67-00:50.68`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: 复古车辆/飞行器弧线动作。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
