# 《所有人都来了》SH01–SH13 生产级提示词包 V2

- 活动分支：`DFT_MASTERPLAN_WILD_RETURN_V4`
- 覆盖区间：`00:00–00:42`，13 个剪辑镜头，合计 42.0 秒；全部为单源关键帧镜头。
- 画幅与交付：`21:9`，优先原生高分辨率 PNG，成片基准 `1915×821` 或同等准确比例。
- 画面权威：`04_lookdev/references/DFT_DIRECTOR_REFERENCE.png` 只锁视觉语言；阿白身份只由三张真实猫照片与 `05_asset_bible/approved/ABAI_DUAL_STATE_SHEET_V2_APPROVED.png` 锁定；配角身份与服装以 `05_asset_bible/SUPPORTING_CAST_IDENTITY_LOCK_V2.md` 为活动权威。
- 受限旧参考：`SUPPORTING_CAST_A_V1_attempt_001.png`、`SUPPORTING_CAST_B_V1_attempt_001.png` 仅可提取脸型、物种、毛色、体型、两足比例、工装版式和演出服装；严禁继承乐器陈列、熊的托盘／酒杯、排排站构图、缺失野生第三状态。所有其他被否决 V1 设定、旧黑毛撮／单条肋纹阿白与旧写实绘本风格不进入活动参考链。
- 音频：生成视频只做环境声与拟音；Oasis《The Masterplan》仅供后期剪辑配乐，不得嵌入生成视频。
- 全包共同现实规则：`intentional_scale_exceptions: []`；普通重力、承重、抓握、脚地接触、投影、透视与物种解剖始终成立。DFT 平面化空间不是缩小建筑或破坏身体结构的许可。

---

## SH01｜灰晨小镇地理建立｜00:00–00:04｜4.0s

### IMAGE PROMPT

```text
[NARRATIVE_TIME] FACTORY_LAST_SHIFT；故事第一刻，灰晨，最后一个工作日尚未正式开始；远在第一次换装与最终野生回归之前。

[CHARACTER_STATE_LOCK] 本镜无可读近景角色。若道路上出现极小工人点，只能是 FACTORY_BIPED_UNIFORM 的两足拟人动物剪影，统一深蓝工装；不得辨认或复制阿白，不得出现四足野生状态、华服或乐器。

[STATE_TRANSITION_RULE] 本镜不发生任何服装或身体状态转换；所有远景生命状态保持两足工装。

[INTENTIONAL_REALITY_EXCEPTIONS] []。旧纸童话的空间压平仅限美术表达；建筑、道路、烟囱、荒野和任何远景角色仍遵守一致尺度与透视。

[STYLE_FINGERPRINT] 21:9 DFT 旧纸蛋彩／哑光水粉童话画面；温暖旧纸底上有低频、可控的纸纤维与干刷痕，朴拙细描边和大块平面形状，边缘微微磨损但轮廓清楚。深青灰、褪色砖红、风沙土黄、旧芥末黄与少量氧化绿，整体比风格参考亮约一档；低饱和、哑光、安静荒诞。纵深被适度压平但地理关系、遮挡、道路汇聚和空气层次清楚；细节集中于厂区烟囱、重复窗格和道路，天空与荒野保持干净低噪。

[REFERENCE_ROLES] `04_lookdev/references/DFT_DIRECTOR_REFERENCE.png`＝唯一媒介、色彩、边缘、空间压平与气质参考，不继承其人物、月亮、鸟、舟、道具或事件；`04_lookdev/STYLE_BIBLE_V1.md`＝活动画风与禁项；`05_asset_bible/SCALE_LEDGER_V1.md`＝建筑、烟囱、道路尺度；`FIN-001` 若被加载，只作开场地理与高空构图候选，不作为风格或角色身份权威。任何被否决旧场景图不得参与。

[SUBJECT_AND_ACTION] 从荒野一侧望向资源枯竭型西北工业小镇：红砖厂区、两层宿舍、主街、岔路、中央广场轮廓与镇外风沙坡地同框；45–60m 高烟囱完整直立、完全无烟；小镇尚在呼吸但没有繁忙感。极少远景工人点沿道路缓慢走向厂区，不能成为画面主体。观众第一眼应读懂“城镇很大、生命很小、最后一天刚开始”。

[CAMERA_AND_COMPOSITION] 21:9 高空斜俯瞰极远景，24–28mm 感，稳定轴线从镇外荒野朝厂区；相机高度足以同时看到街道网络与厂区，但不是垂直地图。厂区置于画面中偏左，通向荒野的道路从右下前景弯入，中景宿舍与广场形成尺度阶梯，烟囱在后三分之一处竖起；地平线位于上三分之一，留出灰蓝天空负空间。前景风沙坡、道路，中景住宅与厂区，背景低山和晨空三层清晰；焦点覆盖地理锚点，不做浅景深。

[LIGHTING] 阴冷灰晨的漫射天空为大面积柔和顶侧主光；厂房个别旧芥末灯为极弱实景暖点，不形成魔法光；填充低对比，烟囱与屋檐有柔软炭灰背光边缘。曝光保护天空与旧纸高光，阴影有层次但不死黑；无浓雾、无末日火光。

[SPACE_AND_CONTINUITY] 厂区烟囱与高窗的方向需可延续至 SH02–SH08；主街从镇外进入厂门，住宅与广场位于厂区之外，荒野在镇缘。烟囱全程完整无烟；城镇只是陈旧和资源耗尽，不是爆炸后的废墟。屏幕运动方向预留为右下至左中，供 SH02 工人进入厂院。

[SCALE_LOCK] 烟囱约 45–60m，明显高于 6–8m 厂房和 6.5–8m 两层住宅；住宅每层门窗比例一致，主街建筑间宽约 10–14m；路灯 5–6m。任何远景动物都必须远小于同平面门窗和建筑，只随深度缩小，绝不能与房屋同大。至少以烟囱＋重复高窗＋两层住宅三组参照证明尺度。

[GROUP_ACTION_LOCK] 无可读群像表演；最多只保留不同道路、不同间距、不同步幅的微小工人点，不形成复制队列，不添加第二个阿白或猫群。

[NEGATIVE] 禁止烟囱冒烟、火灾、爆炸、末日废土、坍塌、阴森雾、夜黑恐怖、魔法光、糖果色；禁止动物大过房屋、玩具城、微缩建筑、错误楼层、扭曲道路透视；禁止近景人物、群猫、重复角色、乐器、华服、四足野生动物；禁止照片写实、塑料3D、游戏渲染、商业日漫、通透水彩、油画厚涂、吉祥物可爱；禁止文字、招牌伪字、logo、水印。大形清晰、细节密度受控、平面区域平滑低噪；no film grain, no random speckle, no muddy micro-texture, no over-sharpened halos, no fake pixel-level detail, no JPEG artifacts, no noisy background.
```

### AIGC IMAGE-TO-VIDEO PROMPT

```text
[STYLE_FINGERPRINT] 继承输入关键帧的 21:9 DFT 旧纸蛋彩／哑光水粉：低频旧纸纤维、朴拙细描边、大块平面形、深青灰与赭金褪色调、低对比灰晨光、适度压平而地理可读的景深、干净低噪天空和荒野。

[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the input image's exact art style and the style fingerprint above in every frame. Treat the approved SH01 image as the immutable first frame and visual bible. Animate this same artwork; do not reinterpret, redraw, beautify, simplify, or replace its art direction. Preserve medium, edge language, paper texture scale, palette, contrast, lighting logic, architecture geometry, smoke-free chimney, flattened depth treatment and composition density. Only the specified camera drift, tiny distant movement and natural atmosphere may evolve.

[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No model-default redraw; no photoreal aerial footage, drone-video realism, plastic CGI, 3D miniature, game render, anime, cel shading, glossy digital painting, watercolor wash, oil impasto, extra grain or sharpened AI texture.

[NARRATIVE_TIME] FACTORY_LAST_SHIFT / GRAY_MORNING_TOWN_ESTABLISH；最后工作日灰晨，进入工厂之前。

[CHARACTER_STATE_LOCK] state_id=FACTORY_BIPED_UNIFORM；仅允许不可辨识的两足深蓝工装远景生命点，不得出现阿白近景、华服或四足野生状态。

[STATE_TRANSITION_RULE] 全镜保持 FACTORY_BIPED_UNIFORM；无服装转换、无身体转换、无野生化。

[DURATION] 4.0s

[DURATION_RATIONALE] 一个地理建立镜头只需要一次极慢推近和非常轻微的环境运动；4秒足以让观众读清镇、厂、道路与荒野，也能保留开场呼吸。动作单一且适合一张源图，不延长为无内容停留。

[TIMELINE]
0.0–1.0s: 表演：画面从关键帧精确构图开始；相机在高空斜俯轴线上以24–28mm感进行几乎不可察觉的直线前推，不摇摆、不滚转。远景工人点仅有极微小右下至左中的步移；烟囱无烟且绝对静止。全景深、曝光与灰晨漫射光锁定，前景纸面风沙纹理保持静态，只允许一两缕干草轻颤；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
1.0–2.5s: 表演：前推持续但速度不增加，前景坡地与中景屋顶产生轻微视差，建筑几何和道路汇聚保持不变；远景工人保持不同间距和速度，绝不突然放大。焦点仍覆盖厂区与道路，灯点不闪烁；天空亮度仅有自然的极缓上升，不产生日出光束；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
2.5–3.5s: 表演：推近逐步减速，烟囱与重复窗格略更可读；荒野中一阵弱风让一小片草顺同一方向伏动后回弹。相机高度、轴线、地平线、色彩与纸张媒介全部锁定，无新建筑、角色或烟雾出现；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
3.5–4.0s: 表演：相机完全缓停并留出半秒可剪辑终帧；远景脚步继续微动，草叶 settling，所有建筑稳定。最终帧仍是完整无烟烟囱、可读道路与小尺度生命点的安静地理全景；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。

[CONTINUITY_LOCKS] FACTORY_LAST_SHIFT；烟囱完整无烟；厂区、住宅、广场、道路与荒野位置不变；所有远景生命若可见均为两足深蓝工装且不可辨识阿白；建筑与角色尺度、镜头轴线、21:9 构图、旧纸蛋彩媒介全程不变。

[NEGATIVE] 无剪切、无跳帧、无突然变焦、无无人机摆动、无建筑形变、无道路滑移、无烟雾生成、无天灾、无闪灯、无新角色、无角色复制、无动物变大、无文字；无闪烁、纹理爬行、边缘沸腾、噪点、残影或运动模糊糊脸。

[AUDIO] 仅环境声：很远的低风、稀疏干草摩擦、几乎听不见的厂区金属余响；不生成对白、歌声、音乐、BGM 或 soundtrack。《The Masterplan》只在后期剪辑加入。
```

---

## SH02｜工厂外院分层进入｜00:04–00:07｜3.0s

### IMAGE PROMPT

```text
[NARRATIVE_TIME] FACTORY_LAST_SHIFT；灰晨工厂开工前，工人从各处进入秩序区，尚未打卡。

[CHARACTER_STATE_LOCK] 狗、绵羊、兔、大象、驴均为 FACTORY_BIPED_UNIFORM：两足拟人工人、物种头部和毛爪／蹄、统一深蓝旧棉工装并按体型放码；老狗棕黑粗毛垂耳宽肩，绵羊灰白卷毛小弯角，兔灰米短毛且一耳略弯，大象灰蓝皮短牙且体格最大，驴灰褐短毛长耳瘦高。阿白不在可读前中景；不得出现猫形背景工人。所有角色空爪或仅持工牌，不持乐器、托盘、酒杯。

[STATE_TRANSITION_RULE] 本镜无状态转换；全体始终两足工装，不提前露出华服或四足结构。

[INTENTIONAL_REALITY_EXCEPTIONS] []。不同物种共用人类工业设施是故事世界常态，但门洞、步态、重量和相对体型必须可用可信。

[STYLE_FINGERPRINT] 21:9 DFT 旧纸蛋彩／哑光水粉；旧纸低频纤维、干而温和的手工描边、平面块面、轻微磨旧边缘，深青工装与灰蓝晨气压住褪砖红厂墙，少量旧芥末门灯。低饱和、哑光、安静克制；横向构图有明确前中后景和轻度空间压平，人物轮廓大而可读，背景纹理稀疏低噪。

[REFERENCE_ROLES] DFT 参考＝媒介、调色、边缘与气质，不继承具体内容；`SUPPORTING_CAST_IDENTITY_LOCK_V2.md`＝配角身份、体型与工装唯一活动锁；旧 A/B 人设图若加载，仅限上述身份服装字段，严禁乐器陈列、托盘、排排站；`SCALE_LEDGER_V1.md`＝厂门、窗格、路灯尺度；`GROUP_ACTION_LEDGER_120S_V2.md#SH02`＝每个角色动作；不得使用被否决旧场景图作为风格或空间权威。

[SUBJECT_AND_ACTION] 高位大全景展示工厂外院的不同到达阶段：前景老狗正跨过院门阴影；中景绵羊已经进入短队列并安静站稳；兔抬一只毛爪／前肢看旧打卡钟；远中景大象从足够高宽的主门走出；后景驴沿侧坡道接近。观众应读到“不同生命被同一制度收拢”，但动作不是复制粘贴。

[CAMERA_AND_COMPOSITION] 21:9 高位大全景，28–35mm 感，相机位于院墙内侧偏右、向左后方厂门斜看，稳定不夸张透视。前景院门框与一段旧铁栏形成遮挡，老狗在左下；羊与兔分处中景中部和右中；大象置于左后高门内，驴更远。院地标线把视线导向打卡区；建筑占画面约三分之二，角色不塞满画幅。中深景清楚，无浅景深虚化吞掉尺度参照。

[LIGHTING] 灰蓝天空柔光从右上侧进入，厂门内部较暗但保留大象轮廓；门灯仅给门框和工装边缘一丝旧芥末暖色。地面潮冷而非镜面反光，角色投影短而柔；曝光优先保证深蓝工装、门洞和窗格层级。

[SPACE_AND_CONTINUITY] 延续 SH01 的无烟烟囱方向与灰晨色温；工人运动方向从画面边缘汇向中景打卡区，为 SH03 足部与 SH04 打卡器连接。厂院宽、主门在左后、打卡区在中右，路径不可互相穿透；厂房陈旧但结构完整。

[SCALE_LOCK] 工厂主门净高≥3.3m、净宽≥2.8m，大象2.55m两足总高可自然通过且头顶有净空；工业高窗窗台约1.1m、窗顶约3.2m，角色绝不与整扇高窗等高；院墙、门灯、标线和人物脚地接触一致。至少显示“大象＋主门＋高窗”和“老狗＋院门＋地标线”两套同平面尺度关系；后景驴只按透视缩小。

[GROUP_ACTION_LOCK] 老狗＝跨门槛中段、身体三分之二侧向；绵羊＝已排队静候、重心双脚；兔＝抬爪看钟、头向上但身体不动；大象＝慢步出高门、一脚将落；驴＝后景接近、手臂自然下垂。前中后景至少五种物种、五种相位；每个活动主角色仅一个实例，无阿白、无猫群。

[NEGATIVE] 禁止全员同向排排站、同腿齐步、同时举工牌、复制姿势、重复大象／狐狸／兔；禁止第二只猫或猫形背景居民；禁止大象堵小门、门洞低于大象、动物与窗户或厂房同高、玩具建筑、错误地面接触；禁止乐器、托盘、酒杯、华服、四足姿态、人手、裸皮、额外肢体；禁止烟囱烟、末日废墟、恐怖、写实、3D、日漫、吉祥物；禁止伪文字、logo、水印。clean silhouette edges, controlled detail density, large readable shapes, smooth light gradients, low-noise image; no random speckle, muddy micro-texture, sharpening halos, fake detail or JPEG artifacts.
```

### AIGC IMAGE-TO-VIDEO PROMPT

```text
[STYLE_FINGERPRINT] 输入帧的21:9旧纸蛋彩／哑光水粉、深青灰与褪砖红、朴拙细描边、低频纸纤维、平面块形、灰晨柔光与可读的压平纵深；角色为克制的两足拟人动物工人。

[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the input image's exact art style and every identity, costume, architecture and scale dimension. Treat SH02 as immutable first frame; animate the same painted cutout-like world without redrawing, beautifying or changing medium. Only the assigned staggered walk/gesture phases and a restrained high-camera drift may move.

[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal fur or skin, no plastic 3D, game render, generic anime, cel-shaded redraw, glossy illustration, watercolor migration, oil paint, extra digital grain, sharper synthetic texture or character redesign.

[NARRATIVE_TIME] FACTORY_LAST_SHIFT / FACTORY_YARD_ARRIVAL；灰晨开工前，工人由不同路径进入院区、尚未打卡。

[CHARACTER_STATE_LOCK] state_id=FACTORY_BIPED_UNIFORM；狗、羊、兔、象、驴始终为两足深蓝工装，各一实例，无猫、无华服、无四足状态。

[STATE_TRANSITION_RULE] 本镜无状态转换；五位角色只推进各自到达动作，服装与身体结构全程锁定。

[DURATION] 3.0s

[DURATION_RATIONALE] 五个角色各自只继续一个短动作，相机只做轻微横向滑动；3秒足够读清分层到达和门洞尺度，继续延长会增加身份漂移与群像克隆风险。

[TIMELINE]
0.0–0.8s: 表演：从关键帧开始；高位28–35mm相机沿院墙向左进行极慢短滑，保持地平线和轴线。老狗前脚越过门槛、后脚仍在外；绵羊静候；兔刚抬爪看钟；大象后脚在高门内；驴后景慢步。焦点覆盖中景队列与门洞，灰晨曝光、门灯与投影锁定；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
0.8–1.8s: 表演：老狗完成一步并减速；兔只转动头眼确认钟面后放低少许手腕；大象以真实重量迈出一步，身体无弹跳；驴缩短与队列距离但仍在后景；绵羊只做呼吸和轻微耳动。相机滑动产生前景栏杆与中景人物的轻微视差，不改变角色相对尺度；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
1.8–2.5s: 表演：老狗进入院内并让出前景；绵羊向前挪半步但不与他人齐步；兔手爪回到胸侧；大象脚掌完整着地，衣料因重量迟缓下沉；驴继续一小步。灯、窗、门和地标线不闪烁不形变；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
2.5–3.0s: 表演：相机与角色动作同时缓停，留下可剪终帧：五个角色分别处于已到、等待、看钟、刚出门、仍接近的不同阶段。所有衣料、耳尾轻微 settling；画面不新增人物；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。

[CONTINUITY_LOCKS] FACTORY_BIPED_UNIFORM；老狗、羊、兔、大象、驴各一个，身份与相对体型固定；无阿白、无猫；高门≥3.3m并适配大象；行进方向汇向打卡区；烟囱无烟；21:9构图和DFT媒介不变。

[NEGATIVE] 无同步齐步、无动作互换、无角色穿透、无新角色或复制、无四足化、无服装变化、无人手、无肢体变形；无门窗呼吸、地面滑移、尺度漂移、突然推拉、意外切镜、闪烁、纹理爬行、伪文字。

[AUDIO] 仅环境声：稀疏工鞋／蹄足落水泥地、远处金属门轻响、布料摩擦、清晨风；无对白、音乐、BGM、歌声。《The Masterplan》后期配入。
```

---

## SH03｜不同足部越过标线｜00:07–00:10｜3.0s

### IMAGE PROMPT

```text
[NARRATIVE_TIME] FACTORY_LAST_SHIFT；工厂排队区，SH02 到达之后、SH04 打卡之前。

[CHARACTER_STATE_LOCK] 画面只读足部与工装裤脚：老狗、绵羊、兔、大象四种两足工人均为 FACTORY_BIPED_UNIFORM，深蓝旧棉裤脚按体型放码；足部保持物种结构，狗的毛足／旧工鞋、羊蹄、兔足、大象厚重脚掌可区分。无阿白身份锚，无猫足；无华服、乐器或四足野生骨架。

[STATE_TRANSITION_RULE] 无状态转换；每双足保持两足行走与承重，不变化为人脚或野生四足。

[INTENTIONAL_REALITY_EXCEPTIONS] []。低机位和长焦压缩不允许改变物种足部尺寸、地面接触或重力。

[STYLE_FINGERPRINT] 21:9 DFT旧纸蛋彩／哑光水粉插镜；深青裤脚、灰蓝水泥与一道褪色旧芥末地标线形成简洁大形，朴拙手绘边缘、低频纸纹、克制炭灰接触影。空间比写实略平但足部遮挡与前后尺度明确；细节集中在四种足部和磨损标线，地面平整干净、低噪。

[REFERENCE_ROLES] DFT参考＝媒介、边缘、色彩；`SUPPORTING_CAST_IDENTITY_LOCK_V2.md`＝物种足部、相对体型与统一工装；旧A/B板若加载仅作体型与工装裤脚参考，不继承排排站或道具；`SCALE_LEDGER_V1.md`＝兔／狗／羊／大象相对尺寸和地面关系；SHOT_COVERAGE SH03＝镜头与动作权威。

[SUBJECT_AND_ACTION] 四种足部在不同前后景、不同步相越过一条磨损地面标线：前景老狗一只脚正落地；中左羊蹄已经跨过；中右兔的一只小足刚抬起；后景大象脚掌仍在线后、即将压下。只表现制度把不同身体导向同一条线，不显示完整人物或群体齐步。

[CAMERA_AND_COMPOSITION] 21:9 超低机位足部特写／近景，70mm感，镜头距地约10–15cm，沿标线斜向取景而非正侧平铺。磨损标线从左下通向右后；前景狗足占左三分之一但不裁断关节，中景羊蹄与兔足错开，后景大象脚掌以真实纵深进入右侧。浅至中等景深：焦点落在羊蹄与标线交点，前景狗足轻微柔化但轮廓清楚，大象不糊成无形块。

[LIGHTING] 灰晨侧顶柔光从厂门方向扫过地面，标线和水泥微微提亮；脚下接触影短而明确，填光保留深蓝裤脚褶皱。无高反射积水、无强戏剧光、无魔法脚光。

[SPACE_AND_CONTINUITY] 延续 SH02 的运动方向，所有足部由画面右后／边缘向左前打卡区前进；地面材质、标线色与厂院一致。下一镜 SH04 可由一次脚掌落地声切到打卡机压下声。

[SCALE_LOCK] 同一深度上兔足最小，大象脚掌最大且重量感最强；前景狗足因靠近可显大，但需以标线宽度、接触影和遮挡解释，不能大过后景大象到失真。所有脚／蹄完整落在同一地面平面，裤脚与足部连接可信；无悬浮、穿地或错误透视。

[GROUP_ACTION_LOCK] 老狗＝落地相位；羊＝已跨线承重相位；兔＝抬足摆动相位；大象＝线后准备落足相位。四种动作阶段、四种轮廓，不出现两双相同鞋复制，不组成齐步。

[NEGATIVE] 禁止四双脚同时跨线、同一条腿重复、复制鞋、混淆身体归属；禁止人类鞋脚、人类裸脚、五趾人足、额外脚、断肢、脚穿地、悬浮、错误接触影；禁止猫足、华服裤脚、乐器；禁止大象脚缩成兔足或兔足放大，禁止地标线弯折成伪透视；禁止照片写实、3D、日漫、过度景深、速度糊；禁止文字、logo、水印、随机颗粒、泥状纹理、锐化光晕、伪细节与JPEG压缩。
```

### AIGC IMAGE-TO-VIDEO PROMPT

```text
[STYLE_FINGERPRINT] 输入帧的21:9旧纸蛋彩足部插镜：旧纸低频纹理、深青与灰蓝平面块、朴拙轮廓、磨损芥末标线、克制接触影和受控浅景深。

[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the exact source artwork, four species-specific feet, trouser construction, ground plane, mark line, palette and matte paper texture. Animate only one staggered step phase per foot and a tiny ground-level track; do not redraw anatomy or exchange limbs.

[STYLE_NEGATIVE] Strictly do not change or replace the art style. No photoreal shoes/fur, CGI feet, anime redraw, glossy game shading, watercolor bleed, oil paint, synthetic grain, high-frequency floor noise or edge sharpening.

[NARRATIVE_TIME] FACTORY_LAST_SHIFT / QUEUE_FOOT_PHASES；SH02到达后、SH04打卡前。

[CHARACTER_STATE_LOCK] state_id=FACTORY_BIPED_UNIFORM；狗足、羊蹄、兔足、象脚均属于两足深蓝工装身体，无猫足、华服或野生四足骨架。

[STATE_TRANSITION_RULE] 无状态转换；每双足只完成既定错峰承重与步态，物种足部和工装裤脚不变形。

[DURATION] 3.0s

[DURATION_RATIONALE] 这是一个节奏插镜，四组足部只需完成错峰越线的一小段；3秒允许重量差异和声音层次可读，同时避免足部在长生成中变形。

[TIMELINE]
0.0–0.7s: 表演：超低70mm感相机沿标线向左前做极短平滑跟移；老狗前脚开始承重，羊蹄已稳在线前，兔足离地，大象脚掌在线后悬停极短预备。焦点在羊蹄与标线，曝光和侧顶柔光锁定；裤脚只随身体轻摆；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
0.7–1.5s: 表演：老狗完成落地并压出短接触影；兔足轻快越线向下；大象脚掌开始慢而重地前移；羊蹄不再迈步，只做重心微换。相机跟移速度恒定，标线不滑动，四足身份不交换；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
1.5–2.3s: 表演：兔足先落地、裤脚轻回弹；大象脚掌随后压到线边，落地振幅极小但重量可读；老狗另一脚仅进入画面边缘，不完成第二步；羊保持。焦点轻缓移向大象脚掌前缘，景深与纸面纹理稳定；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
2.3–3.0s: 表演：相机减速并停在大象脚掌刚完成承重、兔足已越线的终态；灰尘只允许极少低频一圈后落下，所有裤脚settle。终帧仍有四种不同动作相位，便于切到打卡器；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。

[CONTINUITY_LOCKS] FACTORY_BIPED_UNIFORM；狗、羊、兔、大象足部各一组；运动方向与SH02一致；地面标线、相对尺寸、脚地接触、工装裤脚和DFT媒介不变；无阿白、无猫。

[NEGATIVE] 无齐步、无重复脚、无脚数变化、无趾头生长、无物种互换、无漂浮或穿地、无地面波动、无标线滑移、无突然镜头加速、无剪切；无闪烁、边缘沸腾、纹理爬行、噪点或拖影。

[AUDIO] 仅拟音：狗足沉闷一步、羊蹄轻硬一声、兔足柔软轻点、大象脚掌低频落地与工装布摩擦；无音乐、对白、口号或BGM。《The Masterplan》后期加入。
```

---

## SH04｜旧打卡机压下｜00:10–00:13｜3.0s

### IMAGE PROMPT

```text
[NARRATIVE_TIME] FACTORY_LAST_SHIFT；队列抵达打卡点，最后一次制度性打卡正在发生。

[CHARACTER_STATE_LOCK] 主体为老狗 FACTORY_BIPED_UNIFORM 的一只棕黑粗毛简化毛爪与深蓝袖口；背景仅出现绵羊的一只蹄爪等待，身份归属清楚。两足身体虽在画外仍保持两足工装状态；无阿白、无猫、无华服、乐器、托盘或四足结构。

[STATE_TRANSITION_RULE] 无状态转换；毛爪、袖口、工牌和机器在全镜保持同一结构。

[INTENTIONAL_REALITY_EXCEPTIONS] []。拟人毛爪可操作打卡器是世界规则，但抓握、插入方向、机械压力和反作用必须真实可信。

[STYLE_FINGERPRINT] 21:9 DFT旧纸蛋彩／哑光水粉近景；旧铁打卡机为氧化绿与炭灰大形，深蓝袖口、棕黑毛爪和一张无可读文字的褪色工牌构成主体。朴拙细描边、干刷磨损、低频纸张肌理、柔和灰晨光；机器结构清楚但不过度微细，背景队列压成安静平面色块，清晰低噪。

[REFERENCE_ROLES] DFT参考＝媒介、旧物表面、调色与克制气质；`SUPPORTING_CAST_IDENTITY_LOCK_V2.md`＝老狗毛色、工装和物种毛爪；旧A板若加载只限老狗身份／工装，禁止迁移手鼓等乐器；`SCALE_LEDGER_V1.md`＝工牌、毛爪与机器使用尺度；故事与SH04覆盖表＝一次完整打卡动作。禁止以任何被否决旧构图作为活动镜头参考。

[SUBJECT_AND_ACTION] 老狗的棕黑毛爪将一张边缘磨旧、完全没有可读姓名或编号的工牌推入旧机械打卡器槽口；打卡杆正处于压下前一瞬。背景右侧，绵羊的蹄爪握着第二张空白工牌但仍在等待。画面只讲“最后一次打卡”，不展示多余人物。

[CAMERA_AND_COMPOSITION] 21:9近景／特写，70–85mm感，平视略偏机器右侧，轴线沿工牌进入槽口。机器占左侧约55%，毛爪与工牌从右下进入，打卡杆在上中形成视觉压点；背景绵羊蹄爪位于右上柔焦层，不能与主爪融合。焦点精确在工牌前缘、槽口和主毛爪接触处，机器后部与背景柔化；保留负空间避免零件堆满画面。

[LIGHTING] 左上方高窗灰蓝柔光为主光，打卡机边缘有弱旧芥末实景反光；毛爪与工牌有柔和侧轮廓，槽口内部保持可读暗部。曝光不把旧纸、白卡或金属边缘烧白；阴影方向一致。

[SPACE_AND_CONTINUITY] 打卡器位于SH02院内打卡区、SH03标线之后；工牌运动由右向左进入机器，与工人总体进厂方向一致。机器完整、固定在稳固台面上；背景队列只是一层暗示，不新增角色脸或伪文字。

[SCALE_LOCK] 工牌约为老狗毛爪可自然夹持的尺寸，槽口略宽于工牌；打卡杆支点、压头、台面和毛爪不互穿。绵羊背景蹄爪因更远而略小；主爪、袖口、工牌和机器处在可操作的人类工业尺度，无玩具打卡器或巨型卡片。

[GROUP_ACTION_LOCK] 主老狗毛爪＝推进工牌；背景绵羊蹄爪＝静候，未抬杆、未同步插卡。仅两只可见操作肢体且归属明确；不增加第三只手、第二个打卡器或复制工牌。

[NEGATIVE] 禁止可读文字、数字、姓名、伪字、logo、水印；禁止人类手、五根裸指、额外手、融合手、错误抓握、工牌穿过机器、机械零件重复；禁止两只爪同时插卡、同步动作、猫爪、乐器或私服；禁止机器像玩具、卡片巨大、错误投影；禁止照片写实、塑料3D、日漫、商业卡通、恐怖机械；禁止随机颗粒、金属噪点、泥状微纹理、锐化光晕、伪像素细节、JPEG artifacts、noisy background.
```

### AIGC IMAGE-TO-VIDEO PROMPT

```text
[STYLE_FINGERPRINT] 输入帧的21:9旧纸蛋彩机械特写：氧化绿旧铁、深蓝袖口、棕黑毛爪、褪色空白工牌、朴拙线边、低频纸纹与灰蓝窗光；背景为柔焦平面层。

[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the input image's exact painted medium, machine geometry, paw identity, card size, sleeve, palette, light and composition. Animate this one mechanical punch action in the same artwork; do not redesign the hand, machine or card and do not create text.

[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal metal/fur, CGI mechanism, anime or cel-shaded redraw, glossy game art, watercolor bleed, extra scratch/grain, sharpened texture or pseudo-typography.

[NARRATIVE_TIME] FACTORY_LAST_SHIFT / FINAL_CLOCK_IN；最后一次制度性打卡正在发生。

[CHARACTER_STATE_LOCK] state_id=FACTORY_BIPED_UNIFORM；仅老狗毛爪与羊蹄可读，均隶属两足深蓝工装状态，无阿白、华服或四足身体。

[STATE_TRANSITION_RULE] 无服装或身体转换；只允许老狗完成压卡回收、羊继续等待，机器结构不变。

[DURATION] 3.0s

[DURATION_RATIONALE] 一次打卡包含短暂预备、压杆、机械回弹和终止四个连续小相位；3秒能让动作与声音清楚，又不把单一插镜拖长。

[TIMELINE]
0.0–0.6s: 表演：平视70–85mm相机完全锁定；老狗毛爪把空白工牌最后推进约一小段，打卡杆悬停；背景绵羊蹄爪静候。焦点在槽口接触点，灰蓝主光、旧芥末反光和曝光不变，机器底座稳定；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
0.6–1.4s: 表演：老狗另一处画外力量使打卡杆沿唯一铰链向下压，压头垂直落在卡片边缘；主毛爪保持夹持、腕部不扭曲。机器产生极小真实震动，背景蹄爪不跟随。镜头无移动，焦点和尺度锁定；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
1.4–2.2s: 表演：压杆到达最低点发出机械咔哒后回弹到中位；工牌只后移数毫米，毛爪吸收反作用。旧铁反光随杆角度轻变，其他照明和构图保持；不产生火花、烟或新零件；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
2.2–3.0s: 表演：毛爪把已打过但仍无可读字样的工牌退出槽口一小段并停住，杆缓停在起始位；背景绵羊蹄爪仍等待。机器震动settle，终帧保留完整打卡器和清楚接触关系，便于硬切SH05队列；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。

[CONTINUITY_LOCKS] FACTORY_BIPED_UNIFORM；老狗主毛爪与绵羊背景蹄爪各一、归属不变；工牌始终空白无字；打卡器固定、比例不变；运动轴由右向左；无阿白、无猫、无乐器；DFT媒介全程锁定。

[NEGATIVE] 无额外手指或肢体、无手爪融合、无卡片复制、无机器变形、无杆穿透卡片、无文字生成、无意外切镜、无推拉摇移；无闪烁、纹理爬行、金属融化、噪点、残影或速度糊。

[AUDIO] 仅拟音：纸卡摩擦槽口、旧机械杆吱呀、一次干涩咔哒、轻微回弹；背景极弱脚步与衣料声。无对白、音乐、BGM、歌声；《The Masterplan》只后期剪辑。
```

---

## SH05｜工厂正面队列｜00:13–00:16｜3.0s

### IMAGE PROMPT

```text
[NARRATIVE_TIME] FACTORY_LAST_SHIFT；打卡完成后、进入机器大厅之前，制度化队列在厂房正面短暂停留。

[CHARACTER_STATE_LOCK] 八位活动角色全部为 FACTORY_BIPED_UNIFORM：阿白＝ABAI_FACTORY_UNIFORM_PHOTOLOCK，唯一猫，年轻乳白长毛、灰绿眼、粉鼻、帽沿旁仅露非对称天然灰黑头顶斑边缘、深灰蓬松尾，背部鞍状斑大部被工装遮住；年长绵羊、灰蓝大象、瘦高驴、棕黑老狗、赤褐狐狸、灰米兔、深棕熊均按 SUPPORTING_CAST_IDENTITY_LOCK_V2，穿同版深蓝旧棉工装且空爪或持单张无字工牌。熊绝不端托盘；无人持乐器、酒杯或穿华服。

[STATE_TRANSITION_RULE] 无转换；八位角色全镜保持两足工装，禁止提前换华服、露出完整演出装或四足化。

[INTENTIONAL_REALITY_EXCEPTIONS] []。制度性队列允许有意的总体秩序同步，但不豁免各角色手位、脚位、重心、眼线与物种解剖差异。

[STYLE_FINGERPRINT] 21:9 DFT旧纸蛋彩／哑光水粉群像；褪色砖红厂墙、深青工装、灰蓝晨气和少量旧芥末灯，旧纸低频纤维、朴拙细描边、大块清楚剪影、低饱和哑光。稳定正面寓言式构图，平面化但门洞、窗格和队列前后层次可读；人物面部克制、动作迟缓，细节集中在物种轮廓与工装，背景干净低噪。

[REFERENCE_ROLES] DFT参考＝画材、色谱、边缘、平面空间与克制气质；三张阿白照片＝阿白脸、灰绿眼、粉鼻、天然头顶斑与深灰尾身份，不继承照片姿势、环境、光线、写实媒介；批准阿白板＝两足比例和工装翻译；`SUPPORTING_CAST_IDENTITY_LOCK_V2.md`＝七位配角身份与工装活动锁，旧A/B图只限该文件声明的身份服装字段，禁止乐器、托盘、排排站构图泄漏；`SCALE_LEDGER_V1.md`＝厂门、窗格和体型；`GROUP_ACTION_LEDGER_120S_V2.md#SH05`＝动作分工；旧FIN-002仅可作为待修订队列构图证据，不作身份或风格权威。

[SUBJECT_AND_ACTION] 八位不同物种工人在巨大厂门前形成正面但有纵深的短队列：最前两位狗与羊已经静候且脚位不同；第三位兔刚把无字工牌抬到腰胸之间；后方大象只用一只毛爪／前肢调整帽檐；阿白在队列侧后方横移半步让出通道，克制侧视；驴微驼、熊重心稳、狐狸尾巴收拢，三者分处不同深度并保持各自微动作。观众感到秩序，而不是八个复制人偶。

[CAMERA_AND_COMPOSITION] 21:9平视大全景，35mm感，相机位于厂门外正中但略偏右，眼高约1.5m，正面轴线稳定。门洞形成大矩形框，八人分成前中后三层而非一条横排；阿白位于右中三分之一可辨但不居中，最大的大象在左后且完整露出门净空。前景一段地标线，中景角色，背景高门与重复窗格；中等全景深让脸、脚地接触、门顶和窗格都可读。

[LIGHTING] 灰蓝晨光从画面左前柔和照入，门内旧芥末灯作低强度轮廓／实景光；角色面部有微弱正面填充，工装褶皱不黑死，大象与门洞之间有清楚色值分离。投影柔、方向一致；无强轮廓光、无舞台灯、无魔法辉光。

[SPACE_AND_CONTINUITY] 承接SH04打卡后，队列面向厂内机器大厅；工牌已打过但无可读文字，运动方向从画面前方进入后方高门。厂门、窗格、地标线与SH02同一工业尺度；下一镜SH06从高门内反打到机器大厅。烟囱仍无烟，厂房陈旧但未坍塌。

[SCALE_LOCK] 主门净高≥3.3m、净宽≥2.8m，大象2.55m两足高度自然站在门下且头顶留明确净空；高窗窗顶约3.2m，角色不得与整窗等高；阿白1.55m、兔1.30m、狐狸1.65m、狗1.70m、羊1.75m、驴1.90m、熊2.05m、大象2.55m相对比例稳定。同平面至少显示角色＋门洞＋窗格＋地标线，脚地投影一致；后排只因深度缩小。

[GROUP_ACTION_LOCK] 狗＝前排静候、双臂低垂；羊＝前排静候但一蹄稍后；兔＝抬无字工牌；象＝调整帽檐；阿白＝侧移半步并侧视；驴＝微驼站定、长耳后转；熊＝双爪垂落、重心宽；狐狸＝尾巴收拢、看向门内。只允许队列总体方向同步，不允许相同手位和同腿迈步；八个活动角色各一，无背景主角复制，唯一猫为阿白。

[NEGATIVE] 禁止全员同时举工牌、同腿齐步、双手胸前同姿、完全横排、复制剪影；禁止第二只猫、猫群、重复大象／狐狸等主角色；禁止阿白旧竖黑毛撮、琥珀眼、左肋单纹、白尾；禁止熊托盘、乐器、酒杯、华服、四足姿态、人类手、额外肢体；禁止门洞小于大象、动物高过高窗、玩具工厂、尺度漂移、脚悬浮；禁止烟、灾难、恐怖、照片写实、3D、日漫、吉祥物；禁止文字、伪字、logo、水印。clean silhouettes, controlled detail, low noise; no random speckle, muddy micro-texture, over-sharpened halos, fake detail, JPEG artifacts.
```

### AIGC IMAGE-TO-VIDEO PROMPT

```text
[STYLE_FINGERPRINT] 输入帧的21:9旧纸蛋彩正面群像：深青工装、褪砖红高门、灰蓝晨气、低频纸纹、朴拙清楚轮廓、压平而可读的三层队列、克制面部和真实体型差。

[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the approved SH05 source style, all eight identities, exact species, one-cat rule, uniforms, relative scale, door geometry, palette, lighting and composition in every frame. Animate only the assigned staggered micro-actions and a restrained camera settle; do not redraw faces, exchange species or alter costume.

[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal fur, live action, plastic CGI, game render, generic anime, cel shading, glossy illustration, watercolor conversion, oil impasto, added grain or high-frequency detail.

[NARRATIVE_TIME] FACTORY_LAST_SHIFT / ORDERED_QUEUE_BEFORE_MACHINE_HALL；打卡后、进入机器大厅前。

[CHARACTER_STATE_LOCK] state_id=FACTORY_BIPED_UNIFORM；阿白为唯一猫，另有狗、羊、兔、象、驴、熊、狐狸各一，八位始终两足深蓝工装。

[STATE_TRANSITION_RULE] 本镜无状态转换；只推进八种错峰队列微动作，不换华服、不脱工装、不四足化。

[DURATION] 3.0s

[DURATION_RATIONALE] 队列只承担一次秩序性停顿与轻微前移；3秒足够识别八个不同相位和门洞比例，且比长群像更能控制身份、肢体与动作克隆风险。

[TIMELINE]
0.0–0.8s: 表演：平视35mm相机稳定，只有极轻微向前压近；狗、羊前排静候，兔开始抬工牌，象一爪接近帽檐，阿白准备侧移，驴耳后转，熊呼吸，狐狸尾尖微收。全景深、灰蓝主光、门内暖光与建筑尺度锁定；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
0.8–1.7s: 表演：兔把工牌抬到腰胸间即停；象慢慢扶正帽檐；阿白横移半步并把灰绿眼线转向门内，尾巴随重心迟缓摆动；狗与羊只各挪不同幅度的半步，绝不齐步；驴、熊、狐狸保持各自微动作。相机前压极小，不改变队列层次；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
1.7–2.4s: 表演：前排停止，兔手爪下沉少许，象放下手臂；阿白侧移完成并稳定；驴长耳回正，狐狸抬眼，熊仅胸腹呼吸。门灯、窗格、工装颜色和每个角色相对高度不变，无角色互相遮没；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
2.4–3.0s: 表演：相机减速成完全静止，八位角色形成“即将进入”的不同停顿；衣角、耳尾settle，留0.3秒稳定终帧。终态保持大象可通行门洞与阿白唯一猫身份；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。

[CONTINUITY_LOCKS] FACTORY_BIPED_UNIFORM；阿白＝ABAI_FACTORY_UNIFORM_PHOTOLOCK且唯一猫；七配角身份、工装与相对体型固定；狗羊兔象阿白驴熊狐各一；门洞和高窗尺度锁；运动方向进厂；无乐器、托盘、酒杯、华服或四足化。

[NEGATIVE] 无同步举牌／齐步、无动作互换、无角色复制或消失、无猫群、无脸型重绘、无肢体增减、无衣服变化、无建筑缩放、无门窗变形、无突然镜头移动、切镜、闪烁、纹理爬行、噪点或拖影。

[AUDIO] 仅环境声：极轻工装摩擦、分散脚步停住、工牌边缘碰衣、远处金属大厅低鸣；无对白、口号、音乐或BGM。《The Masterplan》仅后期剪辑。
```

---

## SH06｜机器大厅压住阿白｜00:16–00:19｜3.0s

### IMAGE PROMPT

```text
[NARRATIVE_TIME] FACTORY_LAST_SHIFT；队列进入机器大厅，生产线抵达最后停机前一刻。

[CHARACTER_STATE_LOCK] 画面绑定 FACTORY_BIPED_UNIFORM，只有一个可读角色：阿白＝ABAI_FACTORY_UNIFORM_PHOTOLOCK，两足年轻长毛白猫工人，圆润真实猫脸、灰绿眼、粉鼻、帽沿旁非对称天然灰黑头顶斑边缘、深灰蓬松尾；深蓝旧棉工装遮住大部分背部鞍状斑，双爪自然垂低，空爪。无第二只猫、无其他可读工人、无小提琴、酒杯、背心或华服。

[STATE_TRANSITION_RULE] 无状态转换；阿白始终两足工装，不脱衣、不四足化。

[INTENTIONAL_REALITY_EXCEPTIONS] []。机器的压迫感来自真实工业尺度和构图，不允许阿白缩成玩偶、机器悬浮或空间不可能。

[STYLE_FINGERPRINT] 21:9 DFT旧纸蛋彩／哑光水粉工业极远景；深青、氧化绿、炭灰机器与褪砖红梁架形成大块压迫形，阿白乳白小剪影作为唯一亮点。旧纸低频纹理、朴拙结构线、干刷磨损、灰蓝漫射高窗光和少量旧芥末仪表反光；平面化纵深由轨道、栏杆和重复窗格建立，清楚低噪而非脏乱蒸汽朋克。

[REFERENCE_ROLES] DFT参考＝媒介、色彩、平面空间和安静荒诞；三张阿白照片＝身份；批准阿白板＝工装两足比例；`CHARACTER_STATE_LEDGER_V1.md`＝ABAI_FACTORY_UNIFORM_PHOTOLOCK；`SCALE_LEDGER_V1.md`＝机器大厅、栏杆、梯级和高窗尺度；FIN-003为KEEP构图候选时只可验证机器／轨道压迫关系，不覆盖活动风格、身份或本提示细节。

[SUBJECT_AND_ACTION] 巨大的停产机器大厅中，阿白独自站在一条轨道旁面对主传动机，身体略疲惫但重心稳；传动轮仍有最后一点惯性，整个空间仿佛比它更早知道停工。阿白不是英雄姿态，只是一个小工人等待机器停下。

[CAMERA_AND_COMPOSITION] 21:9低机位工业极远景，24mm感，相机约0.5m高，位于轨道右侧并朝左后主机斜看。前景两条轨道形成强透视线，中景阿白位于右下三分之一且完整可辨，左中主机占画面主要重量；背景高窗、梁架与检修平台逐层压向上方。保持深景深，焦点主要在阿白与主机连接区域；不让广角把阿白头身拉伸。

[LIGHTING] 左后高窗灰蓝柔光切出机器大形，阿白有一圈很弱奶白侧缘；仪表和远处工作灯给氧化绿机器少量旧芥末反光。地面与轨道阴影一致、暗部保留层级；无火花、烟、强光束或舞台感。

[SPACE_AND_CONTINUITY] 阿白从SH05高门进入后面对厂内主机，屏幕视线由右向左；轨道通向SH07传动轮细节所在区域。机器大厅檐口、梁架、高窗、平台、栏杆和梯级是同一可用工业系统；SH07之后机器完全停住，SH08从厂门散出。

[SCALE_LOCK] 大厅主跨净高约8–12m、檐口6–8m；工业高窗窗台约1.1m、窗顶约3.2m，阿白1.55m不得与整扇高窗等高；平台栏杆约腰高、梯级可用。主机可巨大但轴承、平台和维护通道与阿白尺寸一致；轨距、投影和地平线证明阿白站在地面而非模型台。

[GROUP_ACTION_LOCK] 非群像。唯一阿白站立面向机器，双爪低垂、耳朵克制前倾、眼线落在传动轮；不增加背景猫、工人复制或围观群体。

[NEGATIVE] 禁止第二只猫、背景猫影、阿白旧黑毛撮／琥珀眼／单肋纹／白尾、巨大卡通眼、人手、额外肢体；禁止小提琴、华服、酒杯、四足姿态；禁止机器像玩具、阿白与高窗同高、栏杆微缩、轨道错误透视、悬浮零件、火花、烟、蒸汽、末日废墟；禁止写实、3D、日漫、赛博朋克、过密机械细节；禁止文字、logo、水印。大形优先、结构清楚、低噪；no random speckle, muddy texture, sharpening halos, fake pixel detail, JPEG artifacts.
```

### AIGC IMAGE-TO-VIDEO PROMPT

```text
[STYLE_FINGERPRINT] 输入帧的21:9旧纸蛋彩工业空间：深青氧化绿大机器、褪砖红梁架、灰蓝高窗光、低频纸纹、朴拙结构线、平面化轨道纵深和唯一乳白阿白小剪影。

[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the exact input artwork, Abai identity and factory state, machine geometry, rail perspective, scale, palette, lighting and matte paper medium. Animate only the final residual machine motion, Abai's restrained breathing/ear response and a very slow low-camera push. Never redesign or enlarge Abai.

[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No live-action factory, photoreal cat, CGI, game/cyberpunk render, anime, cel shading, glossy digital painting, watercolor, smoke-overlay restyle, added grit or sharpened AI detail.

[NARRATIVE_TIME] FACTORY_LAST_SHIFT / LAST_MACHINE_CYCLE；生产线停机前一刻。

[CHARACTER_STATE_LOCK] state_id=FACTORY_BIPED_UNIFORM；唯一可读角色阿白保持 ABAI_FACTORY_UNIFORM_PHOTOLOCK 两足深蓝工装，空爪，无第二只猫或其他可读角色。

[STATE_TRANSITION_RULE] 阿白服装与身体状态全程不变；唯一变化是机器由极低速趋近停止，不允许换装或四足化。

[DURATION] 3.0s

[DURATION_RATIONALE] 该镜只需建立巨大空间、阿白等待和机器最后惯性；3秒能完成一次受控减速并切入SH07细节，不需要额外动作或长时间空停。

[TIMELINE]
0.0–0.8s: 表演：低机位24mm相机沿轨道向前极慢推；主传动轮仅有很小残余旋转，皮带低幅振动。阿白双脚稳、双爪垂低、面向左侧机器，只做呼吸；焦点覆盖阿白和主轮，高窗光、曝光、轨道反光锁定；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
0.8–1.7s: 表演：传动轮进一步减速，皮带摆幅变小；阿白一只耳朵向声音方向转少许，灰绿眼线不离机器，尾尖仅轻摆后停。相机推近保持直线、无摇摆，前景轨道产生微视差，建筑尺度不变；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
1.7–2.4s: 表演：机器接近静止，仪表指针只做极小回落；阿白重心从一脚微移至双脚但不迈步，工装下摆轻落。光线、纸纹、机器结构、窗口与平台全部锁定，不添加灰尘云或火花；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
2.4–3.0s: 表演：传动轮停在可接SH07的明确角度，相机缓停；阿白耳朵回到克制前向，身体与衣料settle。终帧保持巨大机器压住唯一阿白的构图和可用工业尺度；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。

[CONTINUITY_LOCKS] 阿白＝ABAI_FACTORY_UNIFORM_PHOTOLOCK且唯一猫；两足、工装、空爪、照片斑纹与深灰尾锁定；主机、轨道、平台、高窗位置与比例固定；屏幕视线右向左；无烟、无其他角色、无乐器或换装。

[NEGATIVE] 无身份重绘、无脸／斑纹／尾色变化、无猫复制、无肢体变形、无机器融化或新零件、无轨道滑移、无烟火、无突然停顿跳帧、无切镜、无镜头晃动、无闪烁、纹理爬行、噪点或残影。

[AUDIO] 仅环境声：逐渐变慢的低频传动嗡鸣、皮带轻拍、轨道细微共振、阿白工装摩擦；无对白、喵叫、音乐或BGM。《The Masterplan》后期剪辑加入。
```

---

## SH07｜传动归零｜00:19–00:21｜2.0s

### IMAGE PROMPT

```text
[NARRATIVE_TIME] FACTORY_LAST_SHIFT；SH06同一机器在最后惯性阶段，即将完全停住。

[CHARACTER_STATE_LOCK] 本镜叙事状态绑定 FACTORY_BIPED_UNIFORM；无人物。若边缘出现极小工装色块也不得形成可读身体或阿白身份；画面只包含机器、压力表、皮带轮和灰尘。

[STATE_TRANSITION_RULE] 无角色状态转换；机器由“低速残余运动”进入“完全停止”是唯一允许变化。

[INTENTIONAL_REALITY_EXCEPTIONS] []。皮带、轮轴、指针与灰尘均遵守普通惯性和重力，不出现自发魔法或超自然发光。

[STYLE_FINGERPRINT] 21:9 DFT旧纸蛋彩／哑光水粉机械插镜；氧化绿皮带轮、炭灰皮带、褪黄压力表和灰蓝机器暗面构成少量大形，朴拙结构线、低频旧纸纹、干刷普通磨损、柔和窗光。清楚而节制的机械信息，背景压成平面暗色、清晰低噪，不堆赛博零件，不以噪点冒充细节。

[REFERENCE_ROLES] DFT参考＝旧纸画材、哑光旧物和色调；`STYLE_BIBLE_V1.md`＝工业旧物但非末日；`SCALE_LEDGER_V1.md`＝机器零件与检修尺度；SH06批准源图＝最高优先的同一机器、色彩、光线和空间连续性参考，仅在正式生成SH06后使用。旧被否决机械图不得进入活动链。

[SUBJECT_AND_ACTION] 主皮带轮正处于最后半圈减速，压力表指针离零位只剩很小角度，一小束积尘从上方横梁边缘松开、尚未落下。画面没有人物，观众通过机械归零理解“工作真的结束了”。

[CAMERA_AND_COMPOSITION] 21:9机械特写，85mm感，平视略低，从主轮轴侧前方观察。皮带轮占左半，压力表位于右上黄金点，横梁尘粒从上中进入；轮轴、皮带、表盘形成三角，不正中对称。浅至中景深，焦点在轮轴和压力表针，尘粒轮廓可读，背景不生成伪刻度或文字。

[LIGHTING] 左上高窗灰蓝软光沿轮缘滑过，压力表玻璃只有一块柔弱反光，机器暗部由低填充保留结构。无火花、无发光刻度、无强镜面、高亮光晕或烟雾。

[SPACE_AND_CONTINUITY] 与SH06主机同一侧、同一窗光、同一氧化绿涂层；轮轴停止角度应能从SH06终帧连续过来。SH08离厂前机器保持停住；压力表无可读品牌和数字，只以简单刻度表示零位。

[SCALE_LOCK] 轮轴、皮带厚度、表盘与固定螺栓按工业设备真实关系；无巨型玩具表或微小皮带。重力方向与SH06地面一致，灰尘只向下落，所有零件固定连接、不悬浮。

[GROUP_ACTION_LOCK] 不适用；画面中不得添加人物、手、动物头、猫影或围观者。

[NEGATIVE] 禁止人物、手、猫、动物、服装、文字、数字伪字、logo、水印；禁止火花、烟、蒸汽、爆炸、魔法发光、末日破坏；禁止轮轴多一根、皮带复制或断裂、表针重复、零件融化、错误机械连接、灰尘向上；禁止照片写实、3D、日漫、赛博朋克、过密机械纹理；no random speckle, gritty dust cloud, muddy micro-texture, over-sharpened halos, fake pixel detail, JPEG artifacts, noisy background.
```

### AIGC IMAGE-TO-VIDEO PROMPT

```text
[STYLE_FINGERPRINT] 输入帧的21:9旧纸蛋彩机械特写：氧化绿轮体、炭灰皮带、褪黄表盘、灰蓝窗光、低频纸纹、朴拙结构线和干净暗背景。

[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the exact source medium, machine design, part count, scale, paint wear, palette, lighting, lens feel and composition. Animate only physically credible deceleration, pointer return and a few falling dust motes; do not redraw or add machinery.

[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal machinery, CGI, game/cyberpunk render, anime, glossy metal, watercolor wash, extra grit, smoke overlay, synthetic grain or sharpened microdetail.

[NARRATIVE_TIME] FACTORY_LAST_SHIFT / MACHINE_COAST_TO_STOP；SH06同一机器的最后惯性阶段。

[CHARACTER_STATE_LOCK] state_id=FACTORY_BIPED_UNIFORM；本镜无可读人物，叙事仍处于全员两足工装阶段，边缘不得生成阿白或任何完整角色。

[STATE_TRANSITION_RULE] 角色状态不转换；只允许机器由残余运动进入完全停止，禁止新增人物、换装或野生化。

[DURATION] 2.0s

[DURATION_RATIONALE] 纯机械标点只需完成一次减速归零和尘粒落下；2秒提供清楚冲击并保持节奏，超过2秒会变成无叙事停留。

[TIMELINE]
0.0–0.5s: 表演：85mm相机完全锁定；皮带轮以极低速度继续转动，皮带振幅小，压力表针缓慢靠近零位；一小束尘粒刚松开。焦点、灰蓝窗光、表面反光与曝光保持；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
0.5–1.2s: 表演：轮体减速到停止，皮带做一次幅度很小的回摆；表针到零并轻微回弹后固定。尘粒按重力穿过轮缘前方，不能成为浓尘云；所有螺栓和结构保持不变；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
1.2–1.7s: 表演：机器完全静止，只有最后几粒尘继续下降；表玻璃反光不闪烁，相机不动，纸纹不爬。声音余振衰减，画面暗部和尺度锁定；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
1.7–2.0s: 表演：尘粒落出焦平面，所有运动完全settle，留下0.3秒稳定终帧：轮停、针归零、无人物，便于切到离厂；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。

[CONTINUITY_LOCKS] 同一SH06主机、同一轮轴与压力表；零件数量、停止角度、氧化绿涂层、光线、重力方向与DFT媒介固定；全镜无人、无文字、无烟火。

[NEGATIVE] 无反向加速、无皮带断裂、无指针复制、无新零件、无火花烟雾、无镜头移动或意外切镜；无闪烁、纹理爬行、边缘沸腾、噪点、运动残影或压缩伪影。

[AUDIO] 仅拟音：传动低鸣迅速衰减、一次轻微皮带回摆、表针小碰声、尘粒落在金属上的极轻声；无音乐、BGM、对白。《The Masterplan》后期加入。
```

---

## SH08｜离厂，阿白回望半步｜00:21–00:24｜3.0s

### IMAGE PROMPT

```text
[NARRATIVE_TIME] FACTORY_LAST_SHIFT；机器完全停止后，下班铃已响，工人从厂房高门散出；第一次换装尚未开始。

[CHARACTER_STATE_LOCK] 阿白＝ABAI_FACTORY_UNIFORM_PHOTOLOCK且是唯一猫，位于侧后方，两足深蓝工装、灰绿眼、粉鼻、帽沿边天然头顶灰黑斑、深灰蓬松尾；狗、羊、兔、大象、驴、熊、狐狸各一个，均为 SUPPORTING_CAST_IDENTITY_LOCK_V2 的 FACTORY_BIPED_UNIFORM，空爪或持无字工牌。无华服、无乐器、无托盘／酒杯、无四足野生状态。

[STATE_TRANSITION_RULE] 本镜无状态转换；全体保持两足工装。阿白只是停半步回望，不得脱衣或变形。

[INTENTIONAL_REALITY_EXCEPTIONS] []。群体从高门散出遵守普通步态、体型和门洞通行；阿白的停顿不冻结其他角色。

[STYLE_FINGERPRINT] 21:9 DFT旧纸蛋彩／哑光水粉；深青工装从灰蓝厂房暗部流向较亮院外，褪砖红门墙与旧芥末门灯形成克制温差。旧纸低频纹理、朴拙清楚人物边缘、平面而分层的横向流动、低饱和哑光；阿白乳白脸和深灰尾作为小而明确的身份点，背景不脏不密、清晰低噪。

[REFERENCE_ROLES] DFT参考＝媒介、调色、平面空间与情绪；阿白照片＋批准板＝唯一阿白身份与工装；`SUPPORTING_CAST_IDENTITY_LOCK_V2.md`＝配角身份、体型、统一工装；旧A/B板仅身份服装受限用途，禁止道具和排排站；`SCALE_LEDGER_V1.md`＝厂门和大象通行；SH05批准图＝角色服装与体型连续性，SH06／SH07＝停机因果；不得以旧否决离厂图替代活动构图。

[SUBJECT_AND_ACTION] 高大厂门中，七位配角以不同步幅向院外和更衣室方向散出：兔已在最前、狗走过门槛、羊侧让、熊慢起步、狐狸靠墙掠过、驴跨出较长一步、大象最后仍在门内。阿白位于画面右中侧，身体刚停半步，头与灰绿眼回望机器大厅，其他人继续离开。观众应清楚感到它比队伍晚一拍，而非成为领袖。

[CAMERA_AND_COMPOSITION] 21:9中宽景，50mm感，相机位于院内偏左、距地约1.4m，沿门口侧轴观察从左后向右前流出的队伍。厂门占左中并露完整门顶，大象在门内后层；兔和狗分别在前景不同边缘；阿白在右中三分之一留有回望方向负空间，脸清楚但不做特写。前景移动角色形成自然遮挡，中景阿白，背景机器厅暗部；中等景深锁焦阿白并保持门洞可读。

[LIGHTING] 院外灰晨光从右前柔和照入，门内更暗；阿白乳白脸获得自然侧前光，深蓝工装和深灰尾不丢失。旧芥末门灯给门边一线暖色，大象轮廓与门暗部分离；投影方向一致，无戏剧光束。

[SPACE_AND_CONTINUITY] 延续SH05高门和SH06机器大厅轴线；队伍总体由厂内左后走向院外右前，再进入SH09更衣室。阿白回望方向准确指向SH06主机；机器保持停止、烟囱无烟。门口路径宽，不让角色穿墙或互相穿透。

[SCALE_LOCK] 主门≥3.3m高、≥2.8m宽，大象可在后景自然通过；门顶高于所有两足角色。阿白1.55m与大象2.55m、熊2.05m、兔1.30m等体型关系稳定；前景角色因靠近可大但由遮挡、地面和50mm透视解释，后景大象不能被缩成小于兔。脚地投影、门槛和高窗共同证明尺度。

[GROUP_ACTION_LOCK] 兔＝前景已过门、短步；狗＝跨门槛；羊＝侧让；熊＝慢起步；狐狸＝贴墙走；驴＝长步跨出；大象＝最后在门内慢行；阿白＝停半步回望。八种角色八种相位，各一实例；唯一同步只有共同离厂方向，不得齐步或同时回头。

[NEGATIVE] 禁止全员回望、全员齐步、横排离场、复制姿势、角色穿透；禁止第二只猫、背景猫、重复主角色；禁止阿白身份斑／眼色／尾色漂移、旧黑毛撮、琥珀眼、单肋纹；禁止华服、乐器、托盘、酒杯、四足化、人手、额外肢体；禁止门小于大象、动物大过建筑、透视尺度漂移；禁止烟、火、废墟、恐怖、写实、3D、日漫、吉祥物；禁止文字logo水印、随机颗粒、泥状纹理、锐化光晕、伪细节和噪声背景。
```

### AIGC IMAGE-TO-VIDEO PROMPT

```text
[STYLE_FINGERPRINT] 输入帧的21:9旧纸蛋彩离厂群像：深青工装、灰蓝厂内外、褪砖红高门、低频纸纹、清楚朴拙剪影、平面分层流动与唯一乳白阿白身份点。

[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the exact input art style, eight identities, one-cat rule, uniforms, relative species scale, door geometry, lighting, axis and composition. Animate only the assigned staggered exit steps, Abai's half-step pause/head turn, cloth/ear/tail settling and a minimal side-camera drift.

[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal animals, live action, CGI, game render, anime, cel shading, glossy illustration, watercolor or oil conversion, extra grain, noisy fur or identity redraw.

[NARRATIVE_TIME] FACTORY_LAST_SHIFT / EXIT_AFTER_SHUTDOWN；停机与下班铃之后、第一次换装之前。

[CHARACTER_STATE_LOCK] state_id=FACTORY_BIPED_UNIFORM；阿白唯一猫，狗、羊、兔、象、驴、熊、狐狸各一，八位全程两足深蓝工装。

[STATE_TRANSITION_RULE] 无状态转换；仅阿白停半步回望，其他七位继续离厂，不脱衣、不穿华服、不四足化。

[DURATION] 3.0s

[DURATION_RATIONALE] 主要叙事动作只有“群体继续离开、阿白停半步回望”；3秒可读清反差并在阿白眼线上落稳，避免多角色长运动造成复制与变形。

[TIMELINE]
0.0–0.7s: 表演：50mm侧轴相机沿队伍方向极慢向右短移；兔已出门继续短步，狗跨门槛，羊侧让，熊起步，狐狸贴墙，驴长步，大象后层慢行；阿白还随队走。焦点在阿白与门洞之间，外冷内暗光比锁定；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
0.7–1.5s: 表演：阿白前脚落下后不再迈第二步，身体减速；头先停、耳朵再轻转向左后机器厅，灰绿眼跟随。其他七位按各自速度继续，不回头、不齐步；相机仍缓滑，前景产生轻微视差，门洞和体型不变；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
1.5–2.3s: 表演：阿白完成回望，双脚稳、尾巴因惯性小幅摆后回；狗与兔逐渐出前景，羊、熊、狐、驴错开通过，大象仍在高门内但前进一步。景深轻微拉到阿白脸，曝光不呼吸，工装与毛色不改变；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
2.3–3.0s: 表演：相机和阿白动作缓停，阿白保持半秒克制回望；其余人物继续离开画面但不凭空消失，大象脚步settle。最终帧给阿白脸、回望负空间和高门净空，便于切入更衣室；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。

[CONTINUITY_LOCKS] FACTORY_BIPED_UNIFORM；阿白唯一猫且身份照片锁；七配角各一、相对体型和工装固定；机器已停、厂门尺度固定；运动由左后至右前，阿白眼线反向指向机器；无换装、乐器、托盘、酒杯或四足状态。

[NEGATIVE] 无全员回头、无齐步、无动作互换、无复制角色、无猫群、无身份或斑纹漂移、无肢体变形、无穿墙穿人、无门缩小、无建筑呼吸、无意外切镜、突变焦、闪烁、纹理爬行、噪点或残影。

[AUDIO] 仅环境声：错峰脚步、蹄足与大象低频落地、工装布摩擦、门内已停机器的残余空响、一次很轻的下班铃尾音；无对白、音乐、BGM。《The Masterplan》仅后期加入。
```

---

## SH09｜更衣室空间与进门阶段｜00:24–00:28｜4.0s

### IMAGE PROMPT

```text
[NARRATIVE_TIME] FACTORY_LAST_SHIFT / BEFORE_FIRST_WARDROBE_TRANSITION；离厂后进入公共更衣室，第一件工装尚未正式脱下。

[CHARACTER_STATE_LOCK] 八位活动角色全部保持 FACTORY_BIPED_UNIFORM。阿白＝ABAI_FACTORY_UNIFORM_PHOTOLOCK，唯一猫，最后进入；绵羊、大象、驴、老狗、狐狸、兔、熊＝SUPPORTING_CAST_IDENTITY_LOCK_V2 的工厂状态，统一深蓝旧棉工装按体型放码。熊空爪、无托盘；所有人无乐器、酒杯、华服。两足拟人结构完整，每位一头、两臂／前肢、两腿、一尾（大象另有一鼻、两短牙），无四足野生结构。

[STATE_TRANSITION_RULE] 本镜仍在第一次换装边界之前；不得脱掉整件工装、不得穿私服。仅允许走向柜位、坐下、开柜、观察空间等预备动作；绝不触发最终 WILD_RETURN_QUADRUPED。

[INTENTIONAL_REALITY_EXCEPTIONS] []。不同体型共用更衣室，但门、通道、柜、衣钩和长凳必须实际可用；高低衣钩是功能设计，不是梦境尺度。

[STYLE_FINGERPRINT] 21:9 DFT旧纸蛋彩／哑光水粉室内群像；深青铁柜、灰蓝高窗、水泥地、暖灰顶灯和褪色木凳组成安静大形，旧纸低频纤维与干刷普通磨损可见但不脏。角色工装形成统一深青节奏，物种头部与体型打破同质；横向平面空间通过门、柜列、凳、前中后遮挡建立，整体亮度比参考高一档、低饱和、清晰低噪。

[REFERENCE_ROLES] DFT参考＝唯一美术媒介、色谱、边缘与气质；阿白照片＋批准板＝阿白身份／两足工装；`SUPPORTING_CAST_IDENTITY_LOCK_V2.md`＝七位配角身份和工装；旧A/B板若加载只限身份服装，严禁乐器、托盘、排排站、缺失第三状态；`ENV-01_WHITEBOX_3VIEWS_attempt_002.png`＝门、柜列、三层衣钩、长凳、主通道和出口的空间／遮挡预演，只作几何与机位参考，绝不继承白模材质、灯光、灰模风格；`ENV-01_LOCKER_ROOM_SETTING_attempt_002.png`＝待导演判定的空间候选，只可辅助布局，不得覆盖DFT风格和角色；`SCALE_LEDGER_V1.md`、`GROUP_ACTION_LEDGER_120S_V2.md#SH09`＝尺度与动作权威。ENV-01 attempt_001和其他被否决旧设定禁止使用。

[SUBJECT_AND_ACTION] 高位建立整个公共更衣室及八位角色的不同到达阶段：熊已经先坐到长木凳一端；兔正走向低层衣钩；大象仍停在足够高宽的主门边，身体尚未完全进室；老狗只打开一扇铁柜门；阿白最后进入、看向自己的中层柜位；羊在凳后取下无字工牌，驴沿主通道慢走，狐狸在镜边停下观察。无人开始同一个脱衣动作。

[CAMERA_AND_COMPOSITION] 21:9高位空间建立大全景，24–28mm感，相机位于入口对角上方约3.2m、朝柜列和出口斜俯，不做垂直顶视。前景门框与一截高柜形成自然框景；中景长凳纵向引导，八位角色分布在门、凳、柜、衣钩和通道；背景高窗与出口可读。阿白位于右后入口附近且不居中，大象在左侧高门处；保持深景深，柜列、脚地、门顶和人物脸都可辨。

[LIGHTING] 高窗灰蓝漫射光从左上进入，暖灰顶灯为低强度实景填充，形成冷外暖内但不温馨过度的层次；柜门边、木凳和角色轮廓有柔软反光。阿白脸有足够填光辨认灰绿眼与天然头顶斑边缘；阴影方向一致、地面无镜面反射，无舞台灯或神秘光束。

[SPACE_AND_CONTINUITY] 使用ENV-01白模轴线：主门位于画面左前／左侧，柜列沿后墙，三层衣钩分布在柜间，长凳居中但不堵主通道，出口在右后。角色从SH08厂门方向进入；SH10继续同一轴线和位置关系，SH11在凳面，SH12沿柜列层次，SH13仍在同一室内。工装仍穿在身上，柜与钩尚未出现整齐挂好的服装结果。

[SCALE_LOCK] 更衣室净高≥4.5m、主门≥3.3m高且≥2.8m宽、主通道≥3.2m；大象2.55m可在门边自然站立并有头顶净空。铁柜2.2–2.4m高，衣钩分高／中／低三层，凳高约0.50m、深0.55m；熊坐凳脚能接地，兔使用低钩，大象对应高钩。至少展示“大象＋主门＋高窗”和“熊／兔＋凳＋柜／衣钩”两套同平面尺度关系，任何角色不得大过整面柜列。

[GROUP_ACTION_LOCK] 熊＝已坐下；兔＝走向低钩；大象＝仍在门边；老狗＝打开一扇柜门；阿白＝最后进入并看自己的柜；羊＝取下工牌；驴＝沿通道走；狐狸＝镜边停看。八个角色八个动作／相位，站、坐、行、停、开柜分散；每个活动主角色仅一，阿白唯一猫，群像至少八种清楚物种轮廓。

[NEGATIVE] 禁止全员已站在衣钩前、排排站、同手位开柜、同时脱衣、动作克隆；禁止第二只猫、背景猫、重复狐狸／象等主角色；禁止乐器、托盘、酒杯、华服、四足化、工装提前消失、人手、额外肢体；禁止门洞低于大象、通道窄到无法错身、柜子小于兔或凳变成展示台、人物与高窗同高、错误透视；禁止继承白模灰材质、写实数字概念图、照片写实、3D、日漫、吉祥物；禁止伪文字、logo、水印、随机颗粒、脏污微纹理、锐化边、伪细节、JPEG artifacts、noisy background.
```

### AIGC IMAGE-TO-VIDEO PROMPT

```text
[STYLE_FINGERPRINT] 输入帧的21:9 DFT旧纸蛋彩更衣室：深青柜、灰蓝高窗、暖灰顶灯、褪色木凳、低频纸纹、朴拙边缘、平面分层空间和八位不同物种的深蓝工装群像。

[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the source image's exact old-paper tempera/gouache medium, all eight identities, one-cat rule, uniforms, room geometry, whitebox-derived layout, scale, palette, lighting and composition. Animate only the assigned arrival/preparation actions and one restrained high-camera drift; do not begin undressing or redesign the room.

[STYLE_NEGATIVE] Strictly do not change or replace the source art style. No whitebox/gray-render look, architectural visualization, photoreal interior, plastic CGI, game render, anime, glossy digital art, watercolor conversion, added grain, dirty texture or identity redraw.

[NARRATIVE_TIME] FACTORY_LAST_SHIFT / BEFORE_FIRST_WARDROBE_TRANSITION；进入公共更衣室，第一件工装尚未脱下。

[CHARACTER_STATE_LOCK] state_id=FACTORY_BIPED_UNIFORM；阿白唯一猫与七位配角均保持两足深蓝工装，只做进入、坐下、开柜、观察等准备动作。

[STATE_TRANSITION_RULE] 本镜停在第一次换装边界之前；禁止脱下整件工装、穿私服或触发四足野生状态。

[DURATION] 4.0s

[DURATION_RATIONALE] 空间建立需让八位角色分别到达门、凳、柜、衣钩位置，同时读清大象通行与多层衣钩；4秒足够完成单一“进入并就位”动作，不承担脱衣结果。

[TIMELINE]
0.0–1.0s: 表演：高位24–28mm相机从入口对角做极慢向内／向右短滑，轴线和俯角锁定；熊已坐并调整重心，兔朝低钩走，象在门边跨入半步，狗手爪接近柜门，阿白刚进画面，羊、驴、狐保持各自路径。全景深、冷窗光暖顶灯、门柜凳尺度不变；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
1.0–2.1s: 表演：老狗拉开唯一一扇柜门约三分之一；兔到低钩前减速但不抬衣；熊坐稳、双爪落膝；大象以真实重量让一侧肩通过高门；阿白慢走两步并把眼线投向自己的中层柜。羊取工牌、驴沿通道、狐狸镜边停住，动作不同步；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
2.1–3.2s: 表演：相机继续轻滑产生门框、凳、柜列的微视差并逐步减速；狗柜门停稳，兔停在低钩前，大象仍有一部分在门边，阿白到达通道侧但不脱衣；羊工牌垂下，驴放慢，狐狸只转眼。衣料、耳尾按物种轻微惯性响应；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
3.2–4.0s: 表演：相机完全缓停，八位角色落在SH10可衔接的不同预备位置；无人开始同步脱上衣。顶灯、高窗、柜门、凳与角色投影稳定，留0.4秒可剪终帧；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。

[CONTINUITY_LOCKS] FACTORY_BIPED_UNIFORM；阿白唯一猫，七配角各一；门／柜／钩／凳／通道按ENV-01空间锁；大象可通行；所有人仍穿完整工装且无乐器华服；SH10沿同一轴线和角色区域继续。

[NEGATIVE] 无提前脱衣、无动作互换、无齐步或排排站、无复制角色、无猫群、无肢体增减、无柜门复制、无门缩小或空间重排、无相机穿墙、无意外切镜；无闪烁、纹理爬行、边缘沸腾、噪点、残影或曝光呼吸。

[AUDIO] 仅环境声：高窗风、分散脚步、木凳轻响、唯一柜门铰链、深蓝工装摩擦；无对白、音乐、BGM、歌声。《The Masterplan》只在后期剪辑。
```

---

## SH10｜第一次脱工装：八种错峰动作｜00:28–00:32｜4.0s

### IMAGE PROMPT

```text
[NARRATIVE_TIME] FIRST_WARDROBE_TRANSITION / AFTER_LAST_SHIFT_BEFORE_PERFORMANCE；第一次脱衣正在进行，工厂身份被逐件卸下，私人华服尚未穿上。

[CHARACTER_STATE_LOCK] 全体仍为两足拟人结构，绑定 FACTORY_BIPED_UNIFORM 的“工装移除进行中”子相位；只允许各自正在操作的一件工装局部打开／脱下。阿白＝ABAI_FACTORY_UNIFORM_PHOTOLOCK，唯一猫，仍穿深蓝工装并低头解最下方纽扣，帽沿旁天然头顶灰黑斑、灰绿眼、粉鼻、深灰尾不变；熊坐着脱一只靴；羊摘工帽；兔把一件外套挂向低钩；象只松一条背带；狗把一只袖口翻出；驴弯腰解鞋带；狐狸在镜边停住。毛色、体型和统一工装以 SUPPORTING_CAST_IDENTITY_LOCK_V2 为准。无私人华服穿上、无乐器、托盘、酒杯。

[STATE_TRANSITION_RULE] 本镜授权从 FACTORY_BIPED_UNIFORM 向 PERFORMANCE_BIPED_PRIVATE_DRESS 的第一次“仅服装”转换，但只完成工装移除的小相位，不完成私服穿着；身体始终两足。最终 WILD_RETURN_QUADRUPED 只允许在SH35，严禁在此提前发生。

[INTENTIONAL_REALITY_EXCEPTIONS] []。简化毛爪／蹄可操作衣扣鞋带，但抓握、袖口、背带、鞋靴和衣钩接触必须可信；不允许人手或凭空脱衣。

[STYLE_FINGERPRINT] 21:9 DFT旧纸蛋彩／哑光水粉高位群像；深青工装在深青柜和褪木凳间形成不同开合形状，灰蓝高窗光与暖灰顶灯保持克制。旧纸低频肌理、朴拙清晰描边、大块可读剪影、低饱和哑光；群像通过高／中／低身体姿态、前中后景和八种手位组织，平面但不拥挤，清晰低噪。

[REFERENCE_ROLES] DFT参考＝媒介、色彩、边缘、平面空间；阿白照片＋批准板＝阿白身份和工装；`SUPPORTING_CAST_IDENTITY_LOCK_V2.md`＝七配角身份、体型、工装；旧A/B图只限身份服装，严禁乐器、熊托盘、排排站；ENV-01白模attempt_002＝空间／相机／遮挡，绝不继承白模风格；SH09批准图＝最高优先的房间、角色位置、光线和服装连续性；`SCALE_LEDGER_V1.md`＝门柜钩凳；`GROUP_ACTION_LEDGER_120S_V2.md#SH10`＝逐角色动作唯一权威；FIN-004及其他旧脱衣图仅作`group_action_repetition`失败证据，禁止构图与姿势继承。

[SUBJECT_AND_ACTION] 同一更衣室中八位角色同时处于完全不同的第一脱衣动作：前左熊坐凳、只脱下一只靴；后中羊一蹄把工帽从角旁摘离；右下小兔把已脱的一件深蓝外套挂到低钩；后左大象慢慢松开一条肩背带；中左老狗只把一只袖口翻到前臂；前中驴弯腰解一侧鞋带；右侧狐狸在镜边停住看众人、双爪不动；右中阿白低头解工装最下方纽扣。关键帧取各动作最可读的中段，不让任何两人都双手捧衣。

[CAMERA_AND_COMPOSITION] 21:9高位宽景，28–35mm感，沿SH09同一入口对角轴线但降低约0.4m并轻微向右，使凳、三层衣钩和八人手位互不遮挡。熊／驴占前景左右形成高低对比，狗和阿白在中景，羊／象在后景，兔与低钩在右下，狐狸以镜边侧影收束。保持中深景深，焦点落在阿白、熊、兔组成的斜线，同时让后景羊帽和象背带清楚；镜面不复制人物。

[LIGHTING] 继承SH09高窗冷光和暖灰顶灯；主光从左上勾出工装开口与毛色边缘，弱暖灯补足脸和爪的动作细节。地面、凳、柜与角色投影一致；衣物暗部保留深青层次，无裸露皮肤、无戏剧聚光或神秘变形光。

[SPACE_AND_CONTINUITY] 门、柜列、三层衣钩、长凳、主通道和出口完全延续SH09；角色动作在各自站位完成，不互换区域。摘下／松开的工装仍是普通深蓝棉衣物，SH11将其中一件放上凳面，SH12才更明确露出个体毛色，SH13才穿私人华服。镜面只反射空间色块，不生成第二个狐狸或第二个阿白。

[SCALE_LOCK] 净高≥4.5m、门≥3.3×2.8m、通道≥3.2m；柜2.2–2.4m，衣钩分层，凳高0.50m。兔只够到低钩，羊使用中层，大象背带动作不顶天花；熊坐凳脚着地、驴弯腰仍不与柜同高。角色相对尺寸按账本固定；衣物、鞋靴和纽扣按使用者缩放，不出现巨衣／玩具靴。脚地、坐凳和衣钩承重关系清楚。

[GROUP_ACTION_LOCK] 熊＝坐着脱一只靴；羊＝摘帽；兔＝挂外套到低钩；象＝松一条背带；狗＝翻一只袖口；驴＝弯腰解一侧鞋带；狐狸＝停看、空爪；阿白＝解最下方纽扣。八个动作动词、手位、身体高度和相位不同；每个主角色一个，阿白唯一猫；禁止用“所有人脱衣”概括或复制。

[NEGATIVE] 禁止全员脱上衣、全员双手捧衣、同胸前手位、同角度站立、相同动作相位、镜像复制、排排站；禁止第二只猫、镜中复制角色、重复狐狸／象；禁止工装瞬间全部消失、提前穿华服、乐器、托盘、酒杯、四足化、半人半兽、裸露人皮、人类手、额外肢体、衣服穿过身体；禁止兔够高钩、大象顶门、凳柜缩放错误、脚悬浮；禁止FIN-004旧构图泄漏、照片写实、3D、日漫、恐怖、变形光；禁止文字logo水印、随机颗粒、泥状纹理、过锐边、伪细节、JPEG artifacts、noisy background.
```

### AIGC IMAGE-TO-VIDEO PROMPT

```text
[STYLE_FINGERPRINT] 输入帧的21:9 DFT旧纸蛋彩更衣室群像：深青柜与八件工装动作、灰蓝窗光、暖灰顶灯、褪木凳、低频纸纹、朴拙大形、分层高低姿态和清晰低噪表面。

[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the exact source style, room, camera axis, eight identities, one-cat rule, species anatomy, uniforms, action assignments, relative scale, lighting and composition. Each performer may continue only the single assigned micro-action; do not synchronize, exchange actions, complete private dressing or begin quadruped transformation.

[STYLE_NEGATIVE] Strictly do not change or replace the source art style. No photoreal fur/fabric, CGI, game render, anime, cel shading, glossy illustration, watercolor, body-horror transformation, whitebox look, added grain, muddy texture or identity redraw.

[NARRATIVE_TIME] FIRST_WARDROBE_TRANSITION / UNIFORM_REMOVAL_START；最后一班结束后，第一次脱工装刚开始。

[CHARACTER_STATE_LOCK] state_id=FIRST_WARDROBE_TRANSITION；八位保持两足结构，仅各自操作一件工装局部，阿白为唯一猫，私人华服尚未穿上。

[STATE_TRANSITION_RULE] 仅授权 FACTORY_BIPED_UNIFORM 向 PERFORMANCE_BIPED_PRIVATE_DRESS 的服装过渡小相位；本镜不得完成私服穿着，身体不得变化。

[DURATION] 4.0s

[DURATION_RATIONALE] 八人各完成一个互不相同的短脱衣动作，需要约4秒读清开始、执行与settle；不串联第二个动作，不在本镜穿上华服，因此单源群像仍可稳定生成。

[TIMELINE]
0.0–1.0s: 表演：高位28–35mm相机沿SH09轴线做极慢向右下滑，保持全体可见；熊抬起一只脚、羊触帽、兔举外套向低钩、象抓一条背带、狗触袖口、驴俯身到鞋带、狐狸停住、阿白毛爪到最下扣。焦点、冷窗暖灯、门柜凳尺度锁定；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
1.0–2.2s: 表演：八人分别推进唯一动作：熊把靴拉至脚跟；羊帽离开角根；兔将外套衣领挂上低钩；象只松一段背带；狗把一只袖口翻出；驴解开一个鞋带结；狐狸仅眼线移动；阿白解开最下扣。动作速度按体型不同，任何两人不同时抬双爪；相机轻滑产生克制视差；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
2.2–3.2s: 表演：熊靴完全离一脚并停在爪边；羊帽下降到一侧；兔松开已承重的低钩；象背带垂松但工装仍穿；狗袖口停在前臂；驴鞋带散开；狐狸呼吸；阿白最下衣襟分开一小段。衣物物理响应真实，不凭空消失，角色不换位置；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
3.2–4.0s: 表演：相机缓停，各人保持不同完成相位：一只靴离脚、帽刚摘、外套刚挂、背带刚松、单袖翻起、单鞋带解开、停看、下扣解开。耳尾和布料settle，留0.4秒可剪终帧；无人开始第二个动作或穿华服；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。

[CONTINUITY_LOCKS] FIRST_WARDROBE_TRANSITION；全体两足；阿白唯一猫且工装身份锁；七配角各一；八个动作分工不交换；ENV-01空间、门柜钩凳比例、SH09轴线与光线锁定；无私人服装、乐器、托盘、酒杯、四足化。

[NEGATIVE] 无动作克隆、同步脱衣、动作互换、重复角色、镜中分身、猫群、肢体增减、人手、衣物穿模、瞬间裸体、华服跳变、四足／恐怖变形；无相机切轴、突然推拉、空间重排、门柜变形、灯光闪烁、纹理爬行、噪点或残影。

[AUDIO] 仅环境声：八种分散布料摩擦、单只靴落木地／水泥的闷声、帽布轻响、衣钩一声、柜室空气与高窗风；无对白、音乐、BGM、歌声。《The Masterplan》只后期配乐。
```

---

## SH11｜工装被折平｜00:32–00:35｜3.0s

### IMAGE PROMPT

```text
[NARRATIVE_TIME] FIRST_WARDROBE_TRANSITION / AFTER_UNIFORM_REMOVAL_BEFORE_PRIVATE_DRESS；第一次脱衣继续，工装开始被普通而认真地收好。

[CHARACTER_STATE_LOCK] 前景只显示年长绵羊的灰白卷毛前臂与两只简化蹄爪，仍为两足拟人结构；深蓝工装外套已脱下，绵羊尚未穿旧芥末衬衫／深青披肩。背景只以柔焦显示灰米兔的两足侧影，正把另一件深蓝工装挂到低钩，未穿演出服。无阿白、无猫、无乐器、托盘、酒杯；毛爪／蹄爪不可变成人手。

[STATE_TRANSITION_RULE] 仅允许第一次服装转换继续：工装被折叠／挂起，但私人华服尚未进入画面；身体保持两足。禁止提前WILD_RETURN_QUADRUPED。

[INTENTIONAL_REALITY_EXCEPTIONS] []。蹄爪的简化操作遵守可读抓握与布料承重；工装不得自行折叠、悬浮或变形。

[STYLE_FINGERPRINT] 21:9 DFT旧纸蛋彩／哑光水粉手部与衣物插镜；深蓝旧棉布、褪色木凳、灰白卷毛和远处深青柜组成安静大形。旧纸低频纹理与克制干刷表现布料普通磨损，朴拙边缘但接触轮廓清楚；浅景深仍保留背景低衣钩的位置，色彩低饱和、表面干净低噪，细节只集中在折痕与蹄爪接触。

[REFERENCE_ROLES] DFT参考＝媒介、旧物色调和手工边缘；`SUPPORTING_CAST_IDENTITY_LOCK_V2.md`＝绵羊灰白卷毛／小弯角体系、兔灰米毛与统一工装，旧A/B板仅身份服装受限用途，严禁乐器、托盘、排排站；SH10批准图＝同一工装、凳、低钩、光线和第一次转换连续性；ENV-01白模＝凳与低钩几何位置，仅作空间，不继承风格；`SCALE_LEDGER_V1.md`＝凳、衣钩、衣物使用尺度。FIN-004旧图不得作为动作或构图参考。

[SUBJECT_AND_ACTION] 绵羊的两只蹄爪在长木凳上把一件深蓝旧棉工装外套认真折平：左蹄压住已对齐的一侧，右蹄正把另一侧衣襟翻到中央，衣领和袖子结构完整。背景柔焦层中，兔只完成把另一件工装衣领挂到低钩的不同动作。画面强调“收好一段职业身份”，不做象征性撕裂。

[CAMERA_AND_COMPOSITION] 21:9 85mm感手部／衣物特写，相机略高于凳面约25cm，从凳的长边斜看。折叠工装占中左大形，两只蹄爪分别落在不同画面区域且归属清楚；背景右上保留兔与低钩柔焦侧影，不能像多一双前景手。焦点精确在衣襟折线、羊蹄和木凳接触处；凳面纹理受控，前后景分离自然。

[LIGHTING] 左上高窗灰蓝软光横过深蓝布料，暖灰顶灯给木凳与羊毛一点低强度暖填；折线和蹄爪下接触影柔而明确，背景不过曝。无高光塑料布、无神秘辉光或舞台灯。

[SPACE_AND_CONTINUITY] 同一ENV-01更衣室；凳面与SH10一致，兔仍使用右后低钩，柜列保持深青色块。工装只是被收好，后续将在第二次返回时消失；此时钩／凳仍有工装。SH12由布料和毛色细节继续揭露个体身份。

[SCALE_LOCK] 凳高约0.50m、深约0.55m，工装外套按绵羊1.75m两足体型制作，折后仍占合理凳面范围；衣扣、袖口与蹄爪比例可信。背景兔1.30m只使用低钩，低钩和凳不因景深变成玩具。布料必须平贴凳面、蹄爪有承重和接触影。

[GROUP_ACTION_LOCK] 前景绵羊＝折衣襟并压平；背景兔＝挂另一件衣物到低钩。两种动作、两个深度、不同手位和节奏；无第三角色、无同步折衣、无阿白或猫。

[NEGATIVE] 禁止人手、五指、额外蹄爪、融合肢体、手爪归属不清、衣物自行折叠／悬浮／融化、袖子数量错误、工装破裂燃烧；禁止两人同时折衣、前景复制手、背景变成第二只羊；禁止阿白、猫、华服、乐器、托盘、酒杯、四足化；禁止兔够高钩、凳面缩放错误；禁止照片写实、3D、日漫、过度浅景深、脏布恐怖；禁止文字、logo、水印、随机颗粒、泥状微纹理、锐化光晕、伪细节、JPEG artifacts、noisy background.
```

### AIGC IMAGE-TO-VIDEO PROMPT

```text
[STYLE_FINGERPRINT] 输入帧的21:9旧纸蛋彩衣物特写：深蓝旧棉工装、褪木凳、灰白羊毛、深青柔焦柜列、低频纸纹、朴拙清楚接触边缘和克制冷暖室内光。

[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the exact input artwork, sheep hoof-paws, garment construction, bench, rabbit background silhouette, low-hook location, palette, light, lens and matte paper texture. Animate only one careful fold and one background hanging settle; do not add hands, clothes or characters.

[STYLE_NEGATIVE] Strictly do not change or replace the source art style. No photoreal cloth/fur, CGI hands, game render, anime, glossy fabric, watercolor, oil painting, extra scratches/grain, fake textile detail or sharpening.

[NARRATIVE_TIME] FIRST_WARDROBE_TRANSITION / UNIFORM_STORAGE；工装已离身并被普通地折叠、挂起，私人华服尚未出现。

[CHARACTER_STATE_LOCK] state_id=FIRST_WARDROBE_TRANSITION；前景羊与背景兔保持两足结构，仅处理各自深蓝工装，无阿白、无猫、无演出服。

[STATE_TRANSITION_RULE] 只继续工装收纳，不授权身体转换或私服完成；毛爪与蹄爪不得变成人手，严禁提前四足化。

[DURATION] 3.0s

[DURATION_RATIONALE] 一件衣襟翻折、压平与布料settle需要3秒才能读出克制认真；背景兔只做一个挂衣收尾，不增加新的连续动作。

[TIMELINE]
0.0–0.7s: 表演：85mm相机锁定凳面，只有极轻的呼吸式稳定感但不漂移；羊左蹄压住已折侧，右蹄抬起另一侧衣襟；背景兔衣领刚接触低钩。焦点在衣襟和蹄爪，冷窗暖灯与曝光锁定；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
0.7–1.6s: 表演：右蹄将衣襟沿真实布料折线翻向中央，袖子因重力迟缓跟随；左蹄保持承重不滑。背景兔松开衣领，衣物在低钩上轻摆一次；背景保持柔焦，角色不靠近镜头；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
1.6–2.4s: 表演：右蹄沿折面轻压并向外滑一小段，把工装折平；布料中的空气缓慢排出，折痕settle。背景挂衣摆幅衰减，柜、钩、凳不移动，纸纹不爬；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
2.4–3.0s: 表演：两只羊蹄停在不同位置，工装完整折平；兔背景衣物完全静止。相机、焦点和光线保持，留0.4秒稳定终帧，便于切SH12个体毛色细节；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。

[CONTINUITY_LOCKS] FIRST_WARDROBE_TRANSITION；绵羊／兔均两足且尚未穿华服；深蓝工装结构、凳、低钩、房间光线与SH10一致；无阿白、猫、乐器、托盘、酒杯或四足化。

[NEGATIVE] 无人手或肢体突变、无蹄爪复制、无衣物融化／消失／破裂、无布料穿模、无背景角色换种、无新角色、无相机切镜或突然推拉；无闪烁、纹理爬行、噪点、锐化边或残影。

[AUDIO] 仅拟音：厚棉布与木凳摩擦、衣钩轻响、极弱高窗风和室内回声；无音乐、BGM、对白。《The Masterplan》后期加入。
```

---

## SH12｜毛色、角根与阿白鞍状斑｜00:35–00:38｜3.0s

### IMAGE PROMPT

```text
[NARRATIVE_TIME] FIRST_WARDROBE_TRANSITION / INDIVIDUAL_IDENTITY_REVEAL；工装已被逐件脱下但私人华服尚未穿好，不同个体第一次从统一深蓝中显露。

[CHARACTER_STATE_LOCK] 三层可读身份均保持两足拟人结构：前景年长绵羊＝灰白卷毛、瘦长脸边缘和小而自然弯角的角根，工装已脱、尚未穿旧芥末衬衫；中景老狗＝棕黑粗毛、垂耳体系，其肩侧只露一条普通愈合旧伤／毛流缺口，不见人皮、不血腥，尚未穿氧化绿马甲；后中景唯一阿白＝ABAI_FACTORY_UNIFORM_PHOTOLOCK 的工装脱下进行中，转身时第一次清楚露出照片锁定的“背部至后躯单块连续、边缘自然烟灰至炭灰鞍状斑”和深灰蓬松尾，灰绿眼／粉鼻身份不需正面展示但绝不改变。无第二只猫、无华服完成态、无乐器。

[STATE_TRANSITION_RULE] 只进行第一次服装转换；允许工装离开身体、显露天然毛色和普通旧伤，不允许身体解剖变化。阿白仍是两足照片身份，绝不提前进入ABAI_WILD_RETURN_PHOTOLOCK；演出服从SH13开始完成。

[INTENTIONAL_REALITY_EXCEPTIONS] []。旧伤只是已愈合的毛流缺口／细窄疤痕，非超自然图案；阿白鞍状斑是天然毛色，不是衣服、纹身、裂缝或发光记号。

[STYLE_FINGERPRINT] 21:9 DFT旧纸蛋彩／哑光水粉身份细节镜；灰白卷毛、棕黑粗毛、阿白奶白长毛与烟灰鞍状斑构成三种清晰材质大形，深青柜和折叠工装退为低饱和背景。旧纸低频纤维、朴拙毛缘与细描边、哑光干刷；浅景深中的三层形状仍可辨，细节只落在角根、愈合毛流与天然斑纹，清晰低噪，不产生随机毛发噪点。

[REFERENCE_ROLES] DFT参考＝媒介、毛缘处理、低饱和色与安静气质；三张阿白照片＝阿白天然头顶斑、背部连续鞍状斑、深灰尾的唯一身份真值，不继承照片姿势／环境／光线／写实媒介；批准阿白板＝两足比例与项目风格翻译；`CHARACTER_STATE_LEDGER_V1.md`＝阿白工装阶段；`SUPPORTING_CAST_IDENTITY_LOCK_V2.md`＝羊与老狗身份；旧A/B板仅身份毛色体型受限参考，禁止道具与排排站；SH10／SH11批准图＝房间、工装移除进度和光线连续性。旧黑毛撮／单肋纹阿白及被否决人物设定禁止使用。

[SUBJECT_AND_ACTION] 一个连续空间中的三层身份揭示，而非拼贴板：前景左侧柔焦绵羊角根与灰白卷毛掠过；焦点层的老狗抬臂让肩侧一条细窄已愈合毛流缺口可见；后中景阿白背向三分之二侧面，刚把深蓝工装上衣滑离背部，完整露出从背部延续至后躯的一整块自然烟灰鞍状斑和深灰尾。统一制服退出画面，个体差异安静出现。

[CAMERA_AND_COMPOSITION] 21:9细节中近景，65–85mm感，相机位于柜列一侧约胸高，沿三个角色形成的斜纵深轴取景。前景羊角根占左侧柔焦框边，中景狗肩在右中，后中景阿白背部鞍状斑位于中央偏左且不被衣物遮断；深蓝工装形成下沿对角线。焦点首选阿白斑纹与衣缘接触处，同时保证中景狗毛流可辨；无分屏、无多格设计板、无镜面复制。

[LIGHTING] 高窗灰蓝侧逆光勾出三种毛缘，暖灰顶灯提供低强度正填，使阿白奶白毛与烟灰斑边界真实柔和；深蓝工装较暗但不黑死。愈合旧伤无红光、无湿润质感；阴影和反光方向统一。

[SPACE_AND_CONTINUITY] 同一ENV-01柜列侧面；折叠工装仍在凳与钩上，角色没有换到舞台或私室。阿白斑纹首次完整可见，并在后续演出服领口／下摆处按服装遮挡部分保留；SH13开始穿私人华服。镜面如在画外，不得生成任何角色倒影分身。

[SCALE_LOCK] 65–85mm压缩由实际前后位置解释：羊前景较大、狗中景、阿白后中景，不能让羊角变成巨型建筑物或阿白缩成玩具。毛发、工装衣缘、柜把与角色身体比例一致；阿白鞍状斑贴随真实背部曲面，不漂浮、不跨到柜或另一身体。

[GROUP_ACTION_LOCK] 羊＝前景经过／角根露出；老狗＝抬一臂显露肩侧毛流；阿白＝工装滑离背部并转身。三人三动作、三朝向、三景深；阿白唯一猫，羊／狗各一，不增加其他角色或相同斑纹复制。

[NEGATIVE] 禁止拼贴人设板、三格构图、镜像分身、第二只猫、猫群、重复羊狗；禁止阿白旧竖黑毛撮、琥珀眼、左肋单条黑纹、多块装饰斑、白尾、斑纹漂移到衣服或背景；禁止血、伤口、恐怖疤痕、皮肤撕裂、身体变形、四足化、人手、额外肢体；禁止华服完成、乐器、托盘、酒杯；禁止照片写实、3D、日漫、吉祥物、毛发高频噪点；禁止文字logo水印、随机颗粒、泥状纹理、锐化光晕、伪细节、JPEG artifacts、noisy background.
```

### AIGC IMAGE-TO-VIDEO PROMPT

```text
[STYLE_FINGERPRINT] 输入帧的21:9旧纸蛋彩身份细节：灰白羊毛、棕黑狗毛、阿白奶白长毛与单块烟灰鞍状斑、深青柜／工装、低频纸纹、朴拙毛缘和克制冷暖侧光。

[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the source artwork, three identities, exact Abai photolock markings, one-cat rule, biped anatomy, garment-removal stage, room, depth order, palette and paper medium. Animate only a gentle rack focus and one small identity-reveal movement per character; never alter markings or transform bodies.

[STYLE_NEGATIVE] Strictly do not change or replace the source art style. No photoreal fur, live action, CGI, anime, glossy illustration, watercolor, body horror, graphic wound, extra grain, noisy hair strands, sharpened microtexture or redesign.

[NARRATIVE_TIME] FIRST_WARDROBE_TRANSITION / INDIVIDUAL_IDENTITY_REVEAL；工装脱下进行中，私人华服尚未穿好。

[CHARACTER_STATE_LOCK] state_id=FIRST_WARDROBE_TRANSITION；羊、老狗、唯一阿白均保持两足身份，允许显露天然毛色、普通愈合旧伤与阿白照片锁定鞍状斑／深灰尾。

[STATE_TRANSITION_RULE] 只允许工装离开身体并揭示既有身份特征；不穿完整演出装、不改变解剖、不进入 ABAI_WILD_RETURN_PHOTOLOCK。

[DURATION] 3.0s

[DURATION_RATIONALE] 一个由前到后的连续焦点移动可在3秒内读出角根、旧伤毛流和阿白鞍状斑；人物动作保持最小，避免把细节镜过载成三段蒙太奇。

[TIMELINE]
0.0–0.7s: 表演：65–85mm相机固定；焦点先落前景羊角根与灰白卷毛，羊仅缓慢从左向右经过少许；中景狗抬臂准备，后景阿白衣缘尚遮住鞍状斑一小部分。冷侧逆光和暖填不变，三层比例锁定；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
0.7–1.5s: 表演：焦点平滑移至中景老狗肩侧，狗完成小幅抬臂，细窄愈合毛流缺口清楚但无红色；羊前景继续出画少许，阿白只慢转。相机不平移、不变焦，深青柜与工装静止；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
1.5–2.4s: 表演：焦点继续平滑移到阿白背部；阿白把工装衣缘向下／侧滑一小段，完整单块鞍状灰黑斑和深灰尾显露，仍保持两足。狗动作停住，羊只剩柔焦框边；毛发与布料按重力settle；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
2.4–3.0s: 表演：焦点稳在阿白斑纹与衣缘，所有角色动作减速停止；斑纹形状、颜色和位置绝不改变。留0.35秒稳定终帧，便于切到SH13私服颜色进入；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。

[CONTINUITY_LOCKS] FIRST_WARDROBE_TRANSITION；羊、老狗、阿白各一，阿白唯一猫且照片斑纹／深灰尾锁定；全体两足，工装移除中、尚无华服；三层深度、柜列、光线、镜头轴固定；无四足化或伤口变化。

[NEGATIVE] 无斑纹生长／游移／复制、无旧伤扩大或流血、无物种互换、无新角色、无猫群、无肢体变化、无衣服融入身体、无镜头切换／分屏／镜像；无闪烁、焦点抽动、纹理爬行、噪点、毛发沸腾或残影。

[AUDIO] 仅环境声：近处工装布滑过毛发、极轻呼吸、远处衣钩和高窗风；无对白、音乐、BGM、歌声。《The Masterplan》后期加入。
```

---

## SH13｜私人华服错峰完成｜00:38–00:42｜4.0s

### IMAGE PROMPT

```text
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL / PERFORMANCE_DRESSING_COMPLETION；第一次服装转换进入最后整理阶段，个人颜色第一次充满更衣室；尚未取乐器、尚未出发去广场。

[CHARACTER_STATE_LOCK] 八位角色全部保持两足拟人结构，绑定 PERFORMANCE_BIPED_PRIVATE_DRESS 的“最终整理”相位。阿白＝ABAI_PERFORMANCE_DRESS_PHOTOLOCK且唯一猫：奶白长毛、灰绿眼、粉鼻、天然非对称头顶灰黑斑、背部单块鞍状斑与深灰尾，穿略宽奶白衬衫和旧赭红背心，深青短外套在身上但前襟敞开，正在扣背心；羊＝旧芥末衬衫＋深青披肩；大象＝褪色砖红礼服外套；驴＝奶白衬衫＋旧赭背带裤；老狗＝氧化绿马甲＋旧红围巾；狐狸＝深青短外套＋旧金围巾；兔＝奶白衬衫＋旧红裙裤；熊＝旧芥末衬衫＋孔雀蓝背心。所有工装已离身但仍在凳／钩上；无人持乐器、托盘、酒杯。

[STATE_TRANSITION_RULE] 本镜授权完成 FACTORY_BIPED_UNIFORM → PERFORMANCE_BIPED_PRIVATE_DRESS 的服装转换；图像关键帧取私人华服已穿在身上、仅剩最后一个整理动作的时刻，镜尾状态完全进入PERFORMANCE_BIPED_PRIVATE_DRESS。身体不变化；WILD_RETURN_QUADRUPED仍只允许SH35。

[INTENTIONAL_REALITY_EXCEPTIONS] []。略不合身华服是有意叙事设计，但衣物结构完整、可穿、承重和扣合可信；大象礼服偏小不能勒入身体或破裂。

[STYLE_FINGERPRINT] 21:9 DFT旧纸蛋彩／哑光水粉群像；在灰蓝深青更衣室中，旧赭红、旧芥末、孔雀蓝、氧化绿、奶白和旧金第一次出现，全部褪色低饱和、不是糖果色。旧纸低频肌理、朴拙清晰描边、哑光衣料和大块可读剪影；横向平面构图以八种不同手位和高低姿态组织，个体认真克制、不搞怪，背景低噪。

[REFERENCE_ROLES] DFT参考＝媒介、褪色调色、边缘、空间与安静荒诞；阿白照片＋批准板＝阿白身份、两足演出装和斑纹；`SUPPORTING_CAST_IDENTITY_LOCK_V2.md`＝七配角脸型、物种、体型与每套演出服唯一权威；旧A/B图若加载仅限身份／服装视觉参考，严禁继承乐器并排、熊托盘酒杯、排排站或缺失第三状态；SH12批准图＝脱工装进度、毛色和房间连续性；ENV-01白模＝空间几何，仅作blocking；`SCALE_LEDGER_V1.md`＝房间与衣物尺度；`GROUP_ACTION_LEDGER_120S_V2.md#SH13`＝动作分工。FIN-005及旧配角板的雷同胸前系扣构图仅作失败证据，不得继承。

[SUBJECT_AND_ACTION] 平视中宽群像，八位角色各自完成不同的最后整理：阿白位于中左，只扣旧赭红背心靠下的一枚扣，深青短外套已披在身上但敞开；羊在领口侧别好深青披肩的小固定饰；大象把褪色砖红长外衣从一侧肩慢慢披上，另一侧尚未就位；驴坐在凳端只系一侧鞋带；老狗卷起一只奶白衬衫袖口，氧化绿马甲已穿好；狐狸面对镜边用一爪整理旧金围巾，另一爪垂下；兔在腰侧扣旧红裙裤；熊刚从凳上站起，拉正孔雀蓝背心下缘／背部调节带。无人持乐器，动作不复制。

[CAMERA_AND_COMPOSITION] 21:9平视中宽群像，35–40mm感，相机约1.35m高，沿长凳长边斜看柜列，轴线相较SH10降到人物胸腹高度。阿白位于中左但不居中；大象在左后并露完整门／顶高关系；驴与熊分别在凳两端形成坐／起对比；兔低位、羊中位、狗中右、狐狸镜边。前景可有一角折好工装，中景人物，背景柜钩；中深景深让八个手位和服装读得清，镜面不复制狐狸或其他角色。

[LIGHTING] 高窗灰蓝侧光继续统一空间，暖灰顶灯略提升一档，让赭红、芥末、孔雀蓝、氧化绿和奶白显现但仍褪色；阿白灰绿眼和天然头顶斑可读。衣料哑光、阴影柔软、地面投影一致；无舞台灯、魔法换装光、闪亮亮片或糖果高饱和。

[SPACE_AND_CONTINUITY] 同一ENV-01门、柜、三层钩、凳、通道；深蓝工装已折／挂在对应位置，不穿在任何人身上。私人衣服结构与SUPPORTING_CAST_IDENTITY_LOCK_V2一致；SH14才由阿白独自打开琴盒，本镜和同一前景不出现任何乐器。SH15角色从出口错峰离开，服装完成态需与本镜尾帧一致。

[SCALE_LOCK] 更衣室净高≥4.5m、主门≥3.3×2.8m、柜2.2–2.4m、凳0.50m；大象2.55m在室内有净空，兔1.30m在低位操作腰侧，驴／熊坐凳或起身脚地可信。服装按角色体型定制：大象外套偏小但肩宽和袖长仍能穿，兔裙裤不巨大，阿白小扣可由毛爪操作；工装折叠物不改变凳尺度。

[GROUP_ACTION_LOCK] 阿白＝扣背心下扣；羊＝别披肩固定饰；象＝披一侧长衣；驴＝系一侧鞋带；狗＝卷一只袖；狐狸＝镜边整理围巾；兔＝扣腰侧；熊＝站起拉正背心调节带。八种动词／手位／身体高度／朝向，阿白唯一猫，配角各一；任何人不得提前拿乐器，熊不得出现托盘酒杯。

[NEGATIVE] 禁止全员系领口／胸前扣子、同手位、同姿站立、排排站、复制动作、镜中分身；禁止第二只猫、群猫、重复主角色；禁止阿白旧黑毛撮／琥珀眼／单肋纹／白尾或工装混穿；禁止乐器、托盘、酒杯、熊端盘、旧A板乐器陈列；禁止人手、裸露人皮、额外肢体、四足化、衣物穿模或大象外套破裂；禁止门柜凳尺度错乱；禁止糖果色、舞台魔法、照片写实、3D、日漫、吉祥物；禁止文字logo水印、随机颗粒、泥状纹理、锐化光晕、伪细节、JPEG artifacts、noisy background.
```

### AIGC IMAGE-TO-VIDEO PROMPT

```text
[STYLE_FINGERPRINT] 输入帧的21:9 DFT旧纸蛋彩更衣群像：灰蓝深青空间中的褪赭红、旧芥末、孔雀蓝、氧化绿、奶白与旧金华服，低频纸纹、朴拙轮廓、哑光衣料、八种错峰手位和清晰低噪层次。

[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the exact source art style, all eight identities, one-cat rule, photolocked Abai markings, every assigned private outfit, room geometry, relative scale, lighting, camera axis and action allocation. Animate only each character's one final dressing adjustment; do not introduce instruments, trays, cups, uniforms on bodies or quadruped transformation.

[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal cloth/fur, live action, plastic CGI, game render, anime, cel shading, glossy fashion illustration, watercolor, magical transformation glow, body horror, added grain, muddy texture or redesign.

[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL / PERFORMANCE_DRESSING_COMPLETION；第一次换装的最终整理，尚未取乐器或离开更衣室。

[CHARACTER_STATE_LOCK] state_id=PERFORMANCE_BIPED_PRIVATE_DRESS；阿白唯一猫与七位配角均保持两足私人华服完成态，各自只做规定的最后整理动作。

[STATE_TRANSITION_RULE] 本镜完成 FACTORY_BIPED_UNIFORM → PERFORMANCE_BIPED_PRIVATE_DRESS 的服装转换并锁定尾帧；身体不变化，WILD_RETURN_QUADRUPED 禁止提前。

[DURATION] 4.0s

[DURATION_RATIONALE] 八位角色各自完成一个最终服装整理动作，并在镜尾形成稳定华服状态；4秒可读清个体差异，但不承担取乐器或离场，动作负荷仍为每人一个微动作。

[TIMELINE]
0.0–1.0s: 表演：平视35–40mm相机沿凳长边极慢向右短滑；阿白毛爪对准背心下扣，羊触披肩固定处，象一侧肩接外套，驴手爪到鞋带，狗抓单袖，狐看镜边、兔触腰扣、熊开始起身。焦点覆盖阿白与中景群像，冷窗暖灯、服装色和房间尺度锁定；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
1.0–2.2s: 表演：八人推进唯一动作：阿白扣上一枚下扣；羊固定披肩；象把一侧外套提过肩但不做第二侧；驴收紧一个鞋带结；狗卷一次单袖；狐拉直围巾一端；兔扣好腰侧；熊从凳上站起并拉正背心调节带。速度按体型与性格错开，不同时在胸前做同动作；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
2.2–3.2s: 表演：各动作进入收尾：阿白毛爪放低、短外套前襟仍自然敞开；羊检查领饰；象外套一侧落稳；驴脚着地；狗单袖停在前臂；狐围巾settle；兔腰侧平整；熊站稳。相机滑动减速，镜面只保留色块反射不生成分身；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。
3.2–4.0s: 表演：相机完全停住，八位角色保持完成的PERFORMANCE_BIPED_PRIVATE_DRESS，各有不同呼吸、眼线和姿态，衣料与耳尾缓慢settle；无人去拿乐器。留0.4秒稳定终帧供SH14切入阿白琴盒；摄影：相机机位、焦段、运动、构图、焦点、曝光与光线均按本区间前述指令执行，未明示变化保持锁定。

[CONTINUITY_LOCKS] 镜尾全体＝PERFORMANCE_BIPED_PRIVATE_DRESS，两足；阿白＝ABAI_PERFORMANCE_DRESS_PHOTOLOCK且唯一猫；七配角私服与体型固定；八个动作不互换；工装只留凳／钩不穿身；ENV-01空间、门柜凳尺度和冷窗暖灯不变；无乐器托盘酒杯或四足化。

[NEGATIVE] 无动作克隆、同胸前手位、角色复制、猫群、服装换色／互换／跳变、阿白斑纹漂移、熊托盘、乐器凭空出现、人手或肢体变形、四足化、衣物穿模；无镜中分身、相机切轴、突然推拉、空间重排、灯光闪烁、纹理爬行、噪点或残影。

[AUDIO] 仅环境声：不同材质衣料摩擦、一个小扣合声、鞋带收紧、木凳轻响、衣钩与高窗风；无对白、音乐、BGM、歌声。《The Masterplan》仅后期剪辑配乐。
```

---

## 包内自查记录

- 镜头时长：`SH01 4 + SH02 3 + SH03 3 + SH04 3 + SH05 3 + SH06 3 + SH07 2 + SH08 3 + SH09 4 + SH10 4 + SH11 3 + SH12 3 + SH13 4 = 42.0s`，与 `00:00–00:42` 完全一致。
- 视频时间线：13镜均从`0.0s`开始并精确结束于各自声明时长；相邻区间无缺口、无重叠；52条时间区间均显式包含`表演：`与`摄影：`，每镜都有减速／settle和可剪终帧。
- 表结构：13个IMAGE PROMPT均含`NARRATIVE_TIME / CHARACTER_STATE_LOCK / STATE_TRANSITION_RULE / INTENTIONAL_REALITY_EXCEPTIONS / STYLE_FINGERPRINT / REFERENCE_ROLES / SUBJECT_AND_ACTION / CAMERA_AND_COMPOSITION / LIGHTING / SPACE_AND_CONTINUITY / SCALE_LOCK / GROUP_ACTION_LOCK / NEGATIVE`；13个视频提示均以动态`STYLE_FINGERPRINT / STYLE_INHERITANCE_HARD_LOCK / STYLE_NEGATIVE`开头，并含`DURATION / DURATION_RATIONALE / TIMELINE / CONTINUITY_LOCKS / NEGATIVE / AUDIO`。
- 参考链：配角身份以`SUPPORTING_CAST_IDENTITY_LOCK_V2.md`为活动权威；旧A/B板仅按V2声明作受限身份服装参考；ENV-01白模只作空间blocking；FIN-004/005与其他否决图只作为失败证据，不继承动作／构图／风格／身份。
- 状态：SH01–SH09保持`FACTORY_BIPED_UNIFORM`；SH10–SH12是第一次服装转换进行中且身体始终两足；SH13镜尾完成`PERFORMANCE_BIPED_PRIVATE_DRESS`。任何镜头都不得提前出现`WILD_RETURN_QUADRUPED`。
- 群像：所有可读群像均执行唯一阿白、活动主角色各最多一个、至少五种物种（适用时）与逐角色错峰动作；SH10／SH13明确禁止复用旧版雷同脱衣／穿衣姿势。
- 尺度与清晰度：全部镜头绑定`SCALE_LEDGER_V1.md`，`intentional_scale_exceptions: []`；全部图像提示含21:9、DFT旧纸蛋彩、可读大形、受控细节与低噪负面约束。
