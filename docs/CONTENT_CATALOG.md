# Content Catalog

这个仓库按用途分为四类，避免工具、skill、案例文档和生成资料混在一起。

## Skills

- `skills/aigc-film-pipeline/SKILL.md`
  - Codex skill 主入口。
  - 负责继续、规划、QA 或打包 AIGC-first 短片项目。
- `skills/aigc-film-pipeline/references/`
  - skill 按需读取的流程规则。
  - 覆盖故事阶段连续性、人物相似度 QA、白模 QA、pure/annotated 双版本、音频规划、续跑恢复等。

## Tools

- `scripts/validate_pipeline_state.py`
  - 项目状态和生产门禁校验。
- `scripts/visual/`
  - 白模 QA、相似度检测、联系表、pure 图结果标记、annotated 版本生成、最终分镜表重建、音频 guide、animatic、最终视频和交付校验。
- `scripts/blender/`
  - Blender 白模生成与渲染工具。
- `scripts/keep-codex-awake.ps1`
  - Windows 长任务防睡眠辅助工具。

## Docs

- `README.md`
  - 仓库入口和常用命令。
- `docs/CONTENT_CATALOG.md`
  - 当前分类索引。
- `resources/examples/coin-slot/docs/project/`
  - 原项目总览和任务日志。
- `resources/examples/coin-slot/docs/aigc/`
  - 《投币口》AIGC 全流程文档，从规则、视觉圣经、分镜、提示词、白模、音频、QA 到交付。
- `resources/examples/coin-slot/docs/normal-shooting/`
  - 同一故事的常规拍摄版翻译文档。

## Resources

- `resources/examples/coin-slot/csv/`
  - 生产表样例：188 panel 表、stage map、pure image queue、音频 cue、白模 QA、视觉 QA、交付校验等。
- `resources/examples/coin-slot/blender/`
  - 小型白模工程和 camera manifest 示例。
- `resources/examples/coin-slot/media/`
  - Git LFS 管理的图片、音频、视频、Blender 和项目内 `.zip` 交付包，保留原项目相对路径。
- `resources/RESOURCE_MAP.md`
  - 资源说明和大型媒体排除规则。

大型图片、音频、视频、`.zip` 交付包通过 Git LFS 管理；`.rar` 备份包不推送。
