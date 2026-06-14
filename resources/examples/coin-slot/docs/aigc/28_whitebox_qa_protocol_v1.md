# 投币口 / 01_AIGC 白模 QA 协议 v1

## 核心判断

白模不是“有图就行”。白模一旦机位错、主体被遮挡、轴线反了、入口出口关系不对，后续 pure 图会稳定地生成错误画面，而且越高清越难返工。

所以白模进入真实图片生成前必须通过 QA gate。当前项目 188 张 MSB panel 全部视为 `whitebox_required=yes`。任何 panel 如果没有通过白模 QA，禁止生成 pure 图。

本项目的白模标准按“AI 渲染器”逻辑执行：白模必须尽最大可能忠实还原真实图片的构图、人物/环境比例、空间关系、前中后景和遮挡。白模失败时修白模，不改原分镜意图。

## 白模 QA 分层

| 层级 | 检查类型 | 可自动 | 必须人工 |
|---|---|---|---|
| L0 | 文件存在、尺寸、非空图、非全黑/全白 | yes | no |
| L1 | 画幅、曝光、主体大致可见、中心区域无遮挡 | partial | yes |
| L2 | 机位是否对应 panel、主体位置、前中后景、入口出口 | no | yes |
| L3 | 同场景连续性、轴线、相邻 panel 首尾关系 | no | yes |
| L4 | 是否足够指导 AIGC pure 图 | no | yes |
| L5 | 是否可以把白模交给 AIGC 当结构渲染参考 | no | yes |

自动脚本只能作为初筛。最终通过必须有人类导演视角确认。

## 白模通过标准

每张白模必须满足：

1. 文件存在，能打开。
2. 画幅为 16:9，推荐 1280x720 或更高。
3. 图像非空、非全黑、非全白、非严重过曝。
4. 主体或关键空间位置没有被墙、柱、机柜、前景块完全挡住。
5. 摄像机没有穿墙、穿物、落在地面或被模型内部包住。
6. 前景/中景/背景层次能读懂。
7. 人物站位或占位块和 panel 描述一致。
8. 主轴线没有反转，尤其是：
   - 小路段：三兄弟左/近侧，混混右/远侧，逃跑朝废楼方向。
   - 废楼段：入口在近处，电话亭固定远端。
   - 电话亭段：小川从左侧黑暗靠近，电话亭在右侧或中心。
   - 8-bit 段：横版固定，主角左，敌人右。
9. 相邻 panel 能接上，不发生突然 180 度翻转。
10. 如果是 start/end frame 候选，必须能明确作为视频生成首帧或尾帧。
11. 人物尺寸必须遵守比例锚点：小川低于阿磊，彬子矮但压迫，高杆明显最高，大海明显最宽。
12. 同一场景的柜机、门、电话亭、走廊宽度、路灯高度和墙体高度不能随 panel 漂移。
13. 如果白模不能承载分镜意图，判定为 `not_panel_specific`，不得用 prompt 强行补救。

## 失败类型

| issue_type | 说明 | 修正 |
|---|---|---|
| missing_file | 白模文件不存在 | 渲染对应白模 |
| unreadable | 文件损坏或无法打开 | 重新输出 |
| wrong_aspect | 不是 16:9 | 修相机/渲染设置 |
| blank_or_flat | 图像过空、全灰、全黑、全白 | 检查相机是否穿模或曝光 |
| camera_inside_geometry | 相机在墙/模型内部 | 移动相机，重新渲染 |
| blocked_subject | 主体/关键道具被遮挡 | 调整相机或前景遮挡 |
| wrong_axis | 左右阵营或逃跑方向反了 | 回到场景轴线，重设机位 |
| wrong_scale | 人物/空间比例不可信 | 调整占位块大小和相机焦距 |
| missing_anchor | 关键锚点缺失 | 加入入口、电话亭、石块、街机等锚点 |
| poor_layering | 前中后景读不清 | 调整构图和遮挡层级 |
| not_panel_specific | 机位太泛，不能指导该 panel | 新增更细白模 |
| duplicate_or_reused_without_reason | 多张分镜共用近似白模且没有微位移理由 | 重新做 panel-level blocking |

## QA 表字段

`exports/whitebox_qa_checklist.csv` 每行对应一个 MSB panel 和一个 required whitebox：

| 字段 | 含义 |
|---|---|
| whitebox_id | 白模 ID |
| panel_id | 对应 MSB |
| planned_whitebox_path | 计划路径 |
| auto_file_ok | 自动文件检查 |
| auto_image_ok | 自动图像检查 |
| aspect_ok | 画幅 |
| exposure_ok | 曝光/非空 |
| subject_visible | 主体/关键空间可见 |
| occlusion_ok | 没有错误遮挡 |
| camera_position_ok | 机位符合 panel |
| axis_ok | 轴线正确 |
| anchors_ok | 关键锚点存在 |
| adjacent_continuity_ok | 和相邻 panel 能接 |
| panel_specific_ok | 足够指导该 panel |
| qa_status | pending/pass/fail/revise |
| issue_type | 失败类型 |
| fix_action | 修正动作 |
| approved_by | 审核人 |

## QA 流程

1. 根据 `exports/whitebox_expansion_plan.csv` 生成或更新白模。
2. 运行 `tools/qa_whitebox_images.py` 做自动体检。
3. 自动失败的白模立即返工，不进入人工审。
4. 自动通过后生成白模 contact sheet。
5. 人工按本协议检查 L2-L4。
6. 人工再按 L5 判断是否足够像真实图的空间结构；只有 `qa_status=pass` 的白模可以作为 pure 图生成参考。
7. 若 pure 图仍跑偏，回查该白模 QA；如果白模不够具体，新增白模，不只改 prompt。

## 批次门禁

| Batch | 进入 pure 图生成前必须满足 |
|---|---|
| B01 | required 白模全部 pass，入口方向和三兄弟路径清楚 |
| B02 | required 白模全部 pass，街霸机两侧站位和彬子/四人组聚拢清楚 |
| B03 | required 白模全部 pass，门口到小路、堵路左右阵营不反 |
| B04 | required 白模全部 pass，围殴、石块、逃跑路径逐张可接 |
| B05 | required 白模全部 pass，走廊轴线和电话亭位置稳定 |
| B06 | required 白模全部 pass，听筒、电子化、8-bit 横版固定 |

## 严格停止条件

以下任一情况出现，停止真实图片生成：

- 同一场景白模 contact sheet 中入口/出口位置连续漂移。
- 小路阵营左右反复变化。
- 围殴段无法读懂阿磊、小川、小满和四个混混的位置。
- 石块段没有明确“石块在路边前景 -> 小川弯身 -> 遮挡冲击 -> 冻结”的路径。
- 走廊电话亭位置在不同白模中左右跳。
- 8-bit 白模不是横版固定机位。

## v1.1 近似重复白模检测补丁

本轮发现的根本问题不是单张白模坏图，而是白模生成策略错误：`render_whitebox_v2.py` 用同一个 `source_camera` 批量复制多个 MSB panel，只做很小的 deterministic offset。由于白模场景本身是静态的，panel 里的主体动作、前中后景变化、起止帧差异、遮挡设计没有被真正编码进白模，结果就是很多 panel 虽然文件存在、曝光正常、画幅正确，但实际画面几乎一样，不能指导 AIGC pure 图生成。

因此 QA 增加 L1.5：感知相似度 / 分镜差异检测。

自动脚本：`tools/qa_whitebox_images.py`

新增检测：

1. 对每张通过 L0/L1 的白模生成 64x36 灰度缩略图。
2. 计算 mean absolute difference 和 8x8 dHash。
3. 同场景内若 `mad <= 3.5` 或 `dhash <= 3`，视为近似重复候选。
4. 近似重复形成 3 张及以上簇时，整簇标记为 `qa_status=fail`、`issue_type=near_duplicate_whitebox`，除非每一格都有明确 intentional hold 或微位移理由。
5. 相邻 panel 若近似重复，即使未形成大簇，也标记为 `issue_type=adjacent_near_duplicate_whitebox`，除非之后人工明确写入“intentional hold”并补充动作/时长理由。
6. 微小位移可以共用构图逻辑，但仍要输出独立白模和独立 pure 图；如果白模图像完全一样，必须在 `whitebox_composition_reuse_plan.csv` 写明共享参考、故事变化和 prompt delta。

新增 QA 字段：

| 字段 | 含义 |
|---|---|
| similarity_ok | pass/fail/not_checked |
| similarity_cluster | DUP001 等重复簇编号，或 ADJACENT |
| similarity_reference | 该重复簇参考 panel |
| similarity_score | cluster_size 或 mad/dhash 分数 |

新增报告：

`exports/whitebox_similarity_report.csv`

旧检测结果：169 张 required 白模中，73 张保持自动通过，96 张因近似重复失败，形成 16 个重复簇。该结果暴露了流程根因，真实图片生成当时必须暂停。

## v1.2 panel-level 白模与前景相似度补丁

用户进一步明确：白模应尽最大可能忠实还原真实图片构图、比例和空间关系；极端情况下，有多少张分镜就应该有多少白模。项目因此升级为 188/188 panel-level whitebox。

本轮新增：

1. `whitebox_expansion_plan.csv` 全部 MSB panel 改为 `whitebox_required=yes`。
2. `render_whitebox_v2.py` 隐藏基础 blend 中的静态人物锚点，改为每张 panel 按故事临时生成角色体块、道具、动作路径和特写结构。
3. `qa_whitebox_images.py` 的重复检测不再只看灰度全图；新增 RGB 色差和 story foreground mask，避免环境墙面占比过高时误判“人物 blocking 已经变化”的白模为重复。

最新自动 QA 结果：

```text
auto_pass_needs_human_review=188 failed=0 missing=0 similarity_clusters=0 similarity_flagged=0
```

真实图片生成仍需先做人工导演视角 contact sheet 复核。
