# 投币口 / 01_AIGC 对白、语音、音效与音乐模块 v1

## 核心原则

本片不需要传统旁白。语言只在关系、权力和恐惧必须被听见时出现；很多关键处应保持沉默、环境声或声音抽空。声音资产分成两条线：

- 对白/旁白/系统声：见 `exports/dialogue_voice_assets.csv`。
- 音效/环境声/音乐：见 `exports/sound_music_cue_sheet.csv`。
- 最终装配关系：见 `exports/audio_assembly_manifest.csv`。

## 对白/旁白判断表

| ID | 视觉范围 | 时间 | 是否需要语言 | 类型 | 原因 | 文字策略 |
|---|---|---|---|---|---|---|
| AUD_DEC_001 | Clip 01 / MSB001-MSB008 | 00:00-00:16 | no | silence/ambience | 开场要让空间先说话，不用旁白解释。 | 只保留潮湿小区、远处街机漏声和很低的电流感。 |
| AUD_DEC_002 | Clip 02 / MSB009-MSB018 | 00:16-00:34 | yes | dialogue | 三兄弟关系需要通过小声催促和好奇建立。 | 短句，儿童口语，不能文学化。 |
| AUD_DEC_003 | Clip 03 / MSB019-MSB028 | 00:34-00:50 | mostly no | walla/source sound | 进入游戏厅由环境声吞掉人物。 | 街机、人群、按钮声盖住零散话，不写清楚台词。 |
| AUD_DEC_004 | Clip 04 / MSB029-MSB037 | 00:50-01:06 | yes | dialogue | 阿磊和彬子第一次建立对抗。 | 挑衅短句，像小城坏孩子，不像成年人狠话。 |
| AUD_DEC_005 | Clip 05 / MSB038-MSB049 | 01:06-01:28 | minimal | walla/dialogue | 对战主要靠按钮、屏幕和呼吸推进。 | 胜利前不多说，赢后用停顿和彬子一句话埋报复。 |
| AUD_DEC_006 | Clip 06 / MSB050-MSB057 | 01:28-01:42 | yes | dialogue/silence | 老大记仇要听见声音变闷和一句压住的威胁。 | 台词少，重点是声音从热闹中抽离。 |
| AUD_DEC_007 | Clip 07 / MSB058-MSB065 | 01:42-01:56 | yes | dialogue | 离开时用轻松短句做反差。 | 阿磊装酷，小川不安，小满跟着笑。 |
| AUD_DEC_008 | Clip 08 / MSB066-MSB075 | 01:56-02:14 | minimal | dialogue/ambience | 回家路从轻松转危险，台词逐渐断掉。 | 先有一句担心，随后被环境声取代。 |
| AUD_DEC_009 | Clip 09 / MSB076-MSB085 | 02:14-02:32 | yes | dialogue | 堵路需要建立权力关系。 | 彬子说短句，阿磊试图结束冲突。 |
| AUD_DEC_010 | Clip 10 / MSB086-MSB097 | 02:32-02:56 | yes | dialogue/foley | 围殴段不靠长台词，靠推搡、呼吸、孩子断句。 | 小满只叫一声哥，小川说别打了。 |
| AUD_DEC_011 | Clip 11 / MSB098-MSB107 | 02:56-03:16 | mostly no | silence/sfx | 石块段必须声音抽空，不能用台词解释。 | 冲击不血腥，声音用闷响和停顿。 |
| AUD_DEC_012 | Clip 12 / MSB108-MSB119 | 03:16-03:36 | minimal | breath/offscreen | 逃跑段台词失效，只剩呼吸和后方喊声。 | 小川只可能挤出一个“哥”。 |
| AUD_DEC_013 | Clip 13 / MSB120-MSB128 | 03:36-03:52 | no | ambience/foley | 进入废楼要让现实人声被空间吞掉。 | 脚步回声、冷绿灯管、电流。 |
| AUD_DEC_014 | Clip 14 / MSB129-MSB138 | 03:52-04:10 | no | ambience/silence | 无限走廊靠追声消失和空间回声。 | 不旁白，不解释。 |
| AUD_DEC_015 | Clip 15 / MSB139-MSB146 | 04:10-04:24 | no | system/sfx | 电话亭出现时先让铃声成为召唤。 | 电话铃有节奏，不像现代铃声。 |
| AUD_DEC_016 | Clip 16 / MSB147-MSB154 | 04:24-04:40 | yes | whisper/dialogue | 靠近电话亭可以有小川对未知对象的低声。 | 小声、短、像问空气。 |
| AUD_DEC_017 | Clip 17 / MSB155-MSB161 | 04:40-04:50 | yes | dialogue/system | 接电话后可出现一句极轻的“谁啊”，然后让线路回答。 | 线路声不要说清完整解释。 |
| AUD_DEC_018 | Clip 18 / MSB162-MSB169 | 04:50-05:08 | no | transition_sfx | 电子化用电话线、扫描线、像素块完成。 | 不说台词，避免解释。 |
| AUD_DEC_019 | Clip 19 / MSB170-MSB177 | 05:08-05:24 | no | music/sfx | 进入 8-bit 后语言转成系统音和游戏节奏。 | 不使用现代手游音色。 |
| AUD_DEC_020 | Clip 20 / MSB178-MSB188 | 05:24-05:50 | no | music/system/silence | WIN 和 INSERT COIN 用 UI、停顿和待机声完成尾针。 | 不庆祝，不旁白解释。 |

## 台词与语音资产表

| audio_id | time | speaker | type | line | subtext | delivery | wav_name |
|---|---|---|---|---|---|---|---|
| DIA_001 | 00:18.0-00:20.0 | 阿磊 | dialogue | 跟紧点，别让人看见。 | 哥哥装成熟，也带一点偷偷摸摸的兴奋。 | 压低声音，快，像怕被大人听见；尾字吞掉。 | audio/voice_clean/DIA_001_alei_genjin.wav |
| DIA_002 | 00:24.0-00:25.6 | 小川 | dialogue | 里面真能玩吗？ | 主角好奇但不敢自己决定。 | 小声，圆眼睛看哥哥，句尾上扬。 | audio/voice_clean/DIA_002_xiaochuan_nengwan.wav |
| DIA_003 | 00:28.0-00:29.2 | 阿磊 | dialogue | 看我就行。 | 哥哥把自己放在带头位置。 | 短，故作轻松，带一点得意。 | audio/voice_clean/DIA_003_alei_kanwo.wav |
| WLA_001 | 00:40.0-00:48.0 | 游戏厅人群 | walla | 快快快……别站那儿……投一个…… | 旧游戏厅的社会质感，不提供剧情信息。 | 多人含混，远近混杂，不能听清完整句子。 | audio/voice_processed/WLA_001_arcade_walla.wav |
| DIA_004 | 00:57.0-00:58.4 | 彬子 | dialogue | 会玩吗你？ | 第一次羞辱阿磊，建立对抗。 | 短促，鼻音重，下巴往前顶，像挑衅小孩。 | audio/voice_clean/DIA_004_binzi_huiwan.wav |
| DIA_005 | 01:00.0-01:01.0 | 阿磊 | dialogue | 试试呗。 | 阿磊嘴硬，想在弟弟面前撑住。 | 装轻松，句尾轻，实际有点紧。 | audio/voice_clean/DIA_005_alei_shishi.wav |
| DIA_006 | 01:25.0-01:26.2 | 彬子 | dialogue | 你等着。 | 输掉后的羞辱转成报复。 | 低声，咬牙，不喊，几乎被街机声盖住。 | audio/voice_clean/DIA_006_binzi_dengzhe.wav |
| DIA_007 | 01:44.0-01:45.2 | 阿磊 | dialogue | 看见没？ | 离开时的小胜利。 | 压着笑，肩膀一抖。 | audio/voice_clean/DIA_007_alei_kanjianmei.wav |
| DIA_008 | 01:48.0-01:49.8 | 小川 | dialogue | 哥，刚才那个黄头发…… | 小川已经注意到危险。 | 犹豫，话没说完，眼睛看哥哥。 | audio/voice_clean/DIA_008_xiaochuan_huangtoufa.wav |
| DIA_009 | 01:50.0-01:51.0 | 阿磊 | dialogue | 别理他。 | 哥哥把危险轻描淡写。 | 快，装不在乎，打断小川。 | audio/voice_clean/DIA_009_alei_bielita.wav |
| DIA_010 | 02:15.0-02:16.4 | 彬子 | dialogue | 刚才挺能啊。 | 堵路开场，羞辱回收。 | 低、慢、短，带笑但不开心。 | audio/voice_clean/DIA_010_binzi_tingneng.wav |
| DIA_011 | 02:20.0-02:21.0 | 阿磊 | dialogue | 我们回家。 | 阿磊试图用普通话语结束冲突。 | 硬撑，声音不大，尾音有虚。 | audio/voice_clean/DIA_011_alei_huijia.wav |
| DIA_012 | 02:23.0-02:24.3 | 彬子 | dialogue | 谁让你走了？ | 权力关系转向围堵。 | 下巴前顶，咬字硬，不要成年狠话。 | audio/voice_clean/DIA_012_binzi_shuirang.wav |
| DIA_013 | 02:42.0-02:42.8 | 小满 | dialogue | 哥…… | 小弟弟恐惧锚点。 | 很小，快哭但没哭，气不够。 | audio/voice_clean/DIA_013_xiaoman_ge.wav |
| DIA_014 | 02:49.0-02:50.0 | 小川 | dialogue | 别打了…… | 小川第一次试图介入，但没有力量。 | 发白的小声，像从喉咙里挤出来。 | audio/voice_clean/DIA_014_xiaochuan_biedale.wav |
| DIA_015 | 02:51.0-02:52.2 | 彬子 | dialogue | 你再说一遍？ | 把压力从哥哥压向小川。 | 突然低下来，危险但仍是坏孩子，不是成年人。 | audio/voice_clean/DIA_015_binzi_zaishuo.wav |
| SIL_001 | 03:07.0-03:11.0 | 全体 | silence | DESIGNED SILENCE | 石块失手后声音抽空。 | 没有台词；只留高频耳鸣和远处很轻的电流。 | audio/sfx/SIL_001_stone_after_drop.wav |
| DIA_016 | 03:16.5-03:17.2 | 小川 | dialogue | 哥…… | 失手后逃跑前的断裂反应。 | 气息破，几乎听不见，不要哭腔表演。 | audio/voice_clean/DIA_016_xiaochuan_ge_after.wav |
| WLA_002 | 03:19.0-03:26.0 | 后方追兵 | offscreen | 站住！……他跑了…… | 追逐压力，不能盖过小川呼吸。 | 远处、乱、含混，分不清具体是谁。 | audio/voice_processed/WLA_002_pursuers_offscreen.wav |
| DIA_017 | 04:32.0-04:33.0 | 小川 | dialogue | 喂？ | 小川对电话亭的第一声试探。 | 很轻，问空气，声音被走廊吃掉。 | audio/voice_clean/DIA_017_xiaochuan_wei.wav |
| DIA_018 | 04:45.0-04:46.0 | 小川 | dialogue | 谁啊？ | 接起电话后的本能反应。 | 低声，害怕，不要像恐怖片喊叫。 | audio/voice_clean/DIA_018_xiaochuan_shuia.wav |
| SYS_001 | 04:47.0-04:49.0 | 电话线路 | system | READY | 电话把现实接到游戏规则。 | 极轻、断续、像旧电话线里混进街机音，不要清晰机器人女声。 | audio/voice_processed/SYS_001_phone_ready.wav |

## 音效/环境声/音乐 Cue Sheet

这张表不写进分镜图 prompt，只用于声音设计、生成 WAV 和后期装配。

| cue_id | visual range | time | category | cue name | story function | sonic description | sync | intensity | wav_name |
|---|---|---|---|---|---|---|---|---:|---|
| AMB_001 | Clip 01 / MSB001-MSB008 | 00:00.0-00:16.0 | ambience | 潮湿老小区夜底 | 让空间先进入观众身体。 | 低风、远处住户声、潮湿水面、很远的街机漏音。 | free | 2 | audio/ambience/AMB_001_compound_night_loop.wav |
| SFX_001 | Clip 01 / MSB003-MSB008 | 00:08.0-00:16.0 | hard_sfx | 门内 CRT 漏电声 | 引出游戏机房。 | 很轻的 CRT 嗡鸣和蓝绿光感，不要现代电子声。 | object | 2 | audio/sfx/SFX_001_crt_leak_hum.wav |
| FOLEY_001 | Clip 02 / MSB009-MSB018 | 00:16.0-00:34.0 | foley | 三兄弟湿地脚步 | 建立年龄差和跟随节奏。 | 阿磊步子大，小川轻而紧，小满慢半拍。 | action | 2 | audio/sfx/FOLEY_001_three_brothers_steps.wav |
| SFX_002 | Clip 03 / MSB019-MSB028 | 00:34.0-00:50.0 | transition_sfx | 脏门帘擦镜 | 从小区进入游戏厅。 | 塑料门帘贴镜擦过，街机声突然变大。 | cut/transition | 3 | audio/sfx/SFX_002_plastic_curtain_wipe.wav |
| AMB_002 | Clip 03-06 / MSB019-MSB057 | 00:34.0-01:42.0 | ambience | 旧游戏厅底噪 | 让游戏厅成为活空间。 | 多台 CRT、按钮、硬币、少年含混声、低天花混响。 | free | 4 | audio/ambience/AMB_002_old_arcade_loop.wav |
| SFX_003 | Clip 04 / MSB029-MSB037 | 00:58.0-01:02.0 | hard_sfx | 硬币入槽 | 对战仪式开始。 | 旧硬币叮、滑入金属槽、按钮轻响。 | object | 4 | audio/sfx/SFX_003_coin_insert.wav |
| SFX_004 | Clip 05 / MSB038-MSB049 | 01:06.0-01:25.0 | hard_sfx | 街机按键对战 | 把冲突先限制在游戏里。 | 摇杆撞击、彩色按钮快速敲击、CRT 闪白。 | action | 4 | audio/sfx/SFX_004_arcade_duel_buttons.wav |
| SFX_005 | Clip 05 / MSB045-MSB049 | 01:22.0-01:27.0 | hard_sfx | 胜利红光失真 | 哥哥赢和彬子受辱。 | 胜利音效不要用版权旋律，使用原创短促 8-bit 上扬后失真。 | UI/object | 4 | audio/sfx/SFX_005_victory_glitch.wav |
| MUS_001 | Clip 06 / MSB050-MSB057 | 01:28.0-01:42.0 | music | 报复低频第一次出现 | 让游戏厅热闹被彬子情绪压住。 | 很低的单音 drone，几乎像机器故障，不像配乐煽情。 | free | 2 | audio/music/MUS_001_revenge_low_drone.wav |
| TRANS_001 | Clip 07 / MSB058-MSB065 | 01:42.0-01:56.0 | transition_sfx | 街机声远去到路灯声 | 兴奋转向不安。 | 门内街机声被卷帘门和夜路吞掉，路灯电流上来。 | transition | 3 | audio/sfx/TRANS_001_arcade_to_alley.wav |
| AMB_003 | Clip 08-12 / MSB066-MSB119 | 01:56.0-03:36.0 | ambience | 偏僻小路夜底 | 建立小路偏僻和危险。 | 旧路灯电流、远窗声、夜虫、湿地反光空间。 | free | 3 | audio/ambience/AMB_003_secluded_alley_loop.wav |
| SFX_006 | Clip 08 / MSB070-MSB071 | 02:04.0-02:08.0 | foley | 路边碎石预埋 | 让石块先作为环境存在。 | 鞋边蹭过碎砖，石头轻轻滚半圈。 | object | 2 | audio/sfx/SFX_006_roadside_stone_preset.wav |
| MUS_002 | Clip 09-10 / MSB076-MSB097 | 02:14.0-02:56.0 | music | 堵路心跳低脉冲 | 压缩空间，不抢对白。 | 低频脉冲很慢，像远处机器，不像动作片鼓点。 | free | 3 | audio/music/MUS_002_alley_pressure_pulse.wav |
| FOLEY_002 | Clip 10 / MSB086-MSB097 | 02:32.0-02:56.0 | foley | 围住和推搡 | 让暴力真实但不爽片化。 | 衣料摩擦、鞋底湿地滑、身体碰墙，避免清脆拳脚。 | action | 4 | audio/sfx/FOLEY_002_shove_scuffle.wav |
| SIL_001 | Clip 11 / MSB105-MSB107 | 03:07.0-03:11.0 | silence | 石块后声音抽空 | 让事件不可撤回。 | 环境突然掉下去，只剩耳鸣和极轻电流。 | action/result | 5 | audio/sfx/SIL_001_stone_after_drop.wav |
| SFX_007 | Clip 11 / MSB104-MSB106 | 03:05.0-03:07.0 | hard_sfx | 被遮挡的闷响 | 表达失手但避免血腥。 | 前景遮挡下的一声短闷响，低频多，高频少。 | action | 4 | audio/sfx/SFX_007_hidden_stone_impact.wav |
| FOLEY_003 | Clip 12 / MSB108-MSB119 | 03:16.0-03:36.0 | foley | 小川逃跑脚步和书包 | 把恐惧变成身体节奏。 | 乱脚步、白鞋打滑、浅绿书包肩带拍背。 | action | 5 | audio/sfx/FOLEY_003_xiaochuan_escape_run.wav |
| TRANS_002 | Clip 12-13 / MSB118-MSB122 | 03:32.0-03:40.0 | transition_sfx | 黑暗入口吞声 | 现实小路进入废楼。 | 后方喊声被门洞吞掉，脚步变成长走廊回声。 | transition | 4 | audio/sfx/TRANS_002_alley_to_corridor.wav |
| AMB_004 | Clip 13-14 / MSB120-MSB138 | 03:36.0-04:10.0 | ambience | 废楼走廊冷绿底噪 | 建立梦核空间。 | 冷绿荧光灯、远处水滴、空楼混响、电线轻响。 | free | 3 | audio/ambience/AMB_004_abandoned_corridor_loop.wav |
| SFX_008 | Clip 14 / MSB133-MSB138 | 04:00.0-04:10.0 | transition_sfx | 灯管闪成电话铃节奏 | 把空间声音导向电话亭。 | 荧光灯闪烁节奏逐渐变成旧电话铃前奏。 | transition | 3 | audio/sfx/SFX_008_fluorescent_to_ring.wav |
| SFX_009 | Clip 15-17 / MSB139-MSB161 | 04:10.0-04:50.0 | hard_sfx | 旧电话铃 | 召唤小川。 | 老式电话铃，干、近、稳定，带走廊混响。 | object | 4 | audio/sfx/SFX_009_old_phone_ring_loop.wav |
| FOLEY_004 | Clip 17 / MSB155-MSB160 | 04:40.0-04:47.0 | foley | 听筒拿起和电话线 | 电话动作变成转场源头。 | 旧塑料摩擦、听筒离座、弹簧线轻晃。 | object/action | 4 | audio/sfx/FOLEY_004_receiver_lift_cord.wav |
| TRANS_003 | Clip 18 / MSB162-MSB169 | 04:50.0-05:08.0 | transition_sfx | 电话线扫描线扩散 | 现实电子化。 | 电话线噪声变 CRT 扫描线，低分辨率色块闪动。 | transition | 5 | audio/sfx/TRANS_003_phone_scanline_morph.wav |
| MUS_003 | Clip 19-20 / MSB170-MSB188 | 05:08.0-05:50.0 | source_music | 8-bit 横版关卡循环 | 游戏规则接管现实。 | 90年代低分辨率清版街机 loop，有限声部，带不安小调。 | UI/source | 4 | audio/music/MUS_003_8bit_stage_loop.wav |
| SFX_010 | Clip 20 / MSB178-MSB184 | 05:24.0-05:36.0 | hard_sfx | 书包旋风和硬币冲击波 | 技能来自小学生物件。 | 短促像素旋风、硬币弹射、敌人低分辨率后退，不复杂连招。 | action/UI | 4 | audio/sfx/SFX_010_bag_coin_attacks.wav |
| SFX_011 | Clip 20 / MSB186-MSB187 | 05:38.0-05:44.0 | hard_sfx | WIN 出现后的静止 | 爽点后压住庆祝。 | WIN 弹出一声，随后一秒空白，只留街机底噪。 | UI | 3 | audio/sfx/SFX_011_win_stillness.wav |
| SFX_012 | Clip 20 / MSB188 | 05:45.0-05:50.0 | hard_sfx | INSERT COIN 闪烁尾针 | 把胜利变成循环。 | 角落文字闪烁哔声，旧街机待机音回到最初的电话/投币感。 | UI/end | 5 | audio/sfx/SFX_012_insert_coin_blink.wav |

## WAV 生成和总轨策略

1. 先生成 `audio/voice_clean/` 下的干声台词 WAV。
2. 再按 processing 生成 `audio/voice_processed/` 中的电话、远处、人群和系统声版本。
3. 环境声、foley、hard_sfx、transition_sfx、music 分别生成到 `audio/ambience/`、`audio/sfx/`、`audio/music/`。
4. 按 `exports/audio_assembly_manifest.csv` 装配 guide mix，输出到 `audio/mix/coin_slot_audio_guide_v001.wav`。
5. AIGC 视频片段生成后，再根据真实画面长度微调 start/end。

## 检查口径

- 台词不能解释画面已经表达的内容。
- 石块失手后必须声音抽空，不要用台词说明。
- 音乐以源声音和低频结构为主，不能把片子推成热血动作片。
- 8-bit 段是旧街机规则吞掉现实，不是快乐游戏庆祝。
