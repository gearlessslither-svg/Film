# 12 - VU_REF003_R7_012_RUN_MONTAGE_ENTRY - 奔跑Montage入场

- Status: lean QA-recovery input folder; R7 candidates are reference-only.
- Time range: `00:37.20-00:38.12`
- Shot intent: 奔跑 montage 入场短切。

## Upload These

1. Reference video: `01_reference_clip_same_shot_hold_min2s_optional/VU_REF003_R7_012_RUN_MONTAGE_ENTRY_reference_same_shot_hold_min2s_h264_aac.mp4` (upload-compatible H.264/AAC MP4)
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

Short reference material note: this unit is under 2 seconds in the source timeline and is packaged separately.
- Original independent clip: `00_original_independent_reference_clip/VU_REF003_R7_012_RUN_MONTAGE_ENTRY_reference_independent_original_duration_h264_aac.mp4`
- Optional upload workaround: `01_reference_clip_same_shot_hold_min2s_optional/VU_REF003_R7_012_RUN_MONTAGE_ENTRY_reference_same_shot_hold_min2s_h264_aac.mp4`
- The optional workaround only holds this same shot's last frame; it does not splice neighboring shots.
- Preserve the original shot content and do not merge this unit with adjacent units.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `r5_adaptive_generated` | `R5_VU_REF003_010_GRANDIS_TRIO_INTRO_037500ms_02` | 00:37.50 | adaptive_middle | `02_keyframes_for_upload/01_r5_adaptive_generated_R5_VU_REF003_010_GRANDIS_TRIO_INTRO_037500ms_02.png` |

## Asset Locks

- `nadia` (official_identity_lock): `03_asset_locks_for_upload/01_characters_nadia.png`

## R7 Generated Candidates, Reference Only

These images are included for review/reference only and are not part of the default upload image set for this lean package.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_012_start_037234ms` | 00:37.23 | start | `05_r7_generated_candidates_reference_only/01_R7_CAND_012_start_037234ms.png` |
| `R7_CAND_012_end_038091ms` | 00:38.09 | end | `05_r7_generated_candidates_reference_only/02_R7_CAND_012_end_038091ms.png` |

## Official Original Keyframes, Reference Only

These original-style frames are included for timing/composition audit only. Do not upload them as target-style keyframes unless the director explicitly asks for that specific unit.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `OP_SHOT_016` | 00:37.00 | 图2 / Grandis_trio_close | `06_official_original_keyframes_reference_only/01_official_keyframe_OP_SHOT_016.png` |
| `OP_SHOT_017` | 00:38.00 | 图1 / Nadia_run_feet | `06_official_original_keyframes_reference_only/02_official_keyframe_OP_SHOT_017.png` |

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_012_start_037234ms` | 00:37.23 | start | `04_source_reference_frames_audit_only/01_R7_CAND_012_start_037234ms.jpg` |
| `R7_CAND_012_end_038091ms` | 00:38.09 | end | `04_source_reference_frames_audit_only/02_R7_CAND_012_end_038091ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_012_RUN_MONTAGE_ENTRY.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_012_RUN_MONTAGE_ENTRY`.
Time range: `00:37.20-00:38.12`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.
Shot content integrity has higher priority than the 2-second upload constraint:
do not merge, splice, or borrow content from neighboring shots to satisfy duration.

Shot intent: 奔跑 montage 入场短切。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.

Lean package note: R7 generated candidates are deliberately excluded from the
default image upload set after the 161-frame R7 preview failed director QA.
Only re-add an R7 image after director approval for this specific unit.
