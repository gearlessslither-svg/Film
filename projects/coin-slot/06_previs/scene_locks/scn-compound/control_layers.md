# Control Layers - SCN_COMPOUND

## 中文

当前锁包已经索引 `5` 张白模/空间参考。下一步建议为本场景补齐这些可复用控制层：

- Depth: 固定前中后景、距离压缩和遮挡关系。
- Line / Canny: 锁定门框、街机、墙面、地面边界和透视线。
- Segmentation: 分离角色、街机/门帘、墙体、地面、水面反射。
- Normal: 需要 Blender 或 3D 白模更完整时再产出。

## English

The pack currently indexes `5` whitebox/spatial references. Add depth, line, segmentation, and normal layers when a shot becomes part of the next generation batch.

## Shot Priority

| Shot | Camera | Whitebox |
| --- | --- | --- |
| MSB001 | CAM_COMPOUND_01_ESTABLISH | whitebox_renders_v2/B01/WB2_COMPOUND_MSB001.png |
| MSB003 | CAM_COMPOUND_01_ESTABLISH | whitebox_renders_v2/B01/WB2_COMPOUND_MSB003.png |
| MSB006 | CAM_COMPOUND_01_ESTABLISH | whitebox_renders_v2/B01/WB2_COMPOUND_MSB006.png |
| MSB009 | CAM_COMPOUND_02_BROTHERS_APPROACH | whitebox_renders_v2/B01/WB2_COMPOUND_MSB009.png |
| MSB012 | CAM_COMPOUND_02_BROTHERS_APPROACH | whitebox_renders_v2/B01/WB2_COMPOUND_MSB012.png |
