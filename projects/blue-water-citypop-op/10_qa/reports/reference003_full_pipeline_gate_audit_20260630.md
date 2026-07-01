# Reference-003 Full Pipeline Gate Audit

- Rebuilt: `2026-06-30T15:49:49+08:00`
- Status: `not_complete`
- Completion proven: `False`
- Commands OK: `True`

## Summary

- `keyframes_official_generated`: `42`
- `keyframes_pending`: `0`
- `video_units_ready`: `21`
- `video_units_blocked`: `0`
- `segments_decode_pass`: `0`
- `transition_edges_reviewed`: `0`
- `roughcut_decode_ok`: `False`
- `no_text_logo_safety_pass`: `False`
- `completion_gates_passed`: `6`
- `completion_gates_total`: `11`

## Blocking Gates

- `video_units_21_generated` — current: 0/21 decode pass; evidence: `09_edit/rough_cut/reference003_roughcut_transition_audit_template.json`
- `transition_edges_41_reviewed` — current: 0/41 reviewed; evidence: `09_edit/rough_cut/reference003_roughcut_transition_audit_template.json`
- `roughcut_full_decode` — current: decode=False; evidence: `09_edit/rough_cut/reference003_full_op_roughcut_20260630.mp4`
- `duration_match` — current: duration=None; delta=None; evidence: `09_edit/rough_cut/reference003_full_op_roughcut_20260630.mp4`
- `no_text_logo_safety` — current: 0/64 effective pass; gate=False; evidence: `10_qa/reports/reference003_no_text_logo_safety_review_20260630.json`

## Commands

- `project_validation` — ok=True returncode=0
- `keyframe_status_previs_rebuild` — ok=True returncode=0
- `video_unit_readiness_rebuild` — ok=True returncode=0
- `roughcut_assembly_readiness` — ok=True returncode=0
- `roughcut_transition_audit_rebuild` — ok=True returncode=0
- `no_text_logo_safety_review_refresh` — ok=True returncode=0
- `completion_audit_rebuild` — ok=True returncode=0

## Evidence Files

- `keyframe_status_manifest`: `10_qa/reference_match/REFERENCE003_OFFICIAL_KEYFRAME_STATUS_20260630/manifest.json`
- `video_unit_readiness_manifest`: `08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/manifest.json`
- `roughcut_assembly_report`: `10_qa/reports/reference003_roughcut_assembly_20260630.json`
- `roughcut_transition_audit`: `09_edit/rough_cut/reference003_roughcut_transition_audit_template.json`
- `no_text_logo_safety_review`: `10_qa/reports/reference003_no_text_logo_safety_review_20260630.json`
- `completion_audit`: `10_qa/reports/reference003_completion_audit_template_20260630.json`

## Boundary

This audit proves the current gate state only; it cannot replace missing image/video generation or manual visual safety review.
