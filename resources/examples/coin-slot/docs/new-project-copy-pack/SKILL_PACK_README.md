# StoryBoard Skill Pack v1

本目录是 `Universal_Workflow` 的可复用 Skill 组合实现，目标是把核心4项目沉淀统一成固定调用链。

## 先看这三份

1. [新项目使用手册](./NEW_PROJECT_MANUAL.md)
2. [统一迭代治理手册](./SKILL_ITERATION_GOVERNANCE.md)
3. [镜头-主体连续性规则](./CAMERA_SUBJECT_CONTINUITY_RULES.md)
4. [Skill 变更日志](./SKILL_CHANGELOG.md)

## 结构

- `story-video-director-orchestrator/`：主编排 Skill（1）
- `whitebox-qa-gate/`：白模与机位门禁（子 Skill）
- `character-stage-continuity-qa/`：角色阶段锁与相似度门禁（子 Skill）
- `music-edit-render-qa/`：节奏映射、渲染验收门禁（子 Skill）

## 统一接口

- 输入最小集：
  - `project_manifest.json`
  - `frame_continuity_manifest.json`
  - `story_section_map.json`
- 可选增强：
  - `blender_whitebox_spec.json`（或等价 whitebox spec）
  - `character_similarity_qa.csv`
  - `frame_profile.json`
  - `edit_render_plan.json`
- 通用分镜规则：
  - `docs/CAMERA_SUBJECT_CONTINUITY_RULES.md`
- 输出最小集：
  - `asset_integrity_report.json`
  - `delivery_report.md`
  - `next_actions.md`

## 新项目使用（最短路径）

1. 先补齐输入最小集。
2. 运行 `story-video-director-orchestrator`，由主 Skill 触发三个子门禁。
3. 任一门禁失败，先按 `next_actions` 回退修复，再重跑。
4. 三个门禁全部通过后，再进入批量渲染与交付。

## 安装方式（供后续项目直接调用）

将这四个目录复制到你的 Codex skills 目录（例如 `C:\Users\Administrator\.codex\skills\`）后，即可在新项目中直接调用：

- `story-video-director-orchestrator`
- `whitebox-qa-gate`
- `character-stage-continuity-qa`
- `music-edit-render-qa`

## 证据来源

- `F:\StoryBoard\DeathClub\CURRENT_WORKFLOW_STATUS.md`
- `F:\StoryBoard\PixelLove\configs\whitebox_workflow_policy.md`
- `F:\StoryBoard\Dream\projects\plastic_love_citypop\configs\deliverables.md`
- `F:\StoryBoard\投币口0522\投币口\01_AIGC\33_pipeline_review_and_next_project_rules.md`
