# 27 - VU_REF003_R7_027_NIGHT_CITY_GRID - 夜城蓝网格

- Status: organized input folder; visual quality is not yet re-approved.
- Time range: `01:01.44-01:04.94`
- Shot intent: 夜城与蓝色地面/几何图案。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_027_NIGHT_CITY_GRID_reference.mp4`
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `official_keyframe` | `OP_SHOT_029` | 01:01.50 | 图1 / night_city_reveal | `02_keyframes_for_upload/01_official_keyframe_OP_SHOT_029.png` |
| 2 | `r5_adaptive_generated` | `R5_VU_REF003_014_NIGHT_CITY_BLUE_GRID_062500ms_01` | 01:02.50 | adaptive_primary | `02_keyframes_for_upload/02_r5_adaptive_generated_R5_VU_REF003_014_NIGHT_CITY_BLUE_GRID_062500ms_01.png` |
| 3 | `official_keyframe` | `OP_SHOT_030` | 01:03.50 | 图2 / glowing_blue_grid | `02_keyframes_for_upload/03_official_keyframe_OP_SHOT_030.png` |
| 4 | `r5_adaptive_generated` | `R5_VU_REF003_015_NIGHT_AIRCRAFT_PASS_065000ms_01` | 01:05.00 | adaptive_primary | `02_keyframes_for_upload/04_r5_adaptive_generated_R5_VU_REF003_015_NIGHT_AIRCRAFT_PASS_065000ms_01.png` |
| 5 | `r7_generated_candidate` | `R7_CAND_027_start_061466ms` | 01:01.47 | start | `02_keyframes_for_upload/05_r7_generated_R7_CAND_027_start_061466ms.png` |
| 6 | `r7_generated_candidate` | `R7_CAND_027_middle_063188ms` | 01:03.19 | middle | `02_keyframes_for_upload/06_r7_generated_R7_CAND_027_middle_063188ms.png` |
| 7 | `r7_generated_candidate` | `R7_CAND_027_end_064910ms` | 01:04.91 | end | `02_keyframes_for_upload/07_r7_generated_R7_CAND_027_end_064910ms.png` |

## Asset Locks

- `blue_grid_geometry` (official_scene_symbol_lock): `03_asset_locks_for_upload/01_props_vehicles_symbols_blue_grid_geometry.png`

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_027_start_061466ms` | 01:01.47 | start | `04_source_reference_frames_audit_only/01_R7_CAND_027_start_061466ms.jpg` |
| `R7_CAND_027_middle_063188ms` | 01:03.19 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_027_middle_063188ms.jpg` |
| `R7_CAND_027_end_064910ms` | 01:04.91 | end | `04_source_reference_frames_audit_only/03_R7_CAND_027_end_064910ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_027_NIGHT_CITY_GRID.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_027_NIGHT_CITY_GRID`.
Time range: `01:01.44-01:04.94`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: 夜城与蓝色地面/几何图案。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.
