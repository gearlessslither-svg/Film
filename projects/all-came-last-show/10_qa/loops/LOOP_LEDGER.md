# Loop Ledger

Project: `all-came-last-show`
Started: 2026-07-17T02:17:33+08:00

## Attempts

### 2026-07-17 - Director override: wild-return ending

- Verdict: `branch_superseded`
- Failure labels: `director_override`, `ending_replaced`, `character_state_added`, `sequence_missing`, `prop_spacing`
- Feedback: 演出结束后动物脱去华服，工装已经丢失；所有角色从两足拟人状态变为四足野生动物，离开破败城镇走向荒野与新生。乐器不得密集靠在一起。
- Prompt patch: 新增三状态转换账本；人设板取消密集乐器陈列；所有旧双状态配角板退出活动参考链；故事 V2 通过前停止下游生图。

### 2026-07-17T02:28:16+08:00 - LOOKDEV_V1 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/LOOKDEV_V1/attempt_001`
- Failure labels: `director_override`, `style_branch_superseded`, `too_realistic`, `world_rule_replaced`
- Feedback:

> 导演否决：画面过于写实；改用所附DFT童话参考，并将居民改为穿工装的拟人动物。

### 2026-07-17T02:47:00+08:00 - ABAI_DUAL_STATE_SHEET_V1 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/ABAI_DUAL_STATE_SHEET_V1/attempt_001`
- Failure labels: `director_override`, `character_identity_replaced`, `reference_identity_mismatch`
- Feedback:

> 导演提供三张真实猫照片，要求阿白照此猫的真实身份、毛长、眼色与灰黑花纹重新设计；上一版虚构黑毛撮、琥珀眼和肋部条纹作废。

### 2026-07-17T02:51:20+08:00 - ABAI_DUAL_STATE_SHEET_V1 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/ABAI_DUAL_STATE_SHEET_V1/attempt_002`
- Failure labels: none
- Feedback:

> 导演确认：很好。批准照片身份版阿白双状态人设板，记入正式人设版。

### 2026-07-17T02:58:31+08:00 - SUPPORTING_CAST_B_V1 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SUPPORTING_CAST_B_V1/attempt_001`
- Failure labels: `prop_state_mismatch`, `continuity_drift`
- Feedback:

> 自动表面质检通过，但语义质检失败：熊在工厂状态提前端着宴会托盘与两只酒杯。

### 2026-07-17T03:00:09+08:00 - SUPPORTING_CAST_A_V1 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SUPPORTING_CAST_A_V1/attempt_001`
- Failure labels: `director_override`, `ending_replaced`, `character_state_missing`, `prop_spacing`
- Feedback:

> 导演新增苍凉结尾：演出后动物脱去华服，工装已丢失，拟人两足状态转为彻底四足野生动物并离城；同时要求乐器不要靠得太近。当前双状态板缺少野生状态且乐器密集，退出活动参考链。
### 2026-07-17T03:11:05+08:00 - KS21_02_SQUARE_LAST_PERFORMANCE / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/KS21_02_SQUARE_LAST_PERFORMANCE/attempt_001`
- Failure labels: `reference_state_leak`, `species_diversity_lost`, `crowd_identity_duplication`
- Feedback:

> 表面质量与构图可用，但语义质检失败：阿白猫身份泄漏到整个人群，广场居民几乎全部变成猫，违反多物种世界锁。

### 2026-07-17T03:16:10+08:00 - KS21_03_WILD_DEPARTURE_DAWN / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/KS21_03_WILD_DEPARTURE_DAWN/attempt_001`
- Failure labels: `continuity_drift`, `environment_state_mismatch`
- Feedback:

> 构图与物种状态基本成立，但终局城镇烟囱仍在冒烟，像仍在生产，违背工厂停摆、拆除后空城的结尾状态。

### 2026-07-17T03:20:15+08:00 - KS21_03_WILD_DEPARTURE_DAWN / attempt_002

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/KS21_03_WILD_DEPARTURE_DAWN/attempt_002`
- Failure labels: `apocalypse_drift`, `environment_state_overdamaged`
- Feedback:

> 烟囱冷却与八种四足动物已修正，但城镇被画成大面积坍塌废墟，超过剧本所需的停摆、拆除与破败程度，漂移成末日景观。

### 2026-07-17T03:53:08+08:00 - ENV-01_LOCKER_ROOM_SETTING / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/ENV-01_LOCKER_ROOM_SETTING/attempt_001`
- Failure labels: `style_drift`, `photoreal_concept_art_drift`
- Feedback:

> Surface QA passes, but the scene reads as realistic digital concept art instead of the director's flat DFT old-paper tempera fairy-tale language.

### 2026-07-17T03:55:05+08:00 - ENV-01_LOCKER_ROOM_SETTING / attempt_002

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/ENV-01_LOCKER_ROOM_SETTING/attempt_002`
- Failure labels: none
- Feedback:

> DFT flattening and palette now materially improved; spatial lock is readable. Awaiting director visual approval before promotion.

### 2026-07-17T04:04:09+08:00 - ENV-02_SQUARE_DANCEHALL_SETTING / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/ENV-02_SQUARE_DANCEHALL_SETTING/attempt_001`
- Failure labels: none
- Feedback:

> Composition, no-smoke chimney, square-hall axis and DFT palette pass internal review; awaiting director visual approval.

### 2026-07-17T04:04:33+08:00 - ENV-01_WHITEBOX / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/ENV-01_WHITEBOX/attempt_001`
- Failure labels: none
- Feedback:

> Master, overhead and interior reverse views are readable; awaiting director approval.

### 2026-07-17T04:04:33+08:00 - ENV-02_WHITEBOX / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/ENV-02_WHITEBOX/attempt_001`
- Failure labels: none
- Feedback:

> Master and overhead geography pass; hall reverse is readable after camera repair. Awaiting director approval.

### 2026-07-17T05:06:14+08:00 - FIN-005 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/FIN-005/attempt_001`
- Failure labels: `narrative_state_mismatch`
- Feedback:

> Elephant drifted back into dark-blue workwear during private-dress phase.

### 2026-07-17T05:06:14+08:00 - FIN-006 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/FIN-006/attempt_001`
- Failure labels: `narrative_state_mismatch`
- Feedback:

> Elephant wore dark-blue workwear during private-dress travel phase.

### 2026-07-17T05:06:14+08:00 - FIN-011B / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/FIN-011B/attempt_001`
- Failure labels: `sequence_missing`
- Feedback:

> Middle anchor skipped directly to complete quadruped form.

### 2026-07-17T05:06:14+08:00 - FIN-011B / attempt_002

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/FIN-011B/attempt_002`
- Failure labels: `narrative_state_mismatch`
- Feedback:

> Halfway posture passed, but garments remained on bodies after the last-clothes boundary.

### 2026-07-17T05:06:15+08:00 - FIN-001 / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-001/attempt_001`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T05:06:15+08:00 - FIN-002 / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-002/attempt_001`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T05:06:15+08:00 - FIN-003 / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-003/attempt_001`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T05:06:16+08:00 - FIN-004 / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-004/attempt_001`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T05:06:16+08:00 - FIN-005 / attempt_002

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-005/attempt_002`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T05:06:17+08:00 - FIN-006 / attempt_002

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-006/attempt_002`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T05:06:17+08:00 - FIN-007 / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-007/attempt_001`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T05:06:17+08:00 - FIN-008 / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-008/attempt_001`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T05:06:18+08:00 - FIN-009 / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-009/attempt_001`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T05:06:18+08:00 - FIN-010 / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-010/attempt_001`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T05:06:18+08:00 - FIN-011A / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-011A/attempt_001`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T05:06:19+08:00 - FIN-011B / attempt_003

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-011B/attempt_003`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T05:06:19+08:00 - FIN-011C / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-011C/attempt_001`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T05:06:19+08:00 - FIN-012A / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-012A/attempt_001`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T05:06:20+08:00 - FIN-012B / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-012B/attempt_001`
- Failure labels: none
- Feedback:

> Internal semantic, composition and surface QA passed; awaiting director aesthetic approval.

### 2026-07-17T10:24:38+08:00 - FINAL_FRAMES_120S_COVERAGE_V1 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/FINAL_FRAMES_120S_COVERAGE_V1/attempt_001`
- Failure labels: `runtime_undercoverage`, `missing_intermediate_beat`, `hero_frame_overload`, `character_environment_scale_mismatch`, `architectural_scale_collapse`, `perspective_scale_inconsistency`, `group_action_repetition`, `performance_clone`, `transformation_phase_flattening`, `duplicate_character_instance`
- Feedback:

> 导演确认：15张仅是视觉锚点，不能支撑120秒；部分建筑比同平面动物还小；穿脱衣与变形群像动作雷同。

### 2026-07-17T10:24:56+08:00 - SHOT_COVERAGE_120S_V2 / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/SHOT_COVERAGE_120S_V2/attempt_001`
- Failure labels: `director_review_pending`
- Feedback:

> 内部覆盖核验：00:00–02:00无缺口；38镜42帧；烟囱、变形、结尾使用多锚点；尺度与群像动作账本已建立。等待导演确认颗粒度和旧图取舍后才能生成。

### 2026-07-17T10:30:55+08:00 - FIN-001 / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-001/attempt_001`
- Failure labels: none
- Feedback:

> 保留为3–5秒城镇地理锚点；不得继续承担10秒段落。

### 2026-07-17T10:30:55+08:00 - FIN-002 / attempt_001

- Verdict: `revise`
- Attempt: `10_qa/loops/attempts/FIN-002/attempt_001`
- Failure labels: `character_environment_scale_mismatch`
- Feedback:

> 队列同步可保留，但大型物种通行尺度未被证明。

### 2026-07-17T10:30:55+08:00 - FIN-003 / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-003/attempt_001`
- Failure labels: none
- Feedback:

> 保留为3秒机器大厅锚点；透视与工业尺度成立。

### 2026-07-17T10:30:55+08:00 - FIN-004 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/FIN-004/attempt_001`
- Failure labels: `group_action_repetition`, `performance_clone`
- Feedback:

> 群体几乎同时双手拿工装，脱衣动作克隆。

### 2026-07-17T10:30:55+08:00 - FIN-005 / attempt_002

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/FIN-005/attempt_002`
- Failure labels: `group_action_repetition`, `performance_clone`
- Feedback:

> 多数角色同时在胸前系扣或整理领口。

### 2026-07-17T10:30:55+08:00 - FIN-006 / attempt_002

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/FIN-006/attempt_002`
- Failure labels: `character_environment_scale_mismatch`, `architectural_scale_collapse`, `perspective_scale_inconsistency`
- Feedback:

> 同景深门窗小于动物，人物方向也不像向灯光汇聚。

### 2026-07-17T10:30:55+08:00 - FIN-007 / attempt_001

- Verdict: `revise`
- Attempt: `10_qa/loops/attempts/FIN-007/attempt_001`
- Failure labels: `character_environment_scale_mismatch`, `group_action_repetition`
- Feedback:

> 广场构图可保留，但礼堂门未证明大象可通行，多人重复端杯对谈。

### 2026-07-17T10:30:56+08:00 - FIN-008 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/FIN-008/attempt_001`
- Failure labels: `group_action_repetition`, `performance_clone`, `crowd_choreography_flattening`
- Feedback:

> 多组舞伴重复双手相握摇摆，节拍相位雷同。

### 2026-07-17T10:30:56+08:00 - FIN-009 / attempt_001

- Verdict: `revise`
- Attempt: `10_qa/loops/attempts/FIN-009/attempt_001`
- Failure labels: `duplicate_character_instance`, `sequence_missing`
- Feedback:

> 集体凝视可以保留，但画面出现两个大象，且缺烟囱直立起始锚点。

### 2026-07-17T10:30:56+08:00 - FIN-010 / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-010/attempt_001`
- Failure labels: none
- Feedback:

> 空钩揭示与家具尺度可保留为2秒主镜头；集体短暂停顿有叙事理由。

### 2026-07-17T10:30:56+08:00 - FIN-011A / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/FIN-011A/attempt_001`
- Failure labels: `group_action_repetition`, `performance_clone`
- Feedback:

> 所有角色以近似姿势拿衣服，重复导演指出的脱衣同动作。

### 2026-07-17T10:30:56+08:00 - FIN-011B / attempt_003

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/FIN-011B/attempt_003`
- Failure labels: `transformation_phase_flattening`, `group_action_repetition`
- Feedback:

> 所有角色处于同一爬行相位，且状态边界不清。

### 2026-07-17T10:30:56+08:00 - FIN-011C / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/FIN-011C/attempt_001`
- Failure labels: `duplicate_character_instance`, `performance_clone`, `character_environment_scale_mismatch`
- Feedback:

> 野生状态像物种陈列，出现重复狐狸、动物站上长凳，出口尺度存疑。

### 2026-07-17T10:30:56+08:00 - FIN-012A / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/FIN-012A/attempt_001`
- Failure labels: `character_environment_scale_mismatch`, `architectural_scale_collapse`, `perspective_scale_inconsistency`, `duplicate_character_instance`
- Feedback:

> 动物与镇缘整栋房屋接近或更大，纵深关系失效，另有重复狐狸。

### 2026-07-17T10:30:56+08:00 - FIN-012B / attempt_001

- Verdict: `hold`
- Attempt: `10_qa/loops/attempts/FIN-012B/attempt_001`
- Failure labels: none
- Feedback:

> 阿白与远处城镇尺度成立，可作2–3秒回望起始锚点。

### 2026-07-17T10:53:41+08:00 - SH10 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH10/attempt_001`
- Failure labels: none
- Feedback:

> 内部语义审查通过：八个物种各一个，八种动作与相位清楚；阿白唯一；大象—门、兔—低钩两组尺度成立；镜中狐狸是同一角色的单一反射层。

### 2026-07-17T10:53:41+08:00 - SH18 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH18/attempt_001`
- Failure labels: none
- Feedback:

> 内部语义审查通过：五个角色从不同道路向同一灯光汇聚；动物远小于同平面门窗和楼层；大象—候车棚、兔—住宅两组尺度成立；无重复物种。

### 2026-07-17T11:06:46+08:00 - SH27 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH27/attempt_001`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: unique multi-species cast, differentiated actions, usable hall scale for elephant, DFT matte-gouache coherence, correct biped performance phase, no horror or duplicate main species; surface QA pass. Director aesthetic review remains pending.

### 2026-07-17T11:10:34+08:00 - SH14 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH14/attempt_001`
- Failure labels: `prompt_drift`
- Feedback:

> 表面与风格QA通过，但琴盒盖接近完全打开，未命中IMAGE PROMPT规定的约20–35度动作相位；源图无法无缝承接既定I2V起点。

### 2026-07-17T11:10:39+08:00 - SH03 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH03/attempt_001`
- Failure labels: none
- Feedback:

> 内部语义审查通过：狗鞋、羊蹄、兔足、大象脚四种足部清楚；动作相位错开；地标线、脚地接触与相对尺度可信；DFT旧纸低噪，无文字与肢体复制。

### 2026-07-17T11:13:24+08:00 - SH14 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH14/attempt_002`
- Failure labels: none
- Feedback:

> 内部语义审查通过：唯一照片锁阿白、演出服与唯一完整小提琴成立；琴盒保持低角度部分开启且爪—盒沿接触可读；柜、凳、门、角色比例成立；DFT旧纸蛋彩清晰低噪，无额外肢体或文字。

### 2026-07-17T11:13:27+08:00 - SH04 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH04/attempt_001`
- Failure labels: `duplicate_character_instance`, `style_drift`, `noisy_microdetail`
- Feedback:

> 硬失败：背景出现多只清楚羊形队列，复制活动角色；毛发与旧铁高频写实、过暗过厚，偏离DFT平面旧纸蛋彩。主爪—空白卡—打卡机接触可保留。

### 2026-07-17T11:15:46+08:00 - SH04 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH04/attempt_002`
- Failure labels: none
- Feedback:

> 内部语义审查通过：背景复制羊已清除；仅一只老狗主爪和一只等待羊蹄；两张工牌空白；打卡机、槽口与抓握接触成立；DFT平面旧纸风和低噪恢复。

### 2026-07-17T11:16:09+08:00 - SH28_KF01 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH28_KF01/attempt_001`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: intact smoke-free 45–60m chimney reads above real town floors; fixed telephoto axis, safe left fall space, non-apocalyptic DFT treatment, surface QA pass. Center crop/resample normalized to 1915x821 without changing story content. Director review pending.

### 2026-07-17T11:16:33+08:00 - SH15 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH15/attempt_001`
- Failure labels: `narrative_state_mismatch`
- Feedback:

> 多物种、动作差异、门洞尺度与DFT表面通过，但阿白头顶生成了带硬边帽檐的深蓝帽，演出状态不允许工帽或任何帽子。

### 2026-07-17T11:18:22+08:00 - SH28_KF02 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH28_KF02/attempt_001`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: same telephoto town and scale family, intact chimney leans left toward empty industrial space, no smoke/fire/explosion or architectural collapse, low restrained base disturbance, surface QA pass. Director review pending.

### 2026-07-17T11:18:50+08:00 - SH07 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH07/attempt_001`
- Failure labels: none
- Feedback:

> 内部语义审查通过：与SH06同一机器家族、氧化绿材质和高窗光；轮带与轴承结构可信，表针接近零位且无伪数字；尘粒局限于横梁下方，不是烟雾；无人无文字，表面QA通过。

### 2026-07-17T11:20:04+08:00 - SH15 / attempt_002

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH15/attempt_002`
- Failure labels: `identity_redraw`
- Feedback:

> 帽子已移除且群像保持，但阿白照片锁的非对称灰黑天然头顶斑一并被抹去，身份锚缺失。

### 2026-07-17T11:22:10+08:00 - SH11 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH11/attempt_001`
- Failure labels: `narrative_state_mismatch`, `prompt_drift`
- Feedback:

> 硬失败：羊与背景兔仍穿完整带口袋深蓝工装，同时又折叠/挂另一件工装，违背第一次脱衣阶段和本镜角色状态。折叠抓握、凳钩尺度、两种动作可保留。

### 2026-07-17T11:23:08+08:00 - SH29 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH29/attempt_001`
- Failure labels: `continuity_drift`, `unlocked_smoke`
- Feedback:

> Hard semantic reject despite surface QA pass: a visible smoke plume appears from a chimney through the hall door, contradicting the stopped factory/no-smoke continuity. Cast diversity, action staggering, anatomy, scale and composition may be kept.

### 2026-07-17T11:23:37+08:00 - SH15 / attempt_003

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH15/attempt_003`
- Failure labels: `identity_redraw`
- Feedback:

> 第二次局部编辑仍未恢复阿白非对称灰黑天然头顶斑；其余内容保持正确。

### 2026-07-17T11:26:15+08:00 - SH11 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH11/attempt_002`
- Failure labels: none
- Feedback:

> 内部语义审查通过：深蓝工装只存在于凳面与低钩，角色身体不再穿工装；羊蹄从画外压平已折衣物，另一前肢在画外不构成解剖缺失；兔穿朴素奶白内层挂衣，动作、尺度、接触和低噪均成立。

### 2026-07-17T11:27:03+08:00 - SH15 / attempt_004

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH15/attempt_004`
- Failure labels: none
- Feedback:

> 内部语义审查通过：阿白无帽并恢复不规则天然灰色头顶毛斑；六种物种各一，六个离场相位不同；唯一琴与琴弓成立；大象可通过宽门；肢体道具、DFT媒介和低噪表面通过。

### 2026-07-17T11:27:33+08:00 - SH29 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH29/attempt_002`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: forbidden smoke removed; eight distinct species retain differentiated reaction beats, believable hall scale, correct biped performance state, coherent DFT storybook texture. Director aesthetic review pending.

### 2026-07-17T11:30:26+08:00 - SH12 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH12/attempt_001`
- Failure labels: `identity_redraw`, `anatomy_fail`, `reference_state_leak`
- Feedback:

> 硬失败：阿白尾巴大部被画成白色，违反照片身份的整条深灰蓬松尾；背部鞍状斑过窄像单条纹；前景羊双手接近裸露人类五指。三层构图、狗肩旧伤与更衣室可保留。

### 2026-07-17T11:30:41+08:00 - SH16 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH16/attempt_001`
- Failure labels: none
- Feedback:

> 内部语义审查通过：唯一狐狸两足华服、推门半步与远灯眼线清楚；住宅门窗和檐口明显大于角色、街道尺度真实；无猫、无道具复制、肢体接触可信；DFT旧纸蛋彩清晰低噪。

### 2026-07-17T11:30:56+08:00 - SH15 / attempt_004

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH15/attempt_004`
- Failure labels: none
- Feedback:

> 内部语义审查通过：阿白无帽并恢复不规则天然灰色头顶毛斑；六种物种各一，六个离场相位不同；唯一琴与琴弓成立；大象可通过宽门；肢体道具、DFT媒介和低噪表面通过。attempt_004 是仅修复单一身份锚（阿白天然头顶毛斑）的受控例外；attempt_001–003 均为失败证据，未进入 selected，未被链入任何下游生成或交付。

### 2026-07-17T11:31:34+08:00 - SH30 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH30/attempt_001`
- Failure labels: none
- Feedback:

> Hard semantic failure: background contains an orderly row of roughly sixteen readable biped silhouettes, violating the sparse unreadable varied-height non-lineup lock; industrial chimney silhouettes also appear through the doorway although the distant factory is forbidden in this insert.

### 2026-07-17T11:34:06+08:00 - SH30 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH30/attempt_002`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: six tiny irregular retreating silhouettes replace the lineup; forbidden factory stacks are gone; empty stage, practical scale, no smoke/instruments/clothing, and DFT low-noise language hold. Director aesthetic review pending.

### 2026-07-17T11:34:23+08:00 - SH17 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH17/attempt_001`
- Failure labels: `text_artifact`
- Feedback:

> 大象身份、袖口动作、候车棚净空与城镇尺度通过，但站牌下方面板出现不可读伪文字状线条，违反无伪文字硬门禁。

### 2026-07-17T11:35:34+08:00 - SH12 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH12/attempt_002`
- Failure labels: none
- Feedback:

> 硬门禁通过：阿白尾巴从根至尖为深炭灰，背部为自然宽鞍状斑；前景羊仅头部与卷毛柔焦框边，无人类手；三角色唯一、两足更衣状态、老狗肩部普通旧伤、尺度解剖与DFT低噪均成立。

### 2026-07-17T11:36:44+08:00 - SH17 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH17/attempt_002`
- Failure labels: none
- Feedback:

> 内部语义审查通过：下方站牌为无字风化金属面，无伪文字；唯一大象、两足华服、单袖整理、鼻牙和手爪结构可信；棚顶净空、长椅与城镇建筑尺度成立；DFT旧纸蛋彩清晰低噪。

### 2026-07-17T11:38:52+08:00 - SH31 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH31/attempt_001`
- Failure labels: `group_action_repetition`, `continuity_drift`, `anatomy_prop_error`
- Feedback:

> Hard semantic failure: although the eight species and building scale are good, the ensemble reads mainly as the same walking action; Abai is not the last/nearest departing figure, and the bear does not visibly support the only closed case with both paws.

### 2026-07-17T11:39:23+08:00 - SH02 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH02/attempt_001`
- Failure labels: none
- Feedback:

> 硬门禁通过：厂房与门洞明显大于角色且象可自然通过；狗、羊、兔、象、驴五物种唯一，分处跨门、静候、抬爪打卡、出门、沿坡接近五相位；抓牌、脚地接触与肢体成立；DFT哑光旧纸、低噪且无猫群。

### 2026-07-17T11:41:18+08:00 - SH19 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH19/attempt_001`
- Failure labels: none
- Feedback:

> 内部语义审查通过：狐、羊、象、狗、兔五物种各一且无猫；五种步幅与落足相位不同、前后层次分开，不形成齐步队列；足腿归属可追踪；街道、路灯和建筑比例真实；DFT媒介清晰低噪。

### 2026-07-17T11:43:12+08:00 - SH31 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH31/attempt_002`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: exactly eight unique species, Abai is the last near-right figure with correct markings and empty paws, bear is one layer ahead with the single closed case, distinct rabbit/donkey/dog/sheep beats read, and architecture remains convincingly larger than all animals. Director aesthetic review pending.

### 2026-07-17T11:43:13+08:00 - SH05 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH05/attempt_001`
- Failure labels: `group_action_duplication`, `composition_failure`, `identity_redraw`
- Feedback:

> 硬失败：八物种计数正确、门洞尺度正常，但角色被排成近乎单一横列，羊与兔同时持卡、其余多为相同双臂垂落站姿，缺少前中后三层和八种动作相位；阿白尾巴出现浅白段，未锁为整条深灰。

### 2026-07-17T11:45:50+08:00 - SH20 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH20/attempt_001`
- Failure labels: `duplicate_character_instance`
- Feedback:

> 三区空间、唯一低音提琴、象门洞尺度和动作分区成立，但右侧长桌出现两名年长绵羊实例，违反每种活动主角色最多一个。

### 2026-07-17T11:47:30+08:00 - SH32 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH32/attempt_001`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: exactly eight unique species in staggered entry phases; rabbit stops first, Abai reads behind, bear has the single closed case, dog signals back, and elephant remains outside fully readable below an oversized doorway. Empty hooks/cabinets are explicit, scale and DFT low-noise style hold. Director aesthetic review pending.

### 2026-07-17T11:47:44+08:00 - SH05 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH05/attempt_001`
- Failure labels: `group_action_repetition`, `group_action_duplication`, `composition_failure`, `identity_redraw`
- Feedback:

> 硬失败：八物种计数正确、门洞尺度正常，但角色被排成近乎单一横列，羊与兔同时持卡、其余多为相同双臂垂落站姿，缺少前中后三层和八种动作相位；阿白尾巴出现浅白段，未锁为整条深灰。

### 2026-07-17T11:47:57+08:00 - SH05 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH05/attempt_002`
- Failure labels: none
- Feedback:

> 硬门禁通过：八物种各一且无背景动物；狗静候、羊错步、兔唯一举卡、象调帽、阿白横移、驴微驼、熊宽站、狐狸侧望形成八相位并分布于前中后三层；门洞和高窗显著大于角色，象有净空；阿白整条深灰尾，解剖抓握和DFT低噪成立。

### 2026-07-17T11:49:19+08:00 - SH20 / attempt_002

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH20/attempt_002`
- Failure labels: `character_removed`
- Feedback:

> 重复绵羊已消失，但编辑同时移除了应保留的切面包绵羊，镜头只剩六种物种，未满足七角色地理建立。

### 2026-07-17T11:52:27+08:00 - SH08 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH08/attempt_001`
- Failure labels: none
- Feedback:

> 硬门禁通过：八物种各一，队伍跨前中后三层向院外流动；兔已过门、狗过门槛、羊侧让手势、熊慢步、狐狸贴墙、驴长步、大象最后留门内，只有阿白在右中半步停顿并回望；厂门完整且象有净空，阿白整条深灰尾，脚地接触与DFT低噪成立。

### 2026-07-17T11:52:48+08:00 - SH34 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH34/attempt_001`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: exactly eight unique species perform eight immediately distinct clothing actions (sleeve, vest button, fold coat, draw scarf, shoe, boot, shawl, shoulder-shirt); all remain fur-covered upright bipeds, no body transition, closed case stays separate, and room scale/style are coherent. Director aesthetic review pending.

### 2026-07-17T11:55:27+08:00 - SH20 / attempt_003

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH20/attempt_003`
- Failure labels: none
- Feedback:

> 通过：宽幅舞厅空间的人类尺度门洞、长桌与舞台比例可信；恰好七个非猫物种且各一只（狗、狐、驴、象、熊、羊、兔）；动作区分清楚：狗演奏唯一低音提琴、狐与驴处于不同舞步相位、象进门、熊摆杯、羊切面包、兔搬凳；肢体与道具可读，DFT童话质感稳定且无可见文字噪点。

### 2026-07-17T11:57:04+08:00 - SH09 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH09/attempt_001`
- Failure labels: `text_artifact`, `identity_redraw`
- Feedback:

> 硬失败：八物种与八动作、室内尺度和解剖均成立，但后门上出现可读 EXIT 标牌，铁柜也残留伪标签；阿白尾巴根部出现浅白段，未保持根至尖整条深炭灰。

### 2026-07-17T11:57:12+08:00 - SH35_KF01 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH35_KF01/attempt_001`
- Failure labels: `group_action_repetition`, `state_transition_mismatch`
- Feedback:

> Hard semantic failure at the boundary anchor: the unclad biped state is safe and anatomically clean, but elephant trunk does not reach the floor, donkey knees remain straight, and sheep/Abai preparation phases read too neutral, weakening the required eight distinct transition starts.

### 2026-07-17T11:59:19+08:00 - SH21 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH21/attempt_001`
- Failure labels: `identity_redraw`
- Feedback:

> 构图、六物种、动作区分、唯一琴弓和建筑比例均合格；但阿白头顶照片锁定的自然灰黑冠斑过淡近乎消失，身份锚不足。

### 2026-07-17T12:00:20+08:00 - SH09 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH09/attempt_002`
- Failure labels: none
- Feedback:

> 硬门禁通过：八物种各一且分处坐、走低钩、停高门、开单柜、最后进入看柜、取空白卡、沿通道走、镜边停看八相位；象门净空、熊凳脚接地、兔低钩尺度成立；所有标牌与柜门文字已清除，阿白尾巴根至尖深炭灰，DFT低噪和解剖成立。

### 2026-07-17T12:00:38+08:00 - SH35_KF01 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH35_KF01/attempt_002`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: exactly eight unique unclad fur-covered bipeds remain anatomically safe; Abai leans, rabbit crouches, bear supports on bench, elephant trunk alone touches floor, dog/fox paws stagger, sheep lowers one side, donkey pre-bends. Clothes and case stay separate; no horror or early quadruped. Director aesthetic review pending.

### 2026-07-17T12:02:32+08:00 - SH21 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH21/attempt_002`
- Failure labels: none
- Feedback:

> 通过：阿白左耳后至冠顶的自然不对称灰黑毛斑已恢复，非帽子或阴影；六物种恰各一只且仅一只猫，兔侧让、羊回望、象行进、熊转椅、狗背向舞台动作互异；唯一琴与弓，门厅对大象尺度充裕，肢体与道具可读，DFT哑光童话风格稳定且无伪文字。

### 2026-07-17T12:03:53+08:00 - SH35_KF02 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH35_KF02/attempt_001`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: same room/cast and prop positions continue from KF01; eight species occupy clearly staggered transition phases, Abai has asymmetric one-paw contact, rabbit is most advanced, and no horror/magic/exposed anatomy/extra limbs appears. Clothing and case remain separate. Director aesthetic review pending.

### 2026-07-17T12:04:05+08:00 - SH13 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH13/attempt_001`
- Failure labels: none
- Feedback:

> 硬门禁通过：八物种各一、八种动作清楚——象单肩披衣、阿白扣背心下扣、羊别披肩侧扣、驴坐系单鞋带、狗卷单袖、熊背向拉背心后调节带、兔扣腰侧、狐狸镜边整理围巾；无乐器托盘酒杯，工装仅静态折挂；室内尺度、解剖抓握、阿白整条深灰尾与DFT低噪均成立。

### 2026-07-17T12:05:08+08:00 - SH22 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH22/attempt_001`
- Failure labels: none
- Feedback:

> 通过：单一阿白身份清楚，灰绿眼、粉鼻、自然不对称冠斑、深灰尾和演出服均锁定；无帽无工装。唯一小提琴与一弓结构可读，肩颌、左爪琴颈、右爪弓与落弦接触可信，无额外肢体或近景乐器；远景仅一不可辨非猫舞者色块。空间尺度、DFT哑光旧纸质感和低噪均合格。

### 2026-07-17T12:07:17+08:00 - SH23 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH23/attempt_001`
- Failure labels: none
- Feedback:

> 通过：画面仅一狐一狗，无猫、第三舞伴、乐器或杯盘；狐狸已交叉落足转出且尾巴滞后，老狗在远后方后重心半步停住，动作相位、朝向与剪影明显不同，未牵手未镜像。四肢和单尾可追踪、脚地接触可信，舞厅建筑尺度远大于角色，DFT哑光低噪风格稳定。

### 2026-07-17T12:08:33+08:00 - SH35_KF03 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH35_KF03/attempt_001`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: exactly eight unique true quadruped species, no clothing or anthropomorphic residue; Abai matches the photo-lock markings and remains cat-sized, rabbit is smallest, elephant largest, other scale tiers are plausible. Eight actions differ and all garments/case remain abandoned. Director aesthetic review pending.

### 2026-07-17T12:09:33+08:00 - SH13 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH13/attempt_001`
- Failure labels: `dimension_mismatch`
- Feedback:

> 语义硬门禁均通过，但文件尺寸为1914×822，未满足交付硬锁1915×821；不得直接入选。

### 2026-07-17T12:09:48+08:00 - SH13 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH13/attempt_002`
- Failure labels: none
- Feedback:

> 精确尺寸硬门禁通过：1915×821；仅做机械尺寸规整，八物种八动作、比例、解剖、服装、阿白身份与DFT低噪语义内容保持不变。

### 2026-07-17T12:10:45+08:00 - SH24 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH24/attempt_001`
- Failure labels: `background_character_leak`
- Feedback:

> 前景六角色与六个指定动作、桌具和尺度基本合格，但中央门洞后出现大量可辨动物群，造成物种重复、动作同质化，并使画面不再是恰好六名角色。

### 2026-07-17T12:12:45+08:00 - SH36 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH36/attempt_001`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: exactly eight unique true quadrupeds leave in staggered phases; rabbit is already outside, fox crosses, Abai remains mid-back, elephant is last and clearly smaller than the oversized doorway. Clothes/case remain inside, no biped/clothing residue, and town architecture dwarfs small animals. Director aesthetic review pending.

### 2026-07-17T12:13:55+08:00 - SH24 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH24/attempt_002`
- Failure labels: none
- Feedback:

> 通过：门洞与舞池背景已完全清空，无人物、猫形或物种重复；全画面恰好熊、羊、狗、象、狐、兔各一。动作互异且道具归属清楚：熊用唯一酒瓶向唯一空杯倒酒、羊递面包、狗空爪侧耳听、象扶桌且鼻下垂、狐空爪轻笑、兔低位拾唯一餐巾；无托盘和乐器。成人长桌、门厅与大厅比例可信，肢体无融合，DFT哑光低噪风格合格。

### 2026-07-17T12:16:27+08:00 - SH37 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH37/attempt_001`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: eight unique animal marks occupy distinct grass, scrub, forest, riverbed and branch routes; town remains real scale, houses dominate every animal, even the elephant is far smaller than a house footprint, and cat/rabbit remain tiny. No duplicated icon pattern or common direction; DFT aerial language holds. Director aesthetic review pending.

### 2026-07-17T12:22:39+08:00 - SH38_KF02 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH38_KF02/attempt_001`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: same single photo-locked Abai, same left-back town/right-front dawn landscape and low axis; four-limb feline run is readable, crown/saddle/dark tail remain continuous, cat stays far below architecture scale, and no duplicate/ghost trail or style drift appears. Director aesthetic review pending.

### 2026-07-17T12:24:06+08:00 - SH25 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH25/attempt_001`
- Failure labels: none
- Feedback:

> 四门通过：scale—二层栏杆、舞池、舞台与长桌形成可信礼堂尺度，大象仍远小于空间；species_action—狐单转、狗后仰停、驴重侧步、兔短步穿行、羊错拍、象肩鼻摆、熊坐姿单足打拍，七物种各一无猫；anatomy_props—脚影承重、单象鼻、蹄爪与尾巴归属清楚，无乐器杯盘；style_noise—DFT旧纸哑光水粉、稀疏节奏与低噪通过自动QA。

### 2026-07-17T12:28:07+08:00 - SH33 / attempt_001

- Verdict: `reject`
- Attempt: `10_qa/loops/attempts/SH33/attempt_001`
- Failure labels: `group_action_repetition`, `performance_clone`, `prop_duplication`, `continuity_drift`
- Feedback:

> Hard semantic failure in reused legacy frame: eight characters mostly repeat the same upright stare toward lockers instead of eight distinct micro-reactions; at least two closed cases are visible and the elephant carries one while the bear does not perform the unique case-setdown continuity beat.

### 2026-07-17T12:29:16+08:00 - SH26 / attempt_001

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH26/attempt_001`
- Failure labels: none
- Feedback:

> 四门通过：scale—驴前景足不超画高35%，兔最小、象足最宽且舞台台沿/桌腿/木板保持正常礼堂尺度；species_action—驴重横落、兔轻短步、象稳足单鼻低摆、狗脚跟小转、羊后撤半步五物种五相位各一无猫；anatomy_props—每腿归属清楚、两腿结构与接触影成立、单象鼻无融合／人脚／额外肢体，无乐器杯盘；style_noise—DFT旧纸哑光水粉低机位、动作边缘清楚且自动QA通过。

### 2026-07-17T12:34:58+08:00 - SH33 / attempt_002

- Verdict: `pass`
- Attempt: `10_qa/loops/attempts/SH33/attempt_002`
- Failure labels: none
- Feedback:

> Internal hard-QA pass: exactly eight unique species perform eight distinct micro-reactions—Abai hook touch, rabbit under-bench check, elephant cabinet open, dog seated, donkey badge-slot check, traceable single fox mirror reflection, sheep shawl hold, bear two-paw setdown. Exactly one closed case exists and elephant is empty-handed; empty hooks/cabinets and real room scale dominate. Director aesthetic review pending.

