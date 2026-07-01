# AIGC Video Generation Brief — VU_REF003_004_AIRCRAFT_BRIEF_REVEAL — R5 Expanded Package

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_reference.mp4`
- Ordered keyframe anchors: 3 total = 1 official + 2 R5 adaptive generated
- 图1 = `R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_014500ms_02` (r5_adaptive_generated, 00:14.50, adaptive_middle): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/keyframes/01_R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_014500ms_02.png`
  - function: Brief aircraft reveal is a fast prop/camera state change; current single anchor does not cover entry and exit/reveal phase.
- 图2 = `OP_SHOT_007` (official_keyframe, 00:15.00, 图1 / aircraft_brief_reveal): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/keyframes/02_OP_SHOT_007.png`
  - function: 飞行器短露
- 图3 = `R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_016000ms_01` (r5_adaptive_generated, 00:16.00, adaptive_primary): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/keyframes/03_R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_016000ms_01.png`
  - function: Brief aircraft reveal is a fast prop/camera state change; current single anchor does not cover entry and exit/reveal phase.
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_004_AIRCRAFT_BRIEF_REVEAL.mp4`

## How To Feed This To The AIGC Video Site

Use the reference clip as the primary timing/camera/motion guide. Use the ordered
keyframe anchors as visual identity, scene, prop, and transition-state locks.
The generated segment should follow the reference clip's motion and duration,
but use the generated keyframes as the remake's visual world.

If the chosen AIGC site cannot accept all ordered images, keep the first and last anchors, then prioritize R5 adaptive anchors and turning-point official anchors. Do not reorder the remaining images.

## Primary Direction

Generate a clean live-action remake segment for `VU_REF003_004_AIRCRAFT_BRIEF_REVEAL`. Preserve
the reference-003 OP timing, shot function, screen direction, and edit rhythm.
Replace all readable original text, credits, lyrics, subtitles, broadcaster
marks, logos, and watermarks with clean no-text composition.

Use the setting chapter and packaged asset locks as hard identity, prop,
vehicle, animal, symbol, location, and scene-continuity constraints. The AIGC
model must not redesign visible characters, props, vehicles, or recurring
environments.

## Unit Metadata

- Title: 飞行器短暂露出
- Time range: `00:14.50-00:16.50`
- Whitebox required: `True`
- Roughcut slot: `4`
- Package type: `reference003_r5_expanded_video_segment`

## Transition Context

- `TE_REF003_006_006_TO_007`: 云层增长填画 -> 飞行器短露 | OP_SHOT_007 begins from the reference-003 timing after OP_SHOT_006: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_007_007_TO_008`: 飞行器短露 -> 主标题无字安全位 | OP_SHOT_008 begins from the reference-003 timing after OP_SHOT_007: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

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

## R5 Expanded Notes

- This package includes R5 adaptive generated frames when they exist for this unit.
- R5 frames are not raw screenshots; they are generated pure-image assets with output paths.
- Keep the ordered images in timeline order. Do not skip a R5 frame that carries a unique transition, action, prop, or identity state unless the video site image limit forces triage.

## Reject Conditions

- Any readable text, title, credit, lyric, subtitle, NHK/broadcaster mark, logo,
  watermark, or random symbol appears.
- The generated segment ignores the reference clip's timing or screen direction.
- Keyframe anchors are reordered, skipped, or replaced with unrelated imagery.
- Nadia does not match the `OP_SHOT_011_v2` official face lock whenever visible.
- Any visible character face/costume/age identity, prop, vehicle, animal, symbol,
  or recurring scene structure drifts from the packaged locks.
- Minor characters are aged up, sexualized, or dressed immodestly.
- The MP4 cannot complete-decode.
