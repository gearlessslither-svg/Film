# AIGC Video Generation Brief — VU_REF003_012_GRANDIS_VEHICLE_ACTION

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_012_GRANDIS_VEHICLE_ACTION_reference.mp4`
- Ordered keyframe anchors:
- 1. `OP_SHOT_023` at `00:48.00`: Grandis 动作桥; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_023.png`
- 2. `OP_SHOT_024` at `00:49.50`: 车辆/飞行器空中动作; anchor image `08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/outputs/OP_SHOT_024_VEHICLE_LOCK_R1.png`
- 3. `OP_SHOT_025` at `00:51.50`: 全员群像; anchor image `08_generation/jobs/REFERENCE003_IDENTITY_REPAIR_R1_20260630/outputs/OP_SHOT_025_R1.png`
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_012_GRANDIS_VEHICLE_ACTION/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_segments/VU_REF003_012_GRANDIS_VEHICLE_ACTION.mp4`

## Primary Direction

Use the reference video clip as the primary source for timing, camera movement,
screen direction, composition function, and transition rhythm. Use the generated
keyframe anchors as the visual remake identity and start/end/mid-frame anchors.
Use the setting chapter and asset lock images as hard identity, prop, vehicle,
animal, symbol, location, and scene-continuity constraints. The AIGC model must
not redesign visible characters, props, vehicles, or recurring environments.

Generate a clean live-action remake segment for `VU_REF003_012_GRANDIS_VEHICLE_ACTION`. Preserve
the reference-003 OP motion and duration while replacing all readable original
text, credits, lyrics, subtitles, broadcaster marks, logos, and watermarks with
clean no-text composition.

## Unit Metadata

- Title: Grandis 车辆动作到群像
- Time range: `00:48.00-00:51.50`
- Whitebox required: `True`
- Roughcut slot: `12`

## Transition Context

- `TE_REF003_022_022_TO_023`: Jean 反应近景 -> Grandis 动作桥 | OP_SHOT_023 begins from the reference-003 timing after OP_SHOT_022: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_023_023_TO_024`: Grandis 动作桥 -> 车辆/飞行器空中动作 | OP_SHOT_024 begins from the reference-003 timing after OP_SHOT_023: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_024_024_TO_025`: 车辆/飞行器空中动作 -> 全员群像 | OP_SHOT_025 begins from the reference-003 timing after OP_SHOT_024: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_025_025_TO_026`: 全员群像 -> Nautilus 水下初现 | OP_SHOT_026 begins from the reference-003 timing after OP_SHOT_025: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

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

## Reject Conditions

- Any readable text, title, credit, lyric, subtitle, NHK/broadcaster mark, logo,
  watermark, or random symbol appears.
- The generated segment ignores the reference clip's timing or screen direction.
- Keyframe anchors are reordered, skipped, or replaced with unrelated imagery.
- Nadia does not match the `OP_SHOT_011_v2` official face lock.
- Any visible character face/costume/age identity, prop, vehicle, animal, symbol,
  or recurring scene structure drifts from the packaged locks.
- Minor characters are aged up, sexualized, or dressed immodestly.
- The MP4 cannot complete-decode.
