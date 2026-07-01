# 蓝水晶 90s Citypop 真人片头 / Blue Water Citypop OP

这是一个按工业化 AIGC 影视流程归拢的项目文件夹。

- 项目代号: `blue-water-citypop-op`
- 项目状态: active
- 当前阶段: `08_generation`
- 原始项目位置: (not linked yet)
- 外部/样例资源: (not linked yet)

## 使用方式

1. 导演把点子、截图、视频、参考图放入 `01_intake/source_inputs/` 或 `01_intake/references/`。
2. AI 分析结果写入 `01_intake/analysis/`，并同步更新 `project.yaml` 的阶段状态。
3. 创意方向确认后，把故事、美术、角色、场景、道具、灯光等前置资源分别放入 `03_story/`、`04_lookdev/`、`05_asset_bible/`。
4. 白模、镜头机位、ControlNet/深度/线稿/法线/分割等控制层放入 `06_previs/`。
5. 关键分镜、图像提示词、视频提示词和镜头清单放入 `07_shots/`。
6. 点击“分析当前项目”或运行 `scripts/analyze_aigc_project.py`，在 `10_qa/reports/` 输出缺失项和审美风险报告。
7. 批量生成、剪辑、QA 和交付分别进入 `08_generation/` 到 `11_delivery/`。

## 总控台读取约定

- `project.yaml`: 项目元数据、阶段顺序、模型策略、资产策略。
- `assets_link_map.md`: 外部旧目录、LFS 资源、参考资料和大文件映射。
- `07_shots/shot_list.csv`: 镜头级任务表，后续可被 GUI、Blender、图片模型和视频模型共同读取。
- 每个阶段目录只放本阶段的“产物”和“决策证据”，临时缓存不进入 Git。

## v2 重制说明

已按用户纠正重建为《蓝宝石之谜》1m30s OP 结构致敬版：第一镜为白鸽在天空翱翔；后续为巴黎世博、蓝宝石、发明家、追逐、飞行、海底潜艇、敌影和海天线收尾。

## v3 高贴近复刻说明

已按用户纠正重建：从《蓝宝石之谜》1m30s OP 原画/画面功能发散，开头为云层与白鸟，随后 Jean 飞机、标题位、太阳闪光、角色介绍、奔跑段、Nautilus 下潜、海底都市、Nemo/Nadia/Blue Water、出海与最终标志位。Nadia/Jean 均按 14 岁原设处理，Nadia 使用已选 C 版蜜色肤色与原服装色块锁定。
