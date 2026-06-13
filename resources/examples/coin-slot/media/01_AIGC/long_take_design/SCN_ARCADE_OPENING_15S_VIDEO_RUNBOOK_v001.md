# SCN_ARCADE Opening 15s Video Runbook v001

Shot ID: `LTK_ARCADE_OPEN_001`

Use this runbook when sending the SCN_ARCADE opening long take to a video model. It is an execution checklist, not a new creative direction.

## Required Files

Reference lock:

- `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_REFERENCE_LOCK_v001.md`

Formal prompt:

- `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_FORMAL_VIDEO_PROMPT_v002.csv`

Visual anchors:

- First frame: `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF01_test_v001.png`
- Mid frame 1: `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF02_test_v001.png`
- Mid frame 2: `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF03_test_v002.png`
- End frame: `01_AIGC/long_take_design/test_generations/LTK_ARCADE_OPEN_KF04_test_v001.png`

Character references:

- `01_AIGC/character_design_v2/CHR_BRO_A_older_brother_turnaround_expression_v001_glasses.png`
- `01_AIGC/character_design_v2/CHR_BRO_B_protagonist_turnaround_expression_v001_distinct.png`
- `01_AIGC/character_design_v2/CHR_BRO_C_younger_brother_turnaround_expression_v001_chubby.png`

Environment references:

- `01_AIGC/environment_lookdev/SCN_ARCADE/SCN_ARCADE_lookdev_A_entrance_wide_v002_game_screens.png`
- `01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/CAM_ARCADE_01_ENTRANCE_WIDE_constraint_whitebox_v001.png`
- `01_AIGC/long_take_design/SCN_ARCADE_OPENING_15S_KEYFRAME_BOARD_v003.png`

## Preferred Setup

Use a model or workflow that accepts multiple visual references or keyframes.

Load in this order:

1. Environment mother.
2. Entrance whitebox.
3. Keyframe board.
4. KF01, KF02, KF03_v002, KF04 in time order.
5. Three character references.
6. Formal video prompt and negative prompt from `SCN_ARCADE_OPENING_15S_FORMAL_VIDEO_PROMPT_v002.csv`.

Target duration: `15s`.

Target aspect: `16:9`.

Motion: slow child-height left-to-right pan/truck. No cuts.

## If The Tool Supports Multi-Keyframe Video

Use these timing anchors:

- `0.0s`: KF01, empty street.
- `5.0s`: KF02, entrance reveal.
- `10.0s`: KF03_v002, brothers enter from the right edge.
- `14.5s`: KF04, curtain wipe into arcade.

This is the best route for spatial consistency.

## If The Tool Supports Only First/Last Frame

Use:

- First frame: KF01.
- Last frame: KF04.

Put KF02 and KF03_v002 as visual references if the tool allows extra references. If it does not, keep their content in the motion prompt:

- entrance revealed around `5.0s`;
- brothers enter from frame right around `10.0s`;
- A Lei visibly causes the curtain movement around `11.5s`.

## If The Tool Supports Only Image-To-Video From One Frame

Use KF01 only for the first attempt.

Expected weakness: the model may invent the entrance and boys incorrectly. Treat this output as motion exploration only, not a continuity-approved take.

If using one-frame image-to-video, a safer two-pass approach is:

1. Generate `0.0s-7.5s` from KF01 to KF02.
2. Generate `7.5s-15.0s` from KF03_v002 to KF04.
3. Stitch only after visual QA.

## QA Checklist

Accept only if all are true:

- The shot remains one continuous left-to-right movement.
- KF01 has no people and no visible entrance.
- KF02 reveals the entrance at frame right and has no children.
- KF02 curtain is not mysteriously open.
- KF03 keeps empty left/center wall and places the brothers near the right-side entrance.
- A Lei keeps glasses in readable views.
- Xiao Chuan keeps backpack, red scarf, and skinny body shape.
- Xiao Man remains small and chubby, not a duplicate of Xiao Chuan.
- KF04 shows A Lei visibly lifting or pushing the plastic curtain.
- Arcade screens stay fictional and unreadable.

Reject if any are true:

- It cuts to a new angle or montage.
- The boys become front-facing posed portraits.
- The video adds extra adults, crowds, or readable game-room signage.
- Any real arcade game title, logo, or recognizable character appears.
- The entrance, plastic curtain, or cabinet layout becomes a modern arcade.
- The curtain changes state before a visible cause.

## Recommended First Test

Run a low-cost preview using all four keyframes if possible.

Do not judge the final look first. Judge in this order:

1. Continuity of camera movement.
2. Entrance and curtain causality.
3. Three-brother height/costume readability.
4. SCN_ARCADE environment consistency.
5. Final image polish.

Only promote a take after the first four checks pass.
