# 07 - VU_REF003_R7_007_JEAN_FACE_FLASH - Jean帽子正脸短插

- Status: lean QA-recovery input folder; R7 candidates are reference-only.
- Time range: `00:28.86-00:29.49`
- Shot intent: Jean 正脸/帽子短促亮相，单独约束 Jean 身份。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_007_JEAN_FACE_FLASH_reference_upload_h264_aac.mp4` (upload-compatible H.264/AAC MP4)
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

No target-style keyframe is approved for default upload in this unit. Use the reference clip, asset locks, and prompt; do not substitute original-style frames as visual style anchors.

## Asset Locks

- `jean` (official_identity_lock): `03_asset_locks_for_upload/01_characters_jean.png`

## R7 Generated Candidates, Reference Only

These images are included for review/reference only and are not part of the default upload image set for this lean package.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_007_start_028892ms` | 00:28.89 | start | `05_r7_generated_candidates_reference_only/01_R7_CAND_007_start_028892ms.png` |
| `R7_CAND_007_end_029458ms` | 00:29.46 | end | `05_r7_generated_candidates_reference_only/02_R7_CAND_007_end_029458ms.png` |

## Official Original Keyframes, Reference Only

These original-style frames are included for timing/composition audit only. Do not upload them as target-style keyframes unless the director explicitly asks for that specific unit.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `OP_SHOT_012` | 00:29.00 | 图1 / Jean_hat_face | `06_official_original_keyframes_reference_only/01_official_keyframe_OP_SHOT_012.png` |

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_007_start_028892ms` | 00:28.89 | start | `04_source_reference_frames_audit_only/01_R7_CAND_007_start_028892ms.jpg` |
| `R7_CAND_007_end_029458ms` | 00:29.46 | end | `04_source_reference_frames_audit_only/02_R7_CAND_007_end_029458ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_007_JEAN_FACE_FLASH.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_007_JEAN_FACE_FLASH`.
Time range: `00:28.86-00:29.49`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: Jean 正脸/帽子短促亮相，单独约束 Jean 身份。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.

Lean package note: R7 generated candidates are deliberately excluded from the
default image upload set after the 161-frame R7 preview failed director QA.
Only re-add an R7 image after director approval for this specific unit.
