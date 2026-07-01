# 05 - VU_REF003_R7_005_NADIA_CLOSE_INSERT - Nadia近景插入

- Status: organized input folder; visual quality is not yet re-approved.
- Time range: `00:25.90-00:26.82`
- Shot intent: Nadia 从侧脸进入更近的人物状态。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_005_NADIA_CLOSE_INSERT_reference.mp4`
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `official_keyframe` | `OP_SHOT_011` | 00:27.00 | 图2 / Nadia_close | `02_keyframes_for_upload/01_official_keyframe_OP_SHOT_011.png` |
| 2 | `r7_generated_candidate` | `R7_CAND_005_start_025931ms` | 00:25.93 | start | `02_keyframes_for_upload/02_r7_generated_R7_CAND_005_start_025931ms.png` |
| 3 | `r7_generated_candidate` | `R7_CAND_005_end_026788ms` | 00:26.79 | end | `02_keyframes_for_upload/03_r7_generated_R7_CAND_005_end_026788ms.png` |

## Asset Locks

- `nadia` (official_identity_lock): `03_asset_locks_for_upload/01_characters_nadia.png`
- `blue_water_pendant` (official_prop_lock): `03_asset_locks_for_upload/02_props_vehicles_symbols_blue_water_pendant.png`

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_005_start_025931ms` | 00:25.93 | start | `04_source_reference_frames_audit_only/01_R7_CAND_005_start_025931ms.jpg` |
| `R7_CAND_005_end_026788ms` | 00:26.79 | end | `04_source_reference_frames_audit_only/02_R7_CAND_005_end_026788ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_005_NADIA_CLOSE_INSERT.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_005_NADIA_CLOSE_INSERT`.
Time range: `00:25.90-00:26.82`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: Nadia 从侧脸进入更近的人物状态。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.
