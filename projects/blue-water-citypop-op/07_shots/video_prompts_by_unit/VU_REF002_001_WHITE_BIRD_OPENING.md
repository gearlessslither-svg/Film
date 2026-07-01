# VU_REF002_001_WHITE_BIRD_OPENING - 参考片白鸟开场长段

- Unit type: `single_subject_motion_sequence`
- Time range: 00:00-00:04.50
- Source: reference-002-opening bounded local analysis
- Whitebox required: `false`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_001` (图1 / bird_foreground_start): 白鸟近景掠过蓝天，第一帧即有运动主体。
- 图2 = `OP_SHOT_002` (图2 / bird_glide_continuation): 同一白鸟拉开距离，在蓝天中持续滑翔。

## 剧本镜头意图 / Script Intent

reference-002 不是先空云层，而是白鸟从第一帧起控制画面；用长时间蓝天白鸟运动建立歌曲入口。

## 帧间关系 / Frame Relationships

图1和图2必须像同一只白鸟的连续开场，不要变成空云层开场，也不要提前出现飞机。

Incoming edges: none  
Intra-unit edges: TE_REF002_001_BIRD_FOREGROUND_TO_GLIDE  
Outgoing edges: TE_REF002_002_BIRD_TO_CREDIT_SAFE

## 镜头计划 / Camera Plan

- Movement: locked-to-gentle-follow sky camera; bird crosses foreground then settles into readable glide
- Framing: 21:9 blue sky, white bird dominant at start then mid-distance
- Lens: wide anamorphic sky plate, deep focus
- Screen Direction: bird motion stays consistent across the first two images
- Focus: white bird silhouette against clean blue sky
- Lighting: clean saturated daylight, no title text or subtitles

## AIGC Video Prompt

Use the ordered images exactly as listed above. Follow the reference-002 timing for this unit and preserve the scripted function over any previous generated still. Do not generate readable title text, logo, subtitles, watermark, random letters, or direct animation screenshot copying. Keep motion, sky direction, scale, and light transitions consistent with the listed transition edges.

## Generation Requirements

- Use reference-002-opening timing as the active evidence for 00:00-00:23; do not reuse the superseded 24s one-take timing.
- Pure image/video generation must be title-safe: no readable Japanese title, no NHK logo, no subtitles, no watermark, no random text.
- Maintain the selected C-version Nadia lock whenever Nadia appears: 14-year-old, honey-tan skin, short navy-black bob, gold earrings/bangles, red-orange/white adventure outfit, Blue Water pendant, non-sexualized.
- Treat the previous generated stills as replaceable material evidence, not as the source of timing truth.

## Negative / Failure Conditions

- 如果开场第一眼没有白鸟则失败。
- 如果飞机或标题字在 00:00-00:04.5 出现则失败。
