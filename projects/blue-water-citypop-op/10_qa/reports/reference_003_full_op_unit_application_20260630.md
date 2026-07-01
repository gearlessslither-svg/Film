# Reference 003 Full OP Unit Application Audit

Updated: 2026-06-30T04:45:05+08:00

## Verdict

PASS for structural application. The full 84.44s OP reference is now the official project unit map.

## Applied Counts

- Units: 21 (`VU_REF003_001` through `VU_REF003_021`)
- Keyframe cards mapped: 42 (`OP_SHOT_001` through `OP_SHOT_042`)
- Transition edges: 41
- Board status after rewrite: `prompt_ready_reference003` for all 42 cards

## Important Correction

The earlier `reference-002-opening` plan and `REFERENCE002_REGEN_20260630` trial images are superseded. They must not be used as accepted 1:1 remake output.

## Files Updated

- `03_story/scripts/director_shooting_script.md`
- `03_story/idea_board/idea_board.json`
- `03_story/idea_board/idea_board.md`
- `07_shots/video_units.json`
- `07_shots/transition_edges.json`
- `06_previs/camera_manifests/video_unit_camera_manifest.json`
- `07_shots/shot_list.csv`
- `07_shots/prompts/OP_SHOT_001.md` through `OP_SHOT_042.md`
- `07_shots/video_prompts/OP_SHOT_001.md` through `OP_SHOT_042.md`
- `07_shots/video_prompts_by_unit/VU_REF003_*.md`

## Next Flow Step

Generate official keyframes from `prompt_ready_reference003`, starting with a small visual QA batch before attempting larger production batches.
