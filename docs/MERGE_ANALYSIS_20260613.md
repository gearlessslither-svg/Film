# Story / Film Merge Analysis - 2026-06-13

Observation time: 2026-06-13 22:25:55 +0800

## Scope

- Remote repository: `gearlessslither-svg/Film`
- Local sources compared:
  - `Story/投币口/`
  - `Story/NEW_PROJECT_COPY_PACK_v1/`
- Unrelated local app projects in `Story/` were not merged.
- `.rar`, `.DS_Store`, `__pycache__`, `.pyc`, and `.blend1` backup files were excluded.

## What Was Already Covered By Remote

- Standard project layout under `projects/coin-slot/`.
- Reusable toolkit layout under `skills/`, `scripts/`, `apps/pipeline-hub/`, and `resources/examples/coin-slot/`.
- Final-delivery mainline records, including final storyboard/video/audio references and completed pure-panel production status.
- Existing LFS archive for most images, audio, video, Blender files, and zip deliverables.

## Complementary Local Content Added

- Arcade scene lookdev and spatial-control assets:
  - `resources/examples/coin-slot/media/01_AIGC/environment_lookdev/`
  - `scripts/visual/build_arcade_obj_whitebox.py`
  - `scripts/visual/build_arcade_camera_whiteboxes.py`
  - `scripts/visual/build_arcade_formal_prompt_pack.py`
  - `scripts/blender/create_arcade_mother_whitebox.py`
  - `scripts/blender/import_arcade_mother_obj.py`
- Camera/subject logic and three-brother reference locks:
  - `resources/examples/coin-slot/docs/aigc/34_camera_subject_logic_rules.md`
  - `resources/examples/coin-slot/media/01_AIGC/character_design_v2/THREE_BROTHERS_*`
- 15-second SCN_ARCADE opening long-take package:
  - `resources/examples/coin-slot/media/01_AIGC/long_take_design/`
- Local B01 v002/v003 candidate and rejected assets:
  - `resources/examples/coin-slot/media/01_AIGC/visual_assets/pure/micro_storyboard/B01/*_v002.png`
  - `resources/examples/coin-slot/media/01_AIGC/visual_assets/rejected/`
- Reusable new-project copy pack:
  - `resources/examples/coin-slot/configs/`
  - `resources/examples/coin-slot/docs/new-project-copy-pack/`

## Mainline Updates

- Restored local production constraints into the AIGC rules:
  - video character-load limits,
  - prop causality locks,
  - actual image-based whitebox use,
  - camera/subject/gaze/movement logic.
- Added macOS Chinese font fallbacks back to `scripts/visual/annotate_visual_asset.py`.

## Conflicts Kept Separate

Some local CSVs were semantically different from the remote mainline. The remote versions looked like the more current completed-production records, while the local versions preserved v002/v003 planning and some partially corrupted text fields. These were not allowed to overwrite mainline CSVs.

Conflict snapshots are stored at:

```text
resources/examples/coin-slot/local-story-20260613/csv/
```

The current mainline remains:

```text
resources/examples/coin-slot/csv/
```

## Not Merged

- `投币口0522.rar` and any `.rar` backup package.
- Unrelated local projects such as `ai-invest-copilot`, `personal-finance-hub`, `director-training-lab`, and `mullvad-speed-guard`.
- Local `.blend1` backup files.
