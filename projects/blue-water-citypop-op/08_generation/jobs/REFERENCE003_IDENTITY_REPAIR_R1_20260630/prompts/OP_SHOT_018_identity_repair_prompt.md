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
