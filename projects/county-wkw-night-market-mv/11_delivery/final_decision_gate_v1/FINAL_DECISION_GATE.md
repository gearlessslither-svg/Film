# Final Decision Gate V1

Project: `county-wkw-night-market-mv`  
Chinese title: 县城王家卫  
Project type: music MV, weak story, strong mood/visuals  
Gate date: 2026-07-08

## Current Verified State

The project has no blocking internal failures in the latest local validation:

- Validator: `10_qa/validate_completion_state.py`
- Latest JSON: `10_qa/completion_state_v1.json`
- Latest CSV: `10_qa/completion_state_v1.csv`
- Current status: `pending_director_or_external_i2v`
- Blocking failures: `0`
- Director acceptance: `pending`

This means the creative files, lookdev images, asset locks, 14 keyframes, 14 bilingual video prompts, no-music audio rule, local proxy clips, proxy MV, upload package, zip integrity, and current proxy candidate checksums are ready.

## Why The Project Is Not Final Yet

One of these two final gates must be completed:

1. The director explicitly accepts the local proxy motion style as the final MV style.
2. The 14 returned external image-to-video clips are placed in the intake folder, assembled, QA'd, and packaged as the final external-AIGC MV.

Until one gate is complete, the project is production-ready but not final-delivery complete.

## Option A - Accept Proxy Style As Final

Use this path only if the director accepts the local pan/zoom proxy motion as the final visual language.

Authoritative acceptance evidence:

- Update `11_delivery/final_proxy_candidate_v1/DIRECTOR_ACCEPTANCE_NOTE.md`
- Change the decision line to a status beginning with `accepted`, for example:
  `Status: accepted_proxy_final - 2026-07-08`
- State the final audio choice:
  - `with_scratch_music`
  - `ambience_only`
  - `replace_music_later`

After acceptance:

1. Run `python3 11_delivery/final_decision_gate_v1/finalize_proxy_acceptance.py --confirm-director-accepts-proxy-final --audio-choice with_scratch_music`
2. If the final audio choice is different, replace `with_scratch_music` with `ambience_only` or `replace_music_later`.
3. The script updates the acceptance note, audit, handoff, README, checksums, proxy candidate zip, final decision gate zip, and completion validator output.

Completion evidence for this path:

- `completion_state_v1.json` reports `overall_status=complete_proxy_final`
- The final proxy candidate zip passes zip validation
- Handoff states proxy final has been accepted

## Option B - Continue External I2V

Use this path if the director wants true image-to-video motion.

Upload source:

- `11_delivery/packages/external_i2v_upload_v1/county_wkw_external_i2v_upload_v1.zip`

Returned clips must be saved here:

- `09_edit/external_clips/external_i2v_clips_v1/`

Expected returned filenames:

- `VP001_KF001_external_i2v.mp4`
- `VP002_KF002_external_i2v.mp4`
- `VP003_KF003_external_i2v.mp4`
- `VP004_KF004_external_i2v.mp4`
- `VP005_KF005_external_i2v.mp4`
- `VP006_KF006_external_i2v.mp4`
- `VP007_KF007_external_i2v.mp4`
- `VP008_KF008_external_i2v.mp4`
- `VP009_KF009_external_i2v.mp4`
- `VP010_KF010_external_i2v.mp4`
- `VP011_KF011_external_i2v.mp4`
- `VP012_KF012_external_i2v.mp4`
- `VP013_KF013_external_i2v.mp4`
- `VP014_KF014_external_i2v.mp4`

Hard rule for every external clip:

- ambience / sound effects only
- no music
- no BGM
- no soundtrack

After all 14 clips are present:

1. Run `python3 09_edit/tools/assemble_external_mv_v1.py --check-only`
2. Run `python3 09_edit/tools/assemble_external_mv_v1.py`
3. Run `python3 10_qa/validate_completion_state.py`
4. Review the generated final external files and package
5. Update `10_qa/PROJECT_COMPLETION_AUDIT_V1.md` and `00_admin/handoff/HANDOFF_LATEST.md`

Completion evidence for this path:

- 14 returned external clips are present and readable
- `11_delivery/final_external_mv_v1/county_wkw_external_mv_v1_ambience_only.mp4` exists
- `11_delivery/final_external_mv_v1/county_wkw_external_mv_v1_with_scratch_music.mp4` exists
- `11_delivery/packages/final_external_mv_v1/county_wkw_final_external_mv_v1.zip` exists and passes zip validation
- `completion_state_v1.json` reports `overall_status=complete_external_final`

## Current Recommended Stop Point

Do not generate more still images in this window. The next meaningful action is a director decision or external clip return.
