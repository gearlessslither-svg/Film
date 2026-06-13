> 双语说明 / Bilingual note: 本文件保留英文原文，以避免破坏提示词、文件名、路径、字段名和脚本读取。中文使用时请把它视为生产记录、规则、索引或提示词资产；英文正文为可执行/可追溯原文。 / The English source text is preserved to keep prompts, filenames, paths, field names, and script parsing stable. Treat this as a production record, rule, index, or prompt asset; the English body is the executable and traceable source text.

# Resource Map

`resources/examples/coin-slot/` is a lightweight case study extracted from the Coin Slot project.

- `case-study-readme.md`: original project index.
- `csv/`: production table examples for panels, stage state, pure image queues, audio cues, whitebox QA, visual QA, and delivery validation.
- `configs/`: reusable new-project manifests, continuity maps, edit/render plans, asset-integrity checks, audio/animatic manifests, and QA templates imported from the local copy pack.
- `blender/`: small whitebox example files and camera manifests.
- `media/`: Git LFS archive of Coin Slot image, audio, video, Blender, and in-project zip deliverables, preserving source-relative paths.
- `docs/new-project-copy-pack/`: reusable startup manual, camera-subject continuity rules, and skill iteration governance imported from `NEW_PROJECT_COPY_PACK_v1`.
- `local-story-20260613/`: local Story conflict snapshots kept separate from the remote mainline CSVs.

RAR backup packages are intentionally excluded. Keep future bulky generated media in `media/` only when it is meant to be part of the LFS archive.

`projects/coin-slot/` is the standardized project-folder version of this same case study. It keeps the reusable production structure, while `assets_link_map.md` points back to this resource archive instead of duplicating the large LFS media.
