# VU_REF003_001_BLACK_CLOUD_FADEIN - 黑场到云层蓝天淡入

- Unit type: `fadein_establishing_pair`
- Time range: 00:00.00-00:02.00
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_001` (图1 / black_to_cloud_start, 00:00.00): Black frame or very dark fade beginning into luminous cloud texture, no subject yet.
- 图2 = `OP_SHOT_002` (图2 / bright_cloud_sky_reveal, 00:01.50): Bright white cloud mass opens into saturated blue sky, no bird yet.

## Script Intent

完整 OP 从黑场/暗部起，淡入明亮云层和蓝天；不是白鸟第一帧开场。

## Frame Relationships

建立天空舞台，为白鸟入画预留空间；不要提前出现标题、人物或飞机。

Incoming: none  
Intra: TE_REF003_001_001_TO_002  
Outgoing: TE_REF003_002_002_TO_003

## Camera Plan

- Movement: fade from black into bright cloud plate, then reveal blue sky opening
- Framing: sky/cloud establishing, no character
- Lens: wide sky plate
- Screen Direction: none yet
- Focus: cloud mass and sky gradient
- Lighting: bright daylight emerging from black

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
