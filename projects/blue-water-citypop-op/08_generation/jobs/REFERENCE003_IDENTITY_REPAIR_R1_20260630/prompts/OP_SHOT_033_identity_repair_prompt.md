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
