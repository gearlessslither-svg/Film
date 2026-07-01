# 01 - VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG - 开场长段A：黑场云层到白鸟入画

- Status: organized input folder; visual quality is not yet re-approved.
- Time range: `00:00.00-00:07.00`
- Shot intent: 连续天空开场，黑场/云层/白鸟作为一个长运动短语处理。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG_reference.mp4`
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `official_keyframe` | `OP_SHOT_001` | 00:00.00 | 图1 / black_to_cloud_start | `02_keyframes_for_upload/01_official_keyframe_OP_SHOT_001.png` |
| 2 | `official_keyframe` | `OP_SHOT_002` | 00:01.50 | 图2 / bright_cloud_sky_reveal | `02_keyframes_for_upload/02_official_keyframe_OP_SHOT_002.png` |
| 3 | `official_keyframe` | `OP_SHOT_003` | 00:02.50 | 图1 / bird_entry | `02_keyframes_for_upload/03_official_keyframe_OP_SHOT_003.png` |
| 4 | `r5_adaptive_generated` | `R5_VU_REF003_002_WHITE_BIRD_SKY_003500ms_02` | 00:03.50 | adaptive_middle | `02_keyframes_for_upload/04_r5_adaptive_generated_R5_VU_REF003_002_WHITE_BIRD_SKY_003500ms_02.png` |
| 5 | `official_keyframe` | `OP_SHOT_004` | 00:05.00 | 图2 / bird_glide | `02_keyframes_for_upload/05_official_keyframe_OP_SHOT_004.png` |
| 6 | `r5_adaptive_generated` | `R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01` | 00:07.00 | adaptive_primary | `02_keyframes_for_upload/06_r5_adaptive_generated_R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01.png` |
| 7 | `r7_generated_candidate` | `R7_CAND_001_start_000030ms` | 00:00.03 | start | `02_keyframes_for_upload/07_r7_generated_R7_CAND_001_start_000030ms.png` |
| 8 | `r7_generated_candidate` | `R7_CAND_001_middle_003500ms` | 00:03.50 | middle | `02_keyframes_for_upload/08_r7_generated_R7_CAND_001_middle_003500ms.png` |
| 9 | `r7_generated_candidate` | `R7_CAND_001_end_006970ms` | 00:06.97 | end | `02_keyframes_for_upload/09_r7_generated_R7_CAND_001_end_006970ms.png` |

## Asset Locks

- `white_bird` (official_prop_lock): `03_asset_locks_for_upload/01_props_vehicles_symbols_white_bird.png`

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_001_start_000030ms` | 00:00.03 | start | `04_source_reference_frames_audit_only/01_R7_CAND_001_start_000030ms.jpg` |
| `R7_CAND_001_middle_003500ms` | 00:03.50 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_001_middle_003500ms.jpg` |
| `R7_CAND_001_end_006970ms` | 00:06.97 | end | `04_source_reference_frames_audit_only/03_R7_CAND_001_end_006970ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG`.
Time range: `00:00.00-00:07.00`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: 连续天空开场，黑场/云层/白鸟作为一个长运动短语处理。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.
