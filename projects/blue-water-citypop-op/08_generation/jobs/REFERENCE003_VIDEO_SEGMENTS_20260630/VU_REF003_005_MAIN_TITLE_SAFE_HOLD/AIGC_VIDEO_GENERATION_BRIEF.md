# AIGC Video Generation Brief — VU_REF003_005_MAIN_TITLE_SAFE_HOLD

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_005_MAIN_TITLE_SAFE_HOLD_reference.mp4`
- Ordered keyframe anchors:
- 1. `OP_SHOT_008` at `00:18.50`: 主标题无字安全位; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_008_v2.png`
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_005_MAIN_TITLE_SAFE_HOLD/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_segments/VU_REF003_005_MAIN_TITLE_SAFE_HOLD.mp4`

## Primary Direction

Use the reference video clip as the primary source for timing, camera movement,
screen direction, composition function, and transition rhythm. Use the generated
keyframe anchors as the visual remake identity and start/end/mid-frame anchors.
Use the setting chapter and asset lock images as hard identity, prop, vehicle,
animal, symbol, location, and scene-continuity constraints. The AIGC model must
not redesign visible characters, props, vehicles, or recurring environments.

Generate a clean live-action remake segment for `VU_REF003_005_MAIN_TITLE_SAFE_HOLD`. Preserve
the reference-003 OP motion and duration while replacing all readable original
text, credits, lyrics, subtitles, broadcaster marks, logos, and watermarks with
clean no-text composition.

## Unit Metadata

- Title: 主标题功能位无字 hold
- Time range: `00:17.00-00:22.00`
- Whitebox required: `False`
- Roughcut slot: `5`

## Transition Context

- `TE_REF003_007_007_TO_008`: 飞行器短露 -> 主标题无字安全位 | OP_SHOT_008 begins from the reference-003 timing after OP_SHOT_007: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_008_008_TO_009`: 主标题无字安全位 -> 太阳光线转场 | OP_SHOT_009 begins from the reference-003 timing after OP_SHOT_008: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

# VU_REF003_005_MAIN_TITLE_SAFE_HOLD - 主标题功能位无字 hold

- Unit type: `no_text_title_safe_hold`
- Time range: 00:17.00-00:22.00
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_008` (图1 / main_title_safe_no_text, 00:18.50): Clean blue sky and diagonal cloud band where the original title sits, but completely text-free.

## Script Intent

原片主标题/logo 长 hold；生成版必须替换为无字天空构图，保留标题位功能和节奏。

## Frame Relationships

不得生成原片标题或任何文字；只保留“这里是标题位”的构图功能。

Incoming: TE_REF003_007_007_TO_008  
Intra: none  
Outgoing: TE_REF003_008_008_TO_009

## Camera Plan

- Movement: locked or subtle drifting sky hold
- Framing: clean central title-safe negative space over sky/cloud band
- Lens: wide graphic sky plate
- Screen Direction: minimal drift
- Focus: sky and cloud geometry
- Lighting: bright blue sky

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
