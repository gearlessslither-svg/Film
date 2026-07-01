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
