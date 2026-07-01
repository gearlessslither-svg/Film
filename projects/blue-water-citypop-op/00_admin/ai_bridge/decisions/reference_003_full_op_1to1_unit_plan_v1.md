# Reference 003 Full OP 1:1 Unit Plan v1

Updated: 2026-06-30 04:40 Asia/Shanghai

## Direct Answer

The project was not yet truly based on this full `[2160P] 蓝宝石之谜OP 修复..mp4` video for a 1:1 remake. The previous active work used the shorter `reference-002-opening` evidence package for the first 23 seconds. The seven images generated immediately before this decision are therefore only abandoned trial material, not accepted production keyframes.

This file makes `reference-003-full-op-2160p` the new authoritative reference for full-OP remake planning.

## Source Evidence

- Source video: `/Users/jaychoupp/Library/Containers/com.tencent.qq/Data/Downloads/[2160P] 蓝宝石之谜OP 修复..mp4`
- Project copy: `01_intake/references/reference-003-full-op-2160p.mp4`
- Manifest: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/manifest.json`
- Contact sheet: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/contact_sheets/reference-003-full-op-2160p_contact_sheet_2fps.jpg`
- Section sheets:
  - `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/contact_sheets/sections/00_00_24.jpg`
  - `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/contact_sheets/sections/01_24_48.jpg`
  - `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/contact_sheets/sections/02_48_66.jpg`
  - `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/contact_sheets/sections/03_66_84.jpg`
- Frame-stack roughcut: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/roughcuts/reference-003-full-op-2160p_frame_stack_2fps.mp4`
- GPT packet: `00_admin/ai_bridge/packets/20260630_043518_reference-003-full-op-2160p_pixel_remake.json`

## Media Check

- Duration: 84.437333 seconds
- Video: H.264, 1440 x 1080, ~23.976 fps, 2024 frames
- Sampled review frames: 169 at 2fps
- Full decode: pass
- Frame-stack roughcut decode: pass

## 1:1 Unit Table

| Unit | Time | Reference Function | Remake Rule |
|---|---:|---|---|
| `VU_REF003_001_BLACK_CLOUD_FADEIN` | 00:00.00-00:02.00 | black/fade to bright cloud and blue sky | recreate fade/sky function; no text |
| `VU_REF003_002_WHITE_BIRD_SKY` | 00:02.50-00:07.00 | white bird enters and glides over blue sky | bird motion leads; replace lyric/subtitle area with clean sky |
| `VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS` | 00:07.00-00:14.00 | bird continues under credits; cloud bank grows | no generated credits; preserve negative space and cloud rhythm |
| `VU_REF003_004_AIRCRAFT_BRIEF_REVEAL` | 00:14.50-00:16.50 | aircraft wing/plane short reveal | brief scale-controlled reveal only; no long chase |
| `VU_REF003_005_MAIN_TITLE_SAFE_HOLD` | 00:17.00-00:22.00 | main title/logo hold over sky | no generated title/logo; use clean title-safe sky composition |
| `VU_REF003_006_SUN_FLARE_TO_NADIA` | 00:22.50-00:23.50 | sky/sun flare transition | light bloom prepares character entry |
| `VU_REF003_007_NADIA_PROFILE_ENTRY` | 00:24.00-00:27.50 | Nadia profile, look change, close-up | Nadia C lock, age-safe; keep side/profile timing |
| `VU_REF003_008_JEAN_INTRO` | 00:28.00-00:30.50 | Jean hat/face introduction | Jean 14-year-old inventor lock; no text |
| `VU_REF003_009_MARIE_KING_MEADOW` | 00:31.00-00:34.00 | Marie/King meadow gag and smile | child-safe, bright meadow, no subtitles |
| `VU_REF003_010_GRANDIS_TRIO_INTRO` | 00:34.50-00:37.50 | Grandis trio pose/close-ups | adult trio intro; theatrical but grounded |
| `VU_REF003_011_RUNNING_MONTAGE` | 00:38.00-00:47.50 | Nadia/Jean/Marie/group running montage | preserve beat order and left-right run direction |
| `VU_REF003_012_GRANDIS_VEHICLE_ACTION` | 00:48.00-00:51.50 | Grandis/vehicle action and group lineup | fast action bridge into Nautilus section |
| `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS` | 00:52.00-01:01.00 | Nautilus undersea passes under credits | no generated credits; preserve underwater shaft-light motion |
| `VU_REF003_014_NIGHT_CITY_BLUE_GRID` | 01:01.50-01:04.50 | night city and glowing blue ground diagram | keep blue grid/city relation; no readable text |
| `VU_REF003_015_NIGHT_AIRCRAFT_PASS` | 01:05.00-01:06.00 | aircraft night pass | short dark vehicle pass, scale controlled |
| `VU_REF003_016_NEMO_SUNSET_PROFILE` | 01:06.50-01:11.00 | Nemo/captain profile at sunset | adult captain portrait, no karaoke/credit text |
| `VU_REF003_017_NADIA_SOLEMN_CLOSE` | 01:11.50-01:13.00 | Nadia solemn front close-up | Nadia C lock, age-safe, serious portrait |
| `VU_REF003_018_BLUE_WATER_SYMBOL` | 01:13.50-01:17.00 | Blue Water jewel / Nadia overlay / underwater texture | replace NHK/credits with clean symbol composition |
| `VU_REF003_019_WATER_SPLASH_TRANSITION` | 01:17.50-01:19.50 | watery/icy burst to sky | dynamic water transition; no text |
| `VU_REF003_020_FINAL_SKY_SAFE_HOLD` | 01:19.50-01:23.00 | NHK end card over blue sky/sun | replace NHK with clean final sky/logo-safe hold |
| `VU_REF003_021_BLACK_TAIL` | 01:23.50-01:24.44 | black tail | editorial black, no generated art needed |

## Production Consequences

- `reference-003-full-op-2160p` supersedes `reference-002-opening` as the active full-project timing source.
- The old `VU_REF002_*` opening units are no longer sufficient for a 1:1 remake.
- The existing 42 keyframes should be treated as a style/identity library only until they are remapped to this full unit table.
- The generated `REFERENCE002_REGEN_20260630` output is not accepted and should not be callback-filled into the board.
- All generated frames must remove/replace original readable credits, NHK marks, lyrics, subtitles, and title lettering while preserving shot timing, composition function, and motion role.

## Next Required Step

Rewrite `video_units.json`, `transition_edges.json`, `camera_manifest.json`, `shot_list.csv`, and affected prompts from this full-OP table before producing new official keyframes. Do not continue generating from `VU_REF002_*`.
