# 10 - VU_REF003_R7_010_GRANDIS_TRIO_WIDE - Grandis三人组广角

- Status: organized input folder; visual quality is not yet re-approved.
- Time range: `00:33.95-00:35.95`
- Shot intent: Grandis 三人组广角亮相。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_010_GRANDIS_TRIO_WIDE_reference.mp4`
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `official_keyframe` | `OP_SHOT_014` | 00:34.00 | 图2 / Marie_King_close | `02_keyframes_for_upload/01_official_keyframe_OP_SHOT_014.png` |
| 2 | `r5_adaptive_generated` | `R5_VU_REF003_010_GRANDIS_TRIO_INTRO_034500ms_01` | 00:34.50 | adaptive_primary | `02_keyframes_for_upload/02_r5_adaptive_generated_R5_VU_REF003_010_GRANDIS_TRIO_INTRO_034500ms_01.png` |
| 3 | `official_keyframe` | `OP_SHOT_015` | 00:35.50 | 图1 / Grandis_trio_wide | `02_keyframes_for_upload/03_official_keyframe_OP_SHOT_015.png` |
| 4 | `r7_generated_candidate` | `R7_CAND_010_start_033981ms` | 00:33.98 | start | `02_keyframes_for_upload/04_r7_generated_R7_CAND_010_start_033981ms.png` |
| 5 | `r7_generated_candidate` | `R7_CAND_010_middle_034952ms` | 00:34.95 | middle | `02_keyframes_for_upload/05_r7_generated_R7_CAND_010_middle_034952ms.png` |
| 6 | `r7_generated_candidate` | `R7_CAND_010_end_035923ms` | 00:35.92 | end | `02_keyframes_for_upload/06_r7_generated_R7_CAND_010_end_035923ms.png` |

## Asset Locks

- `grandis` (official_identity_lock): `03_asset_locks_for_upload/01_characters_grandis.png`
- `sanson` (official_identity_lock): `03_asset_locks_for_upload/02_characters_sanson.png`
- `hanson` (official_identity_lock): `03_asset_locks_for_upload/03_characters_hanson.png`

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_010_start_033981ms` | 00:33.98 | start | `04_source_reference_frames_audit_only/01_R7_CAND_010_start_033981ms.jpg` |
| `R7_CAND_010_middle_034952ms` | 00:34.95 | middle | `04_source_reference_frames_audit_only/02_R7_CAND_010_middle_034952ms.jpg` |
| `R7_CAND_010_end_035923ms` | 00:35.92 | end | `04_source_reference_frames_audit_only/03_R7_CAND_010_end_035923ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_010_GRANDIS_TRIO_WIDE.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_010_GRANDIS_TRIO_WIDE`.
Time range: `00:33.95-00:35.95`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: Grandis 三人组广角亮相。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.
