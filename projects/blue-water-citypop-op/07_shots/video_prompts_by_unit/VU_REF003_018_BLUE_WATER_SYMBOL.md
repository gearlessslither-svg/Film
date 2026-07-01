# VU_REF003_018_BLUE_WATER_SYMBOL - Blue Water 象征与水下纹理

- Unit type: `symbolic_jewel_transition`
- Time range: 01:13.50-01:17.00
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_035` (图1 / Blue_Water_jewel_symbol, 01:13.50): Blue Water jewel/sapphire symbol over clean blue field, no text or marks.
- 图2 = `OP_SHOT_036` (图2 / blue_symbol_bloom, 01:15.00): Cyan-blue bloom or energy texture replaces original text overlay, jewel feeling preserved.
- 图3 = `OP_SHOT_037` (图3 / underwater_texture, 01:16.50): Underwater blue texture and light pattern, clean and text-free.

## Script Intent

Blue Water/宝石/水下纹理承担象征性转场，原片 NHK/文字必须替换。

## Frame Relationships

保留 Blue Water 象征，不生成 NHK 或文字。

Incoming: TE_REF003_034_034_TO_035  
Intra: TE_REF003_035_035_TO_036, TE_REF003_036_036_TO_037  
Outgoing: TE_REF003_037_037_TO_038

## Camera Plan

- Movement: jewel/symbol overlay dissolves into blue underwater texture
- Framing: macro jewel and abstract blue texture
- Lens: macro to wide texture
- Screen Direction: symbolic not geographic
- Focus: jewel facets and blue energy
- Lighting: cyan/blue glow

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
