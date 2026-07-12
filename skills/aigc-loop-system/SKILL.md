---
name: aigc-loop-system
description: Use when planning, generating, reviewing, repairing, or packaging AIGC film work that should improve through recorded feedback loops; when the user asks for loop engineering, self-iteration, human feedback, attempt records, failure libraries, prompt patches, quality gates, batch-generation stop rules, or converting AIGC film/image/video workflows into evaluate-and-iterate systems.
---

# AIGC Loop System

This skill turns AIGC film work from one-shot prompting into a recorded production loop:

```text
brief -> constraints -> attempt -> evaluate -> diagnose -> revise -> record -> promote/reject/stop
```

Use it as the supervisory layer over `aigc-film-pipeline`, `aigc-film-project-auditor`, `image-quality-guard`, `idea-engine`, Blender/previs work, image generation, video prompts, and delivery packaging.

Treat `$aigc-production-hard-rules` as the mandatory generation baseline. Loops may tighten project-specific thresholds, but must not weaken its dynamic style, professional image specification, shot-specific duration, full-timeline, continuity, or QA gates without explicit director override.

## Core Rule

Do not continue a batch after a director-visible failure. Start or update a loop, record the failed attempt, write failure labels, patch the prompt/constraints, and regenerate a small pilot before resuming scale.

## Director Override And Supersession Loop

When the director changes story, character presence, ending, transformation state, prop concept, or sequence structure after assets already exist:

1. Treat the instruction as an explicit override event and stop every dependent task.
2. Record `director_override` plus the narrowest applicable labels: `story_branch_superseded`, `character_removed`, `prop_concept_replaced`, `ending_replaced`, `sequence_missing`, or `typography_invalid`.
3. Mark affected outputs and prompts `superseded` or `rejected`; preserve them for evidence but remove them from active references, current Board rows, packages, callbacks, and downstream generations.
4. Write one replacement constraint set before regenerating. Do not keep stacking old and new requirements into one prompt.
5. Resume with one pilot from the replacement branch. Only after it passes may the remaining batch continue.

An automatic QA pass cannot rescue a director-superseded asset. Narrative validity and director intent outrank surface cleanliness.

## Multi-Project Rule

Never use one universal aesthetic rubric for all projects. Use a two-layer system:

- **Global loop layer**: method, attempt records, failure labels, stop rules, human feedback, and evidence discipline.
- **Project loop layer**: style-specific goals, allowed weirdness, scoring weights, pass thresholds, and director taste.

Only promote a project-local lesson to global memory after deciding its scope: project-only, style-family, tool-specific, pipeline-stage, or truly global.

## Project Profile / Adapter Rule

Every project loop must declare its project profile before serious generation:

- `project_type`: music MV, story film, lookdev set, video-reference remake, tool test, etc.
- `style_family`: anime, photoreal, documentary, surreal comedy, horror, mixed media, etc.
- `workflow_family`: lookdev-only, script-first, reference-remake, image-set, video-first, etc.
- `primary_success_metric`: aesthetics, story, continuity, motion, speed, traffic, or reproducibility.
- `allowed_complexity`: low, medium, or high.

Use the profile to select the workflow adapter and rubric weights. A lesson from another project starts as a hypothesis unless the project type, style family, workflow family, tool, stage, audience intent, and complexity are compatible. Aesthetic rules are never global by default.

## Quick Start

For any project-bound AIGC asset:

1. Ensure the project has `10_qa/loops/`:
   ```bash
   python3 Film/scripts/loop/loop_attempt.py init-project Film/projects/<slug> \
     --project-type music_mv \
     --style-family anime \
     --workflow-family lookdev_only \
     --primary-success-metric aesthetics \
     --allowed-complexity low
   ```
2. Start an attempt before or immediately after generation:
   ```bash
   python3 Film/scripts/loop/loop_attempt.py start-attempt Film/projects/<slug> \
     --asset-id 02_gao_qiu_football \
     --stage lookdev_image \
     --prompt path/to/prompt.md \
     --output path/to/output.png \
     --source path/to/reference.png
   ```
3. Run automatic QA when the output is an image:
   ```bash
   python3 Film/scripts/loop/loop_attempt.py auto-qa Film/projects/<slug> \
     --asset-id 02_gao_qiu_football \
     --attempt latest
   ```
4. Record human/director review:
   ```bash
   python3 Film/scripts/loop/loop_attempt.py review Film/projects/<slug> \
     --asset-id 02_gao_qiu_football \
     --attempt latest \
     --verdict reject \
     --label dirty_frame \
     --label subject_lost \
     --feedback "主体不突出，画面太脏" \
     --must-change "只保留一个主神、一个场景、一个转场装置"
   ```
5. If rejected, create one revised pilot before any further batch generation.

## Loop Gates

Use these gates across the film pipeline:

- **Topic loop**: idea must pass hook, visual promise, feasibility, and risk checks before project setup.
- **Lookdev loop**: 2-3 pilots must pass before batch styleframes.
- **Keyframe loop**: every generated keyframe gets an attempt record, auto QA, and pass/reject verdict.
- **Video prompt loop**: motion prompt must pass feasibility before external generation.
- **Video output loop**: generated clips get temporal stability and edit-usefulness review.
- **Delivery loop**: package must validate file completeness, source mapping, and final director acceptance.
- **Skill loop**: repeated failures become scoped project rules; only reviewed repeated rules become global lessons.

Before applying a lesson from another project, ask whether the new project shares the same medium, tool, style family, generation model, audience, and production stage. If not, treat the lesson as a hypothesis, not a rule.

Read `references/loop-contract.md` before creating or changing a project-level loop contract. Read `references/rubrics.md` when judging image, video prompt, video output, or delivery attempts.
Read `references/multi-project-learning.md` when converting project feedback into reusable system knowledge.

## Human Feedback

Human feedback is mandatory for aesthetic and director-intent decisions. Automatic checks can warn about noise, missing files, broken schemas, or continuity, but they cannot approve taste.

Record human feedback in structured form:

```yaml
verdict: reject
failure_labels:
  - dirty_frame
  - subject_lost
must_change:
  - "主体必须 45-65% 画面高度"
  - "只保留一个梦境/现实转场装置"
```

If the user gives free-form feedback, translate it into labels and prompt patches before regenerating.

## Stop Rules

Stop generation and loop instead when:

- one output has a hard failure in subject, face/anatomy, style coherence, or composition cleanliness;
- two outputs in a batch share the same failure label;
- the output is attractive but violates the style/identity/scene lock;
- the prompt grows by adding more style references instead of removing ambiguity;
- the user says the direction is wrong, dirty, noisy, mixed, generic, or not the intended aesthetic.
- the user removes a character, replaces a prop/story mechanism, or changes the ending while dependent generation is running.

## Prompt Patch Principle

A rejected attempt should usually make the next prompt shorter and clearer, not richer.

Prefer:

- one dominant subject;
- one concrete setting;
- one transition or transformation device;
- 1-2 hero details;
- clear negative constraints.

Avoid:

- long lists of decorative props;
- multiple style references fighting each other;
- full-frame crowds, confetti, fake symbols, or pseudo-text;
- "more cinematic / more detailed" as a repair.

Treat `prop_design_fake`, `unlocked_prop`, `prop_state_mismatch`, `symbolism_overload`, `typography_invalid`, and `sequence_missing` as semantic failures. Regenerate or rebuild the asset/sequence; do not run surface denoising as the primary fix.

## Promotion

Only promote an output to production when:

- required hard rubric categories pass;
- failure labels are empty or explicitly waived by the director;
- auto QA is pass or manually accepted warn;
- prompt, output path, review, and verdict are recorded;
- any user feedback has been converted into the next reusable rule or rejected as one-off taste.
- the attempt belongs to the active director-approved narrative branch and is not listed as superseded in the loop, handoff, Board, or package manifest.

## Skill Maintenance

When repeated loop failures reveal a reusable rule:

1. Keep it project-local first in `10_qa/loops/LOOP_LEDGER.md`.
2. If it recurs across projects, propose ingestion through `aigc-film-project-memory`.
3. Patch the relevant skill only when the rule is scoped, testable, and safe.
