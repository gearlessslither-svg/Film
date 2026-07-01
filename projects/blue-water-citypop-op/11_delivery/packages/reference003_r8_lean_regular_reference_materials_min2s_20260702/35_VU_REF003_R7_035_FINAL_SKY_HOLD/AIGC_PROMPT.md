# 35 - VU_REF003_R7_035_FINAL_SKY_HOLD - 最终天空Hold

- Status: lean QA-recovery input folder; R7 candidates are reference-only.
- Time range: `01:20.79-01:23.58`
- Shot intent: 最终无字天空 hold。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_035_FINAL_SKY_HOLD_reference_upload_h264_aac.mp4` (upload-compatible H.264/AAC MP4)
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

No target-style keyframe is approved for default upload in this unit. Use the reference clip, asset locks, and prompt; do not substitute original-style frames as visual style anchors.

## Asset Locks

- none

## R7 Generated Candidates, Reference Only

These images are included for review/reference only and are not part of the default upload image set for this lean package.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_035_start_080819ms` | 01:20.82 | start | `05_r7_generated_candidates_reference_only/01_R7_CAND_035_start_080819ms.png` |
| `R7_CAND_035_middle_082186ms` | 01:22.19 | middle | `05_r7_generated_candidates_reference_only/02_R7_CAND_035_middle_082186ms.png` |
| `R7_CAND_035_end_083554ms` | 01:23.55 | end | `05_r7_generated_candidates_reference_only/03_R7_CAND_035_end_083554ms.png` |

## Official Original Keyframes, Reference Only

These original-style frames are included for timing/composition audit only. Do not upload them as target-style keyframes unless the director explicitly asks for that specific unit.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `OP_SHOT_041` | 01:22.00 | 图2 / final_sun_hold | `06_official_original_keyframes_reference_only/01_official_keyframe_OP_SHOT_041.png` |
| `OP_SHOT_042` | 01:23.50 | 图1 / black_tail | `06_official_original_keyframes_reference_only/02_official_keyframe_OP_SHOT_042.png` |

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_035_start_080819ms` | 01:20.82 | start | `04_source_reference_frames_audit_only/01_R7_CAND_035_start_080819ms.jpg` |
| `R7_CAND_035_middle_082186ms` | 01:22.19 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_035_middle_082186ms.jpg` |
| `R7_CAND_035_end_083554ms` | 01:23.55 | end | `04_source_reference_frames_audit_only/03_R7_CAND_035_end_083554ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_035_FINAL_SKY_HOLD.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_035_FINAL_SKY_HOLD`.
Time range: `01:20.79-01:23.58`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.
Shot content integrity has higher priority than the 2-second upload constraint:
do not merge, splice, or borrow content from neighboring shots to satisfy duration.

Shot intent: 最终无字天空 hold。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.

Lean package note: R7 generated candidates are deliberately excluded from the
default image upload set after the 161-frame R7 preview failed director QA.
Only re-add an R7 image after director approval for this specific unit.
