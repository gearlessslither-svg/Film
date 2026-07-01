# Reference 002 Opening Unit Recut v1

Updated: 2026-06-30T02:50:27+08:00

## Decision

Use `reference-002-opening` as active timing evidence for the first 23 seconds. The previous `opening_24s_onetake_previs.mp4` remains a useful Blender/camera experiment, but it is not accepted as the remake timing because it over-continuizes the opening and gives the aircraft too much screen importance.

## Shot / Unit Table

| Time | Active unit | Keyframes | Method | Notes |
|---:|---|---|---|---|
| 00:00-00:04.50 | `VU_REF002_001_WHITE_BIRD_OPENING` | `OP_SHOT_001`, `OP_SHOT_002` | image keyframes + AIGC video | White bird starts immediately and continues as the opening subject. |
| 00:05.00-00:08.50 | `VU_REF002_002_BIRD_CREDIT_SAFE_SKY` | `OP_SHOT_003` | still/roughcut hold, optional subtle AIGC drift | Preserve negative space where reference text exists, but generate no text. |
| 00:09.00-00:14.00 | `VU_REF002_003_CLOUD_BANK_AIRCRAFT_REVEAL` | `OP_SHOT_004`, `OP_SHOT_005` | simple Blender scale check + keyframes, then AIGC motion | Cloud expansion dominates; aircraft appears briefly only. |
| 00:14.50-00:21.00 | `VU_REF002_004_TITLE_SAFE_HOLD_TO_FLARE` | `OP_SHOT_006` | frame-stack timing + AIGC light drift/flare | Replace title/logo with clean no-text title-safe sky. |
| 00:21.50-00:23.00 | `VU_REF002_005_NADIA_CLOSEUP_ENTRY` | `OP_SHOT_007` | keyframe + AIGC character motion | Nadia enters after the flare; keep C-version age/costume lock. |

## Transition Edges

- `TE_REF002_001_BIRD_FOREGROUND_TO_GLIDE`
- `TE_REF002_002_BIRD_TO_CREDIT_SAFE`
- `TE_REF002_003_CREDIT_SAFE_TO_CLOUD_BANK`
- `TE_REF002_004_CLOUD_BANK_TO_AIRCRAFT`
- `TE_REF002_005_AIRCRAFT_TO_TITLE_SAFE`
- `TE_REF002_006_TITLE_FLARE_TO_NADIA`
- `TE_REF002_007_NADIA_TO_CHARACTER_CONTINUE`

## QA Checks

- Opening first frame must contain the white bird; no empty-cloud prelude.
- No generated readable title, logo, subtitles, watermark, or random letters.
- Aircraft appears only as a short reveal after cloud expansion; reject aircraft-led 24s one-take timing.
- Nadia appears only after the light transition around 21.5s, age-appropriate and non-sexualized.
- Post-23s timing is provisional until more reference evidence is available.

## Files Updated

- `03_story/scripts/director_shooting_script.md`
- `07_shots/video_units.json`
- `07_shots/transition_edges.json`
- `06_previs/camera_manifests/video_unit_camera_manifest.json`
- `07_shots/video_prompts_by_unit/VU_REF002_*.md`
- `07_shots/shot_list.csv`
- `03_story/idea_board/idea_board.json`
- `03_story/idea_board/idea_board.md`
- `07_shots/idea_board_prompts.csv`
