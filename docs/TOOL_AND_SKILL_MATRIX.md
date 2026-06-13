# Tool And Skill Matrix

本文档把当前愿景拆成可运行工具、Skill 和项目产物。`projects/coin-slot/` 是样板项目。

| Workflow stage | GUI surface | Script / tool | Skill | Primary artifact |
| --- | --- | --- | --- | --- |
| 新建项目 | Pipeline Hub 新建项目表单 | `scripts/create_aigc_project.py` | `$aigc-film-pipeline` | `projects/<slug>/project.yaml` |
| 导入旧项目资源 | Pipeline Hub 链接资源表单 | `POST /api/projects/<slug>/links` | `$aigc-film-pipeline` | `assets_link_map.md` |
| 投币口样板种子 | CLI / sample setup | `scripts/seed_coin_slot_sample_project.py` | `$aigc-film-pipeline` | 12-shot sample batch |
| 结构检查 | Pipeline Hub 验证按钮 | `scripts/validate_aigc_project.py` | `$aigc-film-pipeline` | API validation JSON |
| 全流程资产分析 | Pipeline Hub 分析按钮 | `scripts/analyze_aigc_project.py` | `$aigc-film-project-auditor` | `10_qa/reports/project_audit_latest.md` |
| 导演级审美建议 | 报告面板 + Skill | 人工/AI 读取分析报告和抽样资产 | `$aigc-film-project-auditor` | `10_qa/reports/director_aesthetic_review_latest.md` |
| 阶段状态 | Pipeline Hub 阶段面板 | `analyze_stages()` | `$aigc-film-pipeline` | stage weak/missing lists |
| 镜头生产准备 | Pipeline Hub 镜头表 | `07_shots/shot_list.csv` | `$aigc-film-pipeline` | shot-level task table |
| 白模/空间 QA | 后续专用面板 | `scripts/visual/qa_whitebox_images.py`, `qa_whitebox_similarity.py` | `$aigc-film-pipeline` | `06_previs/qa/` |
| 分镜/音频/交付验证 | 后续专用面板 | `scripts/visual/build_*`, `validate_final_delivery.py` | `$aigc-film-pipeline` | `11_delivery/` |

## Current Completion

- 可运行本地 GUI: `apps/pipeline-hub/server.py`
- 可创建新标准项目: done
- 可链接旧项目和 LFS 资源目录: done
- 可验证标准项目结构: done
- 可分析项目资产、抽样大资源、输出缺失项和审美风险: done
- 可读取投币口样板并展示阶段/镜头/报告: done
- 投币口 12 镜头标准样板批次: done

## Next Expansion

后续每个阶段可以继续拆出专用面板：

- Intake Analyzer: 读取导演输入、截图、视频，生成初步分析。
- Direction Board: 比较 2 到 4 个故事/美术方向，并记录导演确认。
- Asset Bible Manager: 管理角色、场景、道具、色彩、灯光和连续性锁。
- Previs Builder: 管理 Blender 白模、机位、控制层和白模 QA。
- Shot Factory: 批量生成关键帧、图片提示词、视频提示词和失败复盘。
- QA Console: 汇总审美、空间、角色一致性、声音、剪辑和交付风险。
