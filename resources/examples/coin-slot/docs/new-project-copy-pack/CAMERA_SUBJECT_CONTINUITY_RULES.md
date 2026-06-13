> 双语说明 / Bilingual note: 本文件保留英文原文，以避免破坏提示词、文件名、路径、字段名和脚本读取。中文使用时请把它视为生产记录、规则、索引或提示词资产；英文正文为可执行/可追溯原文。 / The English source text is preserved to keep prompts, filenames, paths, field names, and script parsing stable. Treat this as a production record, rule, index, or prompt asset; the English body is the executable and traceable source text.

# Camera-Subject Continuity Rules v1

## Universal Principle

Storyboard images are not character reference sheets. A character should not face the camera by default.

For every panel, the character's facing direction, gaze, body orientation, and screen movement must follow the camera motivation and the story action. The camera may show a face only when the shot is a reaction, confrontation, or deliberately staged reveal.

## Required Shot Logic

Before generating any storyboard frame, assign one `camera_subject_relation`:

| relation | default character facing | use case |
|---|---|---|
| `rear_follow` | back view or three-quarter back | entering a space, walking forward, fleeing, chasing, following a character |
| `over_shoulder` | foreground shoulder/back/head visible, gaze aimed at target | discovering an object, watching an opponent, looking at a screen or doorway |
| `pov_or_subjective` | character usually off-camera or not looking at camera | what the character sees |
| `profile_cross` | side profile or three-quarter side | crossing frame, moving from one space to another |
| `reaction_cut` | front or three-quarter front allowed | explicit emotional reaction beat |
| `confrontation` | characters face each other, not the viewer | standoff, argument, duel, threat |
| `insert_detail` | no portrait logic | hands, props, buttons, weapons, phones, objects |

## Mandatory Prompt Fields

Every human-containing storyboard prompt must include:

1. `camera_subject_relation`: one of the relations above.
2. `character_facing`: backs to camera / three-quarter back / side profile / looking at target / front reaction.
3. `gaze_target`: the thing the character is actually looking at.
4. `camera_motivation`: follows the character / reveals the space / watches a reaction / locks a confrontation / shows an insert.

## Default Rules

- If the camera follows a character into a space, the character should be back-facing or three-quarter back-facing.
- If the character is discovering something, show their shoulder/back/profile and the object of attention.
- If the character is fleeing or chasing, never make them stop and look at camera unless the panel is explicitly a reaction cut.
- If the shot is about a place, object, or threat, do not turn it into a portrait.
- If the panel says "walks toward", "enters", "approaches", "runs to", "turns toward", or "looks at", the prompt must specify the target and facing direction.

## Prohibited Defaults

- Do not make every character face the viewer.
- Do not use character-sheet logic in storyboard frames.
- Do not create a staged lineup unless the story explicitly calls for one.
- Do not let characters look at the camera without a story reason.
- Do not sacrifice movement direction or spatial continuity just to show faces.

## Useful Prompt Phrases

- `rear follow shot`
- `camera follows behind the characters`
- `backs to camera`
- `three-quarter back view`
- `back of heads and shoulders visible`
- `characters look toward the target, not at the camera`
- `moving into the space, not posing`
- `single continuous movie frame, no character-sheet logic`

## Negative Prompt Phrases

- `front-facing portrait`
- `posing for camera`
- `looking at camera`
- `character sheet`
- `turnaround reference`
- `all faces toward viewer`
- `staged lineup`

## QA Failure Types

| issue_type | meaning | required fix |
|---|---|---|
| `wrong_camera_subject_relation` | shot function and character facing conflict | rewrite prompt with explicit relation/facing/gaze |
| `staged_character_sheet_logic` | storyboard looks like a posed reference image | return to action direction and camera motivation |
| `gaze_breaks_story_logic` | character looks at camera without reason | define `gaze_target`; regenerate |
| `movement_direction_broken` | character body direction contradicts story movement | restore axis and travel direction |

## Acceptance Gate

A generated frame cannot pass storyboard QA until its camera relation, character facing, gaze target, and movement direction match the adjacent panels.
