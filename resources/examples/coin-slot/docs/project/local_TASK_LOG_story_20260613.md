# TASK_LOG

## Current Total Goal

Upgrade the `投币口` AIGC-first cinematic package from a broad 20-shot concept board into a production-grade design and micro-storyboard package. Current priority is fixing character sameness with detailed biographies, silhouettes, face/body/expression/gesture design, then expanding the film into a 5-6 minute fine storyboard plan with 188 planned storyboard panels and several hundred planned image assets before future video generation.

## Completion Status

animatic_audio_guide_and_s0_character_fix_done_real_image_batch_in_progress

## Completed Work

- Created custom skill `cinematic-storyboard-director` for story, visual bible, storyboard, keyframe prompt, and AIGC-first workflow.
- Installed/extracted Blender at `C:\Users\user1\Apps\Blender-5.1.2\Blender Foundation\Blender 5.1\blender.exe`.
- Created project structure at `E:\视觉\投币口`.
- Built AIGC-first folder `01_AIGC` and normal shooting folder `02_Normal_Shooting`.
- Updated story to the current version:
  - three brothers only, no girls
  - hidden game room in an old residential compound
  - older brother beats the short bully boss at Street Fighter
  - bully group blocks the brothers on a secluded alley while they go home
  - protagonist uses a roadside stone in panic, then escapes into an abandoned building
  - phone booth electronicization leads to 8-bit arcade world and `WIN / INSERT COIN`
- Created and updated:
  - `01_AIGC/00_project_rules.md`
  - `01_AIGC/01_visual_continuity_bible.md`
  - `01_AIGC/02_scene_reference_prompts.md`
  - `01_AIGC/03_aigc_storyboard.md`
  - `01_AIGC/04_video_prompts.md`
  - `01_AIGC/05_negative_constraints.md`
  - `01_AIGC/06_keyframe_prompts.md`
  - `01_AIGC/07_generation_run_plan.md`
  - `01_AIGC/08_shot_asset_map.md`
  - `01_AIGC/09_image_asset_manifest.md`
  - `01_AIGC/10_morning_review_index.md`
- Created Blender whitebox script and renders:
  - `01_AIGC/blender/coin_slot_whitebox.py`
  - `01_AIGC/blender/coin_slot_whitebox.blend`
  - `01_AIGC/blender/camera_manifest.csv`
  - `01_AIGC/whitebox_renders/*.png`
- Generated visual assets:
  - 2 character reference images in `01_AIGC/character_refs`
  - 6 scene reference images in `01_AIGC/scene_refs`
  - 12 keyframes in `01_AIGC/keyframes`
  - 20 storyboard visual panels in `01_AIGC/storyboard_panels`
  - 7 contact sheets in `01_AIGC/contact_sheets`
- Created export tables:
  - `01_AIGC/exports/asset_output_paths.csv`
  - `01_AIGC/exports/video_clip_sequence.csv`
- Created package archive:
  - `01_AIGC/exports/coin_slot_aigc_overnight_package.zip`
- Created reusable skill `overnight-autonomous-runner` at `C:\Users\user1\.codex\skills\overnight-autonomous-runner`.
- Validated `overnight-autonomous-runner` with `quick_validate.py`; result: `Skill is valid!`.
- Created heartbeat automation:
  - id: `continue-overnight-work`
  - name: `Continue 投币口 overnight work`
  - schedule: every 30 minutes
  - target: current thread
- Heartbeat resumed at `2026-05-21 21:49:42 +08:00`, read this log first, found no new user requirements, and confirmed no stale old-conflict keywords outside `TASK_LOG.md`.
- Deleted heartbeat automation `continue-overnight-work` because all current known requirements are complete and continued checks would be obsolete until the user adds new work.
- 2026-05-22: Upgraded the AIGC video director workflow based on the principle that AIGC video constrains model inference rather than filming reality.
- 2026-05-22: Updated `C:\Users\user1\.codex\skills\cinematic-storyboard-director\references\aigc-video.md` with motion direction, subject position, start/end frame, path, prompt structure, keyframe, and testing rules.
- 2026-05-22: Added project workflow files:
  - `01_AIGC/11_aigc_director_workflow.md`
  - `01_AIGC/12_motion_control_table.md`
  - `01_AIGC/13_generation_units.md`
  - `01_AIGC/14_structured_video_prompts.md`
  - `01_AIGC/15_aigc_preflight_checklist.md`
- 2026-05-22: Updated existing AIGC index and plan files so actual video generation now starts from generation units and structured prompts rather than the narrative storyboard alone.
- 2026-05-22: Rebuilt `01_AIGC/exports/coin_slot_aigc_overnight_package.zip` with the new workflow files, whitebox references, generated visual assets, export CSVs, and normal shooting translation.
- 2026-05-22: Updated reusable skill `codex-connection-resilience` at `C:\Users\user1\.codex\skills\codex-connection-resilience` for network disconnect, rate-limit, resume prompt, and optional local watchdog recovery.
- 2026-05-22: Verified watchdog script `C:\Users\user1\.codex\skills\codex-connection-resilience\scripts\watch-codex-link.ps1` creates `.codex-resume/RESUME_PROMPT.md` for this project in safe `PrepareOnly` mode.
- 2026-05-22: Confirmed local packaged Codex executable is discoverable but cannot launch from PowerShell here (`Access is denied`), so `CliResume` must stay opt-in and needs a working Codex CLI path via `-CodexPath` before it can auto-resume.
- 2026-05-22: User identified two major issues:
  - character references are too generic and lack memorable personality, face/body traits, expression range, and visual hooks
  - 20 macro shots are far too few for a 5-6 minute film under the newer fine-storyboard rule
- 2026-05-22: Added character redesign system:
  - `01_AIGC/16_character_design_bible_v2.md`
  - `01_AIGC/17_character_sheet_generation_prompts_v2.md`
- 2026-05-22: Added production micro-storyboard system:
  - `01_AIGC/18_micro_storyboard_rules_v4.md`
  - `01_AIGC/19_micro_storyboard_188_panels.csv`
  - `01_AIGC/20_micro_storyboard_generation_batches.md`
  - `01_AIGC/21_asset_expansion_plan_v2.md`
  - `01_AIGC/22_micro_storyboard_prompt_pack.md`
- 2026-05-22: Added export planning CSVs:
  - `01_AIGC/exports/character_design_v2_asset_plan.csv`
  - `01_AIGC/exports/micro_storyboard_asset_plan.csv`
  - `01_AIGC/exports/micro_storyboard_image_prompts.csv`
- 2026-05-22: Created planned output directories:
  - `01_AIGC/character_design_v2`
  - `01_AIGC/micro_storyboard_panels/B01` through `B06`
  - `01_AIGC/micro_storyboard_contact_sheets`
  - `01_AIGC/micro_keyframes_v2`
  - `01_AIGC/whitebox_renders_v2`
- 2026-05-22: Updated `README.md`, `00_project_rules.md`, `01_visual_continuity_bible.md`, `04_video_prompts.md`, `05_negative_constraints.md`, `06_keyframe_prompts.md`, `07_generation_run_plan.md`, `08_shot_asset_map.md`, `10_morning_review_index.md`, `14_structured_video_prompts.md`, and `15_aigc_preflight_checklist.md` to treat the old 20-shot board as macro storyboard only.
- 2026-05-22: Rebuilt `01_AIGC/exports/coin_slot_aigc_overnight_package.zip` with the new files.
- 2026-05-22: Added reusable dialogue/voice/audio rules to `C:\Users\user1\.codex\skills\cinematic-storyboard-director`:
  - `references/dialogue-voice-audio.md`
  - updated `SKILL.md`, `references/workflow.md`, and `references/output-templates.md`
- 2026-05-22: Added project audio design module:
  - `01_AIGC/23_dialogue_voice_sound_music_plan.md`
  - `01_AIGC/24_wav_generation_and_audio_assembly_plan.md`
  - `01_AIGC/exports/dialogue_voice_decision_table.csv`
  - `01_AIGC/exports/dialogue_voice_assets.csv`
  - `01_AIGC/exports/sound_music_cue_sheet.csv`
  - `01_AIGC/exports/audio_assembly_manifest.csv`
- 2026-05-22: Added visual dual-version and spatial consistency production rules:
  - `01_AIGC/25_visual_asset_dual_version_rules.md`
  - `01_AIGC/26_spatial_consistency_bible_v1.md`
  - `01_AIGC/27_whitebox_expansion_plan_v2.md`
  - `01_AIGC/exports/micro_storyboard_pure_image_prompts.csv`
  - `01_AIGC/exports/micro_storyboard_annotation_metadata.csv`
  - `01_AIGC/exports/visual_asset_dual_version_plan.csv`
  - `01_AIGC/exports/whitebox_expansion_plan.csv`
  - `01_AIGC/exports/visual_asset_qa_checklist.csv`
  - `01_AIGC/exports/visual_asset_issue_log.csv`
- 2026-05-22: Changed normal shooting strategy to delta-only references:
  - `02_Normal_Shooting/05_delta_only_reference_plan.md`
  - `01_AIGC/exports/normal_shooting_delta_asset_plan.csv`
- 2026-05-22: Rendered 169 required whitebox v2 images with Blender via `01_AIGC/blender/render_whitebox_v2.py`.
- 2026-05-22: Added reusable whitebox contact sheet tooling:
  - `01_AIGC/tools/make_contact_sheet.py`
  - `01_AIGC/whitebox_contact_sheets_v2`
  - `01_AIGC/whitebox_contact_sheets_v2_passcheck`
- 2026-05-22: User caught a major whitebox QA miss: many whiteboxes were repeated or near-repeated. Root cause was `render_whitebox_v2.py` reusing the same source camera across many MSB panels with only tiny deterministic offsets; the static whitebox did not encode panel-specific action, subject focus, or blocking.
- 2026-05-22: Integrated perceptual similarity detection into `01_AIGC/tools/qa_whitebox_images.py`; QA now writes `similarity_ok`, `similarity_cluster`, `similarity_reference`, and `similarity_score`, plus `exports/whitebox_similarity_report.csv`.
- 2026-05-22: Upgraded whitebox production to panel-level default after user clarified that whiteboxes must closely match final real-image composition/proportion/space:
  - `exports/whitebox_expansion_plan.csv` is now 188/188 `whitebox_required=yes`.
  - `exports/whitebox_qa_checklist.csv` was rebuilt to 188 rows.
  - Added `01_AIGC/29_whitebox_scale_and_blocking_bible_v1.md`.
  - Added `01_AIGC/30_whitebox_panellevel_qa_result_v1.md`.
  - Added `exports/whitebox_scale_anchor_table.csv`.
  - Updated `render_whitebox_v2.py` to hide static base character anchors and rebuild panel-specific character/prop/action blocking per render.
  - Updated `qa_whitebox_images.py` so near-duplicate detection uses grayscale, dHash, RGB color difference, and story foreground mask instead of only gray full-frame similarity.
  - Re-rendered all 188 whiteboxes and generated final contact sheets in `01_AIGC/whitebox_contact_sheets_v2_panellevel_final`.
  - Latest automatic QA: `auto_pass_needs_human_review=188 failed=0 missing=0 similarity_clusters=0 similarity_flagged=0`.

## In Progress

- Audio design, visual dual-version rules, whitebox expansion rules, and QA tables are complete.
- Panel-level whiteboxes are rendered and automatic QA has passed, but human/director contact-sheet review is still needed before treating them as final structural references.
- Formal pure-image generation has started. MSB001-MSB003 have v002 pure images generated and need human/director review before annotated copies.
- Final production WAV files are not yet generated; guide WAVs and the storyboard animatic exist.
- Heartbeat automation is not currently active.

## Next Tasks

1. Continue real pure-image production from `01_AIGC/exports/micro_storyboard_pure_image_prompts.csv`, using `story_stage`, `whitebox_reference_path`, and the S0 clean character refs.
2. Prioritize A-level panels and stage transitions: S0 opening, S3/S4 conflict, S5 escape, S6/S7 phone, S8 8-bit UI.
3. For every generated pure image, run/update `exports/visual_asset_qa_checklist.csv`; root-cause failures in `exports/visual_asset_issue_log.csv`.
4. Generate annotated working copies only after pure images pass, using `01_AIGC/tools/annotate_visual_asset.py`.
5. Replace whitebox placeholders in `exports/animatic/coin_slot_storyboard_animatic_v001.mp4` as more real pure images pass.
6. Replace SAPI/programmatic guide WAVs with final voice, foley, ambience, SFX, and music when a production-grade TTS/audio model or recorded performance is available.
8. After micro-storyboards pass, select keyframe/start/end candidates into `01_AIGC/micro_keyframes_v2` and only then return to video generation units.
9. Produce the PPT-style timed storyboard video after storyboard images and audio are available.
10. If network/disconnect resilience is needed, start the watchdog in safe mode:
   `powershell -ExecutionPolicy Bypass -File "C:\Users\user1\.codex\skills\codex-connection-resilience\scripts\watch-codex-link.ps1" -Workspace "E:\视觉\投币口"`
11. Only use `-Mode CliResume` after confirming a Codex CLI executable can be launched from PowerShell, or after passing a known working executable with `-CodexPath`.

## Blockers Or Issues

- Codex cannot guarantee autonomous continuation if the app, thread, model access, or tool execution is forcibly stopped by the host system.
- If quota/rate limits occur, the durable fallback is to record the state here and use a heartbeat/retry strategy when available.
- Local `codex --help` currently fails from PowerShell with `Access is denied` for the WindowsApps packaged executable. The watchdog can still prepare recovery prompts, but automatic CLI resume is blocked until a launchable CLI path is provided.

## Validation / Tests Run

- Blender background render completed successfully for 21 whitebox cameras.
- Stale story keyword scan returned no old conflict terms for:
  - `勒索`
  - `索要`
  - `门口冲突`
  - `门口失手`
  - `砸凳`
  - `挥动书包`
  - `游戏厅外`
  - `CAM_EXTERIOR`
  - `CONFLICT_SIDE`
  - `EXIT_CONFLICT`
  - `CHASE_VECTOR`
- Current asset counts:
  - character_refs: 2
  - scene_refs: 6
  - keyframes: 12
  - storyboard_panels: 20
  - contact_sheets: 7
- `asset_output_paths.csv` rows: 20; missing asset files: none.
- `video_clip_sequence.csv` rows: 20; missing whitebox files: none.
- Stale keyword scan excluding `TASK_LOG.md` found no matches for old conflict wording or old camera IDs.
- Heartbeat automation file confirmed at `C:\Users\user1\.codex\automations\continue-overnight-work\automation.toml`.
- Heartbeat stale keyword scan at `2026-05-21 21:49:42 +08:00`, excluding `TASK_LOG.md`, found no matches.
- 2026-05-22 validation:
  - `cinematic-storyboard-director` skill validated with `quick_validate.py`; result: `Skill is valid!`.
  - New AIGC workflow files exist: 5/5.
  - `12_motion_control_table.md` contains 20 story rows.
  - `13_generation_units.md` contains 27 generation units.
  - `14_structured_video_prompts.md` contains 27 prompt sections.
  - Every structured prompt has Camera, Subject, Motion, Scene, Composition, Lighting, Style, Keep consistent, and Avoid fields.
  - `asset_output_paths.csv` rows: 20; missing asset files: none.
  - `video_clip_sequence.csv` rows: 20; missing whitebox files: none.
  - Rebuilt package archive size: 64,527,672 bytes.
  - Archive contains `11_aigc_director_workflow.md` through `15_aigc_preflight_checklist.md`.
  - Stale keyword scan excluding `TASK_LOG.md` found no matches for old conflict wording or old camera IDs.
- 2026-05-22 connection resilience validation:
  - `codex-connection-resilience` skill validated with `quick_validate.py`; result: `Skill is valid!`.
  - Watchdog `-Once -DryRun` on this project succeeded and would write `.codex-resume/RESUME_PROMPT.md`.
  - Watchdog with failed probe URL reported `Connectivity unavailable; waiting for recovery` and did not attempt resume.
  - Watchdog `PrepareOnly` non-dry run wrote `E:\视觉\投币口\.codex-resume\RESUME_PROMPT.md`.
  - Watchdog `CliResume -DryRun` printed the exact `codex resume --last "<prompt>" --cd "<workspace>"` command without launching Codex.
  - Watchdog non-dry `CliResume` skipped auto-resume because the local Codex CLI cannot launch from PowerShell (`Access is denied`).
  - Missing `TASK_LOG.md` dry-run test warned clearly and did not auto-resume.
  - Existing lock dry-run test skipped resume during cooldown as expected.
- 2026-05-22 character/micro-storyboard upgrade validation:
  - `19_micro_storyboard_188_panels.csv` rows: 188.
  - Clip panel distribution: 01=8, 02=10, 03=10, 04=9, 05=12, 06=8, 07=8, 08=10, 09=10, 10=12, 11=10, 12=12, 13=9, 14=10, 15=8, 16=8, 17=7, 18=8, 19=8, 20=11.
  - Micro-storyboard asset plan rows: 188.
  - Micro-storyboard image prompt rows: 188.
  - Character design v2 asset plan rows: 32.
  - Micro-storyboard batches: B01=28, B02=29, B03=28, B04=34, B05=35, B06=34.
  - Asset type counts in micro storyboard: storyboard=117, keyframe=34, start_frame=15, end_frame=20, prop=2.
  - New required files 16-22 and export CSVs exist.
  - Rebuilt package archive size: 64,979,843 bytes.
- 2026-05-22 audio/dual-visual/whitebox planning validation:
  - Dialogue/voice decision rows: 20.
  - Dialogue/voice asset rows: 22.
  - Sound/music cue rows: 27.
  - Audio assembly manifest rows: 48.
  - Micro-storyboard pure image prompt rows: 188.
  - Micro-storyboard annotation metadata rows: 188.
  - Visual dual-version plan rows: 220.
  - Whitebox expansion plan rows: 188; required=yes 169, optional 19.
  - Whitebox required by batch: B01=17, B02=29, B03=20, B04=34, B05=35, B06=34.
  - Normal shooting delta asset plan rows: 7.
  - Visual asset QA checklist rows: 220.
- 2026-05-22 whitebox v2 render and QA validation:
  - Blender `render_whitebox_v2.py` rendered 169 required whiteboxes; skipped=0.
  - Low-level image QA initially passed all 169 after camera target fixes.
  - User review identified widespread duplicate/near-duplicate whiteboxes that low-level QA missed.
  - Root cause: repeated source camera reuse with tiny offsets and no panel-specific blocking/action encoding.
  - `qa_whitebox_images.py` now includes perceptual similarity QA using MAD and dHash.
  - Current result: auto_pass_needs_human_review=73, failed=96, missing=0, similarity_clusters=16, similarity_flagged=96.
  - `exports/whitebox_similarity_report.csv` and `exports/whitebox_issue_log.csv` record the failure; pure image generation remains blocked.
- 2026-05-22 whitebox generation repair attempt:
  - Added semantic target, panel proxy, and camera override logic to `01_AIGC/blender/render_whitebox_v2.py`.
  - First semantic pass reduced duplicate failures from 96 to 9 but introduced 29 low-level blocked/flat failures.
  - Second pass currently reports auto_pass_needs_human_review=109, failed=60, missing=0, similarity_clusters=3, similarity_flagged=18.
  - Root cause remains generation-side: scene-safe camera rails and per-panel blocking need to be designed more deliberately before pure image generation.
- 2026-05-22 panel-level whitebox final:
  - Rebuilt whitebox expansion to 188/188 required panels.
  - Rendered `whitebox_renders_v2` for all 188 MSB panels.
  - Final whitebox QA: `auto_pass_needs_human_review=188`, `failed=0`, `missing=0`, `similarity_clusters=0`, `similarity_flagged=0`.
  - Contact sheets: `01_AIGC/whitebox_contact_sheets_v2_panellevel_final/B01_contact_sheet.jpg` through `B06_contact_sheet.jpg`.
- 2026-05-22 story-stage and character similarity fix:
  - Added stage-state continuity to `01_AIGC/00_project_rules.md`, `31_story_stage_continuity_rules.md`, and reusable skill reference `cinematic-storyboard-director/references/aigc-video.md`.
  - Added `01_AIGC/32_character_similarity_qa_protocol.md`.
  - Added `01_AIGC/33_pipeline_review_and_next_project_rules.md`.
  - Added `exports/panel_stage_state_map.csv` and updated 188 pure/image prompt rows with `story_stage`, `character_stage_lock`, `wardrobe_state`, `environment_stage_lock`, and `whitebox_reference_path`.
  - Old dirty/too-similar character refs were downgraded to stage reference or rejected similarity reference.
  - Generated S0 clean character candidates:
    - `01_AIGC/character_design_v2/CHR_BRO_A_older_brother_front_design_v002_clean.png`
    - `01_AIGC/character_design_v2/CHR_BRO_B_protagonist_front_design_v002_clean.png`
    - `01_AIGC/character_design_v2/CHR_BRO_C_younger_brother_front_design_v003_clean_distinct.png`
  - QA contact sheet: `01_AIGC/contact_sheets/character_s0_clean_v002_contact_sheet_ascii.jpg`.
- 2026-05-22 first real micro-storyboard production:
  - Generated pure real image `01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB012_v001.png`.
  - Generated annotated working copy `01_AIGC/visual_assets/annotated/micro_storyboard/B01/MSB012_v001_annotated.png`.
  - Updated `exports/visual_asset_dual_version_plan.csv`, `exports/visual_asset_qa_checklist.csv`, and `exports/visual_asset_issue_log.csv`.
  - Added `exports/real_image_generation_queue.csv` with 188 ordered rows; MSB012 marked generated, remaining panels queued.
- 2026-05-22 audio guide and animatic:
  - Installed local `imageio` and `imageio-ffmpeg` Python packages for video muxing.
  - Generated 21 SAPI guide voice WAVs using `Microsoft Huihui Desktop`; this is timing guide only, not final child performance.
  - Added `01_AIGC/tools/build_audio_guide.py`.
  - Generated 27 programmatic ambience/SFX/music guide WAVs.
  - Built `01_AIGC/audio/mix/coin_slot_audio_guide_v001.wav` at 48kHz stereo, duration 351 seconds.
  - Added `01_AIGC/tools/build_storyboard_animatic.py`.
  - Built `01_AIGC/exports/animatic/coin_slot_storyboard_animatic_v001.mp4` with 188 timed panels and guide audio; duration 00:05:51, 1280x720, 12 fps, AAC audio.
  - Built `01_AIGC/exports/animatic/animatic_panel_timing.csv`.
- 2026-05-28 formal pure image production start:
  - Generated formal pure images:
    - `01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB001_v002.png`
    - `01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB002_v002.png`
    - `01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB003_v002.png`
  - Preserved existing v001 files and used v002 paths to avoid overwriting prior work.
  - Updated `exports/real_image_generation_queue.csv`, `exports/visual_asset_qa_checklist.csv`, and `exports/visual_asset_dual_version_plan.csv`.
  - Current real-image queue status: `pure_generated_needs_human_review=3`, `queued=184`, `outdated_design_changed_needs_regeneration=1`.
  - Current visual QA status: `pure_generated_needs_human_review=3`, `planned=216`, `rejected_design_changed=1`.
  - Created review contact sheet `01_AIGC/contact_sheets/micro_storyboard_B01_formal_pure_first3_v002.jpg`.
  - Note: MSB001 has a small possible wall-mark/no-text review risk; do not annotate until human/director review confirms it.
- 2026-05-28 SCN_ARCADE lookdev and mother whitebox pivot:
  - Adopted revised environment strategy: generate 3-5 environment lookdev candidates, select a mother image, build a high-fidelity visual constraint whitebox from that mother, derive camera-specific whiteboxes, then use whiteboxes for spatial control and the mother image for style control.
  - Generated SCN_ARCADE lookdev candidates:
    - `01_AIGC/environment_lookdev/SCN_ARCADE/SCN_ARCADE_lookdev_A_entrance_wide_v001.png`
    - `01_AIGC/environment_lookdev/SCN_ARCADE/SCN_ARCADE_lookdev_B_core_cabinet_v001.png`
    - `01_AIGC/environment_lookdev/SCN_ARCADE/SCN_ARCADE_lookdev_C_reaction_corner_v001.png`
  - Refined selected A candidate into `01_AIGC/environment_lookdev/SCN_ARCADE/SCN_ARCADE_lookdev_A_entrance_wide_v002_game_screens.png`, preserving plastic curtain, dim gray-yellow light, narrow CRT cabinet aisle, and using fictional non-infringing 1990s arcade screen types.
  - Blender 5.1.2 macOS CLI/argument launch crashes during Metal/GPU initialization before Python execution; GUI app can open, but CLI/headless/scripted launch is currently not reliable on this machine.
  - Created fallback importable OBJ visual constraint whitebox without Blender runtime:
    - `01_AIGC/environment_lookdev/SCN_ARCADE/whitebox_obj/SCN_ARCADE_mother_visual_constraint_whitebox_v001.obj`
    - `01_AIGC/environment_lookdev/SCN_ARCADE/whitebox_obj/SCN_ARCADE_mother_visual_constraint_whitebox_v001.mtl`
    - `01_AIGC/environment_lookdev/SCN_ARCADE/whitebox_obj/SCN_ARCADE_mother_camera_lock_v001.json`
    - `01_AIGC/environment_lookdev/SCN_ARCADE/whitebox_obj/SCN_ARCADE_scene_asset_design_list_v001.csv`
    - `01_AIGC/environment_lookdev/SCN_ARCADE/whitebox_obj/SCN_ARCADE_visual_constraint_compare_v001.jpg`
  - Added generators:
    - `01_AIGC/tools/build_arcade_obj_whitebox.py`
    - `01_AIGC/blender/create_arcade_mother_whitebox.py` (kept for later when Blender CLI is stable)
- 2026-05-28 Blender macOS crash diagnosis:
  - Parsed local macOS DiagnosticReports `.ips` files and Blender's own `blender.crash.txt`.
  - Local machine in crash logs: `MacBookPro18,2`, `ARM-64`, `translated=false`, macOS `26.5 (25F71)`; display report shows Apple M1 Max 32-core GPU with Metal supported.
  - Tested Blender `5.1.2` installed app and Blender `4.5.10 LTS` official macOS arm64 DMG; both answer `--version`, but CLI/background/script launch crashes before project Python runs.
  - Dominant crash chain: `_platform_strstr` -> `blender::gpu::supports_barycentric_whitelist(id<MTLDevice>)` -> `MTLBackend::metal_is_supported()` -> `GPU_backend_type_selection_detect()` -> `WM_init()` -> `main`.
  - Conclusion: this is not caused by SCN_ARCADE scene complexity or the Python generation script; it is likely a Blender/Apple Metal compatibility problem on this macOS + Apple Silicon path. M1 Max is relevant to the Metal driver path, but not because the hardware is underpowered.
  - Added diagnosis note: `01_AIGC/environment_lookdev/SCN_ARCADE/BLENDER_MACOS_CRASH_NOTES.md`.
- 2026-05-28 SCN_ARCADE mother OBJ imported to Blender:
  - Added `01_AIGC/blender/import_arcade_mother_obj.py`.
  - Imported `01_AIGC/environment_lookdev/SCN_ARCADE/whitebox_obj/SCN_ARCADE_mother_visual_constraint_whitebox_v001.obj` through Blender GUI with explicit `Y` forward / `Z` up OBJ axis settings.
  - Created locked review camera `CAM_SCN_ARCADE_MOTHER_MATCH` from `SCN_ARCADE_mother_camera_lock_v001.json`.
  - Saved Blender file `01_AIGC/blender/SCN_ARCADE_mother_visual_constraint_whitebox_v001.blend`.
  - Rendered verified preview `01_AIGC/environment_lookdev/SCN_ARCADE/whitebox_obj/SCN_ARCADE_blender_import_preview_v001.png`.
  - Note: background Blender still crashes before Python execution on this machine; GUI `--python` works for this import path.
- 2026-05-28 SCN_ARCADE derived camera constraint whiteboxes:
  - Added `01_AIGC/tools/build_arcade_camera_whiteboxes.py`.
  - Generated 7 camera-specific whiteboxes from the same SCN_ARCADE OBJ proxy geometry:
    - `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/CAM_ARCADE_01_ENTRANCE_WIDE_constraint_whitebox_v001.png`
    - `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/CAM_ARCADE_01_CHILD_POV_CENTER_constraint_whitebox_v001.png`
    - `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/CAM_ARCADE_02_STREET_FIGHTER_CABINET_constraint_whitebox_v001.png`
    - `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/CAM_ARCADE_03_DUEL_OVER_SHOULDER_constraint_whitebox_v001.png`
    - `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/CAM_ARCADE_04_BOSS_LOSES_REACTION_constraint_whitebox_v001.png`
    - `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/CAM_ARCADE_DETAIL_CONTROL_PANEL_constraint_whitebox_v001.png`
    - `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/CAM_ARCADE_CEILING_PRESSURE_constraint_whitebox_v001.png`
  - Added contact sheet: `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/SCN_ARCADE_camera_constraints_contact_sheet_v001.jpg`.
  - Added camera manifest and 39-panel mapping:
    - `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/SCN_ARCADE_camera_constraint_manifest_v001.csv`
    - `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/SCN_ARCADE_camera_constraint_manifest_v001.json`
    - `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/SCN_ARCADE_panel_camera_constraint_map_v001.csv`
  - Validation: 7/7 images generated at `1672x941`, nonblank check passed, minimum visible projected faces = 110.
  - Panel map covers all SCN_ARCADE panels `MSB019`-`MSB057`; detail inserts `MSB025`, `MSB033`, `MSB037`, `MSB039` use `CAM_ARCADE_DETAIL_CONTROL_PANEL`; atmosphere insert `MSB026` uses `CAM_ARCADE_CEILING_PRESSURE`.
  - Updated `01_AIGC/environment_lookdev/SCN_ARCADE/DELIVERABLES.md` and added `camera_whiteboxes_v001/README.md`.
- 2026-05-28 SCN_ARCADE formal prompt pack:
  - Added `01_AIGC/tools/build_arcade_formal_prompt_pack.py`.
  - Generated `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/SCN_ARCADE_formal_storyboard_prompt_pack_v001.csv`.
  - Generated `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/SCN_ARCADE_formal_storyboard_prompt_pack_v001.md`.
  - Validation: 39 rows, `MSB019` through `MSB057`, all marked `ready_for_formal_generation_with_mother_style_and_whitebox_space`.
  - Camera distribution: `CAM_ARCADE_01_ENTRANCE_WIDE=8`, `CAM_ARCADE_02_STREET_FIGHTER_CABINET=7`, `CAM_ARCADE_03_DUEL_OVER_SHOULDER=11`, `CAM_ARCADE_04_BOSS_LOSES_REACTION=8`, `CAM_ARCADE_DETAIL_CONTROL_PANEL=4`, `CAM_ARCADE_CEILING_PRESSURE=1`.
- 2026-05-28 three-brother reference lock update:
  - User approved the revised character direction and specified that Xiao Man should be a small chubby boy.
  - Generated and saved active S0 clean three-view + expression references:
    - `01_AIGC/character_design_v2/CHR_BRO_A_older_brother_turnaround_expression_v001_glasses.png`
    - `01_AIGC/character_design_v2/CHR_BRO_B_protagonist_turnaround_expression_v001_distinct.png`
    - `01_AIGC/character_design_v2/CHR_BRO_C_younger_brother_turnaround_expression_v001_chubby.png`
  - Added contact sheet: `01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg`.
  - Added required reference lock files:
    - `01_AIGC/character_design_v2/THREE_BROTHERS_CHARACTER_REFERENCE_LOCK_v001.md`
    - `01_AIGC/character_design_v2/THREE_BROTHERS_CHARACTER_REFERENCE_LOCK_v001.csv`
  - Updated `01_AIGC/00_project_rules.md` and `01_AIGC/31_story_stage_continuity_rules.md`: any future storyboard/keyframe/video/image edit containing the three brothers must call the corresponding active character reference images, not text-only descriptions.
  - Updated `01_AIGC/exports/character_design_v2_asset_plan.csv` statuses for BRO_A/BRO_C turnaround and expression references.
- 2026-05-28 SCN_ARCADE opening 15s long take design:
  - Created independent long-take design asset for the start of the arcade scene: `LTK_ARCADE_OPEN_001`.
  - User intent: one roughly 15s continuous shot, camera slowly sweeps left to right from broken old factory-side street/game-room exterior, then reveals the three brothers cautiously sneaking in from the right and slipping into the arcade.
  - Added long-take design document: `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_LONG_TAKE_v001.md`.
  - Added video prompt CSV: `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_LONG_TAKE_prompt_v001.csv`.
  - Added blocking board: `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_LONG_TAKE_blocking_board_v001.png`.
  - The long-take prompt explicitly requires the new three-brother references and keeps Xiao Man as a visibly small chubby boy.
- 2026-05-28 video character-load strategy update:
  - User identified that even with locked environments, AIGC video cannot reliably lock many character identities at once.
  - Added project rule: each video generation unit should default to one primary identifiable performer, with Xiaochuan as the main identity axis.
  - Three-brother group shots now primarily carry spatial relationship, height contrast, movement direction, and mood; use back view, side view, partial occlusion, distance, and short/static shots to reduce face drift.
  - Bully group is treated as group pressure by default; only Binzi needs recurring identifiable face continuity.
  - Saved regenerated MSB012 pure frame candidate:
    - `01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB012_v002.png`
  - Added review contact sheet:
    - `01_AIGC/contact_sheets/micro_storyboard_B01_formal_pure_first4_v002.jpg`
  - Updated `exports/real_image_generation_queue.csv`, `exports/visual_asset_qa_checklist.csv`, and `exports/visual_asset_dual_version_plan.csv`; MSB012 is now `pure_generated_needs_human_review`.
- 2026-05-28 prop-causality continuity update:
  - User caught a logic error in MSB012_v002: distant arcade curtain was already pulled open although no character was at the doorway.
  - Added prop-causality rules to `00_project_rules.md`, `31_story_stage_continuity_rules.md`, and `33_pipeline_review_and_next_project_rules.md`.
  - Rule: state-changing props such as door curtains, doors, phone receivers, stones, bags, lights, and arcade screens must keep their previous state unless a visible/current or prior-panel cause changes them.
  - Regenerated and saved:
    - `01_AIGC/visual_assets/pure/micro_storyboard/B01/MSB012_v003.png`
  - Added updated review contact sheet:
    - `01_AIGC/contact_sheets/micro_storyboard_B01_formal_pure_first4_v003.jpg`
  - Updated queue/QA/dual-version plan to use MSB012_v003. The new candidate fixes the curtain causality, with a remaining no-text review note for tiny right-wall paper/sign details.
- 2026-05-28 SCN_ARCADE opening long-take keyframe split:
  - Split `LTK_ARCADE_OPEN_001` into four generation anchors:
    - `LTK_ARCADE_OPEN_KF01` at `0.0s`: empty wet factory-side street, no characters.
    - `LTK_ARCADE_OPEN_KF02` at `5.0s`: hidden arcade entrance reveal, dirty plastic strips and CRT glow.
    - `LTK_ARCADE_OPEN_KF03` at `10.0s`: three brothers sneak in from right; A Lei, Xiao Chuan, and chubby Xiao Man.
    - `LTK_ARCADE_OPEN_KF04` at `14.5s`: curtain wipe into arcade, boys swallowed by cabinet glow.
  - Added keyframe design document: `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_KEYFRAMES_v001.md`.
  - Added keyframe prompt CSV: `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_KEYFRAME_PROMPTS_v001.csv`.
  - Added clean keyframe board: `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_KEYFRAME_BOARD_v003.png`.
  - Validation: keyframe prompt CSV has 4 rows, all statuses `ready_for_keyframe_generation`; all 5 referenced assets exist (environment mother, interior whitebox, and three active brother references).
  - Note: v001/v002 keyframe boards remain as scratch versions; use v003 for review.
- 2026-05-28 universal camera-subject continuity rule:
  - User identified a reusable storyboard logic failure: follow/entry shots must not default to front-facing portraits; character facing, gaze, body movement, and camera motivation must match adjacent-panel logic.
  - Added project execution rule `01_AIGC/34_camera_subject_logic_rules.md`.
  - Added universal reusable rule `NEW_PROJECT_COPY_PACK_v1/docs/CAMERA_SUBJECT_CONTINUITY_RULES.md`.
  - Updated `NEW_PROJECT_COPY_PACK_v1/00_START_HERE.md`, `docs/NEW_PROJECT_MANUAL.md`, `docs/SKILL_PACK_README.md`, and `docs/SKILL_CHANGELOG.md`.
  - Updated current project rules: `01_AIGC/00_project_rules.md` and `01_AIGC/33_pipeline_review_and_next_project_rules.md`.
  - Moved `MSB020_v002` and `MSB021_v002` to rejected as `wrong_camera_subject_relation`.
  - Updated queue/QA/prompt paths for `MSB020` and `MSB021` to `v003`, with rear-follow/back-facing camera-subject locks.
- 2026-05-28 whitebox constraint correction:
  - User correctly identified that the latest attempted follow-up generation did not truly use whitebox constraints; the prompt only mentioned whitebox paths in text.
  - Stopped importing the newly generated MSB007-MSB011 attempts into the project. Queue/QA remain unchanged for MSB007-MSB011 (`queued`/`planned`).
  - Added rule: a whitebox path in text is not sufficient. Formal pure image generation must either use the whitebox image as actual visual input/image reference or use an approved mother image plus the corresponding whitebox as joint visual constraints.
  - Text-only generations are now classified as exploration only and must not be promoted to `pure_generated_needs_human_review`.
- 2026-05-28 SCN_ARCADE long-take keyword image-generation test:
  - Generated first AI still test for `LTK_ARCADE_OPEN_KF03` using the long-take keyframe prompt, SCN_ARCADE mother style image, entrance whitebox, three-brother character contact sheet, and keyframe board as actual visible references.
  - Saved project copy:
    - `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF03_test_v001.png`
    - `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF03_test_v002.png`
  - Added test manifest:
    - `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_KEYFRAME_TESTS_v001.csv`
  - Validation: PNG `1672x941`, nonblank visual check passed.
  - QA result: the model understands the long-take/keyframe keyword approach well enough for a usable first pass. Environment, plastic curtain, CRT spill, A Lei glasses, Xiao Chuan backpack/scarf, and chubby Xiao Man are readable.
  - v001 issue: the boys felt more like they had already gathered at the entrance than just entered from frame right.
  - v002 improvement: stronger long-take blocking, with empty left/center factory-wall atmosphere and the brothers compressed near the right-side arcade entrance. Use v002 composition language for the formal KF03 prompt.
- 2026-05-28 SCN_COMPOUND mother image selection:
  - User selected the first old-compound exploration image as acceptable.
  - Saved it as the approved SCN_COMPOUND visual mother:
    - `01_AIGC/environment_lookdev/SCN_COMPOUND/SCN_COMPOUND_lookdev_A_courtyard_route_mother_v001.png`
  - Added deliverables/use rules:
    - `01_AIGC/environment_lookdev/SCN_COMPOUND/DELIVERABLES.md`
  - This image is a style/material/lighting mother only, not a completed MSB panel. Future SCN_COMPOUND formal frames must use this mother together with panel-specific whitebox references.
- 2026-05-28 SCN_ARCADE opening long-take full keyframe test set:
  - Continued from the KF03 test and generated the remaining long-take anchor stills with actual visible references loaded into the image model, not text-only path mentions.
  - Saved project copies:
    - `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF01_test_v001.png`
    - `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF02_test_v001.png`
    - `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF04_test_v001.png`
  - Created review contact sheet:
    - `01_AIGC/long_take_design/test_generations/SCN_ARCADE_OPENING_15S_KEYFRAME_TEST_CONTACT_SHEET_v001.jpg`
  - Updated test manifest:
    - `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_KEYFRAME_TESTS_v001.csv`
  - Validation: KF01/KF02/KF03_v002/KF04 all saved as PNG `1672x941`; contact sheet rendered and inspected.
  - QA result: the 4-frame sequence now reads as a continuous left-to-right sweep: empty factory street, right-side hidden entrance reveal, three brothers entering from the right, and curtain-wipe into the arcade. Prop causality is preserved: the KF02 curtain stays still, and KF04 shows A Lei visibly lifting the plastic strip. Character load is handled with back/side/occlusion on KF04; Xiao Man remains visibly small and chubby.
- 2026-06-02 SCN_ARCADE opening long-take formal reference lock:
  - Promoted the tested 4-anchor sequence into a formal reference-lock package for future keyframe/video generation.
  - Added reference lock:
    - `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_REFERENCE_LOCK_v001.md`
  - Added formal keyframe prompt CSV:
    - `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_FORMAL_KEYFRAME_PROMPTS_v002.csv`
  - Added formal video prompt CSV:
    - `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_FORMAL_VIDEO_PROMPT_v002.csv`
  - Active anchor decision: use `LTK_ARCADE_OPEN_KF03_test_v002.png` as the official KF03 blocking anchor; keep `KF03_test_v001.png` only as a superseded test.
  - Validation: formal keyframe CSV parsed with 4 rows / 8 fields; formal video CSV parsed with 1 row / 11 fields; all required visual references exist; selected KF01/KF02/KF03_v002/KF04 anchors are all `1672x941`.
  - Generation rule reinforced: formal generation for this shot must load visible image references. Text-only path mentions remain exploration-only and must not be promoted.
- 2026-06-02 SCN_ARCADE opening long-take video execution package:
  - Added video generation runbook:
    - `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_VIDEO_RUNBOOK_v001.md`
  - Added machine-readable video QA checklist:
    - `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_VIDEO_QA_CHECKLIST_v001.csv`
  - Runbook covers three execution routes: multi-keyframe video, first/last-frame video, and one-frame image-to-video fallback.
  - QA checklist defines 13 pass/fail checks covering camera continuity, KF01/KF02 no-character state, curtain causality, KF03 blocking, the three brother identities, arcade consistency, IP safety, no extra cast, and mood.
  - Validation: runbook file exists; QA checklist has 14 lines including header / 13 checks; formal video prompt and reference lock remain present.
- 2026-06-02 SCN_ARCADE opening long-take deliverables index:
  - Added human-readable deliverables index:
    - `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_DELIVERABLES_v001.md`
  - Added machine-readable deliverables index:
    - `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_DELIVERABLES_v001.csv`
  - The index collects the active formal package, visual anchors, environment/whitebox dependencies, and three-brother character references.
  - It explicitly marks `LTK_ARCADE_OPEN_KF03_test_v002.png` as the active KF03 anchor and `LTK_ARCADE_OPEN_KF03_test_v001.png` as superseded.
  - Validation: deliverables CSV parsed with 20 rows; all referenced paths exist; status distribution `active=19`, `superseded=1`.

## Last Successful Work Time

2026-06-02 22:13:40 +0800

## Rate Limit / Quota Notes

No current rate-limit or quota error has been observed in this phase.

## Resume Instructions

On any restart or wakeup:

1. Read this `TASK_LOG.md` first.
2. Continue from `Next Tasks`.
3. Prefer AIGC project deliverables over normal shooting deliverables unless the user redirects.
4. Update this file after every meaningful phase and before any expected interruption.
5. If no new work is requested, leave the project marked complete for current known requirements.
