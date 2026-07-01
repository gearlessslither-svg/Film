# Video Content Analysis - blue-water-citypop-op

Updated: 2026-06-30T04:40:42+08:00

## Scope

This report covers every current video file inside the project folder after ingesting the full 2160P OP reference. It replaces the earlier 4-video inventory.

## Inventory

| Path | Role | Duration | Resolution | Frames | Decode | Decision |
|---|---|---:|---|---:|---|---|
| `01_intake/analysis/video_reference_packages/reference-002-opening/roughcuts/reference-002-opening_frame_stack_2fps.mp4` | derived_reference_roughcut_superseded | 23.000000s | 960x540 | 46 | pass | Derived 2fps review roughcut for old 23s reference. |
| `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/roughcuts/reference-003-full-op-2160p_frame_stack_2fps.mp4` | active_full_reference_roughcut | 84.500000s | 960x720 | 169 | pass | Derived 2fps roughcut for the active full OP reference. |
| `01_intake/references/nadia_op_reference_002.mp4` | duplicate_reference_alias_superseded | 23.010952s | 1920x1080 | 690 | pass | Byte-identical duplicate of reference-002-opening.mp4. |
| `01_intake/references/reference-002-opening.mp4` | canonical_reference_video_superseded | 23.010952s | 1920x1080 | 690 | pass | Superseded 23s opening reference; covered earlier reference-002 package. |
| `01_intake/references/reference-003-full-op-2160p.mp4` | active_full_reference_video | 84.437333s | 1440x1080 | 2024 | pass | Active full 84.44s OP reference for 1:1 planning. |
| `06_previs/playblasts/opening_24s_onetake_previs.mp4` | blender_previs_candidate_superseded | 24.000000s | 1280x548 | 576 | pass | Generated/previs camera experiment; not accepted timing. |

## Duplicate Groups

- Same SHA-256: `01_intake/references/nadia_op_reference_002.mp4`, `01_intake/references/reference-002-opening.mp4`

## Active Reference Decision

- Active full-reference video: `01_intake/references/reference-003-full-op-2160p.mp4`
- Active full-reference roughcut: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/roughcuts/reference-003-full-op-2160p_frame_stack_2fps.mp4`
- Full OP 1:1 unit plan: `00_admin/ai_bridge/decisions/reference_003_full_op_1to1_unit_plan_v1.md`
- Previous `reference-002-opening` and `opening_24s_onetake_previs` are superseded for timing.
