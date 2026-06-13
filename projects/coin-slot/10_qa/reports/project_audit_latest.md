# AIGC Project Audit Report

Generated at: 2026-06-13T15:53:37+08:00

## Executive Summary

- Project: 投币口 (`coin-slot`)
- Project path: `E:\视觉\coin-slot-aigc-toolkit\projects\coin-slot`
- Readiness score: **50%**
- Stage status: 0 pass, 12 warn, 0 fail
- Project files scanned: 8 (text: 8)
- Linked resource files scanned: 1073 (3d: 2, archive: 2, audio: 98, image: 899, text: 68, video: 4)
- Shot list rows: 0

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
| 00_admin | warn | 3 | - | director_brief |
| 01_intake | warn | 0 | - | source_inputs, references, analysis |
| 02_direction | warn | 1 | - | creative_brief, options, approvals |
| 03_story | warn | 0 | - | outlines, scripts, beats |
| 04_lookdev | warn | 0 | - | styleframes, palettes, lighting, references |
| 05_asset_bible | warn | 0 | - | characters, character_stage_locks, locations, props, continuity |
| 06_previs | warn | 0 | - | blender, camera_manifests, renders, control_layers, qa |
| 07_shots | warn | 1 | - | keyframes, prompts, video_prompts |
| 08_generation | warn | 0 | - | jobs, image_outputs, video_outputs, rejects |
| 09_edit | warn | 0 | - | rough_cut, audio, subtitles, color |
| 10_qa | warn | 0 | - | reports, fix_queue |
| 11_delivery | warn | 0 | - | exports, packages, manifests |

## Priority Recommendations

| Priority | Stage | Problem | Suggested next action |
| --- | --- | --- | --- |
| P0 | 02_direction | 存在模板化、空目录或内容不足的资产: creative_brief, options, approvals | 需要最终创意方向、故事方向、美术方向和确认记录。；需要保留 2 到 4 个方向方案，便于导演选择。；需要方向确认证据，避免后续批量返工。 |
| P0 | 03_story | 存在模板化、空目录或内容不足的资产: outlines, scripts, beats | 需要故事大纲、结构、转折和情绪曲线。；需要剧本、旁白、台词或无对白叙事说明。；需要场次/节拍表，供分镜和声音同步。 |
| P0 | 04_lookdev | 存在模板化、空目录或内容不足的资产: styleframes, palettes, lighting, references | 需要风格帧或关键画面预览。；需要色彩体系、材质关系和视觉对比策略。；需要光照逻辑、时间、空间和情绪规则。；需要可解释的美术/摄影/类型片参考。 |
| P0 | 05_asset_bible | 存在模板化、空目录或内容不足的资产: characters, character_stage_locks, locations, props, continuity | 需要角色设定、脸型、服装、姿态和区分度。；需要不同故事阶段的角色状态锁定。；需要场景设定、空间关系和可拍摄区域。；需要关键道具、使用状态和连续性规则。 |
| P0 | 06_previs | 存在模板化、空目录或内容不足的资产: blender, camera_manifests, renders, control_layers, qa | 需要白模、场景几何、角色站位和镜头约束。；需要镜头机位、焦段、运动和构图说明。；需要白模预览图，便于空间关系审核。；需要深度、线稿、法线、分割等生成控制层。 |
| P0 | 07_shots | 存在模板化、空目录或内容不足的资产: keyframes, prompts, video_prompts | 需要关键分镜图或锁定帧。；需要图片生成提示词。；需要视频生成提示词和运动约束。 |
| P0 | 07_shots | 镜头表没有镜头行，无法驱动批量图像/视频生成。 | 先建立 shot_id、story_beat、camera、action、lighting、prompt_path、status 等字段的镜头级任务。 |
| P1 | 00_admin | 存在模板化、空目录或内容不足的资产: director_brief | 导演意图、保留项、禁止方向需要有真实内容。 |
| P1 | 01_intake | 存在模板化、空目录或内容不足的资产: source_inputs, references, analysis | 需要归档导演原始输入：文字、截图、视频、参考图。；需要整理外部参考和可复用视觉依据。；需要有 AI 对输入材料的分析记录。 |
| P1 | 01_intake | 已有外部/样例资源被链接，但尚未完全归拢到标准阶段目录。 | 按 assets_link_map.md 把旧资源分配到 intake、story、previs、shots、generation 的对应阶段，或保留链接并写清证据来源。 |
| P1 | 04_lookdev | 需要建立审美基准，不能只靠单张参考图推进。 | 补一组风格帧、色彩脚本、光照逻辑、材质参考和禁止项，形成可复用 look bible。 |
| P1 | 06_previs | 白模精度会直接决定 AIGC 的空间稳定性。 | 把关键场景做成更可读的 blocking：比例、站位、镜头高度、焦段、遮挡、前中后景都要可视化。 |
| P1 | 08_generation | 存在模板化、空目录或内容不足的资产: jobs, image_outputs, video_outputs, rejects | 需要生成批次、模型参数、失败原因和复跑策略。；需要图片输出或已归档链接。；需要视频输出或已归档链接。；需要保留废片原因，避免重复犯错。 |
| P1 | 09_edit | 存在模板化、空目录或内容不足的资产: rough_cut, audio, subtitles, color | 需要粗剪、animatic 或节奏样片。；需要对白、旁白、音效、环境声、音乐或临时声轨。；需要字幕或文字节奏稿。；需要调色参考、LUT 或色彩一致性说明。 |
| P1 | 10_qa | 存在模板化、空目录或内容不足的资产: reports, fix_queue | 需要 QA 报告、审片记录和修复建议。；需要待修复项、优先级和责任阶段。 |
| P1 | 11_delivery | 存在模板化、空目录或内容不足的资产: exports, packages, manifests | 需要最终导出文件或交付路径。；需要交付包。；需要交付清单、版本和素材来源。 |
| P2 | 09_edit | 声音和剪辑节奏应尽早进入审美判断。 | 为每个故事节拍建立声音意图、静默点、环境声、音效和音乐推进，而不是等画面完成后补。 |

## Sampled Assets

| Origin | Category | Size KB | Path |
| --- | --- | --- | --- |
| project | text | 0.2 | 00_admin/director_brief.md |
| project | text | 0.2 | 00_admin/project_log.md |
| project | text | 0.1 | 02_direction/creative_brief.md |
| project | text | 0.2 | 07_shots/shot_list.csv |
| project | text | 1.2 | assets_link_map.md |
| project | text | 1.9 | project.yaml |
| project | text | 0.6 | 00_admin/model_config.yaml |
| project | text | 1.6 | README.md |
| linked | text | 4.0 | blender/camera_manifest.csv |
| linked | text | 48.8 | blender/whitebox_v2_manifest.csv |
| linked | text | 6.8 | case-study-readme.md |
| linked | text | 71.5 | csv/19_micro_storyboard_188_panels.csv |
| linked | text | 6.4 | csv/audio_assembly_manifest.csv |
| linked | text | 1.8 | csv/character_similarity_qa.csv |
| linked | text | 2.1 | csv/character_stage_asset_plan.csv |
| linked | text | 5.9 | csv/dialogue_voice_assets.csv |
| linked | text | 3.3 | csv/dialogue_voice_decision_table.csv |
| linked | text | 0.5 | csv/final_delivery_validation_v002.csv |
| linked | text | 115.1 | csv/micro_storyboard_annotation_metadata.csv |
| linked | text | 40.4 | csv/micro_storyboard_asset_plan.csv |
| linked | text | 639.7 | csv/micro_storyboard_pure_image_prompts.csv |
| linked | text | 1.1 | csv/normal_shooting_delta_asset_plan.csv |
| linked | text | 81.1 | csv/panel_stage_state_map.csv |
| linked | text | 1.1 | csv/pipeline_state_validation.csv |

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
