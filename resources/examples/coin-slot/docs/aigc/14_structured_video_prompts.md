# 投币口 / 01_AIGC 结构化视频提示词 v1

用途：实际图生视频优先使用本文件。本文件按 `13_generation_units.md` 的生成单元编写，比 `04_video_prompts.md` 更适合控制运动。

## 全局 Keep consistent

90年代中国小城，中式梦核，潮湿发黄的童年记忆，真实电影质感，低照度，轻微 VHS 噪点，儿童低视角。三兄弟全是男孩：阿磊/哥哥10-11岁稍高，海军蓝旧运动外套、左眉短断点、下巴微扬；小川/主角7岁左右，右耳微外翻、蓝白旧校服外套、小红领巾系得过紧、深色短裤、白色旧球鞋、浅绿色塌书包，紧张时攥书包带；小满/小弟弟5-6岁更小，浅色大衬衫、抓衣角、脚尖内扣。混混四人组：彬子/小矮个老大短小前压、黄发梢、破黑夹克、腰包；高杆/瘦高个长手臂封路；大海/胖子宽身体堵路；小齐/小跑腿起哄但发虚。不要现代手机、液晶屏、现代车辆、女生、额外角色、血腥、英雄化暴力，不要统一脸型、统一发型、统一身材。

## U01

- Camera: 16:9，远景建立，locked-off with very slow push-in，儿童低视角。
- Subject: 老旧小区一楼偏僻角落，没有明显人物动作。
- Motion: 只允许 CRT 微光轻闪和空气轻微浮动。
- Scene: 前景破自行车和潮湿地面，中景隐藏游戏机房门口，背景发黄居民楼和晾衣绳。
- Composition: 门口位于画面中右，建筑占据主体，前景物压低视线。
- Lighting: 暗黄环境光，门口漏出微弱 CRT 蓝绿光。
- Style: 写实电影感，中式梦核，轻微 VHS 颗粒。
- Keep consistent: 居民楼底层储物间式游戏机房、潮湿地面、发黄水泥墙。
- Avoid: 现代商铺、明亮商场、现代招牌、额外人群、镜头大幅移动。

## U02

- Camera: 16:9，全景到中远景，儿童低机位 tracking，跟随三兄弟向门口移动。
- Subject: 哥哥在前，主角背浅绿色书包在中间，小弟弟贴在后面。
- Motion: 三人从画面左后方向右前方小幅前进，最后停在门口。
- Scene: 前景潮湿地面和杂草，中景三兄弟，背景游戏机房门缝 CRT 微光。
- Composition: 哥哥在最前方，主角居中偏左，小弟弟在最后，门口作为终点。
- Lighting: 暗黄小区光，门缝彩光照到脚边。
- Style: 写实童年记忆，低照度。
- Keep consistent: 三兄弟身高差、主角红领巾和绿书包、没有女生。
- Avoid: 变成学生队伍、人物身高错乱、现代小区、镜头绕圈。

## U03

- Camera: 16:9，室内广角，slow dolly in，从入口向街机排布推进。
- Subject: 三兄弟站在入口，哥哥带头迈入，主角和小弟弟跟上。
- Motion: 三人向前小幅进入，烟雾和 CRT 光轻动。
- Scene: 前景脏塑料门帘，中景三兄弟，背景两侧旧街机和低天花。
- Composition: 三兄弟位于画面下方中轴，两侧街机形成压迫通道。
- Lighting: CRT 红蓝绿光，顶部旧荧光灯昏暗。
- Style: 90年代旧游戏机房，真实材质。
- Keep consistent: 低天花板、旧街机、烟雾、三兄弟关系。
- Avoid: 现代电玩城、液晶屏、抓娃娃机、额外女生。

## U04

- Camera: 16:9，中景固定，轻微 handheld 呼吸感。
- Subject: 三兄弟围到街头霸王街机前，哥哥站到操作位。
- Motion: 哥哥向操作位靠近并停下，主角和小弟弟只小幅跟随。
- Scene: 前景磨损摇杆和彩色按钮，中景街霸机和三兄弟，背景旧街机排。
- Composition: 街霸机占画面中心，哥哥在机器前，主角和小弟弟靠左后方。
- Lighting: CRT 屏幕光照脸，烟雾吃光。
- Style: 写实旧街机厅。
- Keep consistent: Street Fighter cabinet、哥哥主导、主角绿书包。
- Avoid: 换成现代游戏、多人混乱、现实打斗提前发生。

## U05

- Camera: 16:9，中近景 over-shoulder，镜头固定在街机屏幕和两人肩背之间。
- Subject: 哥哥和小矮个老大在街霸机两侧对战。
- Motion: 只允许手部操作、屏幕闪烁、老大表情从嚣张变僵住。
- Scene: 前景肩背和按钮，中景 CRT 胜利画面，背景暗处围观轮廓。
- Composition: 屏幕在画面中心，哥哥肩背在左前景，老大在右侧受红光照亮。
- Lighting: 胜利画面红光照到老大脸上。
- Style: 压迫的写实街机厅。
- Keep consistent: 哥哥左侧，小矮个老大右侧，冲突只发生在游戏里。
- Avoid: 现实拳打脚踢、主角参与对战、镜头旋转。

## U06

- Camera: 16:9，低机位中景，slow push-in。
- Subject: 小矮个老大脸色难看，瘦高个、胖子、小跑腿聚到他身后。
- Motion: 三个同伙从背景小幅靠近，老大只用眼神盯住哥哥。
- Scene: 前景街机机身边缘，中景老大，背景三同伙和 CRT 光。
- Composition: 老大在中右前景，三名同伙分散在后方，形成三角压迫。
- Lighting: 红色 CRT 光和暗黄顶灯。
- Style: 写实压迫感。
- Keep consistent: 四人轮廓差异，老大矮但凶。
- Avoid: 立刻动手、四人变成无差别人群、黑社会西装。

## U07

- Camera: 16:9，门口中远景，低机位跟拍。
- Subject: 三兄弟从游戏机房门口出来，哥哥志得意满地比划。
- Motion: 三人从中景向画面右侧走，动作轻松但不要奔跑。
- Scene: 前景脏台阶，中景三兄弟，背景旧卷帘门和门内 CRT 光。
- Composition: 三兄弟从门口中心向右离开，门内 CRT 光留在背景。
- Lighting: 昏黄路灯，门内红蓝光逐渐远去。
- Style: 写实夜色，中式梦核。
- Keep consistent: 没有混混出现，没有冲突，三兄弟全是男孩。
- Avoid: 追逐提前开始、突然暴力、现代商业街。

## U08

- Camera: 16:9，小路全景，稳定低机位 tracking。
- Subject: 三兄弟走在老小区背后的偏僻小路，哥哥还在兴奋比划。
- Motion: 三人沿小路向前走，前方阴影慢慢出现。
- Scene: 前景碎砖石和湿地，中景三兄弟，背景窄巷和旧路灯。
- Composition: 三兄弟在画面左/中，阴影在远处右侧或中轴尽头。
- Lighting: 昏黄旧路灯，远处居民窗微光。
- Style: 潮湿、安静、危险将至。
- Keep consistent: 小路偏僻、围墙、杂草、潮湿地面。
- Avoid: 大街、车流、现代商业区、人群。

## U09

- Camera: 16:9，对峙全景，locked-off，不翻轴。
- Subject: 小矮个老大带三人堵在前方，哥哥挡在两个弟弟前面。
- Motion: 双方只小幅停住和对视，老大可向前半步。
- Scene: 前景湿地反光，中景三兄弟和混混，背景窄巷深处。
- Composition: 三兄弟保持左侧/近侧，四人组保持右侧/远侧，哥哥站在两个弟弟前。
- Lighting: 旧路灯黄光压住画面。
- Style: 写实压迫构图。
- Keep consistent: 三兄弟在左/近侧，四人组在右/远侧，哥哥保护两个弟弟。
- Avoid: 立刻打斗、出现女生、空间左右关系反转。

## U10A

- Camera: 16:9，低机位中景，handheld 小幅晃动。
- Subject: 四个混混靠近哥哥，把哥哥围在中心。
- Motion: 混混向中心挤压，哥哥后退半步，主角和小弟弟停在边缘。
- Scene: 前景肩膀或人影遮挡，中景哥哥，背景水泥墙。
- Composition: 哥哥在画面中心，主角在左侧边缘，小弟弟靠后，混混形成半圆。
- Lighting: 路灯黄，阴影压脸。
- Style: 写实但克制。
- Keep consistent: 主角不动手，小弟弟僵住，四人轮廓不同。
- Avoid: 连续武打、血腥、镜头大旋转。

## U10B

- Camera: 16:9，低机位中景，handheld 轻晃后短暂停住。
- Subject: 哥哥被推搡后失去平衡，主角在侧面惊住。
- Motion: 哥哥向画面中心下方失衡，其他人只围住不做复杂动作。
- Scene: 前景模糊人影，中景哥哥和主角，背景窄墙。
- Composition: 哥哥占中心低位，主角侧面可见，混混只作为压迫边框。
- Lighting: 昏黄路灯，地面反光。
- Style: 压迫、慌乱、非爽片。
- Keep consistent: 暴力短促，不展示血腥结果。
- Avoid: 复杂格斗、拳脚连招、英雄式反击。

## U11A

- Camera: 16:9，中近景，主角侧面，镜头固定。
- Subject: 主角看见路边石块，眼神从哥哥转到地面。
- Motion: 只有眼神和头部小幅下移，石块进入前景注意点。
- Scene: 前景路边石块，中景主角侧脸，背景混乱人影虚化。
- Composition: 石块在画面下方前景，主角侧脸在中景，背景人物虚化。
- Lighting: 路灯黄偏暗。
- Style: 声音抽空前的现实紧张。
- Keep consistent: 石块是路边普通碎石，不是武器。
- Avoid: 刀、棍、凳子、夸张特写、血腥。

## U11B

- Camera: 16:9，道具中近景，短促 handheld。
- Subject: 主角弯身捡起路边石块。
- Motion: 身体向下，手从画面中部到前景石块，动作慌乱。
- Scene: 前景石块和潮湿地面，中景主角手和书包，背景窄巷。
- Composition: 手和石块占画面下半部，绿书包作为身份锚点留在中景。
- Lighting: 路灯黄，地面湿反光。
- Style: 真实、慌乱、非英雄。
- Keep consistent: 主角红领巾、绿书包、白鞋可识别。
- Avoid: 摆拍、武器化、动作流畅得像武打。

## U11C

- Camera: 16:9，中景，短促动作后 locked-off。
- Subject: 失手动作结束后，所有人瞬间停住。
- Motion: 不展示冲击特写；只表现短促慌乱后的冻结和众人反应。
- Scene: 前景人影遮挡，中景主角和老大位置，背景哥哥和墙面。
- Composition: 主角在画面侧面，老大在中景，前景遮挡弱化冲击瞬间。
- Lighting: 路灯黄短暂压成红黄感。
- Style: 惊吓、声音抽空、克制。
- Keep consistent: 主角惊恐，不是英雄；老大受伤不做血腥细节。
- Avoid: 血喷、头部特写、爽片慢动作、庆祝。

## U12A

- Camera: 16:9，低位 handheld tracking，沿小路方向。
- Subject: 主角从僵住状态突然起跑，浅绿色书包剧烈晃动。
- Motion: 主角向小路深处冲出，方向单一。
- Scene: 前景墙面擦过，中景主角，背景混乱人群拉远。
- Composition: 主角占画面左前或中前，后方人群被拉远，逃跑方向指向画面深处。
- Lighting: 路灯拖影，暗处吞没边缘。
- Style: 恐惧、求生、童年噩梦。
- Keep consistent: 红领巾、绿书包、白鞋。
- Avoid: 改变逃跑方向、大街追车、多人混作一团。

## U12B

- Camera: 16:9，手持跟拍后方反应，保持同一逃跑轴线。
- Subject: 后方混混反应过来开始追，主角距离拉开。
- Motion: 追兵从背景向前，但不要追到主角身边。
- Scene: 前景暗墙，主角在远处，追兵在后方。
- Composition: 主角远处偏中，追兵保持后景，墙面形成单向通道。
- Lighting: 旧路灯形成长条拖影。
- Style: 紧张但空间清楚。
- Keep consistent: 追逐从偏僻小路指向废楼方向。
- Avoid: 方向反复、车辆、现代街道、镜头旋转。

## U13

- Camera: 16:9，低机位长走廊，slow tracking-in。
- Subject: 主角单独冲入废弃单位楼走廊。
- Motion: 主角从近处向走廊深处奔跑，身影变小。
- Scene: 前景门框，中景主角，背景重复门洞和消防箱。
- Composition: 走廊中轴透视，主角沿中线向深处缩小。
- Lighting: 冷绿色荧光灯，走廊深处黑。
- Style: 中式梦核，静冷压迫。
- Keep consistent: 废弃单位楼，不是学校、医院或酒店。
- Avoid: 鬼影、怪物、空间突然变形。

## U14

- Camera: 16:9，低位 tracking，贴走廊墙面前进。
- Subject: 主角贴墙跑并小幅回头。
- Motion: 主体向前，头部轻微回看，灯管闪烁节奏变慢。
- Scene: 前景发霉墙面，中景主角，背景重复门洞。
- Composition: 主角靠画面一侧贴墙，走廊纵深占据中心。
- Lighting: 冷绿灯管断续闪。
- Style: 迷路、被空间吞没。
- Keep consistent: 走廊轴线固定，电话亭尚未出现。
- Avoid: 180 度翻转、大幅空间扭曲、换场景。

## U15

- Camera: 16:9，深景 locked-off。
- Subject: 主角远处停下，看到走廊尽头的旧电话亭。
- Motion: 电话亭微光增强，主角慢慢抬头。
- Scene: 前景黑暗走廊，中景主角小身影，背景暖白电话亭。
- Composition: 电话亭在走廊深处中右，主角在远处左/中形成尺度差。
- Lighting: 暖白电话亭光对冷绿环境。
- Style: 临界点、被召唤。
- Keep consistent: 电话亭固定在走廊深处。
- Avoid: 现代电话亭、全息屏、其他出口。

## U16

- Camera: 16:9，中景，slow dolly in。
- Subject: 主角从黑暗靠近电话亭，站到电话亭前伸手犹豫。
- Motion: 左侧黑暗到电话亭前，动作缓慢小幅。
- Scene: 前景电话亭边缘，中景主角，背景冷绿走廊。
- Composition: 电话亭占画面右侧或中心，主角从左侧靠近并停在门前。
- Lighting: 暖白光照红领巾和书包边缘。
- Style: 安静、神秘、现实错误物。
- Keep consistent: 主角服装、电话亭位置、光源方向。
- Avoid: 主角变脸、换衣服、科幻设备化。

## U17

- Camera: 16:9，close-up / insert，固定镜头。
- Subject: 主角颤抖的手拿起旧听筒。
- Motion: 手从下方靠近，听筒被轻轻拿起，电话线晃动。
- Scene: 前景手，中央听筒，背景冷绿边缘虚化。
- Composition: 听筒位于画面中心，手从下方进入，背景保持虚化。
- Lighting: 暖白光照旧塑料。
- Style: 真实道具特写。
- Keep consistent: 旧电话材质、手部比例、电话线。
- Avoid: 智能手机、现代电缆、手指畸形、镜头漂移。

## U18A

- Camera: 16:9，中近景 locked-off，微 push-in。
- Subject: 主角听筒贴耳，电话线开始出现 CRT 扫描线。
- Motion: 扫描线从听筒和电话线向手臂蔓延。
- Scene: 前景电话线，中景主角，背景电话亭和冷绿走廊。
- Composition: 电话线作为前景斜线连接听筒和主角手臂，主角不离开电话亭。
- Lighting: 暖白电话亭光 + CRT 色块微闪。
- Style: 电子化起点，非未来科技。
- Keep consistent: 主角不移动位置，电话亭固定。
- Avoid: Matrix 绿色代码雨、机器人化、未来城市。

## U18B

- Camera: 16:9，中景 locked-off，轻微 push-in。
- Subject: 主角身体轮廓和走廊边缘开始像素化。
- Motion: 低分辨率色块从主角手臂扩散到身体和墙面。
- Scene: 前景电话亭边框，中景主角，背景走廊纵深。
- Composition: 主角固定在电话亭前中景，走廊边缘保持可识别纵深。
- Lighting: 暖白和冷绿被 CRT 扫描线切割。
- Style: CRT 扫描线、像素块、色彩错位。
- Keep consistent: 角色服装色块、电话亭、走廊轴线。
- Avoid: 场景重构、突然跳到8-bit、额外人物。

## U19

- Camera: 16:9，orthographic side-scrolling，固定横版机位。
- Subject: 像素主角在左侧，四个像素敌人从右侧入场。
- Motion: 敌人右到左进入，主角小幅待机动作。
- Scene: 前景像素地砖，中景角色，背景像素废楼走廊和电话亭。
- Composition: 主角固定在左侧，敌人从右侧入场，电话亭保留在背景中右。
- Lighting: 平面化街机光，有限色盘。
- Style: 90年代横版清版街机，8-bit 像素。
- Keep consistent: 主角蓝白校服、红领巾、绿书包色块，敌人轮廓差异。
- Avoid: 3D 卡通、现代手游 UI、西方街头背景。

## U20A

- Camera: 16:9，orthographic side-scrolling，固定横版机位。
- Subject: 像素主角用书包旋风和硬币冲击波清场。
- Motion: 主角左到右小幅推进，技能不超过 2-3 个，敌人被击退。
- Scene: 前景 UI 边缘，中景像素角色，背景像素走廊。
- Composition: 横版舞台固定，主角左/中，敌人右侧，UI 不遮挡角色。
- Lighting: 平面街机光。
- Style: 90年代清版街机爽感，但底色不安。
- Keep consistent: 技能来自小学生物件，敌人保留四人轮廓。
- Avoid: 复杂连招、写实血腥、高清 anime 战斗。

## U20B

- Camera: 16:9，orthographic fixed，UI 居中。
- Subject: 敌人消失，主角像素小人停住，巨大 `WIN` 出现。
- Motion: 画面几乎静止，只允许 UI 弹出。
- Scene: 背景仍是像素废楼走廊。
- Composition: `WIN` 位于画面中心，主角停在左侧或中左。
- Lighting: 平面街机光。
- Style: 老街机胜利画面。
- Keep consistent: `WIN` 居中，主角不庆祝。
- Avoid: 庆祝人群、彩带、现代胜利界面。

## U20C

- Camera: 16:9，orthographic fixed，静止。
- Subject: `WIN` 停顿后，角落闪出 `INSERT COIN`。
- Motion: 只允许 `INSERT COIN` 闪烁和轻微 CRT 抖动。
- Scene: 像素废楼走廊仍在，电话亭轮廓保留。
- Composition: `WIN` 仍在中央，`INSERT COIN` 位于画面角落，背景保持静止。
- Lighting: 旧街机待机光。
- Style: 胜利后的不安尾针。
- Keep consistent: 文本为 `INSERT COIN`，不要改字。
- Avoid: 欢乐结尾、现代 UI、切回现实解释。
