# Decision - Video Reference Pixel Remake Workflow v1

Status: accepted for this project  
Updated: 2026-06-30 02:36 Asia/Shanghai

## Decision

For any shot-accurate or "pixel-level" remake request, the reference video is the source of truth for rhythm, timing, composition anchors, transition points, and camera/subject movement.

Codex must not begin by guessing from memory, public notes, or isolated screenshots. Codex first builds a bounded reference package from the video, then GPT or local bounded analysis decides the editorial structure, then Codex applies the result to project files.

## Required Codex Outputs

- Project video copy under `01_intake/references/`
- Video reference package under `01_intake/analysis/video_reference_packages/<reference_id>/`
- Manifest: `manifest.json`
- Sampled frames and contact sheet
- Frame index CSV
- Scene/cut candidate logs
- GPT bridge packet under `00_admin/ai_bridge/packets/`
- Workflow checklist
- Accepted decisions under `00_admin/ai_bridge/decisions/`
- QA evidence under `10_qa/reference_match/` once remake outputs exist

## Required GPT / Director Role

GPT or director reads only bounded evidence and returns:

- shot/unit rhythm table,
- one-take vs montage vs transition judgment,
- keyframe plan,
- Blender/previs requirements,
- AIGC prompt strategy,
- adversarial checks,
- uncertainties.

## Apply Rule

GPT proposes; Codex applies and validates.

The answer is not production state until Codex writes it into:

- `03_story/scripts/director_shooting_script.md`
- `07_shots/video_units.json`
- `07_shots/transition_edges.json`
- `06_previs/camera_manifests/video_unit_camera_manifest.json`
- `07_shots/video_prompts_by_unit/`

## Current Reference Package

- Reference id: `reference-002-opening`
- Manifest: `01_intake/analysis/video_reference_packages/reference-002-opening/manifest.json`
- Contact sheet: `01_intake/analysis/video_reference_packages/reference-002-opening/contact_sheets/reference-002-opening_contact_sheet_2fps.jpg`
- Latest GPT packet: `00_admin/ai_bridge/packets/20260630_023556_reference-002-opening_pixel_remake.json`
- Checklist: `01_intake/analysis/video_reference_packages/reference-002-opening/workflow_checklist.md`

## Important Current Finding

The prior 24-second Blender one-take candidate must be treated as rhythm-wrong until reworked. The user-provided reference video shows a more segmented opening rhythm: bird sky motion, cloud/credit/title-safe beats, short aircraft reveal, title-safe hold, sun/light transition, and heroine close-up.
