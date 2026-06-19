# Codex Card Image Handoff / Codex 卡片图片生成包

这是电影项目的概念/分镜卡片图片生成包，不是投资策略卡片。请调用当前聊天里的真实生图能力，只为 Tasks 中列出的目标电影卡片生成图片。不要因为上下文里有其他卡片，就自动生成它们。

## Codex Run Mode / 执行模式
- 目标是卡片级生成：如果 Tasks 里只有 1 张卡，就只生成 1 张；有多张才批量生成。
- 生成前可做电影级提示词优化，强化构图、光影、材质、角色连续性和负面约束。
- revision_note 是本轮精修意见，优先级高于长期 notes/prompt_notes；不要把一次性修改写死成永久设定。
- spatial_logic 和 spatial_logic_checks 是硬性空间检查；生成提示词前先核对门内外方向、人物视线、屏幕位置、机位轴线和道具结构。若情绪描述与空间逻辑冲突，空间逻辑优先。
- Concept task 的 scope/act_id/act_context 决定它是全项目设定还是某一幕设定；幕级概念只继承并服务对应 act 的上下文。
- Context cards、global references、nearby storyboard cards、related assets 只用于风格和连续性参考，不是生成目标。
- 每个 task 的 inherited_references/all_references 是必须读取的继承参考；全局人设、设定参考和单卡参考都要纳入生成提示。
- 默认回传全部：除非用户明确要求先挑选，否则你生成的每一张候选图都要保存并回填，不要只回传其中一张。
- 编号记录规则：分镜号/卡片号、版本号、候选号只能写入文件名、version_id、candidate_id 和回填 JSON；绝对不要画进图片像素里。
- 画面必须干净：不要在图上加分镜号、版本号、候选编号、字幕、水印、标签、随机文字或 UI 标记。
- 如果只生成一张图，保存到 suggested_candidate_outputs[0] 或 Suggested output path；如果生成多张候选，按 c01/c02/c03 保存并全部回填。
- 输出保持短：图片预览、保存路径、回填状态。

## Project / 项目
- Project slug: coin-slot
- Project root: /Users/jaychoupp/Desktop/Story/Film/projects/coin-slot
- Packet id: CARD_IMG_20260619_140906
- Packet path: 08_generation/jobs/CARD_IMG_20260619_140906/outputs/CARD_IMG_20260619_140906_card_handoff.md

## Story / 故事
- Title: 投币口 / Coin Slot
- Logline: 90年代北方小城里，三个放学后的孩子偷偷钻进居民楼角落的游戏机房，第一次跨进成人世界灰色而诱人的门缝。

## Context Cards / 上下文概念卡
这些卡片用于统一人物、场景、道具、美术、年代和负面约束；不要自动生成它们，除非它们也出现在 Tasks 里。
```json
[
  {
    "card_id": "BIBLE_CHARACTER_001",
    "scope": "project",
    "act_id": "",
    "category": "character",
    "title": "三个小朋友 / Three children",
    "summary": "第一幕的核心人物组：三个背书包的小学生，熟门熟路但仍然心虚，互相打掩护进入隐藏游戏机房。需要保持年龄、身高差、书包、发型、衣着年代感和表演气质连续。",
    "visual_direction": "1990年代中国北方小城小学生：旧校服或朴素外套、磨旧书包、略脏鞋面、放学后的疲惫和兴奋并存；动作要小心、鬼祟、彼此贴近。",
    "prompt_notes": "three Chinese school children in 1990s northern China, carrying worn schoolbags, cautious and sneaky after school, consistent faces, hairstyles, wardrobe and height differences, cinematic realism",
    "revision_note": "",
    "negative_prompt": "不要现代校服、智能手机、潮牌服饰、夸张动漫表情、年龄过大或过小、角色身份不一致。",
    "selected": true,
    "image_selected": true,
    "status": "draft",
    "references": [
      {
        "ref_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001",
        "asset_ref": "resource:media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
        "asset_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
        "path": "media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
        "origin": "resource",
        "kind": "character_ref",
        "role": "character_design_contact_sheet",
        "note": "三个小朋友统一人设、三视图、表情和服装连续性参考 / Global reference for the three children character identity, turnaround, expressions, and wardrobe continuity.",
        "version_id": "",
        "version_status": "",
        "card_type": "",
        "card_id": "",
        "card_title": ""
      },
      {
        "ref_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
        "asset_ref": "resource:media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
        "asset_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
        "path": "media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
        "origin": "resource",
        "kind": "image",
        "role": "image",
        "note": "给哥哥带一个眼镜",
        "version_id": "",
        "version_status": "",
        "card_type": "",
        "card_id": "",
        "card_title": ""
      }
    ],
    "preview_path": "",
    "versions": []
  },
  {
    "card_id": "BIBLE_LOCATION_001",
    "scope": "project",
    "act_id": "",
    "category": "location",
    "title": "破旧居民楼角落与隐藏游戏机房入口 / Compound corner arcade entrance",
    "summary": "第一幕外部主场景：老居民楼侧面的不起眼角落，暗金属门藏在墙根或楼体边角处，门上有猫眼，老板从里面确认熟人后开门。",
    "visual_direction": "潮湿水泥墙、掉皮涂料、锈迹铁门、暗窄入口、灰尘和旧广告痕迹；构图强调秘密入口、孩子压低身体靠近、门内外光线反差。",
    "prompt_notes": "old residential compound corner in 1990s northern Chinese small city, hidden arcade room entrance, rusty dark metal door with peephole, peeling concrete wall, dim afternoon light, secretive composition",
    "revision_note": "",
    "negative_prompt": "不要现代商业街、霓虹招牌、干净新楼、豪华游戏厅门面、可读随机文字或过度赛博朋克。",
    "selected": true,
    "image_selected": true,
    "status": "draft",
    "references": [
      {
        "ref_id": "WBX_20260616_024949",
        "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
        "asset_id": "WBX_20260616_024949",
        "path": "06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
        "origin": "project",
        "kind": "whitebox",
        "role": "replica_whitebox",
        "note": "隐藏游戏机房入口的空间、机位、旧墙、金属门、猫眼和三个孩子站位参考；作为场景与道具总概念的白模依据。",
        "version_id": "",
        "version_status": "",
        "card_type": "",
        "card_id": "",
        "card_title": "",
        "usage_note": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。",
        "generation_guidance": "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
        "whitebox_interpretation": {
          "mode": "spatial_control_only",
          "source_asset_id": "ACT1_SHOT_003_SOURCE_KEYFRAME",
          "source_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
          "replica_note": "以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
          "tags": [
            "ACT01",
            "SCN_COMPOUND",
            "hidden_arcade_door",
            "peephole",
            "three_children",
            "1to1_replica"
          ],
          "use_for": [
            "camera framing and lens/composition",
            "subject scale, blocking, pose, sightline, and depth order",
            "major set anchors such as doors, windows, corridors, walls, props, and openings",
            "main light direction, shadow rhythm, and scene readability"
          ],
          "preserve": [
            "overall aspect ratio and camera angle",
            "relative positions between characters and key set pieces",
            "door/window/opening height and screen position when present",
            "foreground/midground/background separation"
          ],
          "ignore": [
            "gray clay material",
            "primitive cube/sphere/cylinder shapes",
            "mannequin or toy-like character appearance",
            "unfinished low-poly geometry",
            "plain studio-white lighting unless the shot explicitly asks for it"
          ],
          "prompt_bridge": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。"
        }
      }
    ],
    "preview_path": "",
    "versions": []
  },
  {
    "card_id": "BIBLE_LOOKDEV_001",
    "scope": "project",
    "act_id": "",
    "category": "lookdev",
    "title": "90年代北方小城写实质感 / 1990s northern small-city realism",
    "summary": "全片视觉底色：纪实电影感、低饱和、颗粒但不脏、旧胶片/早期DV记忆感，强调冬春交界或阴天里的灰冷空气。",
    "visual_direction": "冷灰水泥、褪色红黄广告纸、旧木门和铁门、混浊室内烟雾、钨丝灯与街面自然光混合；摄影机克制，少用夸张广角。",
    "prompt_notes": "cinematic realism, 1990s northern Chinese small town, muted colors, natural film grain, smoky interiors, mixed tungsten and overcast daylight, grounded documentary texture",
    "revision_note": "",
    "negative_prompt": "不要过度磨皮、塑料感、CG感、现代高清广告片、过饱和网红色调、随机英文霓虹和水印。",
    "selected": true,
    "image_selected": true,
    "status": "draft",
    "references": [],
    "preview_path": "",
    "versions": []
  },
  {
    "card_id": "BIBLE_PROP_001",
    "scope": "project",
    "act_id": "",
    "category": "prop",
    "title": "旧金属门、猫眼与游戏机房道具 / Door, peephole and arcade props",
    "summary": "关键道具承担叙事信息：猫眼说明老板识别熟人，旧门说明游戏厅隐蔽，室内街机、烟灰缸、硬币和杂乱桌椅说明地下游戏机房生态。",
    "visual_direction": "门要厚重、旧、暗、带磨损把手和猫眼；室内道具应杂乱但有时代感，街机屏幕亮度压住烟雾，不出现现代 LCD 大屏。",
    "prompt_notes": "rusty metal door with peephole, worn handle, 1990s arcade machines, coin slot, smoke haze, ashtrays, cluttered stools and cables, period-correct props",
    "revision_note": "",
    "negative_prompt": "不要现代网吧、电竞椅、液晶显示器、智能门锁、干净商场电玩、随机品牌文字。",
    "selected": true,
    "image_selected": true,
    "status": "draft",
    "references": [
      {
        "ref_id": "WBX_20260616_024949",
        "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
        "asset_id": "WBX_20260616_024949",
        "path": "06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
        "origin": "project",
        "kind": "whitebox",
        "role": "replica_whitebox",
        "note": "隐藏游戏机房入口的空间、机位、旧墙、金属门、猫眼和三个孩子站位参考；作为场景与道具总概念的白模依据。",
        "version_id": "",
        "version_status": "",
        "card_type": "",
        "card_id": "",
        "card_title": "",
        "usage_note": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。",
        "generation_guidance": "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
        "whitebox_interpretation": {
          "mode": "spatial_control_only",
          "source_asset_id": "ACT1_SHOT_003_SOURCE_KEYFRAME",
          "source_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
          "replica_note": "以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
          "tags": [
            "ACT01",
            "SCN_COMPOUND",
            "hidden_arcade_door",
            "peephole",
            "three_children",
            "1to1_replica"
          ],
          "use_for": [
            "camera framing and lens/composition",
            "subject scale, blocking, pose, sightline, and depth order",
            "major set anchors such as doors, windows, corridors, walls, props, and openings",
            "main light direction, shadow rhythm, and scene readability"
          ],
          "preserve": [
            "overall aspect ratio and camera angle",
            "relative positions between characters and key set pieces",
            "door/window/opening height and screen position when present",
            "foreground/midground/background separation"
          ],
          "ignore": [
            "gray clay material",
            "primitive cube/sphere/cylinder shapes",
            "mannequin or toy-like character appearance",
            "unfinished low-poly geometry",
            "plain studio-white lighting unless the shot explicitly asks for it"
          ],
          "prompt_bridge": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。"
        }
      }
    ],
    "preview_path": "",
    "versions": []
  },
  {
    "card_id": "BIBLE_005",
    "scope": "project",
    "act_id": "",
    "category": "lookdev",
    "title": "",
    "summary": "街机厅混混三人组，都是和哥哥同龄的年轻人，但社会痕迹明显，学生气少\n老大，矮个子，黄毛，长相凶狠，耳朵后夹着烟，爱打游戏\n老二，瘦高个，嚣张，穿个白色背心\n老三，胖子，又肥又壮，有点憨憨的",
    "visual_direction": "",
    "prompt_notes": "",
    "revision_note": "",
    "negative_prompt": "",
    "selected": true,
    "image_selected": true,
    "status": "image_ready",
    "references": [],
    "preview_path": "08_generation/jobs/CARD_IMG_20260618_221216/outputs/001_BIBLE_005_v001.png",
    "versions": [
      {
        "version_id": "v001",
        "output_path": "08_generation/jobs/CARD_IMG_20260618_221216/outputs/001_BIBLE_005_v001.png",
        "notes": "电影触发生成；用户确认使用第二张。方向：14-15岁初中小痞子，街机厅混混三人组，作为全局人设/氛围参考。",
        "created_at": "2026-06-18T22:31:50+08:00",
        "status": "final",
        "candidate_id": "",
        "task_id": "",
        "packet_id": "",
        "qa": {}
      }
    ]
  },
  {
    "card_id": "BIBLE_PROP_ARCADE_CABINET_LOCK",
    "scope": "project",
    "act_id": "",
    "category": "prop",
    "title": "双人街机实体道具锁 / Two-player arcade cabinet prop lock",
    "summary": "第二幕核心道具：同一台固定结构的90年代中国小城双人街机，后续所有真人快打挑战镜头都应使用同一结构、同一高度、同一控制台关系。",
    "visual_direction": "一台厚重旧 CRT 双人街机：单一大 CRT 屏幕在上方内嵌，屏幕下方是一个宽控制面板，左右两个操作位并排，两个摇杆、两组磨损彩色按钮、中央投币口或前面板投币口，机身掉漆、边角磕碰、贴纸磨损但不要可读品牌文字。机器前有两个低塑料凳或木凳，玩家坐下/半坐，头和身体都朝向同一块屏幕。",
    "prompt_notes": "fixed 1990s Chinese two-player CRT arcade cabinet, one shared screen, side-by-side controls, worn joysticks and buttons, coin slot, chipped cabinet, two low stools, players face the screen, no readable logos, no modern LCD, no esports setup",
    "revision_note": "需要先跑探索图，再选锚点图做 Blender 1:1 白模/道具锁；所有第二幕对战镜头继承这个道具结构。",
    "negative_prompt": "不要现代电竞厅、液晶屏、立式赛车机、多人现代游戏台、可读 logo、夸张赛博朋克霓虹、玩家面对镜头互瞪。",
    "selected": true,
    "image_selected": true,
    "status": "image_ready",
    "references": [
      {
        "ref_id": "WBX_ARCADE_PROP_20260619_131654",
        "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_ARCADE_PROP_20260619_131654/renders/WBX_ARCADE_PROP_20260619_131654_arcade_cabinet_whitebox.png",
        "asset_id": "WBX_ARCADE_PROP_20260619_131654",
        "path": "06_previs/whitebox_lab/jobs/WBX_ARCADE_PROP_20260619_131654/renders/WBX_ARCADE_PROP_20260619_131654_arcade_cabinet_whitebox.png",
        "origin": "project",
        "kind": "whitebox",
        "role": "arcade_cabinet_prop_lock_whitebox",
        "note": "街机实体白模锁：固定单屏CRT、双操作位、双摇杆按钮、前投币口、双低凳和并排对战关系。",
        "version_id": "",
        "version_status": "",
        "card_type": "",
        "card_id": "",
        "card_title": "",
        "usage_note": "作为街机道具、后脑机位和双人并排关系白模参考，不复制灰白材质。",
        "generation_guidance": "Whitebox guidance / 白模读取说明\n- Use this whitebox as the fixed two-player arcade cabinet prop lock: one shared CRT screen, left/right control stations, wide control deck, front coin slot, and two low stools.\n- Preserve A Lei and the yellow-haired punk as side-by-side players facing the same screen; do not turn them face-to-face or toward camera in duel shots.\n- Preserve screen/control-panel/stool height relationships for rear-head shots and game-screen inserts.\n- Do not copy white material, primitive geometry, or clean test-render look; convert it into gritty 1990s Chinese arcade materials.\n- Negative constraint: no modern LCD, no esports setup, no readable logos, no cyberpunk arcade.",
        "whitebox_interpretation": {
          "mode": "arcade_cabinet_prop_lock",
          "source_asset_id": "BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03",
          "source_path": "08_generation/jobs/CARD_IMG_20260619_130748/outputs/001_BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03.png",
          "replica_note": "专用街机实体白模：固定单屏CRT、双操作位、双摇杆按钮、前投币口、双低凳、玩家并排朝向屏幕的空间关系。",
          "tags": [
            "SCN_ARCADE",
            "ACT02",
            "arcade_cabinet",
            "two_player_controls",
            "rear_head_duel",
            "prop_lock"
          ],
          "use_for": [
            "fixed arcade cabinet proportions",
            "screen/control panel/stool spatial relation",
            "A Lei and yellow-haired punk side-by-side blocking",
            "rear head camera shots",
            "coin slot and screen inserts"
          ],
          "preserve": [
            "single shared CRT screen",
            "left/right side-by-side controls",
            "two low stools",
            "players face the same screen",
            "front coin slot/control deck relation"
          ],
          "ignore": [
            "white material",
            "primitive geometry",
            "unfinished render look"
          ],
          "prompt_bridge": "把白模只当作街机实体、屏幕/控制台/低凳比例、双人并排关系和后脑机位参考；最终图必须按90年代中国小城游戏厅材质重建。"
        }
      }
    ],
    "preview_path": "08_generation/jobs/CARD_IMG_20260619_130748/outputs/001_BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03.png",
    "versions": [
      {
        "version_id": "v001_c01",
        "output_path": "08_generation/jobs/CARD_IMG_20260619_130748/outputs/001_BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c01.png",
        "notes": "Arcade cabinet prop-lock candidate generated with Codex built-in image_gen. c03 is the clearest front structure for Blender 1:1 whitebox; c02 is the best three-quarter relationship view.",
        "created_at": "2026-06-19T13:15:54+08:00",
        "status": "candidate",
        "candidate_id": "c01",
        "task_id": "CARD_IMG_20260619_130748_001",
        "packet_id": "CARD_IMG_20260619_130748",
        "qa": {}
      },
      {
        "version_id": "v001_c02",
        "output_path": "08_generation/jobs/CARD_IMG_20260619_130748/outputs/001_BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c02.png",
        "notes": "Arcade cabinet prop-lock candidate generated with Codex built-in image_gen. c03 is the clearest front structure for Blender 1:1 whitebox; c02 is the best three-quarter relationship view.",
        "created_at": "2026-06-19T13:15:54+08:00",
        "status": "candidate",
        "candidate_id": "c02",
        "task_id": "CARD_IMG_20260619_130748_001",
        "packet_id": "CARD_IMG_20260619_130748",
        "qa": {}
      },
      {
        "version_id": "v001_c03",
        "output_path": "08_generation/jobs/CARD_IMG_20260619_130748/outputs/001_BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03.png",
        "notes": "Arcade cabinet prop-lock candidate generated with Codex built-in image_gen. c03 is the clearest front structure for Blender 1:1 whitebox; c02 is the best three-quarter relationship view.",
        "created_at": "2026-06-19T13:15:54+08:00",
        "status": "final",
        "candidate_id": "c03",
        "task_id": "CARD_IMG_20260619_130748_001",
        "packet_id": "CARD_IMG_20260619_130748",
        "qa": {}
      }
    ]
  }
]
```

## Global References / 全局参考
```json
[
  {
    "ref_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001",
    "asset_ref": "resource:media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
    "asset_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
    "path": "media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
    "origin": "resource",
    "kind": "character_ref",
    "role": "character_design_contact_sheet",
    "note": "三个小朋友统一人设、三视图、表情和服装连续性参考 / Global reference for the three children character identity, turnaround, expressions, and wardrobe continuity.",
    "version_id": "",
    "version_status": "",
    "card_type": "",
    "card_id": "",
    "card_title": ""
  },
  {
    "ref_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
    "asset_ref": "resource:media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
    "asset_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
    "path": "media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
    "origin": "resource",
    "kind": "image",
    "role": "image",
    "note": "给哥哥带一个眼镜",
    "version_id": "",
    "version_status": "",
    "card_type": "",
    "card_id": "",
    "card_title": ""
  },
  {
    "ref_id": "001_BIBLE_005_v001.png",
    "asset_ref": "project:08_generation/jobs/CARD_IMG_20260618_221216/outputs/001_BIBLE_005_v001.png",
    "asset_id": "001_BIBLE_005_v001.png",
    "path": "08_generation/jobs/CARD_IMG_20260618_221216/outputs/001_BIBLE_005_v001.png",
    "origin": "project",
    "kind": "image",
    "role": "image",
    "note": "参考三个混混的设定，这一幕只出现黄毛",
    "version_id": "v001",
    "version_status": "current",
    "card_type": "concept",
    "card_id": "BIBLE_005",
    "card_title": ""
  }
]
```

## Callback / 回填接口
- POST: http://127.0.0.1:8787/api/projects/coin-slot/card-image-output
- Body: {"outputs":[{"card_type":"storyboard|concept","item_id":"...","card_id":"...","version_id":"v001_c01","candidate_id":"c01","task_id":"...","packet_id":"...","output_path":"...","notes":"..."}]}

## Tasks / 目标卡片任务
```json
{
  "packet_id": "CARD_IMG_20260619_140906",
  "tasks": [
    {
      "task_id": "CARD_IMG_20260619_140906_001",
      "card_type": "storyboard",
      "item_id": "ACT1_SHOT_001",
      "scene_id": "SCN_COMPOUND",
      "beat": "放学后偏离大路",
      "shot_type": "远景 / establishing wide shot",
      "frame_description": "傍晚的北方小城，旧居民楼压在灰色街道边。三个背书包的小朋友从放学人流边缘脱离，避开大路，朝居民楼背面走去。",
      "spatial_logic": "",
      "image_prompt": "Cinematic storyboard keyframe, 1990s northern Chinese small city after school, old concrete apartment blocks and dusty street, muted gray winter palette, three Chinese schoolchildren with worn backpacks quietly leaving the main road and heading toward the back corner of a residential building, cautious secretive body language, realistic film still, 35mm lens, natural dusk light, subtle film grain, clean composition, no modern cars, no smartphones, no readable text, no watermark",
      "video_prompt": "Wide observational shot: the school crowd thins out as three children peel away from the main road and move toward the old apartment corner, restrained suspense and everyday realism.",
      "notes": "建立时代、地域和偷偷行动。游戏厅入口不要过早显眼，先让路线和氛围成立。",
      "revision_note": "增加一个摄像机从高空俯瞰这座90年代小城的镜头",
      "spatial_logic_checks": [
        {
          "check_id": "door_axis_and_eyeline",
          "priority": "hard",
          "rule": "门内空间必须位于门打开后的正前方；孩子的脸、身体和视线方向要朝向门内/游戏厅内部，不要让他们看向与门内空间相反的方向。"
        },
        {
          "check_id": "spectator_age_and_blocking",
          "priority": "medium",
          "rule": "围观者以本地少年、中学生和年轻小青年为主，压迫感来自肩膀、后脑勺和站位，不要把画面变成中年成人江湖场。"
        }
      ],
      "target_references": [
        {
          "ref_id": "WBX_20260616_024949",
          "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
          "asset_id": "WBX_20260616_024949",
          "path": "06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
          "origin": "project",
          "kind": "whitebox",
          "role": "replica_whitebox",
          "note": "高精度白模复刻：默认作为该分镜空间、机位、光照和人物动作参考 / high-fidelity replica whitebox for blocking, camera, lighting, and pose.",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": "",
          "usage_note": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。",
          "generation_guidance": "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
          "whitebox_interpretation": {
            "mode": "spatial_control_only",
            "source_asset_id": "ACT1_SHOT_003_SOURCE_KEYFRAME",
            "source_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
            "replica_note": "以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
            "tags": [
              "ACT01",
              "SCN_COMPOUND",
              "hidden_arcade_door",
              "peephole",
              "three_children",
              "1to1_replica"
            ],
            "use_for": [
              "camera framing and lens/composition",
              "subject scale, blocking, pose, sightline, and depth order",
              "major set anchors such as doors, windows, corridors, walls, props, and openings",
              "main light direction, shadow rhythm, and scene readability"
            ],
            "preserve": [
              "overall aspect ratio and camera angle",
              "relative positions between characters and key set pieces",
              "door/window/opening height and screen position when present",
              "foreground/midground/background separation"
            ],
            "ignore": [
              "gray clay material",
              "primitive cube/sphere/cylinder shapes",
              "mannequin or toy-like character appearance",
              "unfinished low-poly geometry",
              "plain studio-white lighting unless the shot explicitly asks for it"
            ],
            "prompt_bridge": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。"
          }
        }
      ],
      "inherited_references": [
        {
          "ref_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001",
          "asset_ref": "resource:media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
          "asset_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
          "path": "media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
          "origin": "resource",
          "kind": "character_ref",
          "role": "character_design_contact_sheet",
          "note": "三个小朋友统一人设、三视图、表情和服装连续性参考 / Global reference for the three children character identity, turnaround, expressions, and wardrobe continuity.",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": ""
        },
        {
          "ref_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
          "asset_ref": "resource:media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
          "asset_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
          "path": "media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
          "origin": "resource",
          "kind": "image",
          "role": "image",
          "note": "给哥哥带一个眼镜",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": ""
        },
        {
          "ref_id": "001_BIBLE_005_v001.png",
          "asset_ref": "project:08_generation/jobs/CARD_IMG_20260618_221216/outputs/001_BIBLE_005_v001.png",
          "asset_id": "001_BIBLE_005_v001.png",
          "path": "08_generation/jobs/CARD_IMG_20260618_221216/outputs/001_BIBLE_005_v001.png",
          "origin": "project",
          "kind": "image",
          "role": "image",
          "note": "参考三个混混的设定，这一幕只出现黄毛",
          "version_id": "v001",
          "version_status": "current",
          "card_type": "concept",
          "card_id": "BIBLE_005",
          "card_title": ""
        },
        {
          "ref_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001",
          "asset_ref": "resource:media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
          "asset_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
          "path": "media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
          "origin": "resource",
          "kind": "character_ref",
          "role": "character_design_contact_sheet",
          "note": "三个小朋友统一人设、三视图、表情和服装连续性参考 / Global reference for the three children character identity, turnaround, expressions, and wardrobe continuity.",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": ""
        },
        {
          "ref_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
          "asset_ref": "resource:media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
          "asset_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
          "path": "media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
          "origin": "resource",
          "kind": "image",
          "role": "image",
          "note": "给哥哥带一个眼镜",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": ""
        },
        {
          "ref_id": "WBX_20260616_024949",
          "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
          "asset_id": "WBX_20260616_024949",
          "path": "06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
          "origin": "project",
          "kind": "whitebox",
          "role": "replica_whitebox",
          "note": "隐藏游戏机房入口的空间、机位、旧墙、金属门、猫眼和三个孩子站位参考；作为场景与道具总概念的白模依据。",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": "",
          "usage_note": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。",
          "generation_guidance": "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
          "whitebox_interpretation": {
            "mode": "spatial_control_only",
            "source_asset_id": "ACT1_SHOT_003_SOURCE_KEYFRAME",
            "source_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
            "replica_note": "以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
            "tags": [
              "ACT01",
              "SCN_COMPOUND",
              "hidden_arcade_door",
              "peephole",
              "three_children",
              "1to1_replica"
            ],
            "use_for": [
              "camera framing and lens/composition",
              "subject scale, blocking, pose, sightline, and depth order",
              "major set anchors such as doors, windows, corridors, walls, props, and openings",
              "main light direction, shadow rhythm, and scene readability"
            ],
            "preserve": [
              "overall aspect ratio and camera angle",
              "relative positions between characters and key set pieces",
              "door/window/opening height and screen position when present",
              "foreground/midground/background separation"
            ],
            "ignore": [
              "gray clay material",
              "primitive cube/sphere/cylinder shapes",
              "mannequin or toy-like character appearance",
              "unfinished low-poly geometry",
              "plain studio-white lighting unless the shot explicitly asks for it"
            ],
            "prompt_bridge": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。"
          }
        },
        {
          "ref_id": "WBX_20260616_024949",
          "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
          "asset_id": "WBX_20260616_024949",
          "path": "06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
          "origin": "project",
          "kind": "whitebox",
          "role": "replica_whitebox",
          "note": "隐藏游戏机房入口的空间、机位、旧墙、金属门、猫眼和三个孩子站位参考；作为场景与道具总概念的白模依据。",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": "",
          "usage_note": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。",
          "generation_guidance": "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
          "whitebox_interpretation": {
            "mode": "spatial_control_only",
            "source_asset_id": "ACT1_SHOT_003_SOURCE_KEYFRAME",
            "source_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
            "replica_note": "以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
            "tags": [
              "ACT01",
              "SCN_COMPOUND",
              "hidden_arcade_door",
              "peephole",
              "three_children",
              "1to1_replica"
            ],
            "use_for": [
              "camera framing and lens/composition",
              "subject scale, blocking, pose, sightline, and depth order",
              "major set anchors such as doors, windows, corridors, walls, props, and openings",
              "main light direction, shadow rhythm, and scene readability"
            ],
            "preserve": [
              "overall aspect ratio and camera angle",
              "relative positions between characters and key set pieces",
              "door/window/opening height and screen position when present",
              "foreground/midground/background separation"
            ],
            "ignore": [
              "gray clay material",
              "primitive cube/sphere/cylinder shapes",
              "mannequin or toy-like character appearance",
              "unfinished low-poly geometry",
              "plain studio-white lighting unless the shot explicitly asks for it"
            ],
            "prompt_bridge": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。"
          }
        },
        {
          "ref_id": "WBX_ARCADE_PROP_20260619_131654",
          "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_ARCADE_PROP_20260619_131654/renders/WBX_ARCADE_PROP_20260619_131654_arcade_cabinet_whitebox.png",
          "asset_id": "WBX_ARCADE_PROP_20260619_131654",
          "path": "06_previs/whitebox_lab/jobs/WBX_ARCADE_PROP_20260619_131654/renders/WBX_ARCADE_PROP_20260619_131654_arcade_cabinet_whitebox.png",
          "origin": "project",
          "kind": "whitebox",
          "role": "arcade_cabinet_prop_lock_whitebox",
          "note": "街机实体白模锁：固定单屏CRT、双操作位、双摇杆按钮、前投币口、双低凳和并排对战关系。",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": "",
          "usage_note": "作为街机道具、后脑机位和双人并排关系白模参考，不复制灰白材质。",
          "generation_guidance": "Whitebox guidance / 白模读取说明\n- Use this whitebox as the fixed two-player arcade cabinet prop lock: one shared CRT screen, left/right control stations, wide control deck, front coin slot, and two low stools.\n- Preserve A Lei and the yellow-haired punk as side-by-side players facing the same screen; do not turn them face-to-face or toward camera in duel shots.\n- Preserve screen/control-panel/stool height relationships for rear-head shots and game-screen inserts.\n- Do not copy white material, primitive geometry, or clean test-render look; convert it into gritty 1990s Chinese arcade materials.\n- Negative constraint: no modern LCD, no esports setup, no readable logos, no cyberpunk arcade.",
          "whitebox_interpretation": {
            "mode": "arcade_cabinet_prop_lock",
            "source_asset_id": "BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03",
            "source_path": "08_generation/jobs/CARD_IMG_20260619_130748/outputs/001_BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03.png",
            "replica_note": "专用街机实体白模：固定单屏CRT、双操作位、双摇杆按钮、前投币口、双低凳、玩家并排朝向屏幕的空间关系。",
            "tags": [
              "SCN_ARCADE",
              "ACT02",
              "arcade_cabinet",
              "two_player_controls",
              "rear_head_duel",
              "prop_lock"
            ],
            "use_for": [
              "fixed arcade cabinet proportions",
              "screen/control panel/stool spatial relation",
              "A Lei and yellow-haired punk side-by-side blocking",
              "rear head camera shots",
              "coin slot and screen inserts"
            ],
            "preserve": [
              "single shared CRT screen",
              "left/right side-by-side controls",
              "two low stools",
              "players face the same screen",
              "front coin slot/control deck relation"
            ],
            "ignore": [
              "white material",
              "primitive geometry",
              "unfinished render look"
            ],
            "prompt_bridge": "把白模只当作街机实体、屏幕/控制台/低凳比例、双人并排关系和后脑机位参考；最终图必须按90年代中国小城游戏厅材质重建。"
          }
        }
      ],
      "all_references": [
        {
          "ref_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001",
          "asset_ref": "resource:media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
          "asset_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
          "path": "media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
          "origin": "resource",
          "kind": "character_ref",
          "role": "character_design_contact_sheet",
          "note": "三个小朋友统一人设、三视图、表情和服装连续性参考 / Global reference for the three children character identity, turnaround, expressions, and wardrobe continuity.",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": ""
        },
        {
          "ref_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
          "asset_ref": "resource:media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
          "asset_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
          "path": "media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
          "origin": "resource",
          "kind": "image",
          "role": "image",
          "note": "给哥哥带一个眼镜",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": ""
        },
        {
          "ref_id": "001_BIBLE_005_v001.png",
          "asset_ref": "project:08_generation/jobs/CARD_IMG_20260618_221216/outputs/001_BIBLE_005_v001.png",
          "asset_id": "001_BIBLE_005_v001.png",
          "path": "08_generation/jobs/CARD_IMG_20260618_221216/outputs/001_BIBLE_005_v001.png",
          "origin": "project",
          "kind": "image",
          "role": "image",
          "note": "参考三个混混的设定，这一幕只出现黄毛",
          "version_id": "v001",
          "version_status": "current",
          "card_type": "concept",
          "card_id": "BIBLE_005",
          "card_title": ""
        },
        {
          "ref_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001",
          "asset_ref": "resource:media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
          "asset_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
          "path": "media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
          "origin": "resource",
          "kind": "character_ref",
          "role": "character_design_contact_sheet",
          "note": "三个小朋友统一人设、三视图、表情和服装连续性参考 / Global reference for the three children character identity, turnaround, expressions, and wardrobe continuity.",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": ""
        },
        {
          "ref_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
          "asset_ref": "resource:media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
          "asset_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
          "path": "media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
          "origin": "resource",
          "kind": "image",
          "role": "image",
          "note": "给哥哥带一个眼镜",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": ""
        },
        {
          "ref_id": "WBX_20260616_024949",
          "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
          "asset_id": "WBX_20260616_024949",
          "path": "06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
          "origin": "project",
          "kind": "whitebox",
          "role": "replica_whitebox",
          "note": "隐藏游戏机房入口的空间、机位、旧墙、金属门、猫眼和三个孩子站位参考；作为场景与道具总概念的白模依据。",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": "",
          "usage_note": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。",
          "generation_guidance": "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
          "whitebox_interpretation": {
            "mode": "spatial_control_only",
            "source_asset_id": "ACT1_SHOT_003_SOURCE_KEYFRAME",
            "source_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
            "replica_note": "以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
            "tags": [
              "ACT01",
              "SCN_COMPOUND",
              "hidden_arcade_door",
              "peephole",
              "three_children",
              "1to1_replica"
            ],
            "use_for": [
              "camera framing and lens/composition",
              "subject scale, blocking, pose, sightline, and depth order",
              "major set anchors such as doors, windows, corridors, walls, props, and openings",
              "main light direction, shadow rhythm, and scene readability"
            ],
            "preserve": [
              "overall aspect ratio and camera angle",
              "relative positions between characters and key set pieces",
              "door/window/opening height and screen position when present",
              "foreground/midground/background separation"
            ],
            "ignore": [
              "gray clay material",
              "primitive cube/sphere/cylinder shapes",
              "mannequin or toy-like character appearance",
              "unfinished low-poly geometry",
              "plain studio-white lighting unless the shot explicitly asks for it"
            ],
            "prompt_bridge": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。"
          }
        },
        {
          "ref_id": "WBX_20260616_024949",
          "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
          "asset_id": "WBX_20260616_024949",
          "path": "06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
          "origin": "project",
          "kind": "whitebox",
          "role": "replica_whitebox",
          "note": "隐藏游戏机房入口的空间、机位、旧墙、金属门、猫眼和三个孩子站位参考；作为场景与道具总概念的白模依据。",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": "",
          "usage_note": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。",
          "generation_guidance": "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
          "whitebox_interpretation": {
            "mode": "spatial_control_only",
            "source_asset_id": "ACT1_SHOT_003_SOURCE_KEYFRAME",
            "source_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
            "replica_note": "以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
            "tags": [
              "ACT01",
              "SCN_COMPOUND",
              "hidden_arcade_door",
              "peephole",
              "three_children",
              "1to1_replica"
            ],
            "use_for": [
              "camera framing and lens/composition",
              "subject scale, blocking, pose, sightline, and depth order",
              "major set anchors such as doors, windows, corridors, walls, props, and openings",
              "main light direction, shadow rhythm, and scene readability"
            ],
            "preserve": [
              "overall aspect ratio and camera angle",
              "relative positions between characters and key set pieces",
              "door/window/opening height and screen position when present",
              "foreground/midground/background separation"
            ],
            "ignore": [
              "gray clay material",
              "primitive cube/sphere/cylinder shapes",
              "mannequin or toy-like character appearance",
              "unfinished low-poly geometry",
              "plain studio-white lighting unless the shot explicitly asks for it"
            ],
            "prompt_bridge": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。"
          }
        },
        {
          "ref_id": "WBX_ARCADE_PROP_20260619_131654",
          "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_ARCADE_PROP_20260619_131654/renders/WBX_ARCADE_PROP_20260619_131654_arcade_cabinet_whitebox.png",
          "asset_id": "WBX_ARCADE_PROP_20260619_131654",
          "path": "06_previs/whitebox_lab/jobs/WBX_ARCADE_PROP_20260619_131654/renders/WBX_ARCADE_PROP_20260619_131654_arcade_cabinet_whitebox.png",
          "origin": "project",
          "kind": "whitebox",
          "role": "arcade_cabinet_prop_lock_whitebox",
          "note": "街机实体白模锁：固定单屏CRT、双操作位、双摇杆按钮、前投币口、双低凳和并排对战关系。",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": "",
          "usage_note": "作为街机道具、后脑机位和双人并排关系白模参考，不复制灰白材质。",
          "generation_guidance": "Whitebox guidance / 白模读取说明\n- Use this whitebox as the fixed two-player arcade cabinet prop lock: one shared CRT screen, left/right control stations, wide control deck, front coin slot, and two low stools.\n- Preserve A Lei and the yellow-haired punk as side-by-side players facing the same screen; do not turn them face-to-face or toward camera in duel shots.\n- Preserve screen/control-panel/stool height relationships for rear-head shots and game-screen inserts.\n- Do not copy white material, primitive geometry, or clean test-render look; convert it into gritty 1990s Chinese arcade materials.\n- Negative constraint: no modern LCD, no esports setup, no readable logos, no cyberpunk arcade.",
          "whitebox_interpretation": {
            "mode": "arcade_cabinet_prop_lock",
            "source_asset_id": "BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03",
            "source_path": "08_generation/jobs/CARD_IMG_20260619_130748/outputs/001_BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03.png",
            "replica_note": "专用街机实体白模：固定单屏CRT、双操作位、双摇杆按钮、前投币口、双低凳、玩家并排朝向屏幕的空间关系。",
            "tags": [
              "SCN_ARCADE",
              "ACT02",
              "arcade_cabinet",
              "two_player_controls",
              "rear_head_duel",
              "prop_lock"
            ],
            "use_for": [
              "fixed arcade cabinet proportions",
              "screen/control panel/stool spatial relation",
              "A Lei and yellow-haired punk side-by-side blocking",
              "rear head camera shots",
              "coin slot and screen inserts"
            ],
            "preserve": [
              "single shared CRT screen",
              "left/right side-by-side controls",
              "two low stools",
              "players face the same screen",
              "front coin slot/control deck relation"
            ],
            "ignore": [
              "white material",
              "primitive geometry",
              "unfinished render look"
            ],
            "prompt_bridge": "把白模只当作街机实体、屏幕/控制台/低凳比例、双人并排关系和后脑机位参考；最终图必须按90年代中国小城游戏厅材质重建。"
          }
        },
        {
          "ref_id": "WBX_20260616_024949",
          "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
          "asset_id": "WBX_20260616_024949",
          "path": "06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
          "origin": "project",
          "kind": "whitebox",
          "role": "replica_whitebox",
          "note": "高精度白模复刻：默认作为该分镜空间、机位、光照和人物动作参考 / high-fidelity replica whitebox for blocking, camera, lighting, and pose.",
          "version_id": "",
          "version_status": "",
          "card_type": "",
          "card_id": "",
          "card_title": "",
          "usage_note": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。",
          "generation_guidance": "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
          "whitebox_interpretation": {
            "mode": "spatial_control_only",
            "source_asset_id": "ACT1_SHOT_003_SOURCE_KEYFRAME",
            "source_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
            "replica_note": "以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
            "tags": [
              "ACT01",
              "SCN_COMPOUND",
              "hidden_arcade_door",
              "peephole",
              "three_children",
              "1to1_replica"
            ],
            "use_for": [
              "camera framing and lens/composition",
              "subject scale, blocking, pose, sightline, and depth order",
              "major set anchors such as doors, windows, corridors, walls, props, and openings",
              "main light direction, shadow rhythm, and scene readability"
            ],
            "preserve": [
              "overall aspect ratio and camera angle",
              "relative positions between characters and key set pieces",
              "door/window/opening height and screen position when present",
              "foreground/midground/background separation"
            ],
            "ignore": [
              "gray clay material",
              "primitive cube/sphere/cylinder shapes",
              "mannequin or toy-like character appearance",
              "unfinished low-poly geometry",
              "plain studio-white lighting unless the shot explicitly asks for it"
            ],
            "prompt_bridge": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。"
          }
        }
      ],
      "existing_output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/001_ACT1_SHOT_001.png",
      "existing_versions": [
        {
          "version_id": "current",
          "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/001_ACT1_SHOT_001.png",
          "notes": "",
          "created_at": "",
          "status": "final",
          "candidate_id": "",
          "task_id": "",
          "packet_id": "",
          "qa": {}
        }
      ],
      "nearby_context": {
        "scene": {
          "scene_id": "SCN_COMPOUND",
          "title": "居民楼角落 / Compound corner",
          "act_id": "ACT01",
          "act_title": "第一幕：进入游戏厅 / Act 1: Entering the arcade"
        },
        "nearby_storyboard_cards": [
          {
            "item_id": "ACT1_SHOT_001",
            "scene_id": "SCN_COMPOUND",
            "beat": "放学后偏离大路",
            "shot_type": "远景 / establishing wide shot",
            "frame_description": "傍晚的北方小城，旧居民楼压在灰色街道边。三个背书包的小朋友从放学人流边缘脱离，避开大路，朝居民楼背面走去。",
            "spatial_logic": "",
            "image_prompt": "Cinematic storyboard keyframe, 1990s northern Chinese small city after school, old concrete apartment blocks and dusty street, muted gray winter palette, three Chinese schoolchildren with worn backpacks quietly leaving the main road and heading toward the back corner of a residential building, cautious secretive body language, realistic film still, 35mm lens, natural dusk light, subtle film grain, clean composition, no modern cars, no smartphones, no readable text, no watermark",
            "notes": "建立时代、地域和偷偷行动。游戏厅入口不要过早显眼，先让路线和氛围成立。",
            "revision_note": "增加一个摄像机从高空俯瞰这座90年代小城的镜头",
            "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/001_ACT1_SHOT_001.png",
            "versions": [
              {
                "version_id": "current",
                "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/001_ACT1_SHOT_001.png",
                "notes": "",
                "created_at": "",
                "status": "final",
                "candidate_id": "",
                "task_id": "",
                "packet_id": "",
                "qa": {}
              }
            ]
          },
          {
            "item_id": "ACT1_SHOT_002",
            "scene_id": "SCN_COMPOUND",
            "beat": "沿墙根靠近隐藏入口",
            "shot_type": "中远景 / tracking medium-wide shot",
            "frame_description": "给一个两个孩子做着游戏中升龙拳和冲击波对打，哥哥在旁边看着笑的镜头",
            "spatial_logic": "",
            "image_prompt": "Cinematic film keyframe, three Chinese schoolchildren in 1990s school clothes sneaking along the wall of a shabby residential building, worn backpacks, old pipes, peeling paint, chipped concrete, one child glancing back nervously while another gestures to stay quiet, northern Chinese small-town realism, low handheld perspective, subdued colors, high-quality stable image, no modern objects, no random text, no watermark",
            "notes": "鬼鬼祟祟但不要惊悚化，表情里要带着窃喜，哥哥在给弟弟讲游戏有多好玩，弟弟全神贯注的听着",
            "revision_note": "",
            "output_path": "",
            "versions": [
              {
                "version_id": "current",
                "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/002_ACT1_SHOT_002.png",
                "notes": "",
                "created_at": "",
                "status": "rejected",
                "candidate_id": "",
                "task_id": "",
                "packet_id": "",
                "qa": {}
              }
            ]
          },
          {
            "item_id": "ACT1_SHOT_003",
            "scene_id": "SCN_COMPOUND",
            "beat": "旧门和猫眼出现",
            "shot_type": "中景 / medium shot",
            "frame_description": "居民楼一楼角落有一扇不起眼的旧金属门，门上有猫眼，没有正式招牌。三个孩子停在门前，压低声音等待。",
            "spatial_logic": "",
            "image_prompt": "Cinematic storyboard keyframe, hidden arcade entrance in the corner of an old Chinese residential building, 1990s northern small city, shabby closed metal door with a small peephole, no obvious signboard, three schoolchildren with backpacks standing on the left side whispering and looking secretive, cracked concrete wall, dim corridor shadow, realistic film still, strong readable composition, no modern signage, no readable text, no watermark",
            "notes": "旧门+猫眼是第一幕核心视觉资产，门要普通、隐蔽、可信。",
            "revision_note": "这个门不太像是游戏厅的门",
            "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
            "versions": []
          },
          {
            "item_id": "ACT1_SHOT_004",
            "scene_id": "SCN_COMPOUND",
            "beat": "老板从猫眼确认熟人",
            "shot_type": "猫眼特写 / peephole close-up",
            "frame_description": "从门内猫眼视角看出去，三个孩子的脸被猫眼畸变压缩，紧张又期待。门内老板确认他们是熟客。",
            "spatial_logic": "",
            "image_prompt": "Cinematic close-up keyframe from inside a closed door peephole, fisheye peephole distortion, three Chinese schoolchildren with worn backpacks visible outside in a shabby apartment corner, nervous excited faces, 1990s northern China, faint green-blue arcade light around the peephole edge, realistic film texture, suspenseful but not horror, clean image, no text, no watermark, no modern objects",
            "notes": "用猫眼制造“被审查/被放行”的边界感。可后续关联孩子人设。",
            "revision_note": "",
            "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/004_ACT1_SHOT_004.png",
            "versions": []
          },
          {
            "item_id": "ACT1_SHOT_005",
            "scene_id": "SCN_COMPOUND",
            "beat": "门缝打开，正对游戏厅内部",
            "shot_type": "后脑门缝镜头 / rear doorway reveal",
            "frame_description": "摄像机站在三个孩子身后，旧金属门在他们正前方打开一条缝。门内不是侧面或反方向，而是正对乌烟瘴气的游戏厅内部；蓝绿CRT光、烟雾和嘈杂声从孩子脸朝向的同一方向涌出来，老板只在门边露出手和半个身影。",
            "spatial_logic": "镜头轴线：摄影机在孩子背后；孩子后脑/肩膀在前景，门和门内游戏厅在他们正前方。门内空间、孩子脸和视线必须同向。老板靠门边，不要挡住游戏厅纵深。",
            "image_prompt": "Cinematic realism, 1990s northern Chinese small-town hidden arcade, smoky air, blue-green CRT glow, worn concrete, old bulky CRT arcade cabinets, muted film grain, no modern screens, no smartphone, no readable text, no watermark. Rear doorway reveal from behind three Chinese schoolboys with backpacks: their heads and shoulders in foreground, an old dark metal door opens directly in front of them, smoky arcade hall visible straight through the doorway, blue-green CRT light spilling toward camera, owner only a partial silhouette at the door edge. The children look forward into the arcade; do not show them facing away from the interior.",
            "notes": "修正门内外方向：开门不是先看孩子正脸，而是先建立孩子背影、门、游戏厅内部在同一条轴线上。",
            "revision_note": "",
            "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/005_ACT1_SHOT_005.png",
            "versions": []
          },
          {
            "item_id": "ACT1_SHOT_006",
            "scene_id": "SCN_ARCADE",
            "beat": "后脑入场：游戏厅全景压过孩子",
            "shot_type": "后脑跟拍广角 / rear-follow wide interior shot",
            "frame_description": "摄像机贴在三个孩子后方跟进门内，先看到他们的后脑勺、书包和肩膀，再看到低矮拥挤的游戏厅全景：一排排旧CRT街机、低凳、年轻围观者和烟雾都在孩子正前方。此时不要急着给正脸表情。",
            "spatial_logic": "入场空间轴线：摄影机在孩子身后，孩子面向游戏厅内部，游戏厅全景在画面前方/深处。孩子、门洞、街机排布、视线方向必须一致；不要把游戏厅放到孩子背后或侧后方。",
            "image_prompt": "Cinematic realism, 1990s northern Chinese small-town hidden arcade, smoky air, blue-green CRT glow, worn concrete, old bulky CRT arcade cabinets, muted film grain, no modern screens, no smartphone, no readable text, no watermark. Rear-follow wide shot from just behind the three brothers entering the arcade. Show the backs of their heads, backpacks and shoulders in the foreground, with the smoky arcade hall opening directly ahead: rows of old CRT cabinets, small stools, youthful local arcade regulars, blue-green screen glow. The children face into the room; no front reaction yet.",
            "notes": "这个镜头负责建立“孩子看见什么”，先给后脑勺+游戏厅全景。",
            "revision_note": "",
            "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/006_ACT1_SHOT_006.png",
            "versions": []
          },
          {
            "item_id": "ACT1_SHOT_007",
            "scene_id": "SCN_ARCADE",
            "beat": "游戏厅鱼龙混杂全貌",
            "shot_type": "广角全景 / wide interior shot",
            "frame_description": "低矮拥挤的游戏厅里，一排排旧街机发出蓝绿光。成年人、少年和孩子混在一起，烟雾让空气显得浑浊。",
            "spatial_logic": "全景里的门口、孩子和街机厅纵深必须能读出同一方向：孩子从入口进入，街机和人群在他们面前，入口应在他们身后或画面边缘，不要反向。",
            "image_prompt": "Wide cinematic interior keyframe of a crowded 1990s Chinese arcade hall, low ceiling, rows of old arcade cabinets, cigarette smoke, mixed crowd of adult men, teenagers, and children, three schoolchildren with backpacks visible near the entrance as small figures, blue-green CRT glow, gritty social realism, northern Chinese small-town underground game room, balanced composition, high image quality, no cyberpunk neon, no modern screens, no readable text, no watermark",
            "notes": "这一条是游戏厅场景设定核心图，既要乱，又要构图可读。",
            "revision_note": "",
            "output_path": "",
            "versions": [
              {
                "version_id": "current",
                "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/007_ACT1_SHOT_007.png",
                "notes": "",
                "created_at": "",
                "status": "rejected",
                "candidate_id": "",
                "task_id": "",
                "packet_id": "",
                "qa": {}
              }
            ]
          },
          {
            "item_id": "ACT1_SHOT_008",
            "scene_id": "SCN_ARCADE",
            "beat": "镜头转到三个孩子表情",
            "shot_type": "转场反应中近景 / arcing reaction medium close shot",
            "frame_description": "承接后脑入场镜头，摄影机从三个孩子身后缓缓绕到他们前侧，第一次看见三张被CRT光照亮的脸：哥哥戴眼镜努力镇定，二弟和小弟兴奋又不安。孩子的眼神仍然越过镜头看向游戏厅内部。",
            "spatial_logic": "这是入场镜头的反打/转身后半段：镜头已绕到孩子前侧，但孩子视线仍朝向游戏厅屏幕方向，不是回头看门外。背景应是游戏厅内部光影，不要破坏前一镜头的入场轴线。",
            "image_prompt": "Cinematic realism, 1990s northern Chinese small-town hidden arcade, smoky air, blue-green CRT glow, worn concrete, old bulky CRT arcade cabinets, muted film grain, no modern screens, no smartphone, no readable text, no watermark. Medium close reaction shot after an arcing camera move: three Chinese schoolboys inside the arcade, faces lit by CRT glow. A Lei wears glasses and a dark blue tracksuit trying to stay calm; middle brother in blue jacket with red scarf and backpack; youngest chubby boy in brown vest. Their eyes look past camera toward the arcade screens, excited and uneasy, smoky arcade background.",
            "notes": "这个镜头负责补“表情”，但必须承接前面后脑入场的方向。",
            "revision_note": "",
            "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/008_ACT1_SHOT_008.png",
            "versions": []
          }
        ],
        "related_assets": [
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "03_story",
            "asset_id": "SCN_COMPOUND_STORY_BEATS",
            "kind": "",
            "role": "beat_sheet",
            "path": "03_story/beats/coin_slot_sample_beat_sheet.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "03_story",
            "asset_id": "SCN_COMPOUND_FULL_SHOT_LIST",
            "kind": "",
            "role": "full_shot_list",
            "path": "07_shots/shot_list.csv"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "04_lookdev",
            "asset_id": "SCN_COMPOUND_LOOK_BIBLE",
            "kind": "",
            "role": "look_bible",
            "path": "04_lookdev/references/coin_slot_look_bible_v001.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "04_lookdev",
            "asset_id": "SCN_COMPOUND_COLOR_SCRIPT",
            "kind": "",
            "role": "color_script",
            "path": "04_lookdev/palettes/coin_slot_color_script.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "04_lookdev",
            "asset_id": "SCN_COMPOUND_VISUAL_REFS",
            "kind": "",
            "role": "visual_references",
            "path": "04_lookdev/references/coin_slot_visual_references.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "04_lookdev",
            "asset_id": "SCN_COMPOUND_SCENE_REFERENCE",
            "kind": "",
            "role": "scene_reference",
            "path": "media/01_AIGC/scene_refs/SC_01_compound_corner_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "05_asset_bible",
            "asset_id": "SCN_COMPOUND_CHARACTER_STAGE_LOCKS",
            "kind": "",
            "role": "character_stage_locks",
            "path": "05_asset_bible/character_stage_locks/coin_slot_character_stage_locks.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "05_asset_bible",
            "asset_id": "SCN_COMPOUND_LOCATION_BIBLE",
            "kind": "",
            "role": "location_bible",
            "path": "05_asset_bible/locations/coin_slot_location_bible.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "05_asset_bible",
            "asset_id": "SCN_COMPOUND_CONTINUITY_LOCKS",
            "kind": "",
            "role": "continuity_locks",
            "path": "05_asset_bible/continuity/coin_slot_continuity_locks.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "SCN_COMPOUND_SCENE_LOCK",
            "kind": "",
            "role": "scene_lock",
            "path": "06_previs/scene_locks/scn-compound/scene_lock.yaml"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "SCN_COMPOUND_CAMERA_MANIFEST",
            "kind": "",
            "role": "camera_manifest",
            "path": "06_previs/scene_locks/scn-compound/camera_manifest.csv"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "SCN_COMPOUND_REFERENCE_ASSETS",
            "kind": "",
            "role": "reference_assets",
            "path": "06_previs/scene_locks/scn-compound/reference_assets.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "SCN_COMPOUND_WHITEBOX_INDEX",
            "kind": "",
            "role": "whitebox_index",
            "path": "06_previs/scene_locks/scn-compound/whitebox_index.csv"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB001_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB002_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB002.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB003_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB003.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB004_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB004.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB005_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB005.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB006_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB006.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB007_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB007.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB008_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB008.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB009_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB009.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB010_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB010.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB011_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB011.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB012_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB012.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB013_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB013.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB014_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB014.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB015_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB015.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB016_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB016.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB017_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB017.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "06_previs",
            "asset_id": "MSB018_WHITEBOX",
            "kind": "",
            "role": "whitebox",
            "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB018.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "07_shots",
            "asset_id": "SCN_COMPOUND_SHOT_LIST",
            "kind": "",
            "role": "shot_list",
            "path": "07_shots/shot_list.csv"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "07_shots",
            "asset_id": "MSB001_IMAGE_PROMPT",
            "kind": "",
            "role": "image_prompt",
            "path": "07_shots/prompts/MSB001.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "07_shots",
            "asset_id": "MSB003_IMAGE_PROMPT",
            "kind": "",
            "role": "image_prompt",
            "path": "07_shots/prompts/MSB003.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "07_shots",
            "asset_id": "MSB006_IMAGE_PROMPT",
            "kind": "",
            "role": "image_prompt",
            "path": "07_shots/prompts/MSB006.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "07_shots",
            "asset_id": "MSB009_IMAGE_PROMPT",
            "kind": "",
            "role": "image_prompt",
            "path": "07_shots/prompts/MSB009.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "07_shots",
            "asset_id": "MSB012_IMAGE_PROMPT",
            "kind": "",
            "role": "image_prompt",
            "path": "07_shots/prompts/MSB012.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "07_shots",
            "asset_id": "SCN_COMPOUND_SHOT_INDEX_188",
            "kind": "",
            "role": "scene_shot_index",
            "path": "07_shots/scene_slices/SCN_COMPOUND_shot_index.csv"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "07_shots",
            "asset_id": "SCN_COMPOUND_PROMPT_PACK_188",
            "kind": "",
            "role": "scene_prompt_pack",
            "path": "07_shots/scene_slices/SCN_COMPOUND_prompt_pack.csv"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "07_shots",
            "asset_id": "MSB001_VIDEO_PROMPT",
            "kind": "",
            "role": "video_prompt",
            "path": "07_shots/video_prompts/MSB001.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "07_shots",
            "asset_id": "MSB003_VIDEO_PROMPT",
            "kind": "",
            "role": "video_prompt",
            "path": "07_shots/video_prompts/MSB003.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "07_shots",
            "asset_id": "MSB006_VIDEO_PROMPT",
            "kind": "",
            "role": "video_prompt",
            "path": "07_shots/video_prompts/MSB006.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "07_shots",
            "asset_id": "MSB009_VIDEO_PROMPT",
            "kind": "",
            "role": "video_prompt",
            "path": "07_shots/video_prompts/MSB009.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "07_shots",
            "asset_id": "MSB012_VIDEO_PROMPT",
            "kind": "",
            "role": "video_prompt",
            "path": "07_shots/video_prompts/MSB012.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "SCN_COMPOUND_IMAGE_OUTPUT_INDEX",
            "kind": "",
            "role": "image_outputs",
            "path": "08_generation/outputs/images/coin_slot_image_outputs_index.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "SCN_COMPOUND_REJECT_LOG",
            "kind": "",
            "role": "rejects",
            "path": "08_generation/rejects/coin_slot_reject_log.md"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "SCN_COMPOUND_STORYBOARD_IMAGE_INDEX",
            "kind": "",
            "role": "storyboard_image_index",
            "path": "08_generation/outputs/images/SCN_COMPOUND_storyboard_image_index.csv"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB001_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB001_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB001_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB001_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB002_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB002_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB002_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB002_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB003_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB003_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB003_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB003_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB004_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB004_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB004_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB004_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB005_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB005_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB005_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB005_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB006_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB006_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB006_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB006_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB007_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB007_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB007_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB007_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB008_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB008_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB008_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB008_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB009_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB009_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB009_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB009_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB010_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB010_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB010_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB010_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB011_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB011_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB011_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB011_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB012_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB012_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB012_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB012_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB013_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB013_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB013_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB013_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB014_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB014_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB014_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB014_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB015_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB015_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB015_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB015_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB016_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB016_v001.png"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB016_FINAL_STORYBOARD",
            "kind": "",
            "role": "final_storyboard_panel",
            "path": "media/01_AIGC/final_storyboard_panels/B01/MSB016_final_storyboard_v002.jpg"
          },
          {
            "scene_id": "SCN_COMPOUND",
            "scene_title": "居民楼角落 / Compound corner",
            "step": "08_generation",
            "asset_id": "MSB017_PURE_KEYFRAME",
            "kind": "",
            "role": "storyboard_keyframe",
            "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB017_v001.png"
          }
        ]
      },
      "generation_context": {
        "global_references": [
          {
            "ref_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001",
            "asset_ref": "resource:media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
            "asset_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
            "path": "media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
            "origin": "resource",
            "kind": "character_ref",
            "role": "character_design_contact_sheet",
            "note": "三个小朋友统一人设、三视图、表情和服装连续性参考 / Global reference for the three children character identity, turnaround, expressions, and wardrobe continuity.",
            "version_id": "",
            "version_status": "",
            "card_type": "",
            "card_id": "",
            "card_title": ""
          },
          {
            "ref_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
            "asset_ref": "resource:media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
            "asset_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
            "path": "media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
            "origin": "resource",
            "kind": "image",
            "role": "image",
            "note": "给哥哥带一个眼镜",
            "version_id": "",
            "version_status": "",
            "card_type": "",
            "card_id": "",
            "card_title": ""
          },
          {
            "ref_id": "001_BIBLE_005_v001.png",
            "asset_ref": "project:08_generation/jobs/CARD_IMG_20260618_221216/outputs/001_BIBLE_005_v001.png",
            "asset_id": "001_BIBLE_005_v001.png",
            "path": "08_generation/jobs/CARD_IMG_20260618_221216/outputs/001_BIBLE_005_v001.png",
            "origin": "project",
            "kind": "image",
            "role": "image",
            "note": "参考三个混混的设定，这一幕只出现黄毛",
            "version_id": "v001",
            "version_status": "current",
            "card_type": "concept",
            "card_id": "BIBLE_005",
            "card_title": ""
          }
        ],
        "context_cards": [
          {
            "card_id": "BIBLE_CHARACTER_001",
            "scope": "project",
            "act_id": "",
            "category": "character",
            "title": "三个小朋友 / Three children",
            "summary": "第一幕的核心人物组：三个背书包的小学生，熟门熟路但仍然心虚，互相打掩护进入隐藏游戏机房。需要保持年龄、身高差、书包、发型、衣着年代感和表演气质连续。",
            "visual_direction": "1990年代中国北方小城小学生：旧校服或朴素外套、磨旧书包、略脏鞋面、放学后的疲惫和兴奋并存；动作要小心、鬼祟、彼此贴近。",
            "prompt_notes": "three Chinese school children in 1990s northern China, carrying worn schoolbags, cautious and sneaky after school, consistent faces, hairstyles, wardrobe and height differences, cinematic realism",
            "revision_note": "",
            "negative_prompt": "不要现代校服、智能手机、潮牌服饰、夸张动漫表情、年龄过大或过小、角色身份不一致。",
            "selected": true,
            "image_selected": true,
            "status": "draft",
            "references": [
              {
                "ref_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001",
                "asset_ref": "resource:media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
                "asset_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
                "path": "media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
                "origin": "resource",
                "kind": "character_ref",
                "role": "character_design_contact_sheet",
                "note": "三个小朋友统一人设、三视图、表情和服装连续性参考 / Global reference for the three children character identity, turnaround, expressions, and wardrobe continuity.",
                "version_id": "",
                "version_status": "",
                "card_type": "",
                "card_id": "",
                "card_title": ""
              },
              {
                "ref_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
                "asset_ref": "resource:media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
                "asset_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
                "path": "media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
                "origin": "resource",
                "kind": "image",
                "role": "image",
                "note": "给哥哥带一个眼镜",
                "version_id": "",
                "version_status": "",
                "card_type": "",
                "card_id": "",
                "card_title": ""
              }
            ],
            "preview_path": "",
            "versions": []
          },
          {
            "card_id": "BIBLE_LOCATION_001",
            "scope": "project",
            "act_id": "",
            "category": "location",
            "title": "破旧居民楼角落与隐藏游戏机房入口 / Compound corner arcade entrance",
            "summary": "第一幕外部主场景：老居民楼侧面的不起眼角落，暗金属门藏在墙根或楼体边角处，门上有猫眼，老板从里面确认熟人后开门。",
            "visual_direction": "潮湿水泥墙、掉皮涂料、锈迹铁门、暗窄入口、灰尘和旧广告痕迹；构图强调秘密入口、孩子压低身体靠近、门内外光线反差。",
            "prompt_notes": "old residential compound corner in 1990s northern Chinese small city, hidden arcade room entrance, rusty dark metal door with peephole, peeling concrete wall, dim afternoon light, secretive composition",
            "revision_note": "",
            "negative_prompt": "不要现代商业街、霓虹招牌、干净新楼、豪华游戏厅门面、可读随机文字或过度赛博朋克。",
            "selected": true,
            "image_selected": true,
            "status": "draft",
            "references": [
              {
                "ref_id": "WBX_20260616_024949",
                "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
                "asset_id": "WBX_20260616_024949",
                "path": "06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
                "origin": "project",
                "kind": "whitebox",
                "role": "replica_whitebox",
                "note": "隐藏游戏机房入口的空间、机位、旧墙、金属门、猫眼和三个孩子站位参考；作为场景与道具总概念的白模依据。",
                "version_id": "",
                "version_status": "",
                "card_type": "",
                "card_id": "",
                "card_title": "",
                "usage_note": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。",
                "generation_guidance": "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
                "whitebox_interpretation": {
                  "mode": "spatial_control_only",
                  "source_asset_id": "ACT1_SHOT_003_SOURCE_KEYFRAME",
                  "source_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
                  "replica_note": "以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
                  "tags": [
                    "ACT01",
                    "SCN_COMPOUND",
                    "hidden_arcade_door",
                    "peephole",
                    "three_children",
                    "1to1_replica"
                  ],
                  "use_for": [
                    "camera framing and lens/composition",
                    "subject scale, blocking, pose, sightline, and depth order",
                    "major set anchors such as doors, windows, corridors, walls, props, and openings",
                    "main light direction, shadow rhythm, and scene readability"
                  ],
                  "preserve": [
                    "overall aspect ratio and camera angle",
                    "relative positions between characters and key set pieces",
                    "door/window/opening height and screen position when present",
                    "foreground/midground/background separation"
                  ],
                  "ignore": [
                    "gray clay material",
                    "primitive cube/sphere/cylinder shapes",
                    "mannequin or toy-like character appearance",
                    "unfinished low-poly geometry",
                    "plain studio-white lighting unless the shot explicitly asks for it"
                  ],
                  "prompt_bridge": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。"
                }
              }
            ],
            "preview_path": "",
            "versions": []
          },
          {
            "card_id": "BIBLE_LOOKDEV_001",
            "scope": "project",
            "act_id": "",
            "category": "lookdev",
            "title": "90年代北方小城写实质感 / 1990s northern small-city realism",
            "summary": "全片视觉底色：纪实电影感、低饱和、颗粒但不脏、旧胶片/早期DV记忆感，强调冬春交界或阴天里的灰冷空气。",
            "visual_direction": "冷灰水泥、褪色红黄广告纸、旧木门和铁门、混浊室内烟雾、钨丝灯与街面自然光混合；摄影机克制，少用夸张广角。",
            "prompt_notes": "cinematic realism, 1990s northern Chinese small town, muted colors, natural film grain, smoky interiors, mixed tungsten and overcast daylight, grounded documentary texture",
            "revision_note": "",
            "negative_prompt": "不要过度磨皮、塑料感、CG感、现代高清广告片、过饱和网红色调、随机英文霓虹和水印。",
            "selected": true,
            "image_selected": true,
            "status": "draft",
            "references": [],
            "preview_path": "",
            "versions": []
          },
          {
            "card_id": "BIBLE_PROP_001",
            "scope": "project",
            "act_id": "",
            "category": "prop",
            "title": "旧金属门、猫眼与游戏机房道具 / Door, peephole and arcade props",
            "summary": "关键道具承担叙事信息：猫眼说明老板识别熟人，旧门说明游戏厅隐蔽，室内街机、烟灰缸、硬币和杂乱桌椅说明地下游戏机房生态。",
            "visual_direction": "门要厚重、旧、暗、带磨损把手和猫眼；室内道具应杂乱但有时代感，街机屏幕亮度压住烟雾，不出现现代 LCD 大屏。",
            "prompt_notes": "rusty metal door with peephole, worn handle, 1990s arcade machines, coin slot, smoke haze, ashtrays, cluttered stools and cables, period-correct props",
            "revision_note": "",
            "negative_prompt": "不要现代网吧、电竞椅、液晶显示器、智能门锁、干净商场电玩、随机品牌文字。",
            "selected": true,
            "image_selected": true,
            "status": "draft",
            "references": [
              {
                "ref_id": "WBX_20260616_024949",
                "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
                "asset_id": "WBX_20260616_024949",
                "path": "06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
                "origin": "project",
                "kind": "whitebox",
                "role": "replica_whitebox",
                "note": "隐藏游戏机房入口的空间、机位、旧墙、金属门、猫眼和三个孩子站位参考；作为场景与道具总概念的白模依据。",
                "version_id": "",
                "version_status": "",
                "card_type": "",
                "card_id": "",
                "card_title": "",
                "usage_note": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。",
                "generation_guidance": "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
                "whitebox_interpretation": {
                  "mode": "spatial_control_only",
                  "source_asset_id": "ACT1_SHOT_003_SOURCE_KEYFRAME",
                  "source_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
                  "replica_note": "以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
                  "tags": [
                    "ACT01",
                    "SCN_COMPOUND",
                    "hidden_arcade_door",
                    "peephole",
                    "three_children",
                    "1to1_replica"
                  ],
                  "use_for": [
                    "camera framing and lens/composition",
                    "subject scale, blocking, pose, sightline, and depth order",
                    "major set anchors such as doors, windows, corridors, walls, props, and openings",
                    "main light direction, shadow rhythm, and scene readability"
                  ],
                  "preserve": [
                    "overall aspect ratio and camera angle",
                    "relative positions between characters and key set pieces",
                    "door/window/opening height and screen position when present",
                    "foreground/midground/background separation"
                  ],
                  "ignore": [
                    "gray clay material",
                    "primitive cube/sphere/cylinder shapes",
                    "mannequin or toy-like character appearance",
                    "unfinished low-poly geometry",
                    "plain studio-white lighting unless the shot explicitly asks for it"
                  ],
                  "prompt_bridge": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。"
                }
              }
            ],
            "preview_path": "",
            "versions": []
          },
          {
            "card_id": "BIBLE_005",
            "scope": "project",
            "act_id": "",
            "category": "lookdev",
            "title": "",
            "summary": "街机厅混混三人组，都是和哥哥同龄的年轻人，但社会痕迹明显，学生气少\n老大，矮个子，黄毛，长相凶狠，耳朵后夹着烟，爱打游戏\n老二，瘦高个，嚣张，穿个白色背心\n老三，胖子，又肥又壮，有点憨憨的",
            "visual_direction": "",
            "prompt_notes": "",
            "revision_note": "",
            "negative_prompt": "",
            "selected": true,
            "image_selected": true,
            "status": "image_ready",
            "references": [],
            "preview_path": "08_generation/jobs/CARD_IMG_20260618_221216/outputs/001_BIBLE_005_v001.png",
            "versions": [
              {
                "version_id": "v001",
                "output_path": "08_generation/jobs/CARD_IMG_20260618_221216/outputs/001_BIBLE_005_v001.png",
                "notes": "电影触发生成；用户确认使用第二张。方向：14-15岁初中小痞子，街机厅混混三人组，作为全局人设/氛围参考。",
                "created_at": "2026-06-18T22:31:50+08:00",
                "status": "final",
                "candidate_id": "",
                "task_id": "",
                "packet_id": "",
                "qa": {}
              }
            ]
          },
          {
            "card_id": "BIBLE_PROP_ARCADE_CABINET_LOCK",
            "scope": "project",
            "act_id": "",
            "category": "prop",
            "title": "双人街机实体道具锁 / Two-player arcade cabinet prop lock",
            "summary": "第二幕核心道具：同一台固定结构的90年代中国小城双人街机，后续所有真人快打挑战镜头都应使用同一结构、同一高度、同一控制台关系。",
            "visual_direction": "一台厚重旧 CRT 双人街机：单一大 CRT 屏幕在上方内嵌，屏幕下方是一个宽控制面板，左右两个操作位并排，两个摇杆、两组磨损彩色按钮、中央投币口或前面板投币口，机身掉漆、边角磕碰、贴纸磨损但不要可读品牌文字。机器前有两个低塑料凳或木凳，玩家坐下/半坐，头和身体都朝向同一块屏幕。",
            "prompt_notes": "fixed 1990s Chinese two-player CRT arcade cabinet, one shared screen, side-by-side controls, worn joysticks and buttons, coin slot, chipped cabinet, two low stools, players face the screen, no readable logos, no modern LCD, no esports setup",
            "revision_note": "需要先跑探索图，再选锚点图做 Blender 1:1 白模/道具锁；所有第二幕对战镜头继承这个道具结构。",
            "negative_prompt": "不要现代电竞厅、液晶屏、立式赛车机、多人现代游戏台、可读 logo、夸张赛博朋克霓虹、玩家面对镜头互瞪。",
            "selected": true,
            "image_selected": true,
            "status": "image_ready",
            "references": [
              {
                "ref_id": "WBX_ARCADE_PROP_20260619_131654",
                "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_ARCADE_PROP_20260619_131654/renders/WBX_ARCADE_PROP_20260619_131654_arcade_cabinet_whitebox.png",
                "asset_id": "WBX_ARCADE_PROP_20260619_131654",
                "path": "06_previs/whitebox_lab/jobs/WBX_ARCADE_PROP_20260619_131654/renders/WBX_ARCADE_PROP_20260619_131654_arcade_cabinet_whitebox.png",
                "origin": "project",
                "kind": "whitebox",
                "role": "arcade_cabinet_prop_lock_whitebox",
                "note": "街机实体白模锁：固定单屏CRT、双操作位、双摇杆按钮、前投币口、双低凳和并排对战关系。",
                "version_id": "",
                "version_status": "",
                "card_type": "",
                "card_id": "",
                "card_title": "",
                "usage_note": "作为街机道具、后脑机位和双人并排关系白模参考，不复制灰白材质。",
                "generation_guidance": "Whitebox guidance / 白模读取说明\n- Use this whitebox as the fixed two-player arcade cabinet prop lock: one shared CRT screen, left/right control stations, wide control deck, front coin slot, and two low stools.\n- Preserve A Lei and the yellow-haired punk as side-by-side players facing the same screen; do not turn them face-to-face or toward camera in duel shots.\n- Preserve screen/control-panel/stool height relationships for rear-head shots and game-screen inserts.\n- Do not copy white material, primitive geometry, or clean test-render look; convert it into gritty 1990s Chinese arcade materials.\n- Negative constraint: no modern LCD, no esports setup, no readable logos, no cyberpunk arcade.",
                "whitebox_interpretation": {
                  "mode": "arcade_cabinet_prop_lock",
                  "source_asset_id": "BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03",
                  "source_path": "08_generation/jobs/CARD_IMG_20260619_130748/outputs/001_BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03.png",
                  "replica_note": "专用街机实体白模：固定单屏CRT、双操作位、双摇杆按钮、前投币口、双低凳、玩家并排朝向屏幕的空间关系。",
                  "tags": [
                    "SCN_ARCADE",
                    "ACT02",
                    "arcade_cabinet",
                    "two_player_controls",
                    "rear_head_duel",
                    "prop_lock"
                  ],
                  "use_for": [
                    "fixed arcade cabinet proportions",
                    "screen/control panel/stool spatial relation",
                    "A Lei and yellow-haired punk side-by-side blocking",
                    "rear head camera shots",
                    "coin slot and screen inserts"
                  ],
                  "preserve": [
                    "single shared CRT screen",
                    "left/right side-by-side controls",
                    "two low stools",
                    "players face the same screen",
                    "front coin slot/control deck relation"
                  ],
                  "ignore": [
                    "white material",
                    "primitive geometry",
                    "unfinished render look"
                  ],
                  "prompt_bridge": "把白模只当作街机实体、屏幕/控制台/低凳比例、双人并排关系和后脑机位参考；最终图必须按90年代中国小城游戏厅材质重建。"
                }
              }
            ],
            "preview_path": "08_generation/jobs/CARD_IMG_20260619_130748/outputs/001_BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03.png",
            "versions": [
              {
                "version_id": "v001_c01",
                "output_path": "08_generation/jobs/CARD_IMG_20260619_130748/outputs/001_BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c01.png",
                "notes": "Arcade cabinet prop-lock candidate generated with Codex built-in image_gen. c03 is the clearest front structure for Blender 1:1 whitebox; c02 is the best three-quarter relationship view.",
                "created_at": "2026-06-19T13:15:54+08:00",
                "status": "candidate",
                "candidate_id": "c01",
                "task_id": "CARD_IMG_20260619_130748_001",
                "packet_id": "CARD_IMG_20260619_130748",
                "qa": {}
              },
              {
                "version_id": "v001_c02",
                "output_path": "08_generation/jobs/CARD_IMG_20260619_130748/outputs/001_BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c02.png",
                "notes": "Arcade cabinet prop-lock candidate generated with Codex built-in image_gen. c03 is the clearest front structure for Blender 1:1 whitebox; c02 is the best three-quarter relationship view.",
                "created_at": "2026-06-19T13:15:54+08:00",
                "status": "candidate",
                "candidate_id": "c02",
                "task_id": "CARD_IMG_20260619_130748_001",
                "packet_id": "CARD_IMG_20260619_130748",
                "qa": {}
              },
              {
                "version_id": "v001_c03",
                "output_path": "08_generation/jobs/CARD_IMG_20260619_130748/outputs/001_BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03.png",
                "notes": "Arcade cabinet prop-lock candidate generated with Codex built-in image_gen. c03 is the clearest front structure for Blender 1:1 whitebox; c02 is the best three-quarter relationship view.",
                "created_at": "2026-06-19T13:15:54+08:00",
                "status": "final",
                "candidate_id": "c03",
                "task_id": "CARD_IMG_20260619_130748_001",
                "packet_id": "CARD_IMG_20260619_130748",
                "qa": {}
              }
            ]
          }
        ],
        "context_references": [
          {
            "ref_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001",
            "asset_ref": "resource:media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
            "asset_id": "THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
            "path": "media/01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg",
            "origin": "resource",
            "kind": "character_ref",
            "role": "character_design_contact_sheet",
            "note": "三个小朋友统一人设、三视图、表情和服装连续性参考 / Global reference for the three children character identity, turnaround, expressions, and wardrobe continuity.",
            "version_id": "",
            "version_status": "",
            "card_type": "",
            "card_id": "",
            "card_title": ""
          },
          {
            "ref_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
            "asset_ref": "resource:media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
            "asset_id": "CHR_BRO_A_late_scuffed_reference_v001.png",
            "path": "media/01_AIGC/character_design_v2/stage_variants/CHR_BRO_A_late_scuffed_reference_v001.png",
            "origin": "resource",
            "kind": "image",
            "role": "image",
            "note": "给哥哥带一个眼镜",
            "version_id": "",
            "version_status": "",
            "card_type": "",
            "card_id": "",
            "card_title": ""
          },
          {
            "ref_id": "WBX_20260616_024949",
            "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
            "asset_id": "WBX_20260616_024949",
            "path": "06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
            "origin": "project",
            "kind": "whitebox",
            "role": "replica_whitebox",
            "note": "隐藏游戏机房入口的空间、机位、旧墙、金属门、猫眼和三个孩子站位参考；作为场景与道具总概念的白模依据。",
            "version_id": "",
            "version_status": "",
            "card_type": "",
            "card_id": "",
            "card_title": "",
            "usage_note": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。",
            "generation_guidance": "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
            "whitebox_interpretation": {
              "mode": "spatial_control_only",
              "source_asset_id": "ACT1_SHOT_003_SOURCE_KEYFRAME",
              "source_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
              "replica_note": "以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
              "tags": [
                "ACT01",
                "SCN_COMPOUND",
                "hidden_arcade_door",
                "peephole",
                "three_children",
                "1to1_replica"
              ],
              "use_for": [
                "camera framing and lens/composition",
                "subject scale, blocking, pose, sightline, and depth order",
                "major set anchors such as doors, windows, corridors, walls, props, and openings",
                "main light direction, shadow rhythm, and scene readability"
              ],
              "preserve": [
                "overall aspect ratio and camera angle",
                "relative positions between characters and key set pieces",
                "door/window/opening height and screen position when present",
                "foreground/midground/background separation"
              ],
              "ignore": [
                "gray clay material",
                "primitive cube/sphere/cylinder shapes",
                "mannequin or toy-like character appearance",
                "unfinished low-poly geometry",
                "plain studio-white lighting unless the shot explicitly asks for it"
              ],
              "prompt_bridge": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。"
            }
          },
          {
            "ref_id": "WBX_20260616_024949",
            "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
            "asset_id": "WBX_20260616_024949",
            "path": "06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
            "origin": "project",
            "kind": "whitebox",
            "role": "replica_whitebox",
            "note": "隐藏游戏机房入口的空间、机位、旧墙、金属门、猫眼和三个孩子站位参考；作为场景与道具总概念的白模依据。",
            "version_id": "",
            "version_status": "",
            "card_type": "",
            "card_id": "",
            "card_title": "",
            "usage_note": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。",
            "generation_guidance": "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
            "whitebox_interpretation": {
              "mode": "spatial_control_only",
              "source_asset_id": "ACT1_SHOT_003_SOURCE_KEYFRAME",
              "source_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
              "replica_note": "以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
              "tags": [
                "ACT01",
                "SCN_COMPOUND",
                "hidden_arcade_door",
                "peephole",
                "three_children",
                "1to1_replica"
              ],
              "use_for": [
                "camera framing and lens/composition",
                "subject scale, blocking, pose, sightline, and depth order",
                "major set anchors such as doors, windows, corridors, walls, props, and openings",
                "main light direction, shadow rhythm, and scene readability"
              ],
              "preserve": [
                "overall aspect ratio and camera angle",
                "relative positions between characters and key set pieces",
                "door/window/opening height and screen position when present",
                "foreground/midground/background separation"
              ],
              "ignore": [
                "gray clay material",
                "primitive cube/sphere/cylinder shapes",
                "mannequin or toy-like character appearance",
                "unfinished low-poly geometry",
                "plain studio-white lighting unless the shot explicitly asks for it"
              ],
              "prompt_bridge": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。"
            }
          },
          {
            "ref_id": "WBX_ARCADE_PROP_20260619_131654",
            "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_ARCADE_PROP_20260619_131654/renders/WBX_ARCADE_PROP_20260619_131654_arcade_cabinet_whitebox.png",
            "asset_id": "WBX_ARCADE_PROP_20260619_131654",
            "path": "06_previs/whitebox_lab/jobs/WBX_ARCADE_PROP_20260619_131654/renders/WBX_ARCADE_PROP_20260619_131654_arcade_cabinet_whitebox.png",
            "origin": "project",
            "kind": "whitebox",
            "role": "arcade_cabinet_prop_lock_whitebox",
            "note": "街机实体白模锁：固定单屏CRT、双操作位、双摇杆按钮、前投币口、双低凳和并排对战关系。",
            "version_id": "",
            "version_status": "",
            "card_type": "",
            "card_id": "",
            "card_title": "",
            "usage_note": "作为街机道具、后脑机位和双人并排关系白模参考，不复制灰白材质。",
            "generation_guidance": "Whitebox guidance / 白模读取说明\n- Use this whitebox as the fixed two-player arcade cabinet prop lock: one shared CRT screen, left/right control stations, wide control deck, front coin slot, and two low stools.\n- Preserve A Lei and the yellow-haired punk as side-by-side players facing the same screen; do not turn them face-to-face or toward camera in duel shots.\n- Preserve screen/control-panel/stool height relationships for rear-head shots and game-screen inserts.\n- Do not copy white material, primitive geometry, or clean test-render look; convert it into gritty 1990s Chinese arcade materials.\n- Negative constraint: no modern LCD, no esports setup, no readable logos, no cyberpunk arcade.",
            "whitebox_interpretation": {
              "mode": "arcade_cabinet_prop_lock",
              "source_asset_id": "BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03",
              "source_path": "08_generation/jobs/CARD_IMG_20260619_130748/outputs/001_BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03.png",
              "replica_note": "专用街机实体白模：固定单屏CRT、双操作位、双摇杆按钮、前投币口、双低凳、玩家并排朝向屏幕的空间关系。",
              "tags": [
                "SCN_ARCADE",
                "ACT02",
                "arcade_cabinet",
                "two_player_controls",
                "rear_head_duel",
                "prop_lock"
              ],
              "use_for": [
                "fixed arcade cabinet proportions",
                "screen/control panel/stool spatial relation",
                "A Lei and yellow-haired punk side-by-side blocking",
                "rear head camera shots",
                "coin slot and screen inserts"
              ],
              "preserve": [
                "single shared CRT screen",
                "left/right side-by-side controls",
                "two low stools",
                "players face the same screen",
                "front coin slot/control deck relation"
              ],
              "ignore": [
                "white material",
                "primitive geometry",
                "unfinished render look"
              ],
              "prompt_bridge": "把白模只当作街机实体、屏幕/控制台/低凳比例、双人并排关系和后脑机位参考；最终图必须按90年代中国小城游戏厅材质重建。"
            }
          }
        ],
        "target_references": [
          {
            "ref_id": "WBX_20260616_024949",
            "asset_ref": "project:06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
            "asset_id": "WBX_20260616_024949",
            "path": "06_previs/whitebox_lab/jobs/WBX_20260616_024949/renders/WBX_20260616_024949_replica_whitebox.png",
            "origin": "project",
            "kind": "whitebox",
            "role": "replica_whitebox",
            "note": "高精度白模复刻：默认作为该分镜空间、机位、光照和人物动作参考 / high-fidelity replica whitebox for blocking, camera, lighting, and pose.",
            "version_id": "",
            "version_status": "",
            "card_type": "",
            "card_id": "",
            "card_title": "",
            "usage_note": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。",
            "generation_guidance": "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
            "whitebox_interpretation": {
              "mode": "spatial_control_only",
              "source_asset_id": "ACT1_SHOT_003_SOURCE_KEYFRAME",
              "source_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
              "replica_note": "以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
              "tags": [
                "ACT01",
                "SCN_COMPOUND",
                "hidden_arcade_door",
                "peephole",
                "three_children",
                "1to1_replica"
              ],
              "use_for": [
                "camera framing and lens/composition",
                "subject scale, blocking, pose, sightline, and depth order",
                "major set anchors such as doors, windows, corridors, walls, props, and openings",
                "main light direction, shadow rhythm, and scene readability"
              ],
              "preserve": [
                "overall aspect ratio and camera angle",
                "relative positions between characters and key set pieces",
                "door/window/opening height and screen position when present",
                "foreground/midground/background separation"
              ],
              "ignore": [
                "gray clay material",
                "primitive cube/sphere/cylinder shapes",
                "mannequin or toy-like character appearance",
                "unfinished low-poly geometry",
                "plain studio-white lighting unless the shot explicitly asks for it"
              ],
              "prompt_bridge": "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。"
            }
          }
        ],
        "target_context": {
          "scene": {
            "scene_id": "SCN_COMPOUND",
            "title": "居民楼角落 / Compound corner",
            "act_id": "ACT01",
            "act_title": "第一幕：进入游戏厅 / Act 1: Entering the arcade"
          },
          "nearby_storyboard_cards": [
            {
              "item_id": "ACT1_SHOT_001",
              "scene_id": "SCN_COMPOUND",
              "beat": "放学后偏离大路",
              "shot_type": "远景 / establishing wide shot",
              "frame_description": "傍晚的北方小城，旧居民楼压在灰色街道边。三个背书包的小朋友从放学人流边缘脱离，避开大路，朝居民楼背面走去。",
              "spatial_logic": "",
              "image_prompt": "Cinematic storyboard keyframe, 1990s northern Chinese small city after school, old concrete apartment blocks and dusty street, muted gray winter palette, three Chinese schoolchildren with worn backpacks quietly leaving the main road and heading toward the back corner of a residential building, cautious secretive body language, realistic film still, 35mm lens, natural dusk light, subtle film grain, clean composition, no modern cars, no smartphones, no readable text, no watermark",
              "notes": "建立时代、地域和偷偷行动。游戏厅入口不要过早显眼，先让路线和氛围成立。",
              "revision_note": "增加一个摄像机从高空俯瞰这座90年代小城的镜头",
              "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/001_ACT1_SHOT_001.png",
              "versions": [
                {
                  "version_id": "current",
                  "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/001_ACT1_SHOT_001.png",
                  "notes": "",
                  "created_at": "",
                  "status": "final",
                  "candidate_id": "",
                  "task_id": "",
                  "packet_id": "",
                  "qa": {}
                }
              ]
            },
            {
              "item_id": "ACT1_SHOT_002",
              "scene_id": "SCN_COMPOUND",
              "beat": "沿墙根靠近隐藏入口",
              "shot_type": "中远景 / tracking medium-wide shot",
              "frame_description": "给一个两个孩子做着游戏中升龙拳和冲击波对打，哥哥在旁边看着笑的镜头",
              "spatial_logic": "",
              "image_prompt": "Cinematic film keyframe, three Chinese schoolchildren in 1990s school clothes sneaking along the wall of a shabby residential building, worn backpacks, old pipes, peeling paint, chipped concrete, one child glancing back nervously while another gestures to stay quiet, northern Chinese small-town realism, low handheld perspective, subdued colors, high-quality stable image, no modern objects, no random text, no watermark",
              "notes": "鬼鬼祟祟但不要惊悚化，表情里要带着窃喜，哥哥在给弟弟讲游戏有多好玩，弟弟全神贯注的听着",
              "revision_note": "",
              "output_path": "",
              "versions": [
                {
                  "version_id": "current",
                  "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/002_ACT1_SHOT_002.png",
                  "notes": "",
                  "created_at": "",
                  "status": "rejected",
                  "candidate_id": "",
                  "task_id": "",
                  "packet_id": "",
                  "qa": {}
                }
              ]
            },
            {
              "item_id": "ACT1_SHOT_003",
              "scene_id": "SCN_COMPOUND",
              "beat": "旧门和猫眼出现",
              "shot_type": "中景 / medium shot",
              "frame_description": "居民楼一楼角落有一扇不起眼的旧金属门，门上有猫眼，没有正式招牌。三个孩子停在门前，压低声音等待。",
              "spatial_logic": "",
              "image_prompt": "Cinematic storyboard keyframe, hidden arcade entrance in the corner of an old Chinese residential building, 1990s northern small city, shabby closed metal door with a small peephole, no obvious signboard, three schoolchildren with backpacks standing on the left side whispering and looking secretive, cracked concrete wall, dim corridor shadow, realistic film still, strong readable composition, no modern signage, no readable text, no watermark",
              "notes": "旧门+猫眼是第一幕核心视觉资产，门要普通、隐蔽、可信。",
              "revision_note": "这个门不太像是游戏厅的门",
              "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/003_ACT1_SHOT_003.png",
              "versions": []
            },
            {
              "item_id": "ACT1_SHOT_004",
              "scene_id": "SCN_COMPOUND",
              "beat": "老板从猫眼确认熟人",
              "shot_type": "猫眼特写 / peephole close-up",
              "frame_description": "从门内猫眼视角看出去，三个孩子的脸被猫眼畸变压缩，紧张又期待。门内老板确认他们是熟客。",
              "spatial_logic": "",
              "image_prompt": "Cinematic close-up keyframe from inside a closed door peephole, fisheye peephole distortion, three Chinese schoolchildren with worn backpacks visible outside in a shabby apartment corner, nervous excited faces, 1990s northern China, faint green-blue arcade light around the peephole edge, realistic film texture, suspenseful but not horror, clean image, no text, no watermark, no modern objects",
              "notes": "用猫眼制造“被审查/被放行”的边界感。可后续关联孩子人设。",
              "revision_note": "",
              "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/004_ACT1_SHOT_004.png",
              "versions": []
            },
            {
              "item_id": "ACT1_SHOT_005",
              "scene_id": "SCN_COMPOUND",
              "beat": "门缝打开，正对游戏厅内部",
              "shot_type": "后脑门缝镜头 / rear doorway reveal",
              "frame_description": "摄像机站在三个孩子身后，旧金属门在他们正前方打开一条缝。门内不是侧面或反方向，而是正对乌烟瘴气的游戏厅内部；蓝绿CRT光、烟雾和嘈杂声从孩子脸朝向的同一方向涌出来，老板只在门边露出手和半个身影。",
              "spatial_logic": "镜头轴线：摄影机在孩子背后；孩子后脑/肩膀在前景，门和门内游戏厅在他们正前方。门内空间、孩子脸和视线必须同向。老板靠门边，不要挡住游戏厅纵深。",
              "image_prompt": "Cinematic realism, 1990s northern Chinese small-town hidden arcade, smoky air, blue-green CRT glow, worn concrete, old bulky CRT arcade cabinets, muted film grain, no modern screens, no smartphone, no readable text, no watermark. Rear doorway reveal from behind three Chinese schoolboys with backpacks: their heads and shoulders in foreground, an old dark metal door opens directly in front of them, smoky arcade hall visible straight through the doorway, blue-green CRT light spilling toward camera, owner only a partial silhouette at the door edge. The children look forward into the arcade; do not show them facing away from the interior.",
              "notes": "修正门内外方向：开门不是先看孩子正脸，而是先建立孩子背影、门、游戏厅内部在同一条轴线上。",
              "revision_note": "",
              "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/005_ACT1_SHOT_005.png",
              "versions": []
            },
            {
              "item_id": "ACT1_SHOT_006",
              "scene_id": "SCN_ARCADE",
              "beat": "后脑入场：游戏厅全景压过孩子",
              "shot_type": "后脑跟拍广角 / rear-follow wide interior shot",
              "frame_description": "摄像机贴在三个孩子后方跟进门内，先看到他们的后脑勺、书包和肩膀，再看到低矮拥挤的游戏厅全景：一排排旧CRT街机、低凳、年轻围观者和烟雾都在孩子正前方。此时不要急着给正脸表情。",
              "spatial_logic": "入场空间轴线：摄影机在孩子身后，孩子面向游戏厅内部，游戏厅全景在画面前方/深处。孩子、门洞、街机排布、视线方向必须一致；不要把游戏厅放到孩子背后或侧后方。",
              "image_prompt": "Cinematic realism, 1990s northern Chinese small-town hidden arcade, smoky air, blue-green CRT glow, worn concrete, old bulky CRT arcade cabinets, muted film grain, no modern screens, no smartphone, no readable text, no watermark. Rear-follow wide shot from just behind the three brothers entering the arcade. Show the backs of their heads, backpacks and shoulders in the foreground, with the smoky arcade hall opening directly ahead: rows of old CRT cabinets, small stools, youthful local arcade regulars, blue-green screen glow. The children face into the room; no front reaction yet.",
              "notes": "这个镜头负责建立“孩子看见什么”，先给后脑勺+游戏厅全景。",
              "revision_note": "",
              "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/006_ACT1_SHOT_006.png",
              "versions": []
            },
            {
              "item_id": "ACT1_SHOT_007",
              "scene_id": "SCN_ARCADE",
              "beat": "游戏厅鱼龙混杂全貌",
              "shot_type": "广角全景 / wide interior shot",
              "frame_description": "低矮拥挤的游戏厅里，一排排旧街机发出蓝绿光。成年人、少年和孩子混在一起，烟雾让空气显得浑浊。",
              "spatial_logic": "全景里的门口、孩子和街机厅纵深必须能读出同一方向：孩子从入口进入，街机和人群在他们面前，入口应在他们身后或画面边缘，不要反向。",
              "image_prompt": "Wide cinematic interior keyframe of a crowded 1990s Chinese arcade hall, low ceiling, rows of old arcade cabinets, cigarette smoke, mixed crowd of adult men, teenagers, and children, three schoolchildren with backpacks visible near the entrance as small figures, blue-green CRT glow, gritty social realism, northern Chinese small-town underground game room, balanced composition, high image quality, no cyberpunk neon, no modern screens, no readable text, no watermark",
              "notes": "这一条是游戏厅场景设定核心图，既要乱，又要构图可读。",
              "revision_note": "",
              "output_path": "",
              "versions": [
                {
                  "version_id": "current",
                  "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/007_ACT1_SHOT_007.png",
                  "notes": "",
                  "created_at": "",
                  "status": "rejected",
                  "candidate_id": "",
                  "task_id": "",
                  "packet_id": "",
                  "qa": {}
                }
              ]
            },
            {
              "item_id": "ACT1_SHOT_008",
              "scene_id": "SCN_ARCADE",
              "beat": "镜头转到三个孩子表情",
              "shot_type": "转场反应中近景 / arcing reaction medium close shot",
              "frame_description": "承接后脑入场镜头，摄影机从三个孩子身后缓缓绕到他们前侧，第一次看见三张被CRT光照亮的脸：哥哥戴眼镜努力镇定，二弟和小弟兴奋又不安。孩子的眼神仍然越过镜头看向游戏厅内部。",
              "spatial_logic": "这是入场镜头的反打/转身后半段：镜头已绕到孩子前侧，但孩子视线仍朝向游戏厅屏幕方向，不是回头看门外。背景应是游戏厅内部光影，不要破坏前一镜头的入场轴线。",
              "image_prompt": "Cinematic realism, 1990s northern Chinese small-town hidden arcade, smoky air, blue-green CRT glow, worn concrete, old bulky CRT arcade cabinets, muted film grain, no modern screens, no smartphone, no readable text, no watermark. Medium close reaction shot after an arcing camera move: three Chinese schoolboys inside the arcade, faces lit by CRT glow. A Lei wears glasses and a dark blue tracksuit trying to stay calm; middle brother in blue jacket with red scarf and backpack; youngest chubby boy in brown vest. Their eyes look past camera toward the arcade screens, excited and uneasy, smoky arcade background.",
              "notes": "这个镜头负责补“表情”，但必须承接前面后脑入场的方向。",
              "revision_note": "",
              "output_path": "08_generation/jobs/IDEA_IMG_20260616_013841/outputs/008_ACT1_SHOT_008.png",
              "versions": []
            }
          ],
          "related_assets": [
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "03_story",
              "asset_id": "SCN_COMPOUND_STORY_BEATS",
              "kind": "",
              "role": "beat_sheet",
              "path": "03_story/beats/coin_slot_sample_beat_sheet.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "03_story",
              "asset_id": "SCN_COMPOUND_FULL_SHOT_LIST",
              "kind": "",
              "role": "full_shot_list",
              "path": "07_shots/shot_list.csv"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "04_lookdev",
              "asset_id": "SCN_COMPOUND_LOOK_BIBLE",
              "kind": "",
              "role": "look_bible",
              "path": "04_lookdev/references/coin_slot_look_bible_v001.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "04_lookdev",
              "asset_id": "SCN_COMPOUND_COLOR_SCRIPT",
              "kind": "",
              "role": "color_script",
              "path": "04_lookdev/palettes/coin_slot_color_script.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "04_lookdev",
              "asset_id": "SCN_COMPOUND_VISUAL_REFS",
              "kind": "",
              "role": "visual_references",
              "path": "04_lookdev/references/coin_slot_visual_references.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "04_lookdev",
              "asset_id": "SCN_COMPOUND_SCENE_REFERENCE",
              "kind": "",
              "role": "scene_reference",
              "path": "media/01_AIGC/scene_refs/SC_01_compound_corner_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "05_asset_bible",
              "asset_id": "SCN_COMPOUND_CHARACTER_STAGE_LOCKS",
              "kind": "",
              "role": "character_stage_locks",
              "path": "05_asset_bible/character_stage_locks/coin_slot_character_stage_locks.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "05_asset_bible",
              "asset_id": "SCN_COMPOUND_LOCATION_BIBLE",
              "kind": "",
              "role": "location_bible",
              "path": "05_asset_bible/locations/coin_slot_location_bible.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "05_asset_bible",
              "asset_id": "SCN_COMPOUND_CONTINUITY_LOCKS",
              "kind": "",
              "role": "continuity_locks",
              "path": "05_asset_bible/continuity/coin_slot_continuity_locks.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "SCN_COMPOUND_SCENE_LOCK",
              "kind": "",
              "role": "scene_lock",
              "path": "06_previs/scene_locks/scn-compound/scene_lock.yaml"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "SCN_COMPOUND_CAMERA_MANIFEST",
              "kind": "",
              "role": "camera_manifest",
              "path": "06_previs/scene_locks/scn-compound/camera_manifest.csv"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "SCN_COMPOUND_REFERENCE_ASSETS",
              "kind": "",
              "role": "reference_assets",
              "path": "06_previs/scene_locks/scn-compound/reference_assets.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "SCN_COMPOUND_WHITEBOX_INDEX",
              "kind": "",
              "role": "whitebox_index",
              "path": "06_previs/scene_locks/scn-compound/whitebox_index.csv"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB001_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB002_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB002.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB003_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB003.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB004_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB004.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB005_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB005.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB006_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB006.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB007_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB007.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB008_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB008.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB009_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB009.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB010_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB010.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB011_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB011.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB012_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB012.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB013_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB013.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB014_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB014.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB015_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB015.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB016_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB016.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB017_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB017.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "06_previs",
              "asset_id": "MSB018_WHITEBOX",
              "kind": "",
              "role": "whitebox",
              "path": "media/01_AIGC/whitebox_renders_v2/B01/WB2_COMPOUND_MSB018.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "07_shots",
              "asset_id": "SCN_COMPOUND_SHOT_LIST",
              "kind": "",
              "role": "shot_list",
              "path": "07_shots/shot_list.csv"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "07_shots",
              "asset_id": "MSB001_IMAGE_PROMPT",
              "kind": "",
              "role": "image_prompt",
              "path": "07_shots/prompts/MSB001.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "07_shots",
              "asset_id": "MSB003_IMAGE_PROMPT",
              "kind": "",
              "role": "image_prompt",
              "path": "07_shots/prompts/MSB003.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "07_shots",
              "asset_id": "MSB006_IMAGE_PROMPT",
              "kind": "",
              "role": "image_prompt",
              "path": "07_shots/prompts/MSB006.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "07_shots",
              "asset_id": "MSB009_IMAGE_PROMPT",
              "kind": "",
              "role": "image_prompt",
              "path": "07_shots/prompts/MSB009.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "07_shots",
              "asset_id": "MSB012_IMAGE_PROMPT",
              "kind": "",
              "role": "image_prompt",
              "path": "07_shots/prompts/MSB012.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "07_shots",
              "asset_id": "SCN_COMPOUND_SHOT_INDEX_188",
              "kind": "",
              "role": "scene_shot_index",
              "path": "07_shots/scene_slices/SCN_COMPOUND_shot_index.csv"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "07_shots",
              "asset_id": "SCN_COMPOUND_PROMPT_PACK_188",
              "kind": "",
              "role": "scene_prompt_pack",
              "path": "07_shots/scene_slices/SCN_COMPOUND_prompt_pack.csv"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "07_shots",
              "asset_id": "MSB001_VIDEO_PROMPT",
              "kind": "",
              "role": "video_prompt",
              "path": "07_shots/video_prompts/MSB001.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "07_shots",
              "asset_id": "MSB003_VIDEO_PROMPT",
              "kind": "",
              "role": "video_prompt",
              "path": "07_shots/video_prompts/MSB003.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "07_shots",
              "asset_id": "MSB006_VIDEO_PROMPT",
              "kind": "",
              "role": "video_prompt",
              "path": "07_shots/video_prompts/MSB006.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "07_shots",
              "asset_id": "MSB009_VIDEO_PROMPT",
              "kind": "",
              "role": "video_prompt",
              "path": "07_shots/video_prompts/MSB009.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "07_shots",
              "asset_id": "MSB012_VIDEO_PROMPT",
              "kind": "",
              "role": "video_prompt",
              "path": "07_shots/video_prompts/MSB012.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "SCN_COMPOUND_IMAGE_OUTPUT_INDEX",
              "kind": "",
              "role": "image_outputs",
              "path": "08_generation/outputs/images/coin_slot_image_outputs_index.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "SCN_COMPOUND_REJECT_LOG",
              "kind": "",
              "role": "rejects",
              "path": "08_generation/rejects/coin_slot_reject_log.md"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "SCN_COMPOUND_STORYBOARD_IMAGE_INDEX",
              "kind": "",
              "role": "storyboard_image_index",
              "path": "08_generation/outputs/images/SCN_COMPOUND_storyboard_image_index.csv"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB001_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB001_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB001_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB001_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB002_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB002_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB002_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB002_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB003_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB003_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB003_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB003_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB004_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB004_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB004_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB004_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB005_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB005_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB005_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB005_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB006_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB006_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB006_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB006_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB007_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB007_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB007_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB007_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB008_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB008_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB008_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB008_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB009_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB009_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB009_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB009_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB010_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB010_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB010_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB010_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB011_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB011_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB011_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB011_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB012_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB012_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB012_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB012_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB013_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB013_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB013_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB013_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB014_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB014_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB014_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB014_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB015_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB015_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB015_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB015_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB016_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB016_v001.png"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB016_FINAL_STORYBOARD",
              "kind": "",
              "role": "final_storyboard_panel",
              "path": "media/01_AIGC/final_storyboard_panels/B01/MSB016_final_storyboard_v002.jpg"
            },
            {
              "scene_id": "SCN_COMPOUND",
              "scene_title": "居民楼角落 / Compound corner",
              "step": "08_generation",
              "asset_id": "MSB017_PURE_KEYFRAME",
              "kind": "",
              "role": "storyboard_keyframe",
              "path": "media/01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB017_v001.png"
            }
          ]
        },
        "whitebox_guidance": [
          "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
          "Whitebox guidance / 白模读取说明\n- Use this whitebox as the fixed two-player arcade cabinet prop lock: one shared CRT screen, left/right control stations, wide control deck, front coin slot, and two low stools.\n- Preserve A Lei and the yellow-haired punk as side-by-side players facing the same screen; do not turn them face-to-face or toward camera in duel shots.\n- Preserve screen/control-panel/stool height relationships for rear-head shots and game-screen inserts.\n- Do not copy white material, primitive geometry, or clean test-render look; convert it into gritty 1990s Chinese arcade materials.\n- Negative constraint: no modern LCD, no esports setup, no readable logos, no cyberpunk arcade."
        ]
      },
      "whitebox_guidance": [
        "Whitebox guidance / 白模读取说明:\n- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.\n- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.\n- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.\n- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.\n- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.\n- Source whitebox replica seed: ACT1_SHOT_003_SOURCE_KEYFRAME.\n- Replica intent / 复刻意图: 以 ACT1_SHOT_003 为母图，尽量 1:1 复刻旧墙、暗金属门、猫眼、门把手、三名孩子在左侧等待的站位、眼线高度和画面比例；白模用于后续第一幕同场景改机位/光照/动作。",
        "Whitebox guidance / 白模读取说明\n- Use this whitebox as the fixed two-player arcade cabinet prop lock: one shared CRT screen, left/right control stations, wide control deck, front coin slot, and two low stools.\n- Preserve A Lei and the yellow-haired punk as side-by-side players facing the same screen; do not turn them face-to-face or toward camera in duel shots.\n- Preserve screen/control-panel/stool height relationships for rear-head shots and game-screen inserts.\n- Do not copy white material, primitive geometry, or clean test-render look; convert it into gritty 1990s Chinese arcade materials.\n- Negative constraint: no modern LCD, no esports setup, no readable logos, no cyberpunk arcade."
      ],
      "suggested_version_id": "v002",
      "suggested_candidate_outputs": [
        {
          "candidate_id": "c01",
          "version_id": "v002_c01",
          "output_path": "08_generation/jobs/CARD_IMG_20260619_140906/outputs/001_ACT1_SHOT_001_v002_c01.png",
          "output_absolute_path": "/Users/jaychoupp/Desktop/Story/Film/projects/coin-slot/08_generation/jobs/CARD_IMG_20260619_140906/outputs/001_ACT1_SHOT_001_v002_c01.png"
        },
        {
          "candidate_id": "c02",
          "version_id": "v002_c02",
          "output_path": "08_generation/jobs/CARD_IMG_20260619_140906/outputs/001_ACT1_SHOT_001_v002_c02.png",
          "output_absolute_path": "/Users/jaychoupp/Desktop/Story/Film/projects/coin-slot/08_generation/jobs/CARD_IMG_20260619_140906/outputs/001_ACT1_SHOT_001_v002_c02.png"
        },
        {
          "candidate_id": "c03",
          "version_id": "v002_c03",
          "output_path": "08_generation/jobs/CARD_IMG_20260619_140906/outputs/001_ACT1_SHOT_001_v002_c03.png",
          "output_absolute_path": "/Users/jaychoupp/Desktop/Story/Film/projects/coin-slot/08_generation/jobs/CARD_IMG_20260619_140906/outputs/001_ACT1_SHOT_001_v002_c03.png"
        }
      ],
      "suggested_output_path": "08_generation/jobs/CARD_IMG_20260619_140906/outputs/001_ACT1_SHOT_001_v002_c01.png",
      "suggested_output_absolute_path": "/Users/jaychoupp/Desktop/Story/Film/projects/coin-slot/08_generation/jobs/CARD_IMG_20260619_140906/outputs/001_ACT1_SHOT_001_v002_c01.png"
    }
  ]
}
```