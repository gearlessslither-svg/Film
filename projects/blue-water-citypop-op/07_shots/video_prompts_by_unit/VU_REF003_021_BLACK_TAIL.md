# VU_REF003_021_BLACK_TAIL - 黑场尾帧

- Unit type: `editorial_black_tail`
- Time range: 01:23.50-01:24.44
- Source: `reference-003-full-op-2160p` full OP 1:1 plan
- Whitebox required: `false`

## Ordered Input Images

- 图1 = `OP_SHOT_042` (图1 / black_tail, 01:23.50): Clean black tail frame after the final sky hold.

## Script Intent

OP 结束进入黑场尾帧；不需要生成复杂画面。

## Frame Relationships

编辑黑场，作为结尾。

Incoming: TE_REF003_041_041_TO_042  
Intra: none  
Outgoing: none

## Camera Plan

- Movement: cut to black
- Framing: full black frame
- Lens: none
- Screen Direction: none
- Focus: none
- Lighting: black

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
