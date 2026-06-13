# SCN_ARCADE Camera Constraint Whiteboxes v001

Purpose:

- Keep the arcade storyboard environment spatially consistent after the mother image has been selected.
- Use the same OBJ proxy geometry as the source for every angle.
- Use the selected mother image as style reference and these camera whiteboxes as spatial reference.

Source files:

- Mother style image: `../SCN_ARCADE_lookdev_A_entrance_wide_v002_game_screens.png`
- OBJ geometry: `../whitebox_obj/SCN_ARCADE_mother_visual_constraint_whitebox_v001.obj`
- OBJ materials: `../whitebox_obj/SCN_ARCADE_mother_visual_constraint_whitebox_v001.mtl`

Generated camera constraints:

- `CAM_ARCADE_01_ENTRANCE_WIDE_constraint_whitebox_v001.png`
- `CAM_ARCADE_01_CHILD_POV_CENTER_constraint_whitebox_v001.png`
- `CAM_ARCADE_02_STREET_FIGHTER_CABINET_constraint_whitebox_v001.png`
- `CAM_ARCADE_03_DUEL_OVER_SHOULDER_constraint_whitebox_v001.png`
- `CAM_ARCADE_04_BOSS_LOSES_REACTION_constraint_whitebox_v001.png`
- `CAM_ARCADE_DETAIL_CONTROL_PANEL_constraint_whitebox_v001.png`
- `CAM_ARCADE_CEILING_PRESSURE_constraint_whitebox_v001.png`

Manifests:

- `SCN_ARCADE_camera_constraint_manifest_v001.csv`
- `SCN_ARCADE_camera_constraint_manifest_v001.json`
- `SCN_ARCADE_panel_camera_constraint_map_v001.csv`
- `SCN_ARCADE_formal_storyboard_prompt_pack_v001.csv`
- `SCN_ARCADE_formal_storyboard_prompt_pack_v001.md`
- `SCN_ARCADE_camera_constraints_validation_v001.json`
- `SCN_ARCADE_camera_constraints_contact_sheet_v001.jpg`

Validation:

- Image count: 7
- Resolution: `1672x941`
- Nonblank check: pass
- Minimum visible projected faces: 110
- Panel mapping count: 39 SCN_ARCADE panels, `MSB019` through `MSB057`
- Formal prompt pack count: 39 SCN_ARCADE panels, all marked `ready_for_formal_generation_with_mother_style_and_whitebox_space`

Usage rule:

For formal image generation, pair each panel's mapped `constraint_whitebox_path` with the mother style image. Keep the dirty plastic entrance strips, low ceiling, two cramped CRT cabinet rows, rear two-player fictional fighting cabinet, stools, warm bulb, fan/wires, and wall scars consistent across every frame. Use only fictional arcade screen graphics with genre-level 1990s beat-em-up/fighting/shooter energy; do not use real game names, logos, UI, or recognizable characters.
