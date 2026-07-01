# 18 - VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER - 奔跑到动作插入簇

- Status: organized input folder; visual quality is not yet re-approved.
- Time range: `00:47.42-00:48.17`
- Shot intent: Jean反应/动作桥接短簇，避免被吞进奔跑长段。

## Upload These

1. Reference video: `01_reference_clip/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER_reference.mp4`
2. Keyframes/images in `02_keyframes_for_upload/`.
3. Asset locks in `03_asset_locks_for_upload/`, if any.
4. This prompt document.

## Keyframes / Images For Upload

| # | Kind | ID | Time | Role | Local file |
|---:|---|---|---:|---|---|
| 1 | `official_keyframe` | `OP_SHOT_022` | 00:47.50 | 图6 / Jean_reaction_close | `02_keyframes_for_upload/01_official_keyframe_OP_SHOT_022.png` |
| 2 | `official_keyframe` | `OP_SHOT_023` | 00:48.00 | 图1 / Grandis_action_close | `02_keyframes_for_upload/02_official_keyframe_OP_SHOT_023.png` |
| 3 | `r7_generated_candidate` | `R7_CAND_018_start_047452ms` | 00:47.45 | start | `02_keyframes_for_upload/03_r7_generated_R7_CAND_018_start_047452ms.png` |
| 4 | `r7_generated_candidate` | `R7_CAND_018_end_048143ms` | 00:48.14 | end | `02_keyframes_for_upload/04_r7_generated_R7_CAND_018_end_048143ms.png` |

## Asset Locks

- `jean` (official_identity_lock): `03_asset_locks_for_upload/01_characters_jean.png`
- `grandis` (official_identity_lock): `03_asset_locks_for_upload/02_characters_grandis.png`
- `sanson` (official_identity_lock): `03_asset_locks_for_upload/03_characters_sanson.png`
- `hanson` (official_identity_lock): `03_asset_locks_for_upload/04_characters_hanson.png`

## Source Reference Frames

These files are included for audit/reference only. Prefer the generated keyframes above for AIGC image inputs unless the director explicitly asks to use source screenshots.

| ID | Time | Role | Local file |
|---|---:|---|---|
| `R7_CAND_018_start_047452ms` | 00:47.45 | start | `04_source_reference_frames_audit_only/01_R7_CAND_018_start_047452ms.jpg` |
| `R7_CAND_018_end_048143ms` | 00:48.14 | end | `04_source_reference_frames_audit_only/02_R7_CAND_018_end_048143ms.jpg` |

## Save Result To

`08_generation/outputs/video/reference003_r7_high_precision_segments/VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER.mp4`

## Prompt To Use

Generate a clean live-action remake segment for `VU_REF003_R7_018_REACTION_TO_ACTION_CLUSTER`.
Time range: `00:47.42-00:48.17`.

Use the reference video clip as the primary source for timing, camera movement,
screen direction, shot duration, and edit rhythm. Use the listed keyframes/images
as visual anchors for identity, props, vehicles, scene geometry, palette, and
continuity. Preserve active asset locks exactly when visible.

Shot intent: Jean反应/动作桥接短簇，避免被吞进奔跑长段。

No readable original title, credit, lyric, subtitle, broadcaster mark, logo,
watermark, or random glyph. Keep minors age-appropriate and non-sexualized.
Do not merge neighboring flashes or montage beats into a false single take.

QA note: this folder is an organized material handoff. Some generated images may
still need director review or replacement before final production approval.
