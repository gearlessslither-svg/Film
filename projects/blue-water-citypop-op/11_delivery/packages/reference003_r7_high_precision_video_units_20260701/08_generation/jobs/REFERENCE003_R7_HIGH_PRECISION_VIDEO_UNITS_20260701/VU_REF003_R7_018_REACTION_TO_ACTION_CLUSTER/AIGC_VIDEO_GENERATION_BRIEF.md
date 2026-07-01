# 18 — VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER — 奔跑到动作插入簇

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER/reference_clip/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER_reference.mp4`
2. Current ordered generated anchors, including latest official + R5 generated images:
- 图1: `OP_SHOT_022` (00:47.50, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER/keyframes/01_OP_SHOT_022.png`
- 图2: `OP_SHOT_023` (00:48.00, official_keyframe) `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER/keyframes/02_OP_SHOT_023.png`
3. Active asset locks:
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_hanson.png`

## Candidate Screenshots For New Image Generation

These are not final assets yet. Use them to generate pure image anchors if the unit needs
more visual states after director review.

- `R7_CAND_018_start_047452ms` (start, 00:47.45, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER/candidate_reference_frames/R7_CAND_018_start_047452ms.jpg`
- `R7_CAND_018_end_048143ms` (end, 00:48.14, P3_reference_video_or_already_handled): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER/candidate_reference_frames/R7_CAND_018_end_048143ms.jpg`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER`.
Time range: `00:47.42-00:48.17`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use the ordered generated anchors above as the
current visual world; they include the latest R5 generated images where available.
Do not rely on older unit prompt text if it omits these anchors.

Shot intent: Jean反应/动作桥接短簇，避免被吞进奔跑长段。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring character flash, drops a listed
generated anchor, invents readable text, redesigns visible locked assets, or
turns a montage/short insert into a false continuous one-take.
