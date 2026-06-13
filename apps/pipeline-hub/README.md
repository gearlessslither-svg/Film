# Pipeline Hub GUI Scope

`pipeline-hub` 是未来总控台的预留应用目录。当前版本先把 GUI 需要依赖的项目结构、脚手架脚本和数据契约落地，避免先做界面后反复改底层格式。

## First Screen

总控台打开后应直接进入项目工作台，而不是展示介绍页。

核心入口：

- 新建项目
- 打开现有项目
- 导入旧项目文件夹
- 检查项目结构
- 查看阶段进度
- 进入镜头生产

## Minimum Useful Version

第一版 GUI 不需要一次做完所有 AIGC 能力，但必须稳定完成这些事：

1. 调用 `scripts/create_aigc_project.py` 创建新项目。
2. 读取 `projects/<slug>/project.yaml` 显示阶段进度。
3. 读取和编辑 `assets_link_map.md`，把旧项目素材映射到标准阶段目录。
4. 打开每个阶段文件夹，并显示该阶段的必需文件是否存在。
5. 读取 `07_shots/shot_list.csv`，显示镜头列表和状态。
6. 调用 `scripts/validate_aigc_project.py` 运行结构检查，提示缺失目录、缺失清单、大文件 Git LFS 风险、`.rar` 风险。

## Later Modules

- Intake Analyzer: 分析导演输入、截图、视频和参考图。
- Direction Board: 展示故事方向、美术方向、风格预览和导演确认状态。
- Asset Bible Manager: 管理角色、场景、道具、颜色、光照和连续性锁定。
- Previs Builder: 管理 Blender 白模、相机、控制层和空间关系 QA。
- Shot Factory: 批量生成关键帧、图片提示词、视频提示词和模型任务。
- QA Console: 汇总角色一致性、空间一致性、白模匹配、交付完整性。

## Implementation Note

GUI 应调用脚本或共享库，不要重新实现另一套项目结构规则。项目目录契约以 `docs/PROJECT_STRUCTURE.md` 和 `scripts/create_aigc_project.py` 为准。
