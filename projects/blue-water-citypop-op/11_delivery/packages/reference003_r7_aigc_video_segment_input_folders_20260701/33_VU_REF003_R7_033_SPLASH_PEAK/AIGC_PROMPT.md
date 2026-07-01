# 33 - VU_REF003_R7_033_SPLASH_PEAK - 水花爆发峰值

- Status: organized input folder; visual quality is not yet re-approved.
- Time range: `01:17.79-01:19.20`
- Shot intent: 水花爆发峰值与天空转场。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_033_SPLASH_PEAK_reference.mp4`
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `official_keyframe` | `OP_SHOT_038` | 01:18.00 | 图1 / water_burst | `02_keyframes_for_upload/01_official_keyframe_OP_SHOT_038.png` |
| 2 | `r5_adaptive_generated` | `R5_VU_REF003_019_WATER_SPLASH_TRANSITION_078500ms_01` | 01:18.50 | adaptive_primary | `02_keyframes_for_upload/02_r5_adaptive_generated_R5_VU_REF003_019_WATER_SPLASH_TRANSITION_078500ms_01.png` |
| 3 | `official_keyframe` | `OP_SHOT_039` | 01:19.00 | 图2 / splash_to_sky | `02_keyframes_for_upload/03_official_keyframe_OP_SHOT_039.png` |
| 4 | `r7_generated_candidate` | `R7_CAND_033_start_077816ms` | 01:17.82 | start | `02_keyframes_for_upload/04_r7_generated_R7_CAND_033_start_077816ms.png` |
| 5 | `r7_generated_candidate` | `R7_CAND_033_middle_078495ms` | 01:18.50 | middle | `02_keyframes_for_upload/05_r7_generated_R7_CAND_033_middle_078495ms.png` |
| 6 | `r7_generated_candidate` | `R7_CAND_033_end_079174ms` | 01:19.17 | end | `02_keyframes_for_upload/06_r7_generated_R7_CAND_033_end_079174ms.png` |

## Asset Locks

- `water_burst_transition` (official_transition_lock): `03_asset_locks_for_upload/01_props_vehicles_symbols_water_burst_transition.png`

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_033_start_077816ms` | 01:17.82 | start | `04_source_reference_frames_audit_only/01_R7_CAND_033_start_077816ms.jpg` |
| `R7_CAND_033_middle_078495ms` | 01:18.50 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_033_middle_078495ms.jpg` |
| `R7_CAND_033_end_079174ms` | 01:19.17 | end | `04_source_reference_frames_audit_only/03_R7_CAND_033_end_079174ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_033_SPLASH_PEAK.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_033_SPLASH_PEAK`.
Time range: `01:17.79-01:19.20`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: 水花爆发峰值与天空转场。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.
