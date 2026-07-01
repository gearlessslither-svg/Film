# Reference-003 Adaptive Frame Promotion R5

- Created: `2026-06-30T20:57:23+08:00`
- Status: `analysis_ready_not_generated_assets`
- Method: shot/video-unit-level adaptive density + novelty-to-existing-anchor + film-function promotion.
- Candidate contact sheet: `01_intake/analysis/reference003_adaptive_frame_audit_r5_20260630/reference003_r5_adaptive_candidates_sheet.jpg`
- R4 candidates: `25`
- R5 selected candidates: `21`
- R5 P1 small-batch candidates: `13`

## Important Limitation

This session has no `ffmpeg`, `cv2`, `moviepy`, or `av` decoder available. R5 therefore does not extract fresh 8-12fps frames from the mp4. It uses existing 0.5s full-video sampled frames plus prior dense/R3 records, and marks units that need denser extraction before final generation.

## Unit Decisions

| # | Unit | Class | Desired FPS | Available FPS | New Cand. | Priority | Note |
|---:|---|---|---:|---:|---:|---|---|
| 1 | `VU_REF003_001_BLACK_CLOUD_FADEIN` | `low_change` | 2 | 2.0 | 0 | `P4_no_new_asset_now` | No new image asset needed at current preview density. |
| 2 | `VU_REF003_002_WHITE_BIRD_SKY` | `high_change` | 6 | 2.0 | 2 | `P1_generate_next_small_batch` | Promote these only after prompt/identity-lock job is created and pure images are generated. |
| 3 | `VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS` | `moderate_long` | 4 | 2.0 | 1 | `P2_review_after_p1` | Promote these only after prompt/identity-lock job is created and pure images are generated. |
| 4 | `VU_REF003_004_AIRCRAFT_BRIEF_REVEAL` | `high_change_short` | 8 | 2.0 | 2 | `P1_generate_next_small_batch` | Promote these only after prompt/identity-lock job is created and pure images are generated. |
| 5 | `VU_REF003_005_MAIN_TITLE_SAFE_HOLD` | `moderate` | 4 | 2.0 | 1 | `P2_review_after_p1` | Promote these only after prompt/identity-lock job is created and pure images are generated. |
| 6 | `VU_REF003_006_SUN_FLARE_TO_NADIA` | `high_change_short` | 8 | 2.0 | 1 | `P2_review_after_p1` | Promote these only after prompt/identity-lock job is created and pure images are generated. |
| 7 | `VU_REF003_007_NADIA_PROFILE_ENTRY` | `high_change` | 6 | 2.0 | 1 | `P2_review_after_p1` | Promote these only after prompt/identity-lock job is created and pure images are generated. |
| 8 | `VU_REF003_008_JEAN_INTRO` | `high_change_short` | 8 | 2.0 | 2 | `P1_generate_next_small_batch` | Promote these only after prompt/identity-lock job is created and pure images are generated. |
| 9 | `VU_REF003_009_MARIE_KING_MEADOW` | `low_change` | 2 | 2.0 | 1 | `P2_review_after_p1` | Promote these only after prompt/identity-lock job is created and pure images are generated. |
| 10 | `VU_REF003_010_GRANDIS_TRIO_INTRO` | `high_change` | 6 | 2.0 | 2 | `P1_generate_next_small_batch` | Promote these only after prompt/identity-lock job is created and pure images are generated. |
| 11 | `VU_REF003_011_RUNNING_MONTAGE` | `already_handled` | 0 | 2.0 | 0 | `P3_reference_video_or_already_handled` | Already covered by R3 or intentionally collapsed to reference video. |
| 12 | `VU_REF003_012_GRANDIS_VEHICLE_ACTION` | `already_handled` | 0 | 2.0 | 0 | `P3_reference_video_or_already_handled` | Already covered by R3 or intentionally collapsed to reference video. |
| 13 | `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS` | `moderate_long` | 4 | 2.0 | 3 | `P1_generate_next_small_batch` | Promote these only after prompt/identity-lock job is created and pure images are generated. |
| 14 | `VU_REF003_014_NIGHT_CITY_BLUE_GRID` | `low_change` | 2 | 2.0 | 1 | `P2_review_after_p1` | Promote these only after prompt/identity-lock job is created and pure images are generated. |
| 15 | `VU_REF003_015_NIGHT_AIRCRAFT_PASS` | `high_change_short` | 8 | 2.0 | 1 | `P2_review_after_p1` | Promote these only after prompt/identity-lock job is created and pure images are generated. |
| 16 | `VU_REF003_016_NEMO_SUNSET_PROFILE` | `collapse_reference_video` | 0 | 2.0 | 0 | `P3_reference_video_or_already_handled` | Already covered by R3 or intentionally collapsed to reference video. |
| 17 | `VU_REF003_017_NADIA_SOLEMN_CLOSE` | `short_accepted_hold` | 1 | 2.0 | 0 | `P4_no_new_asset_now` | No new image asset needed at current preview density. |
| 18 | `VU_REF003_018_BLUE_WATER_SYMBOL` | `high_change` | 6 | 2.0 | 1 | `P2_review_after_p1` | Promote these only after prompt/identity-lock job is created and pure images are generated. |
| 19 | `VU_REF003_019_WATER_SPLASH_TRANSITION` | `high_change_short` | 8 | 2.0 | 2 | `P1_generate_next_small_batch` | Promote these only after prompt/identity-lock job is created and pure images are generated. |
| 20 | `VU_REF003_020_FINAL_SKY_SAFE_HOLD` | `moderate` | 4 | 2.0 | 0 | `P4_no_new_asset_now` | No new image asset needed at current preview density. |
| 21 | `VU_REF003_021_BLACK_TAIL` | `collapse_reference_video` | 0 | 1.06 | 0 | `P3_reference_video_or_already_handled` | Already covered by R3 or intentionally collapsed to reference video. |

## Selected Candidate Reference Frames

### 02. `VU_REF003_002_WHITE_BIRD_SKY` — 白鸟入画与蓝天滑翔
Required locks: `white_bird, opening_sky_clouds`
- `00:07.00` score `39.08` novelty `6.03`: White bird glide changes screen position/scale within a long sky movement; useful middle/final action anchor without generating every frame.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0015.jpg`
- `00:03.50` score `34.11` novelty `10.28`: White bird glide changes screen position/scale within a long sky movement; useful middle/final action anchor without generating every frame.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0008.jpg`

### 03. `VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS` — 白鸟字幕安全位与云层增长
Required locks: `white_bird, opening_sky_clouds`
- `00:14.00` score `195.45` novelty `93.49`: Cloud/bird/title-safe composition changes over a long no-text sky section; adds clean sky state for preview and AIGC prompt.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0029.jpg`

### 04. `VU_REF003_004_AIRCRAFT_BRIEF_REVEAL` — 飞行器短暂露出
Required locks: `jean_aircraft, opening_sky_clouds`
- `00:16.00` score `257.88` novelty `104.86`: Brief aircraft reveal is a fast prop/camera state change; current single anchor does not cover entry and exit/reveal phase.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0033.jpg`
- `00:14.50` score `253.02` novelty `88.84`: Brief aircraft reveal is a fast prop/camera state change; current single anchor does not cover entry and exit/reveal phase.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0030.jpg`

### 05. `VU_REF003_005_MAIN_TITLE_SAFE_HOLD` — 主标题功能位无字 hold
Required locks: `none`
- `00:17.00` score `70.47` novelty `19.85`: 主标题功能位无字 hold: large timeline gap between existing anchors; visually different from nearest existing anchor; local motion/color change peak
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0035.jpg`

### 06. `VU_REF003_006_SUN_FLARE_TO_NADIA` — 太阳光转 Nadia
Required locks: `nadia, opening_sky_clouds`
- `00:23.50` score `100.82` novelty `27.5`: Transition edge from sun flare into Nadia needs a clean bridge frame so AIGC does not invent the cut or lose Nadia lock.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0048.jpg`

### 07. `VU_REF003_007_NADIA_PROFILE_ENTRY` — Nadia 侧脸入场到近景
Required locks: `none`
- `00:27.50` score `195.2` novelty `56.38`: Nadia 侧脸入场到近景: scene-boundary / hard visual turn; visually different from nearest existing anchor; local motion/color change peak
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0056.jpg`

### 08. `VU_REF003_008_JEAN_INTRO` — Jean 帽子与少年发明家入场
Required locks: `jean`
- `00:30.50` score `212.28` novelty `66.48`: Jean intro has fast entry/pose changes; extra frame carries different body/hat/face orientation and protects Jean identity.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0062.jpg`
- `00:28.50` score `206.16` novelty `74.18`: Jean intro has fast entry/pose changes; extra frame carries different body/hat/face orientation and protects Jean identity.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0058.jpg`

### 09. `VU_REF003_009_MARIE_KING_MEADOW` — Marie 与 King 草地段
Required locks: `marie, king, meadow_child_animal_beat`
- `00:31.00` score `131.91` novelty `45.01`: Marie 与 King 草地段: scene-boundary / hard visual turn; visually different from nearest existing anchor; local motion/color change peak
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0063.jpg`

### 10. `VU_REF003_010_GRANDIS_TRIO_INTRO` — Grandis 三人组介绍
Required locks: `grandis, sanson, hanson`
- `00:34.50` score `201.54` novelty `77.68`: Grandis trio introduction changes blocking and group pose; extra frame protects three-person identity and screen direction.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0070.jpg`
- `00:37.50` score `162.94` novelty `65.93`: Grandis trio introduction changes blocking and group pose; extra frame protects three-person identity and screen direction.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0076.jpg`

### 13. `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS` — Nautilus 海底光束段
Required locks: `nautilus, undersea_nautilus_space`
- `00:52.00` score `195.54` novelty `77.43`: Long undersea Nautilus light-pass has distinct submarine/lighting positions; extra frames preserve scale and light-beam progression.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0105.jpg`
- `01:00.50` score `51.93` novelty `16.69`: Long undersea Nautilus light-pass has distinct submarine/lighting positions; extra frames preserve scale and light-beam progression.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0122.jpg`
- `00:57.00` score `48.17` novelty `16.5`: Long undersea Nautilus light-pass has distinct submarine/lighting positions; extra frames preserve scale and light-beam progression.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0115.jpg`

### 14. `VU_REF003_014_NIGHT_CITY_BLUE_GRID` — 夜城与蓝色地面图案
Required locks: `blue_grid_geometry`
- `01:02.50` score `64.23` novelty `23.72`: 夜城与蓝色地面图案: large timeline gap between existing anchors; visually different from nearest existing anchor
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0126.jpg`

### 15. `VU_REF003_015_NIGHT_AIRCRAFT_PASS` — 夜航飞行器短切
Required locks: `jean_aircraft, night_city_blue_grid`
- `01:05.00` score `67.63` novelty `10.26`: Night aircraft pass is a short fast prop movement; an extra end/start state prevents the craft from popping or redesigning.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0131.jpg`

### 18. `VU_REF003_018_BLUE_WATER_SYMBOL` — Blue Water 象征与水下纹理
Required locks: `blue_water_pendant, blue_grid_geometry`
- `01:14.00` score `134.09` novelty `40.79`: Blue Water 象征与水下纹理: scene-boundary / hard visual turn; visually different from nearest existing anchor; local motion/color change peak
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0149.jpg`

### 19. `VU_REF003_019_WATER_SPLASH_TRANSITION` — 水花爆发转天空
Required locks: `water_burst_transition`
- `01:18.50` score `198.99` novelty `66.74`: Water burst transition has materially different splash/sky states; extra anchor helps preserve transition logic.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0158.jpg`
- `01:17.50` score `145.06` novelty `53.39`: Water burst transition has materially different splash/sky states; extra anchor helps preserve transition logic.
  - source: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0156.jpg`

## Effect Compared With R4

- R4 used the available 0.5s full-video samples as a broad gap finder and proposed 25 candidates.
- R5 reduces this to a smaller, shot-aware candidate set by subtracting already-covered R3 units, collapsing slow/accepted holds, scoring novelty against existing anchors, and requiring lock-aware `difference_reason` for each promoted candidate.
- R5 also explicitly marks where the current evidence is insufficient because desired per-unit analysis FPS is higher than the available sample FPS.

## Next Action

Create a bounded R5 image-generation job from only the `P1_generate_next_small_batch` candidates. Do not treat these reference screenshots as assets until regenerated as pure images and QA-passed.
