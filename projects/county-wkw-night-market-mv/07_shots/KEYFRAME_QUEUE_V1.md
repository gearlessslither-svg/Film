# Keyframe Queue V1

项目：县城王家卫 / `county-wkw-night-market-mv`  
来源：`07_shots/SHOT_PLAN_DIRECTOR_SEMANTIC_V1.md`  
状态：all 14 V1 keyframes image_ready  
日期：2026-07-08

## Queue Rule

Do not run this as a full batch until these candidate locks are approved or deliberately accepted for V1 testing:

- `BOY_HARDLOCK_V1`
- `GIRL_HARDLOCK_V1`
- `MOTORCYCLE_HARDLOCK_V1`
- environment/color locks from `05_asset_bible/`

Candidate locks now exist in `08_generation/jobs/hardlocks_v1/outputs/`. All prompts generated from this queue must be bilingual Chinese + English. Video prompts must include ambience/sound effects only; no music, no BGM, no soundtrack.

## Items

| ID | Time | Purpose | Location | Mood Ref | Required Locks | Status | Planned Output |
|---|---:|---|---|---|---|---|---|
| KF001 | 0-5s | 夜市梦境入口 | 夜市入口雨后 | LD001 | boy, motorcycle, night-market | image_ready | `08_generation/jobs/keyframes_v1/outputs/KF001_night_market_entry.png` |
| KF002 | 5-10s | 男孩锚点 | LED 雨棚 | LD002 | boy, motorcycle, lighting | image_ready | `08_generation/jobs/keyframes_v1/outputs/KF002_boy_led_awning.png` |
| KF003 | 10-15s | 女孩第一次回头 | 游戏摊 | LD003 | girl, game-booth, lighting | image_ready | `08_generation/jobs/keyframes_v1/outputs/KF003_girl_game_booth.png` |
| KF004 | 15-20s | 啤酒摊错身 | 啤酒/烧烤摊 | LD004 | boy, girl, motorcycle, stall | image_ready | `08_generation/jobs/keyframes_v1/outputs/KF004_beer_stall_crossing.png` |
| KF005 | 20-25s | 机车启动 | LED 雨棚边 | LD002/LD005 | boy, motorcycle | image_ready | `08_generation/jobs/keyframes_v1/outputs/KF005_motorcycle_start.png` |
| KF006 | 25-31s | 小巷低速跟拍 | 夜市后巷 | LD005 | boy, girl, motorcycle, alley | image_ready | `08_generation/jobs/keyframes_v1/outputs/KF006_alley_ride.png` |
| KF007 | 31-37s | 镜中同框 | 修车铺/匿名 karaoke 门口 | LD006 | boy, girl, motorcycle, repair-shop | image_ready | `08_generation/jobs/keyframes_v1/outputs/KF007_repair_reflection.png` |
| KF008 | 37-43s | 女孩被雨布吞没 | 雨棚/游戏摊边 | LD003/LD006 | girl, rain-curtain, lighting | image_ready | `08_generation/jobs/keyframes_v1/outputs/KF008_girl_rain_curtain.png` |
| KF009 | 43-50s | 批发市场对望 | 批发市场门头 | LD007 | boy, girl, motorcycle, wholesale-market | image_ready | `08_generation/jobs/keyframes_v1/outputs/KF009_wholesale_standoff.png` |
| KF010 | 50-55s | 记忆碎片 | 灯泡/车镜/塑料凳 | LD002/LD003/LD004 | motorcycle, props, lighting | image_ready | `08_generation/jobs/keyframes_v1/outputs/KF010_memory_details.png` |
| KF011 | 55-61s | 离开夜市边缘 | 市场边路 | LD005/LD007 | boy, motorcycle, edge-road | image_ready | `08_generation/jobs/keyframes_v1/outputs/KF011_ride_out.png` |
| KF012 | 61-67s | 田野小路 | 县城外田野 | LD008 | boy, motorcycle, field-road | image_ready | `08_generation/jobs/keyframes_v1/outputs/KF012_field_road.png` |
| KF013 | 67-72s | 女孩远去 | 路口/小公交站 | LD008 | girl silhouette, field-road | image_ready | `08_generation/jobs/keyframes_v1/outputs/KF013_girl_departure.png` |
| KF014 | 72-75s | 梦没说完 | 田野路边 | LD008 | boy, motorcycle, field-road | image_ready | `08_generation/jobs/keyframes_v1/outputs/KF014_boy_stops.png` |

## Prompt Seed Pattern

For each formal keyframe, combine:

1. The unit description from `SHOT_PLAN_DIRECTOR_SEMANTIC_V1.md`.
2. The active rules from `05_asset_bible/setting_chapters/00_project_rules.md`.
3. The relevant character / motorcycle / environment lock files.
4. A local avoid list: no readable text, no logos, no luxury vehicle, no cyberpunk megacity, no celebrity likeness, no sexualized girl styling.

## Suggested Next Job

`keyframes_v1` is now generated. Next: director review, optional still-frame fixes, then bilingual image-to-video prompt packaging.
