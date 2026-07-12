# Ingestion Log - 2026-07-02

## Review Result

User-provided lessons from `coin-slot` and `blue-water-citypop-op` were reviewed and ingested into `lesson-index.json`.

## Corrections Before入库

- "青少年题材少碰" was not stored as an absolute ban. It was rewritten as a medium-reliability caution: minor-centered stories add policy and review friction, so avoid them unless the story needs them.
- Free video quotas for 小云雀, 豆包, and 即梦 were not stored as durable rules. They are time-sensitive and require current verification before each new project.
- The WeChat-bean promotion result was not stored as a universal marketing rule. It is one low-sample experiment and remains `experimental`.
- CapCut/Jianying frame interpolation jitter was stored as a QA risk, not as a confirmed root-cause statement.

## Accepted Active Lessons

- Establish setting chapters and global locks before batch generation.
- Use Blender/whitebox video for spatial/camera understanding when needed, while treating static whitebox stills as broad geometry constraints only.
- Use video-reference workflows for complex motion/expression scenes when current tools support them.
- Separate target-style upload keyframes from official/source/candidate reference images.
- Preserve director semantic meaning above technical cuts.
- Treat frame movement as a viewer-attention and shot-meaning tool.

## Evidence Checked

- `projects/_recycle_bin/coin-slot/05_asset_bible/characters/coin_slot_character_bible.md`
- `projects/_recycle_bin/coin-slot/05_asset_bible/locations/coin_slot_location_bible.md`
- `projects/_recycle_bin/coin-slot/05_asset_bible/props/coin_slot_prop_bible.md`
- `projects/_recycle_bin/coin-slot/05_asset_bible/continuity/coin_slot_continuity_locks.md`
- `projects/_recycle_bin/coin-slot/06_previs/qa/coin_slot_previs_notes.md`
- `projects/_recycle_bin/coin-slot/10_qa/reports/director_aesthetic_review_latest.md`
- `projects/blue-water-citypop-op/11_delivery/manifests/PROJECT_FINAL_SUMMARY_20260702.md`
- `projects/blue-water-citypop-op/11_delivery/manifests/PROJECT_LESSONS_20260702.json`
