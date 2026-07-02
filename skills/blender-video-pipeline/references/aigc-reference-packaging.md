# AIGC Reference Packaging

Use this reference when Blender output will guide an AIGC video model.

## Package Layout

Use a compact package:

```text
project-slug/
  inputs/
    start_frame.png
    end_frame.png
    style_reference.png
  blender/
    scene.blend
    create_scene.py
  renders/
    frames/
    contact_sheet.png
  outputs/
    motion_reference.mp4
  docs/
    aigc_video_prompt.md
    render_notes.md
```

## Prompt Contract

The prompt must tell the video model how to use each input:

- Start frame: first-frame composition, palette, materials, and world design.
- End frame: final reveal, composition, scale, and destination.
- Blender video: camera movement, object motion, construction order, spatial continuity, timing, and parallax.
- Text prompt: final art direction and constraints.

Do not let the model confuse the Blender pass for final style when the Blender pass is only previs.

## Reusable AIGC Prompt Template

```text
Use the uploaded start frame as the exact first-frame visual target.
Use the uploaded end frame as the exact final-frame visual target.
Use the uploaded Blender reference video only for camera path, spatial layout, object motion, construction timing, parallax, and one-take continuity.
Do not copy the Blender preview materials, plain lighting, or simplified geometry literally; reinterpret them in the style of the keyframes and style references.

Create a <duration>s <aspect ratio> one-take cinematic video. No cuts. The camera begins at <start camera description>, travels through <motion path>, and settles on <final reveal>.

Motion beats:
0-<t1>s: <beat 1>
<t1>-<t2>s: <beat 2>
<t2>-<t3>s: <beat 3>
<t3>-<duration>s: <final settle>

Visual style:
<style, palette, material, lighting, texture, atmosphere>

Negative prompt:
No text, no logo, no watermark, no hard cut, no scene jump, no random camera shake, no melting geometry, no rubbery mechanics, no style drift, no extra characters unless specified.
```

## QA Questions

- Does the Blender reference clearly show what moves, when it moves, and where the camera goes?
- Are start/end frame roles separate from the Blender video role?
- Is the AIGC prompt explicit that the Blender video is a motion reference, not final style?
- Does the final video request mention aspect ratio, duration, fps if needed, and one-take continuity?
