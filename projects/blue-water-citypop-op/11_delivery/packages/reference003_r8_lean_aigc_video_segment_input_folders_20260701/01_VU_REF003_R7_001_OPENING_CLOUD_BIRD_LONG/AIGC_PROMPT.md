# 01 - VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG - 开场长段A：黑场云层到白鸟入画

- Status: lean QA-recovery input folder; R7 candidates are reference-only.
- Time range: `00:00.00-00:07.00`
- Shot intent: 连续天空开场，黑场/云层/白鸟作为一个长运动短语处理。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_001_OPENING_CLOUD_BIRD_LONG_reference_upload_h264_aac.mp4` (upload-compatible H.264/AAC MP4)
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `r5_adaptive_generated` | `R5_VU_REF003_002_WHITE_BIRD_SKY_003500ms_02` | 00:03.50 | adaptive_middle | `02_keyframes_for_upload/01_r5_adaptive_generated_R5_VU_REF003_002_WHITE_BIRD_SKY_003500ms_02.png` |
| 2 | `r5_adaptive_generated` | `R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01` | 00:07.00 | adaptive_primary | `02_keyframes_for_upload/02_r5_adaptive_generated_R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01.png` |

## Asset Locks

- `white_bird` (official_prop_lock): `03_asset_locks_for_upload/01_props_vehicles_symbols_white_bird.png`

## R7 Generated Candidates, Reference Only

These images are included for review/reference only and are not part of the default upload image set for this lean package.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_001_start_000030ms` | 00:00.03 | start | `05_r7_generated_candidates_reference_only/01_R7_CAND_001_start_000030ms.png` |
| `R7_CAND_001_middle_003500ms` | 00:03.50 | middle | `05_r7_generated_candidates_reference_only/02_R7_CAND_001_middle_003500ms.png` |
| `R7_CAND_001_end_006970ms` | 00:06.97 | end | `05_r7_generated_candidates_reference_only/03_R7_CAND_001_end_006970ms.png` |

## Official Original Keyframes, Reference Only

These original-style frames are included for timing/composition audit only. Do not upload them as target-style keyframes unless the director explicitly asks for that specific unit.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `OP_SHOT_001` | 00:00.00 | 图1 / black_to_cloud_start | `06_official_original_keyframes_reference_only/01_official_keyframe_OP_SHOT_001.png` |
| `OP_SHOT_002` | 00:01.50 | 图2 / bright_cloud_sky_reveal | `06_official_original_keyframes_reference_only/02_official_keyframe_OP_SHOT_002.png` |
| `OP_SHOT_003` | 00:02.50 | 图1 / bird_entry | `06_official_original_keyframes_reference_only/03_official_keyframe_OP_SHOT_003.png` |
| `OP_SHOT_004` | 00:05.00 | 图2 / bird_glide | `06_official_original_keyframes_reference_only/04_official_keyframe_OP_SHOT_004.png` |

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

Lean package note: R7 generated candidates are deliberately excluded from the
default image upload set after the 161-frame R7 preview failed director QA.
Only re-add an R7 image after director approval for this specific unit.
