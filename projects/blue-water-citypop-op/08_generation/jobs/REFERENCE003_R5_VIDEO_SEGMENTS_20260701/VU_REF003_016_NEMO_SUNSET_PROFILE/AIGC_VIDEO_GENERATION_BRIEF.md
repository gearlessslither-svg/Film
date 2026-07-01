# AIGC Video Generation Brief — VU_REF003_016_NEMO_SUNSET_PROFILE — R5 Expanded Package

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_016_NEMO_SUNSET_PROFILE_reference.mp4`
- Ordered keyframe anchors: 2 total = 2 official + 0 R5 adaptive generated
- 图1 = `OP_SHOT_032` (official_keyframe, 01:06.50, 图1 / Nemo_profile_start): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/keyframes/01_OP_SHOT_032.png`
  - function: Nemo 夕景初入
- 图2 = `OP_SHOT_033` (official_keyframe, 01:09.50, 图2 / Nemo_profile_hold): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/keyframes/02_OP_SHOT_033.png`
  - function: Nemo 夕景 hold
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_016_NEMO_SUNSET_PROFILE/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_016_NEMO_SUNSET_PROFILE.mp4`

## How To Feed This To The AIGC Video Site

Use the reference clip as the primary timing/camera/motion guide. Use the ordered
keyframe anchors as visual identity, scene, prop, and transition-state locks.
The generated segment should follow the reference clip's motion and duration,
but use the generated keyframes as the remake's visual world.

If the chosen AIGC site cannot accept all ordered images, keep the first and last anchors, then prioritize R5 adaptive anchors and turning-point official anchors. Do not reorder the remaining images.

## Primary Direction

Generate a clean live-action remake segment for `VU_REF003_016_NEMO_SUNSET_PROFILE`. Preserve
the reference-003 OP timing, shot function, screen direction, and edit rhythm.
Replace all readable original text, credits, lyrics, subtitles, broadcaster
marks, logos, and watermarks with clean no-text composition.

Use the setting chapter and packaged asset locks as hard identity, prop,
vehicle, animal, symbol, location, and scene-continuity constraints. The AIGC
model must not redesign visible characters, props, vehicles, or recurring
environments.

## Unit Metadata

- Title: Nemo 夕景船长肖像
- Time range: `01:06.50-01:11.00`
- Whitebox required: `False`
- Roughcut slot: `16`
- Package type: `reference003_r5_expanded_video_segment`

## Transition Context

- `TE_REF003_031_031_TO_032`: 夜航飞行器 -> Nemo 夕景初入 | OP_SHOT_032 begins from the reference-003 timing after OP_SHOT_031: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_032_032_TO_033`: Nemo 夕景初入 -> Nemo 夕景 hold | OP_SHOT_033 begins from the reference-003 timing after OP_SHOT_032: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_033_033_TO_034`: Nemo 夕景 hold -> Nadia 庄重正面 | OP_SHOT_034 begins from the reference-003 timing after OP_SHOT_033: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

# VU_REF003_016_NEMO_SUNSET_PROFILE - Nemo 夕景船长肖像

- Unit type: `adult_portrait_hold`
- Time range: 01:06.50-01:11.00
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_032` (图1 / Nemo_profile_start, 01:06.50): Stern adult submarine captain in dark uniform and white cap against sunset sky, no text.
- 图2 = `OP_SHOT_033` (图2 / Nemo_profile_hold, 01:09.50): Nemo holds a dignified profile at sunset, wind and coat shape clear.

## Script Intent

Nemo/船长在夕景中沉稳长 hold，成人角色威严。

## Frame Relationships

成人肖像，不要加入 karaoke/credits text。

Incoming: TE_REF003_031_031_TO_032  
Intra: TE_REF003_032_032_TO_033  
Outgoing: TE_REF003_033_033_TO_034

## Camera Plan

- Movement: portrait hold with subtle push or wind
- Framing: low-angle adult captain portrait at sunset
- Lens: portrait/medium lens
- Screen Direction: gaze off horizon
- Focus: face, hat, uniform silhouette
- Lighting: warm sunset sky

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
