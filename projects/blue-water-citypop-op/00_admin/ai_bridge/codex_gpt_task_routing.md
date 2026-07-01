# Codex / GPT Task Routing

## Always Start Here

Every substantial Codex task in this project should first decide whether the task is:

- local execution,
- compact reasoning,
- or a loop that needs both.

If it needs both, Codex creates a packet in `00_admin/ai_bridge/packets/` before asking GPT for judgment.

## Good GPT Tasks

GPT can safely share these jobs when Codex provides bounded evidence:

| Task | Why GPT helps | Codex packet should include |
|---|---|---|
| Reference rhythm analysis | Editing and film-language judgment are token-heavy but text/visual-summary friendly. | Media info, contact sheet path, sampled frame labels, cut candidates, current wrong assumption. |
| One-take vs montage decision | GPT can reason from script intent and sampled evidence. | Script excerpt, frame timeline, transition candidates, desired output format. |
| Prompt rewrite | GPT is good at style and specificity once continuity facts are fixed. | Unit facts, ordered images, transition edges, forbidden drift. |
| Adversarial review | GPT can attack a plan for continuity failures. | Proposed unit/prompt, evidence paths, known risks. |
| Director options | GPT can compare options without touching local files. | Constraints, candidate plans, acceptance criteria. |

## Keep In Codex

Codex should not delegate these:

- Reading or writing local project files.
- Running video extraction, frame sampling, ffmpeg, Blender, validation, or Pipeline Hub callbacks.
- Managing handoff/session bloat.
- Copying generated images or large media.
- Deciding that a local file was successfully updated.

## Apply Rule

GPT may propose. Codex applies.

No GPT answer is production state until Codex has written it into the project and validated the affected files.
