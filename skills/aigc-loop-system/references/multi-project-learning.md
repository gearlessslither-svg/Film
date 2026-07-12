# Multi-Project Learning

The AIGC film system will contain projects with different styles, goals, tools, and workflows. Loop learning must preserve difference instead of forcing every project into one taste.

## Knowledge Layers

1. **Global method**
   - attempt records;
   - QA and review gates;
   - human feedback;
   - failure labels;
   - prompt patches;
   - stop/resume rules.

2. **Stage-specific rules**
   - idea selection;
   - lookdev;
   - still image/keyframe;
   - video prompt;
   - video output;
   - edit/delivery.

3. **Tool-specific rules**
   - image model behavior;
   - video model behavior;
   - Blender/previs;
   - external retouch or upscaling.

4. **Style-family rules**
   - documentary realism;
   - anime;
   - music MV;
   - surreal comedy;
   - horror;
   - product/brand film;
   - video-reference remake.

5. **Project-local rules**
   - director taste;
   - exact style bible;
   - character and setting locks;
   - project-specific taboos.

## Promotion Test

Before turning a project lesson into a broader rule, answer:

- Is the failure repeated or only one director preference?
- Does it come from model behavior, prompt structure, style choice, or this exact project?
- Would the opposite rule be correct for another project?
- Can the rule be tested in future attempts?
- What is the narrowest safe scope?

Use the narrowest scope that prevents the failure.

## Examples

`Do not use full-frame tiny-object clutter for China Gods Kon-style images`

- Scope: project/style-family.
- Not global, because some collage or crowd projects may intentionally need dense frames.

`Record human verdict before resuming a failed batch`

- Scope: global method.
- Safe across all projects.

`No music/BGM in image-to-video prompts`

- Scope: global hard rule unless user overrides.
- Reason: final edit music is handled separately.

## Project Profiles

Each project loop config should declare:

```yaml
project_profile:
  project_type: music_mv | story_film | lookdev_set | video_reference_remake | tool_test
  style_family: anime | photoreal | surreal | documentary | mixed_media | other
  workflow_family: lookdev_only | script_first | reference_remake | image_set | video_first | tool_test
  medium: still_image | image_to_video | video | mixed
  primary_success_metric: aesthetics | story | continuity | motion | speed | traffic
  allowed_complexity: low | medium | high
  director_review_required: true
  human_feedback_required_at:
    - style_lock
    - pilot_pass
    - batch_resume_after_reject
    - final_acceptance
```

Rubrics can then weight categories differently per project.

## Workflow Adapters

Do not make every project follow every gate with the same intensity. Select an adapter from the project profile:

- `music_mv`: prioritize lookdev, emotional rhythm, keyframe beauty, video prompt feasibility, and edit flow. Story continuity is lighter unless the project says otherwise.
- `story_film`: prioritize setting lock, character/prop continuity, spatial readability, keyframe relationship, video output, and edit delivery.
- `lookdev_set`: prioritize a small number of excellent pilots, contact sheets, style clarity, and rejection labels before scale.
- `video_reference_remake`: prioritize reference analysis, promoted-frame justification, timing/camera/motion match, and generated-asset mapping.
- `tool_test`: prioritize hypothesis, reproducibility, fixed inputs, measured differences, and tool-specific conclusions.

The adapter decides which loop gates are mandatory, which rubric categories are hard fails, and when human feedback is required.

## Rule Import Protocol

When reusing a lesson from another project, record it as:

```yaml
imported_rule:
  source_project: china-gods
  proposed_scope: style_family
  compatibility_checked:
    project_type: false
    style_family: true
    workflow_family: true
    medium: true
    generation_tool: true
    pipeline_stage: true
    audience_intent: false
    allowed_complexity: true
  status: hypothesis
```

If any important compatibility field differs, keep the lesson as `hypothesis`, not `hard_rule`. After 2 or more matching failures in the new scope, promote it only to the narrowest useful scope.

## Human Feedback Placement

Human/director feedback is required at aesthetic and intent gates:

- style direction lock;
- pilot pass before batch generation;
- resume decision after any hard rejection;
- final acceptance or known-caveat delivery.

Automation can reject obvious technical failures, but it cannot grant final taste approval.
