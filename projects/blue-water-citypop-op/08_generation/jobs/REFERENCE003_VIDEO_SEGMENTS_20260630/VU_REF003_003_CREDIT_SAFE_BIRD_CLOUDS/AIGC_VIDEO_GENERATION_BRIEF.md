# AIGC Video Generation Brief — VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS_reference.mp4`
- Ordered keyframe anchors:
- 1. `OP_SHOT_005` at `00:07.50`: 无字职员表安全位; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630/outputs/OP_SHOT_005.png`
- 2. `OP_SHOT_006` at `00:11.50`: 云层增长填画; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630/outputs/OP_SHOT_006_v2.png`
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_segments/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS.mp4`

## Primary Direction

Use the reference video clip as the primary source for timing, camera movement,
screen direction, composition function, and transition rhythm. Use the generated
keyframe anchors as the visual remake identity and start/end/mid-frame anchors.
Use the setting chapter and asset lock images as hard identity, prop, vehicle,
animal, symbol, location, and scene-continuity constraints. The AIGC model must
not redesign visible characters, props, vehicles, or recurring environments.

Generate a clean live-action remake segment for `VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS`. Preserve
the reference-003 OP motion and duration while replacing all readable original
text, credits, lyrics, subtitles, broadcaster marks, logos, and watermarks with
clean no-text composition.

## Unit Metadata

- Title: 白鸟字幕安全位与云层增长
- Time range: `00:07.00-00:14.00`
- Whitebox required: `False`
- Roughcut slot: `3`

## Transition Context

- `TE_REF003_004_004_TO_005`: 白鸟滑翔延续 -> 无字职员表安全位 | OP_SHOT_005 begins from the reference-003 timing after OP_SHOT_004: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_005_005_TO_006`: 无字职员表安全位 -> 云层增长填画 | OP_SHOT_006 begins from the reference-003 timing after OP_SHOT_005: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_006_006_TO_007`: 云层增长填画 -> 飞行器短露 | OP_SHOT_007 begins from the reference-003 timing after OP_SHOT_006: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

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
