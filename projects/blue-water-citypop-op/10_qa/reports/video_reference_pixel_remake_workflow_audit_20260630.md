# Video Reference Pixel Remake Workflow Audit

Updated: 2026-06-30 04:22 Asia/Shanghai

## Verdict

PASS.

The project now has a reusable workflow for video-reference-based, high-fidelity remake work with Codex/GPT division of labor.

## What Was Built

### Global Workflow

- Workflow doc: `docs/VIDEO_REFERENCE_REMAKE_WORKFLOW.md`
- Codex/GPT bridge doc: `docs/CODEX_GPT_BRIDGE.md`
- Reference package builder: `scripts/build_video_reference_remake_package.py`
- Frame-stack roughcut builder: `scripts/build_frame_stack_roughcut.py`
- GPT bridge packet builder: `scripts/create_gpt_bridge_packet.py`
- Project scaffold now creates:
  - `00_admin/ai_bridge/`
  - `01_intake/analysis/video_reference_packages/`
  - `10_qa/reference_match/`

### Project Bridge

- Bridge policy: `00_admin/ai_bridge/bridge_policy.json`
- Task routing: `00_admin/ai_bridge/codex_gpt_task_routing.md`
- Accepted workflow decision: `00_admin/ai_bridge/decisions/video_reference_pixel_remake_workflow_v1.md`
- Accepted frame-stack strategy: `00_admin/ai_bridge/decisions/frame_stack_then_video_model_strategy_v1.md`

## Current Reference Package

Reference id: `reference-002-opening`

- Source copy: `01_intake/references/reference-002-opening.mp4`
- Manifest: `01_intake/analysis/video_reference_packages/reference-002-opening/manifest.json`
- Sampled frames: `01_intake/analysis/video_reference_packages/reference-002-opening/frames_sampled/`
- Contact sheet: `01_intake/analysis/video_reference_packages/reference-002-opening/contact_sheets/reference-002-opening_contact_sheet_2fps.jpg`
- Frame index: `01_intake/analysis/video_reference_packages/reference-002-opening/frame_index.csv`
- Scene detection: `01_intake/analysis/video_reference_packages/reference-002-opening/scene_detection/`
- Workflow checklist: `01_intake/analysis/video_reference_packages/reference-002-opening/workflow_checklist.md`
- Method recommendations: `01_intake/analysis/video_reference_packages/reference-002-opening/unit_method_recommendations.md`
- Frame-stack roughcut: `01_intake/analysis/video_reference_packages/reference-002-opening/roughcuts/reference-002-opening_frame_stack_2fps.mp4`
- Latest GPT packet: `00_admin/ai_bridge/packets/20260630_023556_reference-002-opening_pixel_remake.json`

## Codex / GPT Split

Codex:

- registers video,
- extracts frames,
- builds contact sheets,
- detects cut candidates,
- builds local roughcut,
- writes project files,
- runs Blender/previs,
- validates and updates handoff.

GPT:

- reads bounded packet only,
- decides shot rhythm,
- classifies units as image roughcut / AIGC video / Blender-previs,
- rewrites prompts,
- performs adversarial review.

## Three-Layer Production Rule

1. **Frame-stack/image roughcut first** for timing, montage, title-safe holds, simple composition, early style replacement.
2. **AIGC video model** for motion smoothness: bird wingbeats, hair/cloth, flare, clouds/water, short camera drift.
3. **Blender/previs first** for true long takes, spatial camera moves, aircraft/vehicle scale, multi-character blocking, strong axis/geography risk.

## Current Reference Media

- Duration: 23.01 seconds
- Video: 1920 x 1080, 30fps, H.264
- Sampled frames: 46
- Roughcut: 23 seconds, 960 x 540, 2fps
- All current project video files are inventoried in `10_qa/reports/video_content_analysis_20260630.md`.
- `01_intake/references/nadia_op_reference_002.mp4` is byte-identical to `01_intake/references/reference-002-opening.mp4`.
- `06_previs/playblasts/opening_24s_onetake_previs.mp4` is a generated/previs artifact, not accepted reference timing.

## Validation

Passed:

- `python3 -m py_compile scripts/create_aigc_project.py scripts/validate_aigc_project.py scripts/build_video_reference_remake_package.py scripts/build_frame_stack_roughcut.py scripts/create_gpt_bridge_packet.py`
- `python3 scripts/validate_aigc_project.py projects/blue-water-citypop-op`
- Temporary new-project scaffold validation with video reference directories and bridge files.
- MP4 probe confirmed `reference-002-opening_frame_stack_2fps.mp4` is readable.

## Important Production Note

The prior Blender file `06_previs/playblasts/opening_24s_onetake_previs.mp4` is kept as a superseded camera/blocking experiment. It must not drive the accepted remake timing. The active accepted unit map is now `VU_REF002_001_WHITE_BIRD_OPENING` through `VU_REF002_005_NADIA_CLOSEUP_ENTRY`, recorded in `00_admin/ai_bridge/decisions/reference_002_opening_unit_recut_v1.md`.

## Next Step

Regenerate `OP_SHOT_001` through `OP_SHOT_007` with the new `VU_REF002_*` prompts, then build a generated-keyframe frame-stack roughcut and compare it against `reference-002-opening_frame_stack_2fps.mp4`.
