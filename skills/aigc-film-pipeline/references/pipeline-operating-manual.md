# 投币口 / 全流程生产总控手册 v1

本文件是项目的总入口。目的不是替代已有文档，而是给每次恢复、检查、继续生产时一个稳定判断顺序。

## 当前生产结论

当前项目已经不是 20 镜概念分镜阶段。当前状态是：

- 故事、角色 v2、阶段锁、声音设计、白模 v2、188 面板 review animatic 已建立。
- 188 张 panel-level 白模已通过自动 QA。
- 最终节奏分镜视频 v002 已通过本地校验。
- 真正未完成的是 pure photoreal 微分镜图逐张替换：当前队列以 `exports/real_image_generation_queue.csv` 为准。

## 总流程

| 阶段 | 目标 | 主文件 | 门禁 |
|---:|---|---|---|
| 0 | 恢复上下文 | `TASK_LOG.md` | 必须先读，不从聊天记忆恢复 |
| 1 | 故事和阶段锁 | `31_story_stage_continuity_rules.md` / `exports/panel_stage_state_map.csv` | 188 panels 都有 stage/state |
| 2 | 人物设计 | `16_character_design_bible_v2.md` / `32_character_similarity_qa_protocol.md` | 角色可通过缩略图区分 |
| 3 | 空间白模 | `26_spatial_consistency_bible_v1.md` / `29_whitebox_scale_and_blocking_bible_v1.md` | 188 白模存在且 QA pass |
| 4 | 微分镜生产表 | `19_micro_storyboard_188_panels.csv` | 188 rows，clip 分布正确 |
| 5 | pure 图生成 | `exports/real_image_generation_queue.csv` / `exports/micro_storyboard_pure_image_prompts.csv` | 每张图 pure 通过后才生成 annotated |
| 6 | annotated 工作图 | `tools/annotate_visual_asset.py` | 不污染 pure 图 |
| 7 | 分镜视频重建 | `tools/build_final_storyboard_panels.py` / `tools/build_final_storyboard_video.py` | validation failed=0 |
| 8 | 音频和节奏 | `23_dialogue_voice_sound_music_plan.md` / `24_wav_generation_and_audio_assembly_plan.md` | 音频时长与 188 panel timing 对齐 |
| 9 | 最终包 | `34_final_storyboard_audio_video_delivery_v002.md` | package、video、audio、manifest 都存在 |
| 10 | 续跑运行层 | heartbeat / watchdog / keep-awake | Codex 活着、网络可恢复、Windows 不睡眠 |

## 每次恢复后的固定动作

1. 读取 `TASK_LOG.md`。
2. 运行：

```powershell
python "E:\视觉\投币口\scripts\validate_pipeline_state.py" "E:\视觉\投币口"
```

3. 如果 validation 通过，读取 `exports/real_image_generation_queue.csv` 的下一条 `queued`。
4. 按同 panel 的 `pure_prompt`、`negative_prompt`、`whitebox_reference_path` 生成 pure 图。
5. 保存到 `pure_path`，再运行/更新 QA。
6. pure 图通过后生成 annotated copy。
7. 重建 final storyboard panels、contact sheets、final video 和 validation。
8. 更新 `TASK_LOG.md`。

## 关键规则

- 不允许跳过 whitebox 直接生成 pure 图。
- 不允许把 annotated 图喂给图生视频或图像生成模型。
- 不允许用旧 20 镜替代 188 panel 生产表。
- 不允许用已有 review animatic 冒充最终 pure photoreal 全替换版本。
- 不允许在角色尚未通过相似性 QA 时批量推进后续人物图。
- 每次只推进小批量 pure 图，优先 A 级和阶段转场。

## 当前最高优先级

继续 pure photoreal 微分镜图生产：

1. 从 `real_image_generation_queue.csv` 找下一条 `queued`。
2. 优先 A 级 panel，其次 stage transition 和 conflict/phone/8-bit 节点。
3. 每完成一张就更新队列、QA、dual-version plan。
4. 每完成有意义批次就重建 review video。

## 何时可以进入视频生成单元

只有满足以下条件才进入 `13_generation_units.md`：

- A 级 pure 图基本完成。
- start/end/keyframe 候选足够覆盖每个生成单元。
- 角色身份、空间、阶段状态在 contact sheet 中稳定。
- final storyboard validation 仍为 failed=0。

否则继续做 pure 图和 QA，不提前跑视频。

