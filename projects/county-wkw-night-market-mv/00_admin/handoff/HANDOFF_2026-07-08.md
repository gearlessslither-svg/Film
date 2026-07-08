# 项目交接包 / Handoff — county-wkw-night-market-mv

- 项目根: `/Users/jaychoupp/Story/Film/projects/county-wkw-night-market-mv`
- 项目中文名: 县城王家卫
- 项目类型: 音乐 MV 类，弱剧情，强情绪/强视觉
- 生成时间: 2026-07-08

## 当前状态 / Current State

首批 8 张 lookdev mood frames 已完成并落盘，当前状态为 `image_ready`。本批不是完整 MV 分镜，而是用于锁定“县城夜市真实物件 + 复古未来霓虹 + 暧昧青春感”的视觉方向。

本窗口已完成一次小批量生图和交接刷新。继续推进时仍建议保持小批次，不要在一个窗口里连续堆大量图片。

## 创意主线 / Creative Spine

县城夜市版复古未来 MV：男孩骑机车穿过像横店、义乌周边商贸县城气质的夏夜夜市，在游戏摊、啤酒摊、小巷、KTV 门口和田野小路之间遇见女孩。不是大都市赛博朋克，而是塑料凳、雨棚、电瓶车、啤酒箱、廉价 LED 和雨水反光构成的中国县城浪漫。

## 已锁定设定 / Locked Rules

- 项目分类为音乐 MV，不是强剧情片；先锁情绪线和视觉，不需要完整对白门禁。
- 人物核心：男孩 + 女孩 + 机车。人物数量要少，方便连续性。
- 视觉核心：县城夜市真实物件 + 复古未来霓虹 + 暧昧青春感。
- “王家卫”只作为人类沟通简称；生产提示词要转写成明确视觉语言：90 年代港片式霓虹浪漫、慢门拖影、雨夜反光、红绿黄荧光、玻璃/雨布/镜面遮挡、偏心构图、长焦压缩、孤独旁白感。
- 不要拍成干净的未来都市，不要豪车/豪华科幻机车，不要可读品牌和店招文字。
- 所有交付型提示词必须中英双语，视频生成提示词尤其要中文 + English。
- AIGC 视频提示词必须写明只要音效/环境声，不要音乐/BGM；音乐留到后期剪辑。

## 已完成 / Done

- 创建项目目录和 12 段基础结构。
- 写入项目 brief: `01_intake/PROJECT_BRIEF.md`
- 写入题材门禁: `02_direction/TOPIC_SELECTION_GATE.md`
- 写入弱剧情/情绪线: `03_story/outlines/STORY_SPINE.md`
- 写入风格圣经: `04_lookdev/STYLE_BIBLE.md`
- 写入首批 lookdev 提示词包: `04_lookdev/LOOKDEV_MOOD_FRAMES_V1.md`
- 创建 idea_board: `03_story/idea_board/idea_board.json`
- 创建生成任务: `08_generation/jobs/lookdev_moodframes_v1/MANIFEST.md`
- 生成并复制 8 张 mood frames 到 `08_generation/jobs/lookdev_moodframes_v1/outputs/`
- 生成联系表: `08_generation/jobs/lookdev_moodframes_v1/lookdev_moodframes_v1_contact_sheet.png`
- 写入 QA 记录: `08_generation/jobs/lookdev_moodframes_v1/QA.md`
- 建立 asset bible: `05_asset_bible/`
- 写入导演语义 shot plan: `07_shots/SHOT_PLAN_DIRECTOR_SEMANTIC_V1.md`
- 写入正式 keyframe queue 骨架: `07_shots/KEYFRAME_QUEUE_V1.md`
- 建立并生成 hardlock 候选批次: `08_generation/jobs/hardlocks_v1/`
- 生成 hardlock 联系表: `08_generation/jobs/hardlocks_v1/hardlocks_v1_contact_sheet.png`
- 写入 hardlock QA: `08_generation/jobs/hardlocks_v1/QA.md`
- 补齐正式 keyframes_v1 全 14 张: `08_generation/jobs/keyframes_v1/outputs/`
- 生成 keyframe 联系表: `08_generation/jobs/keyframes_v1/keyframes_v1_contact_sheet.png`
- 写入 keyframe QA: `08_generation/jobs/keyframes_v1/QA.md`
- 写入 14 段中英双语图生视频提示词: `08_generation/jobs/video_prompts_v1/PROMPTS.md`
- 写入剪辑指南: `09_edit/EDIT_GUIDE_V1.md`
- 生成 75 秒无声静态 animatic: `09_edit/animatics/static_animatic_v1/county_wkw_static_animatic_v1_silent.mp4`
- 写入 animatic manifest/QA: `09_edit/animatics/static_animatic_v1/MANIFEST.md` 和 `QA.md`
- 生成 75 秒本地 moving preview（轻微推拉 + 原创草稿音乐）: `09_edit/animatics/moving_preview_v1/county_wkw_moving_preview_v1_with_scratch_music.mp4`
- 写入 moving preview manifest/QA/music notes: `09_edit/animatics/moving_preview_v1/`
- 写入项目完成度审计: `10_qa/PROJECT_COMPLETION_AUDIT_V1.md`
- 写入静态审阅包索引: `11_delivery/packages/static_review_v1/MANIFEST.md`
- 打包静态审阅 zip: `11_delivery/packages/static_review_v1/county_wkw_static_review_v1.zip`
- 打包 moving preview zip: `11_delivery/packages/moving_preview_v1/county_wkw_moving_preview_v1.zip`
- 生成 14 段本地 proxy clips（每段环境声/音效 only，无音乐）: `09_edit/proxy_clips/local_proxy_clips_v1/outputs/`
- 组装 proxy MV 环境声版: `11_delivery/final_proxy_mv_v1/county_wkw_proxy_mv_v1_ambience_only.mp4`
- 组装 proxy MV 草稿音乐版: `11_delivery/final_proxy_mv_v1/county_wkw_proxy_mv_v1_with_scratch_music.mp4`
- 写入 proxy clips/final proxy MV manifest/QA。
- 打包 proxy MV zip: `11_delivery/packages/proxy_mv_v1/county_wkw_proxy_mv_v1.zip`
- 生成外部图生视频上传包: `11_delivery/packages/external_i2v_upload_v1/county_wkw_external_i2v_upload_v1.zip`
- 建立外部视频回收槽位: `09_edit/external_clips/external_i2v_clips_v1/`
- 写入外部视频回收/组装脚本: `09_edit/tools/assemble_external_mv_v1.py`
- 升级外部视频组装脚本：回片到位后会自动生成 final external MV manifest、QA、checksums 和 zip 包。
- 生成 final proxy candidate 封面、checksums、manifest、QA 和签收说明: `11_delivery/final_proxy_candidate_v1/`
- 打包 final proxy candidate: `11_delivery/packages/final_proxy_candidate_v1/county_wkw_final_proxy_candidate_v1.zip`
- 写入完成状态验证器: `10_qa/validate_completion_state.py`
- 生成最新完成状态表: `10_qa/completion_state_v1.json` 和 `10_qa/completion_state_v1.csv`
- 写入最终决策门: `11_delivery/final_decision_gate_v1/FINAL_DECISION_GATE.md`
- 写入 proxy final 签收自动收口脚本: `11_delivery/final_decision_gate_v1/finalize_proxy_acceptance.py`
- 打包最终决策门: `11_delivery/packages/final_decision_gate_v1/county_wkw_final_decision_gate_v1.zip`
- 更新项目 README 当前状态。

8 张输出：

1. `LD001_night_market_entrance.png`
2. `LD002_boy_motorcycle_led_awning.png`
3. `LD003_girl_game_booth_bulbs.png`
4. `LD004_beer_stall_smoke_crossing.png`
5. `LD005_red_green_alley_ride.png`
6. `LD006_ktv_repair_shop_reflection.png`
7. `LD007_wholesale_market_gate.png`
8. `LD008_field_road_before_dawn.png`

QA 摘要：8 张齐全，尺寸均为 `1915 x 821`。LD005 第一版出现可读 `KTV`，已重生为无字灯牌版本并保存 corrected output。整体通过首轮 lookdev。

## 下一步 / NEXT

最新自检结果：`overall_status=pending_director_or_external_i2v`，`blocking_failures=0`，`director_acceptance=pending`。也就是说项目内部素材、提示词、包完整性、六个 zip 包和校验没有硬失败；最终完成只差导演签收 proxy 风格，或回收 14 段外部图生视频并组装外部 AIGC 正片。

建议不要继续生图。下一步只做最终决策门：

1. 先读 `11_delivery/final_decision_gate_v1/FINAL_DECISION_GATE.md`。
2. 导演审核 `11_delivery/packages/final_proxy_candidate_v1/county_wkw_final_proxy_candidate_v1.zip`。当前 QA：proxy 候选片约 74.73 秒、1920x824、24fps、H.264、AAC 音频；音乐是原创草稿，不是最终歌。
3. 下一步有两条路：A）用 `11_delivery/packages/external_i2v_upload_v1/county_wkw_external_i2v_upload_v1.zip` 去外部 AIGC 工具生成 14 段 image-to-video clips，回收后运行 `python3 09_edit/tools/assemble_external_mv_v1.py`，脚本会生成 final external MV 文件和 zip；B）导演明确接受本地 proxy 风格作为最终风格，然后运行 `python3 11_delivery/final_decision_gate_v1/finalize_proxy_acceptance.py --confirm-director-accepts-proxy-final --audio-choice with_scratch_music`，脚本会更新签收、审计、交接、README、校验和压缩包。
4. 所有外部视频生成都必须保留硬规则：只要环境声/音效，不要音乐/BGM/配乐；最终音乐在剪辑阶段加入或替换。

## 怎么继续 / Resume

1. 新窗口先读本文件。
2. 再读 `04_lookdev/LOOKDEV_MOOD_FRAMES_V1.md`、`08_generation/jobs/lookdev_moodframes_v1/QA.md`、`05_asset_bible/setting_chapters/00_project_rules.md`、`07_shots/SHOT_PLAN_DIRECTOR_SEMANTIC_V1.md` 和 `07_shots/KEYFRAME_QUEUE_V1.md`。
3. 查看联系表 `08_generation/jobs/lookdev_moodframes_v1/lookdev_moodframes_v1_contact_sheet.png`，不要重新生成本批，除非导演明确要求返修。
4. 查看 `11_delivery/final_decision_gate_v1/FINAL_DECISION_GATE.md`、`11_delivery/packages/final_proxy_candidate_v1/MANIFEST.md`、`11_delivery/packages/external_i2v_upload_v1/MANIFEST.md` 和 `10_qa/PROJECT_COMPLETION_AUDIT_V1.md`。
5. 运行 `python3 10_qa/validate_completion_state.py` 复查项目完成状态。
6. 下一步不是继续生图，而是审 proxy MV、外部图生视频，或明确接受 proxy 风格作为最终交付路径。所有视频生成提示词继续使用 sound effects / ambience only，no music / no BGM / no soundtrack。
