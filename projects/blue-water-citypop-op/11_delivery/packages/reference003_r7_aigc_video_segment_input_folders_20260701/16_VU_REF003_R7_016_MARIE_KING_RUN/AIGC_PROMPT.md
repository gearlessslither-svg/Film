# 16 - VU_REF003_R7_016_MARIE_KING_RUN - Marie与King奔跑

- Status: organized input folder; visual quality is not yet re-approved.
- Time range: `00:43.50-00:45.50`
- Shot intent: Marie/King 独立奔跑节拍。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_016_MARIE_KING_RUN_reference.mp4`
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `official_keyframe` | `OP_SHOT_020` | 00:43.50 | 图4 / Marie_run | `02_keyframes_for_upload/01_official_keyframe_OP_SHOT_020.png` |
| 2 | `official_keyframe` | `OP_SHOT_021` | 00:45.50 | 图5 / group_run | `02_keyframes_for_upload/02_official_keyframe_OP_SHOT_021.png` |
| 3 | `r7_generated_candidate` | `R7_CAND_016_start_043530ms` | 00:43.53 | start | `02_keyframes_for_upload/03_r7_generated_R7_CAND_016_start_043530ms.png` |
| 4 | `r7_generated_candidate` | `R7_CAND_016_middle_044500ms` | 00:44.50 | middle | `02_keyframes_for_upload/04_r7_generated_R7_CAND_016_middle_044500ms.png` |
| 5 | `r7_generated_candidate` | `R7_CAND_016_end_045470ms` | 00:45.47 | end | `02_keyframes_for_upload/05_r7_generated_R7_CAND_016_end_045470ms.png` |

## Asset Locks

- `marie` (official_identity_lock): `03_asset_locks_for_upload/01_characters_marie.png`
- `king` (official_identity_lock): `03_asset_locks_for_upload/02_characters_king.png`

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_016_start_043530ms` | 00:43.53 | start | `04_source_reference_frames_audit_only/01_R7_CAND_016_start_043530ms.jpg` |
| `R7_CAND_016_middle_044500ms` | 00:44.50 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_016_middle_044500ms.jpg` |
| `R7_CAND_016_end_045470ms` | 00:45.47 | end | `04_source_reference_frames_audit_only/03_R7_CAND_016_end_045470ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_016_MARIE_KING_RUN.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_016_MARIE_KING_RUN`.
Time range: `00:43.50-00:45.50`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: Marie/King 独立奔跑节拍。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.
