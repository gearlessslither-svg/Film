# Reference-003 Frame Promotion R3

- Created: `2026-06-30T19:05:00+08:00`
- Status: `p0_p1_generated_qa_pass_ready_for_optional_expanded_preview_no_new_mp4`
- Supersedes: `reference003_expanded_keyframes_r2_20260630`
- Source dense manifest: `01_intake/analysis/reference003_dense_repair_frames_20260630/manifest.json`
- Decision file: `03_story/expanded_keyframes/reference003_frame_promotion_r3_20260630.json`

## Core Correction

R2 was too aggressive: it converted 48 dense selected screenshots into pending image assets. That is now superseded.

R3 uses the new rule:

1. Dense screenshots are candidates only.
2. Baseline extraction ensures coverage.
3. Visual/semantic/edit differences decide promotion.
4. Repetitive ranges collapse to existing assets plus reference video.
5. Preview count increases only after promoted frames are regenerated as pure image assets.

## Director Overlay

Director review says:

- `OP_SHOT_021` repetition is serious.
- `OP_SHOT_025` repetition is serious.
- `OP_SHOT_032` repetition is serious.
- Other reviewed dense targets show large visual differences.

This means `21/25/32` should not produce many new still assets. They should mainly use existing generated assets plus reference video in the AIGC video prompt.

## Result

| Category | Count | Meaning |
|---|---:|---|
| Existing generated assets | 42 | Current approved image assets |
| Dense selected candidates | 55 | Screenshot candidates, not assets |
| R2 pending slots | 48 | Superseded; do not generate |
| R3 promoted new image assets | 11 | Maximum new generated stills if we expand preview |
| P0 hard replacement | 1 | Generated and QA pass: `OP_SHOT_010` |
| P1 difference expansion | 10 | Generated and QA pass; ready for optional expanded preview / AIGC input |
| Expanded total after P0 generation | 43 | Current approved asset count after replacing OP_SHOT_010 |
| Expanded total after all R3 generation | 53 | All 10 P1 outputs now exist |

P0 is now generated and active. The 10 P1 assets are also generated and registered, but they have not been merged into a new mp4 because the director requested image-only batch work.

Contact sheet: `08_generation/jobs/REFERENCE003_FRAME_PROMOTION_R3_20260630/outputs/REFERENCE003_R3_generated_assets_contact_sheet.jpg`

## P0 Must Generate

| Asset | Parent | Reason |
|---|---|---|
| `OP_SHOT_010_R3_NADIA_PROFILE_BEAUTY_LOCK` | `OP_SHOT_010` | Generated and QA pass. User/director said first Nadia is not beautiful enough. Keep OP_SHOT_011 face lock, but make profile face more refined and impressive. |

## P1 Difference Expansion Assets

These are generated image assets for optional preview expansion before AIGC video segment production:

| Asset | Parent | Time | Status | Reason |
|---|---|---:|---|---|
| `OP_SHOT_018_R3_039750ms_NADIA_RUN_FACE_TURN` | `OP_SHOT_018` | 39.750 | Generated | Nadia run changes into a clearer face/action state. |
| `OP_SHOT_018_R3_040125ms_NADIA_TO_JEAN_BRIDGE` | `OP_SHOT_018` | 40.125 | Generated | End bridge into Jean relationship/transition. |
| `OP_SHOT_019_R3_040750ms_JEAN_RUN_START` | `OP_SHOT_019` | 40.750 | Generated | Jean run start differs from center frame. |
| `OP_SHOT_019_R3_042125ms_JEAN_RUN_END` | `OP_SHOT_019` | 42.125 | Generated | Jean run end/profile action differs from center frame. |
| `OP_SHOT_020_R3_042750ms_MARIE_KING_START` | `OP_SHOT_020` | 42.750 | Generated | Marie/King entry is a distinct start composition. |
| `OP_SHOT_020_R3_044375ms_MARIE_KING_END` | `OP_SHOT_020` | 44.375 | Generated | Marie/King end/wider action state anchors the handoff into group run. |
| `OP_SHOT_023_R3_047250ms_GRANDIS_ACTION_START` | `OP_SHOT_023` | 47.250 | Generated | Grandis action start differs from current center lock. |
| `OP_SHOT_023_R3_048625ms_GRANDIS_TO_VEHICLE_END` | `OP_SHOT_023` | 48.625 | Generated | Outgoing action bridges into vehicle sequence. |
| `OP_SHOT_024_R3_048850ms_VEHICLE_BURST_START` | `OP_SHOT_024` | 48.850 | Generated | Vehicle burst start differs strongly from current vehicle lock. |
| `OP_SHOT_024_R3_050225ms_VEHICLE_FAR_END` | `OP_SHOT_024` | 50.225 | Generated | Vehicle far/end scale state is a separate anchor. |

## Collapsed / Reference-Only

| Parent | Decision | Reason |
|---|---|---|
| `OP_SHOT_021` | No new stills now | Repetitive group-run range; use `OP_SHOT_021_v2` plus reference clip. |
| `OP_SHOT_025` | No new stills now | Repetitive group-lineup range; use current `OP_SHOT_025_R1`. |
| `OP_SHOT_032` | No new stills now | Repetitive Nemo range; use `OP_SHOT_032/033` plus reference clip. |
| `OP_SHOT_033` | Reference-video only | Slow Nemo portrait continuation; existing start/end anchors are enough. |
| `OP_SHOT_034` | Keep R1 repair | Current R1 matches OP_SHOT_011 face lock and was not newly rejected. |

## Next Action

Use the generated `OP_SHOT_010_R3_NADIA_PROFILE_BEAUTY_LOCK` as the current active `OP_SHOT_010`. The 10 P1 expansion assets are ready to be merged into an expanded still-preview or used as shot-level AIGC inputs. Do not generate a new mp4 unless explicitly requested.
