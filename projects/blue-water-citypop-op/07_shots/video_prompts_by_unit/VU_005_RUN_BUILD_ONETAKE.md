# VU_005_RUN_BUILD_ONETAKE - 角色依次入画的横向跟拍一镜到底

- Unit type: `one_take_group`
- Time range: 00:26-00:36
- Source: script-first director design
- Whitebox required: `true`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_014` (图1 / start_Nadia_enters): Nadia 从画面左侧进入奔跑。
- 图2 = `OP_SHOT_015` (图2 / Jean_catches_up): Jean 追上 Nadia，保持同向奔跑。
- 图3 = `OP_SHOT_016` (图3 / Marie_King_join): Marie 与 King 加入同一奔跑方向。
- 图4 = `OP_SHOT_017` (图4 / Grandis_trio_join): Grandis 三人组加入，形成节奏链。
- 图5 = `OP_SHOT_018` (图5 / end_group_dash): 全员横向奔跑队形完成。

## 剧本镜头意图 / Script Intent

剧本把 014-018 写成角色逐个入画到全员横向奔跑的累积段；镜头应按一镜到底/准一镜到底设计，而非五个孤立视频。

## 帧间关系 / Frame Relationships

这是剧本声明的一镜到底/准一镜到底单位。AIGC 必须把图1到最后一图理解为同一连续摄影机运动里的关键状态，不要硬切、不要跳轴、不要改换场地。

Incoming transition edges to respect:
- `TE_006_JEWEL_TO_RUN` from `OP_SHOT_013`: VU_005 图1/OP_SHOT_014 的开头承接宝石蓝光脉冲，像蓝光给奔跑段发令。

Outgoing transition setup:
- `TE_007_GROUP_RUN_TO_BEAT_MONTAGE` to `OP_SHOT_019`: 当前 unit 结尾要准备 wide group run -> Nadia running close-up。

## 镜头计划 / Camera Plan

- Camera movement: continuous side tracking dolly/truck, matching running speed; no hard cut inside unit
- Framing: medium-wide side profile growing wider as more characters enter
- Lens: 35mm anamorphic equivalent, mild parallax, stable horizon
- Screen direction / axis: all characters run left-to-right; never reverse or jump axis
- Focus: deep enough to keep entrants readable; slight focus breathing allowed on lead character
- Lighting: same bright daylight plaza/sky throughout

## AIGC Video Prompt

Use the ordered images exactly as listed above. The script, not the images alone, defines whether this is one take, montage, insert, or transition. Preserve character identity, costume, prop design, screen direction, camera axis, lighting continuity, and the OP rhythm. Do not add text, logo, subtitle, watermark, modern objects, or random readable markings.
Generate one continuous shot moving through 图1 -> 图2 -> ... -> final image as key states. No visible cut inside the unit. Maintain a single camera path and continuous physical motion.

## Negative / Failure Conditions

- 如果任意两帧互换，入画逻辑必须明显出错；如果模型硬切或跳轴则失败；如果全员在图1就已经出现则失败。
