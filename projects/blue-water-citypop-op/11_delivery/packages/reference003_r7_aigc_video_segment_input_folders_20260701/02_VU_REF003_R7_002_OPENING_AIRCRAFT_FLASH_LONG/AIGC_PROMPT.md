# 02 - VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG - 开场长段B：白鸟云层到飞行器闪现

- Status: organized input folder; visual quality is not yet re-approved.
- Time range: `00:07.00-00:16.50`
- Shot intent: 保留白鸟/云层长运动，并精准抓住 00:14.72 飞行器一闪。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG_reference.mp4`
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `r5_adaptive_generated` | `R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01` | 00:07.00 | adaptive_primary | `02_keyframes_for_upload/01_r5_adaptive_generated_R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01.png` |
| 2 | `official_keyframe` | `OP_SHOT_005` | 00:07.50 | 图1 / no_text_credit_safe_bird | `02_keyframes_for_upload/02_official_keyframe_OP_SHOT_005.png` |
| 3 | `official_keyframe` | `OP_SHOT_006` | 00:11.50 | 图2 / cloud_bank_growth | `02_keyframes_for_upload/03_official_keyframe_OP_SHOT_006.png` |
| 4 | `r5_adaptive_generated` | `R5_VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS_014000ms_01` | 00:14.00 | adaptive_primary | `02_keyframes_for_upload/04_r5_adaptive_generated_R5_VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS_014000ms_01.png` |
| 5 | `r5_adaptive_generated` | `R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_014500ms_02` | 00:14.50 | adaptive_middle | `02_keyframes_for_upload/05_r5_adaptive_generated_R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_014500ms_02.png` |
| 6 | `official_keyframe` | `OP_SHOT_007` | 00:15.00 | 图1 / aircraft_brief_reveal | `02_keyframes_for_upload/06_official_keyframe_OP_SHOT_007.png` |
| 7 | `r5_adaptive_generated` | `R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_016000ms_01` | 00:16.00 | adaptive_primary | `02_keyframes_for_upload/07_r5_adaptive_generated_R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_016000ms_01.png` |
| 8 | `r7_generated_candidate` | `R7_CAND_002_start_007030ms` | 00:07.03 | start | `02_keyframes_for_upload/08_r7_generated_R7_CAND_002_start_007030ms.png` |
| 9 | `r7_generated_candidate` | `R7_CAND_002_middle_011750ms` | 00:11.75 | middle | `02_keyframes_for_upload/09_r7_generated_R7_CAND_002_middle_011750ms.png` |
| 10 | `r7_generated_candidate` | `R7_CAND_002_end_016470ms` | 00:16.47 | end | `02_keyframes_for_upload/10_r7_generated_R7_CAND_002_end_016470ms.png` |

## Asset Locks

- `white_bird` (official_prop_lock): `03_asset_locks_for_upload/01_props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `03_asset_locks_for_upload/02_props_vehicles_symbols_jean_aircraft.png`

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_002_start_007030ms` | 00:07.03 | start | `04_source_reference_frames_audit_only/01_R7_CAND_002_start_007030ms.jpg` |
| `R7_CAND_002_middle_011750ms` | 00:11.75 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_002_middle_011750ms.jpg` |
| `R7_CAND_002_end_016470ms` | 00:16.47 | end | `04_source_reference_frames_audit_only/03_R7_CAND_002_end_016470ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_002_OPENING_AIRCRAFT_FLASH_LONG`.
Time range: `00:07.00-00:16.50`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: 保留白鸟/云层长运动，并精准抓住 00:14.72 飞行器一闪。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.
