# Reference-003 Video Segment Execution Packet

- Created: `2026-06-30T06:29:12+08:00`
- Purpose: prepare the 21-unit video generation stage after all 42 official keyframes pass QA.
- Current gate: 11/21 units ready; 10/21 blocked.
- Status: prepared, waiting for 42/42 keyframes. Do not start full video segment generation yet.

## Start Condition

Run `python3 08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/rebuild_reference003_video_unit_readiness.py` after Batch07. Start video generation only when it reports `all_video_units_ready_for_generation` and 21/21 ready.

## Unit Sequence

| # | Unit | Time | Gate | Keyframes | Output |
|---:|---|---|---|---|---|
| 1 | `VU_REF003_001_BLACK_CLOUD_FADEIN` | 00:00.00-00:02.00 | `ready` | OP_SHOT_001, OP_SHOT_002 | `08_generation/outputs/video/reference003_segments/VU_REF003_001_BLACK_CLOUD_FADEIN.mp4` |
| 2 | `VU_REF003_002_WHITE_BIRD_SKY` | 00:02.50-00:07.00 | `ready` | OP_SHOT_003, OP_SHOT_004 | `08_generation/outputs/video/reference003_segments/VU_REF003_002_WHITE_BIRD_SKY.mp4` |
| 3 | `VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS` | 00:07.00-00:14.00 | `ready` | OP_SHOT_005, OP_SHOT_006 | `08_generation/outputs/video/reference003_segments/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS.mp4` |
| 4 | `VU_REF003_004_AIRCRAFT_BRIEF_REVEAL` | 00:14.50-00:16.50 | `ready` | OP_SHOT_007 | `08_generation/outputs/video/reference003_segments/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL.mp4` |
| 5 | `VU_REF003_005_MAIN_TITLE_SAFE_HOLD` | 00:17.00-00:22.00 | `ready` | OP_SHOT_008 | `08_generation/outputs/video/reference003_segments/VU_REF003_005_MAIN_TITLE_SAFE_HOLD.mp4` |
| 6 | `VU_REF003_006_SUN_FLARE_TO_NADIA` | 00:22.50-00:23.50 | `ready` | OP_SHOT_009 | `08_generation/outputs/video/reference003_segments/VU_REF003_006_SUN_FLARE_TO_NADIA.mp4` |
| 7 | `VU_REF003_007_NADIA_PROFILE_ENTRY` | 00:24.00-00:27.50 | `ready` | OP_SHOT_010, OP_SHOT_011 | `08_generation/outputs/video/reference003_segments/VU_REF003_007_NADIA_PROFILE_ENTRY.mp4` |
| 8 | `VU_REF003_008_JEAN_INTRO` | 00:28.00-00:30.50 | `ready` | OP_SHOT_012 | `08_generation/outputs/video/reference003_segments/VU_REF003_008_JEAN_INTRO.mp4` |
| 9 | `VU_REF003_009_MARIE_KING_MEADOW` | 00:31.00-00:34.00 | `ready` | OP_SHOT_013, OP_SHOT_014 | `08_generation/outputs/video/reference003_segments/VU_REF003_009_MARIE_KING_MEADOW.mp4` |
| 10 | `VU_REF003_010_GRANDIS_TRIO_INTRO` | 00:34.50-00:37.50 | `ready` | OP_SHOT_015, OP_SHOT_016 | `08_generation/outputs/video/reference003_segments/VU_REF003_010_GRANDIS_TRIO_INTRO.mp4` |
| 11 | `VU_REF003_011_RUNNING_MONTAGE` | 00:38.00-00:47.50 | `ready` | OP_SHOT_017, OP_SHOT_018, OP_SHOT_019, OP_SHOT_020, OP_SHOT_021, OP_SHOT_022 | `08_generation/outputs/video/reference003_segments/VU_REF003_011_RUNNING_MONTAGE.mp4` |
| 12 | `VU_REF003_012_GRANDIS_VEHICLE_ACTION` | 00:48.00-00:51.50 | `blocked: OP_SHOT_025` | OP_SHOT_023, OP_SHOT_024, OP_SHOT_025 | `08_generation/outputs/video/reference003_segments/VU_REF003_012_GRANDIS_VEHICLE_ACTION.mp4` |
| 13 | `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS` | 00:52.00-01:01.00 | `blocked: OP_SHOT_026, OP_SHOT_027, OP_SHOT_028` | OP_SHOT_026, OP_SHOT_027, OP_SHOT_028 | `08_generation/outputs/video/reference003_segments/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS.mp4` |
| 14 | `VU_REF003_014_NIGHT_CITY_BLUE_GRID` | 01:01.50-01:04.50 | `blocked: OP_SHOT_029, OP_SHOT_030` | OP_SHOT_029, OP_SHOT_030 | `08_generation/outputs/video/reference003_segments/VU_REF003_014_NIGHT_CITY_BLUE_GRID.mp4` |
| 15 | `VU_REF003_015_NIGHT_AIRCRAFT_PASS` | 01:05.00-01:06.00 | `blocked: OP_SHOT_031` | OP_SHOT_031 | `08_generation/outputs/video/reference003_segments/VU_REF003_015_NIGHT_AIRCRAFT_PASS.mp4` |
| 16 | `VU_REF003_016_NEMO_SUNSET_PROFILE` | 01:06.50-01:11.00 | `blocked: OP_SHOT_032, OP_SHOT_033` | OP_SHOT_032, OP_SHOT_033 | `08_generation/outputs/video/reference003_segments/VU_REF003_016_NEMO_SUNSET_PROFILE.mp4` |
| 17 | `VU_REF003_017_NADIA_SOLEMN_CLOSE` | 01:11.50-01:13.00 | `blocked: OP_SHOT_034` | OP_SHOT_034 | `08_generation/outputs/video/reference003_segments/VU_REF003_017_NADIA_SOLEMN_CLOSE.mp4` |
| 18 | `VU_REF003_018_BLUE_WATER_SYMBOL` | 01:13.50-01:17.00 | `blocked: OP_SHOT_035, OP_SHOT_036, OP_SHOT_037` | OP_SHOT_035, OP_SHOT_036, OP_SHOT_037 | `08_generation/outputs/video/reference003_segments/VU_REF003_018_BLUE_WATER_SYMBOL.mp4` |
| 19 | `VU_REF003_019_WATER_SPLASH_TRANSITION` | 01:17.50-01:19.50 | `blocked: OP_SHOT_038, OP_SHOT_039` | OP_SHOT_038, OP_SHOT_039 | `08_generation/outputs/video/reference003_segments/VU_REF003_019_WATER_SPLASH_TRANSITION.mp4` |
| 20 | `VU_REF003_020_FINAL_SKY_SAFE_HOLD` | 01:19.50-01:23.00 | `blocked: OP_SHOT_040, OP_SHOT_041` | OP_SHOT_040, OP_SHOT_041 | `08_generation/outputs/video/reference003_segments/VU_REF003_020_FINAL_SKY_SAFE_HOLD.mp4` |
| 21 | `VU_REF003_021_BLACK_TAIL` | 01:23.50-01:24.44 | `blocked: OP_SHOT_042` | OP_SHOT_042 | `08_generation/outputs/video/reference003_segments/VU_REF003_021_BLACK_TAIL.mp4` |

## Global Rules

- Generate units in order from VU_REF003_001 through VU_REF003_021.
- One unit output per expected_video_output_path; do not overwrite keyframe assets.
- Use unit prompt path and listed QA-pass keyframe anchors; preserve reference-003 timing and camera function.
- Keep generated video clean: no text, titles, credits, lyrics, NHK marks, subtitles, watermarks, or random symbols.
- After each segment, run decode validation and record status in a segment QA report.
- After all 21 segments pass, assemble roughcut in roughcut_slot order and decode-check the full MP4.

## Supporting Tools

- `rebuild_keyframe_status_previs`: `10_qa/reference_match/REFERENCE003_OFFICIAL_KEYFRAME_STATUS_20260630/rebuild_reference003_keyframe_status_previs.py`
- `rebuild_video_unit_readiness`: `08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/rebuild_reference003_video_unit_readiness.py`
- `assemble_roughcut_from_segments`: `09_edit/rough_cut/assemble_reference003_roughcut_from_segments.py`
- `update_transition_review`: `09_edit/rough_cut/update_reference003_transition_review.py`
- `update_no_text_logo_safety_review`: `10_qa/reports/update_reference003_no_text_logo_safety_review.py`
- `video_unit_qa_checklist`: `08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/qa/VIDEO_UNIT_QA_CHECKLIST.md`
- `project_validator`: `/Users/jaychoupp/Story/Film/scripts/validate_aigc_project.py`

## Post-Segment Gates

- `segments_21_decode_pass`: 21/21 expected_video_output_path files exist and complete-decode
- `transition_edges_41_reviewed`: use `python3 09_edit/rough_cut/update_reference003_transition_review.py --export-csv` for the checklist, then record all 41 TE_REF003 edges as reviewed/pass with visual evidence
- `roughcut_assembled`: run `python3 09_edit/rough_cut/assemble_reference003_roughcut_from_segments.py --print-json`; roughcut assembled in roughcut_slot order, duration close to 84.437333 seconds
- `final_no_text_logo_review`: run `python3 10_qa/reports/update_reference003_no_text_logo_safety_review.py --refresh --export-csv`; all 42 keyframes, 21 segments, and final roughcut must be manually reviewed as pass
- `completion_audit_updated`: 10_qa/reports/reference003_completion_audit_template_20260630.* updated from template to evidence-backed audit

## Per-Unit Detail

### 01. `VU_REF003_001_BLACK_CLOUD_FADEIN`

- Title: 黑场到云层蓝天淡入
- Time range: `00:00.00-00:02.00`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_001_BLACK_CLOUD_FADEIN.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_001_BLACK_CLOUD_FADEIN`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_001_BLACK_CLOUD_FADEIN.mp4`
- Current gate: `ready`
- Keyframes:
  - `OP_SHOT_001` `00:00.00` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630/outputs/OP_SHOT_001.png`
  - `OP_SHOT_002` `00:01.50` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630/outputs/OP_SHOT_002.png`
- Transition edges:
  - `TE_REF003_001_001_TO_002` OP_SHOT_001->OP_SHOT_002: 黑场/云层淡入 -> 云层蓝天显现
  - `TE_REF003_002_002_TO_003` OP_SHOT_002->OP_SHOT_003: 云层蓝天显现 -> 白鸟首次入画

### 02. `VU_REF003_002_WHITE_BIRD_SKY`

- Title: 白鸟入画与蓝天滑翔
- Time range: `00:02.50-00:07.00`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_002_WHITE_BIRD_SKY.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_002_WHITE_BIRD_SKY`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_002_WHITE_BIRD_SKY.mp4`
- Current gate: `ready`
- Keyframes:
  - `OP_SHOT_003` `00:02.50` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630/outputs/OP_SHOT_003.png`
  - `OP_SHOT_004` `00:05.00` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630/outputs/OP_SHOT_004.png`
- Transition edges:
  - `TE_REF003_002_002_TO_003` OP_SHOT_002->OP_SHOT_003: 云层蓝天显现 -> 白鸟首次入画
  - `TE_REF003_003_003_TO_004` OP_SHOT_003->OP_SHOT_004: 白鸟首次入画 -> 白鸟滑翔延续
  - `TE_REF003_004_004_TO_005` OP_SHOT_004->OP_SHOT_005: 白鸟滑翔延续 -> 无字职员表安全位

### 03. `VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS`

- Title: 白鸟字幕安全位与云层增长
- Time range: `00:07.00-00:14.00`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS.mp4`
- Current gate: `ready`
- Keyframes:
  - `OP_SHOT_005` `00:07.50` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630/outputs/OP_SHOT_005.png`
  - `OP_SHOT_006` `00:11.50` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630/outputs/OP_SHOT_006_v2.png`
- Transition edges:
  - `TE_REF003_004_004_TO_005` OP_SHOT_004->OP_SHOT_005: 白鸟滑翔延续 -> 无字职员表安全位
  - `TE_REF003_005_005_TO_006` OP_SHOT_005->OP_SHOT_006: 无字职员表安全位 -> 云层增长填画
  - `TE_REF003_006_006_TO_007` OP_SHOT_006->OP_SHOT_007: 云层增长填画 -> 飞行器短露

### 04. `VU_REF003_004_AIRCRAFT_BRIEF_REVEAL`

- Title: 飞行器短暂露出
- Time range: `00:14.50-00:16.50`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL.mp4`
- Current gate: `ready`
- Keyframes:
  - `OP_SHOT_007` `00:15.00` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_007.png`
- Transition edges:
  - `TE_REF003_006_006_TO_007` OP_SHOT_006->OP_SHOT_007: 云层增长填画 -> 飞行器短露
  - `TE_REF003_007_007_TO_008` OP_SHOT_007->OP_SHOT_008: 飞行器短露 -> 主标题无字安全位

### 05. `VU_REF003_005_MAIN_TITLE_SAFE_HOLD`

- Title: 主标题功能位无字 hold
- Time range: `00:17.00-00:22.00`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_005_MAIN_TITLE_SAFE_HOLD.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_005_MAIN_TITLE_SAFE_HOLD.mp4`
- Current gate: `ready`
- Keyframes:
  - `OP_SHOT_008` `00:18.50` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_008_v2.png`
- Transition edges:
  - `TE_REF003_007_007_TO_008` OP_SHOT_007->OP_SHOT_008: 飞行器短露 -> 主标题无字安全位
  - `TE_REF003_008_008_TO_009` OP_SHOT_008->OP_SHOT_009: 主标题无字安全位 -> 太阳光线转场

### 06. `VU_REF003_006_SUN_FLARE_TO_NADIA`

- Title: 太阳光转 Nadia
- Time range: `00:22.50-00:23.50`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_006_SUN_FLARE_TO_NADIA.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_006_SUN_FLARE_TO_NADIA`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_006_SUN_FLARE_TO_NADIA.mp4`
- Current gate: `ready`
- Keyframes:
  - `OP_SHOT_009` `00:23.00` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_009.png`
- Transition edges:
  - `TE_REF003_008_008_TO_009` OP_SHOT_008->OP_SHOT_009: 主标题无字安全位 -> 太阳光线转场
  - `TE_REF003_009_009_TO_010` OP_SHOT_009->OP_SHOT_010: 太阳光线转场 -> Nadia 侧脸入场

### 07. `VU_REF003_007_NADIA_PROFILE_ENTRY`

- Title: Nadia 侧脸入场到近景
- Time range: `00:24.00-00:27.50`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_007_NADIA_PROFILE_ENTRY.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_007_NADIA_PROFILE_ENTRY`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_007_NADIA_PROFILE_ENTRY.mp4`
- Current gate: `ready`
- Keyframes:
  - `OP_SHOT_010` `00:24.50` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_010_v2.png`
  - `OP_SHOT_011` `00:27.00` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_011_v2.png`
- Transition edges:
  - `TE_REF003_009_009_TO_010` OP_SHOT_009->OP_SHOT_010: 太阳光线转场 -> Nadia 侧脸入场
  - `TE_REF003_010_010_TO_011` OP_SHOT_010->OP_SHOT_011: Nadia 侧脸入场 -> Nadia 正面近景
  - `TE_REF003_011_011_TO_012` OP_SHOT_011->OP_SHOT_012: Nadia 正面近景 -> Jean 入场

### 08. `VU_REF003_008_JEAN_INTRO`

- Title: Jean 帽子与少年发明家入场
- Time range: `00:28.00-00:30.50`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_008_JEAN_INTRO.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_008_JEAN_INTRO`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_008_JEAN_INTRO.mp4`
- Current gate: `ready`
- Keyframes:
  - `OP_SHOT_012` `00:29.00` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_012.png`
- Transition edges:
  - `TE_REF003_011_011_TO_012` OP_SHOT_011->OP_SHOT_012: Nadia 正面近景 -> Jean 入场
  - `TE_REF003_012_012_TO_013` OP_SHOT_012->OP_SHOT_013: Jean 入场 -> Marie 与 King 草地笑点

### 09. `VU_REF003_009_MARIE_KING_MEADOW`

- Title: Marie 与 King 草地段
- Time range: `00:31.00-00:34.00`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_009_MARIE_KING_MEADOW.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_009_MARIE_KING_MEADOW`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_009_MARIE_KING_MEADOW.mp4`
- Current gate: `ready`
- Keyframes:
  - `OP_SHOT_013` `00:31.50` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_013.png`
  - `OP_SHOT_014` `00:34.00` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_014.png`
- Transition edges:
  - `TE_REF003_012_012_TO_013` OP_SHOT_012->OP_SHOT_013: Jean 入场 -> Marie 与 King 草地笑点
  - `TE_REF003_013_013_TO_014` OP_SHOT_013->OP_SHOT_014: Marie 与 King 草地笑点 -> Marie 与 King 近景
  - `TE_REF003_014_014_TO_015` OP_SHOT_014->OP_SHOT_015: Marie 与 King 近景 -> Grandis 三人组宽景

### 10. `VU_REF003_010_GRANDIS_TRIO_INTRO`

- Title: Grandis 三人组介绍
- Time range: `00:34.50-00:37.50`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_010_GRANDIS_TRIO_INTRO.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_010_GRANDIS_TRIO_INTRO.mp4`
- Current gate: `ready`
- Keyframes:
  - `OP_SHOT_015` `00:35.50` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_015.png`
  - `OP_SHOT_016` `00:37.00` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_016_v2.png`
- Transition edges:
  - `TE_REF003_014_014_TO_015` OP_SHOT_014->OP_SHOT_015: Marie 与 King 近景 -> Grandis 三人组宽景
  - `TE_REF003_015_015_TO_016` OP_SHOT_015->OP_SHOT_016: Grandis 三人组宽景 -> Grandis 三人组近景
  - `TE_REF003_016_016_TO_017` OP_SHOT_016->OP_SHOT_017: Grandis 三人组近景 -> Nadia 奔跑脚步

### 11. `VU_REF003_011_RUNNING_MONTAGE`

- Title: 角色奔跑 montage
- Time range: `00:38.00-00:47.50`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_011_RUNNING_MONTAGE.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_011_RUNNING_MONTAGE.mp4`
- Current gate: `ready`
- Keyframes:
  - `OP_SHOT_017` `00:38.00` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_017.png`
  - `OP_SHOT_018` `00:39.50` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_018.png`
  - `OP_SHOT_019` `00:41.50` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_019.png`
  - `OP_SHOT_020` `00:43.50` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_020.png`
  - `OP_SHOT_021` `00:45.50` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_021_v2.png`
  - `OP_SHOT_022` `00:47.50` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_022.png`
- Transition edges:
  - `TE_REF003_016_016_TO_017` OP_SHOT_016->OP_SHOT_017: Grandis 三人组近景 -> Nadia 奔跑脚步
  - `TE_REF003_017_017_TO_018` OP_SHOT_017->OP_SHOT_018: Nadia 奔跑脚步 -> Nadia 奔跑正面
  - `TE_REF003_018_018_TO_019` OP_SHOT_018->OP_SHOT_019: Nadia 奔跑正面 -> Jean 奔跑
  - `TE_REF003_019_019_TO_020` OP_SHOT_019->OP_SHOT_020: Jean 奔跑 -> Marie 奔跑
  - `TE_REF003_020_020_TO_021` OP_SHOT_020->OP_SHOT_021: Marie 奔跑 -> 全员奔跑
  - `TE_REF003_021_021_TO_022` OP_SHOT_021->OP_SHOT_022: 全员奔跑 -> Jean 反应近景
  - `TE_REF003_022_022_TO_023` OP_SHOT_022->OP_SHOT_023: Jean 反应近景 -> Grandis 动作桥

### 12. `VU_REF003_012_GRANDIS_VEHICLE_ACTION`

- Title: Grandis 车辆动作到群像
- Time range: `00:48.00-00:51.50`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_012_GRANDIS_VEHICLE_ACTION.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_012_GRANDIS_VEHICLE_ACTION.mp4`
- Current gate: `blocked_until_keyframes_complete`
- Blocking keyframes: OP_SHOT_025
- Keyframes:
  - `OP_SHOT_023` `00:48.00` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_023.png`
  - `OP_SHOT_024` `00:49.50` `generated_reference003_qa_pass` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_024.png`
  - `OP_SHOT_025` `00:51.50` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_025.png`
- Transition edges:
  - `TE_REF003_022_022_TO_023` OP_SHOT_022->OP_SHOT_023: Jean 反应近景 -> Grandis 动作桥
  - `TE_REF003_023_023_TO_024` OP_SHOT_023->OP_SHOT_024: Grandis 动作桥 -> 车辆/飞行器空中动作
  - `TE_REF003_024_024_TO_025` OP_SHOT_024->OP_SHOT_025: 车辆/飞行器空中动作 -> 全员群像
  - `TE_REF003_025_025_TO_026` OP_SHOT_025->OP_SHOT_026: 全员群像 -> Nautilus 水下初现

### 13. `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS`

- Title: Nautilus 海底光束段
- Time range: `00:52.00-01:01.00`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS.mp4`
- Current gate: `blocked_until_keyframes_complete`
- Blocking keyframes: OP_SHOT_026, OP_SHOT_027, OP_SHOT_028
- Keyframes:
  - `OP_SHOT_026` `00:52.50` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_026.png`
  - `OP_SHOT_027` `00:55.00` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_027.png`
  - `OP_SHOT_028` `00:58.50` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_028.png`
- Transition edges:
  - `TE_REF003_025_025_TO_026` OP_SHOT_025->OP_SHOT_026: 全员群像 -> Nautilus 水下初现
  - `TE_REF003_026_026_TO_027` OP_SHOT_026->OP_SHOT_027: Nautilus 水下初现 -> Nautilus 水下通过
  - `TE_REF003_027_027_TO_028` OP_SHOT_027->OP_SHOT_028: Nautilus 水下通过 -> Nautilus 深蓝剪影
  - `TE_REF003_028_028_TO_029` OP_SHOT_028->OP_SHOT_029: Nautilus 深蓝剪影 -> 夜城初现

### 14. `VU_REF003_014_NIGHT_CITY_BLUE_GRID`

- Title: 夜城与蓝色地面图案
- Time range: `01:01.50-01:04.50`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_014_NIGHT_CITY_BLUE_GRID.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_014_NIGHT_CITY_BLUE_GRID`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_014_NIGHT_CITY_BLUE_GRID.mp4`
- Current gate: `blocked_until_keyframes_complete`
- Blocking keyframes: OP_SHOT_029, OP_SHOT_030
- Keyframes:
  - `OP_SHOT_029` `01:01.50` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_029.png`
  - `OP_SHOT_030` `01:03.50` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_030.png`
- Transition edges:
  - `TE_REF003_028_028_TO_029` OP_SHOT_028->OP_SHOT_029: Nautilus 深蓝剪影 -> 夜城初现
  - `TE_REF003_029_029_TO_030` OP_SHOT_029->OP_SHOT_030: 夜城初现 -> 蓝色地面图案
  - `TE_REF003_030_030_TO_031` OP_SHOT_030->OP_SHOT_031: 蓝色地面图案 -> 夜航飞行器

### 15. `VU_REF003_015_NIGHT_AIRCRAFT_PASS`

- Title: 夜航飞行器短切
- Time range: `01:05.00-01:06.00`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_015_NIGHT_AIRCRAFT_PASS.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_015_NIGHT_AIRCRAFT_PASS`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_015_NIGHT_AIRCRAFT_PASS.mp4`
- Current gate: `blocked_until_keyframes_complete`
- Blocking keyframes: OP_SHOT_031
- Keyframes:
  - `OP_SHOT_031` `01:05.50` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_031.png`
- Transition edges:
  - `TE_REF003_030_030_TO_031` OP_SHOT_030->OP_SHOT_031: 蓝色地面图案 -> 夜航飞行器
  - `TE_REF003_031_031_TO_032` OP_SHOT_031->OP_SHOT_032: 夜航飞行器 -> Nemo 夕景初入

### 16. `VU_REF003_016_NEMO_SUNSET_PROFILE`

- Title: Nemo 夕景船长肖像
- Time range: `01:06.50-01:11.00`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_016_NEMO_SUNSET_PROFILE.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_016_NEMO_SUNSET_PROFILE`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_016_NEMO_SUNSET_PROFILE.mp4`
- Current gate: `blocked_until_keyframes_complete`
- Blocking keyframes: OP_SHOT_032, OP_SHOT_033
- Keyframes:
  - `OP_SHOT_032` `01:06.50` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_032.png`
  - `OP_SHOT_033` `01:09.50` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_033.png`
- Transition edges:
  - `TE_REF003_031_031_TO_032` OP_SHOT_031->OP_SHOT_032: 夜航飞行器 -> Nemo 夕景初入
  - `TE_REF003_032_032_TO_033` OP_SHOT_032->OP_SHOT_033: Nemo 夕景初入 -> Nemo 夕景 hold
  - `TE_REF003_033_033_TO_034` OP_SHOT_033->OP_SHOT_034: Nemo 夕景 hold -> Nadia 庄重正面

### 17. `VU_REF003_017_NADIA_SOLEMN_CLOSE`

- Title: Nadia 庄重正面近景
- Time range: `01:11.50-01:13.00`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_017_NADIA_SOLEMN_CLOSE.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_017_NADIA_SOLEMN_CLOSE`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_017_NADIA_SOLEMN_CLOSE.mp4`
- Current gate: `blocked_until_keyframes_complete`
- Blocking keyframes: OP_SHOT_034
- Keyframes:
  - `OP_SHOT_034` `01:12.00` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_034.png`
- Transition edges:
  - `TE_REF003_033_033_TO_034` OP_SHOT_033->OP_SHOT_034: Nemo 夕景 hold -> Nadia 庄重正面
  - `TE_REF003_034_034_TO_035` OP_SHOT_034->OP_SHOT_035: Nadia 庄重正面 -> Blue Water 宝石象征

### 18. `VU_REF003_018_BLUE_WATER_SYMBOL`

- Title: Blue Water 象征与水下纹理
- Time range: `01:13.50-01:17.00`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_018_BLUE_WATER_SYMBOL.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_018_BLUE_WATER_SYMBOL`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_018_BLUE_WATER_SYMBOL.mp4`
- Current gate: `blocked_until_keyframes_complete`
- Blocking keyframes: OP_SHOT_035, OP_SHOT_036, OP_SHOT_037
- Keyframes:
  - `OP_SHOT_035` `01:13.50` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_035.png`
  - `OP_SHOT_036` `01:15.00` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_036.png`
  - `OP_SHOT_037` `01:16.50` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_037.png`
- Transition edges:
  - `TE_REF003_034_034_TO_035` OP_SHOT_034->OP_SHOT_035: Nadia 庄重正面 -> Blue Water 宝石象征
  - `TE_REF003_035_035_TO_036` OP_SHOT_035->OP_SHOT_036: Blue Water 宝石象征 -> 蓝色符号光
  - `TE_REF003_036_036_TO_037` OP_SHOT_036->OP_SHOT_037: 蓝色符号光 -> 水下蓝色纹理
  - `TE_REF003_037_037_TO_038` OP_SHOT_037->OP_SHOT_038: 水下蓝色纹理 -> 水花爆发

### 19. `VU_REF003_019_WATER_SPLASH_TRANSITION`

- Title: 水花爆发转天空
- Time range: `01:17.50-01:19.50`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_019_WATER_SPLASH_TRANSITION.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_019_WATER_SPLASH_TRANSITION.mp4`
- Current gate: `blocked_until_keyframes_complete`
- Blocking keyframes: OP_SHOT_038, OP_SHOT_039
- Keyframes:
  - `OP_SHOT_038` `01:18.00` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_038.png`
  - `OP_SHOT_039` `01:19.00` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_039.png`
- Transition edges:
  - `TE_REF003_037_037_TO_038` OP_SHOT_037->OP_SHOT_038: 水下蓝色纹理 -> 水花爆发
  - `TE_REF003_038_038_TO_039` OP_SHOT_038->OP_SHOT_039: 水花爆发 -> 水花转蓝天
  - `TE_REF003_039_039_TO_040` OP_SHOT_039->OP_SHOT_040: 水花转蓝天 -> 最终蓝天安全位

### 20. `VU_REF003_020_FINAL_SKY_SAFE_HOLD`

- Title: 最终无字天空 hold
- Time range: `01:19.50-01:23.00`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_020_FINAL_SKY_SAFE_HOLD.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_020_FINAL_SKY_SAFE_HOLD`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_020_FINAL_SKY_SAFE_HOLD.mp4`
- Current gate: `blocked_until_keyframes_complete`
- Blocking keyframes: OP_SHOT_040, OP_SHOT_041
- Keyframes:
  - `OP_SHOT_040` `01:20.00` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_040.png`
  - `OP_SHOT_041` `01:22.00` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_041.png`
- Transition edges:
  - `TE_REF003_039_039_TO_040` OP_SHOT_039->OP_SHOT_040: 水花转蓝天 -> 最终蓝天安全位
  - `TE_REF003_040_040_TO_041` OP_SHOT_040->OP_SHOT_041: 最终蓝天安全位 -> 最终太阳 hold
  - `TE_REF003_041_041_TO_042` OP_SHOT_041->OP_SHOT_042: 最终太阳 hold -> 黑场结尾

### 21. `VU_REF003_021_BLACK_TAIL`

- Title: 黑场尾帧
- Time range: `01:23.50-01:24.44`
- Prompt: `07_shots/video_prompts_by_unit/VU_REF003_021_BLACK_TAIL.md`
- Job dir: `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_021_BLACK_TAIL`
- Output: `08_generation/outputs/video/reference003_segments/VU_REF003_021_BLACK_TAIL.mp4`
- Current gate: `blocked_until_keyframes_complete`
- Blocking keyframes: OP_SHOT_042
- Keyframes:
  - `OP_SHOT_042` `01:23.50` `prompt_ready_reference003` `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_042.png`
- Transition edges:
  - `TE_REF003_041_041_TO_042` OP_SHOT_041->OP_SHOT_042: 最终太阳 hold -> 黑场结尾
