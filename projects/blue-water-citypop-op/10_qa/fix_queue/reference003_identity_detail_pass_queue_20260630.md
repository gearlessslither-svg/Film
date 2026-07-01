# Reference-003 Identity and Detail Pass Queue

Created: 2026-06-30

Status: Batch 01 hard replacements applied; Batch 02 identity QA pending. Director confirmed no additional approval is required before starting this pass.

This queue upgrades the current 42-keyframe preview from composition/no-text QA to identity/asset/video-readiness QA. Use `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md` and `reference003_asset_locks_v1.json` as the hard source of truth.

## Global Rules

- Nadia must match `OP_SHOT_011_v2` in all later appearances.
- Other characters use their first accepted appearance/close appearance as current locks.
- Director accepts `OP_SHOT_021_v2` for the current workprint.
- Director rejects `OP_SHOT_025` and `OP_SHOT_034` for the current version.
- The Blue Water pendant, white bird, Jean aircraft, Nautilus, blue grid, water burst, sky/cloud locations, undersea location, night city, and final sky must not redesign themselves between shots.
- Current `generated_reference003_qa_pass` means composition/no-text/timing pass only. It is not equivalent to `video_ready_pass`.

## Batch 01 - Must Fix Before Final Video Generation

R1 application report: `10_qa/reports/reference003_identity_repair_r1_application_20260630.md`

| Priority | Item | Current issue | Required action | Source locks |
|---:|---|---|---|---|
| 1 | `OP_SHOT_024` Grandis vehicle/action craft | Previous vehicle continuity had no dedicated lock and could not use rejected `OP_SHOT_025`. | Applied R1 vehicle/action craft lock: `08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/outputs/OP_SHOT_024_VEHICLE_LOCK_R1.png`. | `OP_SHOT_016_v2`, dense OP24 reference frames |
| 1 | `OP_SHOT_025` group lineup / vehicle tableau | Director rejected the large group portrait as the worst image in this set. Group identity and vehicle/prop design fail current standard. | Applied R1 hard replacement: `08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/outputs/OP_SHOT_025_R1.png`. Keep old `OP_SHOT_025` only as rejected history, never as a lock. | `OP_SHOT_011_v2`, `OP_SHOT_012`, `OP_SHOT_014`, `OP_SHOT_016_v2`, R1 vehicle lock |
| 2 | `OP_SHOT_034` Nadia solemn close | Director rejected the blue/sea-background Nadia image. Face does not meet the `OP_SHOT_011_v2` standard. | Applied R1 hard replacement: `08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/outputs/OP_SHOT_034_R1.png`. | `OP_SHOT_011_v2`, `OP_SHOT_035` |

## Dense Reference Package

- Manifest: `01_intake/analysis/reference003_dense_repair_frames_20260630/manifest.json`
- Combined sheet: `01_intake/analysis/reference003_dense_repair_frames_20260630/reference003_identity_repair_dense_selected_sheet.jpg`
- Image repair job: `08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/manifest.json`

## Director-Accepted Current Workprint Frames

| Item | Decision | Use |
|---|---|---|
| `OP_SHOT_011_v2` | Excellent. | Nadia official face lock. |
| `OP_SHOT_021_v2` | Very good for current workprint. | Can be used as current group-running proxy/reference. |

## Batch 02 - Identity QA Before AIGC Video Upload

QA report: `10_qa/reports/reference003_batch02_identity_qa_after_r1_20260630.md`

| Item | Risk | Check |
|---|---|---|
| `OP_SHOT_018` Nadia run front | Nadia may drift in motion/action frame. | Compare against `OP_SHOT_011_v2`; preserve face, bob, earrings, outfit, pendant if readable. |
| `OP_SHOT_019` Jean run | Jean may drift from intro lock. | Compare against `OP_SHOT_012`; preserve round glasses, blue cap/beret, red bow tie, age. |
| `OP_SHOT_020` Marie run | Marie/King may drift from first lock. | Compare against `OP_SHOT_014`; preserve child-safe age and King scarf. |
| `OP_SHOT_023`/`OP_SHOT_024` Grandis action bridge | Trio and vehicle can redesign under action prompt. | Compare characters against `OP_SHOT_016_v2`; vehicle/action craft needs a new dedicated lock. Do not use rejected `OP_SHOT_025`. |
| `OP_SHOT_032`/`OP_SHOT_033` Nemo sunset | Nemo must remain same actor/identity across hold. | Compare both against `OP_SHOT_032`; preserve cap, uniform, stern adult face. |

## Batch 03 - Detail Density Additions

Use the existing 2fps reference extraction to add only high-value missing details:

- Add intermediate frames in long gaps over 3 seconds where a visual event changes meaning.
- Prioritize `00:07.50-00:23.00`, `00:55.00-01:01.50`, and the running/action montage.
- Do not add density to pure black, title-safe empty sky, or static holds unless a key identity/prop detail is missing.

## Exit Criteria

- All Batch 01 items either pass identity/asset QA or are replaced.
- Every visible major character in a multi-character shot matches the official lock.
- Every recurring prop/vehicle/symbol/location matches the setting chapter.
- Video segment packages remain ready and include the setting chapter plus packaged asset locks.
