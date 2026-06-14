# 投币口 / 01_AIGC 镜头资产对应表 v4

说明：本表保留 20 个叙事镜头的资产对应。20 镜现在只作为 macro storyboard；生产级分镜请查看 `19_micro_storyboard_188_panels.csv`。实际图生视频请再查看 `13_generation_units.md`，高风险镜头已经拆成更短生成单元；结构化提示词在 `14_structured_video_prompts.md`。

| Clip | 段落 | 白模参考图 | 关键帧/参考 | 视频提示词 | 主要风险 | 优先级 |
|---:|---|---|---|---|---|---:|
| 01 | 老旧小区建立 | `whitebox_renders/CAM_COMPOUND_01_ESTABLISH.png` | KF01 | `04_video_prompts.md#clip-01--老旧小区建立` | 变成现代小区或商铺 | 1 |
| 02 | 三兄弟靠近 | `whitebox_renders/CAM_COMPOUND_02_BROTHERS_APPROACH.png` | KF02 / `character_design_v2` 三兄弟设定 | `04_video_prompts.md#clip-02--三兄弟靠近` | 人物关系不清、出现女生 | 1 |
| 03 | 游戏厅入口 | `whitebox_renders/CAM_ARCADE_01_ENTRANCE_WIDE.png` | KF03 | `04_video_prompts.md#clip-03--游戏厅入口` | 变现代电玩城 | 1 |
| 04 | 找到街霸 | `whitebox_renders/CAM_ARCADE_02_STREET_FIGHTER_CABINET.png` | KF04 | `04_video_prompts.md#clip-04--找到街霸` | 街霸机器不明确 | 2 |
| 05 | 哥哥打赢老大 | `whitebox_renders/CAM_ARCADE_03_DUEL_OVER_SHOULDER.png` | KF04 / `character_design_v2` 彬子设定 | `04_video_prompts.md#clip-05--哥哥打赢老大` | 对战变成现实打斗 | 2 |
| 06 | 老大记仇 | `whitebox_renders/CAM_ARCADE_04_BOSS_LOSES_REACTION.png` | `character_design_v2` 混混四人组设定 | `04_video_prompts.md#clip-06--老大记仇` | 四人组混成一团 | 2 |
| 07 | 志得意满离开 | `whitebox_renders/CAM_ARCADE_EXIT_01_LEAVING.png` | `character_design_v2` 三兄弟设定 | `04_video_prompts.md#clip-07--志得意满离开` | 过早进入追逐 | 2 |
| 08 | 偏僻小路 | `whitebox_renders/CAM_ALLEY_01_WALK_HOME.png` | KF05 | `04_video_prompts.md#clip-08--偏僻小路` | 小路不够偏僻 | 1 |
| 09 | 四人堵路 | `whitebox_renders/CAM_ALLEY_02_BLOCKED.png` | KF05 / `character_design_v2` 小路对峙关系图 | `04_video_prompts.md#clip-09--四人堵路` | 堵路关系不清 | 1 |
| 10 | 围殴哥哥 | `whitebox_renders/CAM_ALLEY_03_BROTHER_BEATEN.png` | KF06 | `04_video_prompts.md#clip-10--围殴哥哥` | 动作过复杂、血腥 | 3 |
| 11 | 石块失手 | `whitebox_renders/CAM_ALLEY_04_STONE_HIT.png` | KF07 | `04_video_prompts.md#clip-11--石块失手` | 英雄化或血腥化 | 3 |
| 12 | 主角逃跑 | `whitebox_renders/CAM_ALLEY_05_ESCAPE_VECTOR.png` | KF07 | `04_video_prompts.md#clip-12--主角逃跑` | 逃跑方向漂移 | 2 |
| 13 | 进入废楼 | `whitebox_renders/CAM_CORRIDOR_01_ENTRY_LONG.png` | KF08 | `04_video_prompts.md#clip-13--进入废楼` | 走廊变医院/学校 | 2 |
| 14 | 无限走廊 | `whitebox_renders/CAM_CORRIDOR_02_LOW_TRACK.png` | KF08 | `04_video_prompts.md#clip-14--无限走廊` | 空间扭曲过度 | 2 |
| 15 | 远处电话亭 | `whitebox_renders/CAM_PHONE_01_DISTANT_GLOW.png` | KF09 | `04_video_prompts.md#clip-15--远处电话亭` | 电话亭科幻化 | 1 |
| 16 | 靠近电话亭 | `whitebox_renders/CAM_PHONE_02_APPROACH_CLOSE.png` | KF09 | `04_video_prompts.md#clip-16--靠近电话亭` | 主角变脸 | 2 |
| 17 | 接起电话 | `whitebox_renders/CAM_PHONE_03_RECEIVER_INSERT.png` | KF10 | `04_video_prompts.md#clip-17--接起电话` | 手/听筒变形 | 2 |
| 18 | 电子化 | `whitebox_renders/CAM_PHONE_02_APPROACH_CLOSE.png` | KF10 | `04_video_prompts.md#clip-18--电子化` | 变成绿色代码雨 | 3 |
| 19 | 8-bit进入 | `whitebox_renders/CAM_8BIT_01_STAGE_WIDE.png` | KF11 | `04_video_prompts.md#clip-19--进入8-bit关卡` | 像素规则不稳定 | 1 |
| 20 | WIN/INSERT COIN | `whitebox_renders/CAM_8BIT_02_WIN_SCREEN.png` | KF12 | `04_video_prompts.md#clip-20--win-与-insert-coin` | 结尾过欢乐 | 1 |

## 资产生成顺序

1. 先按 `17_character_sheet_generation_prompts_v2.md` 生成 32 张人物设计图。
2. 再生成环境：老旧小区、偏僻小路、游戏厅/街霸、废楼电话亭、8-bit 关卡。
3. 再按 `19_micro_storyboard_188_panels.csv` 分批生成 MSB001-MSB188。
4. 再从微分镜中筛选 keyframe、start frame、end frame。
5. 最后进入视频，先跑动作少的电话亭段和小路堵截段，再跑围殴、石块失手、电子化和8-bit战斗。

## 新工作流入口

- 叙事顺序：`03_aigc_storyboard.md`
- 运动控制：`12_motion_control_table.md`
- 生成单元：`13_generation_units.md`
- 结构化提示词：`14_structured_video_prompts.md`
- 生成前检查：`15_aigc_preflight_checklist.md`
- 人物返工：`16_character_design_bible_v2.md` / `17_character_sheet_generation_prompts_v2.md`
- 微分镜生产：`18_micro_storyboard_rules_v4.md` / `19_micro_storyboard_188_panels.csv` / `20_micro_storyboard_generation_batches.md`
