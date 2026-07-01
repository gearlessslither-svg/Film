# VU_REF002_002_BIRD_CREDIT_SAFE_SKY - 白鸟带出无字职员表安全位

- Unit type: `title_safe_hold`
- Time range: 00:05.00-00:08.50
- Source: reference-002-opening bounded local analysis
- Whitebox required: `false`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_003` (图1 / bird_credit_safe_negative_space): 白鸟继续在蓝天中缩小，画面中部保留干净无字留白。

## 剧本镜头意图 / Script Intent

参考片此处有文字叠加和白鸟继续运动；纯生成必须只保留构图节奏和留白，不生成任何可读文字。

## 帧间关系 / Frame Relationships

用负空间替代参考里的可读职员表；节奏是 hold，不是新剧情镜头。

Incoming edges: TE_REF002_002_BIRD_TO_CREDIT_SAFE  
Intra-unit edges: none  
Outgoing edges: TE_REF002_003_CREDIT_SAFE_TO_CLOUD_BANK

## 镜头计划 / Camera Plan

- Movement: mostly locked sky hold with subtle bird drift
- Framing: blue sky with clean center negative space, bird small and low/right over time
- Lens: wide anamorphic, graphic flat sky field
- Screen Direction: same bird direction from opening unit
- Focus: bird silhouette and clean sky field
- Lighting: even blue daylight

## AIGC Video Prompt

Use the ordered images exactly as listed above. Follow the reference-002 timing for this unit and preserve the scripted function over any previous generated still. Do not generate readable title text, logo, subtitles, watermark, random letters, or direct animation screenshot copying. Keep motion, sky direction, scale, and light transitions consistent with the listed transition edges.

## Generation Requirements

- Use reference-002-opening timing as the active evidence for 00:00-00:23; do not reuse the superseded 24s one-take timing.
- Pure image/video generation must be title-safe: no readable Japanese title, no NHK logo, no subtitles, no watermark, no random text.
- Maintain the selected C-version Nadia lock whenever Nadia appears: 14-year-old, honey-tan skin, short navy-black bob, gold earrings/bangles, red-orange/white adventure outfit, Blue Water pendant, non-sexualized.
- Treat the previous generated stills as replaceable material evidence, not as the source of timing truth.

## Negative / Failure Conditions

- 出现任何可读字、logo、字幕、水印则失败。
- 如果白鸟方向与前一 unit 无关则失败。
