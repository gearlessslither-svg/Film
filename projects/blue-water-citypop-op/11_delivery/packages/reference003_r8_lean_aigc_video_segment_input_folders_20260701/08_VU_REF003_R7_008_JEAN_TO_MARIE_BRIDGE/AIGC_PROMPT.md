# 08 - VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE - Jean到Marie草地过渡

- Status: lean QA-recovery input folder; R7 candidates are reference-only.
- Time range: `00:29.49-00:31.95`
- Shot intent: Jean 段落过渡到 Marie/King 草地段。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE_reference_upload_h264_aac.mp4` (upload-compatible H.264/AAC MP4)
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `r5_adaptive_generated` | `R5_VU_REF003_008_JEAN_INTRO_030500ms_01` | 00:30.50 | adaptive_primary | `02_keyframes_for_upload/01_r5_adaptive_generated_R5_VU_REF003_008_JEAN_INTRO_030500ms_01.png` |
| 2 | `r5_adaptive_generated` | `R5_VU_REF003_009_MARIE_KING_MEADOW_031000ms_01` | 00:31.00 | adaptive_primary | `02_keyframes_for_upload/02_r5_adaptive_generated_R5_VU_REF003_009_MARIE_KING_MEADOW_031000ms_01.png` |

## Asset Locks

- `jean` (official_identity_lock): `03_asset_locks_for_upload/01_characters_jean.png`
- `marie` (official_identity_lock): `03_asset_locks_for_upload/02_characters_marie.png`
- `king` (official_identity_lock): `03_asset_locks_for_upload/03_characters_king.png`

## R7 Generated Candidates, Reference Only

These images are included for review/reference only and are not part of the default upload image set for this lean package.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_008_start_029518ms` | 00:29.52 | start | `05_r7_generated_candidates_reference_only/01_R7_CAND_008_start_029518ms.png` |
| `R7_CAND_008_middle_030718ms` | 00:30.72 | middle | `05_r7_generated_candidates_reference_only/02_R7_CAND_008_middle_030718ms.png` |
| `R7_CAND_008_end_031919ms` | 00:31.92 | end | `05_r7_generated_candidates_reference_only/03_R7_CAND_008_end_031919ms.png` |

## Official Original Keyframes, Reference Only

These original-style frames are included for timing/composition audit only. Do not upload them as target-style keyframes unless the director explicitly asks for that specific unit.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `OP_SHOT_013` | 00:31.50 | 图1 / Marie_King_meadow | `06_official_original_keyframes_reference_only/01_official_keyframe_OP_SHOT_013.png` |

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_008_start_029518ms` | 00:29.52 | start | `04_source_reference_frames_audit_only/01_R7_CAND_008_start_029518ms.jpg` |
| `R7_CAND_008_middle_030718ms` | 00:30.72 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_008_middle_030718ms.jpg` |
| `R7_CAND_008_end_031919ms` | 00:31.92 | end | `04_source_reference_frames_audit_only/03_R7_CAND_008_end_031919ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_008_JEAN_TO_MARIE_BRIDGE`.
Time range: `00:29.49-00:31.95`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: Jean 段落过渡到 Marie/King 草地段。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.

Lean package note: R7 generated candidates are deliberately excluded from the
default image upload set after the 161-frame R7 preview failed director QA.
Only re-add an R7 image after director approval for this specific unit.
