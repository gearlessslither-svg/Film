# Scene Lock Pack - SCN_ARCADE

Generated at: 2026-06-13T18:44:17+08:00

## 中文

- 项目: 投币口
- 场景: 隐藏游戏厅 (`SCN_ARCADE`)
- 批次: B01
- 主参考: `resource:media/01_AIGC/scene_refs/SC_02_arcade_interior_v001.png`
- 预览图: `project:06_previs/scene_locks/scn-arcade/scn-arcade_preview.png`

这个锁包用于减少同一场景跨镜头生成时的漂移。进入批量生图/视频前，导演应确认主参考、空间轴线、机位、光源、色彩、角色状态和禁错项。

### 必须锁定

- 场景几何、入口/出口方向、前中后景层次、镜头高度和屏幕方向保持一致。
- 参考图、白模、镜头表和提示词必须指向同一个空间。
- 允许天气、烟雾、角色表情、轻微构图微调；不允许地点时代、材质、光源逻辑和角色状态漂移。

## English

- Project: 投币口
- Scene: Hidden Arcade Room (`SCN_ARCADE`)
- Batch: B01
- Master reference: `resource:media/01_AIGC/scene_refs/SC_02_arcade_interior_v001.png`
- Preview: `project:06_previs/scene_locks/scn-arcade/scn-arcade_preview.png`

This pack is the scene continuity contract for image and video generation. It locks the approved reference, spatial axis, camera family, lighting logic, color behavior, control evidence, and reject rules before batch production.

### Locked Anchors

- S1_ARCADE_PLAY: 低天花旧游戏机房、两侧街机、CRT 红蓝绿光、烟雾、脏塑料门帘

### Lighting Logic

- 1990s damp night, CRT blue-green practicals, warm street spill, low-key realism

## Shot Subset

| Shot | Seq | Beat | Camera | Action | Prompt |
| --- | --- | --- | --- | --- | --- |
| MSB019 | 03 | 门帘擦镜 | CAM_ARCADE_01_ENTRANCE_WIDE | 门帘晃动作为隐藏剪辑 | 07_shots/prompts/MSB019.md |
| MSB020 | 03 | 三兄弟入口剪影 | CAM_ARCADE_01_ENTRANCE_WIDE | 站位保持阿磊前、小川中、小满后 | 07_shots/prompts/MSB020.md |
| MSB025 | 03 | 摇杆按钮前景 | CAM_ARCADE_01_ENTRANCE_WIDE | 固定近景 | 07_shots/prompts/MSB025.md |
