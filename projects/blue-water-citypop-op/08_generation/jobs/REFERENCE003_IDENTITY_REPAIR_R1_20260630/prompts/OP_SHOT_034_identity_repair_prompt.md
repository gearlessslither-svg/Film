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
