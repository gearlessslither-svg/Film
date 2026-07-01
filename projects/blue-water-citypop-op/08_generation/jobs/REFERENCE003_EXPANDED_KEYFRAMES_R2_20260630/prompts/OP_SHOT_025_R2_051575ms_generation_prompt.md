# OP_SHOT_025_R2_051575ms R2 expanded keyframe generation prompt

Use case: photorealistic-natural
Asset type: Reference-003 expanded real keyframe asset
Parent shot: `OP_SHOT_025`
Reference time: `51.575` seconds
Dense reference frame: `08_generation/jobs/REFERENCE003_EXPANDED_KEYFRAMES_R2_20260630/refs/expanded_selected/OP_SHOT_025_R2_051575ms_ref.jpg`
Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
Asset locks: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`

## Primary Request

Generate a new 21:9 live-action keyframe asset for this exact dense reference moment. Use the dense reference frame for pose, camera angle, timing, motion phase, and scene layout only. Use the asset locks for all recurring faces, costumes, props, vehicles, locations, and symbols.

## Parent Shot Context

Main group lineup in a bright character tableau, no text overlay.

## Lock Summary

- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_011_v2.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_012.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_014.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_014.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_016_v2.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_016_v2.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_016_v2.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_032.png`
- `electra` (needs_setting_lock)
- `gargoyle` (needs_setting_lock)
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_035.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630/outputs/OP_SHOT_003.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_007.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/outputs/OP_SHOT_024_VEHICLE_LOCK_R1.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_026.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_030.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_038.png`

## Rejection Conditions

- Do not copy anime art, subtitles, lyrics, credits, source text, logos, or watermarks.
- Do not redesign recurring faces, costumes, props, vehicles, animals, locations, or symbols.
- Nadia must match OP_SHOT_011_v2 whenever visible.
- Grandis vehicle/action craft must match the R1 OP_SHOT_024 vehicle lock whenever visible.
- Minors must remain age-appropriate and non-sexualized.
- Output must be a real generated image asset, not a reference placeholder.

## Output

- 1915x821 or higher, 21:9, clean image only.
- Planned output path: `08_generation/jobs/REFERENCE003_EXPANDED_KEYFRAMES_R2_20260630/outputs/OP_SHOT_025_R2_051575ms.png`
