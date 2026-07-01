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
