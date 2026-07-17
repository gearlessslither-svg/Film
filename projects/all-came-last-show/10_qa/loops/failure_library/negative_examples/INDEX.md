# 《所有人都来了》负例证据索引

本索引只链接项目内已保存的失败 attempt、审计记录与输出路径，不复制大图。打开每条 attempt 的 `output_path.txt` 可定位原始失败图；`director_review.md` 与 `verdict.json` 是判定依据。负例只用于回归检查，禁止进入活动参考链、`selected/`、交付 ZIP 或后续图生视频输入。

| 回归风险 | 失败证据 | 失败原因 | 当前通过方向 |
|---|---|---|---|
| 15 张锚点冒充 120 秒完整分镜；尺度、动作、转换同时失守 | [`FINAL_FRAMES_120S_COVERAGE_V1 / attempt_001`](../../attempts/FINAL_FRAMES_120S_COVERAGE_V1/attempt_001/director_review.md) | `runtime_undercoverage`、`missing_intermediate_beat`、动物／建筑比例崩塌、群像动作雷同、转换相位被压平 | 活动版使用 120 秒／38 镜／42 帧账本与三段多锚点镜头。 |
| 建筑小于动物、门洞不可用、透视失去深度证据 | [`FIN-006 / attempt_002`](../../attempts/FIN-006/attempt_002/director_review.md)、[`FIN-012A / attempt_001`](../../attempts/FIN-012A/attempt_001/director_review.md) | 同平面门窗小于动物；镇缘房屋与动物接近或更小；重复狐狸 | 所有城市、门洞和家具镜头绑定 `SCALE_LEDGER_V1.md`，以 SH18、SH32、SH37 等通过帧做回归。 |
| 阿白身份泄漏成全猫群像 | [`KS21_02 / attempt_001`](../../attempts/KS21_02_SQUARE_LAST_PERFORMANCE/attempt_001/director_review.md) | 广场居民几乎全部变成猫，丢失多物种世界 | 每个活动主物种最多一个实例；阿白身份参考不得改写其他角色。 |
| 结尾仍冒烟或漂移成末日废墟 | [`KS21_03 / attempt_001`](../../attempts/KS21_03_WILD_DEPARTURE_DAWN/attempt_001/director_review.md)、[`KS21_03 / attempt_002`](../../attempts/KS21_03_WILD_DEPARTURE_DAWN/attempt_002/director_review.md) | 工厂停摆后烟囱仍冒烟；返修又把普通破败城镇画成大面积坍塌废墟 | 保持无烟、停摆、旧而完整；苍凉不等于灾难毁灭。 |
| DFT 风格漂移、重复背景角色与高频脏细节 | [`SH04 / attempt_001`](../../attempts/SH04/attempt_001/director_review.md) | 背景复制羊群，毛发和旧铁过度写实、过暗、噪声过密 | 使用大形、朴拙细描边、受控旧纸纹理与低噪 DFT 哑光蛋彩。 |
| 阿白状态或照片身份锚被局部编辑破坏 | [`SH15 / attempt_001`](../../attempts/SH15/attempt_001/director_review.md)、[`attempt_002`](../../attempts/SH15/attempt_002/director_review.md)、[`attempt_003`](../../attempts/SH15/attempt_003/director_review.md) | 私服阶段误戴工帽；去帽时又抹掉阿白不规则天然灰黑头顶斑 | 只允许受控单锚修复；活动通过版为 [`attempt_004`](../../attempts/SH15/attempt_004/director_review.md)。 |
| 群像角色实例重复，局部删除又误删应保留角色 | [`SH20 / attempt_001`](../../attempts/SH20/attempt_001/director_review.md)、[`attempt_002`](../../attempts/SH20/attempt_002/director_review.md) | 两只绵羊违反唯一实例；去重时又把唯一绵羊删除 | 生成前列出物种清单，编辑后重新逐个计数；活动通过版为 [`attempt_003`](../../attempts/SH20/attempt_003/director_review.md)。 |
| 演出后连续性泄漏烟雾 | [`SH29 / attempt_001`](../../attempts/SH29/attempt_001/director_review.md) | 表面 QA 通过但门外烟囱出现烟柱，违背停产状态 | 语义连续性优先于表面通过；活动通过版为 [`attempt_002`](../../attempts/SH29/attempt_002/director_review.md)。 |
| 空钩揭示里全员同姿凝视、衣箱重复 | [`SH33 / attempt_001`](../../attempts/SH33/attempt_001/director_review.md)、[V1 锚点终轮推翻记录](../../../FINAL_ANCHOR_SET_V1_DIRECTOR_REVIEW_20260717.md) | 八个角色多为相同站姿与同一眼线；出现多个衣箱且大象持箱 | 八个物种分配八种微反应，唯一衣箱归熊；活动通过版为 [`attempt_002`](../../attempts/SH33/attempt_002/director_review.md)。 |
| 转换起点相位过于一致 | [`SH35_KF01 / attempt_001`](../../attempts/SH35_KF01/attempt_001/director_review.md) | 无衣两足状态虽安全，但准备动作和重心前移相位过于雷同 | 用八种可读准备相位建立 KF01，再进入 KF02 错峰过渡和 KF03 自然四足；活动通过版为 [`attempt_002`](../../attempts/SH35_KF01/attempt_002/director_review.md)。 |

## 使用规则

1. 新提示词或视频输出若命中上表任一模式，使用对应 failure label 立即拒绝，不因画面漂亮或自动表面 QA 通过而放行。
2. 只打开当前要核对的负例；不要把多张失败图同时作为生成参考，也不要把失败图加入风格 hardlock。
3. 负例与活动通过版成对比较时，只继承通过版的明确修复原则，不继承失败图中的角色、构图、烟雾、破坏或重复物件。
