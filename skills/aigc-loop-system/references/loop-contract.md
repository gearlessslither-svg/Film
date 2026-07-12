# Loop Contract Reference

Create a loop contract before serious AIGC batch generation.

## Required Project Structure

```text
10_qa/loops/
  loop_config.yaml
  LOOP_LEDGER.md
  failure_library/
    failure_taxonomy.yaml
    negative_examples/
  rubrics/
    image_keyframe_rubric.yaml
    video_prompt_rubric.yaml
    video_output_rubric.yaml
    delivery_rubric.yaml
  attempts/
    <asset_id>/
      attempt_001/
        prompt.md
        inputs.json
        output_path.txt
        auto_qa.json
        director_review.md
        verdict.json
        next_prompt_patch.md
```

## Attempt Lifecycle

1. **Start**: create attempt folder and record prompt, source refs, output path, stage, and asset id.
2. **Auto-check**: run available deterministic checks, such as image noise/fake-detail QA, validation, file existence, or schema checks.
3. **Human review**: record pass/reject/revise plus failure labels and must-change items.
4. **Prompt patch**: write what must change in the next attempt.
5. **Close**: append result to `LOOP_LEDGER.md`.
6. **Promote**: only after pass.

## Batch Policy

Start with a pilot batch:

- lookdev: 1-3 images;
- image keyframes: 1-3 representative shots;
- video prompts: 1-2 hardest units;
- video outputs: 1 clip per motion pattern.

Do not scale until pilot outputs pass.

## Director Feedback Policy

Director feedback outranks automatic scoring.

Translate feedback into:

- `verdict`;
- `failure_labels`;
- `must_change`;
- `may_keep`;
- `next_prompt_patch`.

Do not dilute feedback into vague style words.

## Negative Example Policy

Every important rejection should copy or link the failed output into:

```text
10_qa/loops/failure_library/negative_examples/
```

Use negative examples as regression tests before repeating a style, model, or prompt pattern.

## Project Profile Contract

`loop_config.yaml` must declare the project profile before batch generation:

- `project_type`
- `style_family`
- `workflow_family`
- `medium`
- `primary_success_metric`
- `allowed_complexity`
- `director_review_required`

The profile chooses the workflow adapter and prevents cross-project rule contamination. A rule imported from another project must be recorded as a hypothesis unless compatibility has been checked across project type, style family, workflow family, medium, tool, pipeline stage, audience intent, and allowed complexity.
