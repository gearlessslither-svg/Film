# AIGC Video Generation Brief — VU_REF003_009_MARIE_KING_MEADOW — R5 Expanded Package

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_009_MARIE_KING_MEADOW_reference.mp4`
- Ordered keyframe anchors: 3 total = 2 official + 1 R5 adaptive generated
- 图1 = `R5_VU_REF003_009_MARIE_KING_MEADOW_031000ms_01` (r5_adaptive_generated, 00:31.00, adaptive_primary): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/keyframes/01_R5_VU_REF003_009_MARIE_KING_MEADOW_031000ms_01.png`
  - function: Marie 与 King 草地段: scene-boundary / hard visual turn; visually different from nearest existing anchor; local motion/color change peak
- 图2 = `OP_SHOT_013` (official_keyframe, 00:31.50, 图1 / Marie_King_meadow): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/keyframes/02_OP_SHOT_013.png`
  - function: Marie 与 King 草地笑点
- 图3 = `OP_SHOT_014` (official_keyframe, 00:34.00, 图2 / Marie_King_close): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/keyframes/03_OP_SHOT_014.png`
  - function: Marie 与 King 近景
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_009_MARIE_KING_MEADOW/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_009_MARIE_KING_MEADOW.mp4`

## How To Feed This To The AIGC Video Site

Use the reference clip as the primary timing/camera/motion guide. Use the ordered
keyframe anchors as visual identity, scene, prop, and transition-state locks.
The generated segment should follow the reference clip's motion and duration,
but use the generated keyframes as the remake's visual world.

If the chosen AIGC site cannot accept all ordered images, keep the first and last anchors, then prioritize R5 adaptive anchors and turning-point official anchors. Do not reorder the remaining images.

## Primary Direction

Generate a clean live-action remake segment for `VU_REF003_009_MARIE_KING_MEADOW`. Preserve
the reference-003 OP timing, shot function, screen direction, and edit rhythm.
Replace all readable original text, credits, lyrics, subtitles, broadcaster
marks, logos, and watermarks with clean no-text composition.

Use the setting chapter and packaged asset locks as hard identity, prop,
vehicle, animal, symbol, location, and scene-continuity constraints. The AIGC
model must not redesign visible characters, props, vehicles, or recurring
environments.

## Unit Metadata

- Title: Marie 与 King 草地段
- Time range: `00:31.00-00:34.00`
- Whitebox required: `False`
- Roughcut slot: `9`
- Package type: `reference003_r5_expanded_video_segment`

## Transition Context

- `TE_REF003_012_012_TO_013`: Jean 入场 -> Marie 与 King 草地笑点 | OP_SHOT_013 begins from the reference-003 timing after OP_SHOT_012: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_013_013_TO_014`: Marie 与 King 草地笑点 -> Marie 与 King 近景 | OP_SHOT_014 begins from the reference-003 timing after OP_SHOT_013: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_014_014_TO_015`: Marie 与 King 近景 -> Grandis 三人组宽景 | OP_SHOT_015 begins from the reference-003 timing after OP_SHOT_014: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

# VU_REF003_009_MARIE_KING_MEADOW - Marie 与 King 草地段

- Unit type: `child_animal_meadow_gag`
- Time range: 00:31.00-00:34.00
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_013` (图1 / Marie_King_meadow, 00:31.50): Marie and small lion cub King in a bright meadow, playful and child-safe.
- 图2 = `OP_SHOT_014` (图2 / Marie_King_close, 00:34.00): Cheerful close character beat for Marie and King, safe and non-threatening.

## Script Intent

Marie/King 在草地中做明亮儿童喜剧节奏。

## Frame Relationships

儿童安全、可爱明亮；不生成字幕。

Incoming: TE_REF003_012_012_TO_013  
Intra: TE_REF003_013_013_TO_014  
Outgoing: TE_REF003_014_014_TO_015

## Camera Plan

- Movement: low meadow hold with small playful motion
- Framing: grass foreground, sky and clouds behind
- Lens: low wide child-safe angle
- Screen Direction: playful forward motion
- Focus: Marie and King
- Lighting: bright daylight meadow

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
