# Reference-003 Identity Repair R1 Prompt Pack

Generate/replace images before any further video assembly.

## OP_SHOT_018

# OP_SHOT_018 identity/detail repair prompt

Use case: photorealistic-natural
Asset type: official replacement keyframe candidate for Reference-003, `OP_SHOT_018`
Priority: 4
Action: `regenerate_if_face_drift_after_dense_reference_review`
Hard replace: `False`

## Primary Request

21:9 live-action remake keyframe of Nadia running toward camera in bright sky light, dynamic but age-appropriate, face matching the official Nadia lock exactly.

## Dense Video Reference Frames

Use these for timing, body pose, camera angle, motion beat, and scene layout only:
- `refs/dense_selected/OP_SHOT_018/OP_SHOT_018_sel_01_038750ms.jpg`
- `refs/dense_selected/OP_SHOT_018/OP_SHOT_018_sel_02_039500ms.jpg`
- `refs/dense_selected/OP_SHOT_018/OP_SHOT_018_sel_03_039750ms.jpg`
- `refs/dense_selected/OP_SHOT_018/OP_SHOT_018_sel_04_040000ms.jpg`
- `refs/dense_selected/OP_SHOT_018/OP_SHOT_018_sel_05_040125ms.jpg`

## Locked Assets

Use these as the source of truth for identity, costumes, props, and continuity:
- `nadia`: `asset_locks/nadia.png`
- `blue_water_pendant`: `asset_locks/blue_water_pendant.png`

## Current Output To Replace Or QA

- Current board image: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_018.png`
- Director/QA note: Use OP_SHOT_011_v2 as Nadia face lock; preserve running pose only from video.

## Rejection Conditions

- Do not use the rejected OP_SHOT_025 image as a character, group, or vehicle lock.
- Do not use the rejected OP_SHOT_034 face as a Nadia lock.
- No readable text, credits, lyrics, subtitles, logo, watermark, or random symbols.
- Minors must remain age-appropriate and non-sexualized.
- No character face swaps, costume redesigns, prop redesigns, or scene drift.

## Output Requirements

- 21:9 image, 1915x821 or higher, pure image only.
- Preserve the reference-video shot function while remaking it as a clean live-action/keyframe image.
- Make the frame usable as an AIGC video anchor, not a poster or marketing still.

## OP_SHOT_019

# OP_SHOT_019 identity/detail repair prompt

Use case: photorealistic-natural
Asset type: official replacement keyframe candidate for Reference-003, `OP_SHOT_019`
Priority: 5
Action: `regenerate_if_face_or_costume_drift_after_dense_reference_review`
Hard replace: `False`

## Primary Request

21:9 live-action remake keyframe of Jean running in the montage, energetic boy inventor, face and costume matching the official Jean lock exactly.

## Dense Video Reference Frames

Use these for timing, body pose, camera angle, motion beat, and scene layout only:
- `refs/dense_selected/OP_SHOT_019/OP_SHOT_019_sel_01_040750ms.jpg`
- `refs/dense_selected/OP_SHOT_019/OP_SHOT_019_sel_02_040875ms.jpg`
- `refs/dense_selected/OP_SHOT_019/OP_SHOT_019_sel_03_041000ms.jpg`
- `refs/dense_selected/OP_SHOT_019/OP_SHOT_019_sel_04_041500ms.jpg`
- `refs/dense_selected/OP_SHOT_019/OP_SHOT_019_sel_05_041875ms.jpg`
- `refs/dense_selected/OP_SHOT_019/OP_SHOT_019_sel_06_042125ms.jpg`

## Locked Assets

Use these as the source of truth for identity, costumes, props, and continuity:
- `jean`: `asset_locks/jean.png`

## Current Output To Replace Or QA

- Current board image: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_019.png`
- Director/QA note: Use OP_SHOT_012 as Jean lock; preserve cap, glasses, jacket, bow tie.

## Rejection Conditions

- Do not use the rejected OP_SHOT_025 image as a character, group, or vehicle lock.
- Do not use the rejected OP_SHOT_034 face as a Nadia lock.
- No readable text, credits, lyrics, subtitles, logo, watermark, or random symbols.
- Minors must remain age-appropriate and non-sexualized.
- No character face swaps, costume redesigns, prop redesigns, or scene drift.

## Output Requirements

- 21:9 image, 1915x821 or higher, pure image only.
- Preserve the reference-video shot function while remaking it as a clean live-action/keyframe image.
- Make the frame usable as an AIGC video anchor, not a poster or marketing still.

## OP_SHOT_020

# OP_SHOT_020 identity/detail repair prompt

Use case: photorealistic-natural
Asset type: official replacement keyframe candidate for Reference-003, `OP_SHOT_020`
Priority: 5
Action: `regenerate_if_marie_or_king_drift_after_dense_reference_review`
Hard replace: `False`

## Primary Request

21:9 live-action remake keyframe of Marie and King running in open daylight, child-safe, cheerful movement, identities matching their first approved lock.

## Dense Video Reference Frames

Use these for timing, body pose, camera angle, motion beat, and scene layout only:
- `refs/dense_selected/OP_SHOT_020/OP_SHOT_020_sel_01_042750ms.jpg`
- `refs/dense_selected/OP_SHOT_020/OP_SHOT_020_sel_02_043125ms.jpg`
- `refs/dense_selected/OP_SHOT_020/OP_SHOT_020_sel_03_043500ms.jpg`
- `refs/dense_selected/OP_SHOT_020/OP_SHOT_020_sel_04_043625ms.jpg`
- `refs/dense_selected/OP_SHOT_020/OP_SHOT_020_sel_05_044375ms.jpg`

## Locked Assets

Use these as the source of truth for identity, costumes, props, and continuity:
- `marie`: `asset_locks/marie.png`
- `king`: `asset_locks/king.png`

## Current Output To Replace Or QA

- Current board image: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_020.png`
- Director/QA note: Use OP_SHOT_014 as Marie/King lock; preserve child-safe age and King scarf.

## Rejection Conditions

- Do not use the rejected OP_SHOT_025 image as a character, group, or vehicle lock.
- Do not use the rejected OP_SHOT_034 face as a Nadia lock.
- No readable text, credits, lyrics, subtitles, logo, watermark, or random symbols.
- Minors must remain age-appropriate and non-sexualized.
- No character face swaps, costume redesigns, prop redesigns, or scene drift.

## Output Requirements

- 21:9 image, 1915x821 or higher, pure image only.
- Preserve the reference-video shot function while remaking it as a clean live-action/keyframe image.
- Make the frame usable as an AIGC video anchor, not a poster or marketing still.

## OP_SHOT_021

# OP_SHOT_021 identity/detail repair prompt

Use case: photorealistic-natural
Asset type: official replacement keyframe candidate for Reference-003, `OP_SHOT_021`
Priority: 9
Action: `keep_as_workprint_reference_and_use_for_group_energy`
Hard replace: `False`

## Primary Request

21:9 live-action group-running reference keyframe, keep current accepted energy; use only as continuity support unless a later QA pass requires a rerender.

## Dense Video Reference Frames

Use these for timing, body pose, camera angle, motion beat, and scene layout only:
- `refs/dense_selected/OP_SHOT_021/OP_SHOT_021_sel_01_044750ms.jpg`
- `refs/dense_selected/OP_SHOT_021/OP_SHOT_021_sel_02_045250ms.jpg`
- `refs/dense_selected/OP_SHOT_021/OP_SHOT_021_sel_03_045375ms.jpg`
- `refs/dense_selected/OP_SHOT_021/OP_SHOT_021_sel_04_045500ms.jpg`
- `refs/dense_selected/OP_SHOT_021/OP_SHOT_021_sel_05_046250ms.jpg`
- `refs/dense_selected/OP_SHOT_021/OP_SHOT_021_sel_06_046375ms.jpg`

## Locked Assets

Use these as the source of truth for identity, costumes, props, and continuity:
- `nadia`: `asset_locks/nadia.png`
- `jean`: `asset_locks/jean.png`
- `marie`: `asset_locks/marie.png`
- `king`: `asset_locks/king.png`
- `grandis`: `asset_locks/grandis.png`
- `sanson`: `asset_locks/sanson.png`
- `hanson`: `asset_locks/hanson.png`

## Current Output To Replace Or QA

- Current board image: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_021_v2.png`
- Director/QA note: Director accepted current OP_SHOT_021_v2 for workprint use.

## Rejection Conditions

- Do not use the rejected OP_SHOT_025 image as a character, group, or vehicle lock.
- Do not use the rejected OP_SHOT_034 face as a Nadia lock.
- No readable text, credits, lyrics, subtitles, logo, watermark, or random symbols.
- Minors must remain age-appropriate and non-sexualized.
- No character face swaps, costume redesigns, prop redesigns, or scene drift.
- This item is already accepted for workprint; only rerender if a later identity QA explicitly fails it.

## Output Requirements

- 21:9 image, 1915x821 or higher, pure image only.
- Preserve the reference-video shot function while remaking it as a clean live-action/keyframe image.
- Make the frame usable as an AIGC video anchor, not a poster or marketing still.

## OP_SHOT_023

# OP_SHOT_023 identity/detail repair prompt

Use case: photorealistic-natural
Asset type: official replacement keyframe candidate for Reference-003, `OP_SHOT_023`
Priority: 3
Action: `regenerate_or_retouch_with_grandis_trio_locks`
Hard replace: `False`

## Primary Request

21:9 live-action action keyframe of Grandis, Sanson, and Hanson in a fast bridge/action beat, faces and costumes matching their official trio lock.

## Dense Video Reference Frames

Use these for timing, body pose, camera angle, motion beat, and scene layout only:
- `refs/dense_selected/OP_SHOT_023/OP_SHOT_023_sel_01_047250ms.jpg`
- `refs/dense_selected/OP_SHOT_023/OP_SHOT_023_sel_02_048000ms.jpg`
- `refs/dense_selected/OP_SHOT_023/OP_SHOT_023_sel_03_048125ms.jpg`
- `refs/dense_selected/OP_SHOT_023/OP_SHOT_023_sel_04_048375ms.jpg`
- `refs/dense_selected/OP_SHOT_023/OP_SHOT_023_sel_05_048500ms.jpg`
- `refs/dense_selected/OP_SHOT_023/OP_SHOT_023_sel_06_048625ms.jpg`

## Locked Assets

Use these as the source of truth for identity, costumes, props, and continuity:
- `grandis`: `asset_locks/grandis.png`
- `sanson`: `asset_locks/sanson.png`
- `hanson`: `asset_locks/hanson.png`

## Current Output To Replace Or QA

- Current board image: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_023.png`
- Director/QA note: Use OP_SHOT_016_v2 as trio lock; do not redesign faces during action.

## Rejection Conditions

- Do not use the rejected OP_SHOT_025 image as a character, group, or vehicle lock.
- Do not use the rejected OP_SHOT_034 face as a Nadia lock.
- No readable text, credits, lyrics, subtitles, logo, watermark, or random symbols.
- Minors must remain age-appropriate and non-sexualized.
- No character face swaps, costume redesigns, prop redesigns, or scene drift.

## Output Requirements

- 21:9 image, 1915x821 or higher, pure image only.
- Preserve the reference-video shot function while remaking it as a clean live-action/keyframe image.
- Make the frame usable as an AIGC video anchor, not a poster or marketing still.

## OP_SHOT_024

# OP_SHOT_024 identity/detail repair prompt

Use case: photorealistic-natural
Asset type: official replacement keyframe candidate for Reference-003, `OP_SHOT_024`
Priority: 2
Action: `create_new_grandis_vehicle_action_craft_lock`
Hard replace: `True`

## Primary Request

21:9 live-action action keyframe establishing a new Grandis vehicle/action craft lock in sky/cloud spray, readable silhouette, consistent retro adventure engineering.

## Dense Video Reference Frames

Use these for timing, body pose, camera angle, motion beat, and scene layout only:
- `refs/dense_selected/OP_SHOT_024/OP_SHOT_024_sel_01_048850ms.jpg`
- `refs/dense_selected/OP_SHOT_024/OP_SHOT_024_sel_02_049350ms.jpg`
- `refs/dense_selected/OP_SHOT_024/OP_SHOT_024_sel_03_049475ms.jpg`
- `refs/dense_selected/OP_SHOT_024/OP_SHOT_024_sel_04_049600ms.jpg`
- `refs/dense_selected/OP_SHOT_024/OP_SHOT_024_sel_05_050225ms.jpg`

## Locked Assets

Use these as the source of truth for identity, costumes, props, and continuity:
- `grandis`: `asset_locks/grandis.png`
- `sanson`: `asset_locks/sanson.png`
- `hanson`: `asset_locks/hanson.png`

## Current Output To Replace Or QA

- Current board image: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_024.png`
- Director/QA note: Create a new vehicle/action craft lock. Do not use rejected OP_SHOT_025.

## Rejection Conditions

- Do not use the rejected OP_SHOT_025 image as a character, group, or vehicle lock.
- Do not use the rejected OP_SHOT_034 face as a Nadia lock.
- No readable text, credits, lyrics, subtitles, logo, watermark, or random symbols.
- Minors must remain age-appropriate and non-sexualized.
- No character face swaps, costume redesigns, prop redesigns, or scene drift.

## Output Requirements

- 21:9 image, 1915x821 or higher, pure image only.
- Preserve the reference-video shot function while remaking it as a clean live-action/keyframe image.
- Make the frame usable as an AIGC video anchor, not a poster or marketing still.

## OP_SHOT_025

# OP_SHOT_025 identity/detail repair prompt

Use case: photorealistic-natural
Asset type: official replacement keyframe candidate for Reference-003, `OP_SHOT_025`
Priority: 1
Action: `hard_replace_rebuild_locked_group_tableau`
Hard replace: `True`

## Primary Request

21:9 live-action locked group tableau replacing the rejected large group portrait: all seven recurring characters arranged together with correct faces, costumes, scale, and Grandis vehicle/action craft continuity.

## Dense Video Reference Frames

Use these for timing, body pose, camera angle, motion beat, and scene layout only:
- `refs/dense_selected/OP_SHOT_025/OP_SHOT_025_sel_01_050700ms.jpg`
- `refs/dense_selected/OP_SHOT_025/OP_SHOT_025_sel_02_051450ms.jpg`
- `refs/dense_selected/OP_SHOT_025/OP_SHOT_025_sel_03_051575ms.jpg`
- `refs/dense_selected/OP_SHOT_025/OP_SHOT_025_sel_04_051700ms.jpg`
- `refs/dense_selected/OP_SHOT_025/OP_SHOT_025_sel_05_051825ms.jpg`
- `refs/dense_selected/OP_SHOT_025/OP_SHOT_025_sel_06_052325ms.jpg`

## Locked Assets

Use these as the source of truth for identity, costumes, props, and continuity:
- `nadia`: `asset_locks/nadia.png`
- `jean`: `asset_locks/jean.png`
- `marie`: `asset_locks/marie.png`
- `king`: `asset_locks/king.png`
- `grandis`: `asset_locks/grandis.png`
- `sanson`: `asset_locks/sanson.png`
- `hanson`: `asset_locks/hanson.png`
- `blue_water_pendant`: `asset_locks/blue_water_pendant.png`

## Current Output To Replace Or QA

- Current board image: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_025.png`
- Director/QA note: Director rejected current OP_SHOT_025 as the worst group image; rebuild from locks.

## Rejection Conditions

- Do not use the rejected OP_SHOT_025 image as a character, group, or vehicle lock.
- Do not use the rejected OP_SHOT_034 face as a Nadia lock.
- No readable text, credits, lyrics, subtitles, logo, watermark, or random symbols.
- Minors must remain age-appropriate and non-sexualized.
- No character face swaps, costume redesigns, prop redesigns, or scene drift.

## Output Requirements

- 21:9 image, 1915x821 or higher, pure image only.
- Preserve the reference-video shot function while remaking it as a clean live-action/keyframe image.
- Make the frame usable as an AIGC video anchor, not a poster or marketing still.

## OP_SHOT_032

# OP_SHOT_032 identity/detail repair prompt

Use case: photorealistic-natural
Asset type: official replacement keyframe candidate for Reference-003, `OP_SHOT_032`
Priority: 6
Action: `regenerate_if_nemo_drift_after_dense_reference_review`
Hard replace: `False`

## Primary Request

21:9 live-action Nemo sunset profile keyframe, stern adult captain, uniform and cap locked, same actor identity as official Nemo lock.

## Dense Video Reference Frames

Use these for timing, body pose, camera angle, motion beat, and scene layout only:
- `refs/dense_selected/OP_SHOT_032/OP_SHOT_032_sel_01_065750ms.jpg`
- `refs/dense_selected/OP_SHOT_032/OP_SHOT_032_sel_02_066250ms.jpg`
- `refs/dense_selected/OP_SHOT_032/OP_SHOT_032_sel_03_066500ms.jpg`
- `refs/dense_selected/OP_SHOT_032/OP_SHOT_032_sel_04_067000ms.jpg`
- `refs/dense_selected/OP_SHOT_032/OP_SHOT_032_sel_05_067375ms.jpg`

## Locked Assets

Use these as the source of truth for identity, costumes, props, and continuity:
- `nemo`: `asset_locks/nemo.png`

## Current Output To Replace Or QA

- Current board image: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_032.png`
- Director/QA note: Use OP_SHOT_032 as current Nemo lock; preserve uniform, cap, stern adult face.

## Rejection Conditions

- Do not use the rejected OP_SHOT_025 image as a character, group, or vehicle lock.
- Do not use the rejected OP_SHOT_034 face as a Nadia lock.
- No readable text, credits, lyrics, subtitles, logo, watermark, or random symbols.
- Minors must remain age-appropriate and non-sexualized.
- No character face swaps, costume redesigns, prop redesigns, or scene drift.

## Output Requirements

- 21:9 image, 1915x821 or higher, pure image only.
- Preserve the reference-video shot function while remaking it as a clean live-action/keyframe image.
- Make the frame usable as an AIGC video anchor, not a poster or marketing still.

## OP_SHOT_033

# OP_SHOT_033 identity/detail repair prompt

Use case: photorealistic-natural
Asset type: official replacement keyframe candidate for Reference-003, `OP_SHOT_033`
Priority: 6
Action: `regenerate_if_nemo_continuity_drift_after_dense_reference_review`
Hard replace: `False`

## Primary Request

21:9 live-action Nemo sunset continuation keyframe, same actor identity as OP_SHOT_032, only angle and sunset lighting shift.

## Dense Video Reference Frames

Use these for timing, body pose, camera angle, motion beat, and scene layout only:
- `refs/dense_selected/OP_SHOT_033/OP_SHOT_033_sel_01_068750ms.jpg`
- `refs/dense_selected/OP_SHOT_033/OP_SHOT_033_sel_02_068875ms.jpg`
- `refs/dense_selected/OP_SHOT_033/OP_SHOT_033_sel_03_069000ms.jpg`
- `refs/dense_selected/OP_SHOT_033/OP_SHOT_033_sel_04_069500ms.jpg`
- `refs/dense_selected/OP_SHOT_033/OP_SHOT_033_sel_05_069625ms.jpg`
- `refs/dense_selected/OP_SHOT_033/OP_SHOT_033_sel_06_070375ms.jpg`

## Locked Assets

Use these as the source of truth for identity, costumes, props, and continuity:
- `nemo`: `asset_locks/nemo.png`

## Current Output To Replace Or QA

- Current board image: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_033.png`
- Director/QA note: Match OP_SHOT_032 exactly; only angle/lighting may change.

## Rejection Conditions

- Do not use the rejected OP_SHOT_025 image as a character, group, or vehicle lock.
- Do not use the rejected OP_SHOT_034 face as a Nadia lock.
- No readable text, credits, lyrics, subtitles, logo, watermark, or random symbols.
- Minors must remain age-appropriate and non-sexualized.
- No character face swaps, costume redesigns, prop redesigns, or scene drift.

## Output Requirements

- 21:9 image, 1915x821 or higher, pure image only.
- Preserve the reference-video shot function while remaking it as a clean live-action/keyframe image.
- Make the frame usable as an AIGC video anchor, not a poster or marketing still.

## OP_SHOT_034

# OP_SHOT_034 identity/detail repair prompt

Use case: photorealistic-natural
Asset type: official replacement keyframe candidate for Reference-003, `OP_SHOT_034`
Priority: 1
Action: `hard_replace_with_nadia_face_lock`
Hard replace: `True`

## Primary Request

21:9 live-action solemn front close-up of Nadia in cool symbolic blue light, face matching OP_SHOT_011_v2 exactly, Blue Water pendant readable, no sea-background face drift.

## Dense Video Reference Frames

Use these for timing, body pose, camera angle, motion beat, and scene layout only:
- `refs/dense_selected/OP_SHOT_034/OP_SHOT_034_sel_01_071200ms.jpg`
- `refs/dense_selected/OP_SHOT_034/OP_SHOT_034_sel_02_071325ms.jpg`
- `refs/dense_selected/OP_SHOT_034/OP_SHOT_034_sel_03_071950ms.jpg`
- `refs/dense_selected/OP_SHOT_034/OP_SHOT_034_sel_04_072075ms.jpg`
- `refs/dense_selected/OP_SHOT_034/OP_SHOT_034_sel_05_072825ms.jpg`

## Locked Assets

Use these as the source of truth for identity, costumes, props, and continuity:
- `nadia`: `asset_locks/nadia.png`
- `blue_water_pendant`: `asset_locks/blue_water_pendant.png`

## Current Output To Replace Or QA

- Current board image: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_034.png`
- Director/QA note: Director rejected current OP_SHOT_034; Nadia must match OP_SHOT_011_v2.

## Rejection Conditions

- Do not use the rejected OP_SHOT_025 image as a character, group, or vehicle lock.
- Do not use the rejected OP_SHOT_034 face as a Nadia lock.
- No readable text, credits, lyrics, subtitles, logo, watermark, or random symbols.
- Minors must remain age-appropriate and non-sexualized.
- No character face swaps, costume redesigns, prop redesigns, or scene drift.

## Output Requirements

- 21:9 image, 1915x821 or higher, pure image only.
- Preserve the reference-video shot function while remaking it as a clean live-action/keyframe image.
- Make the frame usable as an AIGC video anchor, not a poster or marketing still.
