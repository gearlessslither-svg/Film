# 06 - VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE - Nadia到Jean过渡

- Status: organized input folder; visual quality is not yet re-approved.
- Time range: `00:26.82-00:28.86`
- Shot intent: Nadia 段落向 Jean 入场切换，避免混淆人物归属。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE_reference.mp4`
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `official_keyframe` | `OP_SHOT_011` | 00:27.00 | 图2 / Nadia_close | `02_keyframes_for_upload/01_official_keyframe_OP_SHOT_011.png` |
| 2 | `r5_adaptive_generated` | `R5_VU_REF003_007_NADIA_PROFILE_ENTRY_027500ms_01` | 00:27.50 | adaptive_primary | `02_keyframes_for_upload/02_r5_adaptive_generated_R5_VU_REF003_007_NADIA_PROFILE_ENTRY_027500ms_01.png` |
| 3 | `r5_adaptive_generated` | `R5_VU_REF003_008_JEAN_INTRO_028500ms_02` | 00:28.50 | adaptive_middle | `02_keyframes_for_upload/03_r5_adaptive_generated_R5_VU_REF003_008_JEAN_INTRO_028500ms_02.png` |
| 4 | `official_keyframe` | `OP_SHOT_012` | 00:29.00 | 图1 / Jean_hat_face | `02_keyframes_for_upload/04_official_keyframe_OP_SHOT_012.png` |
| 5 | `r7_generated_candidate` | `R7_CAND_006_start_026848ms` | 00:26.85 | start | `02_keyframes_for_upload/05_r7_generated_R7_CAND_006_start_026848ms.png` |
| 6 | `r7_generated_candidate` | `R7_CAND_006_middle_027840ms` | 00:27.84 | middle | `02_keyframes_for_upload/06_r7_generated_R7_CAND_006_middle_027840ms.png` |
| 7 | `r7_generated_candidate` | `R7_CAND_006_end_028832ms` | 00:28.83 | end | `02_keyframes_for_upload/07_r7_generated_R7_CAND_006_end_028832ms.png` |

## Asset Locks

- `nadia` (official_identity_lock): `03_asset_locks_for_upload/01_characters_nadia.png`
- `jean` (official_identity_lock): `03_asset_locks_for_upload/02_characters_jean.png`
- `blue_water_pendant` (official_prop_lock): `03_asset_locks_for_upload/03_props_vehicles_symbols_blue_water_pendant.png`

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_006_start_026848ms` | 00:26.85 | start | `04_source_reference_frames_audit_only/01_R7_CAND_006_start_026848ms.jpg` |
| `R7_CAND_006_middle_027840ms` | 00:27.84 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_006_middle_027840ms.jpg` |
| `R7_CAND_006_end_028832ms` | 00:28.83 | end | `04_source_reference_frames_audit_only/03_R7_CAND_006_end_028832ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_006_NADIA_TO_JEAN_BRIDGE`.
Time range: `00:26.82-00:28.86`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: Nadia 段落向 Jean 入场切换，避免混淆人物归属。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.
