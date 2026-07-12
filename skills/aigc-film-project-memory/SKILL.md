---
name: aigc-film-project-memory
description: Use when starting, planning, reviewing, closing, or restarting any AIGC Film project; when the user mentions project summaries, lessons,经验入库, hard rules, previous project advice, or asks Codex to turn production experience into reusable rules. This skill scans validated project-memory lessons before new projects, checks conflicts/staleness, and enforces active/hard-rule lessons while keeping time-sensitive tool quotas under review.
---

# AIGC Film Project Memory

Use this skill before starting a new AIGC film project and when ingesting user-written project summaries or lessons.

## Mandatory Topic-Selection Gate

Every new AIGC film project must start with a topic-selection pass before creating production folders or generating assets.

In this pass:

1. Evaluate the idea from at least two angles:
   - traffic/audience potential
   - aesthetic and production value
2. Estimate production difficulty and likely failure points.
3. Compare the idea against relevant historical lessons in `references/lesson-index.json`.
4. Check whether the idea depends on time-sensitive platform/tool facts and mark those for current verification.
5. Recommend one of:
   - proceed
   - proceed after narrowing
   - park for later
   - reject or reframe
6. Do not create a full project folder until the user approves the selected direction.

## Operating Rules

1. Read `references/lesson-index.json` before making project-shaping decisions.
2. Treat `hard_rule: true` and `status: active` lessons as mandatory unless the current user explicitly overrides them.
3. Treat `status: needs_current_verification` lessons as reminders to verify current tool/platform behavior before use.
4. Treat `status: experimental` lessons as useful hypotheses, not rules.
5. If two lessons conflict, do not silently choose. State the conflict, preferred lesson, reason, and remaining risk.
6. Prefer current director feedback, completed-project evidence, newer same-area lessons, narrower scope, then human review.
7. Do not ingest a user claim as an active lesson until it is reviewed. If it is partly wrong, rewrite it into a safer, scoped form before入库.

## New Project Preflight

When a new AIGC film project starts:

1. Read `references/lesson-index.json`.
2. Select lessons relevant to the project type, subject, tools, and workflow stage.
3. Output a short "past project advice" section with:
   - mandatory rules
   - relevant active recommendations
   - stale/tool-specific items requiring current verification
   - conflicts or uncertainty
4. Convert selected lessons into concrete checks before generation or packaging.

## Lesson Ingestion Workflow

When the user writes summaries or experience notes:

1. Preserve the original claim.
2. Validate it using local project evidence when available.
3. For tool quotas, platform limits, model behavior, and promotion economics, mark as time-sensitive unless a current official source is verified.
4. Assign:
   - `status`: `active`, `hard_rule`, `experimental`, `needs_current_verification`, `superseded`, `deprecated`, or `context_only`
   - `reliability`: `high`, `medium`, or `low`
   - `scope`
   - `evidence`
   - `review_after`
5. If the user marks a lesson `hard rule`, challenge it once if it is unsafe, overbroad, outdated, or under-evidenced. Only store as `hard_rule: true` after the corrected form is sound.

## Loop Failure Ingestion

When a project records repeated failures in `10_qa/loops/`, treat them as candidate lessons:

1. Prefer concrete failed attempts over memory-only claims.
2. Preserve the failure labels, negative example path, director feedback, and prompt patch.
3. Decide scope before入库: project-local, style-family, image-generation-global, video-prompt-global, or pipeline-global.
4. Do not convert a single taste note into a global hard rule. Require repetition, strong evidence, or explicit user confirmation.
5. If accepted, rewrite the lesson as a testable rule with "Do" guidance and a counterexample.
6. Preserve project diversity. A rule from one style family must not constrain a different style family unless the failure is tool/pipeline-general. Use the narrowest safe scope.

## Useful Commands

Use the selector for a compact view:

```bash
python3 ~/.codex/skills/aigc-film-project-memory/scripts/select_lessons.py --area segmentation
python3 ~/.codex/skills/aigc-film-project-memory/scripts/select_lessons.py --project coin-slot
python3 ~/.codex/skills/aigc-film-project-memory/scripts/select_lessons.py --status needs_current_verification
```

## References

- `references/lesson-index.json`: structured source of truth.
- `references/ingestion-log-20260702.md`: first reviewed ingestion from `coin-slot` and `blue-water-citypop-op`.
