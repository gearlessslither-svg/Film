# 投币口 / 01_AIGC 关键帧提示词包 v3

用途：先生成静态关键帧，验证风格、角色锚点、空间连续性，再进入图生视频。每张关键帧都应搭配对应 Blender 白模参考图。

## 全局风格锁定

中文全局前缀：90年代中国小城，中式梦核，潮湿发黄的童年记忆，真实电影质感，低照度，轻微 VHS 噪点，儿童低视角，旧胶片颗粒。现实段保持真实材质，电子化段使用 CRT 扫描线和低分辨率色块，8-bit 段保持90年代横版街机像素规则。

English global prefix: 1990s small-town China, Chinese dreamcore, humid yellowed childhood memory, cinematic realism, low light, subtle VHS noise, child-height perspective, old film grain. Realistic materials in live-action sections, CRT scanlines and low-resolution color blocks during electronic transformation, strict 1990s side-scrolling arcade pixel rules in the 8-bit section.

## Character Sheet A / 三兄弟（旧版，仅作故事关系参考）

- 用途：仅保留旧故事关系。新版人物生成必须优先使用 `16_character_design_bible_v2.md` 和 `17_character_sheet_generation_prompts_v2.md`。
- 中文提示词：三兄弟关系角色图，灰墙背景，阿磊站在左前方略高，海军蓝旧运动外套，左眉短断点，下巴微扬，装作镇定；小川站在中间半步后，右耳微外翻，蓝白旧校服、过紧红领巾、浅绿色塌书包，双手攥书包带，紧张观察；小满站在右后方更小，圆额头，浅色大衬衫，抓衣角，脚尖内扣，茫然害怕。三人不是同款脸，不是同款发型，不是同款运动服，全是男孩，没有女生。
- English prompt: relationship character sheet of three brothers, grey wall background. A Lei stands slightly forward on the left, taller, old navy track jacket, small break in his left eyebrow, chin slightly raised, pretending calm; Xiao Chuan stands half a step behind in the middle, right ear slightly sticking out, old blue-white school jacket, too-tight red scarf, collapsed pale green schoolbag, gripping straps, nervously observing; Xiao Man stands smaller at the rear right, round forehead, oversized pale shirt, clutching shirt hem, toes turned inward, blank and afraid. Not the same face, not the same haircut, not matching tracksuits, all boys, no girls.
- 禁止变化：不要现代校服、女生、动漫风、过度可爱、统一脸、统一发型、童模脸。

## Character Sheet B / 混混四人组（旧版，仅作故事关系参考）

- 用途：仅保留旧故事关系。新版人物生成必须优先使用 `16_character_design_bible_v2.md` 和 `17_character_sheet_generation_prompts_v2.md`。
- 中文提示词：混混四人组关系角色图，灰墙背景，彬子小矮个老大站在中心前方，短脖子，黄发梢，破黑夹克，斜挂腰包，下巴前顶，受辱后的凶；高杆瘦高个站在一侧，窄长脸，灰白旧夹克，长手臂横住像封路；大海胖子站另一侧，褪色几何 T 恤，汗湿领口，双脚宽站，抹脖子汗，不滑稽；小齐小跑腿站边缘，灰外套只扣一颗，条纹内衫，抠袖口，兴奋和害怕混在一起。四人轮廓差异明显，年龄是小城坏孩子，不是成年人黑帮。
- English prompt: relationship character sheet of four delinquent boys, grey wall background. Binzi, the short boss, stands forward in the center, short neck, yellow-dyed hair tips, torn black jacket, waist bag slung across front, chin pushed forward, fierce from humiliation; Gao Gan, tall skinny boy, stands on one side, long narrow face, old grey-white jacket, long arm held like blocking the road; Dahai, heavyset boy, stands on the other side, faded geometric T-shirt, sweaty collar, feet planted wide, wiping neck sweat, not comic; Xiao Qi, young errand-runner, stands at the edge, grey jacket with one button, striped undershirt, picking sleeve cuff, excitement mixed with fear. Clearly different silhouettes, small-town bad kids, not adult gangsters.
- 禁止变化：不要黑社会西装、现代潮牌、统一制服、无差别路人、统一脸、成年人。

## Keyframe 01 / 老旧小区偏僻角落

- 对应镜头：Clip 01
- 白模参考：`whitebox_renders/CAM_COMPOUND_01_ESTABLISH.png`
- 中文提示词：90年代中国小城非常老旧的居民小区，一楼偏僻角落藏着一个游戏机房，发黄水泥墙、旧楼道、铁栏杆、晾衣绳、破自行车、潮湿地面、墙角杂草，游戏机房门口透出微弱 CRT 彩光，中式梦核，安静偏僻，真实电影质感。
- English prompt: a very old 1990s small-town Chinese residential compound, a hidden arcade room tucked in a remote ground-floor corner, yellowed concrete walls, old stairwell, iron railing, clothesline, broken bicycle, damp ground, weeds in corners, faint CRT glow leaking from the arcade doorway, Chinese dreamcore, quiet secluded mood, cinematic realism.
- 禁止变化：不要现代商业街、正规门店、明亮商场。

## Keyframe 02 / 三兄弟走向游戏机房

- 对应镜头：Clip 02
- 白模参考：`whitebox_renders/CAM_COMPOUND_02_BROTHERS_APPROACH.png`
- 中文提示词：老旧小区一楼偏僻角落，哥哥走在前面，主角背浅绿色旧书包跟在半步后，小弟弟更小更胆怯地贴在后面，三人走向游戏机房门口。儿童低视角，发黄水泥墙，潮湿地面，CRT 微光从门缝里漏出，没有女生。
- English prompt: remote ground-floor corner of an old residential compound, the older brother walks in front, the protagonist with pale green old schoolbag follows half a step behind, the smaller timid younger brother stays close behind, the three boys walk toward the arcade room doorway. Child-height perspective, yellowed concrete walls, damp ground, faint CRT glow leaking from the door, no girls.
- 禁止变化：不要学生队伍、女生、现代小区。

## Keyframe 03 / 游戏厅入口

- 对应镜头：Clip 03
- 白模参考：`whitebox_renders/CAM_ARCADE_01_ENTRANCE_WIDE.png`
- 中文提示词：90年代中国小城旧游戏厅入口，低矮天花板，左右两侧和深处排列旧街机，CRT 屏幕发出红蓝绿色荧光，空气中有烟雾和灰尘，三兄弟站在门口，哥哥带头进入，主角和小弟弟跟上。中式梦核，真实电影感。
- English prompt: 1990s small-town Chinese old arcade entrance, low ceiling, old arcade cabinets along both sides and the back, CRT screens glowing red blue and green, smoky dusty air, three brothers stand at the doorway, older brother leads in, protagonist and younger brother follow. Chinese dreamcore, cinematic realism.
- 禁止变化：不要现代电玩城、液晶屏、女生。

## Keyframe 04 / 街霸对战胜利

- 对应镜头：Clip 05-06
- 白模参考：`whitebox_renders/CAM_ARCADE_03_DUEL_OVER_SHOULDER.png`
- 中文提示词：旧游戏厅里一台街头霸王街机前，哥哥刚刚打赢小矮个混混老大，CRT 屏幕亮起胜利画面，哥哥志得意满，小矮个老大矮但凶狠，破黑夹克黄发腰包，脸被红色屏幕光照亮，旁边瘦高个、胖子、小跑腿聚过来但暂时不动手。低天花板、烟雾、压迫感。
- English prompt: inside the old arcade in front of a Street Fighter cabinet, the older brother has just beaten the short bully boss, the CRT screen glows with a victory moment, the older brother is proud, the short boss is short but fierce with torn black jacket, yellow hair and waist bag, his face lit by red screen glow, the lanky tall bully, fat bully and errand-runner gather nearby but do not attack yet. Low ceiling, smoke, oppressive mood.
- 禁止变化：不要现场开打，不要现代游戏。

## Keyframe 05 / 偏僻小路堵截

- 对应镜头：Clip 08-09
- 白模参考：`whitebox_renders/CAM_ALLEY_02_BLOCKED.png`
- 中文提示词：90年代中国小城老旧小区背后的偏僻小路，发黄水泥围墙、墙角杂草、碎砖石、潮湿地面、旧路灯昏黄。三兄弟回家被四个混混堵住，小矮个老大站在最前面，瘦高个、胖子、小跑腿分散堵住去路，哥哥挡在主角和小弟弟前面。危险、安静、压迫。
- English prompt: secluded alley behind an old 1990s small-town Chinese residential compound, yellowed concrete walls, weeds, broken stones, damp ground, dull yellow old streetlight. The three brothers are blocked by four bullies on their way home, the short fierce boss stands in front, the lanky tall bully, fat bully and errand-runner spread out to block the path, the older brother stands between them and the younger boys. Dangerous, quiet, oppressive.
- 禁止变化：不要大街、车辆、现代商业区。

## Keyframe 06 / 哥哥被围殴

- 对应镜头：Clip 10
- 白模参考：`whitebox_renders/CAM_ALLEY_03_BROTHER_BEATEN.png`
- 中文提示词：偏僻小路里四个混混围住哥哥推搡殴打，哥哥失去平衡，主角站在侧面惊慌无措，小弟弟僵住不敢动。旧路灯昏黄，水泥墙压迫，地上有碎石和潮湿反光。低机位手持电影感。
- English prompt: in the secluded alley, four bullies surround the older brother, shoving and beating him, he loses balance, the protagonist stands to the side shocked and helpless, the younger brother freezes and cannot move. Dull yellow old streetlight, oppressive concrete walls, broken stones and damp reflections on the ground. Low handheld cinematic angle.
- 禁止变化：不要复杂武打，不要血腥。

## Keyframe 07 / 石块失手

- 对应镜头：Clip 11
- 白模参考：`whitebox_renders/CAM_ALLEY_04_STONE_HIT.png`
- 中文提示词：小矮个老大准备对哥哥下狠手，主角看到路边石块，惊恐中弯身捡起石块，下一瞬间砸中老大头部附近，所有人僵住。动作慌乱短促，不是英雄式攻击；旧路灯黄光、地面碎石、潮湿水泥墙，声音仿佛抽空。
- English prompt: the short fierce boss prepares a heavy blow against the older brother, the protagonist sees a roadside stone, bends down in panic to pick it up, then strikes near the boss's head, everyone freezes. Brief chaotic accidental action, not heroic; dull yellow old streetlight, broken stones on the ground, damp concrete walls, sound feels muted.
- 禁止变化：不要血腥特写，不要爽片化。

## Keyframe 08 / 废楼无限走廊

- 对应镜头：Clip 13-14
- 白模参考：`whitebox_renders/CAM_CORRIDOR_01_ENTRY_LONG.png`
- 中文提示词：主角单独冲进废弃单位楼内部，狭窄低矮长走廊，发霉水泥墙，脱落油漆，重复门洞，旧消防箱，地面积水反光，冷绿色荧光灯延伸到黑暗深处。主角蓝白校服、小红领巾、浅绿色书包仍可识别。
- English prompt: the protagonist rushes alone into an abandoned work-unit building, narrow low long corridor, moldy concrete walls, peeling paint, repeated door frames, old fire box, puddles reflecting light, cold green fluorescent tubes stretching into darkness. His blue-white school jacket, red scarf and pale green schoolbag remain identifiable.
- 禁止变化：不要鬼影、医院、学校走廊。

## Keyframe 09 / 远处电话亭

- 对应镜头：Clip 15-16
- 白模参考：`whitebox_renders/CAM_PHONE_01_DISTANT_GLOW.png`
- 中文提示词：废楼走廊深处出现旧电话亭，电话亭不合理地发出稳定暖白微光，周围仍是冷绿色荧光灯和发霉墙面。主角站在远处黑暗中，抬头看向电话亭，红领巾和浅绿色书包边缘被微光照亮。
- English prompt: an old phone booth appears deep inside the abandoned corridor, impossibly emitting steady warm white light while the surroundings remain cold green fluorescent moldy walls. The protagonist stands in distant darkness and looks toward the booth, edges of his red scarf and pale green schoolbag lit by the glow.
- 禁止变化：不要现代电话亭、全息屏、科幻实验室。

## Keyframe 10 / 电子化

- 对应镜头：Clip 17-18
- 白模参考：`whitebox_renders/CAM_PHONE_02_APPROACH_CLOSE.png`
- 中文提示词：主角站在旧电话亭前，听筒贴近耳边，电话线微微晃动，暖白光照亮他的脸、红领巾和浅绿色书包。CRT 扫描线从电话线蔓延到手臂，身体轮廓开始像素化，废楼墙面和走廊边缘分裂成低分辨率色块。
- English prompt: the protagonist stands before the old phone booth with receiver to his ear, phone cord gently swaying, warm white light illuminating his face, red scarf and pale green schoolbag. CRT scanlines spread from the phone cord to his arm, his silhouette begins to pixelate, corridor walls and edges split into low-resolution color blocks.
- 禁止变化：不要绿色代码雨、机器人化、未来城市。

## Keyframe 11 / 8-bit 横版关卡

- 对应镜头：Clip 19
- 白模参考：`whitebox_renders/CAM_8BIT_01_STAGE_WIDE.png`
- 中文提示词：废楼走廊被重写成90年代横版清版街机世界，8-bit 像素风格，背景仍能看出像素墙砖、像素消防箱、像素电话亭。主角变成小学生像素角色，保留蓝白校服、小红领巾、浅绿色书包，混混四人组变成像素敌人，老大像 mini-boss。
- English prompt: the abandoned corridor rewritten as a 1990s side-scrolling beat-em-up arcade world, 8-bit pixel art style, background still showing pixel wall tiles, pixel fire box and pixel phone booth. The protagonist becomes a schoolboy pixel character retaining blue-white jacket, red scarf and pale green schoolbag, the four bullies become pixel enemies, the short boss like a mini-boss.
- 禁止变化：不要现代手游 UI、3D 卡通、可爱 Q 版过度。

## Keyframe 12 / WIN 后 INSERT COIN

- 对应镜头：Clip 20
- 白模参考：`whitebox_renders/CAM_8BIT_02_WIN_SCREEN.png`
- 中文提示词：8-bit 像素舞台静止，敌人消失，废楼横版关卡背景仍在，巨大像素字 `WIN` 出现在画面中央，主角像素小人站在左侧或中央偏左，画面角落闪出小字 `INSERT COIN`，胜利后的安静和不安，像旧街机待机画面。
- English prompt: the 8-bit pixel stage becomes still, enemies vanish, abandoned-corridor side-scrolling background remains, huge pixel text `WIN` appears in the center, the pixel schoolboy stands left or center-left, small text `INSERT COIN` flickers in the corner, quiet unease after victory, like an old arcade attract-mode screen.
- 禁止变化：不要庆祝人群、明亮可爱结尾、现代游戏胜利界面。
