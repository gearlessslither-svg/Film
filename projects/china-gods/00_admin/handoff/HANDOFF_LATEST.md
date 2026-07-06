# 项目交接包 / Handoff — china-gods

> 新窗口先读这份 + `03_story/idea_board/idea_board.json`，不要重新分析整个项目。

- 项目根: `/Users/jaychoupp/Story/Film/projects/china-gods`
- 工具: AIGC Film Pipeline（Pipeline Hub `http://127.0.0.1:8787`），skill `aigc-film-pipeline`
- 生成时间: 2026-07-06 20:33
- 备注: 项目已从 60 张扩展到 100 张。本窗口完成 `066-075` 当前图片输出，更新 `shot_list.csv`，并打包 `china_gods_style_cards_001_075_20260706.zip`。当前窗口 live session 约 60.6MB OK，可以继续小批量生成。

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
- 原 60 张风格卡与详细 10s 提示词：`07_shots/CHINA_GODS_60_STYLE_CARDS.md`
- 061-100 扩展风格卡与详细 10s 提示词：`07_shots/CHINA_GODS_100_EXPANSION_061_100.md`
- 风格 Bible：`04_lookdev/STYLE_BIBLE.md`
- 当前已生成图片：`001-075`（另有 `022` 无字备选，共 76 张 PNG）
- 图片输出目录：`08_generation/jobs/style_cards_60_batch01/outputs/`
- 当前打包文件：`11_delivery/packages/china_gods_style_cards_001_075_20260706.zip`
- 打包说明：`11_delivery/packages/CHINA_GODS_STYLE_CARDS_001_075_PACKAGE.md`
- Git 远端：本批 `001-075` 已推送到提交 `fdb00fd`。
- 远程下载 ZIP：`https://github.com/gearlessslither-svg/Film/raw/main/projects/china-gods/11_delivery/packages/china_gods_style_cards_001_075_20260706.zip`
- 远程图片目录：`https://github.com/gearlessslither-svg/Film/tree/main/projects/china-gods/08_generation/jobs/style_cards_60_batch01/outputs`
- 导演反馈：`022` 离婚窗口中文标牌版很好，已恢复为正式版；无字版作为备选保留。
- 用户确认：中文标牌可保留，只要不是真实品牌、商标、真实机构敏感标识或破坏画面。后续不要过度无字化。

## 下一批 / NEXT
继续生成 `076-100`，从 `076 女娲在手机维修柜台` 开始。不要重新生成 `001-075`。

下一批顺序：
- `076` 女娲在手机维修柜台
- `077` 夸父在跑步机展厅
- `078` 精卫在海滩清理站
- `079` 刑天在无头模特橱窗
- `080` 蚩尤在机器人焊接工厂
- `081` 玉兔在生物制药冷库
- `082` 吴刚在共享办公深夜工位
- `083` 姜子牙在退休活动室
- `084` 申公豹在交通直播间
- `085` 妲己在虚拟主播公司

建议新窗口先生成 `076-085`，保存到同一个输出目录，更新 `shot_list.csv` 状态，再打包 `001-085` 并推送 Git。若继续大量生成，每 8-12 张上传一次，避免远程等待。

## 怎么继续 / Resume
1. 启动 Pipeline Hub：`/Users/jaychoupp/Story/Film_Tool_Launcher.command`
2. 校验：`python3 Film/scripts/validate_pipeline_state.py /Users/jaychoupp/Story/Film/projects/china-gods`
3. 直接读取 `07_shots/CHINA_GODS_100_EXPANSION_061_100.md` 的 `076` 段，调用内置 `image_gen` 生成。
4. 生成后从当前窗口对应的 `/Users/jaychoupp/.codex/generated_images/<thread-id>/` 复制到 `08_generation/jobs/style_cards_60_batch01/outputs/`，按 `shot_076_...png` 命名。
5. 更新 `07_shots/shot_list.csv` 对应状态为下一批状态（建议 `generated_batch07_prelim_pass`），每完成一批打包并 Git LFS 推送。

## 当前窗口注意 / Current Window Note
本窗口最后一次 relay 状态：live session `60.6MB OK`。本批 `066-075` 使用内置 `image_gen` 逐张生成，已复制到项目输出目录；没有重新生成 `001-065`。新窗口不要重新分析项目，只从本交接和 `076` 开始执行。
