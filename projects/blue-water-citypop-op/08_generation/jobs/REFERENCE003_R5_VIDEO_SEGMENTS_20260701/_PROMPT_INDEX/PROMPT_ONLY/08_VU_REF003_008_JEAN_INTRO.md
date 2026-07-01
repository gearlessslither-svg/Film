# 08 — VU_REF003_008_JEAN_INTRO — Jean 帽子与少年发明家入场

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_008_JEAN_INTRO/reference_clip/VU_REF003_008_JEAN_INTRO_reference.mp4`
2. Ordered keyframes:
- 图1: `R5_VU_REF003_008_JEAN_INTRO_028500ms_02` (00:28.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_008_JEAN_INTRO/keyframes/01_R5_VU_REF003_008_JEAN_INTRO_028500ms_02.png`
- 图2: `OP_SHOT_012` (00:29.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_008_JEAN_INTRO/keyframes/02_OP_SHOT_012.png`
- 图3: `R5_VU_REF003_008_JEAN_INTRO_030500ms_01` (00:30.50) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_008_JEAN_INTRO/keyframes/03_R5_VU_REF003_008_JEAN_INTRO_030500ms_01.png`
3. Active asset locks:
- `jean` (official_identity_lock): `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/characters_jean.png`

## Save Result To

`08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_008_JEAN_INTRO.mp4`

## Prompt To Use

# VU_REF003_008_JEAN_INTRO - Jean 帽子与少年发明家入场

- Unit type: `character_intro_pair`
- Time range: 00:28.00-00:30.50
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_012` (图1 / Jean_hat_face, 00:29.00): Jean, 14-year-old French inventor boy, looks up from under a blue cap with round glasses and red bow tie.

## Script Intent

Jean 从帽檐/眼睛到正面少年发明家形象入场。

## Frame Relationships

Jean 保持 14 岁少年发明家，不要成人化。

Incoming: TE_REF003_011_011_TO_012  
Intra: none  
Outgoing: TE_REF003_012_012_TO_013

## Camera Plan

- Movement: hat brim/face reveal with small gesture
- Framing: close to medium portrait against sky
- Lens: portrait lens
- Screen Direction: upward look and hat gesture
- Focus: glasses and eyes
- Lighting: bright outdoor daylight

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
