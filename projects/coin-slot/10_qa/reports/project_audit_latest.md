# AIGC Project Audit Report

Generated at: 2026-06-13T16:32:57+08:00

## Executive Summary

- Project: 投币口 (`coin-slot`)
- Project path: `E:\视觉\coin-slot-aigc-toolkit\projects\coin-slot`
- Audit status: **pass**
- Readiness score: **100%**
- Stage status: 12 pass, 0 warn, 0 fail
- Project files scanned: 78 (text: 78)
- Linked resource files scanned: 1073 (3d: 2, archive: 2, audio: 98, image: 899, text: 68, video: 4)
- Shot list rows: 12

This is a deterministic asset and workflow scan. It identifies structural gaps, template-only files, missing production evidence, and a representative sample for AI-assisted film/aesthetic review.

## Sampling Method

- Sample size limit: 24
- Priority order: project manifests, director/creative docs, shot tables, then representative text/image/video/audio/3D files.
- Placeholder files such as `.gitkeep` are ignored.
- Linked roots considered:
- E:\视觉\coin-slot-aigc-toolkit\resources\examples\coin-slot

## Stage Coverage

| Stage | Status | Files | Missing | Weak / Template |
| --- | --- | --- | --- | --- |
| 00_admin | pass | 4 | - | - |
| 01_intake | pass | 4 | - | - |
| 02_direction | pass | 3 | - | - |
| 03_story | pass | 3 | - | - |
| 04_lookdev | pass | 5 | - | - |
| 05_asset_bible | pass | 5 | - | - |
| 06_previs | pass | 6 | - | - |
| 07_shots | pass | 26 | - | - |
| 08_generation | pass | 4 | - | - |
| 09_edit | pass | 5 | - | - |
| 10_qa | pass | 7 | - | - |
| 11_delivery | pass | 3 | - | - |

## Priority Recommendations

| Priority | Stage | Problem | Suggested next action |
| --- | --- | --- | --- |
| P1 | 01_intake | 已有外部/样例资源被链接，但尚未完全归拢到标准阶段目录。 | 按 assets_link_map.md 把旧资源分配到 intake、story、previs、shots、generation 的对应阶段，或保留链接并写清证据来源。 |
| P1 | 04_lookdev | 需要建立审美基准，不能只靠单张参考图推进。 | 补一组风格帧、色彩脚本、光照逻辑、材质参考和禁止项，形成可复用 look bible。 |
| P1 | 06_previs | 白模精度会直接决定 AIGC 的空间稳定性。 | 把关键场景做成更可读的 blocking：比例、站位、镜头高度、焦段、遮挡、前中后景都要可视化。 |
| P2 | 09_edit | 声音和剪辑节奏应尽早进入审美判断。 | 为每个故事节拍建立声音意图、静默点、环境声、音效和音乐推进，而不是等画面完成后补。 |

## Sampled Assets

| Origin | Category | Size KB | Path |
| --- | --- | --- | --- |
| project | text | 0.5 | 00_admin/director_brief.md |
| project | text | 0.9 | 00_admin/project_log.md |
| project | text | 0.9 | 02_direction/creative_brief.md |
| project | text | 6.5 | 07_shots/shot_list.csv |
| project | text | 1.2 | assets_link_map.md |
| project | text | 1.9 | project.yaml |
| linked | image | 518.6 | media/01_AIGC/final_storyboard_contact_sheets/B01_final_storyboard_contact_sheet_v002.jpg |
| linked | video | 17837.5 | media/01_AIGC/exports/animatic/coin_slot_storyboard_animatic_v001.mp4 |
| linked | audio | 3937.5 | media/01_AIGC/audio/music/MUS_003_8bit_stage_loop.wav |
| linked | 3d | 183.3 | blender/coin_slot_whitebox.blend |
| project | text | 0.6 | 05_asset_bible/character_stage_locks/coin_slot_character_stage_locks.md |
| linked | archive | 129570.4 | media/01_AIGC/exports/coin_slot_final_storyboard_audio_video_v002_review_package.zip |
| linked | image | 500.7 | media/01_AIGC/final_storyboard_contact_sheets/B02_final_storyboard_contact_sheet_v002.jpg |
| linked | video | 12425.2 | media/01_AIGC/exports/animatic/coin_slot_storyboard_animatic_v001_silent.mp4 |
| linked | audio | 7875.0 | media/01_AIGC/audio_clean/music/MUS_003_8bit_stage_loop.wav |
| linked | 3d | 183.3 | media/01_AIGC/blender/coin_slot_whitebox.blend |
| project | text | 0.4 | 05_asset_bible/characters/coin_slot_character_bible.md |
| linked | archive | 63545.8 | media/01_AIGC/exports/coin_slot_aigc_overnight_package.zip |
| linked | image | 547.1 | media/01_AIGC/final_storyboard_contact_sheets/B03_final_storyboard_contact_sheet_v002.jpg |
| linked | video | 45896.8 | media/01_AIGC/exports/final_video/coin_slot_final_storyboard_video_v002.mp4 |
| linked | audio | 1500.0 | media/01_AIGC/audio/ambience/AMB_001_compound_night_loop.wav |
| project | text | 3.8 | 06_previs/camera_manifests/coin_slot_sample_camera_manifest.csv |
| linked | image | 639.8 | media/01_AIGC/final_storyboard_contact_sheets/B04_final_storyboard_contact_sheet_v002.jpg |
| linked | video | 37815.3 | media/01_AIGC/exports/final_video/coin_slot_final_storyboard_video_v002_silent.mp4 |

## Film And Aesthetic Review Checklist

Use the project files and sampled assets to judge:

- Premise: Is the core cinematic idea clear in one sentence, and is the emotional promise specific?
- Story engine: Are conflict, escalation, reversal, payoff, and audience memory designed rather than accidental?
- Visual hierarchy: Does each image have a clear subject, readable silhouette, foreground/midground/background, and motivated negative space?
- Cinematography: Are lens, camera height, movement, blocking, focus, and shot size chosen for story pressure?
- Lighting: Is light motivated by space, time, source, emotion, genre, and material response?
- Color: Is there a color script with contrast, progression, and scene-to-scene logic?
- Production design: Do characters, props, locations, materials, typography, and scale support the same world?
- Continuity: Are character state, wardrobe, dirt, damage, prop state, spatial geography, and screen direction locked per stage?
- Previs: Does the whitebox solve scale, occlusion, camera, staging, and image-model control layers?
- Editing: Is there rhythm across preparation, action, result, reaction, and transition frames?
- Sound: Are voice, silence, ambience, Foley, sound effects, and music designed as story assets?
- AIGC stability: Are prompts, negative constraints, references, control layers, and QA loops strong enough for batch generation?

## Suggested AI Follow-Up Prompt

```text
Use $aigc-film-project-auditor to turn this scan into a director-facing audit.

Project: 投币口 (`coin-slot`)
Project folder: E:\视觉\coin-slot-aigc-toolkit\projects\coin-slot
Latest scan: 10_qa/reports/project_audit_latest.md

Focus the human report on:
- P0 missing work before batch generation.
- Whether the idea, story, lookdev, asset bible, previs, shot list, sound, and delivery plan are industrially ready.
- Aesthetic risks: weak visual hierarchy, unclear lens logic, unmotivated light, missing color script, generic character silhouettes, unstable spatial continuity, weak edit rhythm, and insufficient sound design.
- The smallest next batch that would make the project materially more stable.
```
