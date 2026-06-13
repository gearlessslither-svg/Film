# Scene Lock Pack - SCN_COMPOUND

Generated at: 2026-06-14T00:22:28+08:00

## 中文

- 项目: coin-slot
- 场景: 老小区角落 (`SCN_COMPOUND`)
- 批次: B01
- 主参考: `pending`
- 预览图: `pending`

这个锁包用于减少同一场景跨镜头生成时的漂移。进入批量生图/视频前，导演应确认主参考、空间轴线、机位、光源、色彩、角色状态和禁错项。

### 必须锁定

- 场景几何、入口/出口方向、前中后景层次、镜头高度和屏幕方向保持一致。
- 参考图、白模、镜头表和提示词必须指向同一个空间。
- 允许天气、烟雾、角色表情、轻微构图微调；不允许地点时代、材质、光源逻辑和角色状态漂移。

## English

- Project: coin-slot
- Scene: Old Residential Compound Corner (`SCN_COMPOUND`)
- Batch: B01
- Master reference: `pending`
- Preview: `pending`

This pack is the scene continuity contract for image and video generation. It locks the approved reference, spatial axis, camera family, lighting logic, color behavior, control evidence, and reject rules before batch production.

### Locked Anchors

- S0_START_CLEAN: 老旧居民楼一楼偏僻角落、发黄水泥墙、晾衣绳、破自行车、潮湿地面、门内微弱 CRT 蓝绿光
- S0_START_CLEAN: 阿磊海军蓝外套红白斜条，小川蓝白外套红领巾浅绿书包，小满浅色大衬衫，三人从院内走向角落

### Lighting Logic

- 1990s damp night, CRT blue-green practicals, warm street spill, low-key realism

## Shot Subset

| Shot | Seq | Beat | Camera | Action | Prompt |
| --- | --- | --- | --- | --- | --- |
| MSB001 | 01 | 空镜压低视线 | CAM_COMPOUND_01_ESTABLISH | locked-off，低机位，轻微前推 | 07_shots/prompts/MSB001.md |
| MSB003 | 01 | 门缝 CRT 光 | CAM_COMPOUND_01_ESTABLISH | 只允许光轻闪 | 07_shots/prompts/MSB003.md |
| MSB006 | 01 | CRT 反光到水面 | CAM_COMPOUND_01_ESTABLISH | 低角度近景 | 07_shots/prompts/MSB006.md |
| MSB009 | 02 | 阿磊先进画 | CAM_COMPOUND_02_BROTHERS_APPROACH | 步子比弟弟大半拍 | 07_shots/prompts/MSB009.md |
| MSB012 | 02 | 三人身高差 | CAM_COMPOUND_02_BROTHERS_APPROACH | 三角形站位建立 | 07_shots/prompts/MSB012.md |
