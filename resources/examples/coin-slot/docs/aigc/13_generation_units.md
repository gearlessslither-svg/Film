# 投币口 / 01_AIGC 生成单元拆分表 v1

用途：本表是实际图生视频的执行顺序。20 镜叙事结构不变，但高风险镜头拆成更短、更稳的生成单元。

## 单元总表

| Unit | 来源 | 时长 | 核心事件 | 首帧 | 尾帧 | 白模 | 关键帧 | 风险 | 结构化提示 |
|---|---:|---:|---|---|---|---|---|---|---|
| U01 | Clip 01 | 4s | 老小区建立 | 小区偏角静止 | CRT 微光轻闪 | CAM_COMPOUND_01_ESTABLISH | KF01 | 现代化 | `14_structured_video_prompts.md#u01` |
| U02 | Clip 02 | 5s | 三兄弟靠近 | 三人从院内进入画面 | 三人停在门口 | CAM_COMPOUND_02_BROTHERS_APPROACH | KF02 / CS_A | 人物关系漂移 | `14_structured_video_prompts.md#u02` |
| U03 | Clip 03 | 4s | 进入游戏机房 | 三人入口停住 | 哥哥带头进入 | CAM_ARCADE_01_ENTRANCE_WIDE | KF03 | 现代电玩城 | `14_structured_video_prompts.md#u03` |
| U04 | Clip 04 | 4s | 找到街霸 | 三人靠近街霸机 | 哥哥站到操作位 | CAM_ARCADE_02_STREET_FIGHTER_CABINET | KF04 | 机器不明确 | `14_structured_video_prompts.md#u04` |
| U05 | Clip 05 | 3s | 哥哥赢对战 | 对战画面闪烁 | 老大僵住 | CAM_ARCADE_03_DUEL_OVER_SHOULDER | KF04 | 现实打斗化 | `14_structured_video_prompts.md#u05` |
| U06 | Clip 06 | 3s | 老大记仇 | 老大被红光照脸 | 同伙聚到身后 | CAM_ARCADE_04_BOSS_LOSES_REACTION | KF04 / CS_B | 四人混乱 | `14_structured_video_prompts.md#u06` |
| U07 | Clip 07 | 4s | 离开游戏机房 | 三兄弟出门 | 三人走向小路 | CAM_ARCADE_EXIT_01_LEAVING | SC_03 / CS_A | 过早追逐 | `14_structured_video_prompts.md#u07` |
| U08 | Clip 08 | 5s | 走入偏僻小路 | 三人进入小路 | 前方阴影出现 | CAM_ALLEY_01_WALK_HOME | KF05 | 小路不偏僻 | `14_structured_video_prompts.md#u08` |
| U09 | Clip 09 | 4s | 四人堵路 | 四人站在前方 | 哥哥挡住弟弟 | CAM_ALLEY_02_BLOCKED | KF05 / CS_B | 空间关系不清 | `14_structured_video_prompts.md#u09` |
| U10A | Clip 10 | 2s | 围住哥哥 | 四人靠近 | 哥哥被围在中心 | CAM_ALLEY_03_BROTHER_BEATEN | KF06 | 多人互动 | `14_structured_video_prompts.md#u10a` |
| U10B | Clip 10 | 2s | 哥哥失衡 | 哥哥被围 | 哥哥失去平衡 | CAM_ALLEY_03_BROTHER_BEATEN | KF06 | 动作血腥化 | `14_structured_video_prompts.md#u10b` |
| U11A | Clip 11 | 1.5s | 看见石块 | 主角侧面惊住 | 视线落到路边石块 | CAM_ALLEY_04_STONE_HIT | KF07 | 道具不清 | `14_structured_video_prompts.md#u11a` |
| U11B | Clip 11 | 2s | 捡起石块 | 石块在前景 | 主角弯身捡起 | CAM_ALLEY_04_STONE_HIT | KF07 | 变成武器摆拍 | `14_structured_video_prompts.md#u11b` |
| U11C | Clip 11 | 1.5s | 失手后冻结 | 短促慌乱动作后 | 所有人停住 | CAM_ALLEY_04_STONE_HIT | KF07 | 血腥/英雄化 | `14_structured_video_prompts.md#u11c` |
| U12A | Clip 12 | 2.5s | 主角起跑 | 主角愣住 | 主角冲出画面 | CAM_ALLEY_05_ESCAPE_VECTOR | KF07 | 方向漂移 | `14_structured_video_prompts.md#u12a` |
| U12B | Clip 12 | 2.5s | 追兵反应 | 后方混乱 | 追兵开始追但距离拉开 | CAM_ALLEY_05_ESCAPE_VECTOR | KF07 / CS_B | 追逐混乱 | `14_structured_video_prompts.md#u12b` |
| U13 | Clip 13 | 4s | 进入废楼 | 主角冲入入口 | 身影向深处变小 | CAM_CORRIDOR_01_ENTRY_LONG | KF08 | 走廊换场 | `14_structured_video_prompts.md#u13` |
| U14 | Clip 14 | 4s | 无限走廊 | 主角贴墙跑 | 回头后追声消失 | CAM_CORRIDOR_02_LOW_TRACK | KF08 | 空间扭曲过度 | `14_structured_video_prompts.md#u14` |
| U15 | Clip 15 | 4s | 远处电话亭 | 电话亭远处发光 | 主角停下抬头 | CAM_PHONE_01_DISTANT_GLOW | KF09 | 电话亭科幻化 | `14_structured_video_prompts.md#u15` |
| U16 | Clip 16 | 5s | 靠近电话亭 | 主角在黑暗边缘 | 站到电话亭前伸手 | CAM_PHONE_02_APPROACH_CLOSE | KF09 | 主角变脸 | `14_structured_video_prompts.md#u16` |
| U17 | Clip 17 | 3s | 接起电话 | 手靠近听筒 | 听筒拿起，电话线晃 | CAM_PHONE_03_RECEIVER_INSERT | KF10 | 手部变形 | `14_structured_video_prompts.md#u17` |
| U18A | Clip 18 | 2s | 电话线扫描线 | 听筒贴耳 | 扫描线沿电话线出现 | CAM_PHONE_02_APPROACH_CLOSE | KF10 | 绿色代码雨 | `14_structured_video_prompts.md#u18a` |
| U18B | Clip 18 | 3s | 身体与走廊电子化 | 扫描线抵达手臂 | 主角和走廊边缘像素化 | CAM_PHONE_02_APPROACH_CLOSE | KF10 | 空间重构 | `14_structured_video_prompts.md#u18b` |
| U19 | Clip 19 | 4s | 进入 8-bit | 走廊展平成横版 | 像素敌人从右入场 | CAM_8BIT_01_STAGE_WIDE | KF11 | 变 3D 游戏 | `14_structured_video_prompts.md#u19` |
| U20A | Clip 20 | 2s | 像素清场 | 主角面对敌人 | 敌人被 2-3 个技能击退 | CAM_8BIT_02_WIN_SCREEN | KF12 | 连招过复杂 | `14_structured_video_prompts.md#u20a` |
| U20B | Clip 20 | 1.5s | WIN 静止 | 敌人消失 | `WIN` 居中出现 | CAM_8BIT_02_WIN_SCREEN | KF12 | 结尾过欢乐 | `14_structured_video_prompts.md#u20b` |
| U20C | Clip 20 | 1.5s | INSERT COIN | `WIN` 停顿 | 角落闪出 `INSERT COIN` | CAM_8BIT_02_WIN_SCREEN | KF12 | 尾针不安不足 | `14_structured_video_prompts.md#u20c` |

## 执行顺序

1. 先测 U01-U04：确认老小区、游戏机房、三兄弟关系稳定。
2. 再测 U08-U09：确认偏僻小路和堵路关系稳定。
3. 再测 U15-U17：电话亭段动作少，最适合验证角色一致性。
4. 再测 U13-U14：确认废楼走廊轴线稳定。
5. 再测 U19-U20C：确认 8-bit 规则。
6. 最后测 U10A-U12B 和 U18A-U18B：这些是最高风险动作。

## 变量控制

- 每次只改一个变量：prompt、关键帧、时长、seed、motion strength 或模型。
- 先低清短秒测试，不满意时先修运动和关键帧。
- 通过标准是：动作正确、空间稳定、人物不变、节奏舒服，最后才是画质。
