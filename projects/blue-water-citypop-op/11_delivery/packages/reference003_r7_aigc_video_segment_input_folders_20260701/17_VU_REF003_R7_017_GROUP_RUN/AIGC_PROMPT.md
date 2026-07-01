# 17 - VU_REF003_R7_017_GROUP_RUN - 群像奔跑

- Status: organized input folder; visual quality is not yet re-approved.
- Time range: `00:45.50-00:47.42`
- Shot intent: 全员奔跑群像节拍，必须用多角色锁图。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_017_GROUP_RUN_reference.mp4`
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `official_keyframe` | `OP_SHOT_021` | 00:45.50 | 图5 / group_run | `02_keyframes_for_upload/01_official_keyframe_OP_SHOT_021.png` |
| 2 | `official_keyframe` | `OP_SHOT_022` | 00:47.50 | 图6 / Jean_reaction_close | `02_keyframes_for_upload/02_official_keyframe_OP_SHOT_022.png` |
| 3 | `r7_generated_candidate` | `R7_CAND_017_start_045530ms` | 00:45.53 | start | `02_keyframes_for_upload/03_r7_generated_R7_CAND_017_start_045530ms.png` |
| 4 | `r7_generated_candidate` | `R7_CAND_017_middle_046461ms` | 00:46.46 | middle | `02_keyframes_for_upload/04_r7_generated_R7_CAND_017_middle_046461ms.png` |
| 5 | `r7_generated_candidate` | `R7_CAND_017_end_047392ms` | 00:47.39 | end | `02_keyframes_for_upload/05_r7_generated_R7_CAND_017_end_047392ms.png` |

## Asset Locks

- `nadia` (official_identity_lock): `03_asset_locks_for_upload/01_characters_nadia.png`
- `jean` (official_identity_lock): `03_asset_locks_for_upload/02_characters_jean.png`
- `marie` (official_identity_lock): `03_asset_locks_for_upload/03_characters_marie.png`
- `king` (official_identity_lock): `03_asset_locks_for_upload/04_characters_king.png`
- `blue_water_pendant` (official_prop_lock): `03_asset_locks_for_upload/05_props_vehicles_symbols_blue_water_pendant.png`

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_017_start_045530ms` | 00:45.53 | start | `04_source_reference_frames_audit_only/01_R7_CAND_017_start_045530ms.jpg` |
| `R7_CAND_017_middle_046461ms` | 00:46.46 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_017_middle_046461ms.jpg` |
| `R7_CAND_017_end_047392ms` | 00:47.39 | end | `04_source_reference_frames_audit_only/03_R7_CAND_017_end_047392ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_017_GROUP_RUN.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_017_GROUP_RUN`.
Time range: `00:45.50-00:47.42`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: 全员奔跑群像节拍，必须用多角色锁图。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.
