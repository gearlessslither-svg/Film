# 32 - VU_REF003_R7_032_UNDERWATER_TO_SPLASH - 水下纹理到水花

- Status: lean QA-recovery input folder; R7 candidates are reference-only.
- Time range: `01:16.45-01:17.79`
- Shot intent: 水下纹理进入水花爆发。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_032_UNDERWATER_TO_SPLASH_reference_upload_h264_aac.mp4` (upload-compatible H.264/AAC MP4)
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `r5_adaptive_generated` | `R5_VU_REF003_019_WATER_SPLASH_TRANSITION_077500ms_02` | 01:17.50 | adaptive_middle | `02_keyframes_for_upload/01_r5_adaptive_generated_R5_VU_REF003_019_WATER_SPLASH_TRANSITION_077500ms_02.png` |

## Asset Locks

- `water_burst_transition` (official_transition_lock): `03_asset_locks_for_upload/01_props_vehicles_symbols_water_burst_transition.png`

## R7 Generated Candidates, Reference Only

These images are included for review/reference only and are not part of the default upload image set for this lean package.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_032_start_076481ms` | 01:16.48 | start | `05_r7_generated_candidates_reference_only/01_R7_CAND_032_start_076481ms.png` |
| `R7_CAND_032_middle_077118ms` | 01:17.12 | middle | `05_r7_generated_candidates_reference_only/02_R7_CAND_032_middle_077118ms.png` |
| `R7_CAND_032_end_077756ms` | 01:17.76 | end | `05_r7_generated_candidates_reference_only/03_R7_CAND_032_end_077756ms.png` |

## Official Original Keyframes, Reference Only

These original-style frames are included for timing/composition audit only. Do not upload them as target-style keyframes unless the director explicitly asks for that specific unit.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `OP_SHOT_037` | 01:16.50 | 图3 / underwater_texture | `06_official_original_keyframes_reference_only/01_official_keyframe_OP_SHOT_037.png` |
| `OP_SHOT_038` | 01:18.00 | 图1 / water_burst | `06_official_original_keyframes_reference_only/02_official_keyframe_OP_SHOT_038.png` |

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_032_start_076481ms` | 01:16.48 | start | `04_source_reference_frames_audit_only/01_R7_CAND_032_start_076481ms.jpg` |
| `R7_CAND_032_middle_077118ms` | 01:17.12 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_032_middle_077118ms.jpg` |
| `R7_CAND_032_end_077756ms` | 01:17.76 | end | `04_source_reference_frames_audit_only/03_R7_CAND_032_end_077756ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_032_UNDERWATER_TO_SPLASH.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_032_UNDERWATER_TO_SPLASH`.
Time range: `01:16.45-01:17.79`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: 水下纹理进入水花爆发。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.

Lean package note: R7 generated candidates are deliberately excluded from the
default image upload set after the 161-frame R7 preview failed director QA.
Only re-add an R7 image after director approval for this specific unit.
