# Director Shooting Script - Script-First Video Workflow

Updated: 2026-06-30T04:45:05+08:00

## Hard Principle

剧本控制镜头，镜头控制关键帧，关键帧之间的关系控制 AIGC 图片/视频提示词。图片只负责验证剧本镜头是否成立，不能倒过来决定哪些帧连续。

Production order:

1. 剧本意图 / story intent
2. 镜头单位 / video unit
3. 关键帧角色 / keyframe roles
4. 帧间关系与转场边 / frame relationships and transition edges
5. 白模或 camera manifest / previs when required
6. 图片提示词 / image prompts
7. 组级 AIGC 视频提示词 / unit video prompts
8. 关键帧生成与视频生成 / keyframes and video

## One-Take Rule

一镜到底不能靠 AIGC 从几张孤立图片里“猜连续”。如果剧本设计为一镜到底、复杂调度、复杂空间穿越、多角色连续运动、车辆/飞行器跟拍或强轴线镜头，默认先做：

`首帧 + 尾帧 + 必要关键帧 + Blender 白模/高模或代理模型 + 相机位移动画 + playblast 内录/渲染 + 控制层 -> AIGC 风格化渲染`

AIGC 的职责是渲染和风格化，不是发明空间连续性。任何一镜到底 unit 都必须先证明摄影机路径、主体相对位置、屏幕方向、开始/结束状态成立。

## Reference 003 Full OP 1:1 Recut (Active)

用户提供完整 84.44 秒 2160P OP 后，`reference-003-full-op-2160p` 成为全片主参考。旧 `reference-002-opening` 只覆盖前 23 秒，旧 `VU_REF002_*` 不再作为正式生成入口。

Active source evidence:

- Project video: `01_intake/references/reference-003-full-op-2160p.mp4`
- Contact sheet: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/contact_sheets/reference-003-full-op-2160p_contact_sheet_2fps.jpg`
- Section sheets: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/contact_sheets/sections/`
- Roughcut: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/roughcuts/reference-003-full-op-2160p_frame_stack_2fps.mp4`
- Decision: `00_admin/ai_bridge/decisions/reference_003_full_op_1to1_unit_plan_v1.md`

Generation rule: preserve reference timing, shot function, character entry order, and motion relationship; replace all source readable titles, credits, lyrics, subtitles, NHK/broadcaster marks, and random text with clean no-text live-action composition.

## Anti-Regression Rules

- 不允许直接从单张图片反推一镜到底。
- 不允许把每张关键帧默认当成一个独立镜头。
- 多图视频提示词必须写 `图1`、`图2`、`图3` 的顺序、角色和连接方式。
- 一镜到底必须写清起点、中点、终点、运动路径、屏幕方向、人物相对位置、禁止硬切。
- montage 必须写清硬切节奏，不能被平滑成连续镜头。
- 转场必须同时写前镜头结束状态和后镜头开始状态；数据源放在 `07_shots/transition_edges.json`。
- 复杂空间/多角色调度/上浮出水/车辆方向等风险，必须先看 `06_previs/camera_manifests/video_unit_camera_manifest.json`。

## Video Units

| Unit | Type | Time | Keyframes | Director intent |
|---|---|---:|---|---|
| `VU_REF003_001_BLACK_CLOUD_FADEIN` | `fadein_establishing_pair` | 00:00.00-00:02.00 | OP_SHOT_001, OP_SHOT_002 | 完整 OP 从黑场/暗部起，淡入明亮云层和蓝天；不是白鸟第一帧开场。 |
| `VU_REF003_002_WHITE_BIRD_SKY` | `single_subject_motion_sequence` | 00:02.50-00:07.00 | OP_SHOT_003, OP_SHOT_004 | 白鸟约 2.5 秒入画并在蓝天中持续滑翔，带出 OP 的第一条运动线。 |
| `VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS` | `title_safe_bird_cloud_sequence` | 00:07.00-00:14.00 | OP_SHOT_005, OP_SHOT_006 | 白鸟继续穿过蓝天，原片有职员表和歌词；生成版要保留留白和云层节奏但不能生成可读文字。 |
| `VU_REF003_004_AIRCRAFT_BRIEF_REVEAL` | `brief_spatial_reveal` | 00:14.50-00:16.50 | OP_SHOT_007 | 完整 OP 中飞行器/机翼只短促出现，不能扩成 24 秒一镜到底。 |
| `VU_REF003_005_MAIN_TITLE_SAFE_HOLD` | `no_text_title_safe_hold` | 00:17.00-00:22.00 | OP_SHOT_008 | 原片主标题/logo 长 hold；生成版必须替换为无字天空构图，保留标题位功能和节奏。 |
| `VU_REF003_006_SUN_FLARE_TO_NADIA` | `light_transition_insert` | 00:22.50-00:23.50 | OP_SHOT_009 | 标题位后由蓝天和太阳光线转入 Nadia 入场。 |
| `VU_REF003_007_NADIA_PROFILE_ENTRY` | `character_profile_sequence` | 00:24.00-00:27.50 | OP_SHOT_010, OP_SHOT_011 | Nadia 首次人物入场，侧脸/回头/近景构成第一段角色介绍。 |
| `VU_REF003_008_JEAN_INTRO` | `character_intro_pair` | 00:28.00-00:30.50 | OP_SHOT_012 | Jean 从帽檐/眼睛到正面少年发明家形象入场。 |
| `VU_REF003_009_MARIE_KING_MEADOW` | `child_animal_meadow_gag` | 00:31.00-00:34.00 | OP_SHOT_013, OP_SHOT_014 | Marie/King 在草地中做明亮儿童喜剧节奏。 |
| `VU_REF003_010_GRANDIS_TRIO_INTRO` | `adult_trio_intro_montage` | 00:34.50-00:37.50 | OP_SHOT_015, OP_SHOT_016 | Grandis 三人组从姿态到特写，形成戏剧化成人反派/喜剧能量。 |
| `VU_REF003_011_RUNNING_MONTAGE` | `running_montage_sequence` | 00:38.00-00:47.50 | OP_SHOT_017, OP_SHOT_018, OP_SHOT_019, OP_SHOT_020, OP_SHOT_021, OP_SHOT_022 | Nadia、Jean、Marie/King 和全员奔跑按音乐节拍切换；这是 montage，不是一镜到底。 |
| `VU_REF003_012_GRANDIS_VEHICLE_ACTION` | `vehicle_action_bridge` | 00:48.00-00:51.50 | OP_SHOT_023, OP_SHOT_024, OP_SHOT_025 | 奔跑段后转 Grandis/车辆动作，形成进入 Nautilus/冒险段的桥。 |
| `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS` | `undersea_submarine_sequence` | 00:52.00-01:01.00 | OP_SHOT_026, OP_SHOT_027, OP_SHOT_028 | Nautilus 在水下光束中通过，原片有职员表；生成版保留海底运动和光线，去掉文字。 |
| `VU_REF003_014_NIGHT_CITY_BLUE_GRID` | `night_city_symbolic_reveal` | 01:01.50-01:04.50 | OP_SHOT_029, OP_SHOT_030 | 夜色城市、蓝色几何地面和空中机械形成神秘科技段。 |
| `VU_REF003_015_NIGHT_AIRCRAFT_PASS` | `brief_night_vehicle_pass` | 01:05.00-01:06.00 | OP_SHOT_031 | 夜间飞行器短切，为 Nemo 夕景段转场。 |
| `VU_REF003_016_NEMO_SUNSET_PROFILE` | `adult_portrait_hold` | 01:06.50-01:11.00 | OP_SHOT_032, OP_SHOT_033 | Nemo/船长在夕景中沉稳长 hold，成人角色威严。 |
| `VU_REF003_017_NADIA_SOLEMN_CLOSE` | `solemn_character_close` | 01:11.50-01:13.00 | OP_SHOT_034 | Nadia 进入更严肃、静止、象征性的正面近景。 |
| `VU_REF003_018_BLUE_WATER_SYMBOL` | `symbolic_jewel_transition` | 01:13.50-01:17.00 | OP_SHOT_035, OP_SHOT_036, OP_SHOT_037 | Blue Water/宝石/水下纹理承担象征性转场，原片 NHK/文字必须替换。 |
| `VU_REF003_019_WATER_SPLASH_TRANSITION` | `water_burst_transition` | 01:17.50-01:19.50 | OP_SHOT_038, OP_SHOT_039 | 水体/冰蓝爆发把画面带回天空终段。 |
| `VU_REF003_020_FINAL_SKY_SAFE_HOLD` | `final_no_text_sky_hold` | 01:19.50-01:23.00 | OP_SHOT_040, OP_SHOT_041 | 原片 NHK 结束卡在蓝天和太阳上 hold；生成版必须替换为无字最终天空构图。 |
| `VU_REF003_021_BLACK_TAIL` | `editorial_black_tail` | 01:23.50-01:24.44 | OP_SHOT_042 | OP 结束进入黑场尾帧；不需要生成复杂画面。 |

## Adversarial Tests

1. 顺序测试：一个多图 unit 的图1/图2互换后，如果提示词仍成立，则失败。
2. 单图退化测试：多图 unit 的提示词如果不需要前后图也能完整生成，则失败。
3. 模板重复测试：超过 3 个无关 unit 使用同一句机位运动，判为模板退化。
4. 剧本优先测试：图片好看但违背剧本镜头设计，图片失败。
5. 转场闭环测试：每个 transition edge 必须有前镜头结束状态、后镜头开始状态和 write_into 策略。
6. 一镜到底测试：one_take_group 必须有 start/mid/end 或等价角色、同一屏幕方向、禁止硬切。
7. Montage 测试：montage_sequence 必须明确硬切/拍点，不得被写成连续摄影。
8. 白模门禁测试：whitebox_required=true 的 unit 若要重生最终图或视频，必须先补 previs 或明确风险。

## Output Files

- `07_shots/video_units.json`：镜头单位和关键帧角色。
- `07_shots/transition_edges.json`：转场边，负责图1到图2的连接规则。
- `06_previs/camera_manifests/video_unit_camera_manifest.json`：按 unit 写的机位/轴线/白模门禁。
- `07_shots/video_prompts_by_unit/`：最终视频阶段优先使用的组级提示词。
