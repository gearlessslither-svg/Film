# Reference Video Frame Difference and Asset Promotion Rules

Use these rules whenever a project starts from a reference video or when an existing project needs denser video-based repair.

## Required Contract

- Reference-video analysis has two layers: baseline cadence extraction across the whole video, then difference-driven add-frame selection.
- Dense frame extraction is a local analysis step, not an asset step.
- Extracted screenshots are `candidate_reference_frame` records. They can guide analysis, prompts, whitebox, and AIGC video reference, but they are not final project assets.
- A candidate becomes a `promoted_keyframe_asset` only when it has a clear visual, semantic, edit, or continuity function that is not already covered by an adjacent approved asset.
- A promoted keyframe becomes usable in previews only after it is regenerated as a pure image and recorded with an `output_path`.

## Baseline Cadence

- Always include detected shot/video-unit start and end frames.
- Add regular interval samples across every shot/unit so the whole video has coverage before any intelligent selection happens.
- Use denser baseline samples for short, fast, music-video, action, group, prop-heavy, or transition-heavy sections; use lighter samples for long static holds.
- The baseline pass is for coverage and discovery. It should be allowed to over-collect candidates because promotion happens later.

## Shot / Video-Unit Adaptive Density

- Choose analysis density per shot or video unit. Do not use a single whole-video FPS as the production rule.
- Suggested desired analysis density:
  - Static holds, black frames, title-safe sky/background plates: 1-2fps plus start/end.
  - Slow environment, slow prop, or one-take portrait holds: 2-4fps plus start/end and one essential middle frame if needed.
  - Character intro, fast pose change, group blocking, vehicle movement, water/smoke/light transition: 6-8fps analysis.
  - Very short fast transitions, splash, impact, flash, aircraft/vehicle pass: 8-12fps analysis when a decoder is available.
- Analysis density is not generation density. A 12fps analysis pass may still promote only two or three generated image assets if the shot function is covered.
- For final or director-questioned shot-boundary work, add a source-FPS frame-level pass. Compute at least luminance/gray difference, color histogram difference, and edge/composition difference between adjacent frames, then flag local maxima and one-frame/two-frame insert candidates. This is how brief aircraft, prop, character, or transition flashes are caught when a 2fps or 4fps sheet misses them.
- Cross-check algorithmic boundaries with a second detector when possible, such as PySceneDetect `detect-content` / `detect-adaptive`. Treat agreement between OpenCV frame deltas and PySceneDetect as stronger evidence, but still require semantic review before changing production units.
- If the local environment cannot decode the source video at the desired density, mark `needs_more_extraction_for_final_decision: true` and use the best existing sampled frames only as a provisional R-pass. Do not pretend a 2fps audit is a final dense audit for fast shots.
- For every candidate, compute or estimate novelty against the nearest existing approved anchor and already generated expansion assets. A candidate that differs from the previous sampled frame but is already covered by an existing anchor should be collapsed.
- Use a first review pass to divide candidates into:
  - `P1_generate_next_small_batch`: high-value, low-redundancy candidates worth generating next.
  - `P2_review_after_p1`: useful but optional candidates to revisit if the preview still feels thin.
  - `P3_reference_video_or_already_handled`: one-take, repetitive, already R-generated, or reference-video-only candidates.
- Before generating, view a compact P1-only contact sheet. Remove subtitle-only differences, empty/title-safe variants, edge-frame artifacts, and near-duplicates from P1.

## Local Analysis Accuracy

- Local analysis is reliable for measurable signals: frame similarity, color/light change, camera/subject motion, shot-boundary detection, composition shifts, and duplicate collapse.
- Local analysis is not fully reliable for semantic importance, acting quality, identity beauty, emotional nuance, or whether a frame is the best director-facing beat.
- Use local scores to rank candidates, then apply film judgment, setting/identity locks, and targeted visual review for ambiguous or important decisions.
- A high local-change score can justify review, not automatic asset promotion.

## Token Discipline

- Run screenshot extraction, similarity scoring, motion scoring, and contact-sheet generation locally on disk.
- Keep high-volume frame folders out of the conversation. Return compact metadata: shot/unit id, timecode, thumbnail/contact-sheet path, score, and `difference_reason`.
- Only inspect individual frames in the conversation when a director decision, identity issue, or ambiguous difference requires visual review.

## Promotion Criteria

Promote a candidate frame when at least one of these changes materially:

- Composition, scale, camera position, axis, or screen direction.
- Character pose, gesture, facial state, blocking, or relationship between characters.
- Action phase, including preparation, impact, reaction, reveal, or aftermath.
- Prop, vehicle, costume, damage, dirt, light, water, weather, UI, or scene-state change.
- Story beat, emotional beat, transition edge, or edit function.
- Required first or final frame of a video unit.

Do not promote a candidate only because its timestamp is different.

## One-Take and Slow-Change Shots

- For slow one-take, slow push, hold, dialogue, look, vehicle follow, and Nemo/captain-style continuous shots, default to start frame + end frame + one or two middle transition frames.
- For long continuous openings or one-take phrases around 20-25 seconds, do not automatically create a dozen tiny video units just because there are visual beats inside the phrase. Split into 2-3 AIGC-manageable long chunks, carry the continuous motion in the reference clip and prompt, and use ordered anchors for the important beats.
- Use the reference video plus precise motion/camera prompts to carry the continuous movement.
- If adjacent candidates differ only by micro-position, expression drift, water/light noise, or compression artifacts, collapse them into the nearest promoted keyframe.
- Only add more frames when the shot has a true blocking, story, object, or camera change that the AIGC video model cannot infer reliably from the video reference and prompt.

## High-Change Shots

- For fast montage, group action, choreography, strong prop changes, crowd staging, rapid vehicle movement, or hard transitions, promote more frames when needed.
- Every extra promoted frame must include a `difference_reason` explaining what new information it carries.
- Group and crowd frames require identity anchors from approved locks before generation; text-only prompts are not enough.

## Asset Record Fields

Each promoted frame should record:

- `item_id`
- `parent_video_unit_id`
- `source_video_path`
- `source_timecode` or `source_time_sec`
- `keyframe_role` such as `start`, `middle_transition`, `turning_point`, `end`, or `montage_beat`
- `difference_reason`
- `reference_frame_path`
- `prompt_path`
- `output_path`
- `identity_qa`, `scene_qa`, `prop_qa`, and `video_ready_status`

## Generation Batch State Sync

- A P1 generation batch is not complete until every selected candidate has a real generated `output_path`, a generated contact sheet, and a batch manifest status such as `generated_pending_director_review`.
- If a project stores the same candidate records in more than one place, for example `units[].candidates` and a top-level `promoted_candidate_reference_frames` list, update all copies in the same operation. Do not leave one copy as `candidate_reference_frame_needs_prompt_and_generation` after the image has been generated.
- After P1 image generation, write the new generated anchors back into every affected video-unit prompt file or addendum before packaging AIGC video prompts. A generated image that exists only in an `outputs/` folder is not part of the unit contract yet.
- Save the final generation prompt path or prompt-addendum path for each promoted asset, especially when the live prompt was safety-rephrased or corrected after local QA. Do not let stale pre-generation prompt text remain the only prompt record.
- Treat local contact-sheet QA as a technical pass only: no text, no watermark, no reference-board border, no missing output. Character beauty, face consistency, group identity, and director-facing taste remain `pending_director_review` unless the director explicitly approves them.
- Also run a quick symbol/species/prop QA pass: reject random badges, logo-like marks, unintended military/political emblems, changed animal/mascot species, or changed core prop/vehicle silhouettes even when composition looks good.
- Do not merge P1 generated assets into an expanded preview manifest automatically. First report the generated contact sheet and generated count, then merge only the director-approved assets in timeline order.
- When generating multiple states of a transition, make adjacent assets carry different phases, such as water veil before burst versus peak splash, rather than near-duplicate pretty frames.
- If a source candidate uses a risky partial-body or intimate-feeling framing, preserve the shot function with a safe action/composition rewrite instead of reproducing the risky camera angle.
- Record generated image dimensions. If a tool returns mixed aspect ratios, preview/video assembly should fit or pad onto the target canvas; never stretch assets to match the project ratio.

## Preview Rule

- Expanded previews must be rebuilt from generated assets, not screenshot candidates.
- The preview manifest must include existing approved assets plus newly promoted/generated assets in timeline order.
- If dense analysis finds new candidates but no new generated images exist yet, report the stage as `analysis_ready`, not `preview_expanded`.
- If the final preview count stays the same after dense extraction, state whether no frames were promoted, promoted frames are waiting for generation, or generated frames have not been merged into the preview manifest.
