# 项目交接包 / Handoff — dragon-house-black-green-ink-wash-title-21x9

> 新窗口先读这份。不要重新分析旧风格，也不要回到皮影、剪纸、黑金卡片或旧水墨场景。

- 项目根: `/Users/jaychoupp/Story/Film/projects/dragon-house-black-green-ink-wash-title-21x9`
- 当前风格: `Brutal Ink Dragon Omen`
- 唯一导演锁参考: `04_lookdev/style_references/brutal_ink_omen_v1/director_reference_only_style.png`
- 生成时间: 2026-07-04 05:27 CST
- 当前状态: 20 张故事图 + opening 9s v2 首尾帧 + Blender 9s 运动参考 + AIGC 视频提示词 + 最终压包均已完成

## 已锁定规则 / Locked Rules

- 只使用 `Brutal Ink Dragon Omen`: splashed black ink, old rice paper, dry brush, flying-white gaps, sparse mineral green, sparse cinnabar, faint antique-gold cracks, severe negative space.
- 禁止: shadow-puppet, cut-paper, leather-puppet, ornate-card, black-gold card, soft scenic ink wash, old scenic ink, old Blender proxy style, readable text/logo/watermark, actor likeness, exact official costume, readable sigils.
- 构图规则: 风格接近参考，但构图不能复制参考。必须大胆变化景别、机位、尺度、人物/景观/事件比例，不要连续多张一人一龙。
- 所有 AIGC 视频提示词硬规则: sound effects and ambience only; no music, no BGM, no soundtrack.
- Opening 9s: 使用 v2 移动镜头设计，不使用 v1 静态机关版。首帧硬锁，尾帧作为最终揭示参考；Blender 视频是主要运动/空间/镜头参考。

## 最终交付地址 / Delivery

- 最终压包:
  `/Users/jaychoupp/Story/Film/projects/dragon-house-black-green-ink-wash-title-21x9/11_delivery/packages/dragon-house-black-green-ink-wash-title-21x9_brutal_ink_story20_opening9s_blender_final_v1.zip`
- 最终目录:
  `/Users/jaychoupp/Story/Film/projects/dragon-house-black-green-ink-wash-title-21x9/11_delivery/brutal_ink_omen_story20_opening9s_blender_final_v1/`
- opening 9s 首帧:
  `/Users/jaychoupp/Story/Film/projects/dragon-house-black-green-ink-wash-title-21x9/06_previs/blender/brutal_ink_opening_one_take_9s_v2/inputs/start_frame.png`
- opening 9s 尾帧:
  `/Users/jaychoupp/Story/Film/projects/dragon-house-black-green-ink-wash-title-21x9/06_previs/blender/brutal_ink_opening_one_take_9s_v2/inputs/end_frame.png`
- Blender 9s 运动参考视频:
  `/Users/jaychoupp/Story/Film/projects/dragon-house-black-green-ink-wash-title-21x9/06_previs/blender/brutal_ink_opening_one_take_9s_v2/outputs/brutal_ink_opening_one_take_9s_v2_motion_reference.mp4`
- opening 9s AIGC 综合提示词:
  `/Users/jaychoupp/Story/Film/projects/dragon-house-black-green-ink-wash-title-21x9/06_previs/blender/brutal_ink_opening_one_take_9s_v2/docs/AIGC_OPENING_9S_PROMPT_WITH_BLENDER_REFERENCE.md`
- 全部图生视频提示词索引:
  `/Users/jaychoupp/Story/Film/projects/dragon-house-black-green-ink-wash-title-21x9/11_delivery/brutal_ink_omen_story20_opening9s_blender_final_v1/prompts/AIGC_VIDEO_PROMPT_INDEX.md`

## 已完成 / Done

- 20 张故事/人物/事件图:
  `11_delivery/brutal_ink_omen_story20_opening9s_blender_final_v1/images/story20/`
- opening 9s v2 首尾帧:
  `11_delivery/brutal_ink_omen_story20_opening9s_blender_final_v1/images/opening_9s/`
- story20 + opening 联系表:
  `11_delivery/brutal_ink_omen_story20_opening9s_blender_final_v1/contact_sheets/`
- Blender 9s v2 资产:
  `06_previs/blender/brutal_ink_opening_one_take_9s_v2/`
- Blender `.blend`、脚本、MP4、联系表、渲染说明已复制进最终交付目录:
  `11_delivery/brutal_ink_omen_story20_opening9s_blender_final_v1/blender_9s_v2/`
- QA 核验:
  - story20 图片数: 20
  - opening 图片数: 2
  - Blender MP4: 9.00s, 1344x576, 21:9, 24fps
  - Blender 帧序列: 216 frames
  - 最终 zip: 约 74MB，45 个条目

## Opening 9s 设计摘要 / Opening Design

v2 设计不是静态建筑原地升起，而是一镜到底的权力地图旅行:

1. 低机位从巨大 throne gear / crown wheel 旁贴地出发。
2. 沿黑色血脉墨渠前进，近景齿轮、墨渠、断裂旧纸形成强视差。
3. 穿过升起的城堡节点、桥肋、海峡、王冠齿轮、龙骨弧。
4. 镜头持续 crane-up / dolly-out，到高空俯视完整权力地图。
5. 黑龙影如 eclipse 压顶，矿物绿和朱砂只做稀疏权力节点。

## 复盘已入库 / Lessons Written Back

- `aigc-film-pipeline`: AIGC 视频提示词必须写“只要音效/环境声，不要音乐/BGM/soundtrack”；片头/地图机关一镜到底要先设计镜头旅行路线。
- `blender-video-pipeline`: 补充片头地图类镜头的位移/视差规则、首帧硬锁/尾帧松参考规则、Blender 5.x 动画 API guard、Python 3.14 argparse `%04d` help string 坑。
- `aigc-film-project-memory`: 新增项目经验条目，覆盖 AIGC one-take start/end/Blender reference、title sequence camera displacement、Python 3.14 argparse percent escape。

## Git/归档注意

- 项目级 `.gitignore` 已忽略本地 `.venv-video/`、`renders/frames/`、121MB conversation export zip 和缓存。
- 最终包、最终目录、Blender 源脚本、`.blend`、MP4、图片、提示词、QA 文档应保留。
- 原始 216 帧序列保留在本地工作区用于返修，不作为 git 提交对象。

## 下一步 / NEXT

当前交付已经可用于 AIGC 视频生成。下一步如果继续制作，不是重新做图片，而是:

1. 使用 opening 首帧作为硬性首帧输入。
2. 上传 Blender MP4 作为主要运动/空间/镜头参考。
3. 上传尾帧作为最终揭示参考，不强求像素级尾帧匹配。
4. 使用 `AIGC_OPENING_9S_PROMPT_WITH_BLENDER_REFERENCE.md` 投喂。
5. 生成后 QA 是否一镜到底稳定、无抖动、无音乐、无文字水印、无风格漂移。
