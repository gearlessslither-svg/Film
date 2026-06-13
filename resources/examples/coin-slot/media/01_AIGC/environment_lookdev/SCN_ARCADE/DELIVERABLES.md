> 双语说明 / Bilingual note: 本文件保留英文原文，以避免破坏提示词、文件名、路径、字段名和脚本读取。中文使用时请把它视为生产记录、规则、索引或提示词资产；英文正文为可执行/可追溯原文。 / The English source text is preserved to keep prompts, filenames, paths, field names, and script parsing stable. Treat this as a production record, rule, index, or prompt asset; the English body is the executable and traceable source text.

# SCN_ARCADE Delivery Index

## Selected Mother Image

- `SCN_ARCADE_lookdev_A_entrance_wide_v002_game_screens.png`

## Visual Constraint Whitebox Preview

- `whitebox_obj/SCN_ARCADE_visual_constraint_compare_v001.jpg`
- `whitebox_obj/SCN_ARCADE_visual_constraint_whitebox_2d_v001.png`
- `whitebox_obj/SCN_ARCADE_visual_constraint_overlay_v001.png`

## Blender-Importable Geometry

- `whitebox_obj/SCN_ARCADE_mother_visual_constraint_whitebox_v001.obj`
- `whitebox_obj/SCN_ARCADE_mother_visual_constraint_whitebox_v001.mtl`

## Camera And Asset Locks

- `whitebox_obj/SCN_ARCADE_mother_camera_lock_v001.json`
- `whitebox_obj/SCN_ARCADE_scene_asset_design_list_v001.csv`
- `whitebox_obj/README.md`

## Derived Camera Whiteboxes

- `camera_whiteboxes_v001/SCN_ARCADE_camera_constraints_contact_sheet_v001.jpg`
- `camera_whiteboxes_v001/SCN_ARCADE_camera_constraint_manifest_v001.csv`
- `camera_whiteboxes_v001/SCN_ARCADE_camera_constraint_manifest_v001.json`
- `camera_whiteboxes_v001/SCN_ARCADE_panel_camera_constraint_map_v001.csv`
- `camera_whiteboxes_v001/SCN_ARCADE_formal_storyboard_prompt_pack_v001.csv`
- `camera_whiteboxes_v001/SCN_ARCADE_formal_storyboard_prompt_pack_v001.md`
- `camera_whiteboxes_v001/SCN_ARCADE_camera_constraints_validation_v001.json`
- `camera_whiteboxes_v001/README.md`

Generated constraint cameras:

- `camera_whiteboxes_v001/CAM_ARCADE_01_ENTRANCE_WIDE_constraint_whitebox_v001.png`
- `camera_whiteboxes_v001/CAM_ARCADE_01_CHILD_POV_CENTER_constraint_whitebox_v001.png`
- `camera_whiteboxes_v001/CAM_ARCADE_02_STREET_FIGHTER_CABINET_constraint_whitebox_v001.png`
- `camera_whiteboxes_v001/CAM_ARCADE_03_DUEL_OVER_SHOULDER_constraint_whitebox_v001.png`
- `camera_whiteboxes_v001/CAM_ARCADE_04_BOSS_LOSES_REACTION_constraint_whitebox_v001.png`
- `camera_whiteboxes_v001/CAM_ARCADE_DETAIL_CONTROL_PANEL_constraint_whitebox_v001.png`
- `camera_whiteboxes_v001/CAM_ARCADE_CEILING_PRESSURE_constraint_whitebox_v001.png`

Validation summary:

- 7/7 camera whiteboxes generated at `1672x941`.
- Nonblank validation passed.
- Minimum visible projected faces: 110.
- Panel map covers 39 SCN_ARCADE panels, `MSB019` through `MSB057`.
- Formal prompt pack covers 39 SCN_ARCADE panels and keeps mother style + whitebox space references explicit per row.

## Blender Crash Diagnosis

- `BLENDER_MACOS_CRASH_NOTES.md`

## Next Step

Use `camera_whiteboxes_v001/SCN_ARCADE_panel_camera_constraint_map_v001.csv` for formal SCN_ARCADE image generation. Pair the mapped whitebox with the selected mother image for each panel. Open Blender GUI and import the OBJ only when manual 3D refinement is needed; Blender CLI/headless automation is currently blocked on this Mac by the Metal startup crash.
