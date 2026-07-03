# Brutal Ink Restyle Retrospective — 2026-07-04

## Outcome

Project `dragon-house-black-green-ink-wash-title-21x9` has a finished `Brutal Ink Dragon Omen` delivery package:

- 20 story/event/person images in the locked brutal ink style.
- Opening 9s v2 start and end frames.
- 9s Blender motion-reference video with camera displacement, parallax, raised map nodes, and final aerial reveal.
- AIGC video prompt index for story images plus a dedicated opening 9s prompt that uses the start frame as a hard lock, Blender as motion reference, and the end frame as a loose final-reveal reference.
- Final zip at `11_delivery/packages/dragon-house-black-green-ink-wash-title-21x9_brutal_ink_story20_opening9s_blender_final_v1.zip`.

## Director Feedback That Changed The Work

- Style match is not composition match. The reference is a style lock, not a layout template.
- Repeating one-human-plus-one-dragon compositions made the batch feel narrow. The corrected batch needed events, landscapes, symbols, empty spaces, crowds, councils, battle aftermath, and political rooms.
- The opening could not be a static locked-off mechanism where buildings rise in place. The requested title-sequence feeling needed a traveling camera, visible world scale, and evolving geography.
- All AIGC video prompts must explicitly request sound effects / ambience only and forbid music, BGM, and soundtrack.

## What Worked

- Treating the director reference as a style-only lock preserved the brutal ink look while allowing different visual grammar per scene.
- A story20 structure gave the batch enough coverage across major events and characters without turning every image into the same dragon portrait.
- The opening v2 split solved the static problem: start frame establishes a low traveling map-world; Blender supplies actual spatial travel; end frame gives the large final destination.
- Putting the opening prompt in a dedicated file made the start/end/Blender roles clear enough for external AIGC video tools.

## Failure Modes To Avoid Next Time

- Do not use one accepted style image as a composition stamp.
- Do not batch-generate many story images without an explicit composition diversity checklist.
- Do not describe a Game-of-Thrones-style title sequence only as objects rising from a table; write the camera route first.
- Do not force exact end-frame matching for one-take AIGC shots if it causes jitter or morphing. Start frame can be strict; end frame can be a destination reference.
- Do not put local `.venv-video/`, full frame sequences, or oversized conversation-export zips into git.

## Skill Updates Written

- `skills/aigc-film-pipeline/SKILL.md`: added opening/title/map-mechanism one-take route rule.
- `skills/aigc-film-pipeline/references/next-project-rules.md`: added the same route rule in the next-project checklist.
- `skills/blender-video-pipeline/SKILL.md`: added camera journey, start-hard/end-loose, and audio-rule guidance.
- `skills/blender-video-pipeline/references/aigc-reference-packaging.md`: updated the reusable AIGC prompt template with loose end-frame handling and no-music audio hard rule.
- `skills/blender-video-pipeline/references/blender-automation.md`: added title-map route beats and Blender API guard notes.
- `skills/blender-video-pipeline/references/env-setup.md`: documented the Python 3.14 argparse percent-escape fix.
- `~/.codex/skills/aigc-film-project-memory/references/lesson-index.json`: added three reusable lessons for this project.

## Git Packaging Decision

The project folder contains local repair material and heavy intermediates. The repo should keep curated deliverables and reproducible source, but exclude:

- `.venv-video/`
- `renders/frames/`
- `11_delivery/packages/*conversation_export*.zip`
- cache directories

The final zip, final delivery directory, Blender script, `.blend`, MP4, prompt files, contact sheets, and handoff/retrospective are the useful git artifacts for future continuation.
