# Script-First Video Workflow Audit

Updated: 2026-06-30 04:22 Asia/Shanghai

## Verdict

PASS for the current project workflow gate.

The project now has a script-first video-unit workflow. The existing 42 keyframes remain intact, but their video-generation logic is no longer treated as 42 isolated videos. Each keyframe points back to a video unit, a role inside that unit, a group-level prompt, transition edges when applicable, and a previs/whitebox strategy.

## Current Project Evidence

- Director script: `03_story/scripts/director_shooting_script.md`
- Video units: `07_shots/video_units.json`
- Transition edges: `07_shots/transition_edges.json`
- Camera/previs manifest: `06_previs/camera_manifests/video_unit_camera_manifest.json`
- Unit video prompts: `07_shots/video_prompts_by_unit/`
- Per-card video prompts: `07_shots/video_prompts/OP_SHOT_001.md` through `OP_SHOT_042.md`
- Shot list: `07_shots/shot_list.csv`
- Idea board: `03_story/idea_board/idea_board.json`

## Counts Checked

- Idea board rows: 42
- Rows with `image_ready`: 42
- Per-card image prompts: 42
- Per-card video prompts: 42
- Per-card video prompts with unit-aware header: 42
- Per-card video prompts with `图1`/ordered-frame labels: 42
- `shot_list.csv` rows: 42
- `shot_list.csv` rows with `video_unit_id`: 42
- `shot_list.csv` rows with `keyframe_role`: 42
- `shot_list.csv` rows with `unit_prompt_path`: 42

Empty `transition_in_edges` or `transition_out_edges` cells mean the keyframe has no edge on that side; transition ownership is still stored in `07_shots/transition_edges.json`.

## Reference 002 Opening Recut

Status: active replacement plan for 00:00-00:23.

The previous 24-second Blender one-take previs was reviewed against `reference-002-opening` and superseded for accepted timing. The active opening structure is now:

- `VU_REF002_001_WHITE_BIRD_OPENING` — 00:00-00:04.50, `OP_SHOT_001`, `OP_SHOT_002`
- `VU_REF002_002_BIRD_CREDIT_SAFE_SKY` — 00:05.00-00:08.50, `OP_SHOT_003`
- `VU_REF002_003_CLOUD_BANK_AIRCRAFT_REVEAL` — 00:09.00-00:14.00, `OP_SHOT_004`, `OP_SHOT_005`
- `VU_REF002_004_TITLE_SAFE_HOLD_TO_FLARE` — 00:14.50-00:21.00, `OP_SHOT_006`
- `VU_REF002_005_NADIA_CLOSEUP_ENTRY` — 00:21.50-00:23.00, `OP_SHOT_007`

The old `VU_001_024_OPENING_SKY_BIRD_PLANE_ONETAKE` remains in the project only as a superseded review artifact. It is useful for camera blocking lessons, but it over-continuizes the opening and gives the aircraft too much importance compared with the reference.

All current project video files are inventoried in `10_qa/reports/video_content_analysis_20260630.md`. That report confirms the two reference MP4s are byte-identical, the frame-stack roughcut is a derived 2fps review video, and the 24s previs is independent generated/previs content.

## Global Template / Future Project Gate

The standard project scaffold now creates the script-first files by default:

- `03_story/scripts/director_shooting_script.md`
- `07_shots/video_units.json`
- `07_shots/transition_edges.json`
- `06_previs/camera_manifests/video_unit_camera_manifest.json`
- `07_shots/video_prompts_by_unit/README.md`
- expanded `07_shots/shot_list.csv` video-unit columns

The project validator now checks those contracts. A temporary project created from `scripts/create_aigc_project.py` passed `scripts/validate_aigc_project.py` with the new gate.

## Validation

Passed:

- `python3 -m py_compile scripts/create_aigc_project.py scripts/validate_aigc_project.py`
- `python3 scripts/validate_aigc_project.py projects/blue-water-citypop-op`
- JSON parse for `idea_board.json`, `video_units.json`, `transition_edges.json`, and `video_unit_camera_manifest.json`
- MP4 probe: 24.00 seconds, H.264, 1280 x 548, 24 fps
- Frame sequence count: 576

Known non-blocking mismatch:

- `scripts/validate_pipeline_state.py` still checks an older `01_AIGC` delivery structure and fails on missing legacy files. That failure does not indicate this standardized project folder or Blender previs is broken. Use `scripts/validate_aigc_project.py` for the current `projects/<slug>` contract.

## Remaining Decision

The remaining production work is not approval of the old one-take. The next production action is to regenerate `OP_SHOT_001` through `OP_SHOT_007` from the accepted `VU_REF002_*` prompts, then build and compare a generated-keyframe roughcut against the reference frame-stack roughcut.
