# AIGC Video Generation Brief — VU_REF003_007_NADIA_PROFILE_ENTRY — R5 Expanded Package

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_007_NADIA_PROFILE_ENTRY_reference.mp4`
- Ordered keyframe anchors: 3 total = 2 official + 1 R5 adaptive generated
- 图1 = `OP_SHOT_010` (official_keyframe, 00:24.50, 图1 / Nadia_profile): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/keyframes/01_OP_SHOT_010.png`
  - function: Nadia 侧脸入场
- 图2 = `OP_SHOT_011` (official_keyframe, 00:27.00, 图2 / Nadia_close): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/keyframes/02_OP_SHOT_011.png`
  - function: Nadia 正面近景
- 图3 = `R5_VU_REF003_007_NADIA_PROFILE_ENTRY_027500ms_01` (r5_adaptive_generated, 00:27.50, adaptive_primary): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/keyframes/03_R5_VU_REF003_007_NADIA_PROFILE_ENTRY_027500ms_01.png`
  - function: Nadia 侧脸入场到近景: scene-boundary / hard visual turn; visually different from nearest existing anchor; local motion/color change peak
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_007_NADIA_PROFILE_ENTRY/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_007_NADIA_PROFILE_ENTRY.mp4`

## How To Feed This To The AIGC Video Site

Use the reference clip as the primary timing/camera/motion guide. Use the ordered
keyframe anchors as visual identity, scene, prop, and transition-state locks.
The generated segment should follow the reference clip's motion and duration,
but use the generated keyframes as the remake's visual world.

If the chosen AIGC site cannot accept all ordered images, keep the first and last anchors, then prioritize R5 adaptive anchors and turning-point official anchors. Do not reorder the remaining images.

## Primary Direction

Generate a clean live-action remake segment for `VU_REF003_007_NADIA_PROFILE_ENTRY`. Preserve
the reference-003 OP timing, shot function, screen direction, and edit rhythm.
Replace all readable original text, credits, lyrics, subtitles, broadcaster
marks, logos, and watermarks with clean no-text composition.

Use the setting chapter and packaged asset locks as hard identity, prop,
vehicle, animal, symbol, location, and scene-continuity constraints. The AIGC
model must not redesign visible characters, props, vehicles, or recurring
environments.

## Unit Metadata

- Title: Nadia 侧脸入场到近景
- Time range: `00:24.00-00:27.50`
- Whitebox required: `False`
- Roughcut slot: `7`
- Package type: `reference003_r5_expanded_video_segment`

## Transition Context

- `TE_REF003_009_009_TO_010`: 太阳光线转场 -> Nadia 侧脸入场 | OP_SHOT_010 begins from the reference-003 timing after OP_SHOT_009: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_010_010_TO_011`: Nadia 侧脸入场 -> Nadia 正面近景 | OP_SHOT_011 begins from the reference-003 timing after OP_SHOT_010: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_011_011_TO_012`: Nadia 正面近景 -> Jean 入场 | OP_SHOT_012 begins from the reference-003 timing after OP_SHOT_011: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

# VU_REF003_007_NADIA_PROFILE_ENTRY - Nadia 侧脸入场到近景

- Unit type: `character_profile_sequence`
- Time range: 00:24.00-00:27.50
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_010` (图1 / Nadia_profile, 00:24.50): Age-appropriate Nadia C-version in side/profile close-up after the sun transition, sky behind.
- 图2 = `OP_SHOT_011` (图2 / Nadia_close, 00:27.00): Nadia turns into a closer bright expression, Blue Water identity detail may be visible, non-sexualized.

## Script Intent

Nadia 首次人物入场，侧脸/回头/近景构成第一段角色介绍。

## Frame Relationships

Nadia C 版锁定，14 岁、安全、保守；保留侧脸入场节奏。

Incoming: TE_REF003_009_009_TO_010  
Intra: TE_REF003_010_010_TO_011  
Outgoing: TE_REF003_011_011_TO_012

## Camera Plan

- Movement: small portrait hold and push/angle shift
- Framing: profile to closer face, sky/stone background
- Lens: portrait lens
- Screen Direction: Nadia gaze changes across the beat
- Focus: Nadia face and earrings/pendant details
- Lighting: bright sky bounce

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
