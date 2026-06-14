# Skill Pack Changelog

## v1.1.0 - 2026-05-28

- 新增通用 `CAMERA_SUBJECT_CONTINUITY_RULES.md`。
- 要求所有含人物分镜先定义 `camera_subject_relation`、`character_facing`、`gaze_target` 和 `camera_motivation`。
- 明确禁止把人设图/摆拍逻辑带进分镜图；进入、跟拍、逃跑、追逐、发现目标等镜头默认使用背面、三分之二背面、侧面或过肩关系，只有明确 reaction cut 才允许正脸。
- 新增 QA 失败类型：`wrong_camera_subject_relation`、`staged_character_sheet_logic`、`gaze_breaks_story_logic`、`movement_direction_broken`。

## v1.0.0 - 2026-05-22

- 初始化 `1主3子` Skill 结构：
  - `story-video-director-orchestrator`
  - `whitebox-qa-gate`
  - `character-stage-continuity-qa`
  - `music-edit-render-qa`
- 建立统一接口最小集：
  - 输入：`project_manifest + frame_continuity_manifest + story_section_map`
  - 输出：`asset_integrity_report + delivery_report + next_actions`
- 建立新项目使用手册与统一迭代治理手册。
