# 12-Shot Generation Plan

Scope: seeded 12-shot sample batch from `07_shots/shot_list.csv`.

Inputs:

- image prompts: `07_shots/prompts/`
- video prompts: `07_shots/video_prompts/`
- camera manifest: `06_previs/camera_manifests/coin_slot_sample_camera_manifest.csv`
- linked historical outputs: `resources/examples/coin-slot/media/01_AIGC/`

Policy:

- keep pure outputs separate from annotated review copies,
- record model, seed, reference paths, control paths, and failure reasons per shot,
- do not overwrite linked archive media.
