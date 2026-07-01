# 项目交接包 / Handoff — blue-water-citypop-op

> 新窗口先读这份 + `03_story/idea_board/idea_board.json`，不要重新分析整个项目。

- 项目根: `/Users/jaychoupp/Story/Film/projects/blue-water-citypop-op`
- 工具: AIGC Film Pipeline（Pipeline Hub `http://127.0.0.1:8787`），skill `aigc-film-pipeline`
- 生成时间: 2026-07-01 07:45
- 备注: Completed Reference-003 R7 full high-precision repack: all 84.42s rebuilt into 36 source-FPS/PySceneDetect-informed AIGC video units; prompt-only files now explicitly list current ordered official + R5 generated anchors; 14 P1 candidate screenshots queued for new pure-image generation.

## 最新更新 / Latest Update — 2026-07-02 00:10 CST
- Director caught two additional packaging failures in the first per-segment handoff package:
  1. reference clips could not upload reliably because they were hardlinked source MP4s using `mp4v/mpeg4 Simple Profile` video and no audio;
  2. `02_keyframes_for_upload/` mixed official/original frames, R5 target-style generated frames, and R7 generated candidates, causing style confusion and bad ordering for external AIGC video sites.
- Old package is now explicitly superseded/do-not-use:
  - `11_delivery/packages/reference003_r7_aigc_video_segment_input_folders_20260701/`
- Correct current package to use:
  - `11_delivery/packages/reference003_r8_lean_aigc_video_segment_input_folders_20260701/`
  - Index: `11_delivery/packages/reference003_r8_lean_aigc_video_segment_input_folders_20260701/README.md`
  - Manifest: `11_delivery/packages/reference003_r8_lean_aigc_video_segment_input_folders_20260701/PACKAGE_MANIFEST.json`
- R8 lean package behavior:
  - `01_reference_clip/`: upload-compatible H.264/AAC MP4, yuv420p, faststart, metadata stripped, with silent AAC audio.
  - `02_keyframes_for_upload/`: target-style generated anchors only; no official/original frames and no R7 candidates.
  - `05_r7_generated_candidates_reference_only/`: all 98 R7 generated candidates are retained for audit/reference only.
  - `06_official_original_keyframes_reference_only/`: 63 official/original keyframes retained for composition/timing reference only.
- R8 lean counts and verification:
  - 36/36 unit folders, 36/36 reference clips, 36/36 prompt docs.
  - Upload keyframes: 25 target-style generated anchors.
  - Asset locks: 66.
  - Source reference frames, audit only: 98.
  - R7 reference-only generated candidates: 98.
  - Official/original reference-only keyframes: 63.
  - Missing files: 0.
  - Clip decode failures: 0/36.
  - Non-H.264/AAC reference clips: 0/36.
  - Non-target-style rows in `02_keyframes_for_upload`: 0.
  - Upload keyframe ordering violations: 0.
- Important next step: before external AIGC generation, units with `Upload keyframes = 0` should either use only reference clip + locks + prompt, or receive newly approved target-style keyframes. Do not re-add official/original or R7 candidate images to default upload unless approved per unit.

## 最新更新 / Latest Update — 2026-07-01 23:35 CST
- Director reviewed the newly assembled R7 candidate preview and flagged it as a workflow-level QA failure:
  1. some frames are placed/weighted incorrectly in the timeline, e.g. Nadia entrance is disrupted by earlier sky/cloud material;
  2. faces flicker/mutate, likely worsened by excessive inserted candidate frames;
  3. mid/late sections drift into a different realism/style family.
- Immediate hold: do not treat the previous `production_ready` package as visually approved for external AIGC video generation.
- QA failure report added: `10_qa/reports/reference003_r7_generated_candidate_preview_qa_failure_20260701.md`
- Evidence contact sheets added:
  - `10_qa/reports/r7_preview_audit_nadia_23_29.jpg`
  - `10_qa/reports/r7_preview_audit_late_129_161.jpg`
- Per director priority, a clean per-segment folder package was created before further repairs:
  - Folder root: `11_delivery/packages/reference003_r7_aigc_video_segment_input_folders_20260701/`
  - Index: `11_delivery/packages/reference003_r7_aigc_video_segment_input_folders_20260701/README.md`
  - Manifest: `11_delivery/packages/reference003_r7_aigc_video_segment_input_folders_20260701/PACKAGE_MANIFEST.json`
  - Counts: 36/36 unit folders, 36/36 reference clips, 36/36 `AIGC_PROMPT.md` docs, 186 keyframe/image inputs, 66 asset lock images, 98 source reference frames for audit, missing 0.
  - Each unit folder contains:
    - `01_reference_clip/`
    - `02_keyframes_for_upload/`
    - `03_asset_locks_for_upload/`
    - `04_source_reference_frames_audit_only/`
    - `AIGC_PROMPT.md`
    - `manifest.json`
    - `README.md`
- New packaging script: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/build_reference003_r7_segment_input_folders.py`
- Next work should continue from QA recovery, not external video generation: select/approve a lean set of anchors per unit, quarantine bad style/identity frames, rebuild a reduced R8 preview, then regenerate final production prompts.

## Previous Update — 2026-07-01 17:50 CST
- R7 promoted candidate pure image generation is complete: P1 14/14, P2 20/20, P3 64/64, total 98/98.
- Candidate queue JSON now records status `all_generated_assets_ready`.
- R7 P1/P2/P3 generated assets live under `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/`.
- Final R7 generated-candidate preview MP4 is complete and decodes:
  - MP4: `09_edit/rough_cut/reference003_r7_generated_candidate_animatic_1080p_with_music_20260701.mp4`
  - manifest: `09_edit/rough_cut/r7_generated_candidate_preview/reference003_r7_generated_candidate_preview_manifest.json`
  - report: `09_edit/rough_cut/r7_generated_candidate_preview/reference003_r7_generated_candidate_preview_manifest.md`
  - status: `decode_ok`, 161 frames = 42 official + 21 R5 + 98 R7 generated, R7 missing 0.
- Final AIGC video production package index is ready:
  - MD: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_PROMPT_INDEX/AIGC_VIDEO_PRODUCTION_PACKAGE_INDEX.md`
  - JSON: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_PROMPT_INDEX/AIGC_VIDEO_PRODUCTION_PACKAGE_INDEX.json`
  - Production prompt docs: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_PROMPT_INDEX/PRODUCTION_READY_PROMPT_ONLY/`
  - Counts: 36/36 reference clips, 36/36 production prompt docs, 88 ordered anchor images, 98 R7 generated candidate images, 66 active lock images referenced, missing 0.
- Each R7 unit folder now has `AIGC_VIDEO_PRODUCTION_READY.md` pointing to that unit's reference clip, production prompt document, image inputs, and expected returned MP4 path.
- Helper scripts added:
  - `09_edit/rough_cut/build_reference003_r7_generated_candidate_preview.py`
  - `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/update_r7_promoted_candidate_manifests.py`
  - `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/copy_generated_image_to_candidate.py`
  - `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/build_reference003_r7_aigc_video_production_index.py`
- Git upload readiness:
  - Repo root is `/Users/jaychoupp/Story/Film`, remote `origin` is configured.
  - Git LFS is installed and `.gitattributes` tracks media (`*.png`, `*.jpg`, `*.zip`, `*.mp4`, etc.).
  - Project-level `.gitignore` excludes `00_admin/.venv_vision/`, `__pycache__/`, `*.pyc`, local caches, and logs.
  - Stage only `projects/blue-water-citypop-op/` and avoid unrelated dirty repo changes.
- Project validation passed: `python3 /Users/jaychoupp/Story/Film/scripts/validate_aigc_project.py /Users/jaychoupp/Story/Film/projects/blue-water-citypop-op` -> `project_status=pass`.

## Previous Update — 2026-07-01 08:45 CST
- R7 P1 promoted candidate generation is complete: 14/14 pure generated image assets exist under `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/`.
- P1 manifest: `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/reference003_r7_p1_generated_assets_manifest.md`
- P1 contact sheet: `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/reference003_r7_p1_generated_assets_contact_sheet.jpg`
- P1 anchor addendum: `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/reference003_r7_p1_generated_anchor_addendum.md`
- Affected R7 prompt-only files were updated with `Newly Generated P1 Anchors`; the top-level R7 prompt index links the P1 addendum.
- Director caught identity drift in the Grandis trio batch. Corrected and overwrote:
  - `R7_CAND_011_start_035983ms`
  - `R7_CAND_011_middle_036579ms`
  - `R7_CAND_019_end_048644ms`
- Grandis trio correction rule: always open/view the official trio lock before generating or repairing these shots. Grandis has no glasses/eyewear. Sanson keeps white fedora + sunglasses + pink bow tie. Hanson keeps white cap/goggles + round glasses + yellow scarf/bow. Do not use the older drifted outputs.
- Updated skill rules in `Film/skills/aigc-film-pipeline/references/identity-lock-and-asset-continuity-rules.md`: every locked character/prop/animal/vehicle/scene generation must actually view/use the current official lock before generation, especially after resume or correction.

## 当前 board 状态 / Current board
- 总卡数 / rows: **42**
- 按前缀 / by prefix: {'OP_SH': 42}
- 按状态 / by status: {'generated_reference003_qa_pass': 42}

## 创意主线 / Creative spine
Reference-003 是对《蓝宝石之谜》OP 的 AIGC 真人化/电影化复刻工作流测试：参考视频提供时间、机位、运动和剪辑功能，项目设定章节控制人物、道具、场景和 no-text/no-logo 安全边界。当前目标是先把关键帧/补帧预览做准，再进入外部 AIGC 高质量视频段落生成。

## 已锁定设定 / Locked bible rules（务必延续）
- Nadia 使用 `OP_SHOT_011_v2` 作为当前 official face lock：14 岁、蜜色肤色、短 navy-black bob、金色耳环/手镯、红橙白保守冒险服、Blue Water pendant；禁止成人化、性感化、换脸、长发化。
- Jean 是 14 岁法国少年发明家：蓝帽/蓝外套、圆眼镜、白衬衫、红领结；禁止成人化。
- Marie/King、Grandis trio、Nautilus、Blue Water pendant、blue grid geometry 等均使用 `05_asset_bible/setting_chapters/reference003_asset_locks_v1.json` 中的 official locks。
- 所有纯图和预览禁止生成原片标题、NHK、字幕、职员表、歌词、水印、可读文字或随机字形。
- 截图候选不是资产；只有重新生成的 pure image 并记录 `output_path` 后，才能进入 expanded preview。

## 已完成 / Done
- Reference-003 官方 42 张 keyframe 仍保持 `generated_reference003_qa_pass`，未在本轮改写。
- R5 adaptive frame promotion 已全部生成：21/21 张 R5 候选已从截图候选晋升为 pure generated assets。
- R5 job manifest: `08_generation/jobs/REFERENCE003_ADAPTIVE_FRAME_PROMOTION_R5_20260630/manifest.json`
- R5 analysis manifest: `03_story/expanded_keyframes/reference003_adaptive_frame_promotion_r5_20260630.json`
- R5 21-up 联系表: `08_generation/jobs/REFERENCE003_ADAPTIVE_FRAME_PROMOTION_R5_20260630/outputs/reference003_r5_generated_21up_sheet.jpg`
- R5 输出目录: `08_generation/jobs/REFERENCE003_ADAPTIVE_FRAME_PROMOTION_R5_20260630/outputs/`
- 新增预览脚本: `09_edit/rough_cut/build_reference003_r5_expanded_preview.py`
- 已生成扩展预览 MP4: `09_edit/rough_cut/reference003_r5_expanded_63frame_animatic_1080p_with_music_20260630.mp4`
- 扩展预览 manifest: `09_edit/rough_cut/r5_expanded_preview/reference003_r5_expanded_preview_manifest.json`
- 扩展预览 report: `09_edit/rough_cut/r5_expanded_preview/reference003_r5_expanded_preview_manifest.md`
- 扩展预览参数：63 帧 = 42 official keyframes + 21 R5 adaptive generated assets；84.44 秒；1920x1080；24fps；带原参考音轨；decode_ok。
- 已拆 21 个外部 AIGC 视频镜头包：`08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/`
- 每个镜头包包含：reference clip、ordered keyframe anchors、ordered keyframe contact sheet、legacy redundant per-unit `asset_locks/`、`AIGC_VIDEO_GENERATION_BRIEF.md`、`SEGMENT_QA_CHECKLIST.md`、`manifest.json`。
- 人类优先入口已补齐：`08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/README_USE_THIS_FIRST.md`
- 提示词索引：`08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_PROMPT_INDEX/AIGC_VIDEO_PROMPT_INDEX.md`
- 每镜精简提示词：`08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_PROMPT_INDEX/PROMPT_ONLY/<ORDER>_<UNIT>.md`
- 全局锁图一份：`08_generation/jobs/REFERENCE003_R5_VIDEO_SEGMENTS_20260701/_global_asset_locks/`
- 每镜实际需要的锁图写在 `<UNIT>/active_asset_locks.json` 和 prompt-only 文件里；黑场、尾帧、纯天空 hold 等无角色/道具镜头应为 `none`。per-unit `asset_locks/` 是旧版离线自足冗余结构，不作为导演判断入口。
- 镜头包总计：21/21 ready；63 个 keyframe anchors，其中 42 official + 21 R5 adaptive generated assets。
- 镜头包报告：
  - JSON: `10_qa/reports/reference003_r5_video_segment_all_units01_21_generation_ready_20260701.json`
  - MD: `10_qa/reports/reference003_r5_video_segment_all_units01_21_generation_ready_20260701.md`
- 完整交付压缩包：`11_delivery/packages/reference003_r5_video_segment_packages_20260701.zip`（约 780MB）。
- 轻量提示词索引压缩包：`11_delivery/packages/reference003_r5_video_prompt_index_20260701.zip`（约 28MB）。
- R6 帧级边界复核已完成：`01_intake/analysis/reference003_frame_boundary_refine_r6_20260701/reference003_frame_boundary_refine_r6_20260701.md`
  - OpenCV 源帧率扫描：2024 frames / 23.976fps。
  - 全片候选硬边界：30 个；单帧 flash candidate：1 个，位于 `00:14.72` 飞行器一闪。
  - PySceneDetect 交叉验证：28 scenes，开场关键边界含 `00:14.723`、`00:16.266`、`00:23.440`、`00:25.901`。
- R6 开场长镜头替换包已生成：`08_generation/jobs/REFERENCE003_R6_OPENING_LONG_UNITS_20260701/`
  - L01 `00:00.00-00:07.00` 黑场/云层/白鸟长段，6 anchors。
  - L02 `00:07.00-00:16.50` 白鸟/云层/飞行器短显长段，7 anchors。
  - L03 `00:16.50-00:24.80` 标题安全位/日光/Nadia 首显长段，5 anchors。
  - R6 prompt index: `08_generation/jobs/REFERENCE003_R6_OPENING_LONG_UNITS_20260701/_PROMPT_INDEX/AIGC_VIDEO_PROMPT_INDEX.md`
  - R6 report: `10_qa/reports/reference003_r6_opening_long_units_generation_ready_20260701.md`
  - R6 zip: `11_delivery/packages/reference003_r6_opening_long_units_20260701.zip`（约 67MB，SHA256 `f2f0faea6da267dcec05a7aef7a4d9162343e5746c11dd05ed3865c36733c3be`）。
- 项目内视觉工具 venv 已安装：`00_admin/.venv_vision/`，包含 `opencv-python-headless`、`scenedetect`、`imagehash`、`numpy`。不要全局 pip 安装。
- R7 全片高精度镜头包已生成，当前主包：`08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/`
  - 36/36 video units ready；所有 reference clips decode_ok。
  - Prompt index: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_PROMPT_INDEX/AIGC_VIDEO_PROMPT_INDEX.md`
  - Report: `10_qa/reports/reference003_r7_high_precision_video_units_20260701.md`
  - 交付 zip: `11_delivery/packages/reference003_r7_high_precision_video_units_20260701.zip`（约 274MB，SHA256 `38ddae4686d373f321578d344115d6af6e067b3a8d7c8c9c23ea9c7d739bc86e`）。
  - R7 prompts 已修正：每个 `PROMPT_ONLY` 以当前 ordered generated anchors 为主，明确列出 official + R5 generated images；旧 `Existing Unit Prompt` 不再作为主提示词来源。
  - R7 当前 prompt 引用 generated anchors 88 次，其中 R5 generated anchors 25 次（按 unit 重复引用计数，不是新增资产数）。
- R7 智能截图/新图候选队列已生成：`08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/reference003_r7_candidate_image_generation_queue.md`
  - 候选截图 98 张：P1 14、P2 20、P3 64。
  - P1 contact sheet: `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/reference003_r7_p1_candidate_contact_sheet.jpg`
  - 轻量候选队列 zip: `11_delivery/packages/reference003_r7_candidate_image_generation_queue_20260701.zip`（约 300KB，SHA256 `7aebb4bd45056260945e770059937f10aacfec11f5ae29b0f898617667cb4f59`）。
  - 截图候选仍不是资产；P1 需要生成 pure images 并写入 output_path 后，才能进入新预览或最终视频锚点。
- R7 P1 pure generated assets complete: 14/14.
- R7 P2 pure generated assets complete: 20/20.
- R7 P3 pure generated assets complete: 64/64.
- R7 production-ready AIGC material package complete:
  - Full preview MP4: `09_edit/rough_cut/reference003_r7_generated_candidate_animatic_1080p_with_music_20260701.mp4`
  - Production package index: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_PROMPT_INDEX/AIGC_VIDEO_PRODUCTION_PACKAGE_INDEX.md`
  - Per-unit production prompts: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_PROMPT_INDEX/PRODUCTION_READY_PROMPT_ONLY/`
  - Per-unit reference clips: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/<UNIT>/reference_clip/`
  - R7 generated pure images: `08_generation/jobs/REFERENCE003_R7_PROMOTED_CANDIDATES_20260701/outputs/`
- 项目校验通过：`python3 Film/scripts/validate_aigc_project.py Film/projects/blue-water-citypop-op` -> `project_status=pass`。

## 下一批 / NEXT
- Image generation and preview assembly are complete. Do not regenerate P1/P2/P3 unless the director requests a targeted repair.
- Current final production handoff for external AIGC segment generation:
  1. Open `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_PROMPT_INDEX/AIGC_VIDEO_PRODUCTION_PACKAGE_INDEX.md`.
  2. For each of the 36 units, upload that unit's reference clip, every image listed in its production prompt, and the production prompt document from `_PROMPT_INDEX/PRODUCTION_READY_PROMPT_ONLY/`.
  3. Save each external AIGC returned segment MP4 to `08_generation/outputs/video/reference003_r7_high_precision_segments/<UNIT>.mp4`.
- The older `_PROMPT_INDEX/PROMPT_ONLY/` docs remain as history. Use `_PROMPT_INDEX/PRODUCTION_READY_PROMPT_ONLY/` for actual external AIGC video production because those docs include the 98 new pure generated R7 candidate images.
- 当前优先使用 R7 全片高精度主包：`08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_PROMPT_INDEX/AIGC_VIDEO_PRODUCTION_PACKAGE_INDEX.md`。
- R5/R6 包保留为历史/对照；除非导演指定回退，不再作为主投喂包。
- `AIGC_VIDEO_GENERATION_BRIEF.md` 保留为完整机器/QA包；不要把 legacy per-unit `asset_locks/` 当作本镜全部需要上传的资产。
- 外部生成回来的 R7 MP4 保存到 `08_generation/outputs/video/reference003_r7_high_precision_segments/<UNIT>.mp4`。
- R7 P1/P2/P3 图像批次均已完成；下一步不是继续生图，而是按 production-ready prompt docs 逐镜生成外部 AIGC 视频段。
- 若某段人物漂移或运动不准，只修对应 unit 的图/提示词/视频段，不重做全片。
- 若继续发现一闪而过的人物/道具/转场没抓住，先用 R6 frame-boundary 方法复核对应时段，再决定是否重包或新增关键帧；不要只靠 2fps 联系表。
- 若导演指出人物漂移或某段仍稀薄，优先只修对应 R5/official 图，不重新抽全片、不重做 42 张官方 keyframe。
- 当前 Codex 会话已接近 500MB 窗口上限；继续大批量图像/视频生成建议新窗口接 `HANDOFF_LATEST.md`。

## 怎么继续 / Resume
1. 启动 Pipeline Hub：`/Users/jaychoupp/Story/Film_Tool_Launcher.command`
2. 校验：`python3 Film/scripts/validate_pipeline_state.py /Users/jaychoupp/Story/Film/projects/blue-water-citypop-op`
3. 加卡 → 生成 → 回填 `card-image-output`（只回路径，禁回 base64）→ 核验
4. 每完成一批回来更新本交接 + HANDOFF_LATEST.md
