# VU_REF003_016_NEMO_SUNSET_PROFILE - Nemo 夕景船长肖像

- Unit type: `adult_portrait_hold`
- Time range: 01:06.50-01:11.00
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_032` (图1 / Nemo_profile_start, 01:06.50): Stern adult submarine captain in dark uniform and white cap against sunset sky, no text.
- 图2 = `OP_SHOT_033` (图2 / Nemo_profile_hold, 01:09.50): Nemo holds a dignified profile at sunset, wind and coat shape clear.

## Script Intent

Nemo/船长在夕景中沉稳长 hold，成人角色威严。

## Frame Relationships

成人肖像，不要加入 karaoke/credits text。

Incoming: TE_REF003_031_031_TO_032  
Intra: TE_REF003_032_032_TO_033  
Outgoing: TE_REF003_033_033_TO_034

## Camera Plan

- Movement: portrait hold with subtle push or wind
- Framing: low-angle adult captain portrait at sunset
- Lens: portrait/medium lens
- Screen Direction: gaze off horizon
- Focus: face, hat, uniform silhouette
- Lighting: warm sunset sky

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
