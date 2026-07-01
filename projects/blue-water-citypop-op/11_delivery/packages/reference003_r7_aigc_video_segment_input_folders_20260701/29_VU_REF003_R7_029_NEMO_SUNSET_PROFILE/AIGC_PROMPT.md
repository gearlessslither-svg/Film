# 29 - VU_REF003_R7_029_NEMO_SUNSET_PROFILE - Nemo夕景肖像长段

- Status: organized input folder; visual quality is not yet re-approved.
- Time range: `01:06.02-01:11.36`
- Shot intent: Nemo 船长夕景肖像长段，首尾/中间关键帧承载连续运动。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_029_NEMO_SUNSET_PROFILE_reference.mp4`
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `official_keyframe` | `OP_SHOT_032` | 01:06.50 | 图1 / Nemo_profile_start | `02_keyframes_for_upload/01_official_keyframe_OP_SHOT_032.png` |
| 2 | `official_keyframe` | `OP_SHOT_033` | 01:09.50 | 图2 / Nemo_profile_hold | `02_keyframes_for_upload/02_official_keyframe_OP_SHOT_033.png` |
| 3 | `r7_generated_candidate` | `R7_CAND_029_start_066054ms` | 01:06.05 | start | `02_keyframes_for_upload/03_r7_generated_R7_CAND_029_start_066054ms.png` |
| 4 | `r7_generated_candidate` | `R7_CAND_029_middle_068694ms` | 01:08.69 | middle | `02_keyframes_for_upload/04_r7_generated_R7_CAND_029_middle_068694ms.png` |
| 5 | `r7_generated_candidate` | `R7_CAND_029_end_071333ms` | 01:11.33 | end | `02_keyframes_for_upload/05_r7_generated_R7_CAND_029_end_071333ms.png` |

## Asset Locks

- `nemo` (official_identity_lock): `03_asset_locks_for_upload/01_characters_nemo.png`

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_029_start_066054ms` | 01:06.05 | start | `04_source_reference_frames_audit_only/01_R7_CAND_029_start_066054ms.jpg` |
| `R7_CAND_029_middle_068694ms` | 01:08.69 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_029_middle_068694ms.jpg` |
| `R7_CAND_029_end_071333ms` | 01:11.33 | end | `04_source_reference_frames_audit_only/03_R7_CAND_029_end_071333ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_029_NEMO_SUNSET_PROFILE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_029_NEMO_SUNSET_PROFILE`.
Time range: `01:06.02-01:11.36`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: Nemo 船长夕景肖像长段，首尾/中间关键帧承载连续运动。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.
