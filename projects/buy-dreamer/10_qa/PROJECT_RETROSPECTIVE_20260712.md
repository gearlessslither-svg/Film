# 《概率交易所》/ buy-dreamer 项目复盘

日期：2026-07-12
范围：剧情迭代、角色状态、画风锁、生图、分镜序列、提示词、回传、交付与技能体系。

## 项目结果快照

- 当前Board：7幕、122卡、147版本；122/122视频提示词覆盖，缺失路径0。
- 校验状态：通用提示词合同与Pipeline Hub回传合同通过；叙事状态合同未通过。当前Board缺少顶层`character_state_ledger`，122卡仍有大量`timeline_phase`、`character_state_ids`、`state_transition_rule`及对应提示词标签缺口，不能宣称全门禁通过。
- 本地生成目录统计：199张PNG输出，38个`rejected/`文件。
- 循环系统：51个asset、70次attempt；明确记录36个`hold`、3个`revise`、5个`reject`，其余历史attempt缺少规范化verdict字段。
- 当前有效后半段：男主醒来后短发、无面、空心；独自重返梦贩、进入沙漠、挑战万面债主；结尾新青年说“我想和他换”。
- 当前有效新增交付：男主独自摩挲普通旧木吉他；结尾反转R01–R04四帧与编号故事版。

## 做对了什么

### 1. 角色时间线最终被显式化

前期把“长发民谣艺人”和“醒来后的短发无面空心人”混用，导致抽梦、回忆、现实和镜面层互相污染。建立独立`character_state_ledger.json`、`[NARRATIVE_TIME]`、`[CHARACTER_STATE_LOCK]`和`[STATE_TRANSITION_RULE]`校验方法后，错误已经能被检测；但本次复核确认这些字段尚未完整迁移到当前Board，因此方法成立、项目数据仍未完成收口。

结论：叙事状态账本是跨项目有效方法，应保留在`aigc-production-hard-rules`，但具体发型、服装和变形机制必须项目动态定义。

### 2. 视频风格锁与动态时间轴有效

早期AIGC视频提示词只有动作描述，没有明确继承输入图的剪纸媒介，也没有覆盖完整时长。加入`[STYLE_FINGERPRINT]`、`[STYLE_INHERITANCE_HARD_LOCK]`、`[STYLE_NEGATIVE]`、动态`[DURATION_RATIONALE]`和无缝`[TIMELINE]`后，提示词合同可以自动验证。

结论：`aigc-video-style-lock`职责明确，不应删除或并入画质技能。

### 3. 逐帧画质门阻止了噪点继续传染

万面债主、街景、梦贩特写多次出现全画面三角微纹和假细节。将`image-quality-guard`改为生成前必用、生成后立即QA，并禁止未检查图片进入下一张参考链后，后续平滑哑光大形面明显稳定。

结论：`image-quality-guard`有效；它只负责表面清晰度，不应承担剧情、道具或导演意图判断。

### 4. 多关键帧镜头规则有效

沙漠Boss长镜头和结尾反转都从孤立图片改成共享`SHOT_ID`、有序关键帧、连续转场、编号故事版和完整时间轴，解决了视频工具把关键帧当跳切的问题。

结论：`Multi-Keyframe Single-Shot Gate`应保留，并扩展到片名/Logo出现镜头。

### 5. Pipeline Hub回传最终可验证

项目曾因Hub内存持有旧快照，把144卡磁盘Board覆盖成123卡。后续采用磁盘备份、读取Hub实时Board、结构重写后回读、再运行`validate_pipeline_hub_return.py`，最终得到可核验的7幕/122卡/147版本。

结论：`pipeline-hub-return-guard`有效，但必须新增“活动剧情分支”检查，防止旧剧情被合法HTTP响应重新带回。

## 主要返工原因

### 1. 导演修改被当作局部prompt patch

项目多次发生结构性覆盖：女主救援结尾→男主单线；温馨女友段生成完成→导演取消女主；裂琴修补象征→普通旧吉他。旧要求没有立即退出活动参考链，造成继续生成、打包和Board语义冲突。

根因：缺少“导演覆盖=剧情分支作废”的统一门禁。

新增规则：任何增删角色、替换结尾/变形/道具概念的反馈都必须停止依赖任务，标记`director_override`和`story_branch_superseded`等标签，更新权威剧本/Board/账本/提示词/交接后才恢复。

### 2. 象征性道具被过度设计

为了表达“放下也能捡起来”，旧吉他被设计成长裂缝、黄铜修补片和缺弦。图像清晰、构图成立，但导演认为道具虚假。之后改为结构完整、六弦、仅边角磕碰和漆面磨损的普通旧木吉他才符合故事。

根因：把隐喻直接堆到物体表面，没有先通过功能、结构和真实磨损检查。

新增规则：道具先定义功能、结构、材料、必需零件、年龄和批准损坏；默认使用普通磨损，任何裂缝、补丁、缺件、发光缝都必须有剧本事件授权。

### 3. 自动QA无法判断导演意图

Boss噪点版、裂琴、单张Logo、女友六镜都可能通过像素/尺寸QA，却仍因压迫感、道具可信度、序列缺失或剧情覆盖被拒绝。

根因：把`quality-pass`误读为`director-pass`。

新增规则：自动QA只证明技术表面；导演覆盖、叙事分支、构图意图、道具可信度、准确文字和序列完整性必须由语义门与人审决定。

### 4. 片名文字与片名镜头被混为一件事

图像模型第一次生成“概率交易所”时出现伪字。改用无字底板＋确定性中文字体合成后字形准确，但单张最终Logo仍被导演判定不足，因为“出现”需要过程与分镜。

根因：缺少两级门：准确字形门；片名出现序列门。

新增规则：图像模型负责底板/材质/光影，准确高风险文字优先确定性合成并逐字验证；凡要求Logo“出现”，必须设计时长、出现机制、有序关键帧、转场、终帧停留和编号故事版。

### 5. 提示词通过不断加元素修错，反而制造噪点

万面债主一度同时堆入大量脸、人生片段、面具、闸机、梦罐、时钟和沙漠碎片，语义更完整但画面更脏。缩减为6张英雄脸、3个人生片段和大面积平滑黑液后才成立。

结论：返修prompt应变短、减少歧义；一个主体、一个核心机制、1–2个英雄材料优先于“更多电影感/更多细节”。该规则已由`aigc-loop-system`覆盖，无需新增skill。

## Skill增删改结论

### 不新增整个skill

不创建`aigc-prop-guard`或`aigc-title-logo-skill`。这些触发会与强制父门`aigc-production-hard-rules`、`imagegen`、`aigc-loop-system`重叠，增加上下文与漏触发风险。道具可信度与准确文字/片名序列应成为生产父门的必检项。

### 不删除整个skill

- 保留`aigc-production-hard-rules`：负责跨项目生产合同。
- 保留`aigc-loop-system`：负责导演反馈、失败标签和小批迭代。
- 保留`image-quality-guard`：负责噪点、微纹、清晰度和保守修复。
- 保留`aigc-video-style-lock`：负责输入图视觉语言的逐帧继承。
- 保留`pipeline-hub-return-guard`：负责Board结构、版本、提示词和回读验证。
- 保留`film-session-relay`：本项目多次达到WARN/HIGH，证明窗口预算门必要。

### 修改内容

1. `aigc-production-hard-rules`
   - 新增Director Override And Active Branch Gate。
   - 新增Prop Plausibility And Damage Gate。
   - 新增Exact Text, Logo, And Title-Sequence Gate。
   - Completion Gate增加活动分支、道具结构和准确文字检查。
2. `aigc-loop-system`
   - 新增导演覆盖/分支作废流程。
   - 把`prop_design_fake`、`typography_invalid`、`sequence_missing`定义为语义失败，禁止用去噪代替重做。
3. `pipeline-hub-return-guard`
   - 新增Active Narrative Branch Guard，阻止旧Hub快照或旧剧情版本回灌。
4. `aigc-film-project-memory`
   - 入库导演覆盖、道具可信度、准确文字/片名序列三条经验，并按证据强度区分硬规则与活跃建议。

## 后续优先级

1. 先把叙事状态账本及三类状态字段迁移到当前122卡Board，运行`validate_narrative_state_contract.py`直至PASS；迁移前不得再报告“双门禁全部通过”。
2. 完成《概率交易所》片名出现R01–R04分镜；当前单张Logo已明确不足。
3. 在回传男主旧吉他与反转R01–R04前，先更新活动Board，确保女友温馨段和裂琴版本仍为历史而非当前。
4. 为loop旧attempt补齐缺失verdict字段；当前70次attempt中有26次统计为unknown，降低自动复盘质量。
5. 继续小批生成；会话达到500MB立即交接换窗。
