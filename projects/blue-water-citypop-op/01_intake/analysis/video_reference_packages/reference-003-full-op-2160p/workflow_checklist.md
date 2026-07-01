# Video Reference Remake Workflow Checklist - reference-003-full-op-2160p

## Evidence Package

- Manifest: `manifest.json`
- Project video: `01_intake/references/reference-003-full-op-2160p.mp4`
- Contact sheet: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/contact_sheets/reference-003-full-op-2160p_contact_sheet_2fps.jpg`
- Frame index: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frame_index.csv`
- Scene detection: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/scene_detection`
- GPT bridge packet: `00_admin/ai_bridge/packets/20260630_043518_reference-003-full-op-2160p_pixel_remake.json`

## Codex Completed

- [x] Registered/copy reference video into project.
- [x] Probed media info.
- [x] Extracted sampled frames.
- [x] Generated contact sheet.
- [x] Generated machine scene/cut candidates.
- [x] Wrote manifest and frame index.
- [x] Wrote GPT bridge packet.

## GPT / Director Decision Needed

- [ ] Decide real shot/unit rhythm.
- [ ] Identify one-take vs montage vs transition sections.
- [ ] Identify keyframes and title-safe replacements.
- [ ] List Blender/previs-required units.
- [ ] Produce adversarial checks.

## Codex Apply After Decision

- [ ] Update director shooting script.
- [ ] Update `video_units.json`.
- [ ] Update `transition_edges.json`.
- [ ] Update camera/previs manifest.
- [ ] Rewrite unit prompts.
- [ ] Build Blender/previs only where needed.
- [ ] Run validation and reference-match QA.
