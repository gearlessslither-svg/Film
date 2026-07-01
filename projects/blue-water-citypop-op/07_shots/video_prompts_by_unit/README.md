# Video Prompts By Unit

这些提示词按剧本镜头单位生成，不按单张图片生成。最终图生视频阶段优先使用本目录，而不是 `07_shots/video_prompts/OP_SHOT_*.md` 的旧单帧提示词。

规则：多图单位必须把输入图片按 `图1`、`图2`、`图3` 标清；转场从 `transition_edges.json` 读取，并写入 incoming/unit prompt。

- `VU_001_CLOUD_PRELUDE.md` - 云层静默开场 (single_shot, OP_SHOT_001)
- `VU_002_BIRD_PLANE_SKY_CHAIN.md` - 白鸟到飞机的天空运动链 (scripted_continuity_sequence, OP_SHOT_002, OP_SHOT_003, OP_SHOT_004)
- `VU_003_SUN_FLASH_WIPE.md` - 两次太阳闪光擦入角色段 (transition_insert_pair, OP_SHOT_005, OP_SHOT_006)
- `VU_004_CHARACTER_INTRO_MONTAGE.md` - 角色介绍节奏 montage (montage_sequence, OP_SHOT_007, OP_SHOT_008, OP_SHOT_009, OP_SHOT_010, OP_SHOT_011, OP_SHOT_012, OP_SHOT_013)
- `VU_005_RUN_BUILD_ONETAKE.md` - 角色依次入画的横向跟拍一镜到底 (one_take_group, OP_SHOT_014, OP_SHOT_015, OP_SHOT_016, OP_SHOT_017, OP_SHOT_018)
- `VU_006_RUN_BEAT_MONTAGE.md` - 奔跑四拍表情 montage (montage_sequence, OP_SHOT_019, OP_SHOT_020, OP_SHOT_021, OP_SHOT_022)
- `VU_007_AIRCRAFT_JEWEL_MATCH.md` - 飞机蓝天到 Blue Water 天空倒影 match cut (transition_pair, OP_SHOT_023, OP_SHOT_024)
- `VU_008_NAUTILUS_DIVE_CONTINUITY.md` - Nautilus 下潜连续空间 (multi_shot_continuity, OP_SHOT_025, OP_SHOT_026)
- `VU_009_MECHA_INSERTS.md` - 机械色块与推进插入 (insert_montage, OP_SHOT_027, OP_SHOT_028)
- `VU_010_UNDERSEA_CITY_REVEAL.md` - 海底都市点亮到全景 (continuous_reveal, OP_SHOT_029, OP_SHOT_030)
- `VU_011_SUBMARINE_CREW_MONTAGE.md` - Nautilus 船员与主角严肃 montage (montage_sequence, OP_SHOT_031, OP_SHOT_032, OP_SHOT_033, OP_SHOT_034)
- `VU_012_BLUE_WATER_THREAT_MATCH.md` - Blue Water 蓝光到敌人红光威胁 (transition_pair, OP_SHOT_035, OP_SHOT_036)
- `VU_013_NAUTILUS_ASCENT.md` - Nautilus 加速上升 (single_shot_with_transition_out, OP_SHOT_037)
- `VU_014_SURFACE_ONETAKE.md` - 水下上浮到海天线一镜到底 (one_take_group, OP_SHOT_038, OP_SHOT_039, OP_SHOT_040)
- `VU_015_FINAL_BIRD_SKY_PAN.md` - 白鸟回归到最终天空留白 (one_take_group, OP_SHOT_041, OP_SHOT_042)

## Reference 002 Active Opening Recut

Active 00:00-00:23 unit prompts now live in `VU_REF002_001_WHITE_BIRD_OPENING.md` through `VU_REF002_005_NADIA_CLOSEUP_ENTRY.md`. The old `VU_001_024_OPENING_SKY_BIRD_PLANE_ONETAKE.md` is retained as a superseded review artifact, not accepted timing.

## Reference 003 Active Full OP Units

Official generation now uses `VU_REF003_001_BLACK_CLOUD_FADEIN.md` through `VU_REF003_021_BLACK_TAIL.md`. Older `VU_REF002_*` prompts are superseded by the full 84.44s reference video and should not be used for accepted generation.
