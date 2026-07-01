# Reference-003 Next Window Preflight

- Rebuilt: `2026-06-30T12:42:00+08:00`
- Status: `ready_for_fresh_window_generation`
- Fresh window required: `True`
- Next action: Open a fresh window and generate OP_SHOT_025 through OP_SHOT_042 in queue_order.

## Summary

- `queue_items`: `18`
- `expected_outputs_existing`: `0`
- `expected_outputs_missing`: `18`
- `board_status_counts`: `{'generated_reference003_qa_pass': 24, 'prompt_ready_reference003': 18}`
- `shot_list_status_counts`: `{'generated_reference003_qa_pass': 24, 'prompt_ready_reference003': 18}`
- `project_validation_pass`: `True`

## Gates

- [x] `handoff_files_exist` — True
- [x] `project_validation` — project_status=pass
- [x] `queue_has_18_items` — 18
- [x] `queue_order_op_shot_025_to_042` — ['OP_SHOT_025']..['OP_SHOT_042']
- [x] `batch_counts_6_each` — {'05': 6, '06': 6, '07': 6}
- [x] `reference_frames_exist` — 18/18
- [x] `prompt_files_match_queue_text` — 18/18
- [x] `board_and_shot_list_at_24_18` — board={'generated_reference003_qa_pass': 24, 'prompt_ready_reference003': 18}; shot_list={'generated_reference003_qa_pass': 24, 'prompt_ready_reference003': 18}
- [x] `next_window_packet_ready` — ready_for_fresh_window_image_generation

## Queue

| # | Batch | Item | Reference | Prompt | Output exists |
|---:|---|---|---|---|---|
| 1 | 05 | `OP_SHOT_025` | True | True | False |
| 2 | 05 | `OP_SHOT_026` | True | True | False |
| 3 | 05 | `OP_SHOT_027` | True | True | False |
| 4 | 05 | `OP_SHOT_028` | True | True | False |
| 5 | 05 | `OP_SHOT_029` | True | True | False |
| 6 | 05 | `OP_SHOT_030` | True | True | False |
| 7 | 06 | `OP_SHOT_031` | True | True | False |
| 8 | 06 | `OP_SHOT_032` | True | True | False |
| 9 | 06 | `OP_SHOT_033` | True | True | False |
| 10 | 06 | `OP_SHOT_034` | True | True | False |
| 11 | 06 | `OP_SHOT_035` | True | True | False |
| 12 | 06 | `OP_SHOT_036` | True | True | False |
| 13 | 07 | `OP_SHOT_037` | True | True | False |
| 14 | 07 | `OP_SHOT_038` | True | True | False |
| 15 | 07 | `OP_SHOT_039` | True | True | False |
| 16 | 07 | `OP_SHOT_040` | True | True | False |
| 17 | 07 | `OP_SHOT_041` | True | True | False |
| 18 | 07 | `OP_SHOT_042` | True | True | False |

## Evidence Files

- `handoff_latest`: `00_admin/handoff/HANDOFF_LATEST.md`
- `start_here`: `00_admin/handoff/NEXT_WINDOW_START_HERE_REFERENCE003_20260630.md`
- `queue_json`: `00_admin/ai_bridge/packets/20260630_reference003_remaining_keyframe_generation_queue.json`
- `next_window_packet`: `00_admin/ai_bridge/packets/20260630_reference003_next_window_batch05_07_execution.json`
- `apply_helper`: `00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py`
