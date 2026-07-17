# 《所有人都来了》15 张锚点图导演退回审计

状态：`rejected_as_complete_120s_storyboard`

审计对象：`08_generation/jobs/final_frames_v1/selected/`

联系表：`08_generation/jobs/final_frames_v1/FINAL_FRAMES_CONTACT_SHEET_V1.png`

## 结论

现有 15 张只能作为视觉锚点，不能称为 120 秒版本的完整分镜。V1 让单张图片承担 8–15 秒，且多张同时承载数个连续动作；原 `qa_selected.json` 的 15/15 pass 只证明尺寸和表面图像指标通过，不证明叙事覆盖、世界尺度、群像表演或角色实例数量正确。

逐图复核结果：`KEEP 4 / REVISE 3 / REPLACE 8`。即使标为 `KEEP`，也只按 2–5 秒的明确镜头用途复用，不允许继续承担整个段落。

| 图 | 判定 | 复核意见 |
|---|---|---|
| `FIN-001` | `KEEP` | 城镇、厂房、道路尺度连贯，可作 3–5 秒开场地理远景。 |
| `FIN-002` | `REVISE` | 小型角色与建筑尚可，但大型物种的门洞通行尺度未被证明；队列同步属于工厂秩序段允许的有意同步。 |
| `FIN-003` | `KEEP` | 阿白、机器、轨道与厂房透视成立，可作 3–4 秒工业空间锚点。 |
| `FIN-004` | `REPLACE` | 几乎所有角色都处于双手拿工装的相同阶段，动作克隆严重；应拆成空间主镜头与不同脱衣细节。 |
| `FIN-005` | `REPLACE` | 多数角色同时在胸前系扣或整理领口，只有阿白动作不同；需整体重排群像表演。 |
| `FIN-006` | `REPLACE` | 同景深门窗明显小于动物，纵深缩放不稳定；人物运动方向也更像散开而非赴约汇聚。 |
| `FIN-007` | `REVISE` | 广场构图可保留，但大厅入口未证明可供大象通行，多人重复端杯／对谈；应扩大建筑尺度并重排动作。 |
| `FIN-008` | `REPLACE` | 多组舞伴重复“双手相握摇摆”，节拍与动作相位雷同，属于明显表演克隆。 |
| `FIN-009` | `REVISE` | 城镇尺度基本成立，集体凝视属于有意同步；但有两个显眼大象，且单一状态不能覆盖烟囱直立、倾斜、余波。 |
| `FIN-010` | `KEEP` | 空钩揭示明确，家具与建筑尺度成立；全体短暂停住在此有叙事理由，只可作 2–3 秒主镜头，另补个人反应。 |
| `FIN-011A` | `REPLACE` | 所有人再次用几乎相同姿势拿衣服，正是导演指出的“脱衣同一个动作”。 |
| `FIN-011B` | `REPLACE` | 所有角色处于近似爬行姿态，转换节奏被压平，部分已接近完整四足，状态边界不清。 |
| `FIN-011C` | `REPLACE` | 像物种陈列照：多数动物同向静立，有重复狐狸，部分动物站在长凳上，出口对大象的通行尺度也存疑。 |
| `FIN-012A` | `REPLACE` | 最严重尺度失败：镇缘动物与整栋房屋接近或超过同等视觉尺寸，纵深关系不成立；另有重复狐狸。 |
| `FIN-012B` | `KEEP` | 阿白与远处城镇尺度成立，可作 2–3 秒回望锚点；仍需新增真正转身跑入晨光的结束锚点。 |

## V2 终轮语义审计覆盖

`FIN-010` 的历史 `KEEP` 结论已在 42 帧整套联审中推翻：旧图虽能说明“空钩”，但多数角色仍以近似姿势凝视，并出现多个衣箱以及大象持箱，违反群像动作差异化与道具连续性。

当前活动文件 `08_generation/jobs/final_frames_v2/selected/SH33.png` 来自 `SH33 attempt_002`：八种动物分别执行触碰空钩、钻凳查看、查柜、坐下、摸空工牌槽、借镜面确认、捏住披肩、双爪放下唯一衣箱等八个微反应；内部语义审计通过，仍待导演最终审美复核。

## 失败标签

- `runtime_undercoverage`
- `missing_intermediate_beat`
- `hero_frame_overload`
- `character_environment_scale_mismatch`
- `architectural_scale_collapse`
- `perspective_scale_inconsistency`
- `group_action_repetition`
- `performance_clone`
- `transformation_phase_flattening`
- `duplicate_character_instance`

## 纠正原则

1. V1 清单降级为历史视觉锚点清单；活动生产权转移到 `07_shots/SHOT_COVERAGE_120S_V2.md`。
2. 先审批完整 120 秒时间覆盖，再写单镜头生产提示和生图。
3. 每个含建筑的群像镜头绑定 `05_asset_bible/SCALE_LEDGER_V1.md`，没有显式特殊尺度设计时不得豁免。
4. 每个群像镜头绑定 `07_shots/GROUP_ACTION_LEDGER_120S_V2.md`；工厂队列、烟囱倒塌时的共同停顿、发现空钩后的短暂停顿可作为有叙事目的的同步，其余动作必须错峰。
5. 旧图保留为证据和参考，不覆盖、不删除；`KEEP` 也可被终轮整套联审推翻，`REVISE` 与 `REPLACE` 均须生成新版本后重新接受语义、尺度、动作、连续性和表面 QA。
