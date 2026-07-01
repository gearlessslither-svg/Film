# Reference-003 Frame Promotion R3 Job

- Status: `p0_p1_generated_qa_pass_no_new_mp4`
- Decision manifest: `03_story/expanded_keyframes/reference003_frame_promotion_r3_20260630.json`
- Report: `03_story/expanded_keyframes/reference003_frame_promotion_r3_20260630.md`

## Execution Order

1. Generate only `P0_hard_replace` first:
   - `prompts/OP_SHOT_010_R3_NADIA_PROFILE_BEAUTY_LOCK.md`
   - output: `outputs/OP_SHOT_010_R3_NADIA_PROFILE_BEAUTY_LOCK.png`
2. QA against:
   - identity lock: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_011_v2.png`
   - source reference: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/refs/OP_SHOT_010_ref_002450.jpg`
3. The director chose image-only batch work. All 10 `P1_difference_expansion` prompts have been generated and registered.

Do not use the superseded R2 48-slot plan.

## Outputs

- P0 output: `outputs/OP_SHOT_010_R3_NADIA_PROFILE_BEAUTY_LOCK.png`
- P1 outputs: 10 generated assets under `outputs/OP_SHOT_018_R3_*` through `outputs/OP_SHOT_024_R3_*`
- Contact sheet: `outputs/REFERENCE003_R3_generated_assets_contact_sheet.jpg`

No new mp4 should be generated from this batch unless the director explicitly asks for a preview rebuild.
