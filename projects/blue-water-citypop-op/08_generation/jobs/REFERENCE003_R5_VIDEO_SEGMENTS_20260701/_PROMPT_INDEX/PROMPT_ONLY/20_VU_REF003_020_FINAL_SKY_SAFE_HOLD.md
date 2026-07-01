# 20 — VU_REF003_020_FINAL_SKY_SAFE_HOLD — 最终无字天空 hold

## Upload These

1. Reference video: `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/reference_clip/VU_REF003_020_FINAL_SKY_SAFE_HOLD_reference.mp4`
2. Ordered keyframes:
- 图1: `OP_SHOT_040` (01:20.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/keyframes/01_OP_SHOT_040.png`
- 图2: `OP_SHOT_041` (01:22.00) `08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/VU_REF003_020_FINAL_SKY_SAFE_HOLD/keyframes/02_OP_SHOT_041.png`
3. Active asset locks:
- none for this unit; rely on reference clip + ordered keyframes + no-text rules.

## Save Result To

`08_generation/outputs/video/reference003_r5_expanded_segments/VU_REF003_020_FINAL_SKY_SAFE_HOLD.mp4`

## Prompt To Use

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
