# Pipeline Hub Dev Log / 总控台开发记录

This log records user-facing workflow changes for `apps/pipeline-hub/`.
Generated local images and one-off job outputs should not be committed unless they are curated fixtures.

## 2026-06-20 - Lightweight Codex Handoffs

Problem:
- Codex analysis and generation cards were carrying too much project context, including full story structures and full `idea_board` JSON.
- This wasted tokens and made image/retouch tasks easier to misinterpret because unrelated story context competed with the selected target images and revision notes.

Decision:
- Only remote autopilot, project audit, and structure-wide merge tasks may carry broad project context.
- Normal storyboard image packets, external retouch analysis packets, and external retouch image packets must be scoped to selected targets only.

Implementation:
- `POST /api/projects/<slug>/idea-board` now accepts compact `row_updates` patches keyed by `card_uid` or `item_id`.
- External retouch analysis packets now include only overall style, global retouch references, selected target cards, per-card revision notes, single-card references, and a compact callback schema.
- External retouch image packets now use a dedicated lightweight handoff template.
- Normal card image packets now use compact task payloads instead of embedding full Story, Context Cards, Global References, and raw generation context.
- Frontend `createCardImagePacketForTargets()` passes `packet_kind` so the backend can choose the correct packet template.

Current packet scope contract:
- Analysis card: selected targets, global/single references, revision notes, visual analysis requirements, compact `row_updates` callback.
- Image card: selected targets, required references, continuity locks, whitebox guidance, spatial checks, candidate output paths, image/video callback requirements.
- External retouch: source image, retouch note, global/single references, output paths, image analysis and AIGC video prompt callback.
- Not allowed in normal per-card packets: full `idea_board`, full story outline, unrelated acts, unrelated rows, full project bible dumps, or all project images.

Validation:
- `python3 -m py_compile apps/pipeline-hub/server.py`
- `node --check apps/pipeline-hub/static/app.js`
- Legacy external retouch analysis packet size observed: 12,709 lines.
- New external retouch analysis packet size observed: 185 lines for the same 17 selected targets.

Related skill rule:
- `skills/aigc-film-pipeline/SKILL.md` now requires minimal Codex handoff scope for ordinary per-card work and compact `row_updates` callbacks for text-only card updates.
