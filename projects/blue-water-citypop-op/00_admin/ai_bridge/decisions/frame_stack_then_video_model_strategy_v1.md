# Decision - Frame Stack Then Video Model Strategy v1

Status: accepted  
Updated: 2026-06-30 02:38 Asia/Shanghai

## Decision

For video-reference remake work, the first visible draft should usually be a local frame-stack roughcut, not an immediate AIGC video generation.

This follows traditional animation logic: key images can prove rhythm, composition, cut points, and broad action cheaply. Only units that fail because of motion smoothness should be sent to an AIGC video model. Units that fail because of camera/space continuity should be solved in Blender/previs first.

## Routing

### Image / Frame-Stack Roughcut Is Enough For First Pass

- title-safe holds,
- montage/hard-cut beats,
- simple still compositions,
- slow sky/cloud atmosphere,
- director timing review,
- early style replacement previews.

### AIGC Video Model Needed

- bird wingbeats or organic flight smoothness,
- hair/cloth/face movement,
- flare bloom/wipe transition,
- water/smoke/cloud evolution,
- short camera drift.

### Blender / Previs Needed Before Video Model

- true long one-take,
- camera traveling through space,
- vehicle/aircraft follow where scale/axis matters,
- multi-character continuous blocking,
- strong geography or screen-direction risk.

## Current Implementation

- Script: `scripts/build_frame_stack_roughcut.py`
- Current roughcut: `01_intake/analysis/video_reference_packages/reference-002-opening/roughcuts/reference-002-opening_frame_stack_2fps.mp4`
- Unit method table: `01_intake/analysis/video_reference_packages/reference-002-opening/unit_method_recommendations.md`

## Apply Rule

Before spending AIGC video generation budget, Codex should create or update the roughcut and ask:

1. Is the rhythm right?
2. Are the units correctly split?
3. Which exact units look bad only because motion is choppy?
4. Which exact units are spatially impossible without Blender/previs?

Only then generate video model tasks.
