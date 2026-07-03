---
name: aigc-film-pipeline
description: Use when planning, continuing, QAing, or packaging an AIGC-first short-film production pipeline with setting-chapter-first asset locks, reference-video analysis, difference-driven frame promotion, story-stage locks, character/prop/scene continuity, Blender or whitebox spatial references, pure versus annotated image passes, audio cue sheets, animatics, final storyboard video, and validation scripts.
---

> 双语说明 / Bilingual note: 本文件保留英文原文，以避免破坏提示词、文件名、路径、字段名和脚本读取。中文使用时请把它视为生产记录、规则、索引或提示词资产；英文正文为可执行/可追溯原文。 / The English source text is preserved to keep prompts, filenames, paths, field names, and script parsing stable. Treat this as a production record, rule, index, or prompt asset; the English body is the executable and traceable source text.

# AIGC Film Pipeline

This skill turns a film idea, reference video, still-image set, or existing AIGC project folder into a staged production system. The first production gate is always the setting chapter: lock characters, props, vehicles, animals, symbols, locations, environments, and style before shot planning or generation. Then lock story state, analyze reference-video frame differences when applicable, lock space with whitebox, generate pure images, create annotated review versions, align sound to the same timeline, and rebuild/validate the animatic or storyboard video.

## Start Here

1. Before opening, creating, or continuing any project, read the baseline project rules for the current source type. Always read `references/next-project-rules.md` and `references/setting-chapter-first-rules.md`; for reference-video projects also read `references/frame-difference-asset-promotion-rules.md`.
2. Treat every project as `setting chapter first`, regardless of whether the source is a script, a reference video, a still image set, or a loose idea. Before shot scheduling, whitebox, keyframe generation, or video packaging, create or locate the setting chapter / asset bible.
3. The setting chapter must enumerate all known characters, props, vehicles, animals, symbols, locations, scene environments, style rules, and stage/state variants. Mark unknown but likely-needed assets as `needs_setting_lock`; do not let AIGC invent them later.
4. Get director approval for the setting chapter and its asset-lock plan before entering production. If the user asks to generate shots before this gate, state the missing setting gate and create the setting chapter first.
5. If continuing an existing project, read its setting chapter / `05_asset_bible`, latest handoff, `TASK_LOG.md`/`README.md` if present, and latest validation CSV before making production decisions.
6. Run the project validator when the repo has the expected structure:

```powershell
python scripts/validate_pipeline_state.py <project-root>
```

7. If starting a new standardized `Story/Film/projects/<slug>` project, create the script/video contract only after the setting chapter gate: `03_story/scripts/director_shooting_script.md`, `07_shots/video_units.json`, `07_shots/transition_edges.json`, `06_previs/camera_manifests/video_unit_camera_manifest.json`, `07_shots/video_prompts_by_unit/`, and a `07_shots/shot_list.csv` whose keyframes point back to their video units.
8. For legacy Coin Slot-style projects, keep the existing story-stage/panel/whitebox/audio tables, but do not use that older table set as an excuse to skip the setting chapter gate or script-first/video-unit contract on new projects.

## Core Rules

- Gate 0 is the setting chapter. No shot list, video unit, keyframe prompt, whitebox, pure image, AIGC video package, or final edit may be treated as production-ready until the relevant characters, props, vehicles, animals, symbols, locations, and scene environments are listed and approved.
- For video-first projects, analyze the reference video into a setting chapter before shot-level remake planning. Use the reference video for timing, camera, motion, and edit rhythm, but use the approved setting chapter to control who/what/where appears.
- For reference-video projects, run local analysis by shot/video unit, not by one global FPS. First create baseline coverage for the whole video and every unit start/end, then assign each unit an adaptive desired analysis density based on film function: low for static holds, medium for slow environment/prop movement, high for action, group blocking, transitions, and fast prop/vehicle motion. Keep screenshots on disk and pass only compact metadata, contact sheets, or selected representative frames through the conversation unless direct visual inspection is required.
- Do not equate sampling density with generation density. A unit may need 6-12fps analysis to understand motion, but still only promote start/end plus the few frames that carry new composition, blocking, prop state, or transition function.
- Score candidate frames against existing approved anchors and already generated expansion assets, not only against the immediately previous sampled frame. A high local delta can be a hard cut, text overlay, or noise; a high novelty-to-existing-anchor score plus a clear film-function reason is stronger evidence for promotion.
- Dense extracted frames are only `candidate_reference_frame` records. They are not final keyframes, project assets, or preview frames until promoted by visual/semantic difference and regenerated as new pure images.
- Local analysis is a candidate ranker, not the final director. It is reliable for similarity, motion, shot-boundary, color/light, and composition-change signals, but semantic importance must be checked with film judgment, approved setting locks, and targeted visual review when ambiguous.
- Promote frames that materially change composition, camera position, character pose, action state, prop state, scene state, story beat, or transition logic. Also preserve critical first/final frames of a video unit even when the middle is visually continuous.
- For one-take, slow hold, continuous blocking, or Nemo/captain-style shots, collapse similar frames to start frame + end frame + one or two essential middle transition frames. Use precise prompts plus the reference video for the continuous motion instead of blindly generating every sampled frame.
- For reference-video shot boundaries, run a frame-level pass when precision matters: scan at source FPS for grayscale/color/edge deltas, flag one-frame or two-frame flash inserts, and cross-check with PySceneDetect/OpenCV when available. A 2fps contact sheet is not enough to catch brief aircraft, character, prop, or transition flashes.
- Do not force every detected visual beat into a separate AIGC unit. If the reference is a 20-25 second continuous opening or one-take phrase, split it into 2-3 practical long generation chunks with ordered anchors and precise prompt instructions, rather than many tiny pseudo-shots.
- Before generation, review promoted candidates as a P1/P2/P3 queue. P1 is the next small generation batch; P2 is review later; P3 is reference-video-only or already handled. Remove title-safe empties, subtitle-only differences, repeated near-duplicates, and accepted holds from the first generation batch.
- Every promoted reference frame must become a real generated image asset with stable `item_id`, parent `video_unit_id`, source timecode, `difference_reason`, prompt path, output path, and QA status before it can increase the project's final frame count or appear in an animatic/preview video.
- Expanded previews must be built from the expanded generated-asset manifest: existing approved assets plus newly promoted/generated assets. A dense extraction pass that does not create new generated assets must not be described as an expanded preview.
- For script-first projects, extract the setting chapter from the script before creating the video-unit contract. Do not let later shot prompts invent missing characters, props, or locations.
- Keep `story_stage` as the shared key across storyboard panels, character state, wardrobe state, environment state, audio cue, edit timing, and QA.
- Do not use a single character sheet for the whole film. Create stage-specific character references when clothing, dirt, injury, expression, prop state, or body tension changes.
- Lock identity before scale. The first director-approved face, costume, prop, vehicle, location, or environment image becomes the official lock for that asset/stage; later images must preserve it instead of redesigning it.
- Do not let AIGC reinvent characters, locations, or props shot by shot. Any image with a changed face, swapped costume, altered hero prop, redesigned vehicle, or inconsistent location anchor is `identity_continuity_fail`, even if it is attractive.
- Multi-character, group, crowd, distant-face, montage, and action frames require explicit identity anchors from approved lock images. Text-only prompts are not enough for those frames.
- A generated keyframe cannot become `video_ready_pass` until it passes separate checks for composition, no-text/no-logo safety, character identity, prop continuity, scene continuity, and stage state.
- Do not skip whitebox for production panels. Whitebox is the spatial and camera constraint, not decoration.
- Script controls video units; video units control keyframes; keyframe relationships control AIGC prompts. Do not infer one-take or continuity from generated images alone.
- A keyframe is not automatically a video shot. A video unit may contain one keyframe, many ordered keyframes, or a montage of hard-cut keyframes.
- Multi-keyframe video prompts must explicitly label `图1`, `图2`, `图3` and explain the connection, transition, spatial continuity, and screen direction.
- Every image-to-video / AIGC video generation prompt must include a hard audio rule: sound effects / ambience only; no music, no BGM, no soundtrack. Final edit music is planned separately unless the user explicitly overrides this for a specific project.
- For opening/title/map-mechanism one-takes, plan the camera route before generating or prompting: real displacement, parallax, changing scale, and final reveal. Do not accept a static shot where objects only rise in place unless the director explicitly asks for that.
- AIGC video segment packages must have a human-facing prompt index. The default external-generation entry is `AIGC_VIDEO_PROMPT_INDEX.md` plus per-unit `PROMPT_ONLY.md`; full `AIGC_VIDEO_GENERATION_BRIEF.md` files are machine/QA packets, not the first file a director should open.
- When packages are rebuilt after new generated images are added, the prompt-only file must list the current ordered generated anchors explicitly. Do not use stale `Existing Unit Prompt` text as the primary prompt if it omits newly generated R/P-pass images; older prompt text may be quoted only as history.
- Do not copy every global asset lock into every video unit by default. Keep one package-level `_global_asset_locks/` folder, and for each unit write `active_asset_locks.json` / prompt-only active-lock lines containing only characters, props, vehicles, symbols, animals, or scene locks actually visible or required in that unit. Empty sky, black frames, title-safe holds, and abstract texture units should list no active locks unless a lock is visibly present.
- A per-unit `asset_locks/` folder is allowed only for intentionally self-contained offline transfer, and must be described as redundant. It must not imply that unrelated characters or props appear in that shot.
- One-take, complex blocking, vehicle/aircraft follow, multi-character continuous motion, or strong-axis shots require first/final/critical keyframes plus Blender whitebox/high-proxy models and camera animation/playblast before final AIGC video rendering.
- Keep pure and annotated assets separate. Pure images go to image/video generation; annotated images are only for human review and production communication.
- Every panel should express one visual state. Preparation, action, result, reaction, and transition frames are separate panels.
- Rebuild review panels, contact sheets, animatics, and validation after every meaningful batch.
- Keep Codex handoff packets scoped to the smallest useful context. Normal storyboard image, external retouch analysis, and external retouch image packets should include only target cards/images, required references, revision notes, spatial/continuity/whitebox constraints, and callback schema. Do not embed the full story, full `idea_board`, full project bible, or unrelated rows unless the task is explicitly a project audit, merge, or remote autopilot run.
- Prefer compact callbacks. For card analysis or text-only updates, return `row_updates` patches keyed by `card_uid`/`item_id`; do not POST a full board unless the operation genuinely rewrites project structure.
- Treat reference images as hard intent, not decoration. If a card says to replace a face, character, prop, or environment with project references, preserve that modification intent even when the generation prompt must be rephrased for safety.

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
- `references/setting-chapter-first-rules.md`: Gate 0 rules for creating, approving, and enforcing characters, props, scenes, environments, and style before any shot production.
- `references/next-project-rules.md`: reusable lessons for future AIGC film projects.
- `references/frame-difference-asset-promotion-rules.md`: reference-video dense extraction, visual-difference selection, candidate-to-asset promotion, and expanded-preview rules.
- `references/identity-lock-and-asset-continuity-rules.md`: hard rules for approved character faces, scene anchors, props, vehicles, group frames, and continuity QA.
- `references/story-stage-continuity-rules.md`: stage IDs, character-state locks, and forbidden continuity breaks.
- `references/character-similarity-qa-protocol.md`: character distinctiveness and thumbnail-level QA.
- `references/whitebox-qa-protocol.md`: whitebox health, similarity, and panel-level QA rules.
- `references/visual-asset-dual-version-rules.md`: pure versus annotated asset rules.
- `references/micro-storyboard-rules.md`: micro-panel granularity and batching.
- `references/dialogue-voice-sound-music-plan.md`: dialogue, voice, SFX, ambience, and music planning.
- `references/runtime-resilience-and-keepawake.md`: long-run recovery and keep-awake rules.

Use `$aigc-film-project-auditor` when the user asks for one-click analysis of all current project steps, missing assets, aesthetic risks, or director-facing recommendations before batch generation.

## Pipeline Hub Handoff Rule

Only remote/autopilot packets may carry broad project context. Ordinary per-card production packets must be compact:

- Analysis cards: selected targets + global/single references + revision notes + compact patch callback.
- Image cards: selected targets + required references/continuity locks + whitebox/spatial constraints + output paths.
- External retouch cards: source images + retouch notes + global/single references; no unrelated story context.
- Callback payloads: image outputs or `row_updates`, with `image_analysis` and `video_prompt` when an image is returned.

## Output Standard

End substantial work with: current state, changed tables/assets, validation status, remaining blockers, and the next concrete production batch.
