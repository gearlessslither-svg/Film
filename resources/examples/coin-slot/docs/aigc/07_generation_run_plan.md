# 投币口 / 01_AIGC 生成执行计划 v4

目标：在风格验证通过后，先锁人设和环境，再按生成单元测试视频运动。不要直接跑完整 20 镜，也不要直接跑长镜头。

## 核心原则

- AIGC 视频不是拍摄现实，而是约束模型推测现实。
- 每个生成单元必须明确：主体、运动方向、镜头运动、首帧、尾帧、不变元素和禁止项。
- 叙事顺序看 `03_aigc_storyboard.md`。
- 运动控制看 `12_motion_control_table.md`。
- 实际生成顺序看 `13_generation_units.md`。
- 实际提示词优先用 `14_structured_video_prompts.md`。
- 生成前用 `15_aigc_preflight_checklist.md` 检查。
- 人物返工先看 `16_character_design_bible_v2.md` 和 `17_character_sheet_generation_prompts_v2.md`。
- 微分镜生产先看 `18_micro_storyboard_rules_v4.md`、`19_micro_storyboard_188_panels.csv`、`20_micro_storyboard_generation_batches.md`。
- 资产扩展计划看 `21_asset_expansion_plan_v2.md`。
- 对白、语音、音效、音乐和整轨 WAV 看 `23_dialogue_voice_sound_music_plan.md`、`24_wav_generation_and_audio_assembly_plan.md`。
- 纯图/标注双版本看 `25_visual_asset_dual_version_rules.md`。
- 空间一致性和白模扩展看 `26_spatial_consistency_bible_v1.md`、`27_whitebox_expansion_plan_v2.md`、`29_whitebox_scale_and_blocking_bible_v1.md`、`30_whitebox_panellevel_qa_result_v1.md`、`exports/whitebox_expansion_plan.csv`。

## 第零轮：人物设计返工

优先生成并保存：

| 优先级 | 资产 | 文件参考 | 验证目标 |
|---:|---|---|---|
| 1 | 七个角色单人正面设定 | `17_character_sheet_generation_prompts_v2.md` | 每个人盖住名字后仍能认出 |
| 2 | 七个角色三视图 | `17_character_sheet_generation_prompts_v2.md` | 同一角色正侧背不漂移 |
| 3 | 七个角色表情九宫格 | `17_character_sheet_generation_prompts_v2.md` | 表情不是同一种皱眉强弱变化 |
| 4 | 七个角色姿态四连 | `17_character_sheet_generation_prompts_v2.md` | 角色性格能从站姿和动作看出 |
| 5 | 三兄弟/混混/小路对峙/8-bit 转换关系图 | `17_character_sheet_generation_prompts_v2.md` | 关系、轮廓、色块转换稳定 |

通过标准：

- 三兄弟不只靠身高区别，脸、体态、表情、动作都不同。
- 混混四人不是一群无差别坏孩子。
- 小川必须是“恐惧中失手”，不能像主动复仇。
- 彬子必须是“受辱后报复”，不能像成年黑帮。

## 第一轮：环境和关键故事锚点

再生成或返工：

| 优先级 | 资产 | 文件参考 | 验证目标 |
|---:|---|---|---|
| 1 | KF01 老旧小区偏僻角落 | `06_keyframe_prompts.md` / `18_micro_storyboard_rules_v4.md` | 游戏机房藏在老旧小区一楼偏角 |
| 2 | KF05 偏僻小路堵截 | `06_keyframe_prompts.md` / `19_micro_storyboard_188_panels.csv` | 小路足够偏僻，适合拦路和逃跑 |
| 3 | KF04 街霸对战胜利 | `06_keyframe_prompts.md` / `19_micro_storyboard_188_panels.csv` | 冲突动机是哥哥打赢街霸，小矮个老大丢脸 |
| 4 | 电话亭和废楼 | `02_scene_reference_prompts.md` / `19_micro_storyboard_188_panels.csv` | 电话亭像现实错误物，不像科幻设备 |
| 5 | 8-bit 横版空间 | `02_scene_reference_prompts.md` / `19_micro_storyboard_188_panels.csv` | 保留废楼、电话亭、小川服装色块 |

通过标准：

- 老旧小区和偏僻小路能自然连接到逃跑、废楼。
- 石块是路边现实道具，不是刻意武器。

## 第二轮：白模扩展

先看 `exports/whitebox_expansion_plan.csv`。当前 188 张 MSB panel 全部 `whitebox_required=yes`，必须先有 `whitebox_renders_v2/` 对应白模并通过 QA，再生成 pure 图。

优先顺序：

1. B04 / MSB086-MSB119：围殴、石块、逃跑，最高风险。
2. B05 / MSB120-MSB154：废楼、走廊、电话亭，空间轴线必须稳定。
3. B02 / MSB029-MSB057：街霸机、对战、彬子和四人组聚拢。
4. B03 / MSB058-MSB085：门口离开、小路进入、堵路对峙。
5. B06 / MSB155-MSB188：听筒、电子化、8-bit 横版。
6. B01 / MSB001-MSB028：小区入口和游戏厅入口。

## 第三轮：188 张微分镜 pure/annotated 生成

按 `20_micro_storyboard_generation_batches.md` 分批，不要一次性全跑。每张图生成两个版本：

- pure：`visual_assets/pure/...`，不含任何文字或标注，只给 AIGC 和画质评估。
- annotated：`visual_assets/annotated/...`，由 pure 图后处理叠加标注，只给人类审片。

1. B01 / MSB001-MSB028：老小区到游戏厅入口。
2. B02 / MSB029-MSB057：街霸对战到老大记仇。
3. B03 / MSB058-MSB085：离开到堵路。
4. B05 / MSB120-MSB154：废楼、走廊、电话亭。
5. B04 / MSB086-MSB119：围殴、石块、逃跑。
6. B06 / MSB155-MSB188：电子化和 8-bit 结尾。

每批生成完先做 pure contact sheet，确认人物、空间、动作路径再进入下一批。annotated 版不用于评价画质。

## 第四轮：关键帧和首尾帧精修

从 `19_micro_storyboard_188_panels.csv` 中筛选：

- `asset_type=keyframe`：精修为 `micro_keyframes_v2/`。
- `asset_type=start_frame`：用于视频生成首帧。
- `asset_type=end_frame`：用于视频生成尾帧。
- 高风险段 MSB086-MSB119 必须增加中间帧。

## 第五轮：声音资产设计与 guide WAV

声音不写进分镜图 prompt，单独做：

1. 用 `exports/dialogue_voice_decision_table.csv` 判断每个段落是否需要台词、旁白、系统声或设计沉默。
2. 用 `exports/dialogue_voice_assets.csv` 生成台词、系统声和人群声 WAV。
3. 用 `exports/sound_music_cue_sheet.csv` 生成环境声、foley、硬音效、转场声和音乐 WAV。
4. 用 `exports/audio_assembly_manifest.csv` 装配 `audio/mix/coin_slot_audio_guide_v001.wav`。
5. 等 AIGC 视频片段真实时长确定后，再微调输出最终 mix。

## 第六轮：按生成单元测试视频

先低成本测试运动，不追求最终画质。按风险从低到高生成：

1. U01-U04：老旧小区到游戏厅入口，动作简单，先锁三兄弟关系。
2. U08-U09：偏僻小路和堵路，动作少但关系重要。
3. U15-U17：电话亭段，动作少，最适合测连续性。
4. U05-U07：街霸胜利和离开，测试游戏厅内人群和机器。
5. U13-U14：废楼走廊，测试追逐和空间拉长。
6. U19-U20C：8-bit 段，测试像素规则。
7. U10A-U12B：围殴、石块失手和逃跑，最后做，因为动作最容易跑偏。
8. U18A-U18B：电子化转场单独做。

## 测试变量规则

- 第一次测试用短秒数和低成本设置，只看动作、镜头、空间和身份。
- 一次只改一个变量：prompt、关键帧、时长、seed、motion strength 或模型。
- 先保运动，再保画质：动作正确 > 空间稳定 > 人物不变 > 节奏舒服 > 画质提升。
- 如果运动路径错，优先改关键帧或拆短生成单元，不要只改 prompt。
- 高风险动作必须使用隐藏剪辑：人影遮挡、黑墙擦镜、CRT 闪白、电话线 match cut、像素 UI 停顿。

## 单镜头检查

- Start Frame 是否接上上一镜。
- End Frame 是否能接下一镜。
- 运动方向是否明确，主体和镜头运动是否冲突。
- 前景/中景/背景是否稳定。
- 是否需要中间帧。
- 三兄弟和混混四人组身份是否稳定。
- 场景是否继承白模机位。
- 是否只发生了提示词允许的动作。
- 是否出现了现代物件、女生、血腥、英雄化暴力。
- 是否有隐藏剪辑方案。

## 返工规则

- 人物漂移：先回到人设图，不改剧情动作。
- 空间漂移：回到 Blender 白模图，缩短镜头动作。
- 暴力过强：减少动作数量，强调慌乱、失控、声音抽空。
- 小路不成立：强化老小区背后、围墙、杂草、碎砖石、旧路灯。
- 8-bit过现代：限制为 low-resolution 8-bit side-scrolling beat-em-up, 1990s arcade, limited color palette。
