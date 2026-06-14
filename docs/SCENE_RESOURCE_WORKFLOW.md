# Scene Resource Workflow / 场戏资源工作流

本文档把 Pipeline Hub 的下一代信息架构定义为「按幕/场戏驱动」而不是「按文件夹驱动」。导演在工作时优先选择一场戏，然后围绕这场戏查看、标注、再创作、评估影响、生成新版本，并循环到这一场戏通过为止。

This document defines the next Pipeline Hub information architecture as scene-driven instead of folder-driven. The director first chooses a scene, then reviews, annotates, re-creates, impact-checks, generates, and iterates that scene until it passes.

## Core Opinion / 核心判断

你的方向是对的：电影项目的最小决策单位不应该是单个图片或单个 CSV，而应该是「一幕/一场戏」。资源类型和制作步骤仍然存在，但它们应该作为场戏内部的纵向生产链展示。

Your direction is right: the smallest decision unit in a film project should not be a single image or CSV. It should be an act or scene. Resource types and production steps still exist, but they should appear as a vertical production chain inside the selected scene.

## Target UX / 目标界面

1. 左侧：幕/场戏树。
   Left: act and scene tree.
2. 中间：当前场戏的步骤泳道。
   Center: stage lanes for the selected scene.
3. 右侧：选中资源详情、版本、备注、依赖关系。
   Right: selected resource detail, versions, notes, and dependencies.
4. 底部：再创作影响表、待生成队列、版本生成记录。
   Bottom: re-creation impact table, generation queue, and version run history.

## Scene First Resource View / 按场戏查看资源

选中某一场戏后，总控台必须只展示这一场戏相关资源，并按标准步骤分组：

After selecting a scene, the hub must show only resources related to that scene, grouped by the standard stages:

| Step | 中文说明 | English |
| --- | --- | --- |
| `03_story` | 剧本、节拍、对白 | Script, beats, dialogue |
| `04_lookdev` | 风格、色彩、光照、美术参考 | Lookdev, color, lighting, art refs |
| `05_asset_bible` | 角色/场景/道具/连续性锁 | Character, scene, prop, continuity locks |
| `06_previs` | 白模、机位、场景锁、空间 QA | Whitebox, camera, scene lock, spatial QA |
| `07_shots` | 镜头表、关键帧、图片/视频提示词 | Shot list, keyframes, image/video prompts |
| `08_generation` | 生成任务、输出图、输出视频、废片 | Jobs, image/video outputs, rejects |
| `09_edit` | 粗剪、声音、字幕、调色 | Rough cut, sound, subtitles, color |
| `10_qa` | 一致性、审美、修复队列 | Consistency, aesthetic review, fix queue |
| `11_delivery` | 当前场戏交付物 | Scene-level deliverables |

每一步都需要支持筛选、✅/× 标注、备注、再创作入口。

Every step needs filters, use/reject marks, notes, and a re-creation entry point.

场戏工作台的筛选应至少包含四类：步骤、资源类别、标注状态、关键词。资源类别不要求所有项目手写，可由 `asset_id`、`role`、`path` 和步骤推断，例如剧本、分镜提示词、白模、场景锁、分镜关键帧、音频、视频、文档。

The Scene Workbench should include at least four filters: step, resource kind, mark status, and keyword. Resource kind does not have to be manually authored for every project; it can be inferred from `asset_id`, `role`, `path`, and step, such as script, shot prompt, whitebox, scene lock, storyboard keyframe, audio, video, and document.

## Required Data Model / 必需数据模型

### Scene Manifest / 场戏清单

每个项目需要一个稳定清单，例如：

Each project needs a stable manifest, for example:

```yaml
schema_version: 1
project_slug: coin-slot
acts:
  - act_id: ACT01
    title: 第一幕 / Act 1
    scenes:
      - scene_id: SCN_COMPOUND
        scene_slug: scn-compound
        title: 居民楼角落 / Compound corner
        shot_ids: [MSB001, MSB003, MSB006, MSB009, MSB012]
      - scene_id: SCN_ARCADE
        scene_slug: scn-arcade
        title: 游戏厅入口 / Arcade entrance
        shot_ids: [MSB019, MSB020, MSB025]
```

建议路径 / Recommended path:

```text
projects/<slug>/00_admin/scene_manifest.yaml
```

### Scene Status / 场戏状态

场戏状态用于驱动循环，而不是替代人工判断。推荐状态：

Scene status drives the iteration loop, but never replaces human judgment. Recommended states:

| Status | 中文含义 | English |
| --- | --- | --- |
| `draft` | 初始草稿，资源尚未完整挂接 | Initial draft; assets may be incomplete |
| `in_progress` | 制作中 | In production |
| `needs_changes` | 审片后需要继续修改 | Needs another revision after review |
| `impact_ready` | 已生成影响评估表，等待确认 | Impact table is ready for confirmation |
| `generation_queued` | 已确认资产新增/修改，并写入生成队列 | Asset create/modify choices are queued |
| `generation_failed` | 生成适配器执行失败，需要检查日志或重配适配器 | Generation adapter failed; inspect logs or fix adapter config |
| `review_ready` | 本轮资产已生成，等待审片 | Ready for review |
| `approved` | 这一场戏当前版本已通过 | Current scene version is approved |

每次人工状态变更都要写入审片记录，保留当时的状态、备注、关联变更请求和时间。

Every manual status change should append a review record with status, note, linked change request, and timestamp.

建议路径 / Recommended path:

```text
projects/<slug>/10_qa/scene_reviews/<scene_id>.yaml
```

### Scene Resource Manifest / 场戏资源清单

每场戏需要一个资源清单，把所有步骤的资产挂到同一个 `scene_id` 下：

Each scene needs a resource manifest that attaches every stage asset to the same `scene_id`:

```yaml
scene_id: SCN_ARCADE
stage_assets:
  "03_story":
    - asset_id: SCN_ARCADE_STORY_BEATS
      path: 03_story/beats/...
      role: beat_sheet
  "06_previs":
    - asset_id: SCN_ARCADE_SCENE_LOCK
      path: 06_previs/scene_locks/scn-arcade/scene_lock.yaml
      role: scene_lock
  "07_shots":
    - asset_id: MSB019_IMAGE_PROMPT
      path: 07_shots/prompts/MSB019.md
      role: image_prompt
```

建议路径 / Recommended path:

```text
projects/<slug>/06_previs/scene_locks/<scene_slug>/scene_resource_manifest.yaml
```

### Resource Version Record / 资源版本记录

每次生成或修改都必须记录版本号、触发原因和来源：

Every generation or modification must record version number, trigger, and lineage:

```yaml
asset_id: MSB019_KEYFRAME
scene_id: SCN_ARCADE
stage_id: "07_shots"
version: v003
status: candidate
created_at: "2026-06-14T02:30:00+08:00"
change_request_id: CR_SCN_ARCADE_20260614_001
trigger_step: "06_previs"
trigger_asset_id: SCN_ARCADE_SCENE_LOCK
parent_version: v002
output_path: 08_generation/outputs/images/MSB019_v003.png
notes: 根据新的门帘运动方向重生成 / Regenerated from the new curtain-motion direction.
```

建议路径 / Recommended path:

```text
projects/<slug>/10_qa/version_registry/<scene_id>.yaml
```

## Re-Creation Loop / 再创作闭环

再创作不是直接点「生成」。它必须先变成一个变更请求：

Re-creation is not a direct Generate click. It first becomes a change request:

1. 选择场戏和步骤。
   Select a scene and step.
2. 写下创作方向，例如「游戏厅入口更潮湿、门帘运动更明确」。
   Write the creative direction, such as "make the arcade entrance wetter and the curtain motion clearer."
3. 系统生成影响评估表。
   The system creates an impact analysis table.
4. 用户选择哪些资产新增、哪些资产修改、哪些保持不动。
   The user chooses which assets to create, modify, check, or keep.
5. 系统生成任务队列。
   The system creates a generation queue.
6. 场戏状态自动变为 `generation_queued`。
   The scene status automatically becomes `generation_queued`.
7. 点击「开始生成任务包」后，系统为每个队列项写出可执行 brief，并把版本标为 `candidate`。
   Clicking "Start generation packet" writes an executable brief for each queued item and marks each version as `candidate`.
8. 真实图片/视频/文本/剪辑工具完成后，把最终输出路径回填到版本记录。
   After the real image, video, text, or edit tool finishes, link the final output path back into the version record.
9. 每个输出写版本号和触发来源。
   Every output records version and trigger source.
10. QA 通过后把候选版本晋级为当前版本，并将场戏标记为 `approved`。
   After QA passes, promote candidate versions to current.
11. 系统自动保存场戏快照，冻结这一轮通过时的资源清单、当前版本、候选版本、变更请求和审片尾记录。
    The system automatically saves a scene snapshot that freezes the approved resource manifest, current versions, candidate versions, change requests, and review tail.

## Scene Snapshot / 场戏快照

场戏快照是每轮 `approved` 的基线，不替代原始资产，也不覆盖版本记录。它回答一个问题：这一场戏在某次通过时，系统认定哪些资源、版本和变更请求构成了当时的完整状态。

A scene snapshot is the baseline for each `approved` iteration. It does not replace source assets or version records. It answers one question: when this scene passed review, which resources, versions, and change requests made up the accepted state?

建议路径 / Recommended path:

```text
projects/<slug>/10_qa/scene_snapshots/<scene_id>_<YYYYMMDD_HHMMSS>.yaml
```

快照应至少包含：

Each snapshot should include at least:

| Field | 中文含义 | English |
| --- | --- | --- |
| `snapshot_id` | 快照 ID | Snapshot ID |
| `scene_id` | 场戏 ID | Scene ID |
| `status` | 保存快照时的场戏状态，通常是 `approved` | Scene status when saved, usually `approved` |
| `current_versions` | 当时被采用的当前版本 | Current accepted versions |
| `candidate_versions` | 仍待判断的候选版本 | Candidate versions still under review |
| `change_requests` | 本场戏相关变更请求摘要 | Related change request summaries |
| `review_tail` | 最近审片记录 | Recent review records |
| `resource_manifest` | 当时的场戏资源清单 | Scene resource manifest at that moment |

## Generation Adapter / 生成适配层

当前内置适配器是 `manual_packet`。它不伪造图片或视频结果，而是为每个已确认队列项生成一个任务包：

The built-in adapter is `manual_packet`. It does not fake image or video outputs. It creates a handoff packet for every confirmed queue item:

```text
projects/<slug>/08_generation/jobs/<change_request_id>/outputs/<queue_id>_<asset_id>_<version>.md
```

任务包包含场戏、变更请求、触发步骤、资产、目标版本、父版本和创作方向。真实生成器可以读取这份任务包，生成结果后回填 `final_output_path`，再由人工审片决定是否晋级为 `current`。

The packet contains scene, change request, trigger step, asset, target version, parent version, and creative direction. A real generator can read the packet, produce the output, write back `final_output_path`, and then a human reviewer decides whether to promote it to `current`.

回填字段：

Output attachment fields:

| Field | 中文含义 | English |
| --- | --- | --- |
| `packet_path` | `manual_packet` 任务包路径 | Path to the `manual_packet` brief |
| `target_path` | 原计划写入或修改的资产路径 | Planned target path |
| `final_output_path` | 真实图片/视频/文本/剪辑输出路径 | Real produced output path |
| `output_exists` | 回填时文件是否已在项目内存在 | Whether the file existed in-project when attached |

### Command Adapter / 命令适配器

项目可以在下面文件中配置本地生成器：

Projects can configure local generators here:

```text
projects/<slug>/00_admin/generation_adapters.yaml
```

命令适配器默认不启用。启用前必须确认不会上传敏感素材、不会写出项目目录之外的文件：

Command adapters are disabled by default. Before enabling one, confirm that it will not upload sensitive material or write outside the project directory:

```json
{
  "adapter_id": "local_image_generator",
  "label": "Local Image Generator",
  "type": "command",
  "enabled": true,
  "requires_confirmation": false,
  "timeout_seconds": 300,
  "command": ["python3", "scripts/run_generation_adapter.py"],
  "output_path_template": "08_generation/outputs/{asset_id}_{target_version}.png"
}
```

执行时，系统会：

When executed, the system will:

1. 先写出任务包 `.md` 和任务 JSON。
   Write a `.md` packet and task JSON first.
2. 以项目根目录为工作目录运行 `command`。
   Run `command` from the project root.
3. 通过 stdin 传入任务 JSON，并设置环境变量：`PIPELINE_TASK_JSON`、`PIPELINE_TASK_PACKET`、`PIPELINE_PROJECT_ROOT`、`PIPELINE_QUEUE_ID`、`PIPELINE_ASSET_ID`、`PIPELINE_TARGET_VERSION`。
   Pass the task JSON via stdin and set the same values as environment variables.
4. 命令可以在 stdout 输出 JSON，例如：`{"final_output_path":"08_generation/outputs/MSB019_v003.png"}`。
   The command may write JSON to stdout, for example `{"final_output_path":"08_generation/outputs/MSB019_v003.png"}`.
5. 系统捕获 stdout/stderr 到 `08_generation/jobs/<change_request_id>/logs/`。
   The system captures stdout/stderr under `08_generation/jobs/<change_request_id>/logs/`.

版本状态建议：

Recommended version statuses:

| Status | 中文含义 | English |
| --- | --- | --- |
| `queued` | 已选择新增/修改，等待生成任务包 | Selected for create/modify, waiting for packet |
| `candidate` | 任务包或真实输出已准备审片 | Packet or real output is ready for review |
| `current` | 当前通过版本 | Current approved version |
| `superseded` | 已被新 current 版本替代 | Replaced by a newer current version |

## Impact Analysis Table / 影响评估表

当任一步骤改动后，系统必须列出可能受影响资产：

When any step changes, the system must list possibly affected assets:

| Action | Scope | Asset | Stage | Why | Default |
| --- | --- | --- | --- | --- | --- |
| modify | direct | scene_lock.yaml | `06_previs` | 场景空间/运动方向改变 | selected |
| modify | downstream | MSB019.md | `07_shots` | 提示词引用场景锁 | selected |
| create | downstream | MSB019_v004.png | `08_generation` | 关键帧需重出图 | optional |
| modify | downstream | rough_cut timing | `09_edit` | 镜头节奏可能变化 | optional |
| check | shared | character bible | `05_asset_bible` | 角色身份未变，仅需确认 | unselected |

`Action` 是系统建议，不是最终命令。确认入队前，导演可以把每一行改成 `create`、`modify` 或 `check`；只有 `create` 和 `modify` 会进入生成队列，`check` 会留在变更请求里作为人工核对项。

`Action` is a system suggestion, not the final command. Before queue confirmation, the director can override each row to `create`, `modify`, or `check`; only `create` and `modify` enter the generation queue, while `check` remains in the change request as a human review item.

默认规则：

Default rules:

- 改故事会影响 lookdev、asset bible、previs、shots、generation、edit、QA。
- 改 lookdev 会影响场景锁、提示词、图像/视频生成、调色。
- 改角色/场景 bible 会影响所有引用该 bible 的场戏。
- 改白模/机位会影响镜头提示词、关键帧、视频提示词、剪辑。
- 改关键帧会影响视频提示词、生成输出、剪辑、QA。
- 改声音会影响剪辑节奏和交付验证。

## Version Naming / 版本命名

建议命名格式：

Recommended naming:

```text
<scene_id>_<stage_id>_<asset_role>_<asset_id>_<version>
SCN_ARCADE_07_shots_image_prompt_MSB019_v003.md
SCN_ARCADE_08_generation_keyframe_MSB019_v003.png
```

每个版本必须能回答三个问题：

Every version must answer three questions:

1. 它属于哪一幕/哪场戏？
   Which act or scene does it belong to?
2. 它属于哪个步骤？
   Which production step does it belong to?
3. 它是由哪一次、哪个步骤的改动触发的？
   Which change request and which step triggered it?

## Optimizations / 可继续优化

1. **共享资产与场戏资产分离**：角色 bible、全片色彩规则、声音母版是共享资产；镜头提示词、白模、关键帧是场戏资产。
   **Separate shared assets from scene assets**: character bible, global color rules, and sound master are shared; shot prompts, whiteboxes, and keyframes are scene assets.
2. **只生成差异，不全量重跑**：再创作默认生成 delta queue，除非用户明确选择全量重做。
   **Generate deltas, not everything**: re-creation defaults to a delta queue unless the user chooses a full rebuild.
3. **影响等级**：`direct`、`downstream`、`shared`、`delivery_only` 四级，避免表格太吵。
   **Impact levels**: `direct`, `downstream`, `shared`, `delivery_only`, so the table stays readable.
4. **版本晋级机制**：candidate -> selected -> approved -> current；被替换版本标记为 superseded，不删除。
   **Version promotion**: candidate -> selected -> approved -> current; replaced versions become superseded, not deleted.
5. **场戏快照**：每轮完成后保存 scene snapshot，便于回滚和对比。
   **Scene snapshots**: save a scene snapshot after each iteration for rollback and comparison.
6. **预算提示**：生成前估算会新增多少图、多少视频、多少人工 QA。
   **Budget preview**: estimate how many images, videos, and human QA checks the run will create.
7. **跨场景警报**：如果修改共享角色或场景 bible，提示其它受影响场戏。
   **Cross-scene alerts**: if a shared character or scene bible changes, warn about other affected scenes.

## Implementation Order / 实现顺序

1. 建立 `scene_manifest.yaml`，让项目知道有哪些幕/场戏和镜头。
   Create `scene_manifest.yaml` so the project knows its acts, scenes, and shots.
2. 后端返回 `scenes`、`scene_assets`、`resource_versions`。
   Backend returns `scenes`, `scene_assets`, and `resource_versions`.
3. 前端增加「场戏工作台」：左侧场戏树，中间步骤泳道，右侧资源详情。
   Frontend adds a Scene Workbench: scene tree, stage lanes, resource detail.
4. 增加变更请求与影响评估表。
   Add change requests and impact analysis tables.
5. 增加生成队列和版本记录。
   Add generation queues and version records.
6. 增加晋级/回滚/场戏完成状态。
   Add promotion, rollback, and scene completion status.
7. 增加 `approved` 快照，作为每轮循环的可回滚基线。
   Add `approved` snapshots as the rollback baseline for each iteration.
