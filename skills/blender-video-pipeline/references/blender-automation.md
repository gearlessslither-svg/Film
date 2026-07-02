# Blender Automation Patterns

Use this reference when writing Blender Python for video scenes.

## Script Structure

Use a single reproducible scene script:

1. Define absolute project paths.
2. Clear the scene.
3. Set render engine, resolution, fps, frame range, and output frame path.
4. Create materials.
5. Create geometry with named objects and collections.
6. Create animation controls and keyframes.
7. Create camera, target, lens animation, and constraints.
8. Save the `.blend`.
9. Render frames only after the scene is saved.

## Modeling For Motion References

Motion-reference geometry should be readable:

- Use strong silhouettes and separated layers.
- Add enough bevels and normals for light to reveal shape.
- Use color/material grouping to clarify moving systems.
- Keep scale relationships consistent across the shot.
- Prefer named control empties for buildings, mechanisms, doors, rings, platforms, and linked assemblies.

## One-Take Camera Control

For one-shot movement:

- Create a `camera_look_target` empty.
- Add a `TRACK_TO` constraint on the camera.
- Keyframe camera location, target location, lens, and sometimes depth of field.
- Use 4-6 camera beats for a 10s shot rather than dozens of micro keys.
- Check start, midpoint, and end frames before full render.

Example timing for 10s at 24fps:

- `1-72`: establish map/table/scene surface.
- `73-144`: construction or transformation begins around the camera.
- `145-204`: camera moves through the built space with parallax.
- `205-240`: final reveal and settle.

## Rendering

Prefer frame sequences:

```python
scene.render.filepath = "/project/renders/frames/frame_"
scene.render.image_settings.file_format = "PNG"
scene.frame_start = 1
scene.frame_end = 240
scene.render.fps = 24
```

For quick previews, temporarily lower resolution, frame range, samples, or render every nth frame. For final AIGC references, keep the same camera and timing as the intended upload.

## QA Before Full Render

Render at least three frames:

- First frame: validates aspect ratio, foreground, and initial state.
- Midpoint: validates transformation clarity and camera path.
- Final frame: validates reveal, target framing, and no clipping.

If any sample frame is wrong, fix the Blender script before full animation.
