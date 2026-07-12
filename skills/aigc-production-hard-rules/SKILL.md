---
name: aigc-production-hard-rules
description: >-
  Mandatory cross-project production gate for AIGC film text, storyboards, image
  prompts, image generation, video prompts, and video generation. Use whenever
  Codex creates or revises shot cards, visual prompts, generated keyframes,
  image-to-video prompts, video packages, or production-ready film descriptions.
  Dynamically derives style and duration from the current project and approved
  references while requiring professional composition, camera, lighting,
  performance, narrative-time character state, continuity, negative constraints,
  and QA. These rules are global
  and must be followed across projects unless the user explicitly overrides one.
---

# AIGC Production Hard Rules

Apply this skill as the mandatory parent gate for AIGC film production. The constraints are global; the creative answer is project-specific.

## Global Versus Dynamic

Always enforce the workflow and quality fields below. Never hard-code one project's aesthetic, camera language, duration, character design, or negative style list into another project.

Before producing anything:

1. Read the smallest sufficient current project sources: approved story/dialogue, handoff, project/style bible, character/location/prop/continuity locks, active storyboard, and approved references.
2. Read active global hard rules from `$aigc-film-project-memory` when the task can be shaped by them.
3. Resolve conflicts in favor of current director feedback, then the current project's approved visual evidence.
4. Build a project-specific style fingerprint and continuity set from actual sources.
5. Do not import an earlier project's style vocabulary merely because it worked before.

## Director Override And Active Branch Gate

Treat the newest explicit director instruction as a branch-changing event, not a small prompt note, whenever it adds/removes a character, changes a story outcome, replaces a prop concept, changes a transformation state, or invalidates a sequence already generated.

1. Stop the affected batch immediately. Finish no downstream keyframe, package, callback, or video prompt that depends on the superseded branch.
2. Record the override in the project loop with `director_override` plus a narrower label such as `story_branch_superseded`, `character_removed`, `prop_concept_replaced`, or `ending_replaced`.
3. Update the authoritative script/outline, active branch marker, character/prop state ledger, Board rows, prompt package, and handoff before resuming production. If the user only requests exploration, keep it outside the active Board until approved.
4. Preserve old assets as historical evidence, but move them out of the active reference chain and current delivery. Never use a visually attractive superseded image as a reference merely because it is recent.
5. Before packaging or returning, prove that every included asset and prompt belongs to the same active narrative branch. A package mixing current and superseded branches fails.

## Storyboard And Production Text Gate

Do not return a concept sentence as a production storyboard. Every shot card must include:

- dramatic beat and intended audience perception;
- duration analysis when the shot will become video;
- shot size and composition;
- camera height, side, axis, angle, lens/perceptual focal length, distance, movement, and final settle;
- character performance, blocking, eye line, hands, body weight, expression, and prop interaction;
- key/fill/rim/practical lighting, color, shadow, focus/exposure, and any change;
- foreground/midground/background, spatial logic, parallax, occlusion, and screen direction;
- character, costume, prop, location, style, and transition continuity;
- source-specific negative constraints and project audio rule;
- a detailed image prompt and, when applicable, a detailed video prompt.

If the story or dialogue is not approved for a story-driven project, obey the global story/dialogue gate and stop before production assets.

## Narrative Timeline And Character State Gate

For any story with time jumps, transformations, flashbacks, memories, reflections, alternate selves, or before/after character designs, dynamically derive a project-specific character-state ledger before prompting or generation. This gate defines the method, never a universal hairstyle, costume, or transformation. Never infer a character's current design from the most recently generated image or from another project.

1. Define stable `timeline_phase` and `character_state_id` values at every narrative boundary. Each state must specify observable locks: age/face identity, exact hair length and silhouette, facial hair, body condition, costume layers/colors, carried and forbidden props, injuries/marks, emotional baseline, location eligibility, and the event that permits transition to another state.
2. Determine the correct state from the current project's approved script, director feedback, continuity evidence, and chronological position. If these sources clearly resolve the state, analyze and bind it without asking. If the boundary or design is genuinely ambiguous and different choices would materially change the image, ask the director before generation; never silently guess.
3. Bind every shot, keyframe, image version, and video prompt to one explicit `timeline_phase` plus the applicable character state IDs. A flashback, reflection, dream double, future image, or memory inside the frame must receive its own layered state ID rather than overwrite the foreground character state.
4. Put these fields before subject/action in every production prompt:

```text
[NARRATIVE_TIME] <phase, position relative to the transformation boundary, foreground/recollection/reflection layer>
[CHARACTER_STATE_LOCK] <character -> state_id -> observable hair/face/costume/body/prop locks>
[STATE_TRANSITION_RULE] <no transition in this shot, or the exact time/event/visual mechanism that authorizes it>
```

5. Filter references by state. A reference from another phase may be used only for its declared role, such as face identity or camera blocking; explicitly forbid transfer of its hair, costume, body condition, props, lighting, or environment. Do not mix pre- and post-transformation references without role labels.
6. Treat descriptive words such as `long hair` or `short hair` as insufficient when silhouette matters. State an observable boundary, for example `loose black hair reaches jaw-to-shoulder and visibly overlaps the collar` or `neat cropped hair clears both ears and never touches the collar`.
7. Allow a state change only in the declared transition shot and at the declared timeline beat. All preceding frames keep the earlier state; all subsequent frames use the new state unless the story explicitly enters another temporal layer.
8. QA images by state, not only one by one. Build chronological contact sheets and compare the same character across adjacent shots and both sides of every transition boundary. Label and reject `narrative_state_mismatch`, `premature_state_transition`, `reference_state_leak`, or `layer_state_collision`.
9. Packaging and return must fail when a card/version lacks state IDs, uses a prompt from a different state, or lets a version-level legacy prompt override a corrected card-level state. Preserve the old version as evidence, but do not export it as production-ready.

## Image Prompt And Image Generation Gate

Apply `$image-quality-guard` before every image generation task, not only after the user reports noise. Its generation gate is mandatory: require large readable shapes, controlled detail density, clean silhouette edges, smooth flat areas, low noise, and detail concentrated on the subject and one or two hero materials. Explicitly forbid random speckle, muddy micro-texture, over-sharpened halos, fake pixel-level detail, JPEG artifacts, noisy backgrounds, and full-frame micro-ornament.

Before writing or using an image prompt, dynamically analyze the current project and references. Put the following in the prompt:

1. `[STYLE_FINGERPRINT]`: actual medium, edges/linework, texture/material vocabulary, palette, contrast, lighting logic, character proportions, environment geometry, depth treatment, and density.
2. `[SUBJECT_AND_ACTION]`: exact identity, stage, pose, body weight, hands, eye line, expression, costume, prop interaction, and moment before/after.
3. `[CAMERA_AND_COMPOSITION]`: aspect ratio, shot size, camera height/side/angle/axis, lens feel, distance, framing, foreground/midground/background, negative space, focus, and depth.
4. `[LIGHTING]`: motivated sources, key/fill/rim/practical directions, hardness, color, exposure hierarchy, shadow and reflection behavior.
5. `[SPACE_AND_CONTINUITY]`: project location geometry, screen direction, character/prop placement, linked shots, and immutable locks.
6. `[NEGATIVE]`: source-specific failure prevention, including style migrations absent from the project; anatomy, identity, text/logo, clutter, mutation, and continuity failures as applicable.

Use approved character, location, prop, whitebox, and prior-frame references according to their roles. A motion/blocking reference must not override the approved art style. Generate no image until the prompt is detailed enough to be independently staged by a cinematographer and art department.

After generation, inspect composition, identity, anatomy, style, lighting, spatial continuity, text artifacts, and dimensions. Preserve failed and alternate attempts as versions; do not silently promote a candidate.

Run the `$image-quality-guard` QA gate immediately after each generated image, before generating the next image or using the output as a reference. Inspect normal view and 100% detail and run `qa_ai_image.py` for project files. If it warns or fails, decide immediately: regenerate semantic/style/composition failures; use conservative local cleanup only for surface noise on an otherwise correct frame. Never chain a failed or unreviewed image into the next generation. Stop a batch when one image has unresolved `noisy_microdetail`, `dirty_frame`, `style_drift`, or `identity_redraw`.

## Prop Plausibility And Damage Gate

Treat recurring or story-critical props as designed objects, not decoration. Before generation, bind each prop to a stable `prop_state_id` with:

- function and base geometry;
- material and construction;
- required parts and forbidden missing parts;
- age/wear level;
- exact approved damage, repair, residue, or transformation evidence;
- the story event that permits a state change.

Use ordinary wear before symbolic damage. Do not add cracks, missing strings, staples, brass plates, patches, scorch marks, blood, glowing seams, or other visual metaphors unless the script/director explicitly requires each one. A prop may be old without being broken and repaired.

QA props for structural plausibility and narrative necessity in addition to image cleanliness. Count repeated parts when count matters, inspect contact points and load-bearing geometry, and compare adjacent shots. Label implausible or over-symbolized results `prop_design_fake`, `unlocked_prop`, `prop_state_mismatch`, or `symbolism_overload`; regenerate them rather than denoise them.

## Exact Text, Logo, And Title-Sequence Gate

Do not treat attractive pseudo-text as acceptable production typography.

1. Store every required title, logo wordmark, subtitle, sign, and dialogue graphic as verbatim text and define language/script, glyph count, reading order, layout, and allowed variants.
2. Use image generation for the visual plate, emblem, material, lighting, and environment. For exact Chinese or other high-risk typography, prefer deterministic font/vector/raster compositing for the final glyphs unless the generated text passes character-by-character review.
3. Validate exact text visually and, when possible, with deterministic source text. Reject any wrong, missing, extra, malformed, pseudo, or reordered glyph; keep it as `typography_invalid` evidence.
4. A title/logo requested to “appear” is a shot, not a single finished still. Design the appearance mechanism, duration, camera/material/light movement, ordered keyframes, transitions, final hold, and numbered storyboard sheet under the multi-keyframe gate.
5. Keep a clean no-text plate and a separable exact wordmark when practical so the title sequence can be revised without regenerating the art direction.

## Multi-Keyframe Single-Shot Gate

When two or more generated images are keyframes of one continuous shot, treat them as one shot, not as separate storyboard shots. This is a hard rule:

1. Finish and QA every keyframe first. Lock one `shot_id`, then assign gap-free display order `01`, `02`, `03`... from the actual dramatic and temporal sequence. Do not use filenames or generation time as story order.
2. After all keyframes exist, create one additional storyboard-sheet image from the approved keyframe files. Composite the originals without regenerating or restyling them. Place panels in reading order, print a clear deterministic sequence number on every panel, and preserve each source image's aspect ratio, crop, color, and identity. A sheet with missing, duplicate, or ambiguous numbers fails.
3. Save the sheet as a separate project asset and keep every individual keyframe. The sheet is for sequence review and packaging; it does not replace source frames and must not be promoted as a keyframe automatically.
4. Rewrite the storyboard/video prompt as one shot with multiple numbered keyframes. Use this structure:

```text
[SHOT_ID] <one shared shot id>
[SHOT_INTENT] <one continuous dramatic action and camera idea>
[KEYFRAME_SEQUENCE]
01 | <time or phase> | <source path/id> | <pose, framing, camera, light, space, continuity state>
02 | <time or phase> | <source path/id> | <what changes from 01; what stays locked>
...
[TRANSITIONS]
01 -> 02 | <continuous performance, camera, focus, lighting, material and environment interpolation; no cut unless explicitly designed>
...
[STORYBOARD_SHEET] <sheet path>
```

5. The numbered keyframes must map into one gap-free `[TIMELINE]` in the video prompt. Each keyframe is an anchor state within that shot, not permission to invent a cut, change axis, redraw identity, replace the art style, or reset the environment.
6. Before packaging, verify: one shared shot id; ordered unique numbers; all source paths exist; sheet panel count equals keyframe count; labels match prompt order; the timeline references every keyframe in order; and no keyframe is silently omitted.

## Video Prompt And Video Generation Gate

Apply `$aigc-video-style-lock` in full.

Mandatory sequence:

1. Analyze the approved source image and current project to write a dynamic style fingerprint.
2. Put the positive style-inheritance lock and explicit `strictly do not change or replace the source image art style` negative before motion.
3. Analyze the shot to choose an appropriate duration. Never default every image to 5 seconds.
4. State `[DURATION_RATIONALE]` and split overloaded shots rather than forcing unstable complexity.
5. Cover 0.0s to the exact endpoint with an ordered, gap-free, professionally time-coded timeline. Allocate time by dramatic weight, not equal division by habit.
6. For every time beat, specify performance/blocking/eye line; camera height/side/axis/lens/distance/movement; shot-size/composition/focus/exposure; lighting/shadows; environment/material/secondary motion; continuity locks; and held values.
7. End on an explicit usable final-frame state with motion deceleration or a deliberate hold.
8. State ambience/SFX only and no music/BGM/soundtrack unless the user explicitly overrides the global audio rule.

QA the first, middle, and final frames against the approved input. Reject unresolved style drift, identity redraw, medium conversion, timeline collapse, accidental cuts, flicker, mutation, or unusable endpoints.

## Completion Gate

Do not claim an image, prompt, card, package, or return is complete unless:

- current project sources were used rather than assumed;
- all mandatory fields are present and project-specific;
- style and continuity locks are explicit;
- narrative phase and character state IDs are explicit and validated across transition boundaries;
- video duration was analyzed rather than defaulted;
- the complete timeline is covered when video applies;
- paths/versions are preserved when working in Pipeline Hub;
- applicable validators pass;
- every generated image passed immediate image-quality QA before it was used as a reference or included in a batch;
- multi-keyframe shots include the numbered storyboard sheet and single-shot numbered prompt structure;
- every packaged asset belongs to the current director-approved narrative branch and no superseded branch leaks into the delivery;
- story-critical props pass structural plausibility and approved prop-state checks;
- exact text is verified character by character, and title/logo appearance requests include a sequence rather than only a terminal still;
- candidates remain candidates until director selection.

An attractive result that violates a hard rule is a failed result.

Run `scripts/validate_prompt_contract.py <board-or-manifest.json>` on every newly created or modified prompt set. Legacy prompts may remain historical, but they must pass this contract before they are reused for new image or video generation.

For projects with narrative state changes, also run `scripts/validate_narrative_state_contract.py <board.json> --project-root <project-root>`. Do not package, return, or generate when it reports a missing/mismatched phase, state ID, version prompt, transition rule, or multi-keyframe storyboard sheet.
