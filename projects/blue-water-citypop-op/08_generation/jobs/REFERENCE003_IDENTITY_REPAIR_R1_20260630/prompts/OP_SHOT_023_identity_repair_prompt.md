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
