> 双语说明 / Bilingual note: 本文件保留英文原文，以避免破坏提示词、文件名、路径、字段名和脚本读取。中文使用时请把它视为生产记录、规则、索引或提示词资产；英文正文为可执行/可追溯原文。 / The English source text is preserved to keep prompts, filenames, paths, field names, and script parsing stable. Treat this as a production record, rule, index, or prompt asset; the English body is the executable and traceable source text.

# Pipeline Hub Test Report

Generated at: 2026-06-13T16:12:00+08:00

## Scope

Test the current AIGC pipeline vision with `projects/coin-slot/` as the sample project.

## Implemented Functions

- Local GUI hub at `apps/pipeline-hub/server.py`.
- Project creation API and GUI form.
- Existing project resource linking API and GUI form.
- Project structure validation button.
- Project asset/aesthetic analysis button.
- Project dashboard with readiness, P0 blockers, shot rows, and stage status.
- Stage panel for all 12 standardized workflow stages.
- Shot table viewer for `07_shots/shot_list.csv`.
- Latest audit report viewer.
- Coin Slot 12-shot sample seed script.

## Coin Slot Sample State

| Check | Result |
| --- | --- |
| Standard project path | `projects/coin-slot/` |
| Linked archive | `resources/examples/coin-slot` |
| Standard stages | 12 |
| Stage status | 12 pass, 0 warn, 0 fail |
| Shot rows | 12 |
| Audit status | pass |
| Readiness | 100% |
| P0 blockers | 0 |
| Linked files scanned | 1073 |
| Project files scanned | 68 |

## Commands Verified

```powershell
python -m py_compile apps\pipeline-hub\server.py scripts\analyze_aigc_project.py scripts\create_aigc_project.py scripts\validate_aigc_project.py scripts\seed_coin_slot_sample_project.py
node --check apps\pipeline-hub\static\app.js
python scripts\validate_aigc_project.py projects\coin-slot
python scripts\analyze_aigc_project.py projects\coin-slot --sample-size 24 --print-json
python scripts\seed_coin_slot_sample_project.py --force
```

## GUI/API Smoke Test

The local hub was started on `127.0.0.1:8789` for API testing and `127.0.0.1:8790` for visual screenshot testing.

Verified API results:

- HTML root returned 200.
- `GET /api/projects` returned the Coin Slot project.
- `GET /api/projects/coin-slot` returned 12 stages and 12 shot rows.
- `POST /api/projects/coin-slot/analyze` returned `status=pass`, `readiness=100`, `p0=0`.
- Temporary create/link/validate smoke project succeeded and was safely deleted.

## Visual Check

Headless Chrome screenshot confirmed:

- Project list renders.
- Coin Slot is selected.
- Metrics render as `Readiness 100%`, `P0 0`, `Shot rows 12`, `Stage status 12/0/0`.
- Stage panel displays Chinese stage names and pass status.
- Shot table displays seeded shot rows.
- Layout is readable at 1440x1000.

## Remaining Product-Level Expansions

The current system is a working minimum platform. Next valuable expansions are dedicated stage tools:

- Intake Analyzer.
- Direction Board.
- Asset Bible Manager.
- Previs Builder with stronger Blender/control-layer handling.
- Shot Factory for batch prompt/model jobs.
- QA Console for visual, spatial, audio, and delivery checks.
