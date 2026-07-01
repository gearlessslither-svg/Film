# 04 - VU_REF003_R7_004_NADIA_PROFILE_CONTINUE - Nadia侧脸延续

- Status: lean QA-recovery input folder; R7 candidates are reference-only.
- Time range: `00:24.80-00:25.90`
- Shot intent: Nadia 首次亮相后的侧脸延续，不并入 Jean。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_004_NADIA_PROFILE_CONTINUE_reference_upload_h264_aac.mp4` (upload-compatible H.264/AAC MP4)
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

No target-style keyframe is approved for default upload in this unit. Use the reference clip, asset locks, and prompt; do not substitute original-style frames as visual style anchors.

## Asset Locks

- `nadia` (official_identity_lock): `03_asset_locks_for_upload/01_characters_nadia.png`
- `blue_water_pendant` (official_prop_lock): `03_asset_locks_for_upload/02_props_vehicles_symbols_blue_water_pendant.png`

## R7 Generated Candidates, Reference Only

These images are included for review/reference only and are not part of the default upload image set for this lean package.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_004_start_024830ms` | 00:24.83 | start | `05_r7_generated_candidates_reference_only/01_R7_CAND_004_start_024830ms.png` |
| `R7_CAND_004_end_025871ms` | 00:25.87 | end | `05_r7_generated_candidates_reference_only/02_R7_CAND_004_end_025871ms.png` |

## Official Original Keyframes, Reference Only

These original-style frames are included for timing/composition audit only. Do not upload them as target-style keyframes unless the director explicitly asks for that specific unit.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `OP_SHOT_010` | 00:24.50 | 图1 / Nadia_profile | `06_official_original_keyframes_reference_only/01_official_keyframe_OP_SHOT_010.png` |

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_004_start_024830ms` | 00:24.83 | start | `04_source_reference_frames_audit_only/01_R7_CAND_004_start_024830ms.jpg` |
| `R7_CAND_004_end_025871ms` | 00:25.87 | end | `04_source_reference_frames_audit_only/02_R7_CAND_004_end_025871ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_004_NADIA_PROFILE_CONTINUE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_004_NADIA_PROFILE_CONTINUE`.
Time range: `00:24.80-00:25.90`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: Nadia 首次亮相后的侧脸延续，不并入 Jean。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.

Lean package note: R7 generated candidates are deliberately excluded from the
default image upload set after the 161-frame R7 preview failed director QA.
Only re-add an R7 image after director approval for this specific unit.
