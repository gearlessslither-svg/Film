# AIGC Video Generation Brief — VU_REF003_020_FINAL_SKY_SAFE_HOLD — R5 Expanded Package

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_020_FINAL_SKY_SAFE_HOLD_reference.mp4`
- Ordered keyframe anchors: 2 total = 2 official + 0 R5 adaptive generated
- 图1 = `OP_SHOT_040` (official_keyframe, 01:20.00, 图1 / final_sky_safe): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/keyframes/01_OP_SHOT_040.png`
  - function: 最终蓝天安全位
- 图2 = `OP_SHOT_041` (official_keyframe, 01:22.00, 图2 / final_sun_hold): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/keyframes/02_OP_SHOT_041.png`
  - function: 最终太阳 hold
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_020_FINAL_SKY_SAFE_HOLD.mp4`

## How To Feed This To The AIGC Video Site

Use the reference clip as the primary timing/camera/motion guide. Use the ordered
keyframe anchors as visual identity, scene, prop, and transition-state locks.
The generated segment should follow the reference clip's motion and duration,
but use the generated keyframes as the remake's visual world.

If the chosen AIGC site cannot accept all ordered images, keep the first and last anchors, then prioritize R5 adaptive anchors and turning-point official anchors. Do not reorder the remaining images.

## Primary Direction

Generate a clean live-action remake segment for `VU_REF003_020_FINAL_SKY_SAFE_HOLD`. Preserve
the reference-003 OP timing, shot function, screen direction, and edit rhythm.
Replace all readable original text, credits, lyrics, subtitles, broadcaster
marks, logos, and watermarks with clean no-text composition.

Use the setting chapter and packaged asset locks as hard identity, prop,
vehicle, animal, symbol, location, and scene-continuity constraints. The AIGC
model must not redesign visible characters, props, vehicles, or recurring
environments.

## Unit Metadata

- Title: 最终无字天空 hold
- Time range: `01:19.50-01:23.00`
- Whitebox required: `False`
- Roughcut slot: `20`
- Package type: `reference003_r5_expanded_video_segment`

## Transition Context

- `TE_REF003_039_039_TO_040`: 水花转蓝天 -> 最终蓝天安全位 | OP_SHOT_040 begins from the reference-003 timing after OP_SHOT_039: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_040_040_TO_041`: 最终蓝天安全位 -> 最终太阳 hold | OP_SHOT_041 begins from the reference-003 timing after OP_SHOT_040: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_041_041_TO_042`: 最终太阳 hold -> 黑场结尾 | OP_SHOT_042 begins from the reference-003 timing after OP_SHOT_041: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

# VU_REF003_020_FINAL_SKY_SAFE_HOLD - 最终无字天空 hold

- Unit type: `final_no_text_sky_hold`
- Time range: 01:19.50-01:23.00
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_040` (图1 / final_sky_safe, 01:20.00): Clean final blue sky card with soft cloud and no text, replacing the broadcaster end card.
- 图2 = `OP_SHOT_041` (图2 / final_sun_hold, 01:22.00): Blue sky with bright sun glow and clear negative space, no logo or text.

## Script Intent

原片 NHK 结束卡在蓝天和太阳上 hold；生成版必须替换为无字最终天空构图。

## Frame Relationships

这里是最终 logo-safe 留白，不生成 NHK 或任何字。

Incoming: TE_REF003_039_039_TO_040  
Intra: TE_REF003_040_040_TO_041  
Outgoing: TE_REF003_041_041_TO_042

## Camera Plan

- Movement: locked final sky hold with sun glow
- Framing: blue sky, sun orb, clean final negative space
- Lens: wide sky plate
- Screen Direction: none
- Focus: sky/sun composition
- Lighting: bright sun glow

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
