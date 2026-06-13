# 投币口 / 最终分镜音视频交付 v002

生成时间：2026-05-22 晚

## 核心输出

- 最终节奏视频：`01_AIGC/exports/final_video/coin_slot_final_storyboard_video_v002.mp4`
- 静音视频：`01_AIGC/exports/final_video/coin_slot_final_storyboard_video_v002_silent.mp4`
- 低噪音频：`01_AIGC/audio/mix/coin_slot_audio_clean_v002.wav`
- 188 面板最终分镜图：`01_AIGC/final_storyboard_panels/`
- 6 张分批联系表：`01_AIGC/final_storyboard_contact_sheets/`
- 分镜面板清单：`01_AIGC/exports/final_storyboard/final_storyboard_panel_manifest_v002.csv`
- 分镜 QA：`01_AIGC/exports/final_storyboard/final_storyboard_qa_v002.csv`
- 视频时序：`01_AIGC/exports/final_video/coin_slot_final_storyboard_video_v002_timing.csv`
- 音频 clean manifest：`01_AIGC/exports/audio_clean_assembly_manifest_v002.csv`
- 音频 QA：`01_AIGC/exports/audio_clean_qa_v002.csv`

## 本轮修复

- 修复 `exports/panel_stage_state_map.csv` 乱码问题。
- 修复 `exports/micro_storyboard_pure_image_prompts.csv` 里大面积问号乱码问题。
- 重建 `exports/real_image_generation_queue.csv`，保留 188 面板生产顺序。
- 生成 188/188 可审片最终分镜面板。
- 重新合成低噪音频，降低旧版 guide 中的宽带噪声感。
- 用最终分镜面板和 clean 音频合成 5:51 的节奏视频。

## 当前真实图像状态

本轮已经产出完整可审片分镜视频，但 188 张 pure photoreal 微分镜并未全部完成：

- `REAL_DRAFT`：1 张，`MSB012_v001.png`，需按最新角色设计复审或重生。
- `WHITEBOX_QA_PASS`：187 张，使用已经通过 panel-level QA 的白模作为结构分镜占位。

因此，当前视频是“最终节奏分镜视频 / review animatic”，不是 188 张 pure photoreal 图全部替换后的最终 AIGC 视频。后续真实图生成应从已修复的 `exports/micro_storyboard_pure_image_prompts.csv` 和 `exports/real_image_generation_queue.csv` 继续。

## 音频降噪结果

旧版 guide：

- 文件：`audio/mix/coin_slot_audio_guide_v001.wav`
- 时长：351.000 秒
- peak：0.702972
- RMS：0.030399
- 8kHz 以上能量比例：0.06767602

新版 clean：

- 文件：`audio/mix/coin_slot_audio_clean_v002.wav`
- 时长：351.000 秒
- peak：0.592773
- RMS：0.010628
- 8kHz 以上能量比例：0.00000518

## 视频校验

- 文件：`exports/final_video/coin_slot_final_storyboard_video_v002.mp4`
- 时长：00:05:51.00
- 分辨率：1280x720
- 帧率：12 fps
- 视频编码：mpeg4 / mp4v
- 音频：AAC LC, 48000 Hz, stereo
- 时序行数：188
- 时序总时长：351.0 秒
- 首尾面板：MSB001 到 MSB188

## 继续 pure 图生成时的规则

1. 从 `exports/real_image_generation_queue.csv` 的 `queued` 行继续。
2. 每次生成前读取同 panel 的 `pure_prompt`、`negative_prompt`、`whitebox_reference_path`。
3. pure 图通过后再生成 annotated copy。
4. 每张图更新 `exports/visual_asset_qa_checklist.csv` 和 `exports/visual_asset_issue_log.csv`。
5. 替换 final video 时优先替换 A 级面板和阶段转场面板。
