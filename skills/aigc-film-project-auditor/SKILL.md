---
name: aigc-film-project-auditor
description: Audit an AIGC film or video project folder for missing workflow assets, weak stage evidence, aesthetic risks, cinematic storytelling gaps, lookdev/previs/shot/prompt readiness, and industrial production blockers. Use when the user asks for one-click analysis of all current project steps, an asset health report, missing-work suggestions, creative QA, film-language review, or recommendations before batch image/video generation.
---

> 双语说明 / Bilingual note: 本文件保留英文原文，以避免破坏提示词、文件名、路径、字段名和脚本读取。中文使用时请把它视为生产记录、规则、索引或提示词资产；英文正文为可执行/可追溯原文。 / The English source text is preserved to keep prompts, filenames, paths, field names, and script parsing stable. Treat this as a production record, rule, index, or prompt asset; the English body is the executable and traceable source text.

# AIGC Film Project Auditor

Use this skill to turn a project folder scan into a director-facing production and aesthetic audit. The goal is not only to count files, but to judge whether the project is ready for stable AIGC image/video production.

## Workflow

1. Run the deterministic project scan from the repo root:

```powershell
python scripts/analyze_aigc_project.py projects/<project-slug> --sample-size 24
```

2. Read the generated report:

```text
projects/<project-slug>/10_qa/reports/project_audit_latest.md
```

3. Load `references/film-aesthetic-audit-rubric.md` when judging story, cinematography, production design, lookdev, whitebox/previs, editing rhythm, sound, image prompts, video prompts, or AIGC batch stability.

4. If the report lists representative images, videos, whitebox renders, contact sheets, or animatics, inspect them directly when tools are available. If direct visual inspection is not possible, say the audit is based on manifests, filenames, counts, and text evidence.

5. Produce a concise director-facing report with:

- Current readiness state.
- P0 blockers before batch generation.
- P1 missing assets that should be produced next.
- Aesthetic and cinematic risks.
- The smallest useful next production batch.
- Which evidence was actually inspected and which conclusions are inferred.

## Standards

- Separate missing evidence from creative judgment. A folder can be empty because work is missing, or because work exists only in an external linked archive.
- Prioritize the upstream cause. For example, bad image prompts may actually be caused by missing story-state locks, weak asset bible, or vague whitebox blocking.
- Prefer concrete film terms over generic taste words: shot size, lens, camera height, blocking, motivated light, color script, silhouette, screen direction, edit rhythm, sound perspective, texture, material, foreground/midground/background.
- Treat sound as part of the image/video plan, not a late finishing step.
- For AIGC, judge whether the pipeline has enough constraints for consistency: stage-specific character references, spatial whitebox, control layers, negative constraints, prompt templates, QA loops, and reject analysis.

## Report Shape

Lead with priorities:

```text
P0 - Must fix before batch generation
P1 - Should fix before serious production
P2 - Improves polish or scale
```

For every recommendation, include:

- Stage.
- Problem.
- Why it matters cinematically.
- Concrete next asset or decision to create.
- Whether the recommendation comes from scanned evidence, direct visual review, or inference.

End with a short next-batch proposal. A good next batch is small enough to finish, but large enough to remove uncertainty: for example 3 styleframes, 1 refined whitebox scene, 6 locked shots, 1 character stage sheet, and 1 sound mood pass.

## Tool Contract

The future GUI "Analyze Current Project" button should call:

```powershell
python scripts/analyze_aigc_project.py projects/<project-slug> --sample-size 24 --print-json
```

The button should open `10_qa/reports/project_audit_latest.md` after the command completes. The command returns process success even when the project has missing work; missing work is reported inside the audit status.

When the user asks to automatically fill missing work, the GUI "Autofill" button should call:

```powershell
python scripts/autofill_aigc_project.py projects/<project-slug> --max-rounds 3 --sample-size 24 --print-json
```

This agent may write safe local drafts and queue Codex/image2/Blender/plugin adapter tasks. External commands run only when explicitly enabled in `00_admin/autofill_config.yaml` and allowed by the current invocation.
