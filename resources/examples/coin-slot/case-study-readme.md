# 投币口

中式梦核 / 90年代小城 / 街机异化短片项目。

本项目采用 AIGC 优先工作流：先用 Blender 白模锁空间和机位，再生成关键帧，最后进入图生视频。正常拍摄版作为同一故事的传统制作翻译。

## 目录

```text
投币口/
  01_AIGC/
  02_Normal_Shooting/
```

## 01_AIGC

- `00_project_rules.md`：项目规则、AIGC 生成原则、主体和空间锁定
- `01_visual_continuity_bible.md`：色彩、角色、混混、空间轴线、转场规则
- `02_scene_reference_prompts.md`：老小区、游戏机房、偏僻小路、废楼、电话亭、8-bit 等主场景参考图提示词
- `03_aigc_storyboard.md`：20 条 AIGC 叙事镜头表
- `04_video_prompts.md`：基础视频提示词包
- `05_negative_constraints.md`：全局和分段负面约束
- `06_keyframe_prompts.md`：角色表、环境图和 12 张关键帧提示词
- `07_generation_run_plan.md`：推荐生成顺序、通过标准、返工规则
- `08_shot_asset_map.md`：镜头、白模、关键帧、视频提示词对应表
- `09_image_asset_manifest.md`：角色、场景、关键帧和联系表资产清单
- `10_morning_review_index.md`：明早检查索引
- `11_aigc_director_workflow.md`：AIGC 视频导演工作流
- `12_motion_control_table.md`：20 镜运动控制表
- `13_generation_units.md`：实际图生视频生成单元
- `14_structured_video_prompts.md`：结构化视频提示词
- `15_aigc_preflight_checklist.md`：生成前检查表
- `16_character_design_bible_v2.md`：人物小传、外形、表情、姿态、记忆点返工圣经
- `17_character_sheet_generation_prompts_v2.md`：32 张新版人物设定图生成提示词
- `18_micro_storyboard_rules_v4.md`：5-6 分钟超细分镜规则和 188 张 panel 分配
- `19_micro_storyboard_188_panels.csv`：MSB001-MSB188 微分镜生产表
- `20_micro_storyboard_generation_batches.md`：188 张微分镜分批生成计划
- `21_asset_expansion_plan_v2.md`：几百张图级别的资产扩展计划
- `22_micro_storyboard_prompt_pack.md`：188 张微分镜图像提示词使用说明
- `23_dialogue_voice_sound_music_plan.md`：对白、语音、音效、环境声和音乐模块
- `24_wav_generation_and_audio_assembly_plan.md`：WAV 生成与整轨装配计划
- `25_visual_asset_dual_version_rules.md`：纯画面母版和标注工作版双版本规则
- `26_spatial_consistency_bible_v1.md`：空间一致性和跑偏修正机制
- `27_whitebox_expansion_plan_v2.md`：白模扩展计划和判定规则
- `28_whitebox_qa_protocol_v1.md`：白模 QA 协议和进入 pure 图生成的门禁
- `35_full_pipeline_operating_manual_v1.md`：从恢复、故事、白模、pure 图、音频、视频到续跑的全流程总控
- `36_runtime_resilience_and_keepawake_v1.md`：heartbeat、watchdog、黑屏/屏保防睡眠和续跑边界

## Blender 白模

- `01_AIGC/blender/coin_slot_whitebox.blend`：Blender 白模工程
- `01_AIGC/blender/coin_slot_whitebox.py`：白模生成脚本
- `01_AIGC/blender/camera_manifest.csv`：机位清单
- `01_AIGC/whitebox_renders/`：21 张 Blender 1280x720 白模机位图
- `01_AIGC/whitebox_renders/contact_sheet.png`：机位联系表
- `01_AIGC/character_refs/`：角色设定图
- `01_AIGC/scene_refs/`：场景参考图
- `01_AIGC/keyframes/`：KF01-KF12 关键帧图
- `01_AIGC/storyboard_panels/`：SB01-SB20 分镜视觉板
- `01_AIGC/contact_sheets/`：人设、场景、关键帧、20 镜分镜、白模联系表
- `01_AIGC/34_final_storyboard_audio_video_delivery_v002.md`：最终分镜音视频交付索引、QA 和后续 pure 图生成说明
- `01_AIGC/final_storyboard_panels/`：188 张最终审片分镜面板
- `01_AIGC/final_storyboard_contact_sheets/`：188 张最终分镜的分批联系表
- `01_AIGC/audio/mix/coin_slot_audio_clean_v002.wav`：低噪音频 guide
- `01_AIGC/exports/final_video/coin_slot_final_storyboard_video_v002.mp4`：5:51 最终节奏分镜视频
- `01_AIGC/exports/final_storyboard/`：最终分镜面板清单和 QA
- `01_AIGC/character_design_v2/`：新版人物单人、三视图、表情、姿态和关系图计划输出目录
- `01_AIGC/micro_storyboard_panels/`：MSB001-MSB188 微分镜计划输出目录
- `01_AIGC/micro_storyboard_contact_sheets/`：微分镜批次联系表计划输出目录
- `01_AIGC/micro_keyframes_v2/`：新版精修关键帧计划输出目录
- `01_AIGC/whitebox_renders_v2/`：补充白模机位计划输出目录
- `01_AIGC/audio/`：语音、环境声、音效、音乐和整轨 mix 计划输出目录

## 01_AIGC / Audio Exports

- `exports/dialogue_voice_decision_table.csv`：按剧情和分镜判断哪里需要台词、旁白、系统声或沉默
- `exports/dialogue_voice_assets.csv`：台词、系统声、人群声和语音 WAV 资产表
- `exports/sound_music_cue_sheet.csv`：音效、环境声、foley、转场声、音乐 cue sheet
- `exports/audio_assembly_manifest.csv`：将语音、音效、环境声、音乐装配成 guide WAV 的时间表
- `exports/micro_storyboard_pure_image_prompts.csv`：188 张纯画面母版提示词，不含任何文字标注
- `exports/micro_storyboard_annotation_metadata.csv`：188 张标注工作版后处理元数据
- `exports/visual_asset_dual_version_plan.csv`：人物和微分镜的 pure/annotated 双版本路径表
- `exports/whitebox_expansion_plan.csv`：188 张微分镜的白模需求判定
- `exports/whitebox_qa_checklist.csv`：required 白模逐张 QA 清单
- `exports/whitebox_issue_log.csv`：白模问题和返工记录
- `exports/normal_shooting_delta_asset_plan.csv`：实拍版差异补充参考图计划
- `exports/pipeline_state_validation.csv`：全流程状态校验脚本输出

## 02_Normal_Shooting

- `00_director_proposal.md`：导演提案
- `01_story_outline.md`：故事大纲
- `02_visual_bible.md`：正常拍摄版视觉圣经
- `03_shooting_storyboard.md`：正常拍摄分镜
- `04_production_notes.md`：制作备注

## scripts

- `scripts/validate_pipeline_state.py`：检查项目当前是否满足继续 pure 图生产的状态门禁
- `scripts/keep-codex-awake.ps1`：运行期间阻止 Windows 自动睡眠，默认允许显示器关闭

## 推荐下一步

先运行全流程校验，再继续 pure photoreal 微分镜图生产：

1. 运行 `python scripts/validate_pipeline_state.py "E:\视觉\投币口"`。
2. 从 `exports/real_image_generation_queue.csv` 读取下一条 `queued`。
3. 用 `exports/micro_storyboard_pure_image_prompts.csv` 的同 panel 提示词和 `whitebox_reference_path` 生成 pure 图。
4. pure 图通过 QA 后，再生成 annotated 工作版。
5. 每完成有意义批次，重建 final storyboard panels、contact sheets、final video 和 validation。
6. 从通过的 pure 图里选出关键帧、start frame 和 end frame，再回到 `13_generation_units.md` 做视频测试。

当前重要判断：旧 20 镜是 macro storyboard，不再视为足够的生产分镜。
