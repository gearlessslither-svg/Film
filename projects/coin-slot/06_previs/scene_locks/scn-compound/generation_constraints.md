# Generation Constraints - SCN_COMPOUND

## Prompt Anchor / 正向锚点

- Use the scene master reference and the matching whitebox for each shot.
- Preserve 1990s small-town China, damp lived-in surfaces, restrained VHS grain, low-key realism.
- Keep practical lighting motivated by CRT screens, old bulbs, street spill, and wet reflections.
- Maintain locked scene geography, screen direction, child scale, and foreground/midground/background relation.

## Continuity Anchors / 连续性锚点

- S0_START_CLEAN: 老旧居民楼一楼偏僻角落、发黄水泥墙、晾衣绳、破自行车、潮湿地面、门内微弱 CRT 蓝绿光
- S0_START_CLEAN: 阿磊海军蓝外套红白斜条，小川蓝白外套红领巾浅绿书包，小满浅色大衬衫，三人从院内走向角落
- The three brothers are ordinary children, curious and only slightly tense; no fight damage yet.
- S0_START_CLEAN: 老旧居民楼一楼偏僻角落、发黄水泥墙、晾衣绳、破自行车、潮湿地面、门内微弱 CRT 蓝绿光
- S0_START_CLEAN: 阿磊海军蓝外套红白斜条，小川蓝白外套红领巾浅绿书包，小满浅色大衬衫，三人从院内走向角落

## Negative Rules / 禁止漂移

- No modern phones, clean malls, LED signage, fashionable contemporary wardrobe, glossy cyberpunk neon, or ad-style lighting.
- No text, captions, labels, arrows, diagrams, watermarks, or storyboard borders in generation outputs.
- Do not let the location mutate between shots; only camera angle, character blocking, smoke density, and minor light flicker may vary.
- Do not mix later-stage injury, alley dirt, phone booth glow, or 8-bit world states into this scene unless the shot list explicitly says so.
