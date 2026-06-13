> 双语说明 / Bilingual note: 本文件保留英文原文，以避免破坏提示词、文件名、路径、字段名和脚本读取。中文使用时请把它视为生产记录、规则、索引或提示词资产；英文正文为可执行/可追溯原文。 / The English source text is preserved to keep prompts, filenames, paths, field names, and script parsing stable. Treat this as a production record, rule, index, or prompt asset; the English body is the executable and traceable source text.

# Project Structure Template

```text
project_name/
  project_manifest.json
  audio/
    song.wav
  configs/
    director_bible.json
    character_bible.json
    environment_spatial_bible.json
    frame_continuity_manifest.json
    asset_integrity_report.json
    story_section_map.json
    frame_profile.json
    effect_catalog.json
    edit_render_plan.json
    audio_analysis.json
    sequencer_config.json
    whitebox_workflow_policy.md
  prompts/
    visual_bible.md
    reference_sheet_prompts.json
    storyboard_frame_prompts.json
    video_prompt_pack.json
    negative_constraints.md
  reference_images/
    original_inputs/
    generated_bible_refs/
    style_tests/
  character_refs/
  environment_refs/
  blender/
    whitebox_generator.py
    camera_manifest.csv
  whitebox_renders/
  video_frames/
    frame_001.png
    frame_002.png
    module_NAME_001.png
    _whitebox_proxy_story/
    _placeholder_from_reference/
    _discarded_continuity_candidates/
  modules/
  remotion/
  scripts/
  exports/
```

## Folder Rules

- `audio/`: only approved project music. Automatic renderers should ignore root-level audio.
- `video_frames/`: only frames intended for video editing.
- `video_frames/_whitebox_proxy_story/`: temporary Blender/layout blocking previews. They are never counted as finished story frames.
- `video_frames/_placeholder_from_reference/`: preview placeholders copied from reference/fallback images. They are never counted as finished story frames.
- `video_frames/_discarded_continuity_candidates/`: visually useful images that failed continuity, camera, or asset-integrity QA.
- `reference_images/`, `character_refs/`, `environment_refs/`: references only, not automatic video assets.
- `whitebox_renders/`: Blender camera reference images, not final art.
- `configs/`: source of truth for the editor and renderer.
- `exports/`: generated videos, screenshots, contact sheets, and verification artifacts.
- Contact sheets should be split by layer: whitebox cameras, visual anchors, final story frames, and placeholders/rejected assets.

## Naming Rules

- `frame_###.png`: global story order.
- `story_###.png`: global story order.
- `module_NAME_###.png`: ordered local module.
- `shot_NAME_###.png`: ordered local shot group.
- unnumbered images: aesthetic pool unless manifest says otherwise.
- A numbered story filename is not proof of completion. Run `asset_integrity_report.json` checks before using it as a final story asset.
- A whitebox or proxy preview filename is never proof of final art. If it keeps the edit working, classify it as `whitebox_proxy_only` until regenerated as final story art.
