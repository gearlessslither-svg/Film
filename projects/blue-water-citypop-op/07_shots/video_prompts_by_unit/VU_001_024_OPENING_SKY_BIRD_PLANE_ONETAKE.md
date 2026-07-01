# VU_001_024_OPENING_SKY_BIRD_PLANE_ONETAKE

Status: candidate replacement pending user review  
Time range: 00:00-00:24  
Type: one-take Blender previs

## Source Of Truth

Use the Blender previs as camera and spatial truth:

- Blend: `06_previs/blender/opening_24s_onetake_previs.blend`
- Playblast: `06_previs/playblasts/opening_24s_onetake_previs.mp4`
- Keyframe contact sheet: `10_qa/reports/contact_sheet_OPENING_24S_ONETAKE_PREVIS_KEYFRAMES.jpg`
- Frame sequence: `06_previs/renders/opening_24s_onetake_animation_frames/opening_24s_0001.png` through `opening_24s_0576.png`

## AIGC Video Prompt

Create a single continuous 24-second live-action cinematic one-take in 21:9. No cuts, no title text, no logo, no subtitles, no animated screenshot look.

图1 / 00:00 / start: a clean saturated blue sky with soft white cloud banks and the white dove-like bird already gliding in the sky, wide anamorphic framing, calm opening breath, no aircraft visible yet.

图2 / 00:02 / white bird enters: a white dove-like bird glides into frame and becomes the camera's motive. The camera begins a smooth aerial follow, matching the bird's screen direction and height.

图3 / 00:06 / tracking midpoint: continue following the same white bird through the same blue sky and cloud field. Preserve cloud geography and screen direction from 图2. The bird should feel like the same physical subject, not a new generated bird.

图4 / 00:09 / aircraft reveal: without cutting, the camera's follow path brings a Jean-style handmade retro flying machine into view in the same sky space. The aircraft is wood-and-canvas, small, bright, and adventurous, revealed by camera motion rather than appearing as a separate insert.

图5 / 00:13 / bird and aircraft cross: maintain one continuous camera path while the white bird and retro flying machine share the frame. Their relative positions must make spatial sense: the bird remains the foreground/midground guide, the aircraft crosses mid-distance behind or beside it, both moving through the same cloud layer.

图6 / 00:18 / return to sky: the camera gradually lets the aircraft drift away and returns attention to the blue sky, white clouds, and the bird. This is not a hard transition; it is a motivated pan/track inside the same one-take.

图7 / 00:24 / end state: finish back on blue sky, soft clouds, and the white bird, leaving clean negative space for the next editorial beat.

Camera: continuous aerial follow camera starting on the white bird; wide anamorphic lens, subtle focal length change, stable horizon, soft daylight, same cloud geography throughout. Motion should feel like a real camera move planned from a Blender previs, not a slideshow morph.

Continuity constraints: keep the bird design, flight direction, sky color, cloud density, and relative scale consistent from 图1 through 图7. The aircraft must be introduced by camera movement and spatial blocking. No hard cuts, no teleporting objects, no sudden weather change, no character montage, no sun-flash transition inside this 24-second unit.

Adversarial checks: if 图4 works as an isolated airplane shot without 图2/图3, the prompt failed. If the ending does not return to the bird and blue sky, the unit failed. If the AIGC system adds text or logos, reject the result.
