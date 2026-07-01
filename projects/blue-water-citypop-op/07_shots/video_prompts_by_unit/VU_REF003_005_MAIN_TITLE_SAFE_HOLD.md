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
