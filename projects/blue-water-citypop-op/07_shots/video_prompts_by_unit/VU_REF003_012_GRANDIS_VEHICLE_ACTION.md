# VU_REF003_012_GRANDIS_VEHICLE_ACTION - Grandis 车辆动作到群像

- Unit type: `vehicle_action_bridge`
- Time range: 00:48.00-00:51.50
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `true`

## Ordered Input Images

- 图1 = `OP_SHOT_023` (图1 / Grandis_action_close, 00:48.00): Grandis and companions surge into an action beat, lively but live-action grounded.
- 图2 = `OP_SHOT_024` (图2 / vehicle_sky_action, 00:49.50): A retro adventure vehicle or craft arcs through blue sky and cloud spray, energetic but readable.
- 图3 = `OP_SHOT_025` (图3 / group_lineup, 00:51.50): Main group lineup in a bright character tableau, no text overlay.

## Script Intent

奔跑段后转 Grandis/车辆动作，形成进入 Nautilus/冒险段的桥。

## Frame Relationships

车辆/飞行器比例和方向要锁；不生成文字。

Incoming: TE_REF003_022_022_TO_023  
Intra: TE_REF003_023_023_TO_024, TE_REF003_024_024_TO_025  
Outgoing: TE_REF003_025_025_TO_026

## Camera Plan

- Movement: fast action cut from character energy to vehicle/air movement and group lineup
- Framing: vehicle sky/city action plus group pose
- Lens: wide action lens
- Screen Direction: vehicle momentum carries forward
- Focus: vehicle scale and group identity
- Lighting: bright sky/city

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
