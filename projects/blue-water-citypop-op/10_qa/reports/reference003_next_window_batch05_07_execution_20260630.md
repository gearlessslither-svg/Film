# Reference-003 Next Window Execution Packet

- Created: `2026-06-30T06:23:01+08:00`
- Purpose: fresh-window execution plan for the remaining 18 official keyframes, Batch05 to Batch07.
- Current state: 24/42 official keyframes QA pass; 18/42 prompt-ready.
- This packet does not generate images in the current WARN window.

## Start Here

1. Open a fresh Codex window/session for `blue-water-citypop-op`.
2. Read `00_admin/handoff/HANDOFF_LATEST.md` and this packet.
3. Run `python3 00_admin/ai_bridge/packets/run_reference003_next_window_preflight.py` and continue only if it reports `ready_for_fresh_window_generation`.
4. Run Batch05, then Batch06, then Batch07. Keep outputs in the expected batch `outputs/` folders.
5. After each batch: QA, update only compact row fields, validate project, refresh handoff.

## Batch Sequence

### REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY

- Manifest: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/manifest.json`
- Reference sheet: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/REFERENCE003_QA_BATCH05_reference_sheet.jpg`
- Prompt pack: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/prompts/BATCH05_generation_prompt_pack.md`
- QA checklist: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/BATCH05_QA_CHECKLIST.md`
- Expected QA report: `10_qa/reports/reference003_qa_batch05_keyframes_20260630.md`

| Item | Timecode | Unit | Reference | Prompt | Expected output |
|---|---:|---|---|---|---|
| `OP_SHOT_025` | 00:51.50 | `VU_REF003_012_GRANDIS_VEHICLE_ACTION` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_025_ref_005150.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/prompts/OP_SHOT_025_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_025.png` |
| `OP_SHOT_026` | 00:52.50 | `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_026_ref_005250.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/prompts/OP_SHOT_026_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_026.png` |
| `OP_SHOT_027` | 00:55.00 | `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_027_ref_005500.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/prompts/OP_SHOT_027_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_027.png` |
| `OP_SHOT_028` | 00:58.50 | `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_028_ref_005850.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/prompts/OP_SHOT_028_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_028.png` |
| `OP_SHOT_029` | 01:01.50 | `VU_REF003_014_NIGHT_CITY_BLUE_GRID` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_029_ref_010150.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/prompts/OP_SHOT_029_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_029.png` |
| `OP_SHOT_030` | 01:03.50 | `VU_REF003_014_NIGHT_CITY_BLUE_GRID` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_030_ref_010350.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/prompts/OP_SHOT_030_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_030.png` |

### REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY

- Manifest: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/manifest.json`
- Reference sheet: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/REFERENCE003_QA_BATCH06_reference_sheet.jpg`
- Prompt pack: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/prompts/BATCH06_generation_prompt_pack.md`
- QA checklist: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/BATCH06_QA_CHECKLIST.md`
- Expected QA report: `10_qa/reports/reference003_qa_batch06_keyframes_20260630.md`

| Item | Timecode | Unit | Reference | Prompt | Expected output |
|---|---:|---|---|---|---|
| `OP_SHOT_031` | 01:05.50 | `VU_REF003_015_NIGHT_AIRCRAFT_PASS` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_031_ref_010550.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/prompts/OP_SHOT_031_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_031.png` |
| `OP_SHOT_032` | 01:06.50 | `VU_REF003_016_NEMO_SUNSET_PROFILE` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_032_ref_010650.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/prompts/OP_SHOT_032_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_032.png` |
| `OP_SHOT_033` | 01:09.50 | `VU_REF003_016_NEMO_SUNSET_PROFILE` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_033_ref_010950.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/prompts/OP_SHOT_033_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_033.png` |
| `OP_SHOT_034` | 01:12.00 | `VU_REF003_017_NADIA_SOLEMN_CLOSE` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_034_ref_011200.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/prompts/OP_SHOT_034_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_034.png` |
| `OP_SHOT_035` | 01:13.50 | `VU_REF003_018_BLUE_WATER_SYMBOL` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_035_ref_011350.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/prompts/OP_SHOT_035_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_035.png` |
| `OP_SHOT_036` | 01:15.00 | `VU_REF003_018_BLUE_WATER_SYMBOL` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_036_ref_011500.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/prompts/OP_SHOT_036_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_036.png` |

### REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY

- Manifest: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/manifest.json`
- Reference sheet: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/REFERENCE003_QA_BATCH07_reference_sheet.jpg`
- Prompt pack: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/prompts/BATCH07_generation_prompt_pack.md`
- QA checklist: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/BATCH07_QA_CHECKLIST.md`
- Expected QA report: `10_qa/reports/reference003_qa_batch07_keyframes_20260630.md`

| Item | Timecode | Unit | Reference | Prompt | Expected output |
|---|---:|---|---|---|---|
| `OP_SHOT_037` | 01:16.50 | `VU_REF003_018_BLUE_WATER_SYMBOL` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_037_ref_011650.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/prompts/OP_SHOT_037_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_037.png` |
| `OP_SHOT_038` | 01:18.00 | `VU_REF003_019_WATER_SPLASH_TRANSITION` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_038_ref_011800.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/prompts/OP_SHOT_038_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_038.png` |
| `OP_SHOT_039` | 01:19.00 | `VU_REF003_019_WATER_SPLASH_TRANSITION` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_039_ref_011900.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/prompts/OP_SHOT_039_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_039.png` |
| `OP_SHOT_040` | 01:20.00 | `VU_REF003_020_FINAL_SKY_SAFE_HOLD` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_040_ref_012000.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/prompts/OP_SHOT_040_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_040.png` |
| `OP_SHOT_041` | 01:22.00 | `VU_REF003_020_FINAL_SKY_SAFE_HOLD` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_041_ref_012200.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/prompts/OP_SHOT_041_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_041.png` |
| `OP_SHOT_042` | 01:23.50 | `VU_REF003_021_BLACK_TAIL` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_042_ref_012350.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/prompts/OP_SHOT_042_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_042.png` |

## Batch QA Rules

- Generate in a fresh Codex window/session before starting Batch05.
- Read HANDOFF_LATEST.md first; do not re-analyze the whole project from scratch.
- Use the reference frame and prompt file listed for each item; keep source timing and composition function from reference-003-full-op-2160p.
- Return and record only output_path plus compact row_updates; never paste or POST base64 or the whole board.
- No readable text, titles, credits, lyrics, NHK marks, subtitles, watermarks, or random symbols in any generated output.
- Keep Nadia and all minor characters age-appropriate, modestly clothed, and non-sexualized.
- After every batch, write QA report, update board/shot_list statuses, rerun validate_aigc_project.py, and refresh handoff.

## Remaining Keyframe Generation Queue

- Markdown queue with full prompt text: `00_admin/ai_bridge/packets/20260630_reference003_remaining_keyframe_generation_queue.md`
- Machine queue: `00_admin/ai_bridge/packets/20260630_reference003_remaining_keyframe_generation_queue.json`
- Fresh-window preflight: `00_admin/ai_bridge/packets/run_reference003_next_window_preflight.py`
- Latest preflight report: `10_qa/reports/reference003_next_window_preflight_20260630.md`
- Coverage: `OP_SHOT_025` to `OP_SHOT_042`, Batch05 then Batch06 then Batch07.
- Use the queue item `generation_prompt_text`, `reference_frame`, and `expected_output_path`; after visual QA, run the listed apply command.

## Post-Generation Apply Helper

- Helper: `00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py`
- Dry-run all remaining outputs: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch all`
- Apply one finished batch after visual QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 05 --apply`
- Apply all three finished batches after visual QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch all --apply`
- Safety: default is dry-run; `--apply` refuses missing outputs unless `--allow-partial` is explicitly used.

## Supporting Tools

- Rebuild keyframe status sheet/animatic after Batch07: `10_qa/reference_match/REFERENCE003_OFFICIAL_KEYFRAME_STATUS_20260630/rebuild_reference003_keyframe_status_previs.py`
- Project validator: `/Users/jaychoupp/Story/Film/scripts/validate_aigc_project.py`
- Relay status check: `/Users/jaychoupp/Story/Film/skills/film-session-relay/scripts/relay.py status`

## After Batch07

- `board_42_keyframes_qa_pass`: 42/42 rows in idea_board and shot_list are generated_reference003_qa_pass; evidence: 03_story/idea_board/idea_board.json, 07_shots/shot_list.csv, QA reports batch01-batch07
- `official_outputs_exist`: all 42 official output_path files exist on disk; evidence: reference003 status inventory rebuilt after Batch07
- `status_previs_rebuilt`: 10_qa/reference_match/REFERENCE003_OFFICIAL_KEYFRAME_STATUS_20260630/manifest.json reports 42 official generated keyframes and decode_ok=true; command: `python3 10_qa/reference_match/REFERENCE003_OFFICIAL_KEYFRAME_STATUS_20260630/rebuild_reference003_keyframe_status_previs.py`; evidence: rebuilt status sheet + status animatic MP4
- `video_units_unblocked`: 08_generation/jobs/REFERENCE003_VIDEO_UNITS_READY_20260630/manifest.json can be refreshed to 21/21 ready_for_video_generation; evidence: all video unit keyframes have generated_reference003_qa_pass outputs

## Next Stage

Start 21 VU_REF003 video segment generation in video_units.json order, then transition review, roughcut assembly, full decode QA, and final completion audit.
