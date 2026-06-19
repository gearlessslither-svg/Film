# Generation Task / 生成任务: GEN_CR_SCN_COMPOUND_20260615_024139_001

- Scene / 场戏: SCN_COMPOUND
- Change request / 变更请求: CR_SCN_COMPOUND_20260615_024139
- Trigger step / 触发步骤: 08_generation
- Asset / 资产: MSB001_PURE_KEYFRAME
- Stage / 步骤: 08_generation
- Target version / 目标版本: v002
- Action / 动作: modify
- Source or target path / 原路径或目标路径: media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB001_v001.png
- Parent version / 父版本: v001

## Creative Direction / 创作方向

Board generation request / 画布生成请求

Scene / 场戏: SCN_COMPOUND 居民楼角落 / Compound corner
Main image / 主图: MSB001_PURE_KEYFRAME
Main path / 主图路径: media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB001_v001.png

Main brief / 主图备注:
游戏厅加一道关着的门，门上有个猫眼，三个小孩子出现在画面左侧，有点鬼鬼祟祟的样子，注意，三个小孩子各自有各自的动作，神态和走位，不要太接近，但整体是要描述他们偷偷摸摸的想要去这个门这里的场景

Reference stack / 关联素材:
- Reference / 关联图: character_s0_clean_v002_contact_sheet_ascii.jpg
  Path: media/01_AIGC/contact_sheets/character_s0_clean_v002_contact_sheet_ascii.jpg
  Relation note / 连线说明: Use selected visual element from this reference.
  Reference note / 关联图备注: 三个少年的人设

Output goal / 输出目标:
- Generate a clean, stable, high-quality key image suitable for downstream video AIGC.
- Preserve the main composition unless the note explicitly changes it.
- Integrate reference elements only according to relation notes.
- Avoid noise, distorted anatomy, inconsistent character identity, unreadable composition, watermarks, random text, and unwanted new props.

## Operator Notes / 操作说明

- Use this brief as the handoff packet for the image, video, text, edit, or QA tool that will produce the real asset.
- 使用这份 brief 作为外部图片、视频、文本、剪辑或 QA 工具的任务交接包。
- After real output is produced, replace or link the final asset path in the version record, then promote the version if it passes review.
- 真实输出完成后，把最终资产路径回填到版本记录；审片通过后再晋级为 current。
