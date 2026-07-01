# VU_REF002_005_NADIA_CLOSEUP_ENTRY - 光线落到 Nadia 侧脸近景

- Unit type: `character_entry_insert`
- Time range: 00:21.50-00:23.00
- Source: reference-002-opening bounded local analysis
- Whitebox required: `false`

## 输入图片顺序 / Ordered Input Images

- 图1 = `OP_SHOT_007` (图1 / Nadia_profile_entry): Nadia C 版少女侧脸/近景从光线后出现，年龄安全、服装保守、Blue Water 可作为小型识别点。

## 剧本镜头意图 / Script Intent

reference-002 末尾从太阳光线切到 Nadia 身体/侧脸；本段只建立 heroine entry，不扩展为完整角色 montage。

## 帧间关系 / Frame Relationships

Nadia 是 21.5 秒后才进入的第一个人物，不要提前把角色 montage 塞到 12 秒。

Incoming edges: TE_REF002_006_TITLE_FLARE_TO_NADIA  
Intra-unit edges: none  
Outgoing edges: TE_REF002_007_NADIA_TO_CHARACTER_CONTINUE

## 镜头计划 / Camera Plan

- Movement: flare resolves into a short Nadia close/profile insert with minimal character motion
- Framing: safe close/profile, no sexualized body emphasis, bright sky or stone edge background
- Lens: portrait lens, clean commercial live-action face lock
- Screen Direction: the incoming brightness resolves into her look direction, no abrupt unrelated setup
- Focus: Nadia face and Blue Water identity detail if visible
- Lighting: sunlit sky bounce after flare

## AIGC Video Prompt

Use the ordered images exactly as listed above. Follow the reference-002 timing for this unit and preserve the scripted function over any previous generated still. Do not generate readable title text, logo, subtitles, watermark, random letters, or direct animation screenshot copying. Keep motion, sky direction, scale, and light transitions consistent with the listed transition edges.

## Generation Requirements

- Use reference-002-opening timing as the active evidence for 00:00-00:23; do not reuse the superseded 24s one-take timing.
- Pure image/video generation must be title-safe: no readable Japanese title, no NHK logo, no subtitles, no watermark, no random text.
- Maintain the selected C-version Nadia lock whenever Nadia appears: 14-year-old, honey-tan skin, short navy-black bob, gold earrings/bangles, red-orange/white adventure outfit, Blue Water pendant, non-sexualized.
- Treat the previous generated stills as replaceable material evidence, not as the source of timing truth.

## Negative / Failure Conditions

- 如果 Nadia 被成人化、性感化或服装漂移则失败。
- 如果她在 21.5 秒前进入则失败。
