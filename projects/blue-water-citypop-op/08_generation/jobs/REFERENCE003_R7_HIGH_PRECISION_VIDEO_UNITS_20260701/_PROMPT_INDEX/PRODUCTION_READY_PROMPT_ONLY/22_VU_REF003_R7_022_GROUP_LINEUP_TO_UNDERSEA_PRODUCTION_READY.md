# 22 - VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA - 群像到海底过渡

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:50.68-00:52.43`
- Shot intent: 群像 tableau 过渡进入 Nautilus 海底段。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA/reference_clip/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_025` | 00:51.50 | 图3 / group_lineup | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA/keyframes/01_OP_SHOT_025.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_052000ms_01` | 00:52.00 | adaptive_primary | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA/keyframes/02_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_052000ms_01.png` |
| `official_keyframe` | `OP_SHOT_026` | 00:52.50 | 图1 / undersea_start | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA/keyframes/03_OP_SHOT_026.png` |
| `r7_generated_candidate` | `R7_CAND_022_start_050706ms` | 00:50.71 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_022_start_050706ms.png` |
| `r7_generated_candidate` | `R7_CAND_022_middle_051552ms` | 00:51.55 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_022_middle_051552ms.png` |
| `r7_generated_candidate` | `R7_CAND_022_end_052397ms` | 00:52.40 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_022_end_052397ms.png` |
| `asset_lock:characters` | `nadia` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png` |
| `asset_lock:characters` | `jean` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png` |
| `asset_lock:characters` | `marie` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_marie.png` |
| `asset_lock:characters` | `king` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_king.png` |
| `asset_lock:props_vehicles_symbols` | `nautilus` |  | official_prop_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_022_start_050706ms` | 00:50.71 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_022_start_050706ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA/candidate_reference_frames/R7_CAND_022_start_050706ms.jpg` |
| `R7_CAND_022_middle_051552ms` | 00:51.55 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_022_middle_051552ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA/candidate_reference_frames/R7_CAND_022_middle_051552ms.jpg` |
| `R7_CAND_022_end_052397ms` | 00:52.40 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_022_end_052397ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA/candidate_reference_frames/R7_CAND_022_end_052397ms.jpg` |

## Active Asset Locks

- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_king.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_nautilus.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_022_GROUP_LINEUP_TO_UNDERSEA`.
Time range: `00:50.68-00:52.43`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: 群像 tableau 过渡进入 Nautilus 海底段。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
