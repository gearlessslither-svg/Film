# 22 — VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA — 群像到海底过渡

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA/reference_clip/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_025` (00:51.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA/keyframes/01_OP_SHOT_025.png`
- 图2: `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_052000ms_01` (00:52.00, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA/keyframes/02_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_052000ms_01.png`
- 图3: `OP_SHOT_026` (00:52.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA/keyframes/03_OP_SHOT_026.png`
3. Active asset locks:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_king.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_022_start_050706ms` (start, 00:50.71, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA/candidate_reference_frames/R7_CAND_022_start_050706ms.jpg`
- `R7_CAND_022_end_052397ms` (end, 00:52.40, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA/candidate_reference_frames/R7_CAND_022_end_052397ms.jpg`
- `R7_CAND_022_middle_051552ms` (middle, 00:51.55, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA/candidate_reference_frames/R7_CAND_022_middle_051552ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA`.
Time range: `00:50.68-00:52.43`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: 群像 tableau 过渡进入 Nautilus 海底段。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
