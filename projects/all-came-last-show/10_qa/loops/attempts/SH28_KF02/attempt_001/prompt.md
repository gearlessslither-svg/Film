# 《所有人都来了》SH27–SH38 生产提示词包 V2

状态：`production_prompt_ready / generation_requires_active_plan_approval`

活动分支：`DFT_MASTERPLAN_WILD_RETURN_V4`  
成片规格：全部 `21:9`，建议原生输出 `1915×821 PNG` 或更高同画幅无损图；DFT 旧纸蛋彩／哑光水粉；清晰、低噪。  
音乐规则：本包不把音乐写入任何生成提示。Oasis《The Masterplan》仅在后期剪辑使用；生成视频只含环境声与动作音效。

## 权威与引用边界

- `04_lookdev/references/DFT_DIRECTOR_REFERENCE.png`：只作 `STYLE_ONLY`，锁旧纸蛋彩／哑光水粉、朴拙手工边缘、褪色深青赭金、寓言式平面空间与安静荒诞；禁止继承其中人物、船、鸟、月亮、道具和事件。
- `05_asset_bible/approved/ABAI_DUAL_STATE_SHEET_V2_APPROVED.png`：只作阿白两足身份、比例和服装翻译；三张 `references/abai_photo_lock/*.JPG` 作阿白脸、天然斑纹、尾巴与四足结构硬锁，不继承照片媒介、姿势、家具或光线。
- `08_generation/jobs/supporting_cast_v1/outputs/SUPPORTING_CAST_A_V1_attempt_001.png` 与 `.../SUPPORTING_CAST_B_V1_attempt_001.png`：依 `SUPPORTING_CAST_IDENTITY_LOCK_V2.md`，只提取配角脸型、物种、毛色、体型、两足比例、工装版式与演出服装；禁止继承乐器陈列、托盘、排排站构图或缺失的第三状态。
- `ENV-01_WHITEBOX_3VIEWS_attempt_002.png`、`ENV-02_WHITEBOX_3VIEWS_attempt_003.png`：只作 `SPACE/CAMERA/BLOCKING_ONLY`；不得覆盖 DFT 风格、角色身份、衣着或照明。
- `FIN-010.png` 仅可给 SH33 作 `STORY_CONTENT_CANDIDATE`；`FIN-012B.png` 仅可给 SH38-KF01 作 `STORY/COMPOSITION_CANDIDATE`。其余 V1 锚点、被否决场景图和旧设定全部排除在活动风格与身份链之外。
- 文本硬锁：`CHARACTER_STATE_LEDGER_V1.md`、`TRANSFORMATION_STATE_LEDGER_V1.md`、`SUPPORTING_CAST_IDENTITY_LOCK_V2.md`、`SCALE_LEDGER_V1.md`、`GROUP_ACTION_LEDGER_120S_V2.md`。

## 镜头合同总览

| 镜头 | 成片时间 | 准确时长 | 图像锚点 | 连续镜头要求 |
|---|---:|---:|---:|---|
| SH27 | 01:24–01:28 | 4.0s | 1 | 单一反打，演出减速 |
| SH28 | 01:28–01:31 | 3.0s | 2 | KF01→KF02，同一长焦镜头，无切镜 |
| SH29 | 01:31–01:34 | 3.0s | 1 | 群体错峰反应 |
| SH30 | 01:34–01:36 | 2.0s | 1 | 余波物件插镜 |
| SH31 | 01:36–01:39 | 3.0s | 1 | 空街返回 |
| SH32 | 01:39–01:42 | 3.0s | 1 | 门内反打、不同进门相位 |
| SH33 | 01:42–01:44 | 2.0s | 1 | 空钩主揭示 |
| SH34 | 01:44–01:47 | 3.0s | 1 | 最后脱华服，仍为两足 |
| SH35 | 01:47–01:52 | 5.0s | 3 | KF01→KF02→KF03，一镜三锚点，无切镜 |
| SH36 | 01:52–01:55 | 3.0s | 1 | 四足离开更衣室 |
| SH37 | 01:55–01:57 | 2.0s | 1 | 镇外俯瞰分路 |
| SH38 | 01:57–02:00 | 3.0s | 2 | KF01→KF02，回望后跑向晨光，无切镜 |

---

## SH27｜演出反打，阿白先听见异动

### IMAGE PROMPT — SH27

```text
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:24，最后演出仍在继续、烟囱异动尚未显形；没有回忆、梦境或并置时间层。
[CHARACTER_STATE_LOCK] 阿白=ABAI_PERFORMANCE_DRESS_PHOTOLOCK：唯一猫，年轻乳白长毛，灰绿色眼、粉鼻、非对称灰黑头顶天然毛斑、背部至后躯单块鞍状灰黑斑、深灰蓬松尾，奶白衬衫+旧赭红背心+深青短外套，持结构完整且尺寸合适的旧木小提琴与琴弓；绵羊=灰白卷毛瘦脸小弯角、旧芥末衬衫+深青披肩；大象=灰蓝皮肤、两枚短牙、最大体格、褪色砖红礼服外套；狗=棕黑粗毛垂耳宽肩、氧化绿马甲+旧红围巾；狐狸=褪色赤褐毛白下颌蓬松尾、深青短外套+旧金围巾；兔=灰米短毛、一耳略弯、奶白衬衫+旧红裙裤；熊=深棕厚毛宽体、旧芥末衬衫+孔雀蓝背心。所有角色仍是两足拟人动物，物种头、毛爪/蹄、尾巴与简化直立身体；一物种一实例。
[STATE_TRANSITION_RULE] 本镜头禁止换装、脱衣或身体转化；从第一帧到最后一帧保持 PERFORMANCE_BIPED_PRIVATE_DRESS。阿白只允许琴弓减速、耳朵转向，不得提前四足。
[INTENTIONAL_REALITY_EXCEPTIONS] 仅批准“动物以简化两足拟人结构穿衣并用毛爪/蹄完成表演”这一项目规则；普通重力、接触、建筑尺度和乐器结构全部真实。无巨物、微缩、漂浮或复制角色例外。
[STYLE_FINGERPRINT] DFT 温柔荒诞工业挽歌：旧纸底上的蛋彩与哑光水粉，细密却朴拙的手工描线，轮廓略有人工抖动但干净，颜料覆盖不透明、触感柔和；褪色深青、灰蓝、赭金、旧红、孔雀蓝、奶白，整体比导演参考亮约一档；低饱和、中低反差，稳定的赭金实景灯与冷灰蓝环境光；寓言式平面空间但门窗、台阶、桌面和人物前后关系仍具可信透视；大形清楚、细节集中于阿白毛斑、小提琴木面和礼服布料；清晰低噪，无满屏微纹理。
[REFERENCE_ROLES] DFT_DIRECTOR_REFERENCE=STYLE_ONLY；ABAI_DUAL_STATE_SHEET_V2_APPROVED+三张阿白照片=ABAI_IDENTITY/COSTUME/FUR_PATTERN_ONLY；SUPPORTING_CAST_A/B 旧板=IDENTITY_AND_WARDROBE_ONLY，受 SUPPORTING_CAST_IDENTITY_LOCK_V2 限制；ENV-02_WHITEBOX_3VIEWS_attempt_003=SPACE/CAMERA/BLOCKING_ONLY；SCALE_LEDGER+GROUP_ACTION_LEDGER=TEXT_HARD_LOCK。FIN-007 与其他被退回锚点不得作为风格、身份、角色数量或动作参考。
[SUBJECT_AND_ACTION] 广场/礼堂一体空间的反打大全景：阿白位于左中景独立表演点，琴弓还在弦上但速度已变慢，右耳先转向画外工厂方向，视线仍克制；远处另一层只有兔的手风琴作为第二节拍点，不能与小提琴并排；羊侧身听见变化后刚转头；大象在长桌旁仅用肩与象鼻缓慢摆动；狗沿右侧走向画外；熊坐着举杯但未喝；狐狸刚结束旋转，重心落在一侧、双爪分开。每人动作动词、相位、朝向、眼线和手位不同，阿白不是领袖，画面至少七种清楚物种轮廓。
[CAMERA_AND_COMPOSITION] 21:9，35mm 感，稳定平视偏低的大全景反打，摄影机约 1.35m 高，从舞池外沿朝礼堂与分散表演点看；阿白位于左侧三分之一，右侧留给长桌与礼堂主门，前景用一小段空舞池和摇动灯串作框景，中景分置阿白/狐狸/熊，后景分置兔/羊/大象/狗；地平线略低于画面中线，横向运动方向可从右向左剪入 SH28；不使用中央排排站、对称合照或多人正对镜头。焦点在阿白耳朵、琴弓与邻近人物反应，后景仍可辨物种。
[LIGHTING] 赭金旧灯串与礼堂内钨丝灯从右上/后方作柔暖主光，灰蓝夜色从左侧作低强度填光，人物边缘有薄薄旧金轮廓光；阿白白毛不过曝，炭灰斑保留层次；灯串末端有极轻微亮度不稳但本图不表现坍塌。阴影哑光、边缘柔，金属与酒杯无现代高光。
[SPACE_AND_CONTINUITY] 礼堂檐口、主门、舞台、舞池和长桌沿用 ENV-02 白模轴线；表演点互相分开，阿白的小提琴与远处兔手风琴不在同一前景；通往工厂的方向在画外右后方，为 SH28 视线动机；阿白的位置、琴弓方向和灯串端点应可接 SH29。背景不得凭空增加舞台、烟囱或第二礼堂。
[SCALE_LOCK] 礼堂檐口约 7–9m、室内净高约 5.5–7m、主门净高≥3.4m/净宽≥3.0m，舞台高约 0.65m；同平面 2.55m 两足大象明显低于门楣与檐口；桌面、杯、琴和台阶按使用者真实可用比例；前后景人物只按透视缩小，建筑不得像动物玩具屋。
[GROUP_ACTION_LOCK] 阿白=拉琴减速/左中景/耳向画外；兔=远处演奏手风琴/后景；羊=听后转头/中后景；象=桌旁慢摆/右中景；狗=向画外行走/右后景；熊=坐姿举杯不喝/中景；狐=结束旋转并侧停/前中景。不得有两位主要角色共享“端杯+正面站立”或“演奏+同手位”；不得复制阿白、狐狸、大象或任何主角色。
[NEGATIVE] no photorealism, no plastic 3D, no generic anime, no Disney mascot cuteness, no glossy game render, no watercolor wash replacing matte tempera/gouache, no dark-horror fairy tale, no red eyes, fangs, screams, apocalypse, magical glow or smoke; no second cat, second fox, second elephant, duplicate silhouettes or species replaced by recolored cats; no human hands, naked human skin, extra/missing/fused limbs, impossible grip, floating feet, broken violin, missing strings, dense instrument display, repeated cup-holding, cloned dance poses, line-up composition, tiny hall, animal-sized house, incorrect door clearance, pseudo-text, logo, watermark; no film grain, random speckle, muddy micro-texture, sharpening halos, fake pixel detail, JPEG artifacts or noisy background.
```

### AIGC IMAGE-TO-VIDEO PROMPT — SH27

```text
[STYLE_FINGERPRINT] 严格继承 SH27 输入关键帧的 DFT 旧纸蛋彩/哑光水粉：朴拙细线、柔哑不透明颜料、受控旧纸触感、褪色深青赭金与一档提亮的低饱和照明、寓言式压平空间与可信建筑尺度、简化两足物种比例、清晰低噪大形。
[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the input image's exact art style and the style fingerprint above in every frame. Treat SH27 as the immutable first frame and visual bible. Animate this same artwork; do not reinterpret, redraw, beautify, simplify or replace its art direction. Preserve medium, hand-drawn edges, paper/paint texture, palette, contrast, lighting logic, every identity/costume/prop, environment geometry, depth treatment and composition density. Only the specified micro-performance, lamp motion and camera motion may change.
[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No model-default redraw; no migration to photoreal, 3D/CGI, commercial anime, Disney mascot, glossy game art, watercolor, oil paint or horror illustration; no added grain, texture crawl, edge shimmer, palette pumping or detail invention.
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:24–01:28；烟囱事件前，演出两足层。
[CHARACTER_STATE_LOCK] 阿白=ABAI_PERFORMANCE_DRESS_PHOTOLOCK；全体可读居民=PERFORMANCE_BIPED_PRIVATE_DRESS；服装、物种身份、小提琴与各自动作相位从输入帧到终帧不变。
[STATE_TRANSITION_RULE] 本视频不授权角色状态转换；只允许阿白耳朵转向与琴弓减速，所有角色全程保持两足演出态。
[DURATION] 4.0s
[DURATION_RATIONALE] 一个可读的“演出仍在继续→阿白先察觉→琴弓减速”的表演变化，加一次极慢推近和结尾剪辑停顿需要 4 秒；动作克制且同一轴线，不应拆镜。
[TIMELINE]
0.0–0.8s: 表演：维持输入大全景。阿白继续完成一次短弓，耳朵尚朝前；狐狸旋转余势正在收住，象鼻与肩缓慢摆动，熊杯停在胸口、狗继续右行。摄影机 35mm、1.35m 高、固定轴线开始极慢前推；焦点锁阿白与琴弓，暖灯/冷填光和曝光保持。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
0.8–1.8s: 表演：阿白右耳先向画外工厂方向转约一个小角度，眼睛不夸张睁大，琴弓速度下降；羊在后景晚半拍转头，其他人仍按各自动作继续。摄影机仅推进约画幅深度的 2–3%，无摇移无变焦；灯串轻微摆，衣料和毛发只有自然惯性。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
1.8–3.0s: 表演：阿白完成当前弓段后让弓毛仍贴弦、手臂减速至近乎停住；狐狸完全落稳，狗走到画面右缘但不消失，大象减小摆幅，熊尚未喝。焦点仍锁阿白，后景物种不糊成同类；礼堂几何、尺度、角色位置与屏幕方向全部保持。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
3.0–4.0s: 表演：阿白耳朵保持指向画外，琴弓悬停，胸口一次克制呼吸；灯串末端出现极细微颤动，其他表演动作自然减速但不齐停。摄影机平滑减速并在 3.6s 后定住，结尾保留 0.4s 可剪辑稳定帧；阴影、纸纹和曝光不变化。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
[CONTINUITY_LOCKS] 唯一阿白与其照片斑纹、演出服和完整小提琴；配角物种/毛色/服装与一物种一实例；每人动作分工；ENV-02 礼堂/舞台/舞池/长桌轴线；阿白左中景、工厂视线朝右后画外；21:9、35mm、真实比例、无切镜。
[NEGATIVE] no cut, whip pan, zoom jump, camera roll, reframing reset, crowd teleport, duplicated character, species morph, second cat, synchronized freeze, exaggerated surprise, mouth speech, lip sync, human fingers, extra limbs, costume swap, broken violin, added instruments, cup multiplication, tiny architecture, scale pumping, flicker, jitter, frame warping, texture crawl, style drift, text, logo or watermark.
[AUDIO] 仅环境声/音效：远处含混的舞步、杯底轻碰木桌、琴弓摩弦尾音、旧灯串细响和极远处低频结构震动；不生成人声歌词，不嵌入音乐/BGM/配乐。《The Masterplan》由后期剪辑另行铺设。
```

---

## SH28｜烟囱受控倒下（一个连续镜头，两锚点）

### IMAGE PROMPT — SH28_KF01（编号 01／起始锚点）

```text
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:28，烟囱倒塌发生前的最后完整状态；这是 SH28 连续镜头的 01 号锚点。
[CHARACTER_STATE_LOCK] 画面不出现可辨识角色正脸；若广场最远层有极小人物点，只能是 PERFORMANCE_BIPED_PRIVATE_DRESS 的多物种剪影且不可读作第二个主角色。阿白与配角身份不得被烟尘或远景模型重画。
[STATE_TRANSITION_RULE] 本镜头只允许工厂烟囱从完整直立进入受控倾斜；任何动物都禁止身体状态转换。KF01 必须是完整、竖直、无裂成两段的烟囱。
[INTENTIONAL_REALITY_EXCEPTIONS] 无。烟囱倾倒服从普通重力、真实铰转与安全距离；DFT 空间压平不是微缩建筑许可。
[STYLE_FINGERPRINT] DFT 旧纸蛋彩/哑光水粉，细而朴拙的手绘边缘，低饱和灰蓝夜色、氧化绿、褪色砖红与旧赭金灯点，整体亮于参考约一档；平面化长焦层叠但建筑体量、遮挡和景深缩小可信；清洁大形、受控纸面触感、低噪，不用颗粒冒充煤尘。
[REFERENCE_ROLES] DFT_DIRECTOR_REFERENCE=STYLE_ONLY；ENV-02_WHITEBOX_3VIEWS_attempt_003=广场至工厂视线轴/SPACE_ONLY；SCALE_LEDGER=烟囱与两层建筑尺寸硬锁。FIN-009 和被退回场景仅作失败证据，不输入风格、身份、烟囱形态或粉尘。
[SUBJECT_AND_ACTION] 远处工厂烟囱完整竖立在小镇建筑之后，高而细、结构连续，烟囱完全无烟；前景一段礼堂灯串出现几乎不可察的横向微颤，中景屋顶与街灯安静，烟囱根部暂时无明显尘云。画面建立即将失稳前的克制静止。
[CAMERA_AND_COMPOSITION] 21:9，100–135mm 长焦感，稳定极远景，摄影机位于广场边缘约 1.6m 高、朝工厂方向；烟囱位于右侧三分之一，灯串斜穿左上前景，红砖屋顶形成中景水平层，左侧留出烟囱将要倾倒的安全负空间；同一固定轴线贯穿 KF01→KF02，无切镜、无换焦段、无重置构图。焦点在烟囱与根部，中前景略软但形体清楚。
[LIGHTING] 冷灰蓝暮色作整体柔填光，工厂背后有微弱桃橘天光勾边；前景旧金灯泡不过曝，烟囱受侧逆光呈清楚暗色轮廓；无闪电、火光、爆炸或超自然照明。
[SPACE_AND_CONTINUITY] 烟囱在工厂用地内，距广场和礼堂有明确街区/屋顶层隔离，倾倒方向为画面左侧空置工业带而非人群；灯串、屋脊、路灯和烟囱根部位置必须与 KF02 像素级连续；镇貌仍是衰败但可用的工业小城，不是末日废墟。
[SCALE_LOCK] 烟囱约 45–60m，远高于 6.5–8m 两层住宅与 5–6m 路灯；两层住宅窗门保持正常楼层节奏；任何远处动物点都必须远小于房屋，不得为可读性放大；烟囱直径、长度与根部支撑呈真实工业比例。
[GROUP_ACTION_LOCK] 无可读群像动作；禁止新增复制人群。若保留极远处静影，只允许稀疏、多物种、各自不同朝向的微小剪影，全部小于门窗高度。
[NEGATIVE] no smoke from chimney, no flame, explosion, lightning, apocalypse, collapsed town, cracked-everywhere ruins, supernatural glow, tiny chimney, short toy tower, animal-sized houses, giant distant animals, duplicate elephant/fox/cat, crowd close-up, photoreal, 3D, anime, mascot, glossy render, horror, pseudo-text, watermark; no random dust, film grain, speckle, muddy micro-texture, sharpening halo, fake detail or JPEG artifacts.
```

### IMAGE PROMPT — SH28_KF02（编号 02／终止锚点）

```text
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:31，SH28 同一镜头末端；烟囱已从 KF01 连续受控倾斜但尚未完全着地。
[CHARACTER_STATE_LOCK] 画面无可辨识角色正脸；任何极远人影仍为 PERFORMANCE_BIPED_PRIVATE_DRESS 的小尺度多物种剪影，不发生身份、服装或物种变化。
[STATE_TRANSITION_RULE] 只允许烟囱由 KF01 的竖直完整状态绕根部向画面左侧安全工业空地倾斜至约 25–35°离开竖直；烟囱保持一体、不炸裂。动物状态不变。
[INTENTIONAL_REALITY_EXCEPTIONS] 无。倾倒必须服从真实重力、惯性、根部扬尘和安全距离；不允许魔法或规模失真。
[STYLE_FINGERPRINT] 与 SH28_KF01 完全相同的 DFT 旧纸蛋彩/哑光水粉：旧纸、柔哑不透明颜料、朴拙干净手绘边缘、褪色深青灰蓝/砖红/赭金、平面长焦层叠与可信透视尺度；清晰低噪，粉尘是一块受控半透明大形而非随机颗粒。
[REFERENCE_ROLES] SH28_KF01=最高优先级同镜头起始构图/几何/光色/材质；DFT_DIRECTOR_REFERENCE=STYLE_ONLY；ENV-02_WHITEBOX_3VIEWS_attempt_003=SPACE_AXIS_ONLY；SCALE_LEDGER=烟囱、住宅和路灯尺寸。FIN-009 不作为活动风格或结构参考。
[SUBJECT_AND_ACTION] 同一根烟囱整体向画面左侧空置工业带受控倾斜，长度、直径和砖/混凝土节段连续；只有根部出现一团低矮、浓度克制的土黄扬尘，尘云不吞没建筑、不扩散到广场；前景同一灯串摆幅略增，中景屋顶保持完整，无火焰、爆炸、碎片雨或末日破坏。
[CAMERA_AND_COMPOSITION] 严格复刻 KF01 的 21:9、100–135mm、1.6m 高、固定摄影机、右三分之一根部和左侧安全负空间；烟囱顶端沿可预测圆弧进入左侧负空间，根部像素位置不漂移；无摇摄、无推拉、无镜头切换。焦点仍在烟囱和根部，前景灯串软焦程度不变。
[LIGHTING] 完全继承 KF01 冷灰蓝暮色、微弱桃橘天缘与旧金灯泡；倾斜只改变烟囱自身受光面和投影方向，曝光不泵动，尘云受根部侧光呈柔哑土黄。
[SPACE_AND_CONTINUITY] 所有屋脊、路灯、灯串、工厂根部和广场方向与 KF01 连续；烟囱倒向预留空工业带，绝不跨越礼堂、街道或人物；城镇主体保持结构完整。
[SCALE_LOCK] 烟囱仍是 45–60m 的同一根长构筑物，倾斜后投影长度与角度一致；远高于两层屋顶，根部直径不缩小；远处人物不大于门窗，路灯始终约 5–6m 参照；禁止透视变形导致烟囱忽长忽短。
[GROUP_ACTION_LOCK] 无可读群像；不新增大象、狐狸、猫或复制人群。极远影点只可维持 KF01 数量和位置，动作不需要同步放大。
[NEGATIVE] no broken-in-half chimney, no bending rubber tower, no explosion, flame, smoke plume, debris rain, building collapse, crowd impact, apocalypse, giant dust wall, scale change, camera reset, different skyline, duplicate animals, photoreal, 3D, anime, horror, glossy render, text/logo/watermark; no noisy particle field, grain, random speckle, muddy texture, sharpening halos, fake microdetail or JPEG artifacts.
```

### SH28 多锚点连续性合同

```text
[SHOT_ID] SH28
[SHOT_INTENT] 用一个固定长焦极远景把“完整直立的烟囱”连续过渡到“向安全空地受控倾斜”，让演出与拆除第一次真正碰在一起；不切镜、不爆炸。
[KEYFRAME_SEQUENCE]
01 | 0.0s | SH28_KF01 | 烟囱完整竖直；灯串微颤；根部无尘；固定 100–135mm 轴线。
02 | 3.0s | SH28_KF02 | 同一烟囱整体左倾约 25–35°；根部低尘；同一建筑/灯串/曝光/轴线。
[TRANSITIONS]
01 -> 02 | 0.0–3.0s 内烟囱围绕固定根部作连续重力圆弧，先静止、再缓慢失稳、后加速但未着地；灯串由微颤到小幅摆动；尘只在根部后半段出现。不得插入切镜、重绘天际线、改变焦段、让烟囱断裂或把人物放大。
[STORYBOARD_SHEET] 生成并分别 QA 两锚点后，用原图无再生成地合成 `08_generation/jobs/final_frames_v2/storyboard_sheets/SH28_NUMBERED_SHEET.png`，左至右标清 01、02；此表只作顺序审查，不替代源帧。
```

### AIGC IMAGE-TO-VIDEO PROMPT — SH28

```text
[STYLE_FINGERPRINT] 严格继承 SH28_KF01/KF02 的同一 DFT 旧纸蛋彩与哑光水粉：朴拙干净手绘边缘、柔哑颜料、受控旧纸触感、低饱和灰蓝/砖红/赭金、长焦平面层叠与可信工业尺度、清晰低噪；粉尘保持大块柔形。
[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve both numbered keyframes' exact and matching art style in every interpolated frame. Treat KF01 as the immutable first frame and KF02 as the immutable terminal geometry. Animate this same artwork; do not reinterpret, redraw, beautify, simplify or replace the art direction. Preserve skyline, medium, edges, texture, palette, lighting, architecture, scale, fixed-camera composition and density. Only chimney rotation, root dust and string-light sway may evolve.
[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal, CGI/3D, anime, mascot, glossy game art, watercolor, oil paint, horror, disaster spectacle, model-default redraw, grain, texture crawl, edge shimmer, palette pumping or invented detail.
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:28–01:31；演出外部的烟囱事件层。
[CHARACTER_STATE_LOCK] 若出现极远人物点，其状态固定为 PERFORMANCE_BIPED_PRIVATE_DRESS；无可读角色身份变化。
[STATE_TRANSITION_RULE] 只授权烟囱由完整竖直进入受控左倾；不授权任何动物身体、服装或物种变化。
[SHOT_ID] SH28
[KEYFRAME_SEQUENCE] 01 | 0.0s | SH28_KF01 | 烟囱完整竖直、灯串微颤、根部无尘；02 | 3.0s | SH28_KF02 | 同一烟囱左倾25–35度、仅根部低尘、固定长焦轴线。
[TRANSITIONS] 01 -> 02 | 同一根部连续重力圆弧；天际线、焦段、灯串、建筑尺度和曝光不重置；无切镜、爆炸或断裂。
[STORYBOARD_SHEET] 08_generation/jobs/final_frames_v2/storyboard_sheets/SH28_NUMBERED_SHEET.png
[DURATION] 3.0s
[DURATION_RATIONALE] 两锚点表达一次短促但有重量的受控失稳：需有静止预备、可读倾斜和未落地终点；3 秒足够且避免长时几何漂移，必须保持一镜。
[TIMELINE]
0.0–0.6s: 表演：完全匹配 KF01。烟囱竖直静止，无烟无尘；灯串仅有毫米级颤动。摄影机固定 100–135mm、1.6m 高、无推拉摇移；焦点/曝光/冷暖光比保持。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
0.6–1.4s: 表演：烟囱顶部先向左偏离，根部保持绝对固定，整体刚体开始极慢圆弧旋转至约 8–12°；屋脊和路灯不动。灯串摆幅略增，尚无明显尘云；阴影按旋转自然移动。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
1.4–2.3s: 表演：重力加速使整体倾至约 20–25°，烟囱仍一体、长度不变；根部出现低矮土黄尘团并沿地面小范围外扩，绝不升成烟柱。摄影机、焦点和天际线全锁。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
2.3–3.0s: 表演：烟囱平滑达到 KF02 的 25–35°终态但尚未着地；根部尘团略扩后开始减速，灯串完成一次小摆并回落。最后 0.2s 精确贴合 KF02 作为可剪终帧，无震屏、无爆炸。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
[CONTINUITY_LOCKS] KEYFRAME ORDER 01→02；同一根 45–60m 烟囱、同一根部、同一建筑和灯串、同一左倾方向、固定长焦轴线；城市结构完整，人物仅为不可辨小点；21:9、真实尺度、无切镜。
[NEGATIVE] no skipped keyframe, reverse fall, camera cut, shake, zoom, lens change, skyline morph, chimney stretch/shrink, rubber bending, fracture, explosion, fire, smoke, debris, giant dust, building damage, animal enlargement, duplicate character, flicker, warping, geometry boil, style drift, text, logo or watermark.
[AUDIO] 仅环境声/音效：远处沉闷的结构摩擦与低频轰鸣、灯串轻响、根部土尘的短促摩擦声；不内嵌音乐/BGM/配乐，不生成人声。《The Masterplan》仅在后期剪辑使用。
```

---

## SH29｜广场错峰反应

### IMAGE PROMPT — SH29

```text
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:31，承接 SH28 烟囱开始倾倒的声音；表演刚被打断，所有人仍在演出两足状态。
[CHARACTER_STATE_LOCK] 全体=PERFORMANCE_BIPED_PRIVATE_DRESS；阿白=ABAI_PERFORMANCE_DRESS_PHOTOLOCK，唯一猫、照片锁脸/斑纹/深灰尾、奶白衬衫+赭红背心+深青短外套，完整小提琴与琴弓；熊=深棕厚毛、芥末衬衫+孔雀蓝背心；狐=赤褐毛白下颌、深青外套+旧金围巾；兔=灰米短毛一耳弯、奶白衬衫+旧红裙裤；象=灰蓝皮肤短牙、砖红礼服外套；羊=灰白卷毛小弯角、芥末衬衫+深青披肩；狗=棕黑粗毛垂耳、氧化绿马甲+旧红围巾；驴=灰褐短毛长耳、奶白衬衫+旧赭背带裤。全部两足，物种差异明确，一物种一实例。
[STATE_TRANSITION_RULE] 禁止衣着、身份和身体状态变化；只允许对远处声响作错峰微反应。无人提前脱衣或四足化。
[INTENTIONAL_REALITY_EXCEPTIONS] 仅两足拟人动物表演规则；身体接触、杯与桌承重、小提琴姿势、建筑尺度、惯性均服从普通现实。
[STYLE_FINGERPRINT] DFT 旧纸蛋彩/哑光水粉、朴拙细线与干净剪影，褪色深青/灰蓝/赭金/旧红/孔雀蓝/奶白，亮于参考约一档；稳定寓言式横向群像，空间压平但桌、门、舞池有可信透视；表情克制、不惊悚；大形清楚、低噪，细节集中在阿白毛斑、琴弓、杯与礼服褶皱。
[REFERENCE_ROLES] DFT_DIRECTOR_REFERENCE=STYLE_ONLY；阿白批准板+照片=ABAI_IDENTITY/COSTUME_ONLY；配角 A/B 板=受 V2 活动锁约束的 IDENTITY/WARDROBE_ONLY；ENV-02_WHITEBOX=SPACE/BLOCKING_ONLY；GROUP_ACTION_LEDGER SH29+SCALE_LEDGER=TEXT_HARD_LOCK；SH27=前一镜角色位置/灯光方向连续性；SH28=声源方向而非画风覆盖。
[SUBJECT_AND_ACTION] 50mm 群体中景捕捉不同反应相位：左侧阿白把琴弓从弦上降低但小提琴仍稳托；熊正把杯放回桌面；狐狸只转上半身、脚仍维持旋转结束位；兔蹲低用两只毛爪靠近耳侧但不完全遮脸；大象一爪扶住轻晃桌沿，鼻子下垂稳定重心；羊停在半步；狗看向摇动灯串而非烟囱；驴侧身扶稳刚失衡的舞伴但不抓成同一姿势。没有人惊叫，没有全员仰头。
[CAMERA_AND_COMPOSITION] 21:9，50mm 感，摄影机约 1.4m 高，位于舞池外侧沿 SH27 同一大轴线切近；阿白在左中景、桌与大象在右中景，兔在低位前景，狐狸/羊/狗/驴分布到中后景；用前景空椅背形成轻遮挡，画面中心保留反应间的负空间。人物不横排、不等距、不全正面；焦点覆盖阿白弓、熊杯与兔的低姿态，后景眼线仍清楚。
[LIGHTING] 延续 SH27 的赭金旧灯与冷灰蓝环境填光；烟囱声不引入闪光。灯串晃动使局部暖光在桌面上轻微偏移，阿白白毛不过曝，象皮与熊毛保留哑光体积；阴影柔、曝光稳定。
[SPACE_AND_CONTINUITY] 广场/礼堂布局、长桌、舞池边缘、灯串方向与 SH27 连续；声源在画外右后方；阿白琴弓由 SH27 悬停继续降低，熊的杯由举起继续放下；SH30 将切到空舞台与灯串余波，因此右后景保留该方向。
[SCALE_LOCK] 礼堂主门≥3.4m、舞台约0.65m、桌椅和杯可实际使用；2.55m 两足象低于门楣且扶桌姿势可信；所有脚/蹄落在同一地面透视；中后景人物按深度缩小，不得与门窗/建筑等高。
[GROUP_ACTION_LOCK] 阿白=降琴弓；熊=放杯；狐=上身半转；兔=蹲低护耳；象=扶桌；羊=停半步；狗=看灯；驴=扶稳舞伴。至少三种高度、四种朝向、八种动作；禁止全员仰头、遮脸、背对或同一手位。
[NEGATIVE] no screaming, panic stampede, exaggerated open mouths, synchronized looking-up, cloned hand-to-face gesture, duplicate cat/fox/elephant, species homogenization, human hands, extra limbs, fused paws, impossible cup/table contact, broken violin, dense instruments, costume swap, early undressing, quadruped transition, tiny hall, giant animals, photoreal, 3D, anime, Disney mascot, glossy render, watercolor drift, horror, apocalypse, magical light, text/logo/watermark; no film grain, speckles, muddy microtexture, sharpening halos, fake detail or JPEG noise.
```

### AIGC IMAGE-TO-VIDEO PROMPT — SH29

```text
[STYLE_FINGERPRINT] 严格继承 SH29 的 DFT 旧纸蛋彩/哑光水粉、朴拙干净手绘边缘、褪色深青赭金低饱和色、柔哑照明、寓言式平面群像与可信尺度、简化两足物种比例、清晰低噪纹理。
[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the input image's exact art style in every frame. Animate the same artwork without reinterpretation, redraw, beautification, simplification or replacement. Preserve all identities, costumes, anatomy, props, environment geometry, palette, lighting, edges, paper/paint behavior, depth treatment and composition density; only the assigned staggered reactions and minimal camera settle may change.
[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No model-default photorealism, CGI/3D, anime, mascot, glossy game art, watercolor, oil paint or horror; no grain, texture crawl, edge flicker, palette shift or face redraw.
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:31–01:34；烟囱异动后的广场反应层。
[CHARACTER_STATE_LOCK] 阿白=ABAI_PERFORMANCE_DRESS_PHOTOLOCK；全体居民=PERFORMANCE_BIPED_PRIVATE_DRESS；演出服、物种身份与道具全程锁定。
[STATE_TRANSITION_RULE] 本视频无状态转换；只允许八个角色按账本错峰反应，不得提前脱衣或四足化。
[DURATION] 3.0s
[DURATION_RATIONALE] 一个冲击声后的群体反应需要先传到近景、再传到后景并留短暂静默；3 秒可读且避免复杂群像长时间漂移。
[TIMELINE]
0.0–0.6s: 表演：精确保持输入姿势前一刻：灯串先小摆，桌面杯水产生轻微波纹；阿白弓仍接近弦，熊杯刚开始下降。摄影机 50mm、1.4m 高、固定轴线；焦点/曝光/暖冷光保持。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
0.6–1.5s: 表演：反应错峰发生：阿白降低琴弓；熊把杯底放到桌面；狐狸只转上身；兔蹲低；象扶稳桌沿。羊、狗、驴仍晚半拍，所有动作幅度克制，衣料/毛发按惯性响应。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
1.5–2.3s: 表演：羊停在半步，狗视线上移到灯串，驴侧身扶稳舞伴；阿白弓停在胸前下方，熊爪离开杯，象保持桌沿。摄影机极轻向右平移不超过画幅 2%，制造前景椅背微视差，禁止改轴。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
2.3–3.0s: 表演：所有人进入不同终态的短静默：有人低、有人侧、有人仍扶物，不形成齐停造型；灯串摆幅减小，杯水回稳。摄影机在 2.7s 平滑定住，最后 0.3s 可剪；光线与空间锁定。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
[CONTINUITY_LOCKS] 唯一阿白/狐狸/象等主角色；演出服不变；阿白完整琴与弓、熊单一杯、长桌和灯串；SH27→SH29 动作因果；右后方声源、50mm 同轴线、真实比例、无切镜。
[NEGATIVE] no cut, camera shake, zoom, crowd teleport, all-at-once reaction, all looking up, cloned gestures, duplicated species, second cat, facial exaggeration, speech/lip sync, costume change, early transformation, human hands, extra limbs, prop duplication, broken violin, cup spill spectacle, flicker, warping, style drift, text/logo/watermark.
[AUDIO] 仅环境声/音效：远处低频坍塌余响、杯底落木桌、桌腿轻响、琴弓离弦的短尾音、衣料与动物足部轻摩擦；无音乐/BGM/配乐、无歌词或口型声。《The Masterplan》仅后期剪辑使用。
```

---

## SH30｜演出余波插镜

### IMAGE PROMPT — SH30

```text
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:34，烟囱异动后的余波，人物已退出主视觉，灯还未全部熄灭。
[CHARACTER_STATE_LOCK] 远处若保留静影，只能是 PERFORMANCE_BIPED_PRIVATE_DRESS 的原角色，数量与 SH29 连续、不可辨脸且不得复制；阿白不在可读前景，不新增猫。
[STATE_TRANSITION_RULE] 本镜头无角色状态转换；只允许尘、灯串和舞台布边的物理余振。不得提前出现四足动物或脱下的华服。
[INTENTIONAL_REALITY_EXCEPTIONS] 无。物件受风和低频震动的幅度保持现实，尘埃不具魔法形状。
[STYLE_FINGERPRINT] DFT 旧纸蛋彩/哑光水粉物件插镜，朴拙手绘边缘、柔哑不透明颜料、褪色深青灰蓝与旧金灯点，低对比、克制余韵；前中后景压平但台沿、灯串和远处人影有可信深度；大形清楚、平滑色面、低噪，尘只作少量柔软颗粒群。
[REFERENCE_ROLES] DFT_DIRECTOR_REFERENCE=STYLE_ONLY；ENV-02_WHITEBOX=舞台/灯串/舞池空间 ONLY；SH29=灯色、人物远景数量与余振因果；SCALE_LEDGER=舞台/礼堂尺度；不使用任何被退回人物板作动作或构图。
[SUBJECT_AND_ACTION] 70–85mm 插镜：空舞台的旧布边在右侧轻轻震动，左上同一串旧金灯泡仍在小幅摆，舞台台面落下一层非常薄的土尘；人物只在远处成为数个不同高低、不同物种的静影，退到背景而不抢主体。画面强调演出突然留下的空白，不是灾难现场。
[CAMERA_AND_COMPOSITION] 21:9，70–85mm，中近物件镜头，摄影机约 1.0m 高，轻微侧视舞台台沿；前景用一块虚焦空椅边缘框住左下，焦点在布边/台沿尘与一枚晃动灯泡，远处人物位于下方窄条且不居中；构图从 SH29 的群像密度突然收缩到留白。固定镜头，无宏大废墟全景。
[LIGHTING] 旧金灯泡作局部柔暖主光，灰蓝环境光填满空舞台，亮度比 SH29 略降但不黑；布边与薄尘有柔和侧逆光，灯泡不过曝、不闪爆，阴影稳定。
[SPACE_AND_CONTINUITY] 舞台高约0.65m、灯串方向、空椅和远处人物层级承接 SH29；远处工厂不入镜；为 SH31 空街冷色回落预留灰蓝基调。不得凭空出现新乐器、倒塌建筑或散落服装。
[SCALE_LOCK] 舞台台沿与台阶保持可用尺度，灯泡/线缆/椅背比例真实；远处静影必须低于礼堂门楣并按透视缩小；尘层不改变物体体量。
[GROUP_ACTION_LOCK] 无可读群像；远处静影只保留不同高低/朝向，不允许复制同一轮廓或全员整齐横排。
[NEGATIVE] no collapsing stage, no ruined hall, no explosion, flame, smoke wall, apocalypse, horror, magical dust, crowded foreground, readable duplicate animals, second cat, new instrument pile, broken props, tiny stage, giant figures, photoreal, 3D, anime, mascot, glossy render, watercolor drift, text/logo/watermark; no heavy film grain, random speckles, muddy texture, sharpening halo, fake microdetail, noisy background or JPEG artifacts.
```

### AIGC IMAGE-TO-VIDEO PROMPT — SH30

```text
[STYLE_FINGERPRINT] 严格继承 SH30 输入图的 DFT 旧纸蛋彩/哑光水粉物件语言：朴拙干净边缘、柔哑颜料、褪色深青灰蓝/旧金、平面留白与真实物件尺度、清晰低噪。
[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the input image's exact art style and every visible design in all frames. Animate this same artwork only; do not redraw, restyle, beautify or replace it. Preserve medium, edges, texture, palette, light, stage geometry, lamp count, background silhouettes, depth and density. Only subtle settling motion is allowed.
[STYLE_NEGATIVE] Strictly do not change or replace the source style. No photoreal, CGI/3D, anime, mascot, glossy render, watercolor, oil paint, horror/disaster art, grain, texture crawl, edge shimmer or palette pumping.
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:34–01:36；演出余波物件层。
[CHARACTER_STATE_LOCK] 远处不可辨静影若存在，固定为 PERFORMANCE_BIPED_PRIVATE_DRESS；不得新增或重画任何活动角色。
[STATE_TRANSITION_RULE] 本视频无角色状态转换；只允许灯串、布边和薄尘的物理余振。
[DURATION] 2.0s
[DURATION_RATIONALE] 纯余波插镜只需一次灯串回摆、布边震动与薄尘落定；2 秒提供清楚标点而不拖慢叙事。
[TIMELINE]
0.0–0.5s: 表演：匹配输入构图。灯串由 SH29 余势向右小摆，布边同向震一下，薄尘刚从台沿落下；固定 70–85mm、1.0m 高，焦点锁布边与灯泡，曝光保持。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
0.5–1.3s: 表演：灯串回摆幅度缩小，布边出现一次更弱的反向波，少量尘粒在侧逆光中下降；远处人物仅有呼吸/重心微动，不改变数量或轮廓。摄影机完全静止，空间与阴影锁定。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
1.3–2.0s: 表演：灯串接近垂直，布边停住，尘粒落到台面；灯光亮度缓慢降极小一档但不熄灭。最后 0.3s 稳定持有可剪终帧。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
[CONTINUITY_LOCKS] 同一舞台/灯串/布边/远景静影，灯串数量与位置不变；SH29 余振因果、SH31 冷色过渡；21:9、固定镜头、真实尺度。
[NEGATIVE] no cut, zoom, shake, new debris, dust explosion, stage damage, lamp multiplication, silhouette duplication, crowd approach, animal morph, light flicker, exposure pumping, geometry warping, style drift, text/logo/watermark.
[AUDIO] 仅环境声/音效：灯线细响、布边轻拍、微尘落木台、远风和极远结构余鸣；不嵌入音乐/BGM/配乐，不生成人声。《The Masterplan》后期另行剪入。
```

---

## SH31｜华服角色穿过空街返回

### IMAGE PROMPT — SH31

```text
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:36，演出停止后、尚未回到更衣室，角色仍以为会重新穿回工装。
[CHARACTER_STATE_LOCK] 全体=PERFORMANCE_BIPED_PRIVATE_DRESS；阿白=ABAI_PERFORMANCE_DRESS_PHOTOLOCK，唯一猫、照片锁脸/灰绿眼/粉鼻/天然头顶斑/鞍状背斑/深灰尾，奶白衬衫+旧赭背心+深青短外套；羊=灰白卷毛小弯角、旧芥末衬衫+深青披肩；象=灰蓝厚皮短牙、砖红礼服外套；驴=灰褐短毛长耳、奶白衬衫+赭色背带裤；狗=棕黑粗毛垂耳、氧化绿马甲+旧红围巾；狐=赤褐毛白下颌、深青短外套+旧金围巾；兔=灰米短毛一耳微弯、奶白衬衫+旧红裙裤；熊=深棕厚毛、芥末衬衫+孔雀蓝背心。全员仍为两足拟人结构，一物种一实例。唯一一只旧木琴盒已闭合，由熊稳妥双爪搬运；乐器不可露出或密集出现。
[STATE_TRANSITION_RULE] 本镜头不换装、不脱衣、不转四足；只从“广场演出动作”转为“返回更衣室的两足步行”。演出服、体态和身份全程锁定。
[INTENTIONAL_REALITY_EXCEPTIONS] 仅批准两足拟人动物穿衣、以毛爪/蹄搬琴盒和步行；街道、重力、步态、箱体承重与建筑尺度普通真实。
[STYLE_FINGERPRINT] DFT 旧纸蛋彩/哑光水粉，朴拙细线、柔哑不透明颜料与受控旧纸触感；暖赭金从衣物上褪去，街道恢复灰蓝、氧化绿、褪砖红、奶白，亮度仍高于导演参考约一档；安静苍凉而非末日，寓言式平面街景但楼层、门窗、路灯和人物深度比例可信；清洁大轮廓、低噪，细节只落在前景衣料、琴盒木面和阿白毛斑。
[REFERENCE_ROLES] DFT_DIRECTOR_REFERENCE=STYLE_ONLY；阿白批准板+照片=ABAI_IDENTITY/COSTUME_ONLY；SUPPORTING_CAST_A/B=V2 活动锁许可范围内的 IDENTITY/WARDROBE_ONLY；SCALE_LEDGER=街道/住宅/路灯比例；SH30=冷色与余波时间连续；旧城镇锚点和被否决场景不得覆盖风格、角色或建筑比例。
[SUBJECT_AND_ACTION] 背面/侧背宽景，八个华服角色从空广场沿红砖主街错落返回：狐狸在左前景贴墙快走、尾巴低垂；兔以短小快步从街心越向内侧；大象在右中景缓慢迈大步；熊双爪在腹前搬唯一闭合琴盒；狗落后半步回头听余响；羊一爪压住被风掀起的深青披肩边；驴边走边扶正一侧背带；阿白在中后景空爪、最后离开，头微低。无人列队，无统一步幅，无人演奏或端杯。
[CAMERA_AND_COMPOSITION] 21:9，35mm 感，摄影机约1.25m高，位于主街一侧稳定背面宽景；街道从右前方斜向左后方更衣室方向消失，人物分布在前中后景三层，阿白不居中但可由白毛/深灰尾找到；前景用路灯基座和墙角形成不对称框景，天空/街面留出大块冷色负空间。焦点在熊的闭合琴盒与中层人物，远处阿白仍清楚；无横排合照。
[LIGHTING] 广场后方残余赭金从画面右后方作很弱轮廓光，街道上方灰蓝天光作主填光，路灯为零星旧金实景光；越向更衣室方向越冷，衣服仍保留旧红/深青/芥末色但不发亮；阴影长而柔，无浓雾和灾难烟尘。
[SPACE_AND_CONTINUITY] 承接 SH30，广场在右后画外，角色朝更衣室所在左后方前进；街上无其他队伍，红砖宿舍、窄巷与更衣室远门构成真实城镇路径；唯一琴盒在 SH32 仍由熊搬入；阿白最后离开且不成为领头。镇貌破败但门窗完整、道路可行。
[SCALE_LOCK] 主街建筑间宽约10–14m；一层檐口3.3–3.8m、两层檐口6.5–8m、普通门2.6–2.9m、路灯5–6m；同平面2.55m两足象低于一层檐口与路灯，其他角色按深度缩小；琴盒与阿白小提琴尺寸相配，熊的搬运姿势可信；任何房屋都不得小于动物。
[GROUP_ACTION_LOCK] 狐=贴墙快走；兔=短步横切；象=慢步；熊=搬闭合琴盒；狗=回头听；羊=按披肩；驴=扶背带；阿白=中后景最后步行。八种动作、三层深度、多种朝向；禁止齐步、同摆臂、同回头、重复物种或全员走同一轨迹。
[NEGATIVE] no parade, marching line, synchronized gait, all looking back, duplicated cat/fox/elephant, recolored-cat species, dense instruments, open violin, tray, cups, performance action, costume loss, early quadruped, human hands, extra limbs, fused feet, impossible case grip, tiny houses, oversized animals, miniature street, photoreal, plastic 3D, anime, mascot, glossy render, watercolor drift, horror, apocalypse, smoke/fog wall, pseudo-text, logo or watermark; no grain, speckles, muddy microtexture, sharpening halos, fake pixel detail, noisy background or JPEG artifacts.
```

### AIGC IMAGE-TO-VIDEO PROMPT — SH31

```text
[STYLE_FINGERPRINT] 严格继承 SH31 输入帧的 DFT 旧纸蛋彩/哑光水粉、朴拙干净手绘边缘、褪色冷灰蓝/砖红与残余赭金、柔哑纸面、寓言式压平街景与真实楼层尺度、清晰低噪。
[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the input image's exact style and visual design in every frame. Animate this same artwork only; do not redraw, restyle, beautify, simplify or replace it. Preserve all identities, species, garments, case, architecture, palette, lighting, edges, paper/paint texture, perspective and density. Only assigned walking micro-actions, cloth/tail response and slow camera drift may change.
[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal, CGI/3D, anime, mascot, glossy game art, watercolor/oil conversion, horror, grain, texture crawl, edge shimmer, identity redraw or palette pumping.
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:36–01:39；演出结束后返回更衣室途中。
[CHARACTER_STATE_LOCK] 阿白=ABAI_PERFORMANCE_DRESS_PHOTOLOCK；全体居民=PERFORMANCE_BIPED_PRIVATE_DRESS；演出服、两足体态、唯一闭合琴盒与一物种一实例锁定。
[STATE_TRANSITION_RULE] 本视频无状态转换；只从演出动作转为错峰两足步行，禁止脱衣或四足化。
[DURATION] 3.0s
[DURATION_RATIONALE] 一组错峰步态完成从广场到更衣室的空间桥接，3 秒足以读出“无队列、不同步、暖色退场”，同时避免群像长时间漂移。
[TIMELINE]
0.0–0.7s: 表演：精确承接输入。狐狸先迈一步、兔开始短步横切，象尚在抬脚预备；熊琴盒贴近身体保持水平，阿白在后层刚进入街面。摄影机35mm、1.25m高，沿人物方向极慢前移；焦点/曝光锁定。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
0.7–1.7s: 表演：象完成一次沉重落步，兔完成两次短步，狐狸尾巴随步态摆小弧；羊按住披肩，驴扶正背带，狗回头角度增加但身体继续前行。熊保持箱体水平，衣料/毛发只作自然惯性；人物之间距离不收成队列。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
1.7–2.5s: 表演：前层狐狸向左后空间深入，兔转回主行进方向；狗视线回到前方，羊披肩落稳，阿白慢半拍迈出一步。摄影机只前移约画幅深度3%，路灯基座产生轻微视差，镜头不摇不变焦。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
2.5–3.0s: 表演：整体步态自然减速到可剪终点，熊仍搬琴盒，阿白保持最后位置；残余暖边光进一步变弱但不熄灭。摄影机平滑定住，最后0.2s稳定。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
[CONTINUITY_LOCKS] 演出服、两足状态、唯一阿白/狐狸/象等；唯一闭合琴盒由熊搬；街道右前→左后方向、广场在右后画外、更衣室在左后；35mm、真实尺度、无切镜。
[NEGATIVE] no cut, time jump, line-up, synchronized walk, gait cloning, crowd teleport, duplicated species, second cat, costume swap, instrument reveal, tray/cup addition, early animal transformation, human fingers, extra limbs, case deformation, architecture shrink, scale pumping, flicker, warping, style drift, text/logo/watermark.
[AUDIO] 仅环境声/音效：不同材质与重量的错峰足音、披肩和围巾轻响、琴盒木扣细响、空街风声与远处结构余鸣；无音乐/BGM/配乐，无歌词和口型声。《The Masterplan》后期另行剪辑。
```

---

## SH32｜门内反打，第一批人看见空墙

### IMAGE PROMPT — SH32

```text
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:39，角色从空街回到 ENV-01 更衣室门口，尚未完全确认工装消失。
[CHARACTER_STATE_LOCK] 全员保持 PERFORMANCE_BIPED_PRIVATE_DRESS 与 SUPPORTING_CAST_IDENTITY_LOCK_V2 演出服：阿白=ABAI_PERFORMANCE_DRESS_PHOTOLOCK，唯一猫/照片锁身份/奶白衬衫+赭红背心+深青外套；兔灰米一耳弯/奶白衬衫+旧红裙裤；象灰蓝短牙/砖红礼服外套；熊深棕宽体/芥末衬衫+孔雀蓝背心；狗棕黑垂耳/氧化绿马甲+旧红围巾；羊、驴、狐保持各自活动锁。全部两足；熊搬唯一闭合木琴盒，其他乐器不可见。
[STATE_TRANSITION_RULE] 本镜头只允许“进入→停顿→看见空钩”的表演变化；禁止脱衣、转四足或工装突然重现。角色身份与服装全程不变。
[INTENTIONAL_REALITY_EXCEPTIONS] 仅两足拟人动物穿衣和使用门/琴盒；门洞、地面、家具、重力和遮挡普通真实。镜面只能反射现有角色，绝不生成复制角色。
[STYLE_FINGERPRINT] DFT 旧纸蛋彩/哑光水粉，朴拙细线、柔哑不透明颜料、受控旧纸触感；更衣室灰蓝/氧化绿/褪砖红为主，门外残余旧金暖光进入一条，亮于参考约一档；平面化室内分层但门、柜、钩、凳和通道尺度清楚；克制神情与安静荒诞，干净大形、低噪。
[REFERENCE_ROLES] DFT_DIRECTOR_REFERENCE=STYLE_ONLY；阿白批准板+照片=ABAI_IDENTITY/COSTUME；配角A/B=V2许可的IDENTITY/WARDROBE_ONLY；ENV-01_WHITEBOX_3VIEWS_attempt_002=唯一 SPACE/CAMERA/BLOCKING 参考；SCALE_LEDGER+GROUP_ACTION_LEDGER SH32=TEXT_HARD_LOCK；SH31=入场方向与熊琴盒连续；被拒 ENV-01 attempt_001/旧排排站人设不得作活动风格或构图。
[SUBJECT_AND_ACTION] 摄影机在更衣室内向门口反打：兔最先跨进并突然停住，一耳向前、一耳略弯；阿白在兔肩后刚看见空衣钩墙，视线越过兔而非直视镜头；大象仍在足够高宽的门外，只露完整头肩与一侧前臂，不被门楣裁断；熊正搬唯一闭合琴盒跨门槛；狗已进门但回头示意后方；羊、驴、狐各处于门外、门槛、通道不同阶段。无人横排，无人同时仰头。
[CAMERA_AND_COMPOSITION] 21:9，35–40mm感，摄影机约1.45m高，位于更衣室内靠左、朝右后方大门；门框形成右侧深景框，空钩墙占左中景，长凳从左前景斜向中部；兔位于中心偏右的停顿点，阿白仅部分被兔肩遮挡但脸/头顶斑可读，大象在后景门洞证明尺度；焦点从兔延伸到阿白/空钩，熊琴盒处于中层。保持穿越门槛的纵深，不做正面合照。
[LIGHTING] 室内冷灰蓝顶窗散射光作主填，门外旧金残光从右后方形成轮廓，空钩墙稍亮以引导视线；阿白白毛不过曝，大象灰蓝皮肤与熊深毛有层次；金属衣钩只出微弱哑光反射，无恐怖阴影或超自然光。
[SPACE_AND_CONTINUITY] 严格沿 ENV-01 白模：大门→主通道→长凳→高/中/低衣钩与柜；所有工装、工牌、工帽确实缺席，琴盒仍闭合；角色从 SH31 的街道方向进入，SH33 将从同一空间揭示空钩。镜面不得创造第二狐狸/阿白。
[SCALE_LOCK] 更衣室净高≥4.5m，主门净高≥3.3m/净宽≥2.8m，通道≥3.2m，柜高2.2–2.4m，凳高0.50m；2.55m两足象可自然通过且不顶门楣，兔/阿白与门窗/凳保持既定身高比；琴盒不大于熊躯干且可通过门。
[GROUP_ACTION_LOCK] 兔=先入停住；阿白=从兔肩后看到空墙；象=仍在门外；熊=搬琴盒跨门槛；狗=回头示意；羊/驴/狐=分别处于门外、门槛、通道不同进入相位。禁止八人横排、同一步态、同眼线或门洞小于大象。
[NEGATIVE] no empty-room-only shot, no line-up, no synchronized stop, all staring at camera, duplicate cat/fox/elephant, mirror clone, recolored cats, human hands, extra limbs, fused bodies at doorway, impossible case grip, open instruments, tray/cups, factory uniforms reappearing, early undressing, quadruped form, tiny door, clipped elephant, miniature locker room, photoreal, 3D, anime, mascot, glossy render, watercolor drift, horror, text/logo/watermark; no grain, speckles, muddy microtexture, sharpening halos, fake detail, noisy background or JPEG artifacts.
```

### AIGC IMAGE-TO-VIDEO PROMPT — SH32

```text
[STYLE_FINGERPRINT] 严格继承 SH32 输入图的 DFT 旧纸蛋彩/哑光水粉室内语言：朴拙干净线边、柔哑颜料、冷灰蓝/氧化绿与门外旧金、寓言式压平但尺度明确的柜/门/凳空间、清晰低噪。
[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the input image's exact art style and all visible design in every frame. Animate this same artwork; do not reinterpret, redraw, beautify, simplify or replace it. Preserve identities, garments, anatomy, case, empty hooks, whitebox geometry, palette, light, paper/paint behavior, depth and scale. Only staggered entrance, gaze and camera settle may change.
[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal, 3D/CGI, anime, mascot, glossy game art, watercolor/oil conversion, horror, grain, texture crawl, edge shimmer, identity redraw or palette pumping.
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:39–01:42；进入更衣室并首次看见空钩。
[CHARACTER_STATE_LOCK] 阿白=ABAI_PERFORMANCE_DRESS_PHOTOLOCK；全体居民=PERFORMANCE_BIPED_PRIVATE_DRESS；演出服、两足结构与熊搬运的闭合琴盒锁定。
[STATE_TRANSITION_RULE] 本视频无状态转换；只允许进入、停顿和眼线改变，禁止脱衣、工装重现或四足化。
[DURATION] 3.0s
[DURATION_RATIONALE] 需要在同一镜头里读清“兔先停→阿白从肩后看见→后方仍在进门”的错峰空间因果；3 秒足够且不应切成多镜。
[TIMELINE]
0.0–0.7s: 表演：兔跨完门槛的最后半步，阿白仍在其后前行；熊琴盒保持水平，大象在门外慢步接近，狗刚进门。摄影机35–40mm、1.45m高、固定左内侧轴线，轻微向空钩墙滑动；焦点先锁兔。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
0.7–1.5s: 表演：兔突然停住并把视线落到左侧空钩；阿白因遮挡晚半拍抬眼，从兔肩后看见同一墙面；熊减速但未停，大象仍不入门。摄影机横滑不超过画幅3%，焦点平缓从兔移到阿白/空钩，曝光不变。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
1.5–2.3s: 表演：狗回头示意后方，熊跨门槛并稳住琴盒，羊/驴/狐分别前进小半步；兔保持低位停顿，阿白胸口一次轻呼吸。门外暖光和室内冷光保持，衣料/毛发自然沉降。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
2.3–3.0s: 表演：所有人停在不同阶段，大象仍完整处于高大门洞后方；摄影机滑动减速，焦点最终落在阿白眼线与空钩之间，最后0.3s稳定可剪。无人形成齐排。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
[CONTINUITY_LOCKS] SH31→SH32行进方向；ENV-01门/通道/凳/柜/空钩；唯一闭合琴盒由熊搬；全员演出服和两足状态；兔先、阿白后、象门外；真实尺度、无切镜。
[NEGATIVE] no cut, camera reset, door morph, crowd teleport, line-up, synchronized stop, duplicated species, mirror clone, second cat, costume change, uniform reappearance, case opening, early transformation, human fingers, extra limbs, clipping through door, scale pumping, flicker, warping, style drift, text/logo/watermark.
[AUDIO] 仅环境声/音效：门槛上错峰足音、琴盒木扣轻响、衣料摩擦、角色呼吸、空室轻回声和门外风；无音乐/BGM/配乐、无歌词或对白。《The Masterplan》仅后期剪辑使用。
```

---

## SH33｜空衣钩主揭示

### IMAGE PROMPT — SH33

```text
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:42，众人已看清工装、工牌和工帽全部不见；这是解释缺席的主揭示，不是转化镜头。
[CHARACTER_STATE_LOCK] 全员仍为 PERFORMANCE_BIPED_PRIVATE_DRESS：阿白=ABAI_PERFORMANCE_DRESS_PHOTOLOCK，唯一猫/照片锁身份/演出服与深灰尾；配角按 SUPPORTING_CAST_IDENTITY_LOCK_V2 的物种、毛色、体型和演出服。熊把唯一闭合琴盒轻放在凳旁；无人持乐器、托盘或多余杯。全部两足，一物种一实例。
[STATE_TRANSITION_RULE] 本镜头只允许发现后的微反应；服装和两足身体不变。空钩不得自动长出工装，任何角色不得提前裸身或四足化。
[INTENTIONAL_REALITY_EXCEPTIONS] 仅两足拟人动物使用更衣室；其他空间、镜面、重力、家具和接触服从现实。镜面不得生成不存在的角色。
[STYLE_FINGERPRINT] DFT 旧纸蛋彩/哑光水粉，细而朴拙的手工边缘、柔哑不透明颜料、受控旧纸触感；冷灰蓝、氧化绿、褪砖红、旧木棕，残余暖色只留在华服，整体亮于参考一档；静态寓言式宽景，空墙和空钩形成清楚负空间，家具与人物比例真实；低噪、平滑色块、克制微表情。
[REFERENCE_ROLES] DFT_DIRECTOR_REFERENCE=STYLE_ONLY；FIN-010.png=STORY_CONTENT/LAYOUT_CANDIDATE_ONLY，不得覆盖风格、角色身份、动作、尺度或人数；阿白批准板+照片=IDENTITY/COSTUME；配角A/B=V2许可的IDENTITY/WARDROBE_ONLY；ENV-01_WHITEBOX=SPACE_ONLY；SCALE_LEDGER+GROUP_ACTION_LEDGER SH33=TEXT_HARD_LOCK。
[SUBJECT_AND_ACTION] 宽景揭示一整面高/中/低层空衣钩、空柜与空凳：阿白在左中景以一只毛爪轻触唯一空钩，另一爪自然下垂；兔蹲低看凳下；大象在右后方打开最宽柜门；狗坐到长凳端部；驴望向空工牌槽；狐狸只在真实镜面中观察众人、身体本体仍可追溯；羊握住自己深青披肩边缘；熊把闭合琴盒轻放到地面。全员短暂停顿但微反应各异，不是同姿势看墙。
[CAMERA_AND_COMPOSITION] 21:9，35mm感，摄影机约1.55m高，介于平视与轻俯之间，从 SH32 门内轴线再向房间推进半个机位；空钩墙占画面上部与左侧大块负空间，角色散落在下方/右侧，长凳斜切前中景；阿白不居中，空钩是视觉主语。焦点覆盖阿白毛爪、空钩和兔的低位反应，后方大象/柜门仍可读；镜面反射角符合几何。
[LIGHTING] 冷灰蓝高窗光均匀照亮空墙，门外旧金残光已更弱；空金属钩有轻微哑光高光，华服保留低强度暖色，人物脸部不沉黑；阴影柔、无恐怖剪影。
[SPACE_AND_CONTINUITY] ENV-01 的门、通道、长凳、柜与三层衣钩不变；所有深蓝工装、工帽、工牌明确缺席；琴盒闭合留在凳边，为 SH34/SH35 继续存在；镜中角色可与本体一一对应，绝不多出第二只狐狸或猫。
[SCALE_LOCK] 房间净高≥4.5m，柜2.2–2.4m，凳高0.50m，衣钩分高/中/低层；大象使用最大柜、兔检查低层空间，人物与柜/凳/钩触点可信；门洞仍足够大但不抢画面。所有脚/蹄接地，家具不变成玩具。
[GROUP_ACTION_LOCK] 阿白=触空钩；兔=看凳下；象=开宽柜；狗=坐凳端；驴=看工牌槽；狐=借镜观察；羊=握披肩边；熊=轻放琴盒。八种微反应、不同高度/朝向/手位；允许共同静默，禁止共同站立凝视。
[NEGATIVE] no uniforms, hats or timecards reappearing, no all-standing stare, no line-up, no synchronized pointing, no duplicate cat/fox/elephant, no mirror-created extra character, no human hands, extra limbs, fused paws, floating feet, open/broken instrument, trays/cups, early undressing, naked biped bodies, quadruped animals, tiny lockers, miniature bench, wrong elephant clearance, photoreal, 3D, anime, mascot, glossy render, watercolor drift, horror, magical disappearance effect, text/logo/watermark; no grain, random speckle, muddy microtexture, sharpening halos, fake detail, noisy background or JPEG artifacts.
```

### AIGC IMAGE-TO-VIDEO PROMPT — SH33

```text
[STYLE_FINGERPRINT] 严格继承 SH33 输入帧的 DFT 旧纸蛋彩/哑光水粉、朴拙干净手绘边缘、冷灰蓝/氧化绿与残余暖衣色、柔哑旧纸、静态寓言空间和可信家具尺度、清晰低噪。
[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the input image's exact art style and every visible design in all frames. Animate this same artwork only; do not reinterpret, redraw, beautify, simplify or replace it. Preserve identities, garments, empty hooks, furniture, mirror geometry, case, palette, light, texture, depth and scale. Only differentiated micro-reactions and a small camera settle may change.
[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal, CGI/3D, anime, mascot, glossy art, watercolor/oil conversion, horror, magical effects, grain, texture crawl, edge shimmer or identity redraw.
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:42–01:44；确认工装消失的空钩揭示。
[CHARACTER_STATE_LOCK] 阿白=ABAI_PERFORMANCE_DRESS_PHOTOLOCK；全体居民=PERFORMANCE_BIPED_PRIVATE_DRESS；演出服、两足结构、空钩与闭合琴盒锁定。
[STATE_TRANSITION_RULE] 本视频无状态转换；只允许差异化微反应，禁止提前裸身或四足化。
[DURATION] 2.0s
[DURATION_RATIONALE] 这是一次短揭示：空钩先读到，再读个人微反应；2 秒能形成停顿且避免把静默误做长时间复制姿势。
[TIMELINE]
0.0–0.5s: 表演：从 SH32 的入场余势进入本构图，摄影机35mm、1.55m高缓慢前移最后一点并显露整面空钩；人物动作尚未完全停。焦点先落空钩，曝光/冷暖比保持。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
0.5–1.3s: 表演：阿白爪尖轻触空钩一次；兔低头看凳下；象把宽柜门打开到终点；狗坐实凳端；驴视线移向空工牌槽；狐狸镜像与本体同步；羊收紧披肩边；熊轻放琴盒。每人动作幅度不同，不齐停。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
1.3–2.0s: 表演：动作分别落稳，空钩保持空，琴盒接触地面后不反弹；摄影机在1.6s完全定住，焦点从空钩轻落到阿白爪尖/空钩接触处，最后0.4s静默可剪。只有呼吸、尾尖和衣料细微沉降。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
[CONTINUITY_LOCKS] ENV-01几何、空钩/空柜/空凳、演出服与两足状态；唯一阿白/狐狸/象等；镜像一一对应；闭合琴盒在凳边；35mm同轴、真实比例、无切镜。
[NEGATIVE] no cut, magical vanish, uniforms appearing, synchronized stare, pose cloning, mirror duplicate, second cat, costume change, early transformation, human fingers, extra limbs, prop teleport, case opening, furniture scaling, flicker, warping, style drift, text/logo/watermark.
[AUDIO] 仅环境声/音效：空钩被轻触的金属细响、柜门轴声、琴盒落地闷响、凳板轻吱、空室风与呼吸；无音乐/BGM/配乐、无对白或歌词。《The Masterplan》仅后期剪入。
```

---

## SH34｜最后脱下华服，仍保持两足

### IMAGE PROMPT — SH34

```text
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:44，确认工装消失之后，最后一次主动脱下私人华服；身体转化边界尚未启动。
[CHARACTER_STATE_LOCK] 开始帧全员为 PERFORMANCE_BIPED_PRIVATE_DRESS；阿白=ABAI_PERFORMANCE_DRESS_PHOTOLOCK；本图捕捉衣物移除的不同中间相位，但物种身份、两足脊柱、两臂/两爪、两腿/两足和一尾不变。阿白唯一猫，照片锁乳白长毛/灰绿眼/粉鼻/头顶天然斑/鞍状背斑/深灰尾，正从深青短外套一侧袖退出，赭红背心与奶白衬衫仍部分穿着；象折褪砖红外套；熊处理孔雀蓝背心；狐抽旧金围巾；兔脱一只鞋；狗弯腰松靴；羊滑下深青披肩；驴让奶白衬衫从一侧肩膀滑落。毛皮覆盖身体，无人类裸肤/性征。琴盒始终闭合。
[STATE_TRANSITION_RULE] 本镜头只授权服装从“穿着”到“整齐放在凳上”的变化；直到 3.0s 终点所有角色仍是完整无衣两足拟人状态。前肢不得落地承重，脊柱/骨盆/肩线不得转为四足；身体变化只能从 SH35-KF01 之后开始。
[INTENTIONAL_REALITY_EXCEPTIONS] 仅两足拟人动物以毛爪/蹄脱衣；普通衣料、重力、关节活动、凳面承重和空间比例真实。无衣状态以完整毛皮表现，不生成裸露人类身体。
[STYLE_FINGERPRINT] DFT 旧纸蛋彩/哑光水粉，朴拙细线、柔哑不透明颜料、受控旧纸触感；冷灰蓝更衣室中散落褪色旧红/深青/芥末/孔雀蓝华服，整体亮于参考一档；平面宽群像但每个动作剪影清楚、家具/门/柜真实可用；温柔克制、不羞辱、不恐怖；低噪大形，细节集中在衣物折叠、阿白天然毛斑和毛皮轮廓。
[REFERENCE_ROLES] DFT_DIRECTOR_REFERENCE=STYLE_ONLY；阿白批准板+照片=ABAI_IDENTITY/FUR/COSTUME；配角A/B=V2许可的IDENTITY/WARDROBE_ONLY，不继承排排站、乐器、托盘；ENV-01_WHITEBOX=SPACE/BLOCKING_ONLY；TRANSFORMATION_STATE_LEDGER=NO_BODY_TRANSITION_BEFORE_SH35；GROUP_ACTION_LEDGER SH34+SCALE_LEDGER=TEXT_HARD_LOCK；SH33=琴盒/凳/空钩连续。
[SUBJECT_AND_ACTION] 40–50mm中宽景，以错峰动作表达最后脱华服：阿白退出深青短外套的一侧袖；熊侧身解孔雀蓝背心下方一个扣；大象把已脱下的砖红外套沿长凳折平；狐狸从颈后抽出旧金围巾；兔坐低只脱下一只鞋；狗弯腰松开一只靴；羊让深青披肩从一侧肩头滑到爪上；驴把奶白衬衫从一侧肩膀脱下、旧赭背带已松。八种动作动词/相位/高度/朝向不同，所有乐器已装盒且无人持有。
[CAMERA_AND_COMPOSITION] 21:9，40–50mm感，摄影机约1.35m高，位于 ENV-01 长凳斜侧，平视略俯；长凳横向贯穿中景但人物交错在前/中/后景，阿白在左中景、象在右中景、兔低位前景、其余穿插；空钩墙保留上方负空间，闭合琴盒在凳末端；焦点覆盖阿白外套袖口、象折衣与兔低位，不做八人并排教学图。
[LIGHTING] 冷灰蓝高窗柔光为主，门外残余暖光几乎消退；华服色块在哑光表面保留低强度暖色，毛皮边缘有轻柔灰金轮廓，阿白白毛不过曝；阴影柔，裸露毛皮不油亮、不照片写实。
[SPACE_AND_CONTINUITY] 更衣室门/通道/柜/三层空钩/长凳/琴盒承接 SH33；工装、工帽、工牌继续缺席；脱下衣物整齐留在长凳而不燃烧/溶解/变毛；SH35-KF01 必须从同一房间、同一相机轴线附近开始，华服和闭合琴盒位置可追溯。
[SCALE_LOCK] 房间净高≥4.5m、门≥3.3×2.8m、通道≥3.2m、柜2.2–2.4m、凳高0.50m；象可在凳旁折衣且不顶顶棚，兔坐凳/靠凳比例可信；衣服按各自动物体型合理放码，阿白外套/琴盒/凳均不随机变大缩小。
[GROUP_ACTION_LOCK] 阿白=退一侧外套袖；熊=解背心下扣；象=折长外套；狐=抽围巾；兔=脱一鞋；狗=松一靴；羊=滑披肩；驴=脱衬衫一肩。禁止全员双爪举衣、同胸前手位、同弯腰角度、同一衣物动作或重复物种。
[NEGATIVE] no body transformation, no quadruped pose, no forelimb weight-bearing, no horror morph, no pain, gore, stretched joints or exposed flesh; no human nude skin/anatomy, human hands/fingers, extra limbs, fused garments, clothing melting into fur, all holding shirts, cloned undressing pose, line-up, duplicate cat/fox/elephant, instruments on bodies, open/broken cases, uniforms reappearing, tiny room/door, photoreal, 3D, anime, mascot, glossy render, watercolor drift, text/logo/watermark; no grain, speckles, muddy microtexture, sharpening halos, fake detail, noisy background or JPEG artifacts.
```

### AIGC IMAGE-TO-VIDEO PROMPT — SH34

```text
[STYLE_FINGERPRINT] 严格继承 SH34 输入图的 DFT 旧纸蛋彩/哑光水粉、朴拙干净手绘边缘、冷灰蓝空间与褪色华服色块、柔哑毛皮/布料、寓言式宽群像和可信家具尺度、清晰低噪。
[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the input image's exact art style and all visible identities, anatomy, garments, room geometry, props, palette, lighting, texture, depth and scale. Animate this same artwork only; do not redraw, beautify, restyle, simplify or replace it. Only the assigned staggered clothing removal and small camera settle may change. Biped anatomy is immutable throughout SH34.
[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal, 3D/CGI, anime, mascot, glossy art, watercolor/oil conversion, horror, body-morph imagery, grain, texture crawl, edge shimmer, identity redraw or palette pumping.
[NARRATIVE_TIME] AFTER_CHANGING_BEFORE_FAREWELL；全片 01:44–01:47；身体转换边界前的最后脱华服。
[CHARACTER_STATE_LOCK] 起点与终点身体状态均绑定 PERFORMANCE_BIPED_PRIVATE_DRESS；阿白身份绑定 ABAI_PERFORMANCE_DRESS_PHOTOLOCK；终点华服已脱但仍保持完整无衣两足结构。
[STATE_TRANSITION_RULE] 只授权衣物从身体移到凳面；不授权解剖状态变化。前肢不接地承重，WILD_RETURN_QUADRUPED 只能从下一镜 SH35 开始。
[DURATION] 3.0s
[DURATION_RATIONALE] 八个角色并行完成各不相同的最后脱衣动作，需要起始错峰、衣物落凳与明确“仍是两足”的终帧；3 秒可读，身体转化留给下一镜。
[TIMELINE]
0.0–0.7s: 表演：匹配输入中间相位。阿白继续退出一侧外套袖；象已把外套铺到凳上；兔抬起一只脚脱鞋；摄影机40–50mm、1.35m高沿凳面极慢侧移，焦点/曝光保持。所有身体仍直立两足。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
0.7–1.6s: 表演：熊解开背心下扣，狐狸抽出围巾，狗完成松靴，羊披肩滑到爪上，驴衬衫越过一侧肩；阿白外套离身但衬衫/背心继续被下一小动作移除。每人节奏不同，衣料受重力落下，不交叉融合。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
1.6–2.4s: 表演：角色把各自最后衣物依次放/折到长凳：象最先完成，羊/狐随后，兔鞋落到凳下整齐位置，阿白最后把衣物放下；熊/狗/驴保持不同弯曲高度。摄影机侧移停止，琴盒与空钩位置锁定。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
2.4–3.0s: 表演：所有人完成无衣两足终态，毛皮完整覆盖、无裸露人类结构；双足承重，前爪不接地，重心尚未前移。衣物与闭合琴盒静置，最后0.3s稳定作为 SH35-KF01 的前置剪辑点。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
[CONTINUITY_LOCKS] SH33琴盒/空钩/凳/衣物位置；八个活动身份；演出服只转为凳上衣物，不融入身体；终点=无衣但仍两足；ENV-01尺度与轴线、21:9、无切镜。
[NEGATIVE] no cut, time jump, synchronized undressing, cloned poses, clothing teleport/melting, body morph, four-legged landing, horror, pain, exposed human skin, human fingers, extra limbs, species change, duplicate character, instrument reveal, uniform return, room scaling, flicker, warping, style drift, text/logo/watermark.
[AUDIO] 仅环境声/音效：不同布料错峰摩擦、扣子/鞋底/长凳轻响、呼吸和空室风；无音乐/BGM/配乐、无对白或歌词。《The Masterplan》仅在后期剪辑使用。
```

---

## SH35｜两足回到四足（一个连续镜头，三锚点）

### IMAGE PROMPT — SH35_KF01（编号 01／无衣两足起始锚点）

```text
[NARRATIVE_TIME] TRANSFORMATION_BOUNDARY_START；全片 01:47、SH35 0.0s；最后衣物已落到凳上，身体转化尚未开始。此帧是连续镜头 01 号锚点。
[CHARACTER_STATE_LOCK] 出站状态仍为 PERFORMANCE_BIPED_PRIVATE_DRESS 的身体结构，阿白=ABAI_PERFORMANCE_DRESS_PHOTOLOCK，但演出服已依 SH34 合理脱下；使用本镜头专用可观察标签 `UNCLAD_BIPED_BOUNDARY`：八个角色均为完整两足拟人动物，一头、两臂/两毛爪或蹄、两腿/两足、一尾，直立肩线与骨盆仍存在，毛皮完整覆盖、无任何人类裸肤/性征。阿白唯一猫，精确保留照片锁灰绿眼、粉鼻、乳白长毛、非对称头顶灰黑天然斑、背至后躯连续鞍状灰黑斑、深灰蓬尾；配角保留 V2 毛色/体型身份。华服与闭合琴盒已与身体分离。
[STATE_TRANSITION_RULE] KF01 是唯一合法起点：本帧不得出现四足承重、物种真实骨架或半途形态；从 KF01 之后、且只在 SH35 的 0.8–5.0s，才允许连续进入 WILD_RETURN_QUADRUPED。衣物/乐器绝不参与转化。
[INTENTIONAL_REALITY_EXCEPTIONS] 批准 SH35 唯一一次童话式身体结构重排，但 KF01 仍只使用项目既定的无衣两足拟人动物例外；转换须无痛、无撕裂、无器官/裸肉、无夸张拉伸，以重心下降、关节自然折叠和毛发轮廓连续来遮蔽结构变化。无其他物理/尺度例外。
[STYLE_FINGERPRINT] DFT 旧纸蛋彩/哑光水粉，朴拙细线、柔哑不透明颜料、受控旧纸触感；冷灰蓝/氧化绿更衣室、旧木棕、凳上少量褪色华服色块，整体亮于参考一档；温柔克制、无羞辱和肉体恐怖；寓言式平面宽景但房间尺度、接地和遮挡可信；清楚大轮廓、低噪，细节集中在阿白天然斑、不同物种毛皮和静置衣料。
[REFERENCE_ROLES] DFT_DIRECTOR_REFERENCE=STYLE_ONLY；阿白批准板+三张照片=ABAI_IDENTITY/FUR_PATTERN/BIPED_TO_WILD_TARGET；配角A/B=V2许可的BIPED IDENTITY ONLY，四足目标由 SUPPORTING_CAST_IDENTITY_LOCK_V2+TRANSFORMATION_STATE_LEDGER 定义；ENV-01_WHITEBOX=SPACE/CAMERA_ONLY；SH34=衣物/琴盒/人物位置连续；SCALE_LEDGER+GROUP_ACTION_LEDGER SH35-KF01=TEXT_HARD_LOCK。旧缺野生状态人设板不得定义转化机制或四足结构。
[SUBJECT_AND_ACTION] 无衣两足起始群像：阿白在左中景仍双足站立但躯干略前倾、双毛爪自然向下；兔在左前景已蹲低但双足承重；熊在右中景以双前爪扶住长凳边；大象在后景象鼻末端先触地但两腿仍直立；狗在中景先放低一只毛爪却未接地；狐狸侧身、一只爪略向前；羊前肩微降；驴双膝尚未弯到地面。华服整齐放在凳上，闭合琴盒靠凳脚，所有角色与衣物/乐器保持分离。
[CAMERA_AND_COMPOSITION] 21:9，35mm感，同一连续镜头固定轴线的起点；摄影机约1.15m高、位于更衣室通道靠门侧，平视偏低宽景，向房间深处看；长凳斜贯右中景，出口位于左后，八个角色以不同高低形成从左前到右后的锯齿轮廓；阿白左中、兔低前景、大象后景；镜面排除在画外以避免复制。焦点覆盖阿白/兔/熊，后景象仍清楚；为后续摄影机缓慢降低/后退留空间。
[LIGHTING] 冷灰蓝高窗柔光作主光，门外将明未明的灰金晨光从左后方轻勾轮廓；华服为低饱和色块，毛皮哑光且阿白白毛不过曝；阴影柔、无强反差、无红光/病态逆光。
[SPACE_AND_CONTINUITY] ENV-01 门/通道/长凳/柜/空钩位置与 SH34 完全连续；工装继续缺席，华服和闭合琴盒静置且后续不得燃烧/融化/粘入身体；出口方向在左后，为 KF03/SH36 的行动目标；镜头轴线、地平线和角色相对位置必须可无缝接 KF02。
[SCALE_LOCK] 房间净高≥4.5m、门≥3.3×2.8m、通道≥3.2m、柜2.2–2.4m、凳高0.50m；两足角色高度：兔1.30m、阿白1.55m、狐1.65m、狗1.70m、羊1.75m、驴1.90m、熊2.05m、象2.55m；大象低于顶棚/门楣且拥有下降空间，所有双足接地。
[GROUP_ACTION_LOCK] 阿白=站立前倾；兔=蹲低；熊=扶凳；象=鼻端触地；狗=放低一爪；狐=单侧爪前伸预备；羊=前肩微降；驴=双膝预弯。八种起始高度与相位，禁止全员同站姿/同蹲姿或同一前爪位置。
[NEGATIVE] no quadruped final anatomy yet, no kneeling line-up, no synchronized crouch, no clothing on bodies, no human nudity/skin/hands/fingers, no genitals, gore, wounds, bones, exposed flesh, melting, stretching, twisting, fused bodies, extra/missing limbs, duplicate cat/fox/elephant, mirror clones, animal-human hybrid horror, costume/prop fusion, open/broken instruments, tiny room or door, photoreal, 3D, anime, mascot, glossy render, watercolor drift, horror lighting, text/logo/watermark; no grain, speckles, muddy microtexture, sharpening halos, fake detail, noisy background or JPEG artifacts.
```

### IMAGE PROMPT — SH35_KF02（编号 02／不同相位的连续中段锚点）

```text
[NARRATIVE_TIME] TRANSFORMATION_IN_PROGRESS；全片约 01:49.5、SH35 约2.5s；这是仅存在于本连续镜头的过渡观察状态 `WILD_RETURN_TRANSITION_KF02`，不得用于前后其他镜头。
[CHARACTER_STATE_LOCK] 转换绑定从阿白 ABAI_PERFORMANCE_DRESS_PHOTOLOCK + 全体 PERFORMANCE_BIPED_PRIVATE_DRESS，单向进入阿白 ABAI_WILD_RETURN_PHOTOLOCK + 全体 WILD_RETURN_QUADRUPED；所有个体身份、毛色、脸型、耳/角/牙、尾巴和相对体型严格继承 KF01。阿白唯一猫，照片锁天然头顶斑、鞍状背斑、灰绿眼、粉鼻、深灰蓬尾不位移、不变成条纹。每个角色按各自物种进入不同转换相位：毛皮连续覆盖，无人类皮肤；前肢逐步成为承重前腿，但没有多余肢体、残留手腕或复制身体。
[STATE_TRANSITION_RULE] 仅授权 KF01→KF02→KF03 的单向连续变化：本帧不得倒回穿衣、不得跳过到所有角色同相位；KF02 后必须在同镜头 5.0s 前完成 WILD_RETURN_QUADRUPED。此过渡状态不允许延续到 SH36。
[INTENTIONAL_REALITY_EXCEPTIONS] SH35 0.8–5.0s 唯一批准的童话式形态转换：通过身体重心前移、肩胛/骨盆轴自然降低、前爪接地、躯干在毛发轮廓内平滑改为物种真实比例；无痛、无惊恐、无肌肉/骨骼外露、无橡胶拉伸、无肢体增殖。衣物和道具完全不参与。
[STYLE_FINGERPRINT] 与 KF01 完全同一 DFT 旧纸蛋彩/哑光水粉：朴拙干净描线、柔哑不透明颜料、受控旧纸、冷灰蓝/氧化绿/灰金晨光、克制童话转换、平面宽景与可信地面/家具比例；清晰低噪，以大轮廓变化而非颗粒/光效表现转化。
[REFERENCE_ROLES] SH35_KF01=同镜头起始身份/空间/相机/光色；阿白三张照片=WILD ANATOMY/FUR PATTERN TARGET，不继承照片媒介；配角四足目标=SUPPORTING_CAST_IDENTITY_LOCK_V2+TRANSFORMATION_STATE_LEDGER；DFT参考=STYLE_ONLY；ENV-01白模=SPACE_ONLY；SCALE_LEDGER+GROUP_ACTION_LEDGER SH35-KF02=TEXT_HARD_LOCK。旧双状态配角板不得提供第三状态或转化动作。
[SUBJECT_AND_ACTION] 同一房间、同一角色布局的错峰中段：阿白一只前爪已在地面承重，另一只尚离地，后足仍维持过渡高度；兔已四爪着地但身体尚未完全伸展；狐狸单侧前爪前伸、另一侧刚下降；狗两只前爪承重而后肢/骨盆仍在降低；羊前身已低、后身尚高；驴双膝接近地面但不跪成拟人姿态；熊双前爪从凳边转为地面稳定；大象前足落稳、后躯仍缓慢下沉。每个角色相位不同，表情平静，无痛苦。
[CAMERA_AND_COMPOSITION] 21:9，35mm，同一轴线；摄影机从 KF01 约1.15m缓慢降至约0.90m并后退极小距离，保持出口左后、长凳右中和角色屏幕位置关系；人物整体高度下降后仍完整入框，阿白和兔在左侧、大象后景、熊右中；焦点优先阿白承重爪与熊/狗的地面接触，房间几何和地平线连续，无切镜/反打/换焦段。
[LIGHTING] 完全继承 KF01 冷灰蓝高窗光和左后灰金晨光；只因身体降低使投影和轮廓光位置自然下移，无闪光、魔法粒子、发光毛发或曝光变化。
[SPACE_AND_CONTINUITY] 空钩、柜、凳、衣物、闭合琴盒、出口和地面纹理像素级连续；华服/琴盒远离落爪区域，不被踩住或卷入身体；每只前爪的地面接触有对应投影，身体互不穿透；相对位置必须直接接 KF03。
[SCALE_LOCK] 房间和家具尺寸不变；过渡中角色体量在两足总高与四足肩高之间自然降低，但质量/躯干长度不忽大忽小。最终目标肩高：兔0.25m、阿白0.28m、狐0.45m、狗0.60m、羊0.80m、驴1.25m、熊1.20m、象2.60m；本帧不强求全部到终值，但同平面大象始终最大、兔最小。
[GROUP_ACTION_LOCK] 阿白=单前爪承重；兔=已四爪着地；狐=单侧前爪前伸；狗=双前爪承重/后肢未完成；羊=前身降低；驴=双膝近地；熊=双前爪转地稳定；象=前足落稳/后躯下沉。禁止全员同跪伏、同高度、同完成度或陈列式整齐排列。
[NEGATIVE] no horror morph, pain, scream, gore, wounds, exposed muscle/bone/flesh, rubber stretching, melting, liquefying, smoke transformation, magical glow, limb sprouting, missing limbs, fused paws, twisted joints, backward knees, human hands/wrists, clothes on body, prop fusion, duplicate species, second cat, cat-like replacement of other species, sudden full-final pose for all, tiny elephant, giant rabbit, furniture/room morph, photoreal, 3D, anime, mascot, glossy render, watercolor drift, text/logo/watermark; no grain, particle noise, muddy texture, sharpening halos, fake detail or JPEG artifacts.
```

### IMAGE PROMPT — SH35_KF03（编号 03／完整四足终止锚点）

```text
[NARRATIVE_TIME] AFTER_FINAL_PERFORMANCE_WILD_DEPARTURE；全片 01:52、SH35 5.0s；转换完成后的第一帧，连续镜头 03 号终止锚点。
[CHARACTER_STATE_LOCK] 全员=WILD_RETURN_QUADRUPED：无衣、无拟人肩线、无可抓握前爪、无直立姿势；阿白=ABAI_WILD_RETURN_PHOTOLOCK，真实四足年轻长毛白猫，灰绿眼、粉鼻、浅粉内耳、非对称灰黑头顶天然斑、背至后躯单块鞍状灰黑斑、深灰蓬尾，真实家猫肩高/体长；羊=真实四足灰白卷毛绵羊、小弯角瘦脸；象=真实四足灰蓝大象、短牙、最大体量；驴=真实四足灰褐驴、长耳；狗=真实四足棕黑粗毛垂耳狗；狐=真实四足赤狐、白下颌蓬尾；兔=真实四足灰米兔、一耳略弯；熊=真实四足深棕熊。每种一个实例。
[STATE_TRANSITION_RULE] KF03 已完成并锁定 WILD_RETURN_QUADRUPED；不得残留两足、衣袖、鞋、手腕或中间态。从此帧至片尾禁止重新直立或穿衣。
[INTENTIONAL_REALITY_EXCEPTIONS] 转换本身至此结束；KF03 不再允许异常解剖或物理例外。四足动物结构、承重、步态、相对尺度和接地均按真实物种；只以 DFT 媒介翻译而非照片写实。
[STYLE_FINGERPRINT] 与 KF01/KF02 完全一致的 DFT 旧纸蛋彩/哑光水粉、朴拙干净描线、柔哑旧纸颜料、冷灰蓝/氧化绿与左后灰金晨光；真实四足动物被平面寓言式空间温柔翻译，毛发与皮肤用大块受控笔触，不做写实毛孔；清晰低噪、无惊悚残影。
[REFERENCE_ROLES] SH35_KF01/KF02=同镜头空间/相机/身份连续；阿白三照片=ABAI_WILD_IDENTITY/ANATOMY/FUR_PATTERN最高身份权威，DFT参考=STYLE_ONLY；配角四足目标=SUPPORTING_CAST_IDENTITY_LOCK_V2+TRANSFORMATION_STATE_LEDGER；ENV-01白模=SPACE_ONLY；SCALE_LEDGER+GROUP_ACTION_LEDGER SH35-KF03=TEXT_HARD_LOCK。旧配角板不定义四足结构。
[SUBJECT_AND_ACTION] 八只完整四足动物已落稳但行为不同：阿白在左中景看向出口；兔已靠近门口迈出短步；狐狸低头嗅地；狗侧身站稳、耳朵听风；绵羊转向长凳边但不接触衣物；驴刚迈出第一步；熊刚抬起头；大象最后在后景落稳，四足均承重。它们不排队、不站上凳，不触碰衣服或琴盒。凳上华服与地面闭合琴盒结构完整。
[CAMERA_AND_COMPOSITION] 21:9，35mm，同一连续轴线终点；摄影机约0.65m高、从 KF02 继续小幅降低并后退，以低机位宽景容纳物种真实体长；出口仍在左后、凳在右中、大象后景，阿白左中、兔门边；镜头不重新居中、不换轴，地平线和空间锚点连续。焦点落在阿白与出口方向，后景大象仍清楚。
[LIGHTING] 沿用前两锚点冷灰蓝室内光；左后门外灰金晨光略亮半级，轻勾四足轮廓，但不形成神圣光束；毛皮/象皮哑光，影子与四足接地一一对应，曝光稳定。
[SPACE_AND_CONTINUITY] ENV-01 几何、空钩、柜、凳、华服、琴盒位置不变；出口有足够通行净宽，兔先行、大象最后；所有动物与凳/衣服/盒保持可见间隔，无踩踏/穿插；直接接 SH36 的离门动作。
[SCALE_LOCK] 四足肩高严格按账本：兔0.25m、阿白0.28m、狐0.45m、狗0.60m、羊0.80m、驴1.25m、熊1.20m、象2.60m；同平面大象最大，兔/阿白最小，房间净高≥4.5m、门≥3.3×2.8m、通道≥3.2m，四足象可转身通过；长凳0.50m高，兔/猫不为可读性放大。
[GROUP_ACTION_LOCK] 阿白=看出口；兔=靠门迈步；狐=嗅地；狗=侧站听风；羊=转向凳边；驴=第一步；熊=抬头；象=最后落稳。禁止动物陈列、齐看镜头、齐步、同一低头或重复物种。
[NEGATIVE] no clothes, hats, shoes, buttons, instruments carried, human hands/wrists, biped shoulders, upright stance, hybrid anatomy, horror residue, pain, gore, exposed flesh, extra/missing/fused limbs, wrong paws/hooves, duplicate cat/fox/elephant, cat-headed other species, animals on bench, stepping on garments/case, tiny elephant, giant rabbit/cat, small door, room scale collapse, photoreal fur, 3D, anime, mascot, glossy render, watercolor drift, magical glow, text/logo/watermark; no grain, speckles, muddy microtexture, sharpening halos, fake detail, noisy background or JPEG artifacts.
```

### SH35 多锚点连续性合同

```text
[SHOT_ID] SH35
[SHOT_INTENT] 在一个稳定、克制、无恐怖的连续镜头里，让八个无衣两足拟人动物以不同相位前移重心，最终成为各自真实四足野生动物；衣物与乐器留在原地。
[KEYFRAME_SEQUENCE]
01 | 0.0s | SH35_KF01 | 无衣两足起始；阿白前倾、兔蹲、熊扶凳、象鼻触地；摄影机35mm/约1.15m高。
02 | 2.5s | SH35_KF02 | 错峰过渡中段；不同角色前爪/前足承重程度不同；摄影机同轴降至约0.90m并小幅后退。
03 | 5.0s | SH35_KF03 | 全员真实四足且行为各异；阿白看出口、兔近门、象后景落稳；摄影机同轴降至约0.65m。
[TRANSITIONS]
01 -> 02 | 0.0–2.5s：先有克制呼吸和重心前倾，再按角色分配错峰让前爪/前足接地；肩胛、骨盆和躯干只在连续毛发轮廓内自然降低。衣物/琴盒/房间完全静止，无切镜、无光效、无疼痛或肢体增殖。
02 -> 03 | 2.5–5.0s：每个角色按不同节奏完成物种真实四足结构与承重，保持毛色/脸/角/牙/耳/尾身份；摄影机继续同轴小幅降低后退，最终让出口成为行动方向。不得同时落稳、不得跳相位、不得重绘空间。
[STORYBOARD_SHEET] 三帧分别通过语义、解剖、尺度和清晰度 QA 后，以原图无再生成地合成 `08_generation/jobs/final_frames_v2/storyboard_sheets/SH35_NUMBERED_SHEET.png`；左至右明确 01、02、03，源帧比例/色彩/裁切不变。
```

### AIGC IMAGE-TO-VIDEO PROMPT — SH35

```text
[STYLE_FINGERPRINT] 严格继承 SH35 三张编号锚点共同的 DFT 旧纸蛋彩/哑光水粉：朴拙干净手绘边缘、柔哑不透明颜料、受控旧纸触感、冷灰蓝/氧化绿/灰金晨光、寓言式平面空间与可信房间尺度；角色形态用清晰大轮廓连续变化，低噪、无恐怖细节。
[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the exact and matching art style of KF01, KF02 and KF03 in every interpolated frame. Treat KF01 as immutable start, KF02 as mandatory ordered midpoint and KF03 as immutable terminal state. Animate the same artwork; do not reinterpret, redraw, beautify, simplify or replace art direction. Preserve identity marks, species, palette, edges, paper/paint texture, lighting, room geometry, props, depth and scale. Only the explicitly authorized body-weight/anatomy transition and slow same-axis camera height change may evolve.
[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal, 3D/CGI, anime, mascot, glossy game art, watercolor/oil conversion, horror/body-horror, magical transformation VFX, grain, texture crawl, edge shimmer, palette pumping, face redraw or environment morph.
[NARRATIVE_TIME] TRANSFORMATION_BOUNDARY_START -> TRANSFORMATION_IN_PROGRESS -> AFTER_FINAL_PERFORMANCE_WILD_DEPARTURE；全片 01:47–01:52。
[CHARACTER_STATE_LOCK] 起点=阿白 ABAI_PERFORMANCE_DRESS_PHOTOLOCK + 全体 PERFORMANCE_BIPED_PRIVATE_DRESS 的无衣两足边界；终点=阿白 ABAI_WILD_RETURN_PHOTOLOCK + 全体 WILD_RETURN_QUADRUPED；身份毛色、角牙耳尾与一物种一实例全程锁定。
[STATE_TRANSITION_RULE] 仅 SH35 的0.8–5.0s授权单向两足到四足转换；必须依序经过三锚点，衣物/琴盒不参与；5.0s后永久锁定 WILD_RETURN_QUADRUPED。
[SHOT_ID] SH35
[KEYFRAME_SEQUENCE] 01 | 0.0s | SH35_KF01 | 无衣两足、不同预备相位；02 | 2.5s | SH35_KF02 | 不同物种不同承重相位；03 | 5.0s | SH35_KF03 | 完整真实四足且行为各异。
[TRANSITIONS] 01 -> 02 | 重心前移、关节自然折叠、前爪错峰接地，无恐怖与肢体增殖；02 -> 03 | 各物种按不同节奏完成真实四足结构，房间、衣物、琴盒、身份与轴线不重置。
[STORYBOARD_SHEET] 08_generation/jobs/final_frames_v2/storyboard_sheets/SH35_NUMBERED_SHEET.png
[DURATION] 5.0s
[DURATION_RATIONALE] 三阶段转化包含起始预备、不同相位的承重转换和真实四足落稳，并需无痛、无跳帧地经过 KF02；5 秒是可读最短长度。三锚点与缓慢同轴降机能抑制形体漂移，必须保持一个连续镜头。
[TIMELINE]
0.0–0.8s: 表演：精确匹配 KF01。八个无衣两足角色保持不同预备姿势，只出现呼吸、耳/尾微动；衣物和琴盒静止。摄影机35mm、约1.15m高、同一轴线开始极慢下沉/后退；焦点在阿白、兔、熊，冷灰蓝/灰金光与曝光锁定。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
0.8–1.8s: 表演：阿白重心前移并让一只前爪接近地面；兔先完成蹲低；狗放低第一只前爪；象鼻触地后前足开始承重；熊从扶凳转向地面。狐狸、羊、驴仍较晚相位。身体轮廓只通过关节自然折叠和毛发遮蔽连续改变，无拉伸/痛苦。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
1.8–3.0s: 表演：平滑经过并在约2.5s准确匹配 KF02：阿白单前爪承重、兔四爪着地、狐单侧前爪前伸、狗双前爪承重而后躯未完成、羊前低后高、驴双膝近地、熊双前爪稳定、象前足稳后躯下沉。摄影机同轴降至约0.90m并小幅后退；房间/衣物/琴盒像素位置连续。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
3.0–4.2s: 表演：各物种继续以不同节奏完成肩胛/骨盆/脊柱与四肢比例；兔最先向门迈小步，狐开始嗅地，阿白第二只前爪落稳，狗侧身，羊/驴/熊依次落稳，大象最后完成。阿白照片斑纹与每个配角身份不漂移，衣物/道具不接触身体。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
4.2–5.0s: 表演：精确收束到 KF03：阿白看出口、兔近门、狐嗅地、狗侧站、羊转向凳边、驴迈第一步、熊抬头、象后景落稳。摄影机降至约0.65m并平滑停止，门外灰金光只轻亮半级；最后0.25s稳定持有，全部四足真实承重。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
[CONTINUITY_LOCKS] KEYFRAME ORDER 01→02→03，三帧均须被经过；唯一阿白和七个不同配角物种；阿白照片毛斑/灰绿眼/深灰尾；配角毛色/角/牙/耳/体型；ENV-01门/通道/凳/柜/空钩；华服和闭合琴盒不动且不融合；35mm同轴下降/后退、真实尺度、无切镜。
[NEGATIVE] no skipped/misordered keyframe, cut, flash, dissolve, camera reset, whip, zoom, simultaneous identical kneel, horror, pain, screaming, gore, bone/flesh exposure, melting, rubber stretching, twisting, limb sprouting/disappearing, human hands/wrists, hybrid residue, duplicate species, second cat, cat-like other animals, identity/fur-pattern drift, clothing/prop fusion, animals on garments/bench, room morph, scale pumping, flicker, geometry boil, style drift, text/logo/watermark.
[AUDIO] 仅环境声/音效：呼吸、毛皮与地面轻擦、不同体重的前爪/蹄/足错峰接地、长凳轻吱、远风和门外晨间环境；不使用骨裂/惨叫等恐怖声音；无音乐/BGM/配乐、无歌词或对白。《The Masterplan》只在后期剪辑使用。
```

---

## SH36｜四足动物离开更衣室

### IMAGE PROMPT — SH36

```text
[NARRATIVE_TIME] AFTER_FINAL_PERFORMANCE_WILD_DEPARTURE；全片 01:52，承接 SH35-KF03，八只动物第一次以完成的野生四足状态穿门进入空街。
[CHARACTER_STATE_LOCK] 全员=WILD_RETURN_QUADRUPED：阿白=ABAI_WILD_RETURN_PHOTOLOCK，唯一真实四足长毛白猫，照片锁灰绿眼、粉鼻、浅粉内耳、非对称灰黑头顶天然斑、背至后躯连续鞍状灰黑斑、深灰蓬尾；兔=灰米真实兔、一耳略弯；狐=赤褐真实赤狐、白下颌蓬尾；狗=棕黑粗毛垂耳中型犬；羊=灰白卷毛小弯角绵羊；驴=灰褐长耳驴；熊=深棕宽体四足熊；象=灰蓝短牙真实四足大象、最大体量。全部无衣、无乐器、无手腕/可抓握前爪、无拟人肩线，一物种一实例。
[STATE_TRANSITION_RULE] 转化已完成并永久锁定；本镜头及后续禁止任何角色直立、穿衣、持物或回到中间态。只允许物种真实四足步态、停听和出门。
[INTENTIONAL_REALITY_EXCEPTIONS] 无新的现实例外。所有四足结构、步态、接地、门洞通行和相对尺度服从真实物种；DFT 仅是媒介翻译。
[STYLE_FINGERPRINT] DFT 旧纸蛋彩/哑光水粉，朴拙干净描线、柔哑不透明颜料、受控旧纸触感；冷灰蓝更衣室向灰金清晨空街过渡，氧化绿/褪砖红做建筑基底，亮度比参考高一档；真实四足轮廓以平面寓言语言简化但解剖准确；门/通道/街道深度可信，清楚大形、低噪，不用写实毛孔或随机毛丝。
[REFERENCE_ROLES] DFT_DIRECTOR_REFERENCE=STYLE_ONLY；SH35_KF03=最高优先级角色身份/四足形态/房间位置/光色连续；阿白三照片=ABAI_WILD_IDENTITY/ANATOMY/FUR_PATTERN；配角四足=SUPPORTING_CAST_IDENTITY_LOCK_V2+TRANSFORMATION_STATE_LEDGER；ENV-01_WHITEBOX=SPACE/CAMERA_ONLY；SCALE_LEDGER+GROUP_ACTION_LEDGER SH36=TEXT_HARD_LOCK。旧两足板只限已授权身份色彩，不提供四足结构或动作。
[SUBJECT_AND_ACTION] 低机位宽景捕捉不同离开相位：灰米兔已先穿过门槛进入街面；赤狐贴左墙轻快掠过；棕黑狗在门内停半步侧耳听风；绵羊与驴以不同步幅错开；熊低头慢走；四足大象最后在房间后方对准宽门、尚未到门槛；阿白在中后景看向门外，晚于兔但不最后。每只动物行为、速度、朝向和高度不同，不列队。
[CAMERA_AND_COMPOSITION] 21:9，35mm感，摄影机约0.38m高，位于更衣室内靠门侧、略低于狗肩，朝门外空街看；门框构成中央偏左的深景框，兔已在门外左前方，狐贴墙，大象位于右后房间深处，阿白中后景由白毛和深灰尾可辨；凳上华服和闭合琴盒只在右侧远中景留下少量连续性，不被动物踩到。焦点覆盖门槛、兔/狐与阿白，后景大象仍清楚；不做动物陈列图。
[LIGHTING] 左前门外灰金晨光作柔主光，室内冷灰蓝高窗光作填光；动物轮廓有轻微灰金边缘，阿白白毛不过曝、象皮/熊毛不发黑；室内华服色块逐渐退到阴影，阴影方向与门光一致。
[SPACE_AND_CONTINUITY] ENV-01 门≥3.3×2.8m、通道与长凳位置延续 SH35；空钩、凳上华服、地面闭合琴盒仍在，不随动物移动；出门方向接空街，兔先、象最后，动物互不穿透/踩踏/堵门；镜面不入构图避免复制。
[SCALE_LOCK] 四足肩高：兔0.25m、阿白0.28m、狐0.45m、狗0.60m、羊0.80m、熊1.20m、驴1.25m、象2.60m；门≥3.3m高/2.8m宽、通道≥3.2m，象可自然通过且低于门楣；凳高0.50m作为猫/兔尺度参照，动物不得为可读性放大，脚爪/蹄与地面接触和阴影匹配。
[GROUP_ACTION_LOCK] 兔=先穿门；狐=贴墙掠过；狗=停听风；羊/驴=错开步幅；熊=慢走；象=最后对准宽门；阿白=中后景看门外。禁止八只动物齐步列队、同一奔跑姿势、同朝向或复制物种。
[NEGATIVE] no clothes, hats, shoes, instruments, trays/cups, human hands/wrists, biped stance, hybrid anatomy, horror residue, extra/missing/fused limbs, wrong paws/hooves, animal clipping, door collision, animals stepping on garments/case, duplicate cat/fox/elephant, recolored cats, line-up parade, tiny door/room, giant rabbit/cat, miniature elephant, photoreal, 3D, anime, mascot, glossy render, watercolor drift, magical glow, text/logo/watermark; no grain, random speckle, muddy microtexture, sharpening halos, fake detail, noisy background or JPEG artifacts.
```

### AIGC IMAGE-TO-VIDEO PROMPT — SH36

```text
[STYLE_FINGERPRINT] 严格继承 SH36 输入帧的 DFT 旧纸蛋彩/哑光水粉、朴拙干净边缘、冷灰蓝室内/灰金门外、柔哑旧纸与真实四足轮廓、可信门洞尺度、清晰低噪。
[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the input image's exact art style and every identity, species anatomy, fur marking, room/street geometry, prop, palette, light, edge, texture, depth and scale in every frame. Animate this same artwork only; do not redraw, restyle, beautify, simplify or replace it. Only assigned species-specific walking, pause/listening and a low slow camera follow may change.
[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal, CGI/3D, anime, mascot, glossy art, watercolor/oil conversion, horror, grain, texture crawl, edge shimmer, identity redraw or palette pumping.
[NARRATIVE_TIME] AFTER_FINAL_PERFORMANCE_WILD_DEPARTURE；全片 01:52–01:55；转换完成后的首次离室。
[CHARACTER_STATE_LOCK] 阿白=ABAI_WILD_RETURN_PHOTOLOCK；全体动物=WILD_RETURN_QUADRUPED；无衣无道具、真实物种四足结构与相对肩高锁定。
[STATE_TRANSITION_RULE] 转换已结束；本视频及后续禁止重新直立、穿衣或回到中间态，只允许真实四足离门动作。
[DURATION] 3.0s
[DURATION_RATIONALE] 需要读清兔先出、不同物种错峰过门、象最后通行的尺度证明；3 秒可完成一个低机位空间桥接并避免群像长时漂移。
[TIMELINE]
0.0–0.6s: 表演：匹配输入。兔完成跨门最后一步，狐开始贴墙前行；狗尚在门内侧耳，阿白刚把重心移向出口，大象后景对准门。摄影机35mm、0.38m高开始极慢向门跟进，焦点/曝光锁定。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
0.6–1.5s: 表演：狐掠过门侧，羊和驴以不同步幅前进，熊慢走半步；狗停住听一拍，阿白开始四足步行。兔已进入门外灰金光但不放大，衣物/琴盒保持静止。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
1.5–2.4s: 表演：狗恢复前行，阿白通过门内中段；象迈出一次沉重但自然的四足步，仍未堵住门；摄影机低位前移不超过画幅深度4%，门框产生自然视差，无摇晃/换轴。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
2.4–3.0s: 表演：前层兔/狐继续向街面分开，羊/驴/熊错峰接近门槛，阿白保持中层，大象最后稳步跟随。摄影机在2.7s减速，结尾门外街面成为主方向，0.3s稳定可剪。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
[CONTINUITY_LOCKS] SH35-KF03身份/四足结构/房间物件；兔先、象最后、阿白中后；ENV-01高宽门/通道；华服与琴盒留室内；一物种一实例、真实肩高、35mm低机位、无切镜。
[NEGATIVE] no cut, speed ramp, line-up, synchronized gait, duplicated species, second cat, biped return, clothing/prop appearance, human paws, limb mutation, animals clipping door/each other, room or scale morph, camera shake, flicker, warping, style drift, text/logo/watermark.
[AUDIO] 仅环境声/音效：兔/狐轻足、狗/羊/驴/熊错峰足音、大象低沉落步、门外风、室内轻回声与远处晨鸟极少量自然环境声；无音乐/BGM/配乐、无歌词或对白。《The Masterplan》后期另行剪入。
```

---

## SH37｜镇外荒野分路

### IMAGE PROMPT — SH37

```text
[NARRATIVE_TIME] AFTER_FINAL_PERFORMANCE_WILD_DEPARTURE；全片 01:55，所有动物已穿过空街到达镇外岔地，开始各奔不同生态方向。
[CHARACTER_STATE_LOCK] 全员=WILD_RETURN_QUADRUPED 且一物种一实例：阿白=ABAI_WILD_RETURN_PHOTOLOCK，照片锁真实四足长毛白猫/灰绿眼/粉鼻/头顶非对称灰黑天然斑/背部鞍状灰黑斑/深灰蓬尾；狐狸=赤褐背、白下颌、蓬尾；兔=灰米、小体型、一耳略弯；狗=棕黑粗毛垂耳；羊=灰白卷毛小弯角；驴=灰褐长耳；熊=深棕宽体；象=灰蓝短牙最大体量。无衣无道具无拟人前爪。
[STATE_TRANSITION_RULE] 四足状态永久锁定；本镜头只发生真实步行/钻入/分岔，不允许直立、穿衣、身体变形或重复实例。
[INTENTIONAL_REALITY_EXCEPTIONS] 无。航拍中的动物可被平面化为简洁可辨轮廓，但不得改变真实相对尺度或放大到房屋大小。
[STYLE_FINGERPRINT] DFT 旧纸蛋彩/哑光水粉航拍极远景，朴拙干净地形边缘、柔哑不透明颜料与受控旧纸触感；风沙土黄、灰蓝清晨、氧化绿灌木、褪砖红小镇、少量灰金天光，亮于参考一档；寓言式平面地图感与真实高空透视并存，动物是小而可辨的色/形点；大地大形清楚、低噪，不用密集砂粒。
[REFERENCE_ROLES] DFT_DIRECTOR_REFERENCE=STYLE_ONLY；SH36=动物身份/出城方向连续；阿白照片=ABAI_WILD_IDENTITY；配角四足=SUPPORTING_CAST_IDENTITY_LOCK_V2+TRANSFORMATION_STATE_LEDGER；SCALE_LEDGER+GROUP_ACTION_LEDGER SH37=TEXT_HARD_LOCK；旧 FIN-012A 与其他被退回荒野图不得作为构图、比例、动物数量或风格参考。
[SUBJECT_AND_ACTION] 高空俯瞰极远景同时看见镇缘、草坡、灌木、林线和干河床：狐狸向左上风沙草坡钻入；兔进入右下低灌木；熊沿上方暗绿林线慢走；大象沿右侧干河床远去；羊、驴、狗分别取三条不同小径；阿白在靠近镇缘的分岔点短暂停住，身体仍朝荒野、头略向镇方向。动物只是小而可辨的运动点，不围成队、不朝同一方向。
[CAMERA_AND_COMPOSITION] 21:9，24mm感，高空斜俯瞰极远景，摄影机等效高度约80–120m；小镇占左下不超过画面四分之一，荒野占主要负空间，干河床从右下引向远方，林线横在上部，路径形成多向分叉；阿白在镇缘附近可由乳白/深灰尾小点找到，但不放大。地平线不入画或只留极窄远缘，焦点为全景深，构图避免动物沿一条对角线排队。
[LIGHTING] 清晨低角度灰金光从画面右上方扫过地形，阴影细长但柔；小镇仍偏冷灰蓝，荒野略暖，形成“离开”而非末日强光；无神光柱、闪烁、浓雾或尘暴。
[SPACE_AND_CONTINUITY] 小镇红砖轮廓承接 SH36 空街，路径真实连接门外街道与镇外分岔；动物分向草坡/灌木/林线/干河床，各自生态去向可读；不新增河流、山脉、车辆或奇幻地貌。阿白尚未离开镇缘，为 SH38 回望保留位置。
[SCALE_LOCK] 航拍严格真实比例：动物与住宅、路灯、道路宽度关系按深度缩小；同一地面四足象最大但仍远小于一栋住宅占地，猫/兔只是更小点；一层檐口3.3–3.8m、两层6.5–8m、主街10–14m作为建筑/道路参照；禁止为可辨性放大动物，可用颜色和路径分离增强可读性。
[GROUP_ACTION_LOCK] 狐=钻草坡；兔=入灌木；熊=走林线；象=沿干河床；羊/驴/狗=三条不同岔路；阿白=镇缘短停。八个不同目标方向与速度，禁止全员奔向同一地平线、复制狐狸/象/猫或排成放射状等距图标。
[NEGATIVE] no animals larger than houses, no miniature town, no giant cat/rabbit/elephant, no duplicated fox/cat/elephant, no repeated animal icons, no all-running-same-direction, no line-up or perfect radial symmetry, no clothes, instruments, biped poses, human paws, hybrid anatomy, tiny toy buildings, fantasy mountains, flood, dust storm, apocalypse, photoreal, 3D, anime, mascot, glossy render, watercolor drift, horror, text/logo/watermark; no film grain, sand-noise field, random speckles, muddy microtexture, sharpening halos, fake detail, noisy background or JPEG artifacts.
```

### AIGC IMAGE-TO-VIDEO PROMPT — SH37

```text
[STYLE_FINGERPRINT] 严格继承 SH37 输入帧的 DFT 旧纸蛋彩/哑光水粉航拍语言：朴拙干净地形边缘、柔哑旧纸颜料、土黄/灰蓝/氧化绿/灰金、寓言地图感与真实比例、清晰低噪大地形。
[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve the input image's exact art style and every animal identity, terrain, town geometry, path, palette, lighting, edge, texture, depth and scale in every frame. Animate this same artwork only; do not redraw, restyle, beautify or replace it. Only short species-specific path motion and a minimal aerial rise may change.
[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal drone footage, CGI/3D, anime, mascot, glossy game art, watercolor/oil conversion, horror, grain, texture crawl, edge shimmer, animal icon redraw or palette pumping.
[NARRATIVE_TIME] AFTER_FINAL_PERFORMANCE_WILD_DEPARTURE；全片 01:55–01:57；镇外荒野分路。
[CHARACTER_STATE_LOCK] 阿白=ABAI_WILD_RETURN_PHOTOLOCK；全体动物=WILD_RETURN_QUADRUPED；八种唯一四足动物、毛色与真实相对尺度锁定。
[STATE_TRANSITION_RULE] 本视频无状态转换；只允许按既定生态方向分路，禁止直立、穿衣、复制或尺度放大。
[DURATION] 2.0s
[DURATION_RATIONALE] 这是一个快速地理标点：需在两秒内明确八只动物走向不同生态方向并留下阿白停顿；长镜会让极小动物身份和比例漂移。
[TIMELINE]
0.0–0.5s: 表演：匹配输入高空构图。狐狸/兔先分别接近草坡与灌木；象沿干河床迈一步；阿白仍停在镇缘。摄影机24mm、高空斜俯、全景深开始极轻上升；地形/曝光锁定。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
0.5–1.3s: 表演：狐进入草坡遮挡一部分身体，兔钻入灌木，熊沿林线前进；羊/驴/狗分别沿不同小径错峰移动，象保持最慢且最大轮廓。阿白只转头向镇一小角度，身体不回走。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
1.3–2.0s: 表演：动物间距进一步拉开但仍维持真实小尺度；摄影机上升仅造成轻微地形视差，随后减速定住。阿白保持镇缘短停，作为 SH38 切入点；最后0.2s稳定。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
[CONTINUITY_LOCKS] 八种唯一动物、四足身份与真实相对尺度；各自固定路径/目标生态；阿白镇缘位置；小镇/道路/河床/林线不变；24mm高空轴线、无切镜。
[NEGATIVE] no cut, zoom dive, camera spin, animal enlargement, icon duplication, path swapping, all animals same direction, second cat/fox/elephant, biped return, clothes/props, terrain morph, building shrink, scale pumping, flicker, warping, style drift, text/logo/watermark.
[AUDIO] 仅环境声/音效：高处风声、很远的不同足音几乎不可闻、草叶/灌木轻擦、干河床微砂声；无音乐/BGM/配乐、无歌词或对白。《The Masterplan》仅后期剪辑使用。
```

---

## SH38｜阿白回望后跑向晨光（一个连续镜头，两锚点）

### IMAGE PROMPT — SH38_KF01（编号 01／回望锚点）

```text
[NARRATIVE_TIME] AFTER_FINAL_PERFORMANCE_WILD_DEPARTURE；全片 01:57、SH38 0.0s；阿白留在镇缘最后回望一次，其他动物已经沿各路离开。
[CHARACTER_STATE_LOCK] 阿白=ABAI_WILD_RETURN_PHOTOLOCK 且为画面唯一可读角色：真实四足年轻长毛白猫，圆润猫脸、短口鼻、灰绿色自然比例眼睛、粉鼻、浅粉内耳，温暖乳白长毛，非对称烟灰/炭灰头顶天然毛斑，背部至后躯单块连续鞍状灰黑斑，深灰蓬松尾；无衣、无乐器、无拟人肩线/手腕、四爪承重。不可出现第二只猫或背景猫影。
[STATE_TRANSITION_RULE] WILD_RETURN_QUADRUPED 永久锁定；只允许自然回头、转身和奔跑，禁止直立、穿衣或再转形。
[INTENTIONAL_REALITY_EXCEPTIONS] 无。阿白四足解剖、回头幅度、接地、风与城镇尺度服从现实；DFT 是媒介而不是比例例外。
[STYLE_FINGERPRINT] DFT 旧纸蛋彩/哑光水粉结尾远景，朴拙干净手绘边缘、柔哑不透明颜料、受控旧纸触感；冷灰蓝空镇、褪砖红轮廓、风沙土黄荒野与灰金/微桃晨光，亮于参考一档；克制、苍凉但通向新生，不煽情不神圣化；平面寓言空间与真实猫/建筑比例并存，清晰大轮廓、低噪，细节集中在阿白照片斑纹与可见灰绿眼。
[REFERENCE_ROLES] 阿白三张照片=最高优先级 WILD_IDENTITY/ANATOMY/FUR_PATTERN；ABAI_DUAL_STATE_SHEET_V2_APPROVED=同一身份与项目内造型连续，不提供四足照片媒介；DFT_DIRECTOR_REFERENCE=STYLE_ONLY；FIN-012B.png=STORY/COMPOSITION_CANDIDATE_ONLY，若与照片身份、尺度或活动风格冲突则舍弃；SH37=镇缘位置/离开方向；SCALE_LEDGER=猫/城镇比例。所有旧黑毛撮、单条肋纹、全白尾和被退回四足群像均排除。
[SUBJECT_AND_ACTION] 四足阿白站在镇外土路与荒草交界，身体已朝画面左前方荒野，头从肩上自然回望右后方空镇；一只灰绿色眼睛接住最后一点旧金灯光，耳朵一前一后，深灰蓬尾低而蓬松，四爪稳稳接地。空镇只有安静建筑轮廓和最后一枚微弱灯点，不出现其他可读动物、人物或烟。
[CAMERA_AND_COMPOSITION] 21:9，50mm感，低机位远景，摄影机约0.25m高、位于阿白右后侧约6–8m，略低于猫眼；阿白位于左侧三分之一，身体朝左前、头回望右后，空镇占右后背景并明显小于荒野面积，左前方留大块晨光负空间为 KF02 奔跑路径；前景两三根虚焦荒草做轻框景，焦点锁阿白回望眼与头顶斑，背斑/尾巴清楚。固定同轴起点，不把猫放大成巨兽。
[LIGHTING] 右后空镇残灯给予阿白可见眼睛一个小而自然的旧金眼神光；左前方清晨灰金/微桃天光作柔逆光，冷灰蓝环境填光保留白毛层次；无圣光、光环、超自然发光或强镜头耀斑。
[SPACE_AND_CONTINUITY] 镇在右后、荒野在左前，承接 SH37 阿白停在镇缘；土路与草地真实连接，其他动物已离开且不回画面；KF02 中阿白将沿同一左前路径转身跑远，城镇和草丛位置必须连续。
[SCALE_LOCK] 四足阿白肩高约0.28m、体长/尾长按真实家猫；远处住宅檐口3.3–8m、路灯5–6m，阿白不得与房屋/门窗同高；前后景缩小、地平线与投影一致，荒草高度与猫爪/腹部关系真实。
[GROUP_ACTION_LOCK] 单角色镜头；禁止新增任何猫、狐狸、大象或人群剪影。远处若有不可辨动物点也应完全离开本构图，避免抢走阿白的最后停顿。
[NEGATIVE] no biped cat, clothes, violin, collar, human paws/wrists, pet-mascot pose, huge eyes, old black forelock, rib stripe, white tail, wrong eye color, extra/missing/fused legs, twisted neck, floating paws, duplicate cat, background cat silhouette, giant cat, miniature town, animal-sized houses, smoke, apocalypse, ruins explosion, divine beam, halo, magical glow, melodramatic tears, photoreal, 3D, anime, Disney mascot, glossy render, watercolor drift, horror, text/logo/watermark; no grain, random speckles, muddy fur microtexture, sharpening halos, fake hair detail, noisy background or JPEG artifacts.
```

### IMAGE PROMPT — SH38_KF02（编号 02／跑向晨光终止锚点）

```text
[NARRATIVE_TIME] AFTER_FINAL_PERFORMANCE_WILD_DEPARTURE；全片 02:00、SH38 3.0s；同一连续镜头末端，阿白已完成回头并真正跑向晨光。
[CHARACTER_STATE_LOCK] 身体状态=WILD_RETURN_QUADRUPED；与 KF01 完全同一 ABAI_WILD_RETURN_PHOTOLOCK：唯一真实四足长毛白猫，灰绿眼/粉鼻/浅粉内耳、非对称灰黑头顶天然斑、背至后躯连续鞍状斑、深灰蓬尾全部连续；无衣无道具，无拟人前爪。奔跑姿态必须符合真实猫科四足步态，四肢归属清楚。
[STATE_TRANSITION_RULE] 四足状态不变；只允许从 KF01 回望姿态连续转头、转肩/躯干并加速到自然跑步。不得切镜、瞬移、换体型或变成另一只猫。
[INTENTIONAL_REALITY_EXCEPTIONS] 无。跑步、毛发/尾巴惯性、爪地接触、投影和尺度全部现实；仅以 DFT 画法表现。
[STYLE_FINGERPRINT] 与 KF01 完全一致的 DFT 旧纸蛋彩/哑光水粉：朴拙干净边缘、柔哑旧纸颜料、冷灰蓝空镇/土黄荒野/灰金微桃晨光、克制苍凉与新生、平面空间和真实比例；清晰低噪，运动以稳定姿势与少量大形拖曳表现，不加颗粒或照片模糊。
[REFERENCE_ROLES] SH38_KF01=最高优先级同镜头身份/空间/光色/相机/起始姿态；阿白照片=WILD_IDENTITY/ANATOMY/FUR_PATTERN；DFT参考=STYLE_ONLY；SH37=荒野方向；SCALE_LEDGER=猫/建筑/荒草比例；FIN-012B 只影响 KF01 候选叙事构图，不能覆盖 KF02 身份或风格。
[SUBJECT_AND_ACTION] 同一只阿白已经转身，沿画面左前方土路跑向灰金晨光；身体呈自然低位猫科奔跑，前后腿分属清楚、至少两爪接地或处于可信腾跃相位，深灰蓬尾顺转身弧线平衡，鞍状背斑沿真实毛流保持。阿白比 KF01 稍向左前远离摄影机，空镇仍在右后背景，最后灯点微弱但未戏剧化熄灭。
[CAMERA_AND_COMPOSITION] 21:9，50mm，同一低轴线；摄影机从 KF01 约0.25m高沿左前方向平滑跟移小段并轻摇约8–12°，不换焦段/机位侧；阿白仍在左侧偏中但向晨光深入，右后空镇保留为较小轮廓，左前晨光负空间被奔跑路径占据一部分。焦点跟随阿白背斑与尾根，背景略软但建筑比例可读；终帧是稳定跟拍中的自然跑姿而非模糊剪影。
[LIGHTING] 左前晨光比 KF01 自然提高极小半档，在阿白毛边形成灰金轮廓；右后残灯不再提供正面眼神光，白毛仍有冷灰蓝填光和层次；无曝光泵动、神光、耀斑或超自然发光。
[SPACE_AND_CONTINUITY] 土路、荒草、空镇、地平线和光源方向与 KF01 连续；阿白沿既定左前路径远离，不穿越地形或瞬移；没有其他动物重新出现。结尾保留空镇为右后安静形状，荒野占主导。
[SCALE_LOCK] 阿白肩高与体长始终按真实家猫0.28m级别，不因跑远而变大；与荒草、土路、住宅/路灯透视关系连续；奔跑接地点和投影匹配，不漂浮、不穿地。
[GROUP_ACTION_LOCK] 单角色镜头，只有一个阿白；禁止背景复制猫、陪跑动物或同一身体残影。尾巴拖影只能是一个连续大形，不得读成第二尾。
[NEGATIVE] no identity change, second cat, ghost trail, duplicated legs/tail, wrong gray markings, black forelock, rib stripe, white tail, giant eyes, biped posture, clothing/violin/collar, human paws, impossible gallop, floating, teleport, motion-smear hiding anatomy, giant cat, shrinking town inconsistency, apocalypse, smoke, divine light, halo, photoreal, 3D, anime, mascot, glossy render, watercolor drift, horror, text/logo/watermark; no grain, speckles, muddy fur, sharpening halos, fake hair detail, noisy background or JPEG artifacts.
```

### SH38 多锚点连续性合同

```text
[SHOT_ID] SH38
[SHOT_INTENT] 在一个低机位连续镜头内，让真实四足阿白最后回望空镇一次，然后转身跑向晨光；结尾苍凉但明确走向新生。
[KEYFRAME_SEQUENCE]
01 | 0.0s | SH38_KF01 | 阿白身体朝左前荒野、头回望右后空镇；50mm/0.25m低机位；灰绿眼接残灯。
02 | 3.0s | SH38_KF02 | 同一阿白转身后沿左前土路自然跑向晨光；摄影机同轴小幅跟移/轻摇；空镇留在右后。
[TRANSITIONS]
01 -> 02 | 0.0–3.0s：先持有回望，再由头、肩、躯干、骨盆、四肢依次转向；阿白迈出第一步后平稳加速，摄影机低位同向跟移并轻摇，不切镜、不瞬移、不换猫。毛发/尾巴按惯性自然响应，城镇/地形/光色连续。
[STORYBOARD_SHEET] 两帧分别通过照片身份、四足解剖、比例和清晰度 QA 后，以原图无再生成地合成 `08_generation/jobs/final_frames_v2/storyboard_sheets/SH38_NUMBERED_SHEET.png`，左至右标 01、02，保留源帧比例/色彩/裁切。
```

### AIGC IMAGE-TO-VIDEO PROMPT — SH38

```text
[STYLE_FINGERPRINT] 严格继承 SH38-KF01/KF02 共同的 DFT 旧纸蛋彩/哑光水粉：朴拙干净手绘边缘、柔哑不透明旧纸颜料、冷灰蓝空镇/土黄荒野/灰金微桃晨光、克制苍凉与新生、平面寓言空间与真实猫/建筑比例、清晰低噪。
[STYLE_INHERITANCE_HARD_LOCK] Strictly preserve both numbered keyframes' exact and matching art style in every interpolated frame. Treat KF01 as immutable start and KF02 as immutable terminal state. Animate this exact same Abai and landscape; do not reinterpret, redraw, beautify, simplify or replace art direction. Preserve photo-locked identity/fur markings/anatomy, medium, edges, texture, palette, lighting, town/terrain geometry, depth, scale and composition density. Only natural head/body turn, running and low same-axis camera follow may evolve.
[STYLE_NEGATIVE] Strictly do not change or replace the source image art style. No photoreal cat/video, CGI/3D, anime, mascot, glossy game art, watercolor/oil conversion, horror, divine fantasy, model-default redraw, grain, texture crawl, edge shimmer, palette pumping, face/fur redraw or background morph.
[NARRATIVE_TIME] AFTER_FINAL_PERFORMANCE_WILD_DEPARTURE；全片 01:57–02:00；阿白最后回望并跑向晨光。
[CHARACTER_STATE_LOCK] 唯一阿白=ABAI_WILD_RETURN_PHOTOLOCK；身体状态=WILD_RETURN_QUADRUPED；三张照片锁脸、灰绿眼、天然头顶斑、鞍状背斑、深灰尾与真实四足解剖全程不变。
[STATE_TRANSITION_RULE] 本视频无身体状态转换；只允许同一四足阿白由回望连续转身并自然起跑，禁止直立、换猫、穿衣或瞬移。
[SHOT_ID] SH38
[KEYFRAME_SEQUENCE] 01 | 0.0s | SH38_KF01 | 身体朝左前荒野、头回望右后空镇；02 | 3.0s | SH38_KF02 | 同一阿白沿左前土路跑向晨光、空镇留在右后。
[TRANSITIONS] 01 -> 02 | 头、肩、躯干、骨盆、四肢依次转向并起跑；摄影机低位同轴跟移，无切镜、瞬移、身份或地形重置。
[STORYBOARD_SHEET] 08_generation/jobs/final_frames_v2/storyboard_sheets/SH38_NUMBERED_SHEET.png
[DURATION] 3.0s
[DURATION_RATIONALE] 回望需要短暂持有，随后一次真实转身和起跑完成终局动作；3 秒是音乐短片结尾的克制长度，两锚点能锁住身份、方向和终态，无需拆镜。
[TIMELINE]
0.0–0.7s: 表演：精确匹配 KF01。阿白四爪稳地、身体朝左前、头回望右后，灰绿眼保留自然残灯点；耳尖/胸毛/尾毛被风轻动。摄影机50mm、0.25m高固定起始轴线，焦点锁眼睛/头顶斑，曝光保持。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
0.7–1.4s: 表演：阿白先把头转回左前，随后肩线和前躯自然跟随，深灰尾向反方向小摆平衡；前爪迈出第一步，后躯尚完成转向。摄影机开始低位同向平滑跟移并轻摇不超过8–12°，无切镜/变焦。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
1.4–2.4s: 表演：阿白完成躯干/骨盆转向并从步行加速为真实猫科小跑，四肢交替清楚，鞍状背斑与尾巴不漂移；摄影机匹配速度，使阿白保持左中区域，空镇自然向右后产生小视差。晨光仅提高极小半档。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
2.4–3.0s: 表演：阿白进入 KF02 的稳定低位跑姿，继续沿左前土路远离；摄影机跟移速度逐渐匹配阿白，画面相对运动减小并在3.0s准确贴合 KF02，可作为干净终帧。城镇仍是右后安静轮廓，无戏剧熄灯。；摄影：镜头、构图、焦点、曝光与照明沿用本区间原有说明并保持连续。
[CONTINUITY_LOCKS] KEYFRAME ORDER 01→02；唯一阿白、三照片锁脸/灰绿眼/天然头顶斑/鞍状背斑/深灰尾；WILD_RETURN_QUADRUPED；镇右后/荒野左前/同一路径；50mm、0.25m低轴线同向跟移、真实尺度、无切镜。
[NEGATIVE] no skipped/reversed keyframe, cut, teleport, sudden sprint, camera whip/zoom/roll, identity or fur-pattern drift, second cat, ghost trail, duplicated legs/tail, biped return, clothing/violin, human paws, anatomy blur, floating, town shrink/morph, giant cat, flicker, warping, style drift, divine glow, text/logo/watermark.
[AUDIO] 仅环境声/音效：近处晨风、荒草摩擦、阿白轻而错峰的四足爪地声、毛发/尾巴风响，空镇方向只留极弱金属余响；不嵌入音乐/BGM/配乐，不生成人声或歌词。《The Masterplan》仅由后期剪辑铺设。
```

---

## 包内自检结果

| 检查项 | 结果 |
|---|---|
| 镜头范围 | SH27–SH38，共 12 个剪辑镜头 |
| 时间覆盖 | 01:24–02:00，共 36.0s；顺序连续，无缺口/重叠 |
| 图像锚点 | 共 16 张：单锚点 9 镜；SH28=2、SH35=3、SH38=2 |
| 视频提示 | 每镜 1 条，共 12 条；每条均从 0.0s 覆盖至准确终点 |
| 图像合同字段 | 每个锚点均含 NARRATIVE_TIME、CHARACTER_STATE_LOCK、STATE_TRANSITION_RULE、INTENTIONAL_REALITY_EXCEPTIONS、STYLE_FINGERPRINT、REFERENCE_ROLES、SUBJECT_AND_ACTION、CAMERA_AND_COMPOSITION、LIGHTING、SPACE_AND_CONTINUITY、SCALE_LOCK、GROUP_ACTION_LOCK、NEGATIVE |
| 视频合同字段 | 每镜均先写动态 STYLE_FINGERPRINT、STYLE_INHERITANCE_HARD_LOCK、STYLE_NEGATIVE，再写 DURATION、DURATION_RATIONALE、无缝 TIMELINE、CONTINUITY_LOCKS、NEGATIVE、AUDIO |
| 多锚点合同 | SH28/SH35/SH38 均为一个 shot_id、明确 01/02(/03) 顺序、连续过渡与待生成编号联系板路径 |
| 身份与状态 | 阿白照片锁；配角 V2 活动身份锁；SH27–SH34 两足演出态，SH35 唯一转换，SH36–SH38 永久四足野生态 |
| 比例 | 每个镜头均绑定 SCALE_LEDGER；无已声明比例例外；远景动物不得大于建筑 |
| 群像动作 | 每个可读群像逐角色分配不同动作/相位/层次；单角色/无人物镜头明确禁止新增复制角色 |
| 视觉质量 | 全部 21:9 DFT 旧纸蛋彩/哑光水粉、清晰低噪；显式禁止颗粒噪点、假微细节、锐化光晕与压缩伪影 |
| 音频 | 只写环境声/音效；所有镜头明确无音乐/BGM；《The Masterplan》仅后期剪辑 |

生成执行仍需遵循活动镜头清单的导演审批状态；本文件不把候选参考自动晋升为成片。
