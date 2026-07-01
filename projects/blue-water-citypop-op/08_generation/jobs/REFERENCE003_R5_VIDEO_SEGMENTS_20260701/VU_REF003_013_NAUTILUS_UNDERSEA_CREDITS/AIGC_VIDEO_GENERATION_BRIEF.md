# AIGC Video Generation Brief — VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS — R5 Expanded Package

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_reference.mp4`
- Ordered keyframe anchors: 6 total = 3 official + 3 R5 adaptive generated
- 图1 = `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_052000ms_01` (r5_adaptive_generated, 00:52.00, adaptive_primary): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/keyframes/01_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_052000ms_01.png`
  - function: Long undersea Nautilus light-pass has distinct submarine/lighting positions; extra frames preserve scale and light-beam progression.
- 图2 = `OP_SHOT_026` (official_keyframe, 00:52.50, 图1 / undersea_start): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/keyframes/02_OP_SHOT_026.png`
  - function: Nautilus 水下初现
- 图3 = `OP_SHOT_027` (official_keyframe, 00:55.00, 图2 / undersea_pass): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/keyframes/03_OP_SHOT_027.png`
  - function: Nautilus 水下通过
- 图4 = `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_057000ms_03` (r5_adaptive_generated, 00:57.00, adaptive_middle): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/keyframes/04_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_057000ms_03.png`
  - function: Long undersea Nautilus light-pass has distinct submarine/lighting positions; extra frames preserve scale and light-beam progression.
- 图5 = `OP_SHOT_028` (official_keyframe, 00:58.50, 图3 / undersea_shadow): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/keyframes/05_OP_SHOT_028.png`
  - function: Nautilus 深蓝剪影
- 图6 = `R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_060500ms_02` (r5_adaptive_generated, 01:00.50, adaptive_middle): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/keyframes/06_R5_VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS_060500ms_02.png`
  - function: Long undersea Nautilus light-pass has distinct submarine/lighting positions; extra frames preserve scale and light-beam progression.
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS.mp4`

## How To Feed This To The AIGC Video Site

Use the reference clip as the primary timing/camera/motion guide. Use the ordered
keyframe anchors as visual identity, scene, prop, and transition-state locks.
The generated segment should follow the reference clip's motion and duration,
but use the generated keyframes as the remake's visual world.

If the chosen AIGC site cannot accept all ordered images, keep the first and last anchors, then prioritize R5 adaptive anchors and turning-point official anchors. Do not reorder the remaining images.

## Primary Direction

Generate a clean live-action remake segment for `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS`. Preserve
the reference-003 OP timing, shot function, screen direction, and edit rhythm.
Replace all readable original text, credits, lyrics, subtitles, broadcaster
marks, logos, and watermarks with clean no-text composition.

Use the setting chapter and packaged asset locks as hard identity, prop,
vehicle, animal, symbol, location, and scene-continuity constraints. The AIGC
model must not redesign visible characters, props, vehicles, or recurring
environments.

## Unit Metadata

- Title: Nautilus 海底光束段
- Time range: `00:52.00-01:01.00`
- Whitebox required: `True`
- Roughcut slot: `13`
- Package type: `reference003_r5_expanded_video_segment`

## Transition Context

- `TE_REF003_025_025_TO_026`: 全员群像 -> Nautilus 水下初现 | OP_SHOT_026 begins from the reference-003 timing after OP_SHOT_025: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_026_026_TO_027`: Nautilus 水下初现 -> Nautilus 水下通过 | OP_SHOT_027 begins from the reference-003 timing after OP_SHOT_026: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_027_027_TO_028`: Nautilus 水下通过 -> Nautilus 深蓝剪影 | OP_SHOT_028 begins from the reference-003 timing after OP_SHOT_027: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_028_028_TO_029`: Nautilus 深蓝剪影 -> 夜城初现 | OP_SHOT_029 begins from the reference-003 timing after OP_SHOT_028: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

# VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS - Nautilus 海底光束段

- Unit type: `undersea_submarine_sequence`
- Time range: 00:52.00-01:01.00
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `true`

## Ordered Input Images

- 图1 = `OP_SHOT_026` (图1 / undersea_start, 00:52.50): Deep blue underwater light shafts with Nautilus silhouette entering, no credits.
- 图2 = `OP_SHOT_027` (图2 / undersea_pass, 00:55.00): Nautilus passes under shimmering surface light, large but graceful.
- 图3 = `OP_SHOT_028` (图3 / undersea_shadow, 00:58.50): Submarine silhouette deepens in blue water with moving light bands, no text.

## Script Intent

Nautilus 在水下光束中通过，原片有职员表；生成版保留海底运动和光线，去掉文字。

## Frame Relationships

潜艇空间连续和比例重要，文字全部替换为干净水下空间。

Incoming: TE_REF003_025_025_TO_026  
Intra: TE_REF003_026_026_TO_027, TE_REF003_027_027_TO_028  
Outgoing: TE_REF003_028_028_TO_029

## Camera Plan

- Movement: slow underwater tracking pass under shafts of light
- Framing: submarine silhouette and hull moving through deep blue water
- Lens: wide underwater lens
- Screen Direction: submarine crosses consistently
- Focus: submarine scale, water shafts, silhouette
- Lighting: blue underwater shafts

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
