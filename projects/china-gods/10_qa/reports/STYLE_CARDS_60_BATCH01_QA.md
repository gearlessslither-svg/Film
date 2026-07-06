# 《中国众神》60 风格卡 Batch 01 QA

生成时间：2026-07-06  
批次：`style_cards_60_batch01`  
范围：001-012  
输出目录：`08_generation/jobs/style_cards_60_batch01/outputs/`  
联系表：`10_qa/reports/style_cards_60_batch01_contact_sheet.png`

## 总体结论

第一批 12 张整体成立，风格硬锁守住：神明基本都不是普通真人古装，而是旧神像、木偶、泥胎、旧彩塑；现代空间清楚，反讽关系明确。

最强卡：

- 001 财神证券大厅：金融空间、红绿屏、香火红、旧财神材质都成立。
- 003 门神写字楼：玻璃旋转门和旧门神冲突强，可继续作为核心风格锚点。
- 006 雷公电母数据中心：现代电力/网络和天雷转换清楚。
- 007 龙王地下停车场：水面低机位很强，现代排水系统里的龙神概念成立。
- 010 观音机场安检：克制、庄严、现代空间清楚。
- 012 土地公拆迁现场：情绪安静，视觉寓言感好。

## 单张记录

| 编号 | 文件 | QA | 备注 |
|---|---|---|---|
| 001 | `shot_001_caishen_securities.png` | 通过 | 红绿屏和香火红平衡好，财神旧木像成立。 |
| 002 | `shot_002_yuelao_dating_app_office.png` | 通过 | 红线/网线关系明确，办公室现代感强。 |
| 003 | `shot_003_door_gods_office_lobby.png` | 通过 | 门神从现代入口中显灵，海报级。 |
| 004 | `shot_004_zaowang_delivery_kitchen.png` | 通过 | 油烟和香火混合，外卖后厨真实。 |
| 005 | `shot_005_yaowang_emergency_waiting.png` | 通过 | 冷白急诊和泥胎药王冲突成立。 |
| 006 | `shot_006_thunder_gods_data_center.png` | 通过 | 数据中心画面很稳，电弧不过分。 |
| 007 | `shot_007_dragon_king_parking_garage.png` | 通过 | 贴水面视角和排水口关系很强。 |
| 008 | `shot_008_nezha_shared_bikes.png` | 轻微清理/可重生 | 共享单车堆和红火轮成立；背景有类似标识的小符号，正式版可弱化。 |
| 009 | `shot_009_laojun_laboratory.png` | 通过 | 实验室和炼丹炉融合清楚。 |
| 010 | `shot_010_guanyin_airport_security.png` | 通过 | 机场安检和观音负担隐喻成立。 |
| 011 | `shot_011_guangong_meeting_room.png` | 轻微清理/可重生 | 会议室关系成立；投影屏有伪图表/文字感，正式版可压低屏幕内容。 |
| 012 | `shot_012_tudigong_demolition_site.png` | 通过 | 小土地公与拆迁现场的尺度反差好。 |

## 下一步

1. 继续生成 013-024，保持同一风格硬锁。
2. 暂不重生 008、011，除非导演想先精修；它们仍可作为方向图使用。
3. 每批生成后继续做联系表和 QA，并更新 `07_shots/shot_list.csv` 状态。

