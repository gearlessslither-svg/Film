# AIGC Video Generation Brief — VU_REF003_010_GRANDIS_TRIO_INTRO

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_010_GRANDIS_TRIO_INTRO_reference.mp4`
- Ordered keyframe anchors:
- 1. `OP_SHOT_015` at `00:35.50`: Grandis 三人组宽景; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_015.png`
- 2. `OP_SHOT_016` at `00:37.00`: Grandis 三人组近景; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_016_v2.png`
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_010_GRANDIS_TRIO_INTRO/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_segments/VU_REF003_010_GRANDIS_TRIO_INTRO.mp4`

## Primary Direction

Use the reference video clip as the primary source for timing, camera movement,
screen direction, composition function, and transition rhythm. Use the generated
keyframe anchors as the visual remake identity and start/end/mid-frame anchors.
Use the setting chapter and asset lock images as hard identity, prop, vehicle,
animal, symbol, location, and scene-continuity constraints. The AIGC model must
not redesign visible characters, props, vehicles, or recurring environments.

Generate a clean live-action remake segment for `VU_REF003_010_GRANDIS_TRIO_INTRO`. Preserve
the reference-003 OP motion and duration while replacing all readable original
text, credits, lyrics, subtitles, broadcaster marks, logos, and watermarks with
clean no-text composition.

## Unit Metadata

- Title: Grandis 三人组介绍
- Time range: `00:34.50-00:37.50`
- Whitebox required: `False`
- Roughcut slot: `10`

## Transition Context

- `TE_REF003_014_014_TO_015`: Marie 与 King 近景 -> Grandis 三人组宽景 | OP_SHOT_015 begins from the reference-003 timing after OP_SHOT_014: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_015_015_TO_016`: Grandis 三人组宽景 -> Grandis 三人组近景 | OP_SHOT_016 begins from the reference-003 timing after OP_SHOT_015: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_016_016_TO_017`: Grandis 三人组近景 -> Nadia 奔跑脚步 | OP_SHOT_017 begins from the reference-003 timing after OP_SHOT_016: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

# VU_REF003_010_GRANDIS_TRIO_INTRO - Grandis 三人组介绍

- Unit type: `adult_trio_intro_montage`
- Time range: 00:34.50-00:37.50
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_015` (图1 / Grandis_trio_wide, 00:35.50): Grandis, Sanson, and Hanson pose theatrically in a live-action period setting.
- 图2 = `OP_SHOT_016` (图2 / Grandis_trio_close, 00:37.00): Close energetic character beat for the adult trio, playful but grounded.

## Script Intent

Grandis 三人组从姿态到特写，形成戏剧化成人反派/喜剧能量。

## Frame Relationships

成人三人组可夸张但要真人化，不混入儿童段。

Incoming: TE_REF003_014_014_TO_015  
Intra: TE_REF003_015_015_TO_016  
Outgoing: TE_REF003_016_016_TO_017

## Camera Plan

- Movement: hard beat cuts and small theatrical pose shifts
- Framing: wide trio then close group
- Lens: medium portrait/wide plaza lens
- Screen Direction: not continuous; montage rhythm
- Focus: Grandis trio
- Lighting: bright outdoor showy light

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
