# Brutal Ink Opening One-Take 10s Blender Brief

Project: `dragon-house-black-green-ink-wash-title-21x9`
Purpose: optional new Blender/2.5D motion reference for the 10-second opening.
Status: not rendered yet.

## Why A New Blender Video Is Needed

The old proxy MP4 came from a different branch and is visually incompatible with the current director lock. It may introduce old style language if used as a strong reference. For this branch, Blender should be redone only after the new start and end frames are generated in the brutal ink style.

## Required Inputs

Generate and place:

- `inputs/start_frame.png`
- `inputs/end_frame.png`

Both must follow:

- `04_lookdev/style_system/brutal_ink_omen_style_lock.md`
- `04_lookdev/style_references/brutal_ink_omen_v1/director_reference_only_style.png`

## Motion Reference Design

Duration: 10 seconds
FPS: 24
Aspect: 21:9
Deliverable: MP4 AIGC motion/control reference, not final art.

Build as a flat layered 2.5D paper scene:

- old paper plane in background
- black dragon brush stroke as 3-5 semi-transparent layered ink ribbons
- small isolated crown/throne subject as a stable low-center silhouette
- sparse mineral green stain layer on the right
- sparse cinnabar mark layers with no readable text
- camera slow push-in and slight drift, not a dramatic 3D flythrough

Timing:

- frames 1-48: paper breathes; first dragon head stroke appears
- frames 49-96: dragon body sweeps across the upper frame
- frames 97-156: green stain bleeds and camera pushes inward
- frames 157-204: dragon closes into circular omen
- frames 205-240: settle on final composition

## AIGC Usage Rule

If this Blender reference is produced, prompts must say:

- Use Blender only for camera timing, parallax, and the dragon-stroke expansion path.
- Final look comes only from the regenerated brutal-ink start/end frames and director reference.
- Do not copy Blender preview materials, guide layers, labels, or proxy geometry.
