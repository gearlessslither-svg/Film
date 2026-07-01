# 03 — VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA — 开场长段C：标题安全位到日光转Nadia

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/reference_clip/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `R5_VU_REF003_005_MAIN_TITLE_SAFE_HOLD_017000ms_01` (00:17.00, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/keyframes/01_R5_VU_REF003_005_MAIN_TITLE_SAFE_HOLD_017000ms_01.png`
- 图2: `OP_SHOT_008` (00:18.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/keyframes/02_OP_SHOT_008.png`
- 图3: `OP_SHOT_009` (00:23.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/keyframes/03_OP_SHOT_009.png`
- 图4: `R5_VU_REF003_006_SUN_FLARE_TO_NADIA_023500ms_01` (00:23.50, r5_adaptive_generated) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/keyframes/04_R5_VU_REF003_006_SUN_FLARE_TO_NADIA_023500ms_01.png`
- 图5: `OP_SHOT_010` (00:24.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/keyframes/05_OP_SHOT_010.png`
3. Active asset locks:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_003_start_016530ms` (start, 00:16.53, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/candidate_reference_frames/R7_CAND_003_start_016530ms.jpg`
- `R7_CAND_003_end_024770ms` (end, 00:24.77, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/candidate_reference_frames/R7_CAND_003_end_024770ms.jpg`
- `R7_CAND_003_middle_020650ms` (middle, 00:20.65, P2_review_after_p1): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/candidate_reference_frames/R7_CAND_003_middle_020650ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA`.
Time range: `00:16.50-00:24.80`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: 无字标题安全位、日光耀斑和 Nadia 首次显影作为开场收束。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
