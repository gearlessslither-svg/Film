# SCN_ARCADE Mother Visual Constraint Whitebox v001

Source mother image:

- `../SCN_ARCADE_lookdev_A_entrance_wide_v002_game_screens.png`

Generated files:

- `SCN_ARCADE_mother_visual_constraint_whitebox_v001.obj`
- `SCN_ARCADE_mother_visual_constraint_whitebox_v001.mtl`
- `SCN_ARCADE_mother_camera_lock_v001.json`
- `SCN_ARCADE_scene_asset_design_list_v001.csv`
- `SCN_ARCADE_visual_constraint_whitebox_2d_v001.png`
- `SCN_ARCADE_visual_constraint_overlay_v001.png`
- `SCN_ARCADE_visual_constraint_compare_v001.jpg`

Purpose:

- Treat the selected game-room mother image as the design source of truth.
- Lock major spatial DNA: dirty plastic entrance curtain, low ceiling, narrow wet aisle, left/right CRT cabinet banks, rear double fighting-game cabinet, stools, central bulb, ceiling fan/wires, wall scars/poster masses.
- Use this OBJ as the first proxy scene for deriving later camera-specific whiteboxes.

Blender import:

1. Open Blender GUI.
2. Import `SCN_ARCADE_mother_visual_constraint_whitebox_v001.obj`.
3. Create a camera named `CAM_SCN_ARCADE_MOTHER_MATCH`.
4. Use `SCN_ARCADE_mother_camera_lock_v001.json` for the suggested camera position, look-at point, focal length, and resolution.

Known limit:

- Blender 5.1.2 macOS CLI currently crashes on this machine during Metal/GPU initialization before Python execution. Until that is fixed, use GUI import for this OBJ.
