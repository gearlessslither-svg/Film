# 28 - VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS - 夜航飞行器短切

- Status: organized input folder; visual quality is not yet re-approved.
- Time range: `01:04.94-01:06.02`
- Shot intent: 夜航飞行器短切。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS_reference.mp4`
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `r5_adaptive_generated` | `R5_VU_REF003_015_NIGHT_AIRCRAFT_PASS_065000ms_01` | 01:05.00 | adaptive_primary | `02_keyframes_for_upload/01_r5_adaptive_generated_R5_VU_REF003_015_NIGHT_AIRCRAFT_PASS_065000ms_01.png` |
| 2 | `official_keyframe` | `OP_SHOT_031` | 01:05.50 | 图1 / night_aircraft_pass | `02_keyframes_for_upload/02_official_keyframe_OP_SHOT_031.png` |
| 3 | `r7_generated_candidate` | `R7_CAND_028_start_064970ms` | 01:04.97 | start | `02_keyframes_for_upload/03_r7_generated_R7_CAND_028_start_064970ms.png` |
| 4 | `r7_generated_candidate` | `R7_CAND_028_end_065994ms` | 01:05.99 | end | `02_keyframes_for_upload/04_r7_generated_R7_CAND_028_end_065994ms.png` |

## Asset Locks

- `jean_aircraft` (official_prop_lock): `03_asset_locks_for_upload/01_props_vehicles_symbols_jean_aircraft.png`

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_028_start_064970ms` | 01:04.97 | start | `04_source_reference_frames_audit_only/01_R7_CAND_028_start_064970ms.jpg` |
| `R7_CAND_028_end_065994ms` | 01:05.99 | end | `04_source_reference_frames_audit_only/02_R7_CAND_028_end_065994ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_028_NIGHT_AIRCRAFT_PASS`.
Time range: `01:04.94-01:06.02`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: 夜航飞行器短切。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.
