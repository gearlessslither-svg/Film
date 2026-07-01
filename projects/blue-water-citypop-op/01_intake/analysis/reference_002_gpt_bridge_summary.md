# Reference 002 GPT Bridge Summary

Updated: 2026-06-30 01:45 Asia/Shanghai

## Source

- Original user file: `/Users/jaychoupp/Downloads/蓝宝石之迷-002.mp4`
- Project copy: `01_intake/references/nadia_op_reference_002.mp4`
- Duration: 23.01 seconds
- Video: 1920x1080, 30fps, H.264
- Audio: AAC stereo

## Codex Local Evidence

- 2fps frame directory: `01_intake/analysis/reference_002_frames_2fps/`
- 2fps contact sheet: `01_intake/analysis/reference_002_2fps_contact_sheet.jpg`
- Scene threshold 0.18 log: `01_intake/analysis/reference_002_scene_threshold_018.log`
- Scene threshold 0.08 log: `01_intake/analysis/reference_002_scene_threshold_008.log`

## First Visual Pass

This is a rough Codex observation from the contact sheet, not the final GPT/director answer:

| Time | Rough content |
|---:|---|
| 00.0-04.5 | White bird over blue sky, slow sustained motion. |
| 05.0-08.0 | Bird continues with title/credit overlay. |
| 08.5-12.0 | Cloud bank expands/fills frame; bird remains part of sky motion. |
| 12.5-14.0 | Flying machine/aircraft appears briefly, much shorter than current Blender one-take assumption. |
| 14.5-19.5 | Title/logo card over sky. |
| 20.0-21.0 | Light/sun flare transition. |
| 21.5-22.5 | Heroine close-up begins. |

## Machine Cut Candidates

Do not treat these as final cuts; they are only algorithmic hints:

- 00.20s / 00.30s
- 12.43s / 12.50s
- 13.33s-14.40s cluster
- 20.73s-22.00s cluster

## GPT Packet

Use this packet for GPT rhythm judgment:

`00_admin/ai_bridge/packets/20260630_014459_reference-002-opening-rhythm-analysis.json`

## What GPT Should Decide

1. Is the reference actually a single one-take, or a sequence of video units?
2. Where are the real editorial beats?
3. Which parts should be modeled in Blender as camera continuity?
4. Which parts should remain montage/title/transition units?
5. How should the current `VU_001_024_OPENING_SKY_BIRD_PLANE_ONETAKE` candidate be revised or replaced?

## Codex Apply Plan After GPT

After GPT or director returns a decision:

1. Write accepted timing into `03_story/scripts/director_shooting_script.md`.
2. Update `07_shots/video_units.json`.
3. Update `07_shots/transition_edges.json`.
4. Update `06_previs/camera_manifests/video_unit_camera_manifest.json`.
5. Rewrite affected `07_shots/video_prompts_by_unit/` prompts.
6. Rebuild Blender previs only for the portions that truly require continuous spatial proof.
7. Validate and update handoff.
