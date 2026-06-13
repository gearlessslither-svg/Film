# NEW PROJECT COPY PACK v1

这个包的目的：让你开新项目时，不再从零搭流程，直接继承当前 `1主3子 skill` 的沉淀。

---

## 1) 你要拷贝什么

把本目录下两部分复制到你的新项目：

- `configs/` -> 新项目 `configs/`
- `docs/` -> 新项目 `docs/`（或 `process_docs/`）

---

## 2) 最小必需文件（先保证这 5 个）

在 `configs/` 中，至少要有：

1. `project_manifest.json`
2. `frame_continuity_manifest.json`
3. `story_section_map.json`
4. `edit_render_plan.json`
5. `asset_integrity_report.json`

有了这 5 个，主 Skill 就能开始编排。

---

## 3) 推荐增强文件（建议一并带上）

- `blender_whitebox_spec.json`
- `whitebox_panellevel_qa_checklist.csv`
- `story_stage_state_map.csv`
- `character_similarity_qa.csv`
- `visual_asset_dual_version_plan.csv`
- `video_continuity_handles_manifest.json`
- `micro_storyboard_panel_plan.csv`
- `shot_asset_map.csv`
- `audio_assembly_manifest.csv`
- `animatic_panel_timing.csv`

---

## 4) 新项目启动顺序（固定）

1. 先调用 `story-video-director-orchestrator`
2. 主 Skill 按顺序触发：
   - `whitebox-qa-gate`
   - `character-stage-continuity-qa`
   - `music-edit-render-qa`
3. 任一门禁失败：先执行 `next_actions.md` 回退，再重跑
4. 三个门禁通过后，再做批量渲染与交付

---

## 5) 统一迭代纪律（非常关键）

不要在项目里私自演化流程规则。
所有“跨项目可复用”的改进，必须按下面文档回写 Skill Pack：

- `docs/SKILL_ITERATION_GOVERNANCE.md`
- `docs/SKILL_ITERATION_PROPOSAL.md`

---

## 6) 参考文档

- `docs/NEW_PROJECT_MANUAL.md`
- `docs/SKILL_PACK_README.md`
- `docs/CAMERA_SUBJECT_CONTINUITY_RULES.md`
- `docs/SKILL_CHANGELOG.md`
