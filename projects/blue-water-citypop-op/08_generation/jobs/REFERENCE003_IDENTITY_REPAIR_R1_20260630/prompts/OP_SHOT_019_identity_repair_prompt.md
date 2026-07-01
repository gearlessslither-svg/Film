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
