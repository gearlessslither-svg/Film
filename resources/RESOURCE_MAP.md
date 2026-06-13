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
