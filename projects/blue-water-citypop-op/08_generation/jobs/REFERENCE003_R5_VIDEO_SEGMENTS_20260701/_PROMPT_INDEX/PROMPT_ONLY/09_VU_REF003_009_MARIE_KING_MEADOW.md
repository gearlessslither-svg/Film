# 09 — VU_REF003_009_MARIE_KING_MEADOW — Marie 与 King 草地段

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/reference_clip/VU_REF003_009_MARIE_KING_MEADOW_reference.mp4`
2. Ordered keyframes:
- 图1: `R5_VU_REF003_009_MARIE_KING_MEADOW_031000ms_01` (00:31.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/keyframes/01_R5_VU_REF003_009_MARIE_KING_MEADOW_031000ms_01.png`
- 图2: `OP_SHOT_013` (00:31.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/keyframes/02_OP_SHOT_013.png`
- 图3: `OP_SHOT_014` (00:34.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/keyframes/03_OP_SHOT_014.png`
3. Active asset locks:
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/characters_king.png`

## Save Result To

`08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_009_MARIE_KING_MEADOW.mp4`

## Prompt To Use

# VU_REF003_009_MARIE_KING_MEADOW - Marie 与 King 草地段

- Unit type: `child_animal_meadow_gag`
- Time range: 00:31.00-00:34.00
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_013` (图1 / Marie_King_meadow, 00:31.50): Marie and small lion cub King in a bright meadow, playful and child-safe.
- 图2 = `OP_SHOT_014` (图2 / Marie_King_close, 00:34.00): Cheerful close character beat for Marie and King, safe and non-threatening.

## Script Intent

Marie/King 在草地中做明亮儿童喜剧节奏。

## Frame Relationships

儿童安全、可爱明亮；不生成字幕。

Incoming: TE_REF003_012_012_TO_013  
Intra: TE_REF003_013_013_TO_014  
Outgoing: TE_REF003_014_014_TO_015

## Camera Plan

- Movement: low meadow hold with small playful motion
- Framing: grass foreground, sky and clouds behind
- Lens: low wide child-safe angle
- Screen Direction: playful forward motion
- Focus: Marie and King
- Lighting: bright daylight meadow

## AIGC Video Prompt

Generate this unit as a faithful live-action remake of the reference-003 OP timing. Use the ordered images as the only keyframe order for this unit. Preserve the reference shot function, motion role, screen direction, and character-entry timing. Replace all original readable titles, credits, lyrics, subtitles, and broadcaster marks with clean no-text composition.

## Generation Requirements

- Use reference-003-full-op-2160p as the timing and composition source.
- Replace original readable titles, credits, lyrics, subtitles, and NHK marks with clean no-text composition while preserving shot function.
- Do not generate literal anime screenshots; produce a faithful live-action remake keyframe/video plan.
- Preserve character age, costume color blocks, motion direction, and OP rhythm.

## Negative / Failure Conditions

- If readable text, logo, credits, lyrics, subtitle, or broadcaster mark appears, reject.
- If timing role or screen function no longer matches reference-003, reject.
- If a montage unit becomes a false continuous one-take, reject.
