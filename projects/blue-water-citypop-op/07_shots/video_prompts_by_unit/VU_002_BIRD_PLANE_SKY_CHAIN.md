# VU_002_BIRD_PLANE_SKY_CHAIN - 白鸟到飞机的天空运动链

- Unit type: `scripted_continuity_sequence`
- Time range: 00:02-00:08
- Source: script-first director design
- Whitebox required: `false`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_002` (图1 / start_action): 白鸟冲入蓝天，歌曲启动。
- 图2 = `OP_SHOT_003` (图2 / motion_match_midpoint): Jean 的小飞机接过白鸟的方向和速度。
- 图3 = `OP_SHOT_004` (图3 / end_title_safe): 飞机远去，形成无字标题安全位。

## 剧本镜头意图 / Script Intent

剧本要求白鸟先启动歌曲，再由 Jean 飞机接过天空方向，最后形成无字标题位。

## 帧间关系 / Frame Relationships

不是凭图片猜连续，而是剧本声明的天空运动链；白鸟和飞机不是同一物体，但运动方向、天空色、云层密度必须承接。

Intra-unit transition edges:
- `TE_002_BIRD_TO_PLANE` `motion_match`: bird wing motion -> plane wing/airframe motion。写法：图2/OP_SHOT_003 继承图1白鸟的天空方向和速度感，像同一片天空里的动作接力。
- `TE_003_PLANE_TO_TITLE_SPACE` `same_subject_recede`: plane close/mid sky -> plane receding into title-safe sky。写法：图3/OP_SHOT_004 必须保留飞机远去和中间留白，服务标题位。

Incoming transition edges to respect:
- `TE_001_CLOUD_TO_BIRD` from `OP_SHOT_001`: 图2/OP_SHOT_002 的开头承接 OP_SHOT_001 的云层静默，白鸟必须像歌曲启动一样突然进入。

Outgoing transition setup:
- `TE_004_SKY_TO_FLASH` to `OP_SHOT_005`: 当前 unit 结尾要准备 title-safe sky brightness -> sun flare bloom。

## 镜头计划 / Camera Plan

- Camera movement: bird rushes past camera, hard/motion match to plane banking through same sky, then plane recedes to title-safe negative space
- Framing: wide sky with fast foreground pass then distant plane
- Lens: wide anamorphic, high shutter clarity on wing pass
- Screen direction / axis: left/right motion must feel continuous through sky
- Focus: bird foreground to plane mid-distance to infinity
- Lighting: same saturated blue sky and white cloud band

## AIGC Video Prompt

Use the ordered images exactly as listed above. The script, not the images alone, defines whether this is one take, montage, insert, or transition. Preserve character identity, costume, prop design, screen direction, camera axis, lighting continuity, and the OP rhythm. Do not add text, logo, subtitle, watermark, modern objects, or random readable markings.
Generate with continuity appropriate to the unit type; if cuts occur, they must preserve the scripted spatial, color, and motion bridge.

## Negative / Failure Conditions

- 如果图2和图3互换，运动链会失效；如果图3不保留标题安全留白，则失败。
