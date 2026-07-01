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
