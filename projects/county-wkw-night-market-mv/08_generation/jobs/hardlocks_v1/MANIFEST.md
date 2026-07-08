# Generation Job Manifest - hardlocks_v1

Project: `county-wkw-night-market-mv`  
Job type: provisional-to-dedicated hardlock generation  
Created: 2026-07-08  
Target count: 4 images  
Target output folder: `08_generation/jobs/hardlocks_v1/outputs/`

## Purpose

Create dedicated visual locks before formal MV keyframe generation. The first lookdev batch is approved as mood direction, but it is not enough to guarantee character and vehicle continuity across the full MV.

## Inputs

- `04_lookdev/LOOKDEV_MOOD_FRAMES_V1.md`
- `08_generation/jobs/lookdev_moodframes_v1/lookdev_moodframes_v1_contact_sheet.png`
- `08_generation/jobs/lookdev_moodframes_v1/QA.md`
- `05_asset_bible/characters/BOY_LOCK_V1.md`
- `05_asset_bible/characters/GIRL_LOCK_V1.md`
- `05_asset_bible/props/MOTORCYCLE_LOCK_V1.md`
- `05_asset_bible/continuity/LOOKDEV_CONTINUITY_V1.md`

## Items

| Item | Target | Status | Planned Output |
|---|---|---|---|
| HL001 | Boy face/body lock sheet | image_ready_candidate | `outputs/HL001_boy_lock_sheet.png` |
| HL002 | Girl face/body lock sheet | image_ready_candidate | `outputs/HL002_girl_lock_sheet.png` |
| HL003 | Used motorcycle lock sheet | image_ready_candidate | `outputs/HL003_motorcycle_lock_sheet.png` |
| HL004 | Two-character distance/reflection lock | image_ready_candidate | `outputs/HL004_two_character_distance_reflection_lock.png` |

## Run Rule

Generated as a small V1 candidate batch. Use for `keyframes_v1` only after director approval or after a deliberate decision to proceed with V1 locks.

## QA Checks

- Lock sheet has no readable text, labels, logos, watermarks, or subtitles inside the image.
- Boy/girl read as adults in their early 20s.
- Girl is grounded and non-sexualized.
- Motorcycle is ordinary and used, not luxury.
- The visual language still feels like county-town neon romance, not glossy cyberpunk.

## Generated Outputs

- Contact sheet: `hardlocks_v1_contact_sheet.png`
- QA record: `QA.md`
