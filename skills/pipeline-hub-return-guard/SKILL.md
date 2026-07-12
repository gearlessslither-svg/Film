---
name: pipeline-hub-return-guard
description: Use when the user says “回传”, “回传到工具”, “回传电影工具”, “同步到 Pipeline Hub”, asks to return or restore AIGC film images/data to the local film tool, or when Codex is about to call Pipeline Hub idea-board/card-image-output callbacks. If “回传” is used without a named destination, first ask whether the destination is the film tool; only continue with this skill after confirmation. Enforces story/act/scene structure, screenplay order, version merging, AIGC video prompts, compact callbacks, and post-return validation.
---

# Pipeline Hub Return Guard

Treat “returned” as a validated film-data package, not merely a successful HTTP response.

Apply `$aigc-production-hard-rules` to returned storyboard text, image prompts, and video prompts before callback or validation.

## Trigger Gate

1. If the user only says “回传” or the destination is ambiguous, ask exactly one short question: `是回传到电影工具（Pipeline Hub）吗？`
2. Do not call a film callback until the user confirms.
3. If the user explicitly says “回传到电影工具” or “Pipeline Hub”, treat that as confirmation and proceed without asking again.
4. Work on one film project per window. Follow `film-session-relay` before crossing projects or handling a large image set.

## Source-of-Truth Order

Read the smallest sufficient set in this order:

1. `00_admin/handoff/HANDOFF_LATEST.md`
2. director script/story outline
3. current `03_story/idea_board/idea_board.json`, if present
4. final/candidate manifests and generated output paths
5. `07_shots/video_units.json`, shot list, transition edges, and the newest applicable video runbook/prompt index
6. active character, scene, prop, style, and QA locks

Never infer final status from filenames alone. Preserve unknowns as unknown.

## Active Narrative Branch Guard

Before any callback, compare the newest director feedback, handoff, authoritative script, Board, package manifest, and loop supersession records.

- Determine one explicit active narrative branch/version for the return.
- If the director removed a character, replaced an ending/prop/state, or rejected a sequence structure, exclude every dependent legacy row, version, prompt, and attachment from the callback even when its file exists and automatic QA passed.
- Preserve superseded assets on disk and in historical manifests, but never let an older Hub snapshot or full-Board POST restore them to the current branch.
- Prefer compact updates for the active branch. Before a full structural rewrite, read the Hub's live Board, compare card counts and branch identifiers, save a disk backup, then POST once and validate by reading back.
- Fail the return when the package mixes current and superseded branches or when the live Hub snapshot would overwrite a newer disk branch.

## Required Return Model

Before returning assets, construct or repair:

- `acts`: screenplay-derived acts with title, summary, dramatic purpose, key beats, and status.
- rows in screenplay order, not filesystem order.
- every row with stable `card_uid`, `item_id`, `act_id`, `scene_id`, beat, status, and project-relative output path.
- versions merged under the same story card. Never create duplicate cards merely because a new image version exists.
- `video_prompt` for every returned storyboard image. Prefer the newest applicable runbook or per-unit prompt; patch only changed v5 shots. Include duration, motion/action, camera, continuity, negative constraints, and the project audio hard rule.
- Every `video_prompt` must apply `$aigc-video-style-lock`: dynamically analyze the current project bible and actual approved image, put `[STYLE_FINGERPRINT]`, `[STYLE_INHERITANCE_HARD_LOCK]`, and `[STYLE_NEGATIVE]` before motion, and preserve that source-specific visual language across all frames. Never hard-code one preferred style. This is not a global anime ban—preserve anime when the source is anime and reject only style migration away from the actual source.
- Every `video_prompt` must first analyze and justify the shot's appropriate duration; never default all cards to 5 seconds. Include `[DURATION_RATIONALE]`, then a continuous `[TIMELINE]` from 0.0s to the exact endpoint with non-uniform time allocated by dramatic weight. Use finer beats around complex changes. Each beat must specify character performance/blocking and eye line; camera height/side/axis/lens/distance/movement; shot-size and composition changes; focus/exposure; key/fill/rim/practical lighting and shadow changes; environment/material/secondary motion; continuity locks; and the final settled state. Fields that do not change must be stated as held.
- approved/current/candidate/fallback distinctions without silently promoting a candidate.
- an explicit active-branch identifier or authoritative-script reference, plus exclusions for director-superseded assets.

If the project has no explicit act split, derive a reviewable 3–5 act structure from the director script and scene batches. State that it is derived; do not alter the story.

## Callback Rules

- Use project-relative `output_path`; never return base64 images.
- Prefer compact `row_updates` keyed by `card_uid` or `item_id` for ordinary updates.
- POST a complete Idea Board only when creating or genuinely rewriting project structure, such as restoring missing acts or rebuilding a corrupted board.
- Include `image_analysis` and `video_prompt` when returning an image result.
- When the Board is empty, always provide a unique explicit `card_uid`; never rely on an empty-ID fallback.
- Preserve unrelated rows and user selections. Never overwrite a final package unless explicitly authorized.

## Hard Completion Gate

Run:

```bash
python3 scripts/validate_pipeline_hub_return.py <project-root>
```

Do not say “回传完成” unless it exits successfully. The gate requires:

- at least one act and one row;
- unique `card_uid` and `item_id`;
- every row assigned to a declared act and a non-empty scene;
- every row containing a non-empty AIGC video prompt;
- every video prompt explicitly preserving the source image's art style rather than relying on a generic style label or universal `no anime` phrase;
- every video prompt covering its declared duration with an ordered, gap-free timeline and an explicit final-frame state;
- every current image and every version path existing inside the project;
- no selected/final promotion invented during transfer.
- no superseded story branch, removed character, replaced prop concept, rejected typography, or obsolete sequence restored into current rows or versions.

After callback, read the Board through the Hub endpoint or disk and run the validator again. Report card count, version count, act count, missing paths, video-prompt coverage, and remaining candidates requiring director review.

## Failure Handling

- If callback rows collapse, duplicate, reorder, or lose metadata, stop and repair the Board before reporting success.
- Record the failure and repair in `HANDOFF_LATEST.md` and the project loop when director-visible.
- Never regenerate images to repair a metadata-only return failure.
- Never treat automatic QA as director selection.
