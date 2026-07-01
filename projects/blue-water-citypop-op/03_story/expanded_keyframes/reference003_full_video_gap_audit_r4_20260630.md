# Reference-003 Full Video Gap Audit R4

- Created: `2026-06-30T20:37:04+08:00`
- Status: `analysis_ready_not_generated_assets`
- Scope: full 21 video units using existing 0.5s sampled reference frames.
- Important: these are candidate reference frames, not final assets. They must be regenerated as clean images before becoming preview/AIGC assets.
- Candidate contact sheet: `01_intake/analysis/reference003_full_video_gap_audit_r4_20260630/reference003_r4_candidate_reference_frames_sheet.jpg`

## Summary

- Existing official keyframe anchors: `42`
- Already generated R3 expansion assets: `11`
- R4 proposed additional generated image candidates: `25`
- R3 was complete only for its batch; it was not a full-video no-more-assets proof.

## Unit Audit

| # | Unit | Time | Anchors | R3 extra | Proposed | Priority | Note |
|---:|---|---|---:|---:|---:|---|---|
| 1 | `VU_REF003_001_BLACK_CLOUD_FADEIN` | 00:00.00-00:02.00 | 2 | 0 | 0 | `P2_review_later` | 2 official anchors cover fade-in; keep reference-video guidance, no new generated image now. |
| 2 | `VU_REF003_002_WHITE_BIRD_SKY` | 00:02.50-00:07.00 | 2 | 0 | 3 | `P1_generate_next_if_expanding_preview` | Needs generated image candidates before expanded still preview. |
| 3 | `VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS` | 00:07.00-00:14.00 | 2 | 0 | 2 | `P1_generate_next_if_expanding_preview` | Needs generated image candidates before expanded still preview. |
| 4 | `VU_REF003_004_AIRCRAFT_BRIEF_REVEAL` | 00:14.50-00:16.50 | 1 | 0 | 2 | `P1_generate_next_if_expanding_preview` | Needs generated image candidates before expanded still preview. |
| 5 | `VU_REF003_005_MAIN_TITLE_SAFE_HOLD` | 00:17.00-00:22.00 | 1 | 0 | 1 | `P2_review_later` | Long no-text/title-safe hold; one mid background state may help PPT preview, but do not over-generate text-zone variants. |
| 6 | `VU_REF003_006_SUN_FLARE_TO_NADIA` | 00:22.50-00:23.50 | 1 | 0 | 2 | `P1_generate_next_if_expanding_preview` | Needs generated image candidates before expanded still preview. |
| 7 | `VU_REF003_007_NADIA_PROFILE_ENTRY` | 00:24.00-00:27.50 | 2 | 1 | 0 | `P2_review_later` | Reference/video-only or static enough for current stage. |
| 8 | `VU_REF003_008_JEAN_INTRO` | 00:28.00-00:30.50 | 1 | 0 | 2 | `P1_generate_next_if_expanding_preview` | Needs generated image candidates before expanded still preview. |
| 9 | `VU_REF003_009_MARIE_KING_MEADOW` | 00:31.00-00:34.00 | 2 | 0 | 1 | `P2_review_later` | Needs generated image candidates before expanded still preview. |
| 10 | `VU_REF003_010_GRANDIS_TRIO_INTRO` | 00:34.50-00:37.50 | 2 | 0 | 2 | `P1_generate_next_if_expanding_preview` | Needs generated image candidates before expanded still preview. |
| 11 | `VU_REF003_011_RUNNING_MONTAGE` | 00:38.00-00:47.50 | 6 | 7 | 0 | `P3_reference_video_or_already_handled` | Already R3-generated 6 running montage assets and deliberately collapsed OP_SHOT_021 repetition. |
| 12 | `VU_REF003_012_GRANDIS_VEHICLE_ACTION` | 00:48.00-00:51.50 | 3 | 3 | 0 | `P3_reference_video_or_already_handled` | Already R3-generated Grandis/vehicle start/end bridge assets and deliberately collapsed OP_SHOT_025 repetition. |
| 13 | `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS` | 00:52.00-01:01.00 | 3 | 0 | 3 | `P1_generate_next_if_expanding_preview` | Needs generated image candidates before expanded still preview. |
| 14 | `VU_REF003_014_NIGHT_CITY_BLUE_GRID` | 01:01.50-01:04.50 | 2 | 0 | 1 | `P2_review_later` | Needs generated image candidates before expanded still preview. |
| 15 | `VU_REF003_015_NIGHT_AIRCRAFT_PASS` | 01:05.00-01:06.00 | 1 | 0 | 2 | `P1_generate_next_if_expanding_preview` | Needs generated image candidates before expanded still preview. |
| 16 | `VU_REF003_016_NEMO_SUNSET_PROFILE` | 01:06.50-01:11.00 | 2 | 0 | 0 | `P3_reference_video_or_already_handled` | Director marked Nemo portrait as one-take/repetitive; keep existing start/end plus precise prompt/video reference. |
| 17 | `VU_REF003_017_NADIA_SOLEMN_CLOSE` | 01:11.50-01:13.00 | 1 | 0 | 0 | `P2_review_later` | Short solemn close-up with accepted R1 repair; no new still unless face quality is rejected. |
| 18 | `VU_REF003_018_BLUE_WATER_SYMBOL` | 01:13.50-01:17.00 | 3 | 0 | 1 | `P2_review_later` | Needs generated image candidates before expanded still preview. |
| 19 | `VU_REF003_019_WATER_SPLASH_TRANSITION` | 01:17.50-01:19.50 | 2 | 0 | 2 | `P1_generate_next_if_expanding_preview` | Needs generated image candidates before expanded still preview. |
| 20 | `VU_REF003_020_FINAL_SKY_SAFE_HOLD` | 01:19.50-01:23.00 | 2 | 0 | 1 | `P2_review_later` | Needs generated image candidates before expanded still preview. |
| 21 | `VU_REF003_021_BLACK_TAIL` | 01:23.50-01:24.44 | 1 | 0 | 0 | `P3_reference_video_or_already_handled` | Black tail, no generated asset needed. |

## Proposed Candidate Frames

### 02. `VU_REF003_002_WHITE_BIRD_SKY` — 白鸟入画与蓝天滑翔
- `00:03.50` delta `3.4` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0008.jpg`
- `00:06.00` delta `4.86` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0013.jpg`
- `00:04.50` delta `6.78` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0010.jpg`

### 03. `VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS` — 白鸟字幕安全位与云层增长
- `00:09.50` delta `1.06` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0020.jpg`
- `00:12.50` delta `36.23` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0026.jpg`

### 04. `VU_REF003_004_AIRCRAFT_BRIEF_REVEAL` — 飞行器短暂露出
- `00:16.00` delta `89.98` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0033.jpg`
- `00:14.50` delta `86.42` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0030.jpg`

### 05. `VU_REF003_005_MAIN_TITLE_SAFE_HOLD` — 主标题功能位无字 hold
- `00:20.00` delta `15.84` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0041.jpg`

### 06. `VU_REF003_006_SUN_FLARE_TO_NADIA` — 太阳光转 Nadia
- `00:23.50` delta `27.49` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0048.jpg`
- `00:22.50` delta `20.32` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0046.jpg`

### 08. `VU_REF003_008_JEAN_INTRO` — Jean 帽子与少年发明家入场
- `00:30.50` delta `83.69` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0062.jpg`
- `00:28.50` delta `71.54` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0058.jpg`

### 09. `VU_REF003_009_MARIE_KING_MEADOW` — Marie 与 King 草地段
- `00:32.50` delta `12.87` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0066.jpg`

### 10. `VU_REF003_010_GRANDIS_TRIO_INTRO` — Grandis 三人组介绍
- `00:34.50` delta `82.11` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0070.jpg`
- `00:37.50` delta `68.87` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0076.jpg`

### 13. `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS` — Nautilus 海底光束段
- `00:53.50` delta `9.11` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0108.jpg`
- `00:56.50` delta `10.62` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0114.jpg`
- `00:59.50` delta `13.58` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0120.jpg`

### 14. `VU_REF003_014_NIGHT_CITY_BLUE_GRID` — 夜城与蓝色地面图案
- `01:02.50` delta `12.14` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0126.jpg`

### 15. `VU_REF003_015_NIGHT_AIRCRAFT_PASS` — 夜航飞行器短切
- `01:05.00` delta `49.72` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0131.jpg`
- `01:06.00` delta `17.55` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0133.jpg`

### 18. `VU_REF003_018_BLUE_WATER_SYMBOL` — Blue Water 象征与水下纹理
- `01:15.50` delta `51.29` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0152.jpg`

### 19. `VU_REF003_019_WATER_SPLASH_TRANSITION` — 水花爆发转天空
- `01:18.50` delta `72.56` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0158.jpg`
- `01:19.50` delta `42.83` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0160.jpg`

### 20. `VU_REF003_020_FINAL_SKY_SAFE_HOLD` — 最终无字天空 hold
- `01:21.00` delta `23.32` source `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0163.jpg`

## Next Action

Before more image generation, convert the P1 rows into a bounded R4 generation job with identity/setting locks. Start with the P1 units, then review P2 only if the expanded preview still feels thin.
