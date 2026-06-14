# 投币口 / 01_AIGC 人物设定图生成提示词 v2

用途：替换旧版“泛角色合影”思路。新版先生成单人可识别角色，再生成关系图、表情图、动作图，最后合成群像。不要先让模型一次性发明七个人。

参考文件：`16_character_design_bible_v2.md`

## 生成顺序

1. 单人正面角色设定：每人 1 张。
2. 单人三视图/turnaround：每人 1 张。
3. 单人表情九宫格：每人 1 张。
4. 单人动作姿态四连：每人 1 张。
5. 三兄弟关系图：1 张。
6. 混混四人组关系图：1 张。
7. 现实群像对峙图：1 张。
8. 8-bit 像素转换图：1 张。

最低应生成：7 个角色 x 4 张 + 4 张关系/转换 = 32 张人物设计图。通过后再进关键帧和视频。

## 全局正向提示词

中文：90年代中国小城，中式梦核现实质感，潮湿发黄的童年记忆，真实儿童和少年，不漂亮化，不广告化，低照度电影感，旧但洗过的衣服、磨损鞋、生活痕迹，开场阶段没有泥灰和打架后脏乱，灰墙背景，角色设计图，清晰正面，完整身体，细节可读，表情具体，姿态有性格。

English: 1990s small-town China, Chinese dreamcore realism, humid yellowed childhood memory, real children and young teens, not beautified, not commercial, cinematic low light, old but washed clothes, worn shoes, lived-in details, opening-stage children without mud, post-fight grime, or later dishevelment, grey wall background, character design sheet, clear front view, full body, readable details, specific expression, personality in posture.

## 全局负面提示词

中文：不要统一脸，不要同款发型，不要同款身材，不要让兄弟互相像，不要童模脸，不要现代校服，不要干净新衣服，不要开场就满身泥灰，不要打架后脏乱提前出现，不要网红审美，不要成年演员脸，不要欧美脸，不要日本动漫脸，不要职业黑帮，不要夸张武器，不要女生，不要血腥，不要所有人都摆同一种酷姿势。

English: no same face, no same haircut, no same body type, do not make siblings look interchangeable, no child model face, no modern school uniform, no brand-new clean clothes, no heavy mud or grime at opening stage, no post-fight dishevelment before the fight, no influencer beauty, no adult actor face, no western face, no anime face, no professional gangster, no exaggerated weapon, no girls, no gore, no identical cool poses.

## 单人正面设定图

### CHR_BRO_A_FRONT / 阿磊正面

中文提示词：阿磊，10-11岁中国小城男孩，三兄弟里的哥哥，戴旧细框近视眼镜，装作很成熟但仍是孩子。方一点的脸，左眉有短断点，短硬头发，后脑略睡扁，下巴微扬，镜片后的眼神从上往下看。眼镜是旧细金属框或黑细框，干净但不时髦，不是潮牌大框。海军蓝旧运动外套，胸前红白斜条，袖口磨毛，拉链头缺漆，裤腿偏长，鞋尖磨白。开场阶段，旧但洗过，不能有泥灰和打架后脏乱。完整身体正面角色设定图，灰墙背景，一只手插外套口袋，另一只手轻推眼镜，脚尖外八，表情是假装镇定。

English prompt: A Lei, 10-11-year-old small-town Chinese boy, the older brother of three boys, wearing old thin-frame prescription glasses, pretending to be mature but still clearly a child. Slightly square face, a small break in his left eyebrow, short stiff hair, slightly flattened back of head, chin lifted, looking slightly downward through the lenses. The glasses are old thin metal or thin black frames, clean but not fashionable, not trendy large frames. Old navy-blue track jacket with red-white diagonal stripe across the chest, frayed cuffs, chipped zipper pull, pants a little too long, scuffed white shoe tips. Opening-stage clothing: old but washed, no mud, no post-fight grime, no later dishevelment. Full-body front character design sheet, grey wall background, one hand in jacket pocket, the other lightly pushing his glasses, toes slightly turned out, expression pretending to be calm.

### CHR_BRO_B_FRONT / 小川正面

中文提示词：小川，7岁中国小城一年级男孩，本片主角，瘦小，不是勇敢英雄，而是容易被吓住的孩子。小脸，圆眼睛，右耳微外翻，低鼻梁，嘴唇半张，家里剪坏的短刘海，额前一撮翘发。蓝白旧校服外套偏大，小红领巾系得过紧，深色短裤，膝盖旧擦痕，白球鞋发灰，浅绿色塌书包，右肩带更松，前袋拉链缺小拉片。完整身体正面角色设定图，双手攥书包带，肩膀缩，表情紧张但忍住。

English prompt: Xiao Chuan, 7-year-old first-grade small-town Chinese boy, the protagonist, small and skinny, not a brave hero but a child easily frightened. Small face, round eyes, right ear slightly sticking out, low nose bridge, lips half open, badly home-cut short bangs, one stubborn tuft on the forehead. Oversized old blue-white school jacket, red scarf tied too tightly, dark shorts, old knee scratches, greyed white sneakers, collapsed pale green schoolbag, right strap looser, missing small zipper pull on front pocket. Full-body front character design sheet, both hands gripping schoolbag straps, shoulders shrunk, tense expression trying to hold back fear.

### CHR_BRO_C_FRONT / 小满正面

中文提示词：小满，5-6岁中国小城男孩，三兄弟里最小，反应慢，胆小，跟着哥哥走，不是小川缩小版。开场阶段，旧但洗过，不能邋遢，不能有泥灰和打架后脏乱。整体更胖一点、更圆一点、更幼，圆额头明显，脸短而圆，脸颊鼓一点，短脖子，像一颗小圆团；眼睛略下垂，带一点胆小可爱的湿润感，眼神慢半拍；小而钝的鼻子，小嘴闭着或轻轻瘪住，不要小川那种半张嘴紧张表情。头发更短，是圆寸或很短的碗盖头，贴头皮，额前短短一排，不要小川同款短刺发和额前翘发，耳朵不突出。换一身和小川完全不同的衣服：干净暖色旧小马甲或薄棉背心，里面浅色长袖，衣领和扣子整齐，裤子偏宽但干净，鞋带系好，鞋旧但不脏。完整身体正面角色设定图，脚尖内扣，膝盖靠近，两手轻轻抓着自己小马甲下摆，表情胆小、可爱、慢半拍、害怕但不哭不卖萌。

English prompt: Xiao Man, 5-6-year-old small-town Chinese boy, the youngest of three brothers, slow to react, timid, follows his older brothers, not a smaller version of Xiao Chuan. Opening-stage costume: old but washed, not sloppy, no mud, no post-fight grime, no later dishevelment. Overall he is chubbier, rounder, and younger: very clear round forehead, short round face, slightly chubby cheeks, short neck, like a small round bundle; slightly drooping eyes with a timid gentle cuteness, delayed gaze; small blunt nose, small mouth closed or faintly downturned, not Xiao Chuan's half-open anxious mouth. Hair is shorter: close-cropped round cut or very short bowl cut, lying close to the head, short tiny fringe across the forehead, no Xiao Chuan-style spiky short hair or forehead tuft, ears not prominent. Give him a completely different outfit from Xiao Chuan: clean warm-colored old small vest or thin padded vest, pale long-sleeve shirt underneath, tidy collar and buttons, clean loose pants, shoelaces tied, shoes old but not dirty. Full-body front character design sheet, toes turned inward, knees close together, both hands gently clutching his small vest hem, expression timid, cute, delayed, afraid but not crying or performing cuteness.

### CHR_BLY_A_FRONT / 彬子正面

中文提示词：彬子，12-13岁中国小城坏孩子，小矮个老大，输掉街霸后最怕丢脸。个子矮，脖子短，肩膀紧，窄脸，下颌用力，嘴角一边歪，左脸靠嘴角有小痣或旧疤点。黑发根和染黄发梢，几缕头发粘在汗上。破黑夹克偏大，暗色 T 恤，旧腰包斜挂在前面，廉价金属链，旧拖鞋或开口凉鞋。完整身体正面角色设定图，下巴往前顶，手拽腰包，表情是受辱后的凶。

English prompt: Binzi, 12-13-year-old small-town Chinese delinquent boy, the short fierce boss, terrified of losing face after losing Street Fighter. Short body, short neck, tight shoulders, narrow face, clenched jaw, one-sided crooked mouth, small mole or old scar near the left corner of his mouth. Black roots with dyed yellow hair tips, a few sweaty strands stuck to his forehead. Oversized torn black jacket, dark T-shirt, old waist bag slung across the front, cheap metal chain, worn slippers or open sandals. Full-body front character design sheet, chin pushed forward, hand yanking the waist bag, expression fierce from humiliation.

### CHR_BLY_B_FRONT / 高杆正面

中文提示词：高杆，13-14岁中国小城瘦高个混混，沉默，负责封路。窄长脸，重眼皮，长鼻梁，薄嘴唇，身体高瘦，塌肩，手臂显得过长。灰白旧夹克袖子略短，露出手腕骨节，松垮裤子，脏鞋，鞋带散开。完整身体正面角色设定图，一只手臂横在身体前像挡路，眼睛半垂，没有表情。

English prompt: Gao Gan, 13-14-year-old tall skinny small-town Chinese delinquent, quiet, used to block the road. Long narrow face, heavy eyelids, long nose bridge, thin lips, very tall and skinny body, sloped shoulders, arms looking too long. Old grey-white jacket with slightly short sleeves exposing bony wrists, loose pants, dirty shoes, one shoelace undone. Full-body front character design sheet, one arm held across his body like blocking a passage, half-lidded eyes, almost expressionless.

### CHR_BLY_C_FRONT / 大海正面

中文提示词：大海，13岁中国小城胖混混，负责用身体堵住空间。圆脸，小眼睛，亮鼻头，短脖子，宽身体。褪色几何图案 T 恤，领口汗湿，外搭旧短袖衬衫，宽松裤子，小腿沾灰，厚手掌。完整身体正面角色设定图，双脚站得很宽，一只手抹脖子汗，表情看着彬子等命令，不滑稽。

English prompt: Dahai, 13-year-old heavyset small-town Chinese delinquent, uses his body to block space. Round face, small eyes, shiny nose, short neck, wide body. Faded geometric-pattern T-shirt with sweaty collar, old short-sleeve overshirt, loose pants, dusty calves, thick palms. Full-body front character design sheet, feet planted wide, one hand wiping neck sweat, expression looking toward Binzi for orders, not comic.

### CHR_BLY_D_FRONT / 小齐正面

中文提示词：小齐，11-12岁中国小城小跑腿，最年轻，靠起哄讨好老大。尖下巴，窄额头，眼睛亮但飘，嘴角快笑快收。灰外套只扣一颗扣子，里面条纹旧内衫，裤脚一高一低，鞋跟踩扁，手指抠袖口。完整身体正面角色设定图，身体前探又想缩回去，表情是兴奋和害怕混在一起。

English prompt: Xiao Qi, 11-12-year-old small-town Chinese errand-runner delinquent, youngest, tries to please the boss by jeering. Pointed chin, narrow forehead, bright but drifting eyes, mouth quickly smiling then stopping. Grey jacket buttoned with only one button, old striped undershirt, uneven trouser cuffs, crushed shoe heels, fingers picking at sleeve cuff. Full-body front character design sheet, body leaning forward but ready to shrink back, expression mixing excitement and fear.

## 三视图 / Turnaround 提示词模板

把上面单人提示词中的外形描述保留，追加：

中文追加：角色三视图 turnaround sheet，正面、侧面、背面并排，保持同一张脸、同一身高比例、同一服装磨损细节，灰墙背景，清晰轮廓，标出服装背面和鞋子细节。

English add-on: character turnaround sheet, front view, side view, back view side by side, same face, same height proportion, same worn clothing details, grey wall background, clear silhouette, readable back-of-clothes and shoe details.

## 表情九宫格提示词模板

### 三兄弟表情项

| 角色 | 九宫格表情 |
|---|---|
| 阿磊 | 假装镇定、推眼镜催促弟弟、赢街霸的得意、被堵时强撑、怕丢脸、被推搡后眼镜歪、看见小川失手后的震惊、想喊却卡住、沉默低头 |
| 小川 | 好奇、紧张、被 CRT 光吸引、看哥哥赢的半笑、小路被堵、看见石块、失手后声音抽空、逃跑恐惧、电话亭前被召唤 |
| 小满 | 胆小跟随、被游戏厅光吓到、很小地跟着笑、发现危险、贴墙僵住、快哭但没哭、看哥哥、看小川、完全不知所措 |

中文模板：`角色名` 表情九宫格，保持同一张脸和同一服装，只画头肩和上半身，九个清晰不同表情：`表情列表`。真实儿童表情，不夸张漫画，不统一皱眉。

English template: expression grid for `character name`, same face and same clothing, head-and-shoulders and upper body only, nine clearly different expressions: `expression list`. Real child expressions, not exaggerated cartoon, no identical frowns.

### 混混表情项

| 角色 | 九宫格表情 |
|---|---|
| 彬子 | 假笑、挑衅、赢前自信、输掉僵住、受辱憋怒、堵路凶狠、准备下狠手、不可置信、失控后的空白 |
| 高杆 | 半垂眼、无聊、看出口、封路、皱眉、用前臂推人、后退半步、看彬子、沉默慌张 |
| 大海 | 呼吸重、跟着笑、看彬子脸色、堵住路、用肩顶人、抹汗、笑意消失、愣住、开始害怕 |
| 小齐 | 快笑、起哄、讨好、身体前探、被瞪后缩、袖口小动作、收声、眼睛乱看、想跑不敢跑 |

## 姿态四连提示词

每个角色生成一张四连动作图，格式为：常态站姿、关系动作、冲突动作、失控/恐惧动作。

| 角色 | 四连动作 |
|---|---|
| 阿磊 | 插兜并推眼镜装成熟；回头催弟弟；挡在弟弟前；被围时肩膀缩住眼镜略歪 |
| 小川 | 攥书包带；看哥哥反应；弯身看见石块；身体歪斜起跑 |
| 小满 | 暖色小马甲抓下摆跟随；贴近哥哥；靠墙僵住；脚尖内扣快哭 |
| 彬子 | 拽腰包挑衅；街霸机前假笑；下巴顶人；受辱后空白 |
| 高杆 | 半垂眼站着；横臂封路；用肩前臂推人；后退半步 |
| 大海 | 宽脚站立；抹脖子汗；用身体堵人；笑意消失 |
| 小齐 | 抠袖口；起哄前探；换重心绕边；眼睛乱看收声 |

中文模板：`角色名` 动作姿态四连，完整身体，四个并排姿态：`动作列表`。保持同一服装、同一脸、同一身高比例，动作真实克制，能看出性格。

English template: four-pose action sheet for `character name`, full body, four side-by-side poses: `pose list`. Same clothing, same face, same height proportion, realistic restrained movement, personality visible in posture.

## 关系图提示词

### REL_BROTHERS / 三兄弟关系图

中文提示词：三兄弟关系角色图，灰墙背景，阿磊站在左前方略高，戴旧细框近视眼镜，海军蓝旧运动外套，下巴微扬，一只手轻推眼镜；小川站在中间半步后，蓝白旧校服、过紧红领巾、浅绿色书包，双手攥书包带；小满站在右后方更小更圆胖，短圆头，干净暖色旧小马甲或薄棉背心，抓马甲下摆，脚尖内扣，胆小可爱但不卖萌。三人不是同款脸，不是同款发型，表情不同：阿磊装镇定，小川紧张观察，小满胆小害怕。真实90年代中国小城儿童。

English prompt: relationship character sheet of three brothers, grey wall background. A Lei stands slightly forward on the left, taller, wearing old thin-frame prescription glasses, old navy track jacket, chin slightly raised, one hand lightly pushing his glasses; Xiao Chuan stands half a step behind in the middle, old blue-white school jacket, too-tight red scarf, pale green schoolbag, gripping straps; Xiao Man stands smaller at the rear right, rounder and chubbier, short round haircut, clean warm-colored old small vest or thin padded vest, clutching vest hem, toes turned inward, timid and cute but not performative. Not the same face, not the same haircut, different expressions: A Lei pretending calm, Xiao Chuan nervously observing, Xiao Man timid and afraid. Real 1990s small-town Chinese children.

### REL_BULLIES / 混混四人关系图

中文提示词：混混四人组关系角色图，灰墙背景，彬子小矮个老大站在中心前方，染黄发梢、破黑夹克、斜挂腰包、下巴前顶；高杆瘦高个站在一侧，灰白旧夹克，长手臂横住像封路；大海胖子站另一侧，褪色几何 T 恤，双脚宽站，抹脖子汗；小齐小跑腿站边缘，灰外套只扣一颗，条纹内衫，抠袖口。四人轮廓差异明显，年龄是小城坏孩子，不是成年人黑帮。

English prompt: relationship character sheet of four delinquent boys, grey wall background. Binzi, the short boss, stands forward in the center, yellow-dyed hair tips, torn black jacket, waist bag slung across front, chin pushed forward; Gao Gan, tall skinny boy, stands on one side, old grey-white jacket, long arm held like blocking the road; Dahai, heavyset boy, stands on the other side, faded geometric T-shirt, feet planted wide, wiping neck sweat; Xiao Qi, young errand-runner, stands at the edge, grey jacket with one button, striped undershirt, picking sleeve cuff. Clearly different silhouettes, small-town bad kids, not adult gangsters.

### REL_ALLEY_STANDOFF / 小路对峙关系图

中文提示词：偏僻小路对峙关系设计图，三兄弟在左侧，混混四人在右侧，哥哥阿磊挡在小川和小满前面，彬子小矮个老大向前压，高杆封住路边，大海堵住中线，小齐在边缘起哄。保持七个人各自外形锚点，湿地、围墙、杂草、碎砖石、旧路灯。不是打斗定格，是冲突前的空间关系图。

English prompt: secluded alley standoff relationship design image, three brothers on the left, four bullies on the right. A Lei blocks in front of Xiao Chuan and Xiao Man, short boss Binzi presses forward, tall Gao Gan seals the side, heavy Dahai blocks the center line, Xiao Qi jeers at the edge. Keep all seven character anchors, wet ground, wall, weeds, broken stones, old streetlight. Not a fight freeze-frame, a spatial relationship design before conflict.

### PIXEL_CHARACTER_CONVERSION / 8-bit 色块转换图

中文提示词：七个角色的 8-bit 像素转换设定图，横版清版街机风格，90年代低分辨率有限色盘。小川保留蓝白外套、红领巾、浅绿色书包、白鞋；阿磊保留海军蓝外套、红白斜条和眼镜像素点；小满保留暖色小马甲、短圆头、圆胖身体和内扣站姿；彬子保留黑夹克、黄发梢、腰包和短小前压；高杆保留高瘦长条身形和横臂封路；大海保留宽体块和褪色 T 恤；小齐保留条纹内衫和抖动待机姿态。背景透明或像素灰底。

English prompt: 8-bit pixel conversion character sheet for seven characters, side-scrolling beat-em-up arcade style, 1990s low-resolution limited palette. Xiao Chuan keeps blue-white jacket, red scarf, pale green schoolbag, white shoes; A Lei keeps navy jacket, red-white stripe, and tiny glasses pixels; Xiao Man keeps warm-colored small vest, short round head, round chubby body, and inward toes; Binzi keeps black jacket, yellow hair tips, waist bag, short forward pressure; Gao Gan keeps tall skinny long body and blocking arm; Dahai keeps wide body block and faded T-shirt; Xiao Qi keeps striped undershirt and jittery idle stance. Transparent background or pixel grey background.

## 通过标准

- 盖住文字说明后，七个角色仍能被区分。
- 只看剪影，阿磊、小川、小满不会混。
- 只看脸，彬子、高杆、大海、小齐不会混。
- 小川的恐惧不是“哭”，而是身体收紧和反应迟滞。
- 彬子的凶不是成熟反派气质，而是受辱后的孩子式狠劲。
- 所有衣服都像旧衣服，不像新买的复古服装。
- 表情九宫格里的九个表情不能只是同一个皱眉强弱变化。
