# Blocking Readability Upgrade Plan

Project: 投币口
Generated at: 2026-06-13T16:32:49+08:00
Status: autofill recommendation asset

## Goal

Raise whitebox/previs usefulness from rough spatial reminder to image-generation control source. The next Blender pass should make scale, eyeline, occlusion, camera height, and foreground/midground/background readable at thumbnail size.

## Required Checks

| Check | Acceptance Criteria |
| --- | --- |
| Scale | child/adult height relation is clear in every shared frame |
| Screen direction | exits, threats, and movement preserve left/right continuity |
| Camera height | low, child-height, eye-level, and high-angle shots are explicitly labeled |
| Lens logic | wide, normal, and compressed views are not mixed accidentally |
| Occlusion | doorframes, cabinets, bodies, and foreground objects support story pressure |
| Depth | each key shot has clear foreground, midground, and background planes |
| Action readability | preparation, action, result, and reaction frames are separated |

## Current Location Coverage

- SCN_ALLEY: 3 shots
- SCN_ARCADE: 3 shots
- SCN_ARCADE_EXIT: 1 shots
- SCN_COMPOUND: 5 shots

## Next Blender Tasks

- Add simple human-scale stand-ins with distinct silhouettes for each character group.
- Add camera markers named by `shot_id`.
- Export one clean whitebox render and one annotated review render per key shot.
- Export depth, line, normal, or segmentation layers only after camera and blocking are approved.
- Add a QA contact sheet before using the renders in image generation.
