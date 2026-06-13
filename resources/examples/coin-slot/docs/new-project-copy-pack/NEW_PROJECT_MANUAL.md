# StoryBoard 新项目使用手册（1主3子 Skill）

适用对象：内部制作团队（剧情向短片 / 音乐向 MV / AIGC 分镜项目）。
目标：新项目启动后，按同一套方法在 7 天内产出首轮可评审版本，并保持可持续迭代。

---

## 1. 你会用到什么

### Skill 组合

- 主 Skill：`story-video-director-orchestrator`
- 子 Skill：`whitebox-qa-gate`
- 子 Skill：`character-stage-continuity-qa`
- 子 Skill：`music-edit-render-qa`

### 统一输入（最小集）

- `project_manifest.json`
- `frame_continuity_manifest.json`
- `story_section_map.json`

### 统一输出（最小集）

- `asset_integrity_report.json`
- `delivery_report.md`
- `next_actions.md`

---

## 2. 新项目初始化（Day0）

### Step A：建目录

按 `F:\StoryBoard\Universal_Workflow\templates\project_structure.md` 建项目目录。

### Step B：拷贝模板

至少复制这些模板到新项目 `configs/`：

- `project_manifest.json`
- `frame_continuity_manifest.json`
- `story_section_map.json`
- `edit_render_plan.json`
- `asset_integrity_report.json`（可先空壳，后续回填）

建议同时复制（增强）：

- `story_stage_state_map.csv`
- `whitebox_panellevel_qa_checklist.csv`
- `character_similarity_qa.csv`
- `visual_asset_dual_version_plan.csv`

---

## 3. 运行顺序（固定，不要改）

## 3.1 主编排入口

先调用：`story-video-director-orchestrator`。

主 Skill 必须按以下顺序触发子门禁：

1. `whitebox-qa-gate`
2. `character-stage-continuity-qa`
3. `music-edit-render-qa`

## 3.2 门禁规则

- 任一子门禁失败：禁止晋升 story 层，必须先执行 `next_actions.md` 回退。
- 三个子门禁全部通过：才允许进入批量渲染与交付。

---

## 4. 每日执行节奏（Day1-Day7）

### Day1：故事与阶段锁

- 完成 story stage 划分与角色阶段状态映射。
- 为每个含人物 panel 指定镜头-主体关系：`rear_follow`、`over_shoulder`、`pov_or_subjective`、`profile_cross`、`reaction_cut`、`confrontation` 或 `insert_detail`。
- 对所有“进入、靠近、逃跑、追逐、发现目标”的镜头，先锁定角色朝向、视线目标和镜头动机，禁止默认正脸看镜头。
- 输出可审阅版 `frame_continuity_manifest.json` 初稿。

### Day2：白模与机位 QA

- 产出白模和机位清单。
- 跑 `whitebox-qa-gate`，拿到 blocked/approved camera 集合。

### Day3：角色阶段与相似度 QA

- 跑 `character-stage-continuity-qa`。
- 把相似度失败资产降级，不得进入正式锚点。

### Day4：资产完整性与分层

- 更新 `asset_integrity_report.json`。
- 严格分层：`story / reference_only / placeholder / whitebox_proxy_only`。

### Day5：节奏映射与渲染计划

- 跑 `music-edit-render-qa`。
- 固化 section map + frame profile + edit render plan。

### Day6-Day7：渲染交付与回退闭环

- 输出首轮交付：视频 / contact sheet / delivery report。
- 未通过项全部写入 `next_actions.md` 并关联证据路径。

---

## 5. 团队使用约束（必须遵守）

1. **不允许项目内私自改规则**：项目里只能写“项目参数”，不能写“新流程定义”。
2. **所有流程升级必须回写 Skill Pack**：见 `SKILL_ITERATION_GOVERNANCE.md`。
3. **不允许跳过门禁**：任何“先出片再补 QA”都视为违规执行。
4. **所有通过/失败必须可追溯**：报告里必须有证据路径。
5. **不允许人设图逻辑污染分镜**：分镜中角色朝向必须服从镜头动机和行动方向，详见 `CAMERA_SUBJECT_CONTINUITY_RULES.md`。

---

## 6. 快速调用口令（给团队）

可直接在协作里用下面这类指令：

- “用 `story-video-director-orchestrator` 初始化这个新项目，按 1主3子跑首轮门禁。”
- “只重跑 `whitebox-qa-gate`，并更新 `next_actions.md`。”
- “按 `music-edit-render-qa` 重建 section map 与渲染计划。”
- “把本轮失败点按治理手册转成统一迭代提案，不在项目目录里扩展流程。”

---

## 7. 你什么时候算“跑通了”

满足以下全部条件才算跑通：

- 最小输入集完整且可读。
- 三个子门禁状态清晰（通过/失败/需人工复核）。
- 失败项已写入 `next_actions.md`，并有具体回退动作。
- 首轮交付物存在，且 `delivery_report.md` 可用于下一轮决策。
