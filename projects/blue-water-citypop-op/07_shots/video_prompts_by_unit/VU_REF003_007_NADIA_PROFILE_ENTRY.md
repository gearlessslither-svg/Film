# VU_REF003_007_NADIA_PROFILE_ENTRY - Nadia 侧脸入场到近景

- Unit type: `character_profile_sequence`
- Time range: 00:24.00-00:27.50
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_010` (图1 / Nadia_profile, 00:24.50): Age-appropriate Nadia C-version in side/profile close-up after the sun transition, sky behind.
- 图2 = `OP_SHOT_011` (图2 / Nadia_close, 00:27.00): Nadia turns into a closer bright expression, Blue Water identity detail may be visible, non-sexualized.

## Script Intent

Nadia 首次人物入场，侧脸/回头/近景构成第一段角色介绍。

## Frame Relationships

Nadia C 版锁定，14 岁、安全、保守；保留侧脸入场节奏。

Incoming: TE_REF003_009_009_TO_010  
Intra: TE_REF003_010_010_TO_011  
Outgoing: TE_REF003_011_011_TO_012

## Camera Plan

- Movement: small portrait hold and push/angle shift
- Framing: profile to closer face, sky/stone background
- Lens: portrait lens
- Screen Direction: Nadia gaze changes across the beat
- Focus: Nadia face and earrings/pendant details
- Lighting: bright sky bounce

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
