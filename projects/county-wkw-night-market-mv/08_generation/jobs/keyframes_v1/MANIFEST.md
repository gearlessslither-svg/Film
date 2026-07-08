# Generation Job Manifest - keyframes_v1

Project: `county-wkw-night-market-mv`  
Job type: formal keyframe batch  
Created: 2026-07-08  
Target count: 14 images  
Target output folder: `08_generation/jobs/keyframes_v1/outputs/`

## Purpose

Generate the full V1 formal MV keyframe backbone from the director semantic shot plan.

## Inputs

- `07_shots/SHOT_PLAN_DIRECTOR_SEMANTIC_V1.md`
- `07_shots/KEYFRAME_QUEUE_V1.md`
- `08_generation/jobs/hardlocks_v1/outputs/HL001_boy_lock_sheet.png`
- `08_generation/jobs/hardlocks_v1/outputs/HL002_girl_lock_sheet.png`
- `08_generation/jobs/hardlocks_v1/outputs/HL003_motorcycle_lock_sheet.png`
- `08_generation/jobs/hardlocks_v1/outputs/HL004_two_character_distance_reflection_lock.png`
- `05_asset_bible/`

## Items

| Item | Source Unit | Purpose | Status | Output |
|---|---|---|---|---|
| KF001 | DS01 | Night-market entry | image_ready | `outputs/KF001_night_market_entry.png` |
| KF002 | DS02 | Boy and motorcycle anchor | image_ready | `outputs/KF002_boy_led_awning.png` |
| KF003 | DS03 | Girl game-booth anchor | image_ready | `outputs/KF003_girl_game_booth.png` |
| KF004 | DS04 | Beer-stall crossing | image_ready | `outputs/KF004_beer_stall_crossing.png` |
| KF005 | DS05 | Motorcycle start detail | image_ready | `outputs/KF005_motorcycle_start.png` |
| KF006 | DS06 | Wet alley ride | image_ready | `outputs/KF006_alley_ride.png` |
| KF007 | DS07 | Repair-shop reflection relationship | image_ready | `outputs/KF007_repair_reflection.png` |
| KF008 | DS08 | Girl behind rain curtain | image_ready | `outputs/KF008_girl_rain_curtain.png` |
| KF009 | DS09 | Wholesale-market standoff | image_ready | `outputs/KF009_wholesale_standoff.png` |
| KF010 | DS10 | Memory-detail insert | image_ready | `outputs/KF010_memory_details.png` |
| KF011 | DS11 | Ride out from night market | image_ready | `outputs/KF011_ride_out.png` |
| KF012 | DS12 | Field road | image_ready | `outputs/KF012_field_road.png` |
| KF013 | DS13 | Girl departure | image_ready | `outputs/KF013_girl_departure.png` |
| KF014 | DS14 | Boy stops | image_ready | `outputs/KF014_boy_stops.png` |

## QA Checks

- Still feels like county-town romance, not glossy cyberpunk.
- Boy/girl/motorcycle stay close enough to `hardlocks_v1`.
- No readable signage, labels, logos, license plates, subtitles, or watermarks.
- Girl remains adult, grounded, and non-sexualized.
- Frames are usable as formal keyframes, not only abstract mood art.

## Generated Outputs

- Contact sheet: `keyframes_v1_contact_sheet.png`
- QA record: `QA.md`
