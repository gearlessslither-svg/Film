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

## Final Versus Control Elements

Every AIGC prompt must explicitly separate:

- **Generate in final video:** visible story/world elements such as architecture, props, route lines meant as in-world decoration, lights, atmospheric effects, characters, vehicles, and final materials.
- **Use only as reference:** camera paths, colored guide lines, arrows, labels, proxy objects, debug overlays, tracking markers, blocking colors, rough gray materials, low-poly geometry, control rigs, and timing markers.
- **Do not generate:** any guide/control element that appears in the Blender video but should not be visible in the final render.

When a Blender reference contains a visually strong guide element, mention it twice: once in the positive instructions as `use only for ...`, and once in the negative prompt as `do not show ...`. This avoids the model copying guides as scene design.

Example:

```text
The red path line in the Blender reference is a control guide for camera direction and mechanism trigger order only. It is not a required final-picture element. Do not render it as a thick red line, glowing rail, floating trajectory, or camera path. If a red route motif is desired, show it only as a very subtle, thin, inlaid map engraving for the first few seconds.
```

## Reusable AIGC Prompt Template

```text
Use the uploaded start frame as the exact first-frame visual target.
Use the uploaded end frame as the exact final-frame visual target.
Use the uploaded Blender reference video only for camera path, spatial layout, object motion, construction timing, parallax, and one-take continuity.
Do not copy the Blender preview materials, plain lighting, or simplified geometry literally; reinterpret them in the style of the keyframes and style references.

Generate in the final video:
<list only the visible final-picture elements that should appear>

Use only as reference, do not visibly generate:
<list guide lines, arrows, colored markers, proxy objects, labels, camera paths, or debug overlays>

Create a <duration>s <aspect ratio> one-take cinematic video. No cuts. The camera begins at <start camera description>, travels through <motion path>, and settles on <final reveal>.

Motion beats:
0-<t1>s: <beat 1>
<t1>-<t2>s: <beat 2>
<t2>-<t3>s: <beat 3>
<t3>-<duration>s: <final settle>

Visual style:
<style, palette, material, lighting, texture, atmosphere>

Negative prompt:
No text, no logo, no watermark, no hard cut, no scene jump, no random camera shake, no melting geometry, no rubbery mechanics, no style drift, no extra characters unless specified, no visible control guides, no colored blocking markers, no camera-path lines, no debug arrows, no labels, no proxy geometry copied from the Blender reference.
```

## QA Questions

- Does the Blender reference clearly show what moves, when it moves, and where the camera goes?
- Are start/end frame roles separate from the Blender video role?
- Is the AIGC prompt explicit that the Blender video is a motion reference, not final style?
- Does the prompt list what should be generated in the final picture?
- Does the prompt list reference-only elements that must not appear in the final picture?
- Are strong guide elements repeated in the negative prompt so the model does not copy them?
- Does the final video request mention aspect ratio, duration, fps if needed, and one-take continuity?
