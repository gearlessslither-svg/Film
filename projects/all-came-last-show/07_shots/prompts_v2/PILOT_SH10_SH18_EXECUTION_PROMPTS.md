# V2 高风险试片执行提示词：SH10 + SH18

状态：`authorized_for_generation_by_full_project_goal_2026-07-17`

工具：Codex 内置 `image_gen`。所有参考图都只按下列角色使用，禁止跨角色泄漏。

## SH10 — 第一次脱工装／群像动作试片

### Reference roles

- `04_lookdev/references/DFT_DIRECTOR_REFERENCE.png`：只锁旧纸蛋彩／哑光水粉媒介、朴拙边缘、深青赭金、寓言式平面空间；不继承具体人物、建筑或故事物件。
- `05_asset_bible/approved/ABAI_DUAL_STATE_SHEET_V2_APPROVED.png`：只锁阿白照片身份翻译、两足比例和深蓝工装；不得复制成第二只猫。
- `08_generation/jobs/supporting_cast_v1/outputs/SUPPORTING_CAST_A_V1_attempt_001.png` 与 `SUPPORTING_CAST_B_V1_attempt_001.png`：只锁配角脸、毛色、体型、两足比例和工装；不继承乐器、托盘、杯子、排排站或画板背景。
- `08_generation/jobs/environment_settings_v1/outputs/ENV-01_LOCKER_ROOM_SETTING_attempt_002.png`：只锁更衣室材质、柜／钩／凳关系和色调。
- `08_generation/jobs/environment_whiteboxes_v1/outputs/ENV-01_WHITEBOX_3VIEWS_attempt_002.png`：只锁空间与机位，不转移 3D 风格。

### IMAGE PROMPT

```text
Use case: illustration-story
Asset type: final cinematic keyframe for a 21:9 two-minute music short

[NARRATIVE_TIME] 00:28–00:32, FIRST_CHANGE inside the public locker room, after the last factory shift and before any private clothes or instruments appear.
[CHARACTER_STATE_LOCK] Exactly eight distinct anthropomorphic biped workers: one and only one Abai long-haired white cat with gray-green eyes, pink nose, asymmetric natural charcoal crown patch and dark gray fluffy tail; one elderly gray-white sheep with small curved horns; one large gray-blue elephant with two short tusks; one lean gray-brown donkey with long ears; one rough brown-black floppy-eared dog; one faded red fox with white jaw and fluffy tail; one small gray-beige rabbit with one slightly bent ear; one broad dark-brown bear. All begin in the same correctly scaled dark navy worn cotton factory uniform. No human hands; only species-appropriate simplified furry paws or hooves.
[STATE_TRANSITION_RULE] This frame shows only the first removal of factory workwear. Bodies remain fully stable biped anthropomorphic animals. No private performance clothes yet, no quadruped posture, no transformation, no wild state.
[INTENTIONAL_REALITY_EXCEPTIONS] none. DFT depth flattening is stylistic only; anatomy, contact, load, scale and perspective remain plausible.
[STYLE_FINGERPRINT] Preserve the supplied DFT reference’s old yellowed-paper tempera and matte gouache language: hand-painted opaque color fields, fine slightly naive dark contour work, restrained paper tooth, deep teal-blue shadows, faded ochre and brick accents, low saturation, quiet fairy-tale absurdity, flattened but readable depth, large simple silhouettes before detail. One stop brighter and gentler than the darkest reference panels. Clean low-noise finish, controlled detail density, no photographic rendering.
[SUBJECT_AND_ACTION] A high wide ensemble moment with eight different micro-actions, all at different phases: bear seated on the near bench pulling off one boot; sheep standing left removing the cap with one hoof; rabbit at a low hook hanging one sleeve of the jacket; elephant by the tall doorway loosening only one shoulder strap; dog mid-right rolling one cuff outward; donkey bending to untie one shoe; fox paused beside the mirror looking at its own collar without touching it; Abai near the center locker looking down while undoing one lower button. Some uniforms remain partly worn, some partly removed, none fully naked. Serious, slow, unshowy expressions. Each silhouette and hand/paw height is different.
[CAMERA_AND_COMPOSITION] Exact 21:9 landscape. High three-quarter wide master, perceptual 30–35mm lens, camera about 2.8m high from the room’s front-left corner, looking diagonally toward the locker wall and tall exit. Three readable layers: near bench and seated bear foreground; Abai, sheep, rabbit, dog, donkey and fox staggered through midground; elephant and oversized doorway in background. Keep negative space around each silhouette; no lineup, no centered symmetry, no repeated pose. Full bodies and floor contacts visible. Camera locked, no Dutch angle.
[LIGHTING] Cool gray dawn daylight enters from two tall windows on frame left; three warm ochre industrial pendant lamps provide soft top practicals. Gentle fill from pale plaster, subtle rim on fur edges, matte short shadows grounded under every foot. Elephant slightly darker in the doorway but fully readable. No dramatic spotlight, glow or horror contrast.
[SPACE_AND_CONTINUITY] Use the approved locker-room geometry: tall arched windows left, dark teal metal lockers and multi-height hooks on the far wall, two long reinforced wooden benches, wide exit right. The room is orderly, worn, not filthy. Clothing folds remain on benches or hooks, not scattered. No instruments, cases, drinks, signs or text.
[SCALE_LOCK] Ceiling at least 4.5m; right exit clear opening at least 3.3m high x 2.8m wide; elephant about 2.55m biped and visibly fits with clearance; lockers 2.2–2.4m; bench seat about 0.5m; hooks at low, middle and high levels. Door, windows and lockers must remain larger than same-plane small animals. Show at least two scale anchors: elephant-to-door clearance and rabbit-to-low-hook/bench relationship.
[GROUP_ACTION_LOCK] Exactly follow the eight distinct actions above. No more than two characters may share the same action verb, hand/paw position, torso direction or action phase. Foreground seated, midground standing/bending, background strap-loosening create different rhythms. One readable pause (fox) among active gestures.
[NEGATIVE] No duplicated cat, fox, elephant or any species; no background cat silhouettes; no all-cat crowd; no identical chest-level hand gesture; no everyone holding clothes; no synchronized undressing; no lineup or character-sheet composition; no extra limbs, human fingers, fused paws, impossible joints, floating feet, body intersections or clothes fused to fur; no miniature door, toy furniture, animal larger than same-plane architecture, broken perspective; no private clothes, violin, accordion, trumpet, drum, tray, glasses, text, logo or watermark; no photorealism, digital concept art, 3D render, anime, Disney mascot, glossy game art, watercolor wash or horror. Clean high-resolution image with low noise, controlled detail density, crisp readable silhouettes, smooth flat areas, natural edge transitions, no random speckle, muddy micro-texture, sharpened halos, fake pixel detail or JPEG artifacts.
```

## SH18 — 十字路口赴约／尺度试片

### Reference roles

- 同一 DFT 风格参考：只锁媒介与画面语言。
- 阿白批准板：只锁阿白身份、演出服和携带的闭合琴盒；不复制角色。
- 配角 A/B 旧板：只锁狐狸、大象、兔、熊的身份和演出服装，不继承乐器陈列、托盘、杯子或排排站。
- `FIN-006` 只作为反例：不得继承其微缩门窗、尺度漂移或角色散开方向。

### IMAGE PROMPT

```text
Use case: illustration-story
Asset type: final cinematic keyframe for a 21:9 two-minute music short

[NARRATIVE_TIME] 00:56–00:59, TRAVEL_TO_LAST_PERFORMANCE, after every character has changed into private performance clothes and before reaching the central square.
[CHARACTER_STATE_LOCK] Exactly five principal anthropomorphic biped animals and no duplicate: faded red fox in deep-teal short jacket and old-gold scarf; largest gray-blue elephant in a slightly tight but intact faded brick-red formal coat; small gray-beige rabbit with one bent ear in cream shirt and old-red skirt-trousers; broad dark-brown bear in old-mustard shirt and peacock-blue vest; one and only one Abai long-haired white cat in cream shirt, worn ochre-red vest and deep-teal short coat, carrying one closed correctly scaled violin case. Stable biped structure, species paws/hooves, no human hands.
[STATE_TRANSITION_RULE] No state change in this shot. All remain PERFORMANCE_BIPED_PRIVATE_DRESS; no factory uniform, no undressing and no quadruped form.
[INTENTIONAL_REALITY_EXCEPTIONS] none. The high view and DFT flattening do not permit scale enlargement or miniature buildings.
[STYLE_FINGERPRINT] Old yellowed-paper tempera and matte gouache DFT fairy-tale frame: opaque hand-painted shapes, fine naive dark contours, restrained paper tooth, deep teal night-blue, faded brick, warm old-gold lamps, low saturation, quiet solemn absurdity, flattened yet intelligible streets and depth. Large clean shapes, controlled detail, one stop brighter than the darkest DFT reference. No photographic or digital-render finish.
[SUBJECT_AND_ACTION] A northwest industrial town crossroads at blue-hour. All five characters move toward the same warm-lit central-square opening near the upper-center of the frame from four different roads: fox fast-walks in from left lane, body angled toward the light; elephant takes a slow heavy step from the bus-stop road at upper-left; rabbit short-runs inward from lower-right; bear walks down from the upper road; Abai is farthest behind on the lower-left road, walking inward with the closed violin case low at one side. Their paths converge; nobody walks away from the light. Serious calm expressions, different stride phases and body orientations.
[CAMERA_AND_COMPOSITION] Exact 21:9 landscape, high oblique town view from about third-floor height, perceptual 28–32mm lens, not a vertical drone shot. Crossroads forms a clear X leading to the lit square; two-story red-brick houses occupy both sides and dominate the frame. Characters are small, placed on separate depth planes, never enlarged for readability. Strong foreground roof/parapet corner on one edge, middle crossroads, background square light and cold smokeless factory chimney. Keep each animal silhouette separated by road geometry.
[LIGHTING] Cool gray-blue ambient sky and matte street shadow; practical lamps at 2700K form small warm pools and one clear destination glow. No magical beams. Long soft shadows align consistently away from lamps; windows are sparse and dim. Exposure preserves dark teal streets without crushing silhouettes.
[SPACE_AND_CONTINUITY] Same stopped, intact-but-worn industrial town: red-brick dormitories, old bus shelter, ten-to-fourteen-meter main street, narrow side lanes, distant central square and one cold smokeless chimney. No ruins, no apocalypse, no modern cars, no Manchester/UK symbols. The road direction must clearly continue toward SH20’s square geography.
[SCALE_LOCK] Two-story eaves 6.5–8m; one-story eaves 3.3–3.8m; public doors 2.6–2.9m; street lamps 5–6m; bus shelter roof 3.3–3.8m; elephant about 2.55m and visibly lower than one-story eaves and lamp heads; rabbit and Abai much smaller than doors on the same plane. Same-plane animals may not reach a full floor height. Every farther character shrinks consistently toward the single perspective system. Show at least two scale anchors: elephant beside the bus shelter/lamp and rabbit beside a residential door/window module.
[GROUP_ACTION_LOCK] Fox fast walk, elephant slow step, rabbit short run, bear steady walk and Abai late walk all use different stride phases, speeds, directions and body rhythms while converging. No queue and no synchronized gait.
[NEGATIVE] Do not reuse FIN-006’s miniature doors or confused travel directions. No character as large as a house, no animal taller than a story, no toy town, no inconsistent vanishing scale, no giant rabbit, no tiny elephant, no forced-perspective exception; no duplicate fox, bear, elephant, rabbit or cat; no background cats; no extra crowd; no factory uniform; no open violin or other visible instrument; no tray, cups, signs, pseudo-text, logo or watermark; no extra limbs, human fingers, fused paws, floating feet or impossible shadows; no photorealism, 3D, anime, Disney mascot, glossy concept art, watercolor wash, horror, magic or apocalypse. Clean high-resolution image with low noise, controlled detail density, crisp readable silhouettes, smooth flat areas, natural edge transitions, no random speckle, muddy micro-texture, sharpened halos, fake pixel detail or JPEG artifacts.
```
