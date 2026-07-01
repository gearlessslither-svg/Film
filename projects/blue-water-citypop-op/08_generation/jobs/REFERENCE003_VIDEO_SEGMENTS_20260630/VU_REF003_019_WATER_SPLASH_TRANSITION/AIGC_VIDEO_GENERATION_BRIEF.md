# AIGC Video Generation Brief — VU_REF003_019_WATER_SPLASH_TRANSITION

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_019_WATER_SPLASH_TRANSITION_reference.mp4`
- Ordered keyframe anchors:
- 1. `OP_SHOT_038` at `01:18.00`: 水花爆发; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_038.png`
- 2. `OP_SHOT_039` at `01:19.00`: 水花转蓝天; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_039.png`
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_019_WATER_SPLASH_TRANSITION/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_segments/VU_REF003_019_WATER_SPLASH_TRANSITION.mp4`

## Primary Direction

Use the reference video clip as the primary source for timing, camera movement,
screen direction, composition function, and transition rhythm. Use the generated
keyframe anchors as the visual remake identity and start/end/mid-frame anchors.
Use the setting chapter and asset lock images as hard identity, prop, vehicle,
animal, symbol, location, and scene-continuity constraints. The AIGC model must
not redesign visible characters, props, vehicles, or recurring environments.

Generate a clean live-action remake segment for `VU_REF003_019_WATER_SPLASH_TRANSITION`. Preserve
the reference-003 OP motion and duration while replacing all readable original
text, credits, lyrics, subtitles, broadcaster marks, logos, and watermarks with
clean no-text composition.

## Unit Metadata

- Title: 水花爆发转天空
- Time range: `01:17.50-01:19.50`
- Whitebox required: `False`
- Roughcut slot: `19`

## Transition Context

- `TE_REF003_037_037_TO_038`: 水下蓝色纹理 -> 水花爆发 | OP_SHOT_038 begins from the reference-003 timing after OP_SHOT_037: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_038_038_TO_039`: 水花爆发 -> 水花转蓝天 | OP_SHOT_039 begins from the reference-003 timing after OP_SHOT_038: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_039_039_TO_040`: 水花转蓝天 -> 最终蓝天安全位 | OP_SHOT_040 begins from the reference-003 timing after OP_SHOT_039: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

# VU_REF003_019_WATER_SPLASH_TRANSITION - 水花爆发转天空

- Unit type: `water_burst_transition`
- Time range: 01:17.50-01:19.50
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_038` (图1 / water_burst, 01:18.00): Bright water/ice-like burst fills frame with blue-white motion, no text.
- 图2 = `OP_SHOT_039` (图2 / splash_to_sky, 01:19.00): Water streaks clear into blue sky and white cloud fragments.

## Script Intent

水体/冰蓝爆发把画面带回天空终段。

## Frame Relationships

动态水花转场，禁止文字。

Incoming: TE_REF003_037_037_TO_038  
Intra: TE_REF003_038_038_TO_039  
Outgoing: TE_REF003_039_039_TO_040

## Camera Plan

- Movement: bursting water transition into sky
- Framing: water splash fills frame then opens to blue sky/cloud
- Lens: wide dynamic transition
- Screen Direction: upward energy
- Focus: water edge and sky reveal
- Lighting: bright blue/white

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
