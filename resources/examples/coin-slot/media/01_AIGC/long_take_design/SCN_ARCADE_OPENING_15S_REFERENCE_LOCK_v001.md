> 双语说明 / Bilingual note: 本文件保留英文原文，以避免破坏提示词、文件名、路径、字段名和脚本读取。中文使用时请把它视为生产记录、规则、索引或提示词资产；英文正文为可执行/可追溯原文。 / The English source text is preserved to keep prompts, filenames, paths, field names, and script parsing stable. Treat this as a production record, rule, index, or prompt asset; the English body is the executable and traceable source text.

# SCN_ARCADE Opening 15s Reference Lock v001

Shot ID: `LTK_ARCADE_OPEN_001`

Purpose: lock the approved visual reference set for the SCN_ARCADE opening long take before any formal video generation or additional in-between keyframe generation.

This file supersedes text-only prompting for this shot. Any formal generation must load the relevant images as actual visible references, not just mention their paths in prompt text.

## Active Reference Set

Environment style mother:

- `01_AIGC/environment_lookdev/SCN_ARCADE/SCN_ARCADE_lookdev_A_entrance_wide_v002_game_screens.png`

Spatial constraint whitebox:

- `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/CAM_ARCADE_01_ENTRANCE_WIDE_constraint_whitebox_v001.png`

Long-take blocking board:

- `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_KEYFRAME_BOARD_v003.png`

Selected keyframe anchors:

- `LTK_ARCADE_OPEN_KF01`: `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF01_test_v001.png`
- `LTK_ARCADE_OPEN_KF02`: `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF02_test_v001.png`
- `LTK_ARCADE_OPEN_KF03`: `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF03_test_v002.png`
- `LTK_ARCADE_OPEN_KF04`: `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF04_test_v001.png`

Character references for any generation containing the brothers:

- `01_AIGC/character_design_v2/CHR_BRO_A_older_brother_turnaround_expression_v001_glasses.png`
- `01_AIGC/character_design_v2/CHR_BRO_B_protagonist_turnaround_expression_v001_distinct.png`
- `01_AIGC/character_design_v2/CHR_BRO_C_younger_brother_turnaround_expression_v001_chubby.png`
- Optional contact sheet: `01_AIGC/character_design_v2/THREE_BROTHERS_turnaround_expression_contact_sheet_v001.jpg`

Review contact sheet:

- `01_AIGC/long_take_design/test_generations/SCN_ARCADE_OPENING_15S_KEYFRAME_TEST_CONTACT_SHEET_v001.jpg`

## Reference Load Order

1. Load the environment mother as style/material/lighting reference.
2. Load the entrance whitebox as spatial reference.
3. Load the keyframe board as blocking/timing reference.
4. Load the selected test keyframe anchor for the requested time.
5. For KF03/KF04 or full-shot video, load the three active character references or the contact sheet.

## Locked Sequence Logic

The shot is one continuous child-height left-to-right pan/truck, not four separate edits.

- `0.0s`: empty wet factory-side street. No people. Entrance not yet visible.
- `5.0s`: entrance appears at frame right. Plastic strips remain still/mostly closed. No children.
- `10.0s`: the three brothers enter from the right edge. Empty left/center frame remains important. Use `KF03_test_v002`, not `KF03_test_v001`, as the active blocking anchor.
- `14.5s`: A Lei visibly lifts a plastic strip. The boys pass through as back/side/partial silhouettes. The arcade interior swallows them.

## Must Hold

- A Lei has old thin-frame glasses and a navy track jacket with red-white diagonal stripe.
- Xiao Chuan is skinny, anxious, in a blue-white school jacket, red scarf, and pale green backpack.
- Xiao Man is a small chubby boy in a warm padded vest and loose patched trousers.
- KF01 and KF02 contain no people.
- KF02 curtain state has no invisible cause; it must not look held open by unseen hands.
- KF04 must show a visible cause for curtain movement: A Lei lifting or pushing one strip.
- Arcade screens are fictional 1990s pixel-art color only.

## Reject Conditions

- Text-only reference paths were used without actual visible image references.
- Any real game title, logo, or recognizable copyrighted game character appears.
- Xiao Man becomes skinny, tall, or visually confused with Xiao Chuan.
- A Lei loses glasses in any readable view.
- The three boys become front-facing posed portraits instead of sneaking into the entrance.
- KF01/KF02 accidentally include children or extra adults.
- The long take loses left-to-right continuity or becomes a montage of unrelated angles.
