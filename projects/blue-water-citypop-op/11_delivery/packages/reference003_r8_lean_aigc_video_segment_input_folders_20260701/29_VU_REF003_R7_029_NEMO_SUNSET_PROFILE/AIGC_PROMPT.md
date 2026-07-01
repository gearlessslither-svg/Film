# 29 - VU_REF003_R7_029_NEMO_SUNSET_PROFILE - Nemo夕景肖像长段

- Status: lean QA-recovery input folder; R7 candidates are reference-only.
- Time range: `01:06.02-01:11.36`
- Shot intent: Nemo 船长夕景肖像长段，首尾/中间关键帧承载连续运动。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_029_NEMO_SUNSET_PROFILE_reference_upload_h264_aac.mp4` (upload-compatible H.264/AAC MP4)
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

No target-style keyframe is approved for default upload in this unit. Use the reference clip, asset locks, and prompt; do not substitute original-style frames as visual style anchors.

## Asset Locks

- `nemo` (official_identity_lock): `03_asset_locks_for_upload/01_characters_nemo.png`

## R7 Generated Candidates, Reference Only

These images are included for review/reference only and are not part of the default upload image set for this lean package.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_029_start_066054ms` | 01:06.05 | start | `05_r7_generated_candidates_reference_only/01_R7_CAND_029_start_066054ms.png` |
| `R7_CAND_029_middle_068694ms` | 01:08.69 | middle | `05_r7_generated_candidates_reference_only/02_R7_CAND_029_middle_068694ms.png` |
| `R7_CAND_029_end_071333ms` | 01:11.33 | end | `05_r7_generated_candidates_reference_only/03_R7_CAND_029_end_071333ms.png` |

## Official Original Keyframes, Reference Only

These original-style frames are included for timing/composition audit only. Do not upload them as target-style keyframes unless the director explicitly asks for that specific unit.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `OP_SHOT_032` | 01:06.50 | 图1 / Nemo_profile_start | `06_official_original_keyframes_reference_only/01_official_keyframe_OP_SHOT_032.png` |
| `OP_SHOT_033` | 01:09.50 | 图2 / Nemo_profile_hold | `06_official_original_keyframes_reference_only/02_official_keyframe_OP_SHOT_033.png` |

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_029_start_066054ms` | 01:06.05 | start | `04_source_reference_frames_audit_only/01_R7_CAND_029_start_066054ms.jpg` |
| `R7_CAND_029_middle_068694ms` | 01:08.69 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_029_middle_068694ms.jpg` |
| `R7_CAND_029_end_071333ms` | 01:11.33 | end | `04_source_reference_frames_audit_only/03_R7_CAND_029_end_071333ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_029_NEMO_SUNSET_PROFILE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_029_NEMO_SUNSET_PROFILE`.
Time range: `01:06.02-01:11.36`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: Nemo 船长夕景肖像长段，首尾/中间关键帧承载连续运动。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.

Lean package note: R7 generated candidates are deliberately excluded from the
default image upload set after the 161-frame R7 preview failed director QA.
Only re-add an R7 image after director approval for this specific unit.
