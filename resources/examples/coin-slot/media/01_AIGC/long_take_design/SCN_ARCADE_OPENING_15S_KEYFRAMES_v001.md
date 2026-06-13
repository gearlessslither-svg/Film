# SCN_ARCADE Opening 15s Long Take Keyframes v001

Parent shot: `LTK_ARCADE_OPEN_001`

Purpose: split the 15s opening long take into generation anchors. These are not separate edits; they are spatial and emotional keyframes for one continuous left-to-right shot.

Required character references for any keyframe containing the brothers:

- `character_design_v2/CHR_BRO_A_older_brother_turnaround_expression_v001_glasses.png`
- `character_design_v2/CHR_BRO_B_protagonist_turnaround_expression_v001_distinct.png`
- `character_design_v2/CHR_BRO_C_younger_brother_turnaround_expression_v001_chubby.png`

Environment references:

- Mother style: `environment_lookdev/SCN_ARCADE/SCN_ARCADE_lookdev_A_entrance_wide_v002_game_screens.png`
- Interior whitebox: `environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/CAM_ARCADE_01_ENTRANCE_WIDE_constraint_whitebox_v001.png`

## Keyframe List

| Keyframe ID | Time | Purpose | Frame Content | Character References |
|---|---:|---|---|---|
| `LTK_ARCADE_OPEN_KF01` | 0.0s | Opening empty environment anchor | Wet broken factory-side street, peeling wall, exposed pipes, sagging wires, faint CRT glow in puddle. No characters. | none |
| `LTK_ARCADE_OPEN_KF02` | 5.0s | Hidden entrance reveal | Dirty plastic strips and dim yellow bulb appear at frame right. Interior arcade glow visible through doorway; still no boys. | none |
| `LTK_ARCADE_OPEN_KF03` | 10.0s | Brothers enter the shot | A Lei leads from right, Xiao Chuan follows with backpack straps, Xiao Man is now a small chubby boy behind them clutching his vest. All three cautious and secretive. | all three |
| `LTK_ARCADE_OPEN_KF04` | 14.5s | Curtain-wipe threshold | A Lei pushes/lifts plastic strip; boys pass through and become partial silhouettes against CRT glow. Curtain partly wipes lens. | all three |

## Continuity Rules

- The camera movement is one continuous child-height left-to-right truck/pan.
- The boys do not run; they slip in carefully.
- A Lei must wear old thin-frame glasses.
- Xiao Chuan must stay skinny, anxious, backpack-centered.
- Xiao Man must read as small, chubby, round, slow, and inward.
- The arcade screen imagery remains fictional and non-infringing.
- No readable signage or game titles.

## Video Assembly Logic

Use `KF01` and `KF04` as the hard start/end visual anchors. Use `KF02` and `KF03` as mid-motion guidance. If the video model supports first/end frame only, use `KF01` as first frame and `KF04` as end frame, then include the `KF02/KF03` descriptions in the motion prompt. If it supports multi-keyframe conditioning, provide all four in time order.
