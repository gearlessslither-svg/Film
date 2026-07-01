# Reference-003 Setting Chapter v1

Status: approved for current production by director instruction on 2026-06-30. No additional confirmation required before continuing the current pass.

This setting chapter is now Gate 0 for `blue-water-citypop-op` Reference-003. All new keyframes, detail pass frames, video units, and AIGC video prompts must use these locks. If a generated image changes a face, prop, vehicle, animal, scene structure, or core symbol, mark it `identity_continuity_fail` or `asset_continuity_fail` even if the image is attractive.

Latest director feedback:

- `OP_SHOT_011_v2` Nadia close-up is excellent and remains the Nadia official face lock.
- `OP_SHOT_021_v2` running group image is excellent enough for the current workprint.
- `OP_SHOT_025` group lineup / large group portrait is rejected for this version.
- `OP_SHOT_034` blue/sea-background Nadia solemn close is rejected for this version.
- R1 hard replacements are now applied for `OP_SHOT_024`, `OP_SHOT_025`, and `OP_SHOT_034`.

## Character Locks

| Asset | Official lock | Production rule |
|---|---|---|
| Nadia | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_011_v2.png` | Director's preferred face. Use this for all Nadia close, profile, running, solemn, group, and video frames. Preserve honey-tan skin, navy-black bob, gold hoops/bangles, modest red-orange/white outfit, and Blue Water pendant. |
| Jean | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_012.png` | First accepted appearance. Preserve 14-year-old inventor identity, brown hair, round glasses, blue cap/beret, blue jacket, white shirt, red bow tie, short trousers, boots, and handmade-inventor energy. |
| Marie | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_014.png` | Use the first accepted close view as identity lock. Preserve very young child age, blonde hair, modest white dress, safe childlike expression. |
| King | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_014.png` | Use the first accepted close view with Marie as lock. Preserve small lion cub scale and red scarf. |
| Grandis | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_016_v2.png` | First accepted close trio view. Preserve adult red-haired leader silhouette, red uniform, theatrical confidence. |
| Sanson | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_016_v2.png` | First accepted close trio view. Preserve tall adult companion silhouette, blond/strong read, and distinct face from Hanson. |
| Hanson | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_016_v2.png` | First accepted close trio view. Preserve shorter bespectacled mechanic identity and distinct face from Sanson. |
| Nemo | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_032.png` | First accepted appearance. Preserve stern adult submarine captain, dark uniform, white cap, sunset authority. |
| Electra | needs dedicated lock | Listed in project canon but no dedicated accepted close keyframe yet. Do not make her a clear hero-face subject in new official frames until a lock is created. |
| Gargoyle | needs dedicated lock | Listed in project canon but not active in current 42-keyframe pass. Do not invent a visible new face without lock approval. |

## Prop, Animal, Vehicle, and Symbol Locks

| Asset | Official lock | Production rule |
|---|---|---|
| Blue Water pendant | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_035.png` plus Nadia lock | Sapphire-blue pendant, central pursuit object and OP emblem. Keep cyan glow clean and text-free. Nadia must retain pendant when visible unless the shot is too wide to read it. |
| White bird | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630/outputs/OP_SHOT_003.png` | Clean white bird/dove in bright blue sky. Do not turn it into a gull flock, fantasy creature, logo, or text-like silhouette. |
| Jean aircraft | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_007.png` | Handmade retro monoplane/aircraft silhouette. Preserve handmade adventure design, not modern aircraft, drone, jet, or car. |
| Grandis vehicle/action craft | `08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/outputs/OP_SHOT_024_VEHICLE_LOCK_R1.png` | R1 vehicle/action craft lock. Do not use rejected `OP_SHOT_025` as a prop or group lock. Preserve red-brown riveted retro adventure craft design, rounded hull, dark underside, and Grandis styling. |
| Nautilus | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_026.png` | Submarine exterior lock. Preserve large graceful undersea silhouette, dark metal body, ocean light scale, and no readable markings. |
| Blue grid / Atlantean geometry | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_030.png` | Glowing blue geometric ground/city motif. Keep abstract and unreadable; no letters, UI text, symbols that resemble logos, or random glyphs. |
| Water burst transition | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_038.png` | Blue-white water/ice burst transition. Preserve clean elemental motion and no text. |

## Scene and Environment Locks

| Scene | Lock source | Production rule |
|---|---|---|
| Opening sky/clouds | `OP_SHOT_002` through `OP_SHOT_006` | Saturated blue sky, bright cloud masses, title-safe empty areas with no generated letters, credits, subtitles, or broadcaster marks. |
| Nadia sky entry | `OP_SHOT_010`, `OP_SHOT_011_v2` | Warm bright sky and sunlight transition into Nadia identity. Later Nadia shots must keep the `OP_SHOT_011_v2` face. |
| Meadow child/animal beat | `OP_SHOT_013`, `OP_SHOT_014` | Bright, safe meadow. Marie and King stay child-safe and playful. |
| Running montage graphic space | `OP_SHOT_017` through `OP_SHOT_022` | Music-beat montage; not a one-take. Character identity locks override any model tendency to redesign faces. Group shots need identity repair before final video. |
| Undersea Nautilus space | `OP_SHOT_026` through `OP_SHOT_028` | Deep ocean, shimmering surface light, large submarine scale. No credits or readable marks. |
| Night city / blue grid | `OP_SHOT_029`, `OP_SHOT_030` | Mysterious dark city and blue geometry. Preserve location structure and avoid readable symbols. |
| Nemo sunset portrait | `OP_SHOT_032`, `OP_SHOT_033` | Sunset adult portrait hold. Preserve Nemo lock and calm authority. |
| Final sky/horizon | `OP_SHOT_040`, `OP_SHOT_041` | Clean no-text final sky, sun glow, and negative space replacing broadcaster/title marks. |

## Current Production Implications

- Existing `generated_reference003_qa_pass` means composition/no-text timing pass, not final identity pass.
- `OP_SHOT_021_v2` is director-accepted for current workprint use.
- Batch 01 R1 repair targets are applied: `OP_SHOT_024` vehicle/action craft lock, `OP_SHOT_025` group lineup/vehicle tableau, and `OP_SHOT_034` Nadia solemn close.
- Next image gate: identity QA for `OP_SHOT_018`, `OP_SHOT_019`, `OP_SHOT_020`, `OP_SHOT_023`, `OP_SHOT_032`, and `OP_SHOT_033`; regenerate only if a visible lock mismatch is found.
- For video generation, each unit package must include these asset locks as identity anchors, especially multi-character units.
