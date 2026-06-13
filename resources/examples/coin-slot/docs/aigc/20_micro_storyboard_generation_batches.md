# 投币口 / 01_AIGC 微分镜生成批次 v1

本文件由 `19_micro_storyboard_188_panels.csv` 汇总而来。188 张 panel 不是最终图片本身，而是下一轮生成 storyboard 图、首尾帧、关键帧和 animatic 的生产表。

每张 panel 的完整图像提示词见 `exports/micro_storyboard_image_prompts.csv`；使用说明见 `22_micro_storyboard_prompt_pack.md`。

## 总体顺序

| Batch | Panels | 内容 | 目的 |
|---|---|---|---|
| B01 | MSB001-MSB028 | 老小区到游戏厅入口 | 先测三兄弟新设计和空间入口 |
| B02 | MSB029-MSB057 | 街霸对战到记仇 | 先测阿磊、彬子和街机冲突种子 |
| B03 | MSB058-MSB085 | 离开到堵路 | 先测回家路线、阴影和对峙站位 |
| B04 | MSB086-MSB119 | 围殴、石块、逃跑 | 最高风险动作拆解，必须逐张审 |
| B05 | MSB120-MSB154 | 废楼、走廊、电话亭 | 测试梦核空间、电话亭和听筒动作 |
| B06 | MSB155-MSB188 | 电子化和 8-bit 结尾 | 测试风格转换、像素规则和 UI 尾针 |

## 每批检查重点

### B01 / 老小区到游戏厅入口

- 范围：MSB001-MSB028，共 28 张。
- 目的：先测三兄弟新设计和空间入口。
- A 级优先：19 张。
- 关键帧候选：MSB003, MSB012, MSB018, MSB024。
- Start frame 候选：MSB007, MSB020。
- End frame 候选：MSB008, MSB016, MSB028。
- 首尾画面：MSB001「空镜压低视线」到 MSB028「街霸机远处出现」。

### B02 / 街霸对战到记仇

- 范围：MSB029-MSB057，共 29 张。
- 目的：先测阿磊、彬子和街机冲突种子。
- A 级优先：18 张。
- 关键帧候选：MSB029, MSB045, MSB046, MSB050, MSB054。
- Start frame 候选：MSB035, MSB038。
- End frame 候选：MSB037, MSB049, MSB057。
- 首尾画面：MSB029「街霸机正面」到 MSB057「街机声变闷」。

### B03 / 离开到堵路

- 范围：MSB058-MSB085，共 28 张。
- 目的：先测回家路线、阴影和对峙站位。
- A 级优先：19 张。
- 关键帧候选：MSB062, MSB066, MSB076, MSB081。
- Start frame 候选：MSB058, MSB067。
- End frame 候选：MSB065, MSB075, MSB085。
- 首尾画面：MSB058「门内到门外」到 MSB085「彬子盯阿磊」。

### B04 / 围殴、石块、逃跑

- 范围：MSB086-MSB119，共 34 张。
- 目的：最高风险动作拆解，必须逐张审。
- A 级优先：28 张。
- 关键帧候选：MSB093, MSB095, MSB102, MSB106, MSB107, MSB115, MSB119。
- Start frame 候选：MSB086, MSB108。
- End frame 候选：MSB096, MSB105, MSB118。
- 首尾画面：MSB086「四人收拢」到 MSB119「黑暗吞没」。

### B05 / 废楼、走廊、电话亭

- 范围：MSB120-MSB154，共 35 张。
- 目的：测试梦核空间、电话亭和听筒动作。
- A 级优先：26 张。
- 关键帧候选：MSB122, MSB132, MSB139, MSB143, MSB152。
- Start frame 候选：MSB120, MSB129, MSB140, MSB147。
- End frame 候选：MSB127, MSB137, MSB146, MSB154。
- 首尾画面：MSB120「入口内反打」到 MSB154「手准备拿起」。

### B06 / 电子化和 8-bit 结尾

- 范围：MSB155-MSB188，共 34 张。
- 目的：测试风格转换、像素规则和 UI 尾针。
- A 级优先：27 张。
- 关键帧候选：MSB158, MSB161, MSB166, MSB169, MSB170, MSB174, MSB183, MSB186, MSB188。
- Start frame 候选：MSB155, MSB162, MSB171。
- End frame 候选：MSB160, MSB168, MSB177, MSB184。
- 首尾画面：MSB155「听筒静止」到 MSB188「INSERT COIN 尾针」。

## 生成策略

1. 每批先生成 A 级 panel，再补 B/C 级。
2. 每批生成完先做 contact sheet，不直接进入视频。
3. 人物漂移时先回到 `16_character_design_bible_v2.md` 和 `17_character_sheet_generation_prompts_v2.md`。
4. 空间漂移时回到 Blender 白模，必要时新增白模相机。
5. MSB086-MSB119 是暴力和逃跑高风险区，只允许克制、慌乱、非血腥表达。
6. MSB155-MSB188 需要保持废楼轮廓，不允许变成独立现代游戏场景。
