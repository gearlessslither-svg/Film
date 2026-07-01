# 11 — VU_REF003_011_RUNNING_MONTAGE — 角色奔跑 montage

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_011_RUNNING_MONTAGE/reference_clip/VU_REF003_011_RUNNING_MONTAGE_reference.mp4`
2. Ordered keyframes:
- 图1: `OP_SHOT_017` (00:38.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_011_RUNNING_MONTAGE/keyframes/01_OP_SHOT_017.png`
- 图2: `OP_SHOT_018` (00:39.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_011_RUNNING_MONTAGE/keyframes/02_OP_SHOT_018.png`
- 图3: `OP_SHOT_019` (00:41.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_011_RUNNING_MONTAGE/keyframes/03_OP_SHOT_019.png`
- 图4: `OP_SHOT_020` (00:43.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_011_RUNNING_MONTAGE/keyframes/04_OP_SHOT_020.png`
- 图5: `OP_SHOT_021` (00:45.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_011_RUNNING_MONTAGE/keyframes/05_OP_SHOT_021.png`
- 图6: `OP_SHOT_022` (00:47.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_011_RUNNING_MONTAGE/keyframes/06_OP_SHOT_022.png`
3. Active asset locks:
- `nadia` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/characters_nadia.png`
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/characters_jean.png`
- `marie` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/characters_marie.png`
- `king` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/characters_king.png`
- `blue_water_pendant` (official_prop_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/props_vehicles_symbols_blue_water_pendant.png`

## Save Result To

`08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_011_RUNNING_MONTAGE.mp4`

## Prompt To Use

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
