# 投币口 / 明早检查索引

## 先看这四张联系表

0. `01_AIGC/final_storyboard_contact_sheets/B01_final_storyboard_contact_sheet_v002.jpg` 到 `B06_final_storyboard_contact_sheet_v002.jpg`
1. `01_AIGC/contact_sheets/characters_contact_sheet.png`
2. `01_AIGC/contact_sheets/scenes_contact_sheet.png`
3. `01_AIGC/contact_sheets/keyframes_contact_sheet.png`
4. `01_AIGC/contact_sheets/storyboard_20_panel_contact_sheet.png`
5. `01_AIGC/contact_sheets/whitebox_contact_sheet.png`

## 先看最终音视频

- `01_AIGC/34_final_storyboard_audio_video_delivery_v002.md`：最终交付索引和 QA。
- `01_AIGC/exports/final_video/coin_slot_final_storyboard_video_v002.mp4`：5:51 最终节奏分镜视频。
- `01_AIGC/audio/mix/coin_slot_audio_clean_v002.wav`：低噪音频 guide。
- `01_AIGC/exports/audio_clean_qa_v002.csv`：新版音频和旧版 guide 的噪声指标对比。

## 再看这些文本文件

- `01_AIGC/16_character_design_bible_v2.md`：人物小传、脸部、体态、表情、姿态和记忆点返工圣经。
- `01_AIGC/17_character_sheet_generation_prompts_v2.md`：新版人物设定图、表情图、姿态图和关系图提示词。
- `01_AIGC/18_micro_storyboard_rules_v4.md`：5-6 分钟超细分镜规则和数量目标。
- `01_AIGC/19_micro_storyboard_188_panels.csv`：MSB001-MSB188 微分镜生产表。
- `01_AIGC/20_micro_storyboard_generation_batches.md`：微分镜分批生成计划。
- `01_AIGC/21_asset_expansion_plan_v2.md`：几百张图级别的资产扩展计划。
- `01_AIGC/22_micro_storyboard_prompt_pack.md`：188 张微分镜图像提示词使用说明。
- `01_AIGC/exports/micro_storyboard_image_prompts.csv`：188 条可直接生成图像的微分镜提示词。
- `01_AIGC/23_dialogue_voice_sound_music_plan.md`：对白、语音、音效、环境声和音乐模块。
- `01_AIGC/24_wav_generation_and_audio_assembly_plan.md`：WAV 生成与整轨装配计划。
- `01_AIGC/31_story_stage_continuity_rules.md`：人物、服装、表情、环境随故事阶段变化的锁定规则。
- `01_AIGC/32_character_similarity_qa_protocol.md`：人物相似度 QA，重点避免兄弟互相长成同一张脸。
- `01_AIGC/33_pipeline_review_and_next_project_rules.md`：本项目流程复盘和下一项目基础规则。
- `01_AIGC/25_visual_asset_dual_version_rules.md`：纯画面母版和标注工作版双版本规则。
- `01_AIGC/26_spatial_consistency_bible_v1.md`：空间一致性和跑偏根因修正。
- `01_AIGC/27_whitebox_expansion_plan_v2.md`：白模扩展规则和数量目标，当前为 188/188 panel-level whitebox。
- `01_AIGC/29_whitebox_scale_and_blocking_bible_v1.md`：人物/环境比例锚点和 blocking 硬规则。
- `01_AIGC/30_whitebox_panellevel_qa_result_v1.md`：188 张白模最终自动 QA 结果。
- `01_AIGC/exports/whitebox_expansion_plan.csv`：每张 MSB 是否需要新增白模的判定表。
- `01_AIGC/exports/dialogue_voice_assets.csv`：台词和语音生成资产表。
- `01_AIGC/exports/sound_music_cue_sheet.csv`：音效、环境声、音乐 cue sheet。
- `01_AIGC/exports/audio_assembly_manifest.csv`：整轨 guide WAV 装配表。
- `01_AIGC/exports/panel_stage_state_map.csv`：188 张分镜的故事阶段、角色状态、服装状态、环境状态和白模引用。
- `01_AIGC/exports/character_stage_asset_plan.csv`：阶段人设资产计划。
- `01_AIGC/exports/character_similarity_qa.csv`：人物相似度 QA 结果。
- `01_AIGC/exports/real_image_generation_queue.csv`：188 张真实 pure 图生产队列，按优先级和故事阶段排序。
- `01_AIGC/exports/animatic/coin_slot_storyboard_animatic_v001.mp4`：188 张分镜按时间排布并合成 guide WAV 的 animatic。
- `01_AIGC/03_aigc_storyboard.md`：20 镜 AIGC 连续分镜。
- `01_AIGC/04_video_prompts.md`：基础视频提示词包。
- `01_AIGC/11_aigc_director_workflow.md`：AIGC 视频导演工作流。
- `01_AIGC/12_motion_control_table.md`：20 镜运动控制表。
- `01_AIGC/13_generation_units.md`：实际图生视频生成单元。
- `01_AIGC/14_structured_video_prompts.md`：结构化视频提示词。
- `01_AIGC/15_aigc_preflight_checklist.md`：生成前检查表。
- `01_AIGC/08_shot_asset_map.md`：镜头、白模、关键帧、视频提示词对应表。
- `01_AIGC/09_image_asset_manifest.md`：所有已生成图像资产的文件名和检查顺序。
- `01_AIGC/exports/asset_output_paths.csv`：资产路径表。
- `01_AIGC/exports/video_clip_sequence.csv`：20 镜视频生成顺序表。
- `02_Normal_Shooting/03_shooting_storyboard.md`：正常拍摄版分镜翻译。

## 当前版本故事逻辑

哥哥带主角和小弟弟进入老旧小区偏僻角落的游戏机房。哥哥在街霸机前打赢小矮个老大，三兄弟志得意满地回家。四个混混在偏僻小路堵住他们，围住哥哥，小弟弟僵住，主角在老大准备下狠手时捡起路边石块失手打中对方。主角受惊逃入废楼，听见电话铃，接起废楼深处的电话亭，世界电子化并展开成 8-bit 横版街机关卡。清场后出现 `WIN`，随后闪出 `INSERT COIN`。

## 明早判断口径

- 人设不满意：先返工 `16_character_design_bible_v2.md` 和 `17_character_sheet_generation_prompts_v2.md`，不要直接改分镜。
- 人物千人一面：检查是否缺少脸部锚点、静止记忆点、运动记忆点、表情库和姿态库。
- 分镜太粗：以 `19_micro_storyboard_188_panels.csv` 为生产分镜，旧 20 镜只作为 macro storyboard。
- 图像生成跑偏：先查 `exports/whitebox_expansion_plan.csv`，如果白模不够细，先补白模，不要只改 prompt。
- 生成图混入文字/标注：说明用了错误提示词；AIGC 喂图只能用 `exports/micro_storyboard_pure_image_prompts.csv`。
- 场景不满意：先返工场景参考，不要直接跑视频。
- 关键帧不满意：只改单帧，不改全局风格。
- 8-bit 不满意：限制为90年代横版清版街机，避免现代手游和高清卡通。
- 运动不满意：先看 `13_generation_units.md` 是否拆得够短，再改关键帧，不要只改 prompt。
- 台词不满意：先判断这句是否真的必要；必要时改语气、停顿和潜台词，不要增加解释性对白。
- 音效/音乐不满意：看 `sound_music_cue_sheet.csv` 的 story_function，不要只改“氛围词”。
