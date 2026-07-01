# 03 - VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA - 开场长段C：标题安全位到日光转Nadia

- Created: 2026-07-01T17:55:37+08:00
- Status: production-ready AIGC video input pack
- Time range: `00:16.50-00:24.80`
- Shot intent: 无字标题安全位、日光耀斑和 Nadia 首次显影作为开场收束。

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/reference_clip/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA_reference.mp4`
2. All image inputs below, in the listed order.
3. This prompt document.

## All Image Inputs

| Kind | ID | Time | Role | Path |
|---|---|---:|---|---|
| `r5_adaptive_generated` | `R5_VU_REF003_005_MAIN_TITLE_SAFE_HOLD_017000ms_01` | 00:17.00 | adaptive_primary | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/keyframes/01_R5_VU_REF003_005_MAIN_TITLE_SAFE_HOLD_017000ms_01.png` |
| `official_keyframe` | `OP_SHOT_008` | 00:18.50 | 图1 / main_title_safe_no_text | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/keyframes/02_OP_SHOT_008.png` |
| `official_keyframe` | `OP_SHOT_009` | 00:23.00 | 图1 / sun_flare_transition | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/keyframes/03_OP_SHOT_009.png` |
| `r5_adaptive_generated` | `R5_VU_REF003_006_SUN_FLARE_TO_NADIA_023500ms_01` | 00:23.50 | adaptive_primary | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/keyframes/04_R5_VU_REF003_006_SUN_FLARE_TO_NADIA_023500ms_01.png` |
| `official_keyframe` | `OP_SHOT_010` | 00:24.50 | 图1 / Nadia_profile | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/keyframes/05_OP_SHOT_010.png` |
| `r7_generated_candidate` | `R7_CAND_003_start_016530ms` | 00:16.53 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_003_start_016530ms.png` |
| `r7_generated_candidate` | `R7_CAND_003_middle_020650ms` | 00:20.65 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_003_middle_020650ms.png` |
| `r7_generated_candidate` | `R7_CAND_003_end_024770ms` | 00:24.77 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_003_end_024770ms.png` |
| `asset_lock:characters` | `nadia` |  | official_identity_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png` |
| `asset_lock:props_vehicles_symbols` | `blue_water_pendant` |  | official_prop_lock | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png` |

## R7 Generated Candidate Anchors

These are now pure generated image assets, not screenshot-only placeholders.

| Asset | Time | Role | Generated image | Source reference frame |
|---|---:|---|---|---|
| `R7_CAND_003_start_016530ms` | 00:16.53 | start | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_003_start_016530ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/candidate_reference_frames/R7_CAND_003_start_016530ms.jpg` |
| `R7_CAND_003_middle_020650ms` | 00:20.65 | middle | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_003_middle_020650ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/candidate_reference_frames/R7_CAND_003_middle_020650ms.jpg` |
| `R7_CAND_003_end_024770ms` | 00:24.77 | end | `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/R7_CAND_003_end_024770ms.png` | `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA/candidate_reference_frames/R7_CAND_003_end_024770ms.jpg` |

## Active Asset Locks

- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/characters_nadia.png`
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_003_OPENING_TITLE_FLARE_NADIA`.
Time range: `00:16.50-00:24.80`.

Use the reference video clip as the primary source for timing, camera motion,
screen direction, and edit rhythm. Use every image listed above as the visual
world for identity, props, vehicle shapes, scene geometry, color, and continuity.
The R7 generated candidate anchors are pure generated assets and should be
treated as current image inputs.

Shot intent: 无字标题安全位、日光耀斑和 Nadia 首次显影作为开场收束。

Preserve active locks exactly when visible. Keep minors age-appropriate and
non-sexualized. Replace all readable original titles, credits, lyrics, subtitles,
broadcaster marks, logos, watermarks, and random glyphs with clean no-text
composition. Keep keyframes in timeline order.

Reject if this segment absorbs a neighboring flash, drops a listed image input,
invents readable text, redesigns visible locked assets, or turns a montage/short
insert into a false continuous one-take.
