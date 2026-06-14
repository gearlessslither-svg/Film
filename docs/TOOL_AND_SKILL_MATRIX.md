# Tool And Skill Matrix / 工具与 Skill 对照表

本文档把当前愿景拆成可运行工具、Skill 和项目产物。`projects/coin-slot/` 是样板项目。
This document breaks the current vision into runnable tools, skills, and project artifacts. `projects/coin-slot/` is the sample project.

| Workflow stage / 流程阶段 | GUI surface / GUI 入口 | Script / tool / 脚本工具 | Skill | Primary artifact / 主要产物 |
| --- | --- | --- | --- | --- |
| 新建项目 / New project | Pipeline Hub 新建项目表单 / new-project form | `scripts/create_aigc_project.py` | `$aigc-film-pipeline` | `projects/<slug>/project.yaml` |
| 导入旧项目资源 / Import old assets | Pipeline Hub 链接资源表单 / link-resource form | `POST /api/projects/<slug>/links` | `$aigc-film-pipeline` | `assets_link_map.md` |
| 投币口样板种子 / Coin Slot sample seed | CLI / sample setup | `scripts/seed_coin_slot_sample_project.py` | `$aigc-film-pipeline` | 12-shot sample batch |
| 结构检查 / Structure check | Pipeline Hub 验证按钮 / validate button | `scripts/validate_aigc_project.py` | `$aigc-film-pipeline` | API validation JSON |
| 全流程资产分析 / Full asset analysis | Pipeline Hub 分析按钮 / analyze button | `scripts/analyze_aigc_project.py` | `$aigc-film-project-auditor` | `10_qa/reports/project_audit_latest.md` |
| 自治补全缺失资产 / Autofill missing assets | Pipeline Hub Autofill 按钮 / autofill button | `scripts/autofill_aigc_project.py` | `$aigc-film-pipeline` + `$aigc-film-project-auditor` | `10_qa/autofill_runs/autofill_latest.md` |
| 导演级审美建议 / Director-level review | 报告面板 + Skill / report panel + skill | 人工/AI 读取分析报告和抽样资产 / human/AI reads report + sampled assets | `$aigc-film-project-auditor` | `10_qa/reports/director_aesthetic_review_latest.md` |
| 阶段状态 / Stage status | Pipeline Hub 阶段面板 / stage panel | `analyze_stages()` | `$aigc-film-pipeline` | stage weak/missing lists |
| 镜头生产准备 / Shot production prep | Pipeline Hub 镜头表 / shot table | `07_shots/shot_list.csv` | `$aigc-film-pipeline` | shot-level task table |
| 白模/空间 QA / Whitebox & spatial QA | 后续专用面板 / dedicated panel (planned) | `scripts/visual/qa_whitebox_images.py`, `qa_whitebox_similarity.py` | `$aigc-film-pipeline` | `06_previs/qa/` |
| 分镜/音频/交付验证 / Storyboard, audio, delivery | 后续专用面板 / dedicated panel (planned) | `scripts/visual/build_*`, `validate_final_delivery.py` | `$aigc-film-pipeline` | `11_delivery/` |

## Current Completion / 当前完成度

- 可运行本地 GUI / Runnable local GUI: `apps/pipeline-hub/server.py`
- 可创建新标准项目 / Can create a new standard project: done
- 可链接旧项目和 LFS 资源目录 / Can link old projects and LFS resource dirs: done
- 可验证标准项目结构 / Can validate standard project structure: done
- 可分析项目资产、抽样大资源、输出缺失项和审美风险 / Can analyze assets, sample large resources, report gaps and aesthetic risks: done
- 可按分析缺口自动补齐安全资产，并生成 Codex/image2/Blender/plugin 适配器任务 / Can autofill safe assets from gaps and generate Codex/image2/Blender/plugin adapter tasks: done
- 可读取投币口样板并展示阶段/镜头/报告 / Can read the Coin Slot sample and show stages/shots/reports: done
- 投币口 12 镜头标准样板批次 / Coin Slot 12-shot standard sample batch: done

## Next Expansion / 后续扩展

后续每个阶段可以继续拆出专用面板 / Each stage can later split into a dedicated panel:

- Intake Analyzer: 读取导演输入、截图、视频，生成初步分析。/ Read director input, screenshots, and video to produce an initial analysis.
- Direction Board: 比较 2 到 4 个故事/美术方向，并记录导演确认。/ Compare 2–4 story/art directions and record the director's approval.
- Asset Bible Manager: 管理角色、场景、道具、色彩、灯光和连续性锁。/ Manage characters, scenes, props, color, light, and continuity locks.
- Previs Builder: 管理 Blender 白模、机位、控制层和白模 QA。/ Manage Blender whiteboxes, cameras, control layers, and whitebox QA.
- Shot Factory: 批量生成关键帧、图片提示词、视频提示词和失败复盘。/ Batch-generate keyframes, image prompts, video prompts, and failure reviews.
- QA Console: 汇总审美、空间、角色一致性、声音、剪辑和交付风险。/ Aggregate aesthetic, spatial, character-consistency, sound, edit, and delivery risks.
