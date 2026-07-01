# 11 — VU_REF003_R7_011_GRANDIS_TRIO_CLOSE — Grandis三人组近景

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_011_GRANDIS_TRIO_CLOSE/reference_clip/VU_REF003_R7_011_GRANDIS_TRIO_CLOSE_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_016` (00:37.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_011_GRANDIS_TRIO_CLOSE/keyframes/01_OP_SHOT_016.png`
### Newly Generated P1 Anchors (promoted pure-image assets)

- `R7_CAND_011_start_035983ms` (start, 00:35.98): `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_011_start_035983ms.png`
- `R7_CAND_011_middle_036579ms` (middle, 00:36.58): `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_011_middle_036579ms.png`

3. Active asset locks:
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_hanson.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_011_start_035983ms` (start, 00:35.98, P1_generate_next_small_batch): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_011_GRANDIS_TRIO_CLOSE/candidate_reference_frames/R7_CAND_011_start_035983ms.jpg`
- `R7_CAND_011_end_037174ms` (end, 00:37.17, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_011_GRANDIS_TRIO_CLOSE/candidate_reference_frames/R7_CAND_011_end_037174ms.jpg`
- `R7_CAND_011_middle_036579ms` (middle, 00:36.58, P1_generate_next_small_batch): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_011_GRANDIS_TRIO_CLOSE/candidate_reference_frames/R7_CAND_011_middle_036579ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_011_GRANDIS_TRIO_CLOSE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_011_GRANDIS_TRIO_CLOSE`.
Time range: `00:35.95-00:37.20`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Grandis 三人组近景/表演状态，不能和前一广角混成同一镜。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
