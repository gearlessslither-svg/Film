# VU_REF002_004_TITLE_SAFE_HOLD_TO_FLARE - 无字标题安全 hold 到光线转场

- Unit type: `title_safe_hold_with_light_transition`
- Time range: 00:14.50-00:21.00
- Source: reference-002-opening bounded local analysis
- Whitebox required: `false`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_006` (图1 / no_text_title_safe_hold): 干净蓝天和云带形成标题功能位，但没有任何可读标题或 logo；结尾准备太阳光线。

## 剧本镜头意图 / Script Intent

参考片 14.5-19.5 是主标题/logo hold，20-21 秒转光线；生成版只能保留天空、留白、鸟/飞行器小比例和光线节奏，不能生成标题。

## 帧间关系 / Frame Relationships

用无字构图替代 logo；光线只负责把画面带到 Nadia，不要在纯生成里写标题。

Incoming edges: TE_REF002_005_AIRCRAFT_TO_TITLE_SAFE  
Intra-unit edges: none  
Outgoing edges: TE_REF002_006_TITLE_FLARE_TO_NADIA

## 镜头计划 / Camera Plan

- Movement: mostly locked title-safe hold, then light rays bloom toward the outgoing transition
- Framing: large clean center negative space, clouds and tiny aircraft/bird only as rhythm anchors
- Lens: wide graphic sky composition
- Screen Direction: sky drift continues from aircraft reveal without becoming a chase shot
- Focus: clean title-safe sky plane and controlled flare
- Lighting: blue sky hold warming into sun rays

## AIGC Video Prompt

Use the ordered images exactly as listed above. Follow the reference-002 timing for this unit and preserve the scripted function over any previous generated still. Do not generate readable title text, logo, subtitles, watermark, random letters, or direct animation screenshot copying. Keep motion, sky direction, scale, and light transitions consistent with the listed transition edges.

## Generation Requirements

- Use reference-002-opening timing as the active evidence for 00:00-00:23; do not reuse the superseded 24s one-take timing.
- Pure image/video generation must be title-safe: no readable Japanese title, no NHK logo, no subtitles, no watermark, no random text.
- Maintain the selected C-version Nadia lock whenever Nadia appears: 14-year-old, honey-tan skin, short navy-black bob, gold earrings/bangles, red-orange/white adventure outfit, Blue Water pendant, non-sexualized.
- Treat the previous generated stills as replaceable material evidence, not as the source of timing truth.

## Negative / Failure Conditions

- 出现可读标题、logo、字幕、水印则失败。
- 如果光线没有把情绪带向 Nadia 入场则失败。
