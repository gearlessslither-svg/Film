# VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS - 白鸟字幕安全位与云层增长

- Unit type: `title_safe_bird_cloud_sequence`
- Time range: 00:07.00-00:14.00
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_005` (图1 / no_text_credit_safe_bird, 00:07.50): Small white bird over clean blue sky with large center negative space, replacing credits with no text.
- 图2 = `OP_SHOT_006` (图2 / cloud_bank_growth, 00:11.50): Large bright cloud bank grows into frame while the bird becomes small or exits.

## Script Intent

白鸟继续穿过蓝天，原片有职员表和歌词；生成版要保留留白和云层节奏但不能生成可读文字。

## Frame Relationships

用无字留白替代职员表；云层从边缘进入并逐渐占据画面。

Incoming: TE_REF003_004_004_TO_005  
Intra: TE_REF003_005_005_TO_006  
Outgoing: TE_REF003_006_006_TO_007

## Camera Plan

- Movement: mostly locked sky hold with bird drift and cloud bank growth
- Framing: clean center negative space, bird small, clouds entering
- Lens: wide graphic sky field
- Screen Direction: same bird direction from previous unit
- Focus: bird and cloud bank
- Lighting: even blue daylight

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
