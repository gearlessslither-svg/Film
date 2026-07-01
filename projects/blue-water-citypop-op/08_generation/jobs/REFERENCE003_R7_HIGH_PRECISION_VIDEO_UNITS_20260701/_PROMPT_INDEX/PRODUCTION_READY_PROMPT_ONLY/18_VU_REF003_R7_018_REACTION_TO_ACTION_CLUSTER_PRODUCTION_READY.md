# 18 - VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER - 奔跑到动作插入簇

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:47.42-00:48.17`
- Shot intent: Jean反应/动作桥接短簇，避免被吞进奔跑长段。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER/reference_clip/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_022` | 00:47.50 | 图6 / Jean_reaction_close | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER/keyframes/01_OP_SHOT_022.png` |
| `official_keyframe` | `OP_SHOT_023` | 00:48.00 | 图1 / Grandis_action_close | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER/keyframes/02_OP_SHOT_023.png` |
| `r7_generated_candidate` | `R7_CAND_018_start_047452ms` | 00:47.45 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_018_start_047452ms.png` |
| `r7_generated_candidate` | `R7_CAND_018_end_048143ms` | 00:48.14 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_018_end_048143ms.png` |
| `asset_lock:characters` | `jean` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png` |
| `asset_lock:characters` | `grandis` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_grandis.png` |
| `asset_lock:characters` | `sanson` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_sanson.png` |
| `asset_lock:characters` | `hanson` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_hanson.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_018_start_047452ms` | 00:47.45 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_018_start_047452ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER/candidate_reference_frames/R7_CAND_018_start_047452ms.jpg` |
| `R7_CAND_018_end_048143ms` | 00:48.14 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_018_end_048143ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER/candidate_reference_frames/R7_CAND_018_end_048143ms.jpg` |

## Active Asset Locks

- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_hanson.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER`.
Time range: `00:47.42-00:48.17`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Jean反应/动作桥接短簇，避免被吞进奔跑长段。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
