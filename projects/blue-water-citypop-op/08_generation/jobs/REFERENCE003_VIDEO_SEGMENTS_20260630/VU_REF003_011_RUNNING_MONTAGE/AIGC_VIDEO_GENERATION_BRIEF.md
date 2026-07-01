# AIGC Video Generation Brief — VU_REF003_011_RUNNING_MONTAGE

## Required Inputs

- Reference video clip: `reference_clip/VU_REF003_011_RUNNING_MONTAGE_reference.mp4`
- Ordered keyframe anchors:
- 1. `OP_SHOT_017` at `00:38.00`: Nadia 奔跑脚步; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_017.png`
- 2. `OP_SHOT_018` at `00:39.50`: Nadia 奔跑正面; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH03/outputs/OP_SHOT_018.png`
- 3. `OP_SHOT_019` at `00:41.50`: Jean 奔跑; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_019.png`
- 4. `OP_SHOT_020` at `00:43.50`: Marie 奔跑; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_020.png`
- 5. `OP_SHOT_021` at `00:45.50`: 全员奔跑; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_021_v2.png`
- 6. `OP_SHOT_022` at `00:47.50`: Jean 反应近景; anchor image `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH04/outputs/OP_SHOT_022.png`
- Setting chapter: `05_asset_bible/setting_chapters/reference003_setting_chapter_v1.md`
- Asset lock manifest: `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json`
- Packaged identity/asset lock images:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/characters_king.png`
- `grandis` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/characters_grandis.png`
- `sanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/characters_sanson.png`
- `hanson` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/characters_hanson.png`
- `nemo` (official_identity_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/characters_nemo.png`
- `electra` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `gargoyle` (needs_setting_lock): no image lock yet; do not invent a clear new design.
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/props_vehicles_symbols_blue_water_pendant.png`
- `white_bird` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/props_vehicles_symbols_white_bird.png`
- `jean_aircraft` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/props_vehicles_symbols_jean_aircraft.png`
- `grandis_vehicle` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/props_vehicles_symbols_grandis_vehicle.png`
- `nautilus` (official_prop_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/props_vehicles_symbols_nautilus.png`
- `blue_grid_geometry` (official_scene_symbol_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/props_vehicles_symbols_blue_grid_geometry.png`
- `water_burst_transition` (official_transition_lock): `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_011_RUNNING_MONTAGE/asset_locks/props_vehicles_symbols_water_burst_transition.png`
- Expected output path: `08_generation/outputs/video/reference003_segments/VU_REF003_011_RUNNING_MONTAGE.mp4`

## Primary Direction

Use the reference video clip as the primary source for timing, camera movement,
screen direction, composition function, and transition rhythm. Use the generated
keyframe anchors as the visual remake identity and start/end/mid-frame anchors.
Use the setting chapter and asset lock images as hard identity, prop, vehicle,
animal, symbol, location, and scene-continuity constraints. The AIGC model must
not redesign visible characters, props, vehicles, or recurring environments.

Generate a clean live-action remake segment for `VU_REF003_011_RUNNING_MONTAGE`. Preserve
the reference-003 OP motion and duration while replacing all readable original
text, credits, lyrics, subtitles, broadcaster marks, logos, and watermarks with
clean no-text composition.

## Unit Metadata

- Title: 角色奔跑 montage
- Time range: `00:38.00-00:47.50`
- Whitebox required: `False`
- Roughcut slot: `11`

## Transition Context

- `TE_REF003_016_016_TO_017`: Grandis 三人组近景 -> Nadia 奔跑脚步 | OP_SHOT_017 begins from the reference-003 timing after OP_SHOT_016: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_017_017_TO_018`: Nadia 奔跑脚步 -> Nadia 奔跑正面 | OP_SHOT_018 begins from the reference-003 timing after OP_SHOT_017: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_018_018_TO_019`: Nadia 奔跑正面 -> Jean 奔跑 | OP_SHOT_019 begins from the reference-003 timing after OP_SHOT_018: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_019_019_TO_020`: Jean 奔跑 -> Marie 奔跑 | OP_SHOT_020 begins from the reference-003 timing after OP_SHOT_019: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_020_020_TO_021`: Marie 奔跑 -> 全员奔跑 | OP_SHOT_021 begins from the reference-003 timing after OP_SHOT_020: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_021_021_TO_022`: 全员奔跑 -> Jean 反应近景 | OP_SHOT_022 begins from the reference-003 timing after OP_SHOT_021: preserve the cut/motion function, but keep the generated remake no-text/no-logo.
- `TE_REF003_022_022_TO_023`: Jean 反应近景 -> Grandis 动作桥 | OP_SHOT_023 begins from the reference-003 timing after OP_SHOT_022: preserve the cut/motion function, but keep the generated remake no-text/no-logo.

## Existing Unit Prompt

# VU_REF003_011_RUNNING_MONTAGE - 角色奔跑 montage

- Unit type: `running_montage_sequence`
- Time range: 00:38.00-00:47.50
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_017` (图1 / Nadia_run_feet, 00:38.00): Nadia running feet/legs beat with sky background, modest costume, no body emphasis.
- 图2 = `OP_SHOT_018` (图2 / Nadia_run_front, 00:39.50): Nadia running front/upper-body beat, determined and age-safe.
- 图3 = `OP_SHOT_019` (图3 / Jean_run, 00:41.50): Jean runs with cap/glasses and inventor outfit, matching the run direction.
- 图4 = `OP_SHOT_020` (图4 / Marie_run, 00:43.50): Marie runs with King nearby, playful and child-safe.
- 图5 = `OP_SHOT_021` (图5 / group_run, 00:45.50): Core group runs together across a grassy ridge or open bright landscape.
- 图6 = `OP_SHOT_022` (图6 / Jean_reaction_close, 00:47.50): Jean close reaction on the running beat, still part of the montage.

## Script Intent

Nadia、Jean、Marie/King 和全员奔跑按音乐节拍切换；这是 montage，不是一镜到底。

## Frame Relationships

保持奔跑方向和节拍，禁止平滑成一镜到底。

Incoming: TE_REF003_016_016_TO_017  
Intra: TE_REF003_017_017_TO_018, TE_REF003_018_018_TO_019, TE_REF003_019_019_TO_020, TE_REF003_020_020_TO_021, TE_REF003_021_021_TO_022  
Outgoing: TE_REF003_022_022_TO_023

## Camera Plan

- Movement: hard beat cuts with matching left-right run energy
- Framing: feet/torso/portrait/group wide beats
- Lens: mixed close and medium-wide lenses
- Screen Direction: mostly left-to-right running continuity
- Focus: runner identity and motion
- Lighting: bright sky/plaza daylight

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
