# 县城王家卫 / County Night Market Retro-Future MV

Project slug: `county-wkw-night-market-mv`

Project type: music MV, weak story, strong mood and visual continuity.

Core idea: a boy on a motorcycle meets a girl in a county-town night market. Neon, beer stalls, game booths, cheap LED lights, alleys, rain-wet roads, and fields outside town turn a small Chinese county into a romantic retro-future dream.

Prompt rule: the human-facing shorthand can be “县城王家卫”, but production prompts should describe the visual language directly: 1990s Hong Kong romantic neon mood, slow-shutter blur, saturated fluorescent color, rain, smoke, reflections, off-center close-ups, telephoto compression, and lonely voiceover feeling.

Do not mix this with `micro-disaster`.

## Current Status - 2026-07-08

First lookdev batch complete:

- 8 mood frames generated and copied to `08_generation/jobs/lookdev_moodframes_v1/outputs/`
- contact sheet: `08_generation/jobs/lookdev_moodframes_v1/lookdev_moodframes_v1_contact_sheet.png`
- QA record: `08_generation/jobs/lookdev_moodframes_v1/QA.md`
- idea board: `03_story/idea_board/idea_board.json`

Planning now available:

- first prompt pack: `04_lookdev/LOOKDEV_MOOD_FRAMES_V1.md`
- asset bible: `05_asset_bible/`
- director semantic shot plan: `07_shots/SHOT_PLAN_DIRECTOR_SEMANTIC_V1.md`
- keyframe queue: `07_shots/KEYFRAME_QUEUE_V1.md`
- hardlock candidate job: `08_generation/jobs/hardlocks_v1/`
- hardlock contact sheet: `08_generation/jobs/hardlocks_v1/hardlocks_v1_contact_sheet.png`
- formal keyframes: `08_generation/jobs/keyframes_v1/outputs/`
- keyframe contact sheet: `08_generation/jobs/keyframes_v1/keyframes_v1_contact_sheet.png`
- bilingual video prompts: `08_generation/jobs/video_prompts_v1/PROMPTS.md`
- edit guide: `09_edit/EDIT_GUIDE_V1.md`
- silent static animatic: `09_edit/animatics/static_animatic_v1/county_wkw_static_animatic_v1_silent.mp4`
- local moving preview with scratch music: `09_edit/animatics/moving_preview_v1/county_wkw_moving_preview_v1_with_scratch_music.mp4`
- completion audit: `10_qa/PROJECT_COMPLETION_AUDIT_V1.md`
- static review package: `11_delivery/packages/static_review_v1/MANIFEST.md`
- static review archive: `11_delivery/packages/static_review_v1/county_wkw_static_review_v1.zip`
- moving preview package: `11_delivery/packages/moving_preview_v1/county_wkw_moving_preview_v1.zip`
- local proxy clips: `09_edit/proxy_clips/local_proxy_clips_v1/outputs/`
- final proxy MV with scratch music: `11_delivery/final_proxy_mv_v1/county_wkw_proxy_mv_v1_with_scratch_music.mp4`
- proxy MV package: `11_delivery/packages/proxy_mv_v1/county_wkw_proxy_mv_v1.zip`
- external I2V upload package: `11_delivery/packages/external_i2v_upload_v1/county_wkw_external_i2v_upload_v1.zip`
- external clip intake folder: `09_edit/external_clips/external_i2v_clips_v1/`
- external MV assembly script: `09_edit/tools/assemble_external_mv_v1.py`
- final proxy candidate package: `11_delivery/packages/final_proxy_candidate_v1/county_wkw_final_proxy_candidate_v1.zip`
- completion state validator: `10_qa/validate_completion_state.py`
- latest completion state: `10_qa/completion_state_v1.json` and `10_qa/completion_state_v1.csv`
- final decision gate: `11_delivery/final_decision_gate_v1/FINAL_DECISION_GATE.md`
- proxy finalizer after explicit acceptance: `11_delivery/final_decision_gate_v1/finalize_proxy_acceptance.py`
- final decision gate package: `11_delivery/packages/final_decision_gate_v1/county_wkw_final_decision_gate_v1.zip`
- external final assembly script now creates final external MV manifest, QA, checksums, and package after all 14 returned clips are present.

Latest validation: `overall_status=pending_director_or_external_i2v`, `blocking_failures=0`.

Next recommended step: review `11_delivery/final_decision_gate_v1/FINAL_DECISION_GATE.md`. Then either explicitly accept the proxy style as final, or use `external_i2v_upload_v1` to generate 14 external image-to-video clips and place the returned MP4 files in `09_edit/external_clips/external_i2v_clips_v1/`.
