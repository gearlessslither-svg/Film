# Codex / GPT Bridge - blue-water-citypop-op

这个目录用于把大任务拆成“Codex 本地执行”和“GPT 紧凑判断”。

## 本项目默认分工

Codex 做：

- 视频抽帧、切点检测、联系表、媒体信息。
- Blender 白模、相机路径、playblast、帧序列。
- 写入 `director_shooting_script.md`、`video_units.json`、`transition_edges.json`、`camera_manifest.json`、提示词和 QA。
- Pipeline Hub 回填和项目验证。

GPT 做：

- 根据 Codex 提供的小包判断参考片节奏。
- 判断一段应该是一镜到底、montage、转场、插入还是普通镜头。
- 改写组级 AIGC 视频提示词。
- 做对抗性审查：哪里不像原片，哪里会破坏连续性，哪里需要补关键帧。

## 工作方式

1. Codex 在 `packets/` 里生成 GPT 小包。
2. GPT 只基于小包回答，不直接读整个项目。
3. GPT 回复保存到 `responses/`。
4. 被采纳的结论保存到 `decisions/`。
5. Codex 把结论落到正式项目文件，并在 `10_qa/reports/` 和交接里记录。

## 当前重点

参考视频：`01_intake/references/nadia_op_reference_002.mp4`

当前要交给 GPT 分担的是：根据抽帧、切点和联系表，判断原片前 23 秒的真实镜头节奏，并给出开场 Blender 预演应该如何重做。
