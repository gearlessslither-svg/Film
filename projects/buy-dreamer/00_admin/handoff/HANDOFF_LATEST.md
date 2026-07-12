# 项目交接包 / Handoff — buy-dreamer

> 新任务先读本文件、`03_story/scripts/director_shooting_script_v3_male_only.md` 和 `03_story/idea_board/idea_board.json`。不要重新分析前三幕，不要恢复已退出当前 Board 的女主救援结尾，也不要覆盖已有图片版本。

- 项目根：`/Users/jaychoupp/Story/Film/projects/buy-dreamer`
- 工具：Pipeline Hub `http://127.0.0.1:8787`
- 更新时间：2026-07-12
- 当前状态：**男主单线 V3 已生成、质检并回传 Pipeline Hub：7幕/122卡/147版本，122/122 视频提示词，缺失路径0；通用提示词合同与Pipeline Hub回传合同PASS，但叙事状态合同FAIL；M01–M12 共15个候选/制作附件版本均未自动 Final。**
- 2026-07-12全项目复盘：`10_qa/PROJECT_RETROSPECTIVE_20260712.md`。本轮不新增或删除整项skill；已强化`aigc-production-hard-rules`、`aigc-loop-system`、`pipeline-hub-return-guard`并向`aigc-film-project-memory`写入三条经验。
- 已确认遗留债务：当前Board没有顶层`character_state_ledger`，大量卡片缺少`timeline_phase`、`character_state_ids`、`state_transition_rule`及相应prompt标签。下一轮必须先完成122卡迁移并让`validate_narrative_state_contract.py`通过，不能沿用旧的“双门禁PASS”表述。
- 新导演状态锁：遇到买梦人至交易完成并回到现实前，男主始终是下颌至肩部、覆盖耳侧与衣领的长发民谣艺人；从D29现实醒来开始，现实本体始终为短发、无面、空心、机械无灵魂状态。回忆/镜面/影子可显示长发旧人格，但必须是独立时间层。
- 状态账本：`03_story/continuity/character_state_ledger.json`；全量审计：`10_qa/continuity_audit/`；迁移脚本：`10_qa/scripts/repair_narrative_state_and_prompts.py`。
- 多关键帧：FX29–FX33已合并为同一镜头`FX_PUPIL_OT`的01–05锚点，故事板大图为`10_qa/continuity_audit/storyboard_sheets/FX_PUPIL_OT_storyboard_sheet.png`。
- Active loops：`NARRATIVE_STATE_EXTRACTION_20260712`与`NARRATIVE_STATE_POSTWAKE_20260712` attempt_001 均被导演拒绝；failure labels为`narrative_state_mismatch`、`premature_state_transition`、`layer_state_collision`。下一轮只允许小批生成修复候选，不允许继续原四批规模生图。
- 当前男主单线产出目录：`08_generation/jobs/MALE_ONLY_V3_20260712/outputs/`；时钟先导图在`08_generation/jobs/MALE_ONLY_V3_PILOT_20260712/outputs/`。输出含梦贩墙影、镜中无面空心、吸入沙漠、沙漠长镜头4帧与编号故事版、结尾反转2帧与编号故事版、梦贩欢迎特写、准确片名卡与透明字标。全部未自动 Final。
- 回传事故与修复：运行中的 Pipeline Hub 曾持有旧 123 卡快照，首次 `idea-image-output` 匹配 0 行并把磁盘 Board 写回旧态；已立即用 `07_shots/storyboards/build_extended_ending_v2.py` 恢复 7 幕/144 卡，再次回传成功。继续前必须以磁盘 144 卡为准，避免旧 Hub 快照再次覆盖。

## 当前 Board｜男主单线 V3（2026-07-12 最新权威）

- 总卡数：**122**
- 7 幕：ACT01 22 / ACT02 20 / ACT03 35 / ACT04 2 / ACT05 3 / ACT06 7 / ACT_FX 33。
- 版本总数：**147**；新男主单线 M01–M12 共15个版本，其中M09/M11含编号故事版附件，M12含透明字标附件。
- `item_id`、`card_uid`：0 重复。
- 视频提示词存在：122/122；全 Board 提示词合同：**122/122 PASS，0 errors**。
- 新卡时长按镜头内容动态分析：4–12秒；每条含 `[STYLE_FINGERPRINT]`、`[STYLE_INHERITANCE_HARD_LOCK]`、`[STYLE_NEGATIVE]`、`[DURATION_RATIONALE]` 和从0.0秒到终点的连续时间轴。
- Pipeline Hub 回读与磁盘回传门禁均 PASS：7幕、122卡、147版本、缺失路径0。

## 男主单线 V3 权威文件

- 导演剧本：`03_story/scripts/director_shooting_script_v3_male_only.md`
- 重建脚本：`07_shots/storyboards/build_male_only_v3.py`
- 生图/视频提示词包：`11_delivery/aigc_prompt_packages/MALE_ONLY_V3_BATCH_20260712/AIGC_PROMPTS_MALE_ONLY_V3_BATCH.md`
- 暂存 Board：`03_story/idea_board/idea_board_male_only_v3_staged.json`
- 回传前 Board 备份：`03_story/idea_board/idea_board_before_male_only_v3_20260712.json`
- 被拒绝的噪点/错字/Boss方案：`08_generation/jobs/MALE_ONLY_V3_20260712/rejected/`，禁止作为后续参考图。
- 片名现为《概率交易所》；项目 slug 仍为`buy-dreamer`。

## 最新故事与角色锁

- 男主遇见梦贩到完成交易并回到现实前：长发民谣艺人。
- 从现实醒来后：短发、完全无面、胸口贯穿空洞、机械无灵魂；此状态贯穿镜子、重返梦贩、沙漠、Boss与豪车结尾，禁止恢复普通脸。
- 醒来后的主线不再出现女主；女性只可作为无面空心环境人物或随从。
- Boss“万面债主”：平滑黏稠黑色纸液、6张异色英雄脸、3个人生片段、中央保险库空洞；禁止王座、皇冠、面具光环、密集小脸和全幅微纹。
- 结尾新青年是独立新角色：偏长发、正常脸、完整胸口、旧木吉他；说“我想和他换”。
- `DREAM_DESERT_TREK_BOSS_REVEAL`是M06–M09的12秒一镜到底；`ENDING_NEW_TRADER_REVEAL`是M10–M11的10秒一镜到底。不得拆成独立切镜。

## 历史 V2 说明

以下“女主进入遗忘之沙”的 V2 内容与旧 E/F 卡仅作为历史记录和磁盘备选，不属于当前 Board，不得覆盖上述 V3。

## 新版后半段权威文件

- 导演剧本：`03_story/scripts/director_shooting_script_v2_extended_ending.md`
- 卡片清单：`07_shots/storyboards/EXTENDED_ENDING_V2.json`
- 可重复构建脚本：`07_shots/storyboards/build_extended_ending_v2.py`

## 新结构

### ACT04｜更好的生活，逐渐空心

- E01：早餐桌上的遗忘缺口。
- E02：本人停下，影子多走两步并抱着不存在的吉他。
- E03：玻璃反射中的胸腔变成永动办公室。
- E04：每过一道闸门，五官少一个细节。
- E05：女主面对仍在摆正餐具的空心无面男主。

### ACT05｜卡片再次指向42号门

- E06：公文包夹层落下迷宫卡与梦沙。
- E07：没有引路人的旧电梯，镜中影子向上指。
- E08：女主再次打开42号门。
- E09：贴地仰拍买梦人背影；真人仅轻扭头，墙影成为由空外套、失针罗盘和封口组成的巨大恶魔。
- E10：买梦人揭示交易真相与失败交易者。
- E11：买梦人打开门后的梦境沙漠，递出失针罗盘。

### ACT06｜遗忘之沙

- F01：女主沿门框深井坠入沙漠。
- F02：门、无弦巨琴、倒立城市与通天楼梯的坟场。
- F03：被红线拴住、永远劳动的影子囚徒。
- F04：背负巨大梦罐和空鸟笼的无脸商队。
- F05：女主凭“弹奏不存在吉他”的手指节奏认出空心男主。
- F06：强行拉走导致男主手臂沙化，她立即停手。
- F07：女主不再拉，只把共同记忆化成一条不稳定道路。
- F08：男主自己选择迈向没有保证的门，脸与胸只部分恢复。
- F09：沙漠折叠，二人奔向无编号、无价格的门。
- F10：回到宽敞新家，男主写下第一道没有划掉的不完美线；裂缝和代价仍在。

## 买梦人对白锁

- “我没拿走他。我只收了他亲手递给我的理由。”
- “有人卖掉梦想，只换来继续活着；有人连这个也换不到。你们已经足够幸运。”
- “你能找到他，但不能替他回来。”

对白只作为剧本与后期配音，不在 AIGC 视频中生成对白音频或字幕。

## 跨项目硬规则（已安装并同步源码）

- 总门禁：`~/.codex/skills/aigc-production-hard-rules/`
- 视频风格/动态时长：`~/.codex/skills/aigc-video-style-lock/`
- 规则源码同步：`/Users/jaychoupp/Story/Film/skills/`
- 提示词合同校验：`~/.codex/skills/aigc-production-hard-rules/scripts/validate_prompt_contract.py`
- 硬规则是跨项目、动态取值、必须遵守：不固定某一画风或时长，但每次必须读取当前项目/图片并写出专业字段。
- 旧 123 卡属于规则升级前的历史提示词；任何旧卡再次用于生图或生视频前，必须先迁移并通过新合同，不得原样直接使用。

## 新卡生图硬锁

- 1915×821，21:9；二维硬边分层剪纸拼贴、三角折面纸纹。
- 现实冷蓝灰；记忆砖红；梦市/超现实裂隙暖琥珀与深青。
- 交易后男主：同一年轻脸、短整黑发、铁灰廉价西装/家居浅灰衬衫、棕公文包，无吉他琴包。
- 女主：21–23、下颌至锁骨黑发、左耳可读、灰米开衫、砖红内搭；不战士化、不奇幻换装。
- 买梦人：既定矮小人设；恶魔只存在于墙影，本体不怪物化。
- 空心/无面用干净剪纸负空间表达，禁止血肉、融化脸手。
- 沙漠不是普通写实沙漠，必须由门、钥匙、纸片、断琴弦、办公室残片和被放弃的选择构成。

## 下一任务必须执行

1. 读取本交接并使用 `$aigc-production-hard-rules`、`$aigc-video-style-lock`、`image-quality-guard`、`film-session-relay`；先修复当前Board的叙事状态合同缺口并复验。
2. 温馨女友段W01–W06曾完成首轮图与编号故事版，但已被导演最新反馈淘汰：`不要女主`，且黄铜片修补裂琴被判定为`prop_design_fake`。active loop：`WARM_ENCOURAGEMENT_REPLACED_20260712/attempt_001`=reject。旧文件保留历史证据，不得回传或打入当前交付。
3. 当前替代镜头为男主独处摩挲普通旧木吉他：`08_generation/jobs/WARM_AND_TWIST_V4_20260712/outputs/009_MALE_HAND_CARESSES_OLD_GUITAR_v001.png`。吉他结构完整、六弦、仅边角轻微磕碰和漆面磨损；无女主、无裂缝和修补片；画质QA PASS。
4. 结尾反转已扩展为R01–R04四帧连续长镜头并生成编号故事版：`08_generation/jobs/WARM_AND_TWIST_V4_20260712/outputs/013_TWIST_R01_R04_NUMBERED_STORYBOARD_v001.png`。当前交付包：`11_delivery/packages/PROBABILITY_EXCHANGE_MALE_GUITAR_AND_TWIST_20260712.zip`；完整提示词：`11_delivery/aigc_prompt_packages/MALE_GUITAR_AND_TWIST_20260712/AIGC_PROMPTS_MALE_GUITAR_AND_TWIST.md`，合同2/2 PASS。
5. 片名Logo单帧已被导演判定不足；active loop `TITLE_LOGO_REVEAL_20260712/attempt_001`为reject，failure label=`storyboard_sequence_missing`。下一次继续时必须完成01–04连续关键帧、编号故事版与单镜头视频提示词。
6. 生成前先应用低噪画质锁；每张生成后立即目检与脚本质检，不合格图进入`rejected/`且不得作为下一张参考。
7. 导演先在 Pipeline Hub 筛选 M01–M12 候选；不得自动 Final。
8. 如果继续生视频，必须直接使用各卡完整视频提示词，保留明确美术风格锁、动态时长、连续时间轴和项目声音规则。
9. 多关键帧镜头必须使用编号故事版和共享SHOT_ID，不得把M06–M09或R01–R04当成跳切组。
10. 回传任何新版本后再次运行提示词合同与`validate_pipeline_hub_return.py`，并报告卡数、版本数、提示词覆盖与缺失路径。

## 历史版本保留

- FX24–FX33、D29A–D29H 已有 v001 候选，目录：`08_generation/jobs/PSYCHOLOGICAL_BREAK_20260712/outputs`。
- 旧结尾 D29–D33 不删除，作为历史/备选结尾保留。
- 所有 current、备选、rejected 资源继续保留并参与完整打包。
