# 14 - VU_REF003_R7_014_NADIA_RUN_FRONT - Nadia正面奔跑

- Status: organized input folder; visual quality is not yet re-approved.
- Time range: `00:39.50-00:41.50`
- Shot intent: Nadia 正面奔跑节拍。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_014_NADIA_RUN_FRONT_reference.mp4`
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `official_keyframe` | `OP_SHOT_018` | 00:39.50 | 图2 / Nadia_run_front | `02_keyframes_for_upload/01_official_keyframe_OP_SHOT_018.png` |
| 2 | `official_keyframe` | `OP_SHOT_019` | 00:41.50 | 图3 / Jean_run | `02_keyframes_for_upload/02_official_keyframe_OP_SHOT_019.png` |
| 3 | `r7_generated_candidate` | `R7_CAND_014_start_039530ms` | 00:39.53 | start | `02_keyframes_for_upload/03_r7_generated_R7_CAND_014_start_039530ms.png` |
| 4 | `r7_generated_candidate` | `R7_CAND_014_middle_040500ms` | 00:40.50 | middle | `02_keyframes_for_upload/04_r7_generated_R7_CAND_014_middle_040500ms.png` |
| 5 | `r7_generated_candidate` | `R7_CAND_014_end_041470ms` | 00:41.47 | end | `02_keyframes_for_upload/05_r7_generated_R7_CAND_014_end_041470ms.png` |

## Asset Locks

- `nadia` (official_identity_lock): `03_asset_locks_for_upload/01_characters_nadia.png`
- `blue_water_pendant` (official_prop_lock): `03_asset_locks_for_upload/02_props_vehicles_symbols_blue_water_pendant.png`

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_014_start_039530ms` | 00:39.53 | start | `04_source_reference_frames_audit_only/01_R7_CAND_014_start_039530ms.jpg` |
| `R7_CAND_014_middle_040500ms` | 00:40.50 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_014_middle_040500ms.jpg` |
| `R7_CAND_014_end_041470ms` | 00:41.47 | end | `04_source_reference_frames_audit_only/03_R7_CAND_014_end_041470ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_014_NADIA_RUN_FRONT.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_014_NADIA_RUN_FRONT`.
Time range: `00:39.50-00:41.50`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: Nadia 正面奔跑节拍。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.
