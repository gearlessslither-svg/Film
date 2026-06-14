> 双语说明 / Bilingual note: 本文件保留英文原文，以避免破坏提示词、文件名、路径、字段名和脚本读取。中文使用时请把它视为生产记录、规则、索引或提示词资产；英文正文为可执行/可追溯原文。 / The English source text is preserved to keep prompts, filenames, paths, field names, and script parsing stable. Treat this as a production record, rule, index, or prompt asset; the English body is the executable and traceable source text.

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
