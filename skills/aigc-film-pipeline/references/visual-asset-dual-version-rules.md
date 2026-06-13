# 投币口 / 01_AIGC 视觉资产双版本规则 v1

## 核心判断

从本版本开始，每一张视觉资产都分成两个版本：

| 版本 | 用途 | 是否给 AIGC 视频模型 | 是否包含文字/箭头/草图/标注 |
|---|---|---|---|
| pure / 纯画面母版 | 图生图、图生视频、关键帧、首尾帧、画质评估 | 是 | 绝对不包含 |
| annotated / 标注工作版 | 导演审片、生成决策、运动控制、返工沟通 | 否 | 可以包含精选标注 |

纯画面母版必须把全部算力留给画面质量、角色一致性、空间关系、光线和材质。任何文字、箭头、分镜边框、画幅线、草图辅助线、摄影说明，都只能在后处理阶段叠到 annotated 版本上。

## 命名规则

| 类型 | pure 路径 | annotated 路径 |
|---|---|---|
| 人物设计 | `visual_assets/pure/character_design_v2/CHR_BRO_B_FRONT_v001.png` | `visual_assets/annotated/character_design_v2/CHR_BRO_B_FRONT_v001_annotated.png` |
| 微分镜 | `visual_assets/pure/micro_storyboard/B01/MSB001_v001.png` | `visual_assets/annotated/micro_storyboard/B01/MSB001_v001_annotated.png` |
| 精修关键帧 | `visual_assets/pure/micro_keyframes_v2/MKF096_v001.png` | `visual_assets/annotated/micro_keyframes_v2/MKF096_v001_annotated.png` |
| 实拍差异参考 | `02_Normal_Shooting/delta_references/NS_DELTA_001_v001.png` | 不强制生成 annotated |

旧目录如 `character_design_v2/`、`micro_storyboard_panels/` 保留为计划/兼容入口；真正进入视频生产的图像以 `visual_assets/pure/` 为准。

## 纯画面提示词硬规则

每条 pure image prompt 必须包含：

- 无制作文字、无字幕、无中文/英文说明、无 UI 标注、无箭头、无图表、无边框、无分镜模板。
- 不要草图线稿，不要 storyboard sketch，不要 contact sheet，不要 layout notes。
- 只生成单张电影画面或角色设定画面。
- 16:9 微分镜画面必须像最终影片静帧，不像制作说明图。
- 人物设定图可以是灰墙背景全身设定，但不允许出现姓名标签和说明文字。
- 如果文字是剧情本身的一部分，例如 8-bit 结尾的 `WIN` / `INSERT COIN`，它不属于制作标注。优先单独做像素 UI 层或后期合成；若必须直接生成在 pure 图里，prompt 必须明确这是画内街机 UI，不是字幕或说明。

英文负面约束：

```text
No text, no captions, no Chinese characters, no English letters, no labels, no arrows, no diagrams, no storyboard frame, no contact sheet, no sketch lines, no layout notes, no watermark.
```

## 标注工作版字段

微分镜 annotated 版本只保留对 AIGC 拍摄最有用的字段，避免把画面盖满：

| 字段 | 是否保留 | 说明 |
|---|---|---|
| 画幅 | 保留 | 例如 16:9 |
| 景别 | 保留 | 远景/中景/近景/特写 |
| 主体位置 | 保留 | 左/中/右、前景/中景/背景 |
| 主体动作 | 保留 | 只写当前 panel 的动作状态 |
| 运动方向 | 保留 | 左到右、向深处、向下、静止 |
| 镜头运动 | 保留 | locked-off / slow push-in / tracking / handheld |
| 前景/中景/背景 | 保留 | 用于空间一致性 |
| 光线 | 保留 | 光源和色彩 |
| 首帧 | 保留 | 若该 panel 是 start frame 或相关候选 |
| 尾帧 | 保留 | 若该 panel 是 end frame 或相关候选 |
| 是否需要中间帧 | 保留 | 高风险动作必须标 |
| 生成风险 | 保留 | 1-2 个最核心风险 |
| 修正方案 | 保留 | 失败后先改什么 |
| 隐藏剪辑/转场方案 | 保留 | 只写可执行的转场 |

不保留：长篇剧情解释、台词全文、音效说明、音乐说明、导演阐述、人物小传。声音信息留在 `23_dialogue_voice_sound_music_plan.md` 和导出表里。

## 标注位置规则

- 不在 pure 图上直接改。
- annotated 版本在画面外侧加信息栏，优先右侧或下方，不遮挡主体脸、手、关键道具。
- 信息栏使用半透明深色底或白底黑字，保持可读。
- 箭头只用于主体位置和运动方向，不用来替代文字说明。
- 如果画面复杂，宁可删减标注，不要覆盖画面。

## QA 规则

每张图先验 pure，再生成 annotated：

1. pure 画面没有任何文字/标注/边框。
2. pure 画面人物身份稳定。
3. pure 画面空间关系符合白模和场景锚点。
4. pure 画面光线和上一张同场景不冲突。
5. pure 通过后才生成 annotated。
6. annotated 只检查标注准确和无遮挡，不用于评价画质。

如果 pure 不合格，删除或标记 rejected，不能用 annotated 遮丑。
