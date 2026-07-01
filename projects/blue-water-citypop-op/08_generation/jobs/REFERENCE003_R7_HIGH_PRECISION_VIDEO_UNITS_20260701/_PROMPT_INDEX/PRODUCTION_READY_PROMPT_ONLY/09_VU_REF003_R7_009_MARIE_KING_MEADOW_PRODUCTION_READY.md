# 09 - VU_REF003_R7_009_MARIE_KING_MEADOW - Marie与King草地段

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:31.95-00:33.95`
- Shot intent: Marie 与 King 草地亮相，儿童/动物锁定。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_009_MARIE_KING_MEADOW/reference_clip/VU_REF003_R7_009_MARIE_KING_MEADOW_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `official_keyframe` | `OP_SHOT_014` | 00:34.00 | 图2 / Marie_King_close | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_009_MARIE_KING_MEADOW/keyframes/01_OP_SHOT_014.png` |
| `r7_generated_candidate` | `R7_CAND_009_start_031979ms` | 00:31.98 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_009_start_031979ms.png` |
| `r7_generated_candidate` | `R7_CAND_009_middle_032950ms` | 00:32.95 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_009_middle_032950ms.png` |
| `r7_generated_candidate` | `R7_CAND_009_end_033921ms` | 00:33.92 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_009_end_033921ms.png` |
| `asset_lock:characters` | `marie` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_marie.png` |
| `asset_lock:characters` | `king` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_king.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_009_start_031979ms` | 00:31.98 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_009_start_031979ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_009_MARIE_KING_MEADOW/candidate_reference_frames/R7_CAND_009_start_031979ms.jpg` |
| `R7_CAND_009_middle_032950ms` | 00:32.95 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_009_middle_032950ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_009_MARIE_KING_MEADOW/candidate_reference_frames/R7_CAND_009_middle_032950ms.jpg` |
| `R7_CAND_009_end_033921ms` | 00:33.92 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_009_end_033921ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_009_MARIE_KING_MEADOW/candidate_reference_frames/R7_CAND_009_end_033921ms.jpg` |

## Active Asset Locks

- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_king.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_009_MARIE_KING_MEADOW.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_009_MARIE_KING_MEADOW`.
Time range: `00:31.95-00:33.95`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: Marie 与 King 草地亮相，儿童/动物锁定。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
