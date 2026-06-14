---
name: aigc-film-pipeline
description: Use when planning, continuing, QAing, or packaging an AIGC-first short-film production pipeline with story-stage locks, character continuity, Blender or whitebox spatial references, pure versus annotated image passes, audio cue sheets, animatics, final storyboard video, and validation scripts.
---

> 双语说明 / Bilingual note: 本文件保留英文原文，以避免破坏提示词、文件名、路径、字段名和脚本读取。中文使用时请把它视为生产记录、规则、索引或提示词资产；英文正文为可执行/可追溯原文。 / The English source text is preserved to keep prompts, filenames, paths, field names, and script parsing stable. Treat this as a production record, rule, index, or prompt asset; the English body is the executable and traceable source text.

# AIGC Film Pipeline

This skill turns a film idea or existing AIGC project folder into a staged production system. It is based on the Coin Slot workflow: lock story state first, lock space with whitebox, generate pure images, create annotated review versions, align sound to the same timeline, then rebuild and validate the animatic or storyboard video.

## Start Here

1. If continuing an existing project, read its `TASK_LOG.md`, `README.md`, and latest validation CSV before making production decisions.
2. Run the project validator when the repo has the expected structure:

```powershell
python scripts/validate_pipeline_state.py <project-root>
```

3. If starting a new project, create the same minimum tables before generating media: story stages, panel list, stage-state map, whitebox plan, image generation queue, audio cue sheet, and validation outputs.

## Core Rules

- Keep `story_stage` as the shared key across storyboard panels, character state, wardrobe state, environment state, audio cue, edit timing, and QA.
- Do not use a single character sheet for the whole film. Create stage-specific character references when clothing, dirt, injury, expression, prop state, or body tension changes.
- Do not skip whitebox for production panels. Whitebox is the spatial and camera constraint, not decoration.
- Keep pure and annotated assets separate. Pure images go to image/video generation; annotated images are only for human review and production communication.
- Every panel should express one visual state. Preparation, action, result, reaction, and transition frames are separate panels.
- Rebuild review panels, contact sheets, animatics, and validation after every meaningful batch.

## Tool Map

- `scripts/validate_pipeline_state.py`: checks project readiness and writes/updates pipeline validation.
- `apps/pipeline-hub/server.py`: local GUI hub for creating, linking, validating, analyzing, and reviewing standardized project folders.
- `scripts/analyze_aigc_project.py`: scans standardized `projects/<slug>/` folders, samples linked resources, and writes `10_qa/reports/project_audit_latest.md` for missing-work and aesthetic review.
- `scripts/autofill_aigc_project.py`: controlled autonomous repair agent that loops analyze -> fill -> analyze, writes safe missing artifacts, and queues or runs enabled Codex/image2/Blender/plugin adapter tasks.
- `scripts/seed_coin_slot_sample_project.py`: rebuilds the standardized 12-shot Coin Slot sample batch from archived CSV/prompt/stage-map resources.
- `scripts/visual/qa_whitebox_images.py`: validates whitebox renders and repeated composition risk.
- `scripts/visual/qa_whitebox_similarity.py`: compares near-duplicate whitebox images.
- `scripts/visual/make_contact_sheet.py`: builds contact sheets for QA and review.
- `scripts/visual/mark_pure_image_result.py`: marks generated pure-image rows as passed or needing regeneration.
- `scripts/visual/annotate_visual_asset.py`: creates annotated review copies after pure images pass.
- `scripts/visual/rebuild_final_storyboard_tables.py`: rebuilds production tables from current panel/image state.
- `scripts/visual/build_final_storyboard_panels.py`: creates 1280x720 final review panels and batch contact sheets.
- `scripts/visual/build_audio_guide.py` and `scripts/visual/build_clean_audio_mix.py`: generate timing-aligned guide audio.
- `scripts/visual/build_storyboard_animatic.py` and `scripts/visual/build_final_storyboard_video.py`: assemble animatic/storyboard video.
- `scripts/visual/validate_final_delivery.py`: validates final panels, audio, timing, and video delivery.
- `scripts/blender/`: Blender whitebox generation and render helpers.
- `scripts/keep-codex-awake.ps1`: Windows keep-awake helper for long local production runs.

## References

Load only the reference needed for the current task:

- `references/pipeline-operating-manual.md`: full continuation order and production gates.
- `references/next-project-rules.md`: reusable lessons for future AIGC film projects.
- `references/story-stage-continuity-rules.md`: stage IDs, character-state locks, and forbidden continuity breaks.
- `references/character-similarity-qa-protocol.md`: character distinctiveness and thumbnail-level QA.
- `references/whitebox-qa-protocol.md`: whitebox health, similarity, and panel-level QA rules.
- `references/visual-asset-dual-version-rules.md`: pure versus annotated asset rules.
- `references/micro-storyboard-rules.md`: micro-panel granularity and batching.
- `references/dialogue-voice-sound-music-plan.md`: dialogue, voice, SFX, ambience, and music planning.
- `references/runtime-resilience-and-keepawake.md`: long-run recovery and keep-awake rules.

Use `$aigc-film-project-auditor` when the user asks for one-click analysis of all current project steps, missing assets, aesthetic risks, or director-facing recommendations before batch generation.

## Output Standard

End substantial work with: current state, changed tables/assets, validation status, remaining blockers, and the next concrete production batch.
