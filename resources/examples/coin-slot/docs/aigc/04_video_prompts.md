# 投币口 / 01_AIGC 基础视频提示词包 v4

使用方式：本文件是基础提示词包，用于理解 20 镜的整体语义。实际图生视频优先使用 `14_structured_video_prompts.md`，并按 `13_generation_units.md` 的生成单元拆分执行。每条只允许一个主要变化。

## 全局连续性前缀

中文：90年代中国小城，中式梦核，潮湿发黄的童年记忆，真实电影质感，低照度，轻微 VHS 噪点，儿童低视角。三兄弟没有女生：阿磊/哥哥10-11岁稍高，海军蓝旧运动外套、左眉短断点、下巴微扬；小川/主角7岁左右，右耳微外翻、蓝白旧校服外套、小红领巾系得过紧、深色短裤、白色旧球鞋、浅绿色塌书包；小满/小弟弟5-6岁更小，浅色大衬衫、抓衣角、脚尖内扣。混混四人组：彬子/小矮个老大最凶，黄发梢、破黑夹克、腰包；高杆/瘦高个长手臂封路；大海/胖子宽身体堵路；小齐/小跑腿起哄但发虚。

English: 1990s small-town China, Chinese dreamcore, humid yellowed childhood memory, cinematic realism, low light, subtle VHS noise, child-height perspective. Three boys only, no girls: A Lei / older brother age 10-11, slightly taller, old navy track jacket, small break in left eyebrow, chin slightly raised; Xiao Chuan / protagonist age about 7, right ear slightly sticking out, old blue-white school jacket, too-tight red scarf, dark shorts, worn white sneakers and collapsed pale green schoolbag; Xiao Man / younger brother age 5-6, smaller, oversized pale shirt, clutching shirt hem, toes turned inward. Four bullies: Binzi / short fierce boss with yellow hair tips, torn black jacket and waist bag; Gao Gan / tall skinny blocker with long arms; Dahai / wide-bodied blocker; Xiao Qi / errand-runner who jeers nervously.

## Clip 01 / 老旧小区建立

- 白模参考：`whitebox_renders/CAM_COMPOUND_01_ESTABLISH.png`
- 中文提示词：90年代小城非常老旧的居民小区，一楼偏僻角落里藏着游戏机房，发黄水泥墙、旧楼道、晾衣绳、破自行车、潮湿地面、墙角杂草，游戏机房门口透出微弱 CRT 彩光。镜头微微推进，环境安静偏僻。
- English prompt: a very old 1990s small-town Chinese residential compound, a hidden arcade room tucked in a remote ground-floor corner, yellowed concrete walls, old stairwell, clothesline, broken bicycle, damp ground, weeds in corners, faint CRT glow leaking from the arcade doorway. Slight push-in, quiet secluded atmosphere.

## Clip 02 / 三兄弟靠近

- 白模参考：`whitebox_renders/CAM_COMPOUND_02_BROTHERS_APPROACH.png`
- 中文提示词：哥哥走在前面，主角背浅绿色书包跟在半步后，小弟弟更小更胆怯地贴在后面，三人走向老旧小区一楼偏僻角落的游戏机房门口。没有女生。儿童低机位 tracking。
- English prompt: the older brother walks in front, the protagonist with a pale green schoolbag follows half a step behind, the smaller timid younger brother trails close behind, the three boys approach the hidden ground-floor arcade room in the old compound. No girls. Child-height tracking shot.

## Clip 03 / 游戏厅入口

- 白模参考：`whitebox_renders/CAM_ARCADE_01_ENTRANCE_WIDE.png`
- 中文提示词：三兄弟站在低矮游戏厅入口，旧街机排列在两侧和深处，CRT 红蓝绿光和烟雾吸引他们。哥哥带头进入，主角和小弟弟跟上。空间结构保持稳定。
- English prompt: the three brothers stand at the low arcade entrance, old arcade cabinets arranged on both sides and in the back, CRT red blue green glow and smoke draw them in. The older brother leads, the protagonist and younger brother follow. Stable room geometry.

## Clip 04 / 找到街霸

- 白模参考：`whitebox_renders/CAM_ARCADE_02_STREET_FIGHTER_CABINET.png`
- 中文提示词：三兄弟围到一台街头霸王街机前，哥哥兴奋地站到操作位，主角在旁边看，小弟弟躲在身后。磨损摇杆、彩色按钮、CRT 屏幕闪烁。
- English prompt: the three brothers gather around a Street Fighter arcade cabinet, the older brother excitedly takes the controls, the protagonist watches beside him, the younger brother hides behind. Worn joystick, colored buttons, CRT screen flicker.

## Clip 05 / 哥哥打赢老大

- 白模参考：`whitebox_renders/CAM_ARCADE_03_DUEL_OVER_SHOULDER.png`
- 中文提示词：哥哥和小矮个混混老大分别站在街霸机器两侧对战，哥哥快速操作并赢下，小矮个老大僵住，脸被胜利画面红光照亮，尴尬又凶狠。
- English prompt: the older brother and the short fierce bully boss stand on both sides of the Street Fighter cabinet, the older brother plays fast and wins, the short boss freezes, his face lit by the red victory glow, embarrassed and furious.

## Clip 06 / 老大记仇

- 白模参考：`whitebox_renders/CAM_ARCADE_04_BOSS_LOSES_REACTION.png`
- 中文提示词：街机胜利画面还亮着，小矮个老大脸色难看，瘦高个、胖子、小跑腿聚到他身后。四人暂时不动手，只用眼神盯着哥哥。
- English prompt: the arcade victory screen still glows, the short boss looks humiliated, the lanky tall bully, fat bully, and errand-runner gather behind him. They do not attack yet, only stare at the older brother.

## Clip 07 / 志得意满离开

- 白模参考：`whitebox_renders/CAM_ARCADE_EXIT_01_LEAVING.png`
- 中文提示词：三兄弟从游戏机房门口出来，哥哥因为刚赢了街霸有点志得意满，边走边比划，主角和小弟弟跟在旁边。街机待机声从门内远去。
- English prompt: the three brothers leave the arcade room, the older brother is proud after winning Street Fighter and gestures excitedly while walking, the protagonist and younger brother follow beside him. Arcade attract-mode sound fades behind them.

## Clip 08 / 偏僻小路

- 白模参考：`whitebox_renders/CAM_ALLEY_01_WALK_HOME.png`
- 中文提示词：三兄弟走在老旧小区背后的偏僻小路，围墙、杂草、碎砖石、潮湿地面、旧路灯。哥哥还在兴奋比划，主角看着他，小弟弟贴在旁边。前方渐渐出现阴影。
- English prompt: the three brothers walk through a secluded alley behind the old compound, concrete walls, weeds, broken stones, damp ground, old streetlight. The older brother still gestures proudly, the protagonist watches him, the younger brother stays close. A shadow slowly appears ahead.

## Clip 09 / 四人堵路

- 白模参考：`whitebox_renders/CAM_ALLEY_02_BLOCKED.png`
- 中文提示词：小矮个老大带着瘦高个、胖子、小跑腿堵住小路前方，三兄弟停下，哥哥挡在两个弟弟前面。气氛从得意转为危险。
- English prompt: the short fierce boss blocks the alley with the lanky tall bully, fat bully, and errand-runner. The three brothers stop, the older brother steps in front of the two younger boys. The mood turns from pride to danger.

## Clip 10 / 围殴哥哥

- 白模参考：`whitebox_renders/CAM_ALLEY_03_BROTHER_BEATEN.png`
- 中文提示词：四个混混围住哥哥，推搡并殴打他，哥哥失去平衡，主角站在侧面不知所措，小弟弟僵住不敢动。低机位手持，压迫感。
- English prompt: the four bullies surround the older brother, shove and beat him, he loses balance, the protagonist stands to the side frozen and confused, the younger brother is too scared to move. Low handheld angle, oppressive.

## Clip 11 / 石块失手

- 白模参考：`whitebox_renders/CAM_ALLEY_04_STONE_HIT.png`
- 中文提示词：小矮个老大准备对哥哥下狠手，主角看到路边石块，惊恐中捡起石块砸向老大头部，动作短促慌乱，所有人瞬间停住，声音抽空。
- English prompt: the short boss prepares a heavy blow against the older brother, the protagonist sees a stone on the roadside, panics, picks it up and strikes the boss near the head, the action is brief and chaotic, everyone freezes, sound drops out.

## Clip 12 / 主角逃跑

- 白模参考：`whitebox_renders/CAM_ALLEY_05_ESCAPE_VECTOR.png`
- 中文提示词：主角从偏僻小路冲出，浅绿色书包剧烈晃动，哥哥和小弟弟留在后方混乱中，追兵反应过来开始追他。旧路灯拖成长条。
- English prompt: the protagonist bolts from the secluded alley, pale green schoolbag swinging hard, the older brother and younger brother remain in the chaos behind, the pursuers react and start chasing him. Old streetlight stretches into long trails.

## Clip 13 / 进入废楼

- 白模参考：`whitebox_renders/CAM_CORRIDOR_01_ENTRY_LONG.png`
- 中文提示词：主角单独冲进废弃单位楼长走廊，发霉水泥墙、重复门洞、冷绿色荧光灯，他沿走廊深处奔跑，身影变小。
- English prompt: the protagonist rushes alone into a long abandoned work-unit corridor, moldy concrete walls, repeated door frames, cold green fluorescent lights, he runs deeper down the corridor and becomes smaller.

## Clip 14 / 无限走廊

- 白模参考：`whitebox_renders/CAM_CORRIDOR_02_LOW_TRACK.png`
- 中文提示词：低位 tracking 镜头贴着走廊前进，主角贴墙跑并回头看，重复门洞让走廊像被拉长，追兵声音逐渐消失。
- English prompt: low tracking shot through the corridor, the protagonist runs close to the wall and looks back, repeated doorways make the corridor feel stretched, pursuer sounds fade away.

## Clip 15 / 远处电话亭

- 白模参考：`whitebox_renders/CAM_PHONE_01_DISTANT_GLOW.png`
- 中文提示词：走廊尽头出现旧电话亭，稳定暖白微光对抗冷绿环境，主角在远处停下，听到电话铃声，慢慢抬头。
- English prompt: an old phone booth appears at the far end of the corridor, steady warm white glow against cold green surroundings, the protagonist stops far away, hears the ringing phone, slowly raises his head.

## Clip 16 / 靠近电话亭

- 白模参考：`whitebox_renders/CAM_PHONE_02_APPROACH_CLOSE.png`
- 中文提示词：主角从黑暗中靠近电话亭，暖白光照亮红领巾和浅绿色书包边缘，他站到电话亭前，伸手犹豫。
- English prompt: the protagonist approaches the phone booth from darkness, warm white light catching his red scarf and pale green schoolbag edge, he stands before the booth and hesitates with one hand raised.

## Clip 17 / 接起电话

- 白模参考：`whitebox_renders/CAM_PHONE_03_RECEIVER_INSERT.png`
- 中文提示词：旧电话听筒特写，主角颤抖的手拿起听筒，电话线轻轻晃动，暖白光照着旧塑料材质。
- English prompt: close insert of the old phone receiver, the protagonist's trembling hand lifts it, the phone cord sways gently, warm white light on aged plastic.

## Clip 18 / 电子化

- 白模参考：`whitebox_renders/CAM_PHONE_02_APPROACH_CLOSE.png`
- 中文提示词：主角听筒贴近耳边，CRT 扫描线从电话线蔓延到手臂，身体轮廓像素化，走廊边缘分裂成低分辨率色块，电话亭位置不变。
- English prompt: the protagonist holds the receiver to his ear, CRT scanlines spread from the phone cord to his arm, his silhouette pixelates, corridor edges split into low-resolution color blocks, phone booth position unchanged.

## Clip 19 / 进入8-bit关卡

- 白模参考：`whitebox_renders/CAM_8BIT_01_STAGE_WIDE.png`
- 中文提示词：废楼走廊展平成90年代横版清版街机世界，主角变成保留蓝白校服、小红领巾、浅绿色书包的像素角色，混混四人组从右侧变成像素敌人入场。
- English prompt: the abandoned corridor flattens into a 1990s side-scrolling beat-em-up arcade world, the protagonist becomes a pixel character retaining blue-white jacket, red scarf and pale green schoolbag, the four bullies enter from the right as pixel enemies.

## Clip 20 / WIN 与 INSERT COIN

- 白模参考：`whitebox_renders/CAM_8BIT_02_WIN_SCREEN.png`
- 中文提示词：像素主角用书包旋风、硬币冲击波击退四个像素敌人，巨大像素字 `WIN` 出现，停顿一秒后角落闪出 `INSERT COIN`，结尾不安。
- English prompt: the pixel protagonist defeats the four pixel enemies using a schoolbag spin and coin shockwave, huge pixel text `WIN` appears, after a one-second pause `INSERT COIN` flickers in the corner, ending with unease.
