# 26 - VU_REF003_R7_026_NAUTILUS_EXIT - Nautilus海底尾段

- Status: lean QA-recovery input folder; R7 candidates are reference-only.
- Time range: `00:58.50-01:01.44`
- Shot intent: Nautilus 海底尾段，不生成原片职员表文字。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_026_NAUTILUS_EXIT_reference_upload_h264_aac.mp4` (upload-compatible H.264/AAC MP4)
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `r5_adaptive_generated` | `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_060500ms_02` | 01:00.50 | adaptive_middle | `02_keyframes_for_upload/01_r5_adaptive_generated_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_060500ms_02.png` |

## Asset Locks

- `nautilus` (official_prop_lock): `03_asset_locks_for_upload/01_props_vehicles_symbols_nautilus.png`

## R7 Generated Candidates, Reference Only

These images are included for review/reference only and are not part of the default upload image set for this lean package.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_026_start_058530ms` | 00:58.53 | start | `05_r7_generated_candidates_reference_only/01_R7_CAND_026_start_058530ms.png` |
| `R7_CAND_026_middle_059968ms` | 00:59.97 | middle | `05_r7_generated_candidates_reference_only/02_R7_CAND_026_middle_059968ms.png` |
| `R7_CAND_026_end_061406ms` | 01:01.41 | end | `05_r7_generated_candidates_reference_only/03_R7_CAND_026_end_061406ms.png` |

## Official Original Keyframes, Reference Only

These original-style frames are included for timing/composition audit only. Do not upload them as target-style keyframes unless the director explicitly asks for that specific unit.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `OP_SHOT_028` | 00:58.50 | 图3 / undersea_shadow | `06_official_original_keyframes_reference_only/01_official_keyframe_OP_SHOT_028.png` |
| `OP_SHOT_029` | 01:01.50 | 图1 / night_city_reveal | `06_official_original_keyframes_reference_only/02_official_keyframe_OP_SHOT_029.png` |

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_026_start_058530ms` | 00:58.53 | start | `04_source_reference_frames_audit_only/01_R7_CAND_026_start_058530ms.jpg` |
| `R7_CAND_026_middle_059968ms` | 00:59.97 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_026_middle_059968ms.jpg` |
| `R7_CAND_026_end_061406ms` | 01:01.41 | end | `04_source_reference_frames_audit_only/03_R7_CAND_026_end_061406ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_026_NAUTILUS_EXIT.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_026_NAUTILUS_EXIT`.
Time range: `00:58.50-01:01.44`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.
Shot content integrity has higher priority than the 2-second upload constraint:
do not merge, splice, or borrow content from neighboring shots to satisfy duration.

Shot intent: Nautilus 海底尾段，不生成原片职员表文字。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.

Lean package note: R7 generated candidates are deliberately excluded from the
default image upload set after the 161-frame R7 preview failed director QA.
Only re-add an R7 image after director approval for this specific unit.
