# VU_REF003_010_GRANDIS_TRIO_INTRO - Grandis 三人组介绍

- Unit type: `adult_trio_intro_montage`
- Time range: 00:34.50-00:37.50
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_015` (图1 / Grandis_trio_wide, 00:35.50): Grandis, Sanson, and Hanson pose theatrically in a live-action period setting.
- 图2 = `OP_SHOT_016` (图2 / Grandis_trio_close, 00:37.00): Close energetic character beat for the adult trio, playful but grounded.

## Script Intent

Grandis 三人组从姿态到特写，形成戏剧化成人反派/喜剧能量。

## Frame Relationships

成人三人组可夸张但要真人化，不混入儿童段。

Incoming: TE_REF003_014_014_TO_015  
Intra: TE_REF003_015_015_TO_016  
Outgoing: TE_REF003_016_016_TO_017

## Camera Plan

- Movement: hard beat cuts and small theatrical pose shifts
- Framing: wide trio then close group
- Lens: medium portrait/wide plaza lens
- Screen Direction: not continuous; montage rhythm
- Focus: Grandis trio
- Lighting: bright outdoor showy light

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
