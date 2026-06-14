> 双语说明 / Bilingual note: 本文件保留英文原文，以避免破坏提示词、文件名、路径、字段名和脚本读取。中文使用时请把它视为生产记录、规则、索引或提示词资产；英文正文为可执行/可追溯原文。 / The English source text is preserved to keep prompts, filenames, paths, field names, and script parsing stable. Treat this as a production record, rule, index, or prompt asset; the English body is the executable and traceable source text.

# Whitebox Workflow Policy

## Purpose

Blender whitebox is a spatial lock, not an art source. It exists to keep recurring rooms, streets, stages, tables, character positions, camera axes, screen direction, and object anchors consistent across different shots and angles.

## Correct Chain

1. Write the director, character, environment, and spatial bibles.
2. Build or update `configs/blender_whitebox_spec.json`.
3. Generate the Blender scene, camera manifest, and whitebox renders.
4. Run camera QA and mark every camera as `approved`, `needs_fix`, or `rejected`.
5. Generate character reference sheets and environment master plates from the bibles.
6. Generate final story frames from approved visual anchors plus approved camera ids.
7. Run asset integrity QA before any frame can enter the final storyboard contact sheet.

## Whitebox Outputs

- `blender/project_whitebox.blend`
- `blender/whitebox_generator.py`
- `blender/camera_manifest.csv`
- `whitebox_renders/*.png`
- `configs/whitebox_camera_qa_report.json`
- `exports/whitebox_camera_contact.jpg`

These outputs are always `reference_only` unless explicitly marked `whitebox_proxy_only` for temporary edit blocking. They are never final art.

## Final Frame Acceptance

A frame can become `story` only if all are true:

- `asset_status` is `generated_final_story_frame`.
- It cites one character anchor, one environment anchor, and an approved `camera_id` when the scene is spatially recurring.
- Its hash is unique or explicitly marked `intentional_reuse`.
- Its hash does not match any whitebox render, root loose reference, character reference, environment reference, or style test.
- It does not visibly retain Blender/viewport artifacts: grey primitive materials, grid floor, flat clay layout, object labels, camera-safe overlays, low-poly blocking shapes, layout color overlays, or empty placeholder rectangles.
- It preserves at least two required spatial anchors from the whitebox camera.

## Contact Sheet Separation

Every project should keep these contact sheets separate:

- Whitebox camera contact sheet: spatial QA only.
- Visual anchor contact sheet: character/environment/style selection only.
- Storyboard contact sheet: final story frames only.
- Placeholder or rejected contact sheet: temporary, duplicate, proxy, or failed assets only.

If a full-story contact sheet contains whitebox renders, visual anchors, repeated placeholders, or proxy overlays, it is not proof that the project has enough final frames to edit.
