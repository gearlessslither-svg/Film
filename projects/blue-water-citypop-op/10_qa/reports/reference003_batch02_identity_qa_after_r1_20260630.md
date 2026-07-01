# Reference-003 Batch 02 Identity QA After R1

Created: 2026-06-30

Status: preliminary pass with dense references ready. Do not assemble final video yet.

## Inputs

- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset locks: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Dense reference manifest: `01_intake/analysis/reference003_dense_repair_frames_20260630/manifest.json`
- R1 application report: `10_qa/reports/reference003_identity_repair_r1_application_20260630.md`
- Updated 42-up status sheet: `10_qa/reference_match/REFERENCE003_OFFICIAL_KEYFRAME_STATUS_20260630/reference003_official_keyframe_status_sheet_42up.jpg`

## Decisions

| Item | Decision | Reason | Output |
|---|---|---|---|
| `OP_SHOT_018` | keep current | Nadia running face remains close enough to `OP_SHOT_011_v2`; dense refs are available if director wants a more source-exact motion pose. | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_018.png` |
| `OP_SHOT_019` | keep current | Jean still reads as the `OP_SHOT_012` boy inventor lock. | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_019.png` |
| `OP_SHOT_020` | keep current | Marie and King remain close enough to `OP_SHOT_014`; child-safe handling preserved. | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_020.png` |
| `OP_SHOT_023` | keep current | Grandis trio remains readable from `OP_SHOT_016_v2`; vehicle continuity is now handled by the new OP24 R1 craft lock. | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_023.png` |
| `OP_SHOT_024` | replaced and locked | New R1 vehicle/action craft lock applied. | `08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/outputs/OP_SHOT_024_VEHICLE_LOCK_R1.png` |
| `OP_SHOT_032` | keep current | Nemo lock source remains the best current identity anchor. | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_032.png` |
| `OP_SHOT_033` | keep current | Nemo continuation remains consistent enough with `OP_SHOT_032`; dense refs are available for later retouch if needed. | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_033.png` |

## Gate

Current image pass can move to video-package refresh after director review of the updated 42-up sheet. Video assembly remains last.
