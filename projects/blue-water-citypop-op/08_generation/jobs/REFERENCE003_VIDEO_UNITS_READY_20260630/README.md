# Reference-003 Video Unit Generation Readiness

- Project: `blue-water-citypop-op`
- Rebuilt: `2026-06-30T15:49:56+08:00`
- Source reference: `reference-003-full-op-2160p`
- Purpose: prepare and verify the video-stage handoff after keyframes.

## Current Gate

- Keyframes: 42/42 official reference-003 QA pass; 0 still prompt-ready.
- Video units: 21/21 have all required keyframes QA-passed; 0/21 are blocked until remaining keyframes finish.
- Transition edges: 41 declared and must be preserved in order.

Do not start full video generation until all 42 keyframes are `generated_reference003_qa_pass` and this script reports 21/21 units ready.

## Unit Readiness

| # | Unit | Time | Status | Keyframes | Blockers |
|---:|---|---|---|---|---|
| 1 | `VU_REF003_001_BLACK_CLOUD_FADEIN` | 00:00.00-00:02.00 | `ready_for_video_generation` | OP_SHOT_001, OP_SHOT_002 | - |
| 2 | `VU_REF003_002_WHITE_BIRD_SKY` | 00:02.50-00:07.00 | `ready_for_video_generation` | OP_SHOT_003, OP_SHOT_004 | - |
| 3 | `VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS` | 00:07.00-00:14.00 | `ready_for_video_generation` | OP_SHOT_005, OP_SHOT_006 | - |
| 4 | `VU_REF003_004_AIRCRAFT_BRIEF_REVEAL` | 00:14.50-00:16.50 | `ready_for_video_generation` | OP_SHOT_007 | - |
| 5 | `VU_REF003_005_MAIN_TITLE_SAFE_HOLD` | 00:17.00-00:22.00 | `ready_for_video_generation` | OP_SHOT_008 | - |
| 6 | `VU_REF003_006_SUN_FLARE_TO_NADIA` | 00:22.50-00:23.50 | `ready_for_video_generation` | OP_SHOT_009 | - |
| 7 | `VU_REF003_007_NADIA_PROFILE_ENTRY` | 00:24.00-00:27.50 | `ready_for_video_generation` | OP_SHOT_010, OP_SHOT_011 | - |
| 8 | `VU_REF003_008_JEAN_INTRO` | 00:28.00-00:30.50 | `ready_for_video_generation` | OP_SHOT_012 | - |
| 9 | `VU_REF003_009_MARIE_KING_MEADOW` | 00:31.00-00:34.00 | `ready_for_video_generation` | OP_SHOT_013, OP_SHOT_014 | - |
| 10 | `VU_REF003_010_GRANDIS_TRIO_INTRO` | 00:34.50-00:37.50 | `ready_for_video_generation` | OP_SHOT_015, OP_SHOT_016 | - |
| 11 | `VU_REF003_011_RUNNING_MONTAGE` | 00:38.00-00:47.50 | `ready_for_video_generation` | OP_SHOT_017, OP_SHOT_018, OP_SHOT_019, OP_SHOT_020, OP_SHOT_021, OP_SHOT_022 | - |
| 12 | `VU_REF003_012_GRANDIS_VEHICLE_ACTION` | 00:48.00-00:51.50 | `ready_for_video_generation` | OP_SHOT_023, OP_SHOT_024, OP_SHOT_025 | - |
| 13 | `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS` | 00:52.00-01:01.00 | `ready_for_video_generation` | OP_SHOT_026, OP_SHOT_027, OP_SHOT_028 | - |
| 14 | `VU_REF003_014_NIGHT_CITY_BLUE_GRID` | 01:01.50-01:04.50 | `ready_for_video_generation` | OP_SHOT_029, OP_SHOT_030 | - |
| 15 | `VU_REF003_015_NIGHT_AIRCRAFT_PASS` | 01:05.00-01:06.00 | `ready_for_video_generation` | OP_SHOT_031 | - |
| 16 | `VU_REF003_016_NEMO_SUNSET_PROFILE` | 01:06.50-01:11.00 | `ready_for_video_generation` | OP_SHOT_032, OP_SHOT_033 | - |
| 17 | `VU_REF003_017_NADIA_SOLEMN_CLOSE` | 01:11.50-01:13.00 | `ready_for_video_generation` | OP_SHOT_034 | - |
| 18 | `VU_REF003_018_BLUE_WATER_SYMBOL` | 01:13.50-01:17.00 | `ready_for_video_generation` | OP_SHOT_035, OP_SHOT_036, OP_SHOT_037 | - |
| 19 | `VU_REF003_019_WATER_SPLASH_TRANSITION` | 01:17.50-01:19.50 | `ready_for_video_generation` | OP_SHOT_038, OP_SHOT_039 | - |
| 20 | `VU_REF003_020_FINAL_SKY_SAFE_HOLD` | 01:19.50-01:23.00 | `ready_for_video_generation` | OP_SHOT_040, OP_SHOT_041 | - |
| 21 | `VU_REF003_021_BLACK_TAIL` | 01:23.50-01:24.44 | `ready_for_video_generation` | OP_SHOT_042 | - |

## Rebuild Command

`python3 08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/rebuild_reference003_video_unit_readiness.py`

## Files

- Machine manifest: `08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/manifest.json`
- Scan table: `08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/video_unit_readiness.csv`
- QA checklist: `08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/qa/VIDEO_UNIT_QA_CHECKLIST.md`
- Rebuild script: `08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/rebuild_reference003_video_unit_readiness.py`
