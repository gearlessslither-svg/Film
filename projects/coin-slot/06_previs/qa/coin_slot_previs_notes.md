> 双语说明 / Bilingual note: 本文件保留英文原文，以避免破坏提示词、文件名、路径、字段名和脚本读取。中文使用时请把它视为生产记录、规则、索引或提示词资产；英文正文为可执行/可追溯原文。 / The English source text is preserved to keep prompts, filenames, paths, field names, and script parsing stable. Treat this as a production record, rule, index, or prompt asset; the English body is the executable and traceable source text.

# Previs Notes

The seed batch references archived whitebox paths from `resources/examples/coin-slot`. Next previs pass should copy or regenerate a 12-shot control layer set under `06_previs/control_layers/` and verify:

- screen direction from compound to arcade and alley,
- child scale against doors, cabinets, and walls,
- foreground occlusion in narrow corridors,
- consistent camera height and lens logic.
