# Film And AIGC Aesthetic Audit Rubric

Use this reference when turning a project scan into creative, cinematic, and production recommendations. The audit should feel like a practical review from a film director, cinematographer, production designer, editor, sound designer, and AIGC pipeline supervisor sitting at the same table.

## Audit Posture

- Judge evidence, not intention. If a project claims a style but has no styleframes, palette, lighting rules, or references, mark the style as unproven.
- Separate taste from function. A shot can be beautiful but fail story, blocking, continuity, or AIGC controllability.
- Prefer production fixes over abstract comments. "Make it more cinematic" is not actionable; "lock camera height, foreground occluder, motivated side light, and screen direction for shots 004-008" is actionable.
- Avoid direct imitation of living artists. Extract transferable technique: contrast, pacing, staging, lensing, production design logic, not personal style mimicry.

## Readiness Ladder

Score each major area from 0 to 5:

- 0: Missing. No usable evidence.
- 1: Fragmentary. A few references or placeholders, no production contract.
- 2: Draft. Direction exists but is too vague for batch generation.
- 3: Usable. Enough for a controlled small batch.
- 4: Strong. Clear constraints, assets, and QA loop.
- 5: Industrial. Repeatable, versioned, sample-validated, and ready for scale.

Batch image/video generation should not start at scale unless story, lookdev, asset bible, previs, and shot plan are at least 3.

## Story And Dramaturgy

Check:

- Premise: Can the core idea be stated in one vivid sentence?
- Want/pressure: What does the subject want, what opposes it, and why now?
- Progression: Does the sequence move through setup, escalation, reversal, payoff, and aftermath?
- Visual causality: Does each image cause the next image, or are they just mood boards?
- Audience memory: What image, sound, action, or object should remain in the audience's mind?
- Duration fit: Does the story scale match the target runtime?

Common gaps:

- A concept exists but no story engine: request an outline and beat sheet before lookdev.
- A mood exists but no conflict or transformation: request 3 alternate story routes.
- Too many ideas for the runtime: request a single dramatic spine and cut secondary concepts.

## Cinematography

Check:

- Shot size: wide, medium, close, insert, POV, overhead, low angle, profile, silhouette.
- Lens logic: wide for space and distortion, normal for observation, telephoto for compression/isolation.
- Camera height: eye level, low, high, object-level, ground-level, shoulder-level.
- Movement: motivated push, pull, pan, tilt, track, handheld, locked-off, crane, orbit.
- Screen direction: consistent left/right geography unless deliberately broken.
- Depth: foreground, midground, background, occlusion, parallax, focus planes.
- Composition: subject hierarchy, leading lines, negative space, frame-within-frame, balance, tension.

Common gaps:

- All shots feel like generic eye-level stills: require camera plan by story beat.
- Image prompts mention "cinematic" but no lens/blocking: add lens, height, distance, foreground, motion.
- Whitebox has no camera manifest: require camera position, focal length, target, height, movement.

## Lighting

Check:

- Motivation: window, lamp, screen, streetlight, fire, industrial light, practical source, moon, sun.
- Direction: front, side, back, top, underlight, rim, silhouette.
- Quality: hard, soft, bounced, diffused, specular, volumetric, low-key, high-key.
- Contrast: exposure ratio, separation, shadow detail, highlight control.
- Time and weather: dawn, noon, dusk, night, rain, fog, dust, interior spill.
- Emotional logic: reveal, conceal, threat, tenderness, alienation, ritual, spectacle.

Common gaps:

- Lighting is only an adjective: request a lighting bible with source, direction, ratio, and color temperature.
- Styleframes disagree on light direction: request a continuity rule per scene.
- Character disappears into background: add rim, value contrast, silhouette separation, or costume adjustment.

## Color And Material

Check:

- Palette: dominant, accent, neutral, forbidden colors.
- Color script: how color changes across story stages.
- Value structure: readable dark/mid/light distribution.
- Temperature contrast: warm/cool motivation and emotional meaning.
- Material response: skin, metal, fabric, glass, plastic, dust, wet surfaces, emissive screens.
- Brand/object memory: whether a prop or environment color becomes a recall anchor.

Common gaps:

- One-note palette: add contrast rules and accent color placement.
- Reference images conflict: choose a primary palette and list forbidden variants.
- AIGC outputs drift: add palette swatches and material descriptors to prompts.

## Production Design

Check:

- World rules: era, technology level, social texture, scale, wear, cleanliness, signage.
- Location grammar: where entrances, exits, hazards, props, and light sources live.
- Props: hero prop state, continuity, damage, movement, and symbolic role.
- Texture: surface age, dirt, scratches, fingerprints, fabric, packaging, labels.
- Graphic design: typography, UI, signage, labels, symbols, readable screen content.

Common gaps:

- Scene is attractive but generic: request location bible and prop function map.
- Hero object lacks state changes: define prop states per story beat.
- Backgrounds drift across shots: lock a spatial map and recurring landmarks.

## Character And Performance

Check:

- Silhouette: readable at thumbnail size.
- Face/hair/body: consistent identity markers.
- Wardrobe: color, cut, material, dirt/damage, stage changes.
- Gesture: posture, tension, center of gravity, hand action, gaze direction.
- Expression: emotional progression, not random variations.
- Relationship to space: distance, power, vulnerability, obstruction, reveal.

Common gaps:

- One character sheet for all stages: require stage-specific character sheets.
- Characters look similar: increase silhouette, palette, wardrobe, age, posture, or props.
- Prompts describe emotion but not performance: add body mechanics and eye-line.

## Previs, Whitebox, And Spatial Control

Check:

- Scale: character height, door/table/object proportions, distance.
- Blocking: start/end positions, action path, occlusion, foreground objects.
- Camera: position, height, focal length, target, movement, frame boundaries.
- Control layers: depth, line, normal, segmentation, masks where useful.
- QA: repeated composition checks, whitebox-to-output similarity, panel-level notes.

Common gaps:

- Whitebox is too crude: refine geometry for silhouettes, major props, camera landmarks, and occluders.
- Space changes between shots: add floor plan and screen-direction map.
- Image model ignores composition: add control layers and stricter prompt contracts.

## Shot And Prompt Readiness

Each shot should have:

- `shot_id` and story beat.
- Shot purpose.
- Camera and lens.
- Blocking and action.
- Lighting and color rule.
- Continuity lock.
- Keyframe path.
- Image prompt path.
- Video prompt path when motion matters.
- Negative constraints.
- QA status.

Common gaps:

- Shot list has rows but no prompt paths: not ready for batch generation.
- Prompts are prose-heavy but spatially weak: add whitebox, camera, blocking, and continuity fields.
- No reject log: failures will repeat; create reject reasons and prompt fixes.

## Editing Rhythm

Check:

- Beat granularity: preparation, action, result, reaction, transition.
- Shot duration: whether image complexity matches screen time.
- Rhythm: acceleration, pause, reveal, impact, recovery.
- Match logic: eyeline, action match, graphic match, sound bridge, contrast cut.
- Information order: what the audience knows before the character, and vice versa.

Common gaps:

- Too few panels for complex action: split into micro-storyboard frames.
- Every shot has similar duration: create rhythm map.
- No animatic: build a simple timing pass before expensive generation.

## Sound And Music

Check:

- Voice: dialogue, narration, system voice, offscreen voice, silence.
- Ambience: room tone, exterior bed, crowd, machinery, wind, neon, rain.
- Foley: footsteps, fabric, object handling, coin, switch, door, breath.
- Designed sound: symbolic, subjective, psychological, mechanical, supernatural.
- Music: theme, pulse, texture, entry/exit points, restraint.
- Perspective: close, distant, muffled, behind wall, subjective, diegetic/non-diegetic.

Common gaps:

- Sound starts after picture lock: request audio cue sheet during storyboard.
- Music is generic mood: define rhythm, instrumentation, silence, and story function.
- No sound-source visibility rules: decide when sound is seen, implied, or hidden.

## AIGC Stability

Check:

- Local/remote model fallback policy exists.
- Style and character references are stage-specific.
- Prompts separate subject, space, camera, light, action, style, negative constraints.
- Pure images and annotated review images are separated.
- Whitebox/control layers are linked to shot IDs.
- QA scripts or manual QA forms exist.
- Failed outputs have reasons and next prompt changes.

Common gaps:

- Strong idea, weak constraints: generate a small locked batch, not a full run.
- Good stills, bad video: add motion prompts, start/end frames, camera motion, action timing.
- Character drift: use stage locks, reference sheets, consistent clothing/material markers.

## Priority Logic

P0 before batch generation:

- Missing story direction or director approval.
- Missing asset bible for characters/locations/props.
- Missing whitebox/camera/control layer for spatially complex shots.
- Missing shot list or prompt paths.
- No model fallback or generation job tracking.

P1 before serious production:

- Weak lookdev, palette, lighting, or material rules.
- No reject log.
- No sound cue plan.
- No animatic or rough timing.
- No continuity checklist.

P2 polish:

- More refined contact sheets.
- Alternate styleframes.
- Better delivery manifests.
- More granular subtitles, audio stems, or color variants.
