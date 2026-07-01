# 15 — VU_REF003_015_NIGHT_AIRCRAFT_PASS — 夜航飞行器短切

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_015_NIGHT_AIRCRAFT_PASS/reference_clip/VU_REF003_015_NIGHT_AIRCRAFT_PASS_reference.mp4`
2. Ordered keyframes:
- 图1: `R5_VU_REF003_015_NIGHT_AIRCRAFT_PASS_065000ms_01` (01:05.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_015_NIGHT_AIRCRAFT_PASS/keyframes/01_R5_VU_REF003_015_NIGHT_AIRCRAFT_PASS_065000ms_01.png`
- 图2: `OP_SHOT_031` (01:05.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_015_NIGHT_AIRCRAFT_PASS/keyframes/02_OP_SHOT_031.png`
3. Active asset locks:
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/props_vehicles_symbols_jean_aircraft.png`

## Save Result To

`08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_015_NIGHT_AIRCRAFT_PASS.mp4`

## Prompt To Use

# VU_REF003_015_NIGHT_AIRCRAFT_PASS - 夜航飞行器短切

- Unit type: `brief_night_vehicle_pass`
- Time range: 01:05.00-01:06.00
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `true`

## Ordered Input Images

- 图1 = `OP_SHOT_031` (图1 / night_aircraft_pass, 01:05.50): Dark retro aircraft passes at night with small colored lights, no text.

## Script Intent

夜间飞行器短切，为 Nemo 夕景段转场。

## Frame Relationships

短促桥接，不扩成长动作。

Incoming: TE_REF003_030_030_TO_031  
Intra: none  
Outgoing: TE_REF003_031_031_TO_032

## Camera Plan

- Movement: short dark vehicle pass
- Framing: close/dark aircraft silhouette and colored lights
- Lens: night action lens
- Screen Direction: brief pass across frame
- Focus: craft shape and lights
- Lighting: dark blue night with small red/purple lights

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
