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
