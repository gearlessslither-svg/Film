# 中国众神

现代社会 + 中国传统众神的写实神怪视觉寓言短片集。每张卡是一条 10 秒独立小故事：现实空间越普通、现代、制度化，神明越旧、越怪、越像庙里供奉物活过来，冲突越强。

- 项目代号: `china-gods`
- 项目状态: active
- 当前阶段: `08_generation`
- 原始预制作交接: `00_admin/PREPRODUCTION_HANDOFF.md`
- 风格参考: `04_lookdev/style_refs/`
- 风格验证: `04_lookdev/style_validation/`
- 60 张风格卡主清单: `07_shots/CHINA_GODS_60_STYLE_CARDS.md`

## 使用方式

1. 先读 `00_admin/PREPRODUCTION_HANDOFF.md` 和 `04_lookdev/STYLE_BIBLE.md`。
2. 生成图片前以 `07_shots/CHINA_GODS_60_STYLE_CARDS.md` 为准。
3. 每张图的 10 秒视频提示词必须保留动作、机位、景别、光影、特效、声音规则。
4. 声音规则全局硬锁：只要环境音/音效，不要音乐、BGM、配乐。
5. 输出图进入 `08_generation/jobs/<job>/outputs/`，不要只留在 Codex 默认生成目录。
6. QA 结论和联系表进入 `10_qa/reports/`。

## 总控台读取约定

- `project.yaml`: 项目元数据、阶段顺序、模型策略、资产策略。
- `assets_link_map.md`: 外部旧目录、LFS 资源、参考资料和大文件映射。
- `07_shots/shot_list.csv`: 镜头级任务表，后续可被 GUI、Blender、图片模型和视频模型共同读取。
- `10_qa/reports/project_audit_latest.md`: 一键分析报告，供导演和 AI 审片 Skill 讨论缺失项与审美风险。
- 每个阶段目录只放本阶段的“产物”和“决策证据”，临时缓存不进入 Git。
