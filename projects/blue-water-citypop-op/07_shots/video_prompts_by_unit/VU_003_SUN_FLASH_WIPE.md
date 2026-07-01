# VU_003_SUN_FLASH_WIPE - 两次太阳闪光擦入角色段

- Unit type: `transition_insert_pair`
- Time range: 00:08-00:12
- Source: script-first director design
- Whitebox required: `false`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_005` (图1 / flash_A): 第一次太阳闪光，作为图形化切点。
- 图2 = `OP_SHOT_006` (图2 / flash_B_transition_out): 第二次太阳闪光，擦入角色介绍。

## 剧本镜头意图 / Script Intent

用两次太阳闪光作为图形化切点，把天空段擦入角色介绍。

## 帧间关系 / Frame Relationships

这是剧本声明的转场单位。图2 的开头必须承接图1 的结束状态；转场关系比单张画面更重要。

Incoming transition edges to respect:
- `TE_004_SKY_TO_FLASH` from `OP_SHOT_004`: 图1/OP_SHOT_005 用太阳闪光打断标题安全位，为角色段预备擦入。

Outgoing transition setup:
- `TE_005_FLASH_TO_CHARACTER` to `OP_SHOT_007`: 当前 unit 结尾要准备 second sun flare -> Nadia character card。

## 镜头计划 / Camera Plan

- Camera movement: locked sky inserts; brightness blooms then resolves
- Framing: sun behind cloud edge, graphic flare
- Lens: telephoto-leaning sky insert with controlled flare
- Screen direction / axis: none; brightness is the transition driver
- Focus: cloud edge and sun bloom
- Lighting: warm flare over blue sky

## AIGC Video Prompt

Use the ordered images exactly as listed above. The script, not the images alone, defines whether this is one take, montage, insert, or transition. Preserve character identity, costume, prop design, screen direction, camera axis, lighting continuity, and the OP rhythm. Do not add text, logo, subtitle, watermark, modern objects, or random readable markings.
Generate the transition so the incoming image begins by inheriting the outgoing image color/motion/object state. The transition is mandatory, not optional decoration.

## Negative / Failure Conditions

- 如果两次闪光没有节奏差异，转场会变成重复素材；如果第二闪不允许擦入角色段，则失败。
