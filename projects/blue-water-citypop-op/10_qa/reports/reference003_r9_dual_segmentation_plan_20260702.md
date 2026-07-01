# Reference-003 R9 Dual Segmentation Plans

This package provides two segmentation views:

- Hard cut: 36 technical units for boundary audit and frame repair.
- Director semantic cut: 16 story-continuity units for external AIGC video generation.

Core rule: shot/story content integrity has higher priority than the platform 2-second single-reference-material rule. Do not merge or splice neighboring shots merely to satisfy duration.

## Which Version To Use

- Use `hard_cut_36_units.json` only for audit, repair, and locating exact source boundaries.
- Use `director_semantic_16_units.json` as the next candidate upload/generation structure.
- Black tail remains special edit-tail handling, not a normal generation unit.

## Director Semantic Cut

| # | Director unit | Time | Dur | Hard units | Decision | Why |
|---:|---|---:|---:|---|---|---|
| 1 | `DS_REF003_001_OPENING_SKY_BIRD` 开场天空与白鸟长运动 | 00:00.00-00:07.00 | 7.00s | 1 | keep | 天空开场是单一气口，保留为长镜头。 |
| 2 | `DS_REF003_002_SKY_AIRCRAFT_REVEAL` 白鸟云层到飞行器一闪 | 00:07.00-00:16.50 | 9.50s | 2 | keep | 虽然含飞行器闪现，但仍属于同一云层/天空运动短语。 |
| 3 | `DS_REF003_003_TITLE_FLARE_NADIA_REVEAL` 标题安全位、日光与Nadia首显 | 00:16.50-00:24.80 | 8.30s | 3 | keep | 开场收束到 Nadia 首次显影，是一个完整引入。 |
| 4 | `DS_REF003_004_NADIA_CONTINUOUS_CLOSE` Nadia侧脸到近景连续段 | 00:24.80-00:26.82 | 2.02s | 4,5 | merge | 同一人物、同一情绪、同一亮相功能，硬切拆分会破坏人脸连续性。 |
| 5 | `DS_REF003_005_NADIA_JEAN_MARIE_BRIDGE` Nadia到Jean再到Marie的角色桥 | 00:26.82-00:31.95 | 5.13s | 6,7,8 | merge | 这是一组角色接力桥，硬切点用于审计，但外部生成应保持转场功能完整。 |
| 6 | `DS_REF003_006_MARIE_KING_MEADOW` Marie与King草地亮相 | 00:31.95-00:33.95 | 2.00s | 9 | keep | Marie/King 是独立人物关系镜头。 |
| 7 | `DS_REF003_007_GRANDIS_TRIO_REVEAL` Grandis三人组广角到近景 | 00:33.95-00:37.20 | 3.25s | 10,11 | merge | 同一三人组亮相，广角到近景属于同一表演段。 |
| 8 | `DS_REF003_008_NADIA_RUN_PHRASE` Nadia奔跑入场与正面节拍 | 00:37.20-00:41.50 | 4.30s | 12,13,14 | merge | 奔跑入场、脚步、正面是 Nadia 动作短语，不应按身体局部硬拆。 |
| 9 | `DS_REF003_009_RUN_MONTAGE_GROUP_PHRASE` Jean、Marie/King到群像奔跑 | 00:41.50-00:47.42 | 5.92s | 15,16,17 | merge | 奔跑 montage 的接力后半段，按角色节奏合并减少身份跳变。 |
| 10 | `DS_REF003_010_ACTION_VEHICLE_BRIDGE` 反应、Grandis动作、车辆与群像转海底 | 00:47.42-00:52.43 | 5.00s | 18,19,20,21,22 | merge | 这是一个快速动作桥，硬切适合定位闪帧，不适合外部逐段生成。 |
| 11 | `DS_REF003_011_NAUTILUS_UNDERSEA_PASSAGE` Nautilus海底连续通过 | 00:52.43-01:01.44 | 9.01s | 23,24,25,26 | merge | 潜艇、水下光带和尾段属于同一环境运动。 |
| 12 | `DS_REF003_012_NIGHT_CITY_AIRCRAFT` 夜城蓝网格与夜航飞行器 | 01:01.44-01:06.02 | 4.59s | 27,28 | merge | 同一夜间空间与飞行器运动，合并更利于环境连续。 |
| 13 | `DS_REF003_013_NEMO_SUNSET_PORTRAIT` Nemo夕景肖像长段 | 01:06.02-01:11.36 | 5.34s | 29 | keep | 完整人物肖像长段，保持独立。 |
| 14 | `DS_REF003_014_NADIA_BLUE_WATER_OMEN` Nadia庄重到Blue Water绽放 | 01:11.36-01:16.45 | 5.09s | 30,31 | merge | Nadia 情绪与宝石象征是一组意义连续的神秘提示。 |
| 15 | `DS_REF003_015_WATER_SPLASH_FINAL_SKY` 水下纹理、水花爆发到最终天空 | 01:16.45-01:23.58 | 7.13s | 32,33,34,35 | merge | 水下到水花再到天空是结尾转场短语，硬拆会破坏收束。 |
| 16 | `DS_REF003_016_BLACK_TAIL` 黑场尾帧 | 01:23.58-01:24.42 | 0.83s | 36 | keep_special | 黑场尾帧是剪辑尾巴，不建议作为普通外部生成素材；单独后期处理。 |

## Hard Cut Purpose

The 36-unit version is not wrong as an audit layer, but it is too mechanical for generation. It is useful for exact boundary diagnosis, not as the primary upload structure.
