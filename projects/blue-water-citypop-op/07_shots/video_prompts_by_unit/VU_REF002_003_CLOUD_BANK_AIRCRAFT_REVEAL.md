# VU_REF002_003_CLOUD_BANK_AIRCRAFT_REVEAL - 云层填画到飞行器短露

- Unit type: `spatial_reveal_pair`
- Time range: 00:09.00-00:14.00
- Source: reference-002-opening bounded local analysis
- Whitebox required: `true`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_004` (图1 / cloud_bank_with_bird_exit): 大片白云从画面右侧/上方扩张，白鸟被云层吞入或掠过。
- 图2 = `OP_SHOT_005` (图2 / brief_aircraft_reveal): Jean 式复古飞行器只短暂露出，保持小比例和参考片的短促存在。

## 剧本镜头意图 / Script Intent

reference-002 在 09-12 秒让云层扩张填满画面，12.5-14 秒才短暂露出飞行器；飞行器不能抢成整段主角。

## 帧间关系 / Frame Relationships

这是云层与飞行器的短桥，不是一镜到底飞行器预演；先用简单 Blender/白模锁比例再交给 AIGC 视频补运动。

Incoming edges: TE_REF002_003_CREDIT_SAFE_TO_CLOUD_BANK  
Intra-unit edges: TE_REF002_004_CLOUD_BANK_TO_AIRCRAFT  
Outgoing edges: TE_REF002_005_AIRCRAFT_TO_TITLE_SAFE

## 镜头计划 / Camera Plan

- Movement: cloud bank grows across frame, then a brief tilt/pan reveals the small aircraft for only a short beat
- Framing: clouds dominate first; aircraft is small and secondary, never a 24s tracking hero
- Lens: wide sky lens with enough scale proof for cloud/aircraft relation
- Screen Direction: bird/cloud motion hands off to aircraft without axis flip
- Focus: cloud mass first, aircraft readable but not dominant
- Lighting: blue daylight with bright cloud whites

## AIGC Video Prompt

Use the ordered images exactly as listed above. Follow the reference-002 timing for this unit and preserve the scripted function over any previous generated still. Do not generate readable title text, logo, subtitles, watermark, random letters, or direct animation screenshot copying. Keep motion, sky direction, scale, and light transitions consistent with the listed transition edges.

## Generation Requirements

- Use reference-002-opening timing as the active evidence for 00:00-00:23; do not reuse the superseded 24s one-take timing.
- Pure image/video generation must be title-safe: no readable Japanese title, no NHK logo, no subtitles, no watermark, no random text.
- Maintain the selected C-version Nadia lock whenever Nadia appears: 14-year-old, honey-tan skin, short navy-black bob, gold earrings/bangles, red-orange/white adventure outfit, Blue Water pendant, non-sexualized.
- Treat the previous generated stills as replaceable material evidence, not as the source of timing truth.
- Use Blender/simple previs before final video if aircraft scale or axis is uncertain.

## Negative / Failure Conditions

- 如果飞行器占满 00:09-00:14 或变成主角则失败。
- 如果云层扩张节奏缺失则失败。
