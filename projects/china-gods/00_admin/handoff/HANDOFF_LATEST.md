# 项目交接包 / Handoff — china-gods

> 新窗口先读这份 + `03_story/idea_board/idea_board.json`，不要重新分析整个项目。

- 项目根: `/Users/jaychoupp/Story/Film/projects/china-gods`
- 工具: AIGC Film Pipeline（Pipeline Hub `http://127.0.0.1:8787`），skill `aigc-film-pipeline`
- 生成时间: 2026-07-06 10:20
- 备注: 已创建正式项目，完成 60 张风格卡清单与 001-028 当前图片输出，并打包 `china_gods_style_cards_001_028_20260706.zip` 准备上传 Git。

## 当前 board 状态 / Current board
_(no idea_board.json found)_

## 创意主线 / Creative spine
中国民间众神像旧庙神像、泥胎、木偶、纸扎一样出现在现代社会空间里，用传统神性和现代制度、消费、职场、医疗、金融、交通场景的错位制造视觉冲击。统一风格关键词：写实神怪、旧金漆、冷荧光、雨夜反光、红香火烟、现代空间压迫感。

## 已锁定设定 / Locked bible rules（务必延续）
- 神明必须是旧神像、泥胎、木雕、纸扎、布袋戏偶、金漆木偶活过来，不要普通真人古装 cosplay。
- 现代空间要真实具体；中文标牌可保留，只要不是品牌、商标、真实机构敏感标识或破坏画面。
- 每张图对应详细 10s AIGC 视频提示词，声音硬规则：只要环境音/音效，不要音乐、BGM、配乐。
- 避免真实品牌、真实公司名、真实股票代码、可识别影视 IP、游戏 CG 盔甲、动漫化、可爱吉祥物。

## 已完成 / Done
- 正式项目目录：`Film/projects/china-gods/`
- 60 张风格卡与详细 10s 提示词：`07_shots/CHINA_GODS_60_STYLE_CARDS.md`
- 风格 Bible：`04_lookdev/STYLE_BIBLE.md`
- 当前已生成图片：`001-028`
- 图片输出目录：`08_generation/jobs/style_cards_60_batch01/outputs/`
- 当前打包文件：`11_delivery/packages/china_gods_style_cards_001_028_20260706.zip`
- 打包说明：`11_delivery/packages/CHINA_GODS_STYLE_CARDS_001_028_PACKAGE.md`
- 导演反馈：`022` 离婚窗口中文标牌版很好，已恢复为正式版；无字版作为备选保留。

## 下一批 / NEXT
继续生成 `029-060`，从 `029 阴司判官在网约车后座` 开始。每 12 张一批做联系表、QA、更新 `07_shots/shot_list.csv` 状态和本交接。

## 怎么继续 / Resume
1. 启动 Pipeline Hub：`/Users/jaychoupp/Story/Film_Tool_Launcher.command`
2. 校验：`python3 Film/scripts/validate_pipeline_state.py /Users/jaychoupp/Story/Film/projects/china-gods`
3. 加卡 → 生成 → 回填 `card-image-output`（只回路径，禁回 base64）→ 核验
4. 每完成一批回来更新本交接 + HANDOFF_LATEST.md
