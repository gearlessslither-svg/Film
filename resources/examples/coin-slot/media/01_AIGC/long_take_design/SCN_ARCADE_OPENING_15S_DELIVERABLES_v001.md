# SCN_ARCADE Opening 15s Deliverables v001

Shot ID: `LTK_ARCADE_OPEN_001`

Status: ready for first formal video generation test with actual visible references.

This index collects the active files for the SCN_ARCADE opening long take. It exists to prevent version drift.

## Active Formal Package

- Reference lock: `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_REFERENCE_LOCK_v001.md`
- Formal video prompt: `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_FORMAL_VIDEO_PROMPT_v002.csv`
- Formal keyframe prompts: `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_FORMAL_KEYFRAME_PROMPTS_v002.csv`
- Video runbook: `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_VIDEO_RUNBOOK_v001.md`
- Video QA checklist: `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_VIDEO_QA_CHECKLIST_v001.csv`
- Deliverables CSV: `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_DELIVERABLES_v001.csv`

## Active Visual Anchors

- KF01: `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF01_test_v001.png`
- KF02: `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF02_test_v001.png`
- KF03: `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF03_test_v002.png`
- KF04: `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF04_test_v001.png`
- Review sheet: `01_AIGC/long_take_design/test_generations/SCN_ARCADE_OPENING_15S_KEYFRAME_TEST_CONTACT_SHEET_v001.jpg`

Use `LTK_ARCADE_OPEN_KF03_test_v002.png` as the active KF03 anchor. `LTK_ARCADE_OPEN_KF03_test_v001.png` is superseded and should not be used for formal blocking.

## Required Dependencies

- Environment mother: `01_AIGC/environment_lookdev/SCN_ARCADE/SCN_ARCADE_lookdev_A_entrance_wide_v002_game_screens.png`
- Entrance whitebox: `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/CAM_ARCADE_01_ENTRANCE_WIDE_constraint_whitebox_v001.png`
- Keyframe board: `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_KEYFRAME_BOARD_v003.png`
- A Lei reference: `01_AIGC/character_design_v2/CHR_BRO_A_older_brother_turnaround_expression_v001_glasses.png`
- Xiao Chuan reference: `01_AIGC/character_design_v2/CHR_BRO_B_protagonist_turnaround_expression_v001_distinct.png`
- Xiao Man reference: `01_AIGC/character_design_v2/CHR_BRO_C_younger_brother_turnaround_expression_v001_chubby.png`

## Use Order

1. Read the reference lock.
2. Load visual references in the runbook order.
3. Use the formal video prompt.
4. Generate a low-cost preview first.
5. Score the result with the QA checklist.
6. Promote only if the critical QA checks pass.

## Critical Locks

- No text-only path prompting for formal outputs.
- KF01 and KF02 contain no people.
- KF02 curtain does not move without a visible cause.
- KF03 uses the right-edge entry blocking from `KF03_test_v002`.
- KF04 shows A Lei visibly lifting or pushing the curtain.
- Xiao Man remains small and chubby.
- No real game titles, logos, or recognizable copyrighted characters.
