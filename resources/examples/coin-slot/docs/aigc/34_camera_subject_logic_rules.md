# 投币口 / 01_AIGC 镜头-主体逻辑规则 v1

## 核心原则

分镜不是人设展示。角色不应该默认正脸看镜头；角色朝向必须服从镜头功能、行动方向和叙事视点。

每个 panel 在生成 pure 图之前，必须先判断这颗镜头属于哪一种镜头关系：

| 镜头关系 | 角色朝向 | 适用情况 |
|---|---|---|
| rear_follow | 背对镜头或三分之二背对镜头 | 镜头跟着角色进入空间、穿过走廊、逃跑、追逐 |
| over_shoulder | 前景角色背/肩/后脑，视线看向目标 | 角色发现某物、观察对手、看街机/电话亭 |
| pov_or_subjective | 角色不看镜头，画面是角色看到的东西 | 孩子视角、电话亭吸引、街机屏幕吸引 |
| profile_cross | 侧脸或三分之二侧脸 | 角色横向经过、从一个空间进入另一个空间 |
| reaction_cut | 可以正脸或三分之二正脸 | 明确切到角色反应、情绪变化、被震住 |
| confrontation | 双方互看，不看镜头 | 对峙、挑衅、堵路、街机对战 |
| insert_detail | 通常无正脸 | 手、道具、按钮、硬币、电话听筒等细节 |

## 禁止默认

- 禁止所有含人物镜头默认正脸面对镜头。
- 禁止在“进入、追随、逃跑、靠近目标”的镜头中让角色停下来摆拍。
- 禁止把人设图逻辑带进分镜图：人设图需要正面，分镜图需要行动逻辑。
- 禁止角色在没有剧情理由时看向镜头。
- 禁止为了看清脸破坏行进方向、空间关系或镜头动机。

## Prompt 必填字段

含人物的 pure 图 prompt 必须写明：

1. `camera_subject_relation`: rear_follow / over_shoulder / pov_or_subjective / profile_cross / reaction_cut / confrontation / insert_detail。
2. `character_facing`: backs to camera / three-quarter back / side profile / looking at target / front reaction。
3. `gaze_target`: arcade room / cabinet screen / opponent / exit / phone booth / stone / offscreen threat 等。
4. `camera_motivation`: follows the character / reveals the space / watches a reaction / locks a confrontation / shows an insert。

## 入口游戏厅段修正规则

MSB019-MSB028 是“孩子进入游戏厅”的连续段落，镜头逻辑优先于脸部展示：

- MSB019：环境/门帘擦镜，无主角正脸。
- MSB020：镜头在三兄弟身后或斜后方，三人背对/三分之二背对镜头，看向拥挤游戏厅。
- MSB021：镜头跟着阿磊往前挤一步，阿磊背对或三分之二背对镜头；小川、小满也看向厅内，不看镜头。
- MSB022：可以切小川侧脸或三分之二侧脸，但他的视线必须看向街机光，不看镜头。
- MSB023：小满躲在小川身后，侧/背向镜头，看向厅内。
- MSB024/MSB027：镜头继续跟随三兄弟进入人群，角色以背影、肩膀、后脑和侧影为主。
- 只有明确写成 reaction_cut 的镜头，才允许角色正脸。

## QA 失败类型

新增失败类型：

| issue_type | 说明 | 修正 |
|---|---|---|
| wrong_camera_subject_relation | 镜头功能与角色朝向冲突，例如跟拍进入却正脸看镜头 | 重写 prompt，明确 rear_follow / backs to camera |
| staged_character_sheet_logic | 分镜像人设展示或摆拍，不像行动中的电影镜头 | 回到 panel 的行动方向和镜头动机 |
| gaze_breaks_story_logic | 角色无理由看镜头，破坏沉浸 | 指定 gaze_target，不允许看镜头 |

## 生成关键词

可复用英文关键词：

- `rear follow shot`
- `camera follows behind the characters`
- `backs to camera`
- `three-quarter back view`
- `back of heads and shoulders visible`
- `characters look into the crowded arcade, not at the camera`
- `moving into the space, not posing`
- `single continuous movie frame, no character-sheet logic`

负面关键词：

- `front-facing portrait`
- `posing for camera`
- `looking at camera`
- `character sheet`
- `turnaround reference`
- `all faces toward viewer`
- `staged lineup`
