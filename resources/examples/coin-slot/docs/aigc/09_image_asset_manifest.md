# 投币口 / 01_AIGC 图像资产生成清单 v1

用途：明早检查所有已生成视觉资产。AIGC 优先，本清单按“先锁人设和环境，再看关键帧，再进视频”的顺序排列。

实际进入图生视频前，请先查看：

- `11_aigc_director_workflow.md`
- `12_motion_control_table.md`
- `13_generation_units.md`
- `14_structured_video_prompts.md`
- `15_aigc_preflight_checklist.md`

## 角色设定

| ID | 文件 | 用途 | 关键锁定 |
|---|---|---|---|
| CS_A | `character_refs/CS_A_three_brothers_v001.png` | 三兄弟人设 | 哥哥10-11岁、主角7岁蓝白校服红领巾绿书包、小弟弟5-6岁；全是男孩 |
| CS_B | `character_refs/CS_B_bully_group_v001.png` | 混混四人组人设 | 小矮个老大、瘦高个、胖子、小跑腿轮廓差异明确 |

## 场景参考

| ID | 文件 | 对应段落 | 白模/文档参考 |
|---|---|---|---|
| SC_01 | `scene_refs/SC_01_compound_corner_v001.png` | 老旧小区偏僻角落 | `CAM_COMPOUND_01_ESTABLISH` / `SCENE_COMPOUND` |
| SC_02 | `scene_refs/SC_02_arcade_interior_v001.png` | 游戏机房内部 | `CAM_ARCADE_01_ENTRANCE_WIDE` / `SCENE_ARCADE` |
| SC_03 | `scene_refs/SC_03_arcade_exit_v001.png` | 游戏机房门口离开点 | `CAM_ARCADE_EXIT_01_LEAVING` / `SCENE_ARCADE_EXIT` |
| SC_04 | `scene_refs/SC_04_secluded_alley_v001.png` | 偏僻小路堵截 | `CAM_ALLEY_02_BLOCKED` / `SCENE_ALLEY` |
| SC_05 | `scene_refs/SC_05_abandoned_corridor_phonebooth_v001.png` | 废楼走廊和电话亭 | `CAM_PHONE_01_DISTANT_GLOW` / `SCENE_CORRIDOR` + `SCENE_PHONEBOOTH` |
| SC_06 | `scene_refs/SC_06_8bit_stage_v001.png` | 8-bit 横版关卡 | `CAM_8BIT_01_STAGE_WIDE` / `SCENE_8BIT` |

## 关键帧

| ID | 文件 | 对应镜头 | 白模参考 |
|---|---|---|---|
| KF01 | `keyframes/KF01_compound_corner_v001.png` | Clip 01 | `CAM_COMPOUND_01_ESTABLISH` |
| KF02 | `keyframes/KF02_three_brothers_approach_v001.png` | Clip 02 | `CAM_COMPOUND_02_BROTHERS_APPROACH` |
| KF03 | `keyframes/KF03_arcade_entrance_v001.png` | Clip 03 | `CAM_ARCADE_01_ENTRANCE_WIDE` |
| KF04 | `keyframes/KF04_street_fighter_victory_v001.png` | Clip 05-06 | `CAM_ARCADE_03_DUEL_OVER_SHOULDER` |
| KF05 | `keyframes/KF05_alley_blocked_v001.png` | Clip 08-09 | `CAM_ALLEY_02_BLOCKED` |
| KF06 | `keyframes/KF06_brother_surrounded_v001.png` | Clip 10 | `CAM_ALLEY_03_BROTHER_BEATEN` |
| KF07 | `keyframes/KF07_roadside_stone_accident_v001.png` | Clip 11 | `CAM_ALLEY_04_STONE_HIT` |
| KF08 | `keyframes/KF08_abandoned_corridor_v001.png` | Clip 13-14 | `CAM_CORRIDOR_01_ENTRY_LONG` |
| KF09 | `keyframes/KF09_distant_phonebooth_v001.png` | Clip 15-16 | `CAM_PHONE_01_DISTANT_GLOW` |
| KF10 | `keyframes/KF10_electronicization_v001.png` | Clip 17-18 | `CAM_PHONE_02_APPROACH_CLOSE` |
| KF11 | `keyframes/KF11_8bit_stage_entry_v001.png` | Clip 19 | `CAM_8BIT_01_STAGE_WIDE` |
| KF12 | `keyframes/KF12_win_insert_coin_v001.png` | Clip 20 | `CAM_8BIT_02_WIN_SCREEN` |

## 联系表

| 文件 | 内容 |
|---|---|
| `contact_sheets/characters_contact_sheet.png` | CS_A + CS_B |
| `contact_sheets/scenes_contact_sheet.png` | SC_01-SC_06 |
| `contact_sheets/keyframes_contact_sheet.png` | KF01-KF12 |
| `contact_sheets/storyboard_20_panel_contact_sheet.png` | 20 镜分镜视觉板 |
| `contact_sheets/whitebox_contact_sheet.png` | 21 张 Blender 白模机位 |

## 检查优先级

1. 三兄弟和混混四人组是否稳定。
2. 老小区、游戏机房、小路、废楼是否像同一个90年代小城空间。
3. 小路冲突是否是“慌乱意外”，不是英雄动作。
4. 电话亭是否像现实错误物，不像科幻设备。
5. 8-bit 段是否保留废楼轮廓，并带有 `WIN` 后 `INSERT COIN` 的不安感。

## 备注

- KF07 使用安全的非血腥环境关键帧：偏僻小路、路灯、路边石块和压迫空间。具体“失手”动作交给 `03_aigc_storyboard.md` 与 `04_video_prompts.md` 控制，不在静态图里做血腥或冲击特写。
- `storyboard_panels/` 中的 SB01-SB20 是按 20 镜分镜顺序整理好的视觉板，可直接用于检查叙事节奏。
- 实际生成时不要直接用 SB01-SB20 长镜头硬跑，先按 `13_generation_units.md` 拆成短单元。
