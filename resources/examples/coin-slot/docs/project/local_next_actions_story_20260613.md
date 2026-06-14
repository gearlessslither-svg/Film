# 投币口 / Next Actions Under Latest Pack Rules

1. Generate A-priority pure MSB story frames from `configs/micro_storyboard_panel_plan.csv`, using approved character anchors, environment bible, and approved whitebox references.
2. Save generated files to their declared `pure_path`; do not place whiteboxes, contact sheets, or character references in final story folders as substitutes.
3. After each generated pure frame, run hash integrity checks and update `configs/frame_continuity_manifest.json` and `configs/asset_integrity_report.json`.
4. Only after pure QA passes, create annotated review copies.
5. Rebuild storyboard contact sheets from approved pure frames only, keeping whitebox and reference sheets separate.
