# VU_REF003_004_AIRCRAFT_BRIEF_REVEAL - 飞行器短暂露出

- Unit type: `brief_spatial_reveal`
- Time range: 00:14.50-00:16.50
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `true`

## Ordered Input Images

- 图1 = `OP_SHOT_007` (图1 / aircraft_brief_reveal, 00:15.00): Jean-style handmade retro aircraft or wing flashes briefly through clouded sky, scale controlled.

## Script Intent

完整 OP 中飞行器/机翼只短促出现，不能扩成 24 秒一镜到底。

## Frame Relationships

短露即可，避免飞行器抢戏；最终视频前需要比例/轴线检查。

Incoming: TE_REF003_006_006_TO_007  
Intra: none  
Outgoing: TE_REF003_007_007_TO_008

## Camera Plan

- Movement: brief reveal from cloud/wing edge to small aircraft in sky
- Framing: aircraft small-to-medium for a short beat, clouds still important
- Lens: wide sky lens with scale proof
- Screen Direction: aircraft direction continues sky motion
- Focus: aircraft silhouette and cloud edge
- Lighting: bright sky

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
