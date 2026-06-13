#!/usr/bin/env python3
"""Seed projects/coin-slot with a representative standardized sample batch."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path


SAMPLE_PANEL_IDS = [
    "MSB001",
    "MSB003",
    "MSB006",
    "MSB009",
    "MSB012",
    "MSB019",
    "MSB020",
    "MSB025",
    "MSB058",
    "MSB066",
    "MSB074",
    "MSB085",
]

SHOT_COLUMNS = [
    "shot_id",
    "sequence",
    "story_beat",
    "duration_sec",
    "aspect_ratio",
    "location",
    "character_stage_lock",
    "start_frame",
    "end_frame",
    "camera",
    "action",
    "lighting",
    "continuity_lock",
    "prompt_path",
    "status",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def index_by(rows: list[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    return {row.get(key, ""): row for row in rows}


def write_text(path: Path, text: str, *, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def write_csv(path: Path, rows: list[dict[str, str]], columns: list[str], *, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
    return True


def build_prompt_doc(panel: dict[str, str], prompt: dict[str, str]) -> str:
    return f"""# {panel['panel_id']} Image Prompt

## Shot Function

- Clip: {panel.get('clip')} / {panel.get('clip_title')}
- Beat: {panel.get('beat')}
- Camera: {panel.get('camera')}
- Shot size: {panel.get('shot_size')}

## Pure Image Prompt

{prompt.get('pure_prompt', panel.get('image_prompt_focus', ''))}

## Negative Prompt

{prompt.get('negative_prompt', panel.get('avoid', ''))}

## Spatial Lock

{prompt.get('spatial_lock', '')}
"""


def build_video_prompt_doc(panel: dict[str, str], prompt: dict[str, str]) -> str:
    return f"""# {panel['panel_id']} Video Prompt

## Motion Intent

{panel.get('pose_motion_note', '')}

## Start State

{panel.get('image_prompt_focus', '')}

## Character / Performance

{panel.get('character_focus', '')}
{panel.get('expression_note', '')}

## Camera

{panel.get('camera', '')}; {panel.get('shot_size', '')}

## Continuity

{prompt.get('story_stage', '')} / {prompt.get('stage_name', '')}
{panel.get('continuity_anchor', '')}

## Avoid

{panel.get('avoid', '')}
"""


def seed_project(project: Path, resources: Path, *, force: bool) -> dict[str, object]:
    csv_root = resources / "csv"
    panels = index_by(read_csv(csv_root / "19_micro_storyboard_188_panels.csv"), "panel_id")
    prompts = index_by(read_csv(csv_root / "micro_storyboard_pure_image_prompts.csv"), "panel_id")
    stage_map = index_by(read_csv(csv_root / "panel_stage_state_map.csv"), "panel_id")

    selected = [panels[panel_id] for panel_id in SAMPLE_PANEL_IDS if panel_id in panels]
    shot_rows = []
    camera_rows = []
    written = []
    skipped = []

    for panel in selected:
        panel_id = panel["panel_id"]
        prompt = prompts.get(panel_id, {})
        stage = stage_map.get(panel_id, prompt)
        prompt_rel = f"07_shots/prompts/{panel_id}.md"
        video_prompt_rel = f"07_shots/video_prompts/{panel_id}.md"

        shot_rows.append(
            {
                "shot_id": panel_id,
                "sequence": panel.get("clip", ""),
                "story_beat": panel.get("beat", ""),
                "duration_sec": "2.0",
                "aspect_ratio": "16:9",
                "location": prompt.get("scene_id", panel.get("clip_title", "")),
                "character_stage_lock": stage.get("character_stage_lock", ""),
                "start_frame": stage.get("whitebox_reference_path", ""),
                "end_frame": prompt.get("pure_path", ""),
                "camera": panel.get("camera", ""),
                "action": panel.get("pose_motion_note", ""),
                "lighting": "1990s damp night, CRT blue-green practicals, warm street spill, low-key realism",
                "continuity_lock": f"{stage.get('story_stage', '')}: {panel.get('continuity_anchor', '')}",
                "prompt_path": prompt_rel,
                "status": "sample_ready",
            }
        )
        camera_rows.append(
            {
                "shot_id": panel_id,
                "camera": panel.get("camera", ""),
                "shot_size": panel.get("shot_size", ""),
                "whitebox_reference_path": stage.get("whitebox_reference_path", ""),
                "spatial_lock": prompt.get("spatial_lock", ""),
                "blocking": panel.get("image_prompt_focus", ""),
                "movement": panel.get("pose_motion_note", ""),
            }
        )

        for rel_path, text in (
            (prompt_rel, build_prompt_doc(panel, prompt)),
            (video_prompt_rel, build_video_prompt_doc(panel, prompt)),
        ):
            if write_text(project / rel_path, text, force=force):
                written.append(rel_path)
            else:
                skipped.append(rel_path)

    if write_csv(project / "07_shots" / "shot_list.csv", shot_rows, SHOT_COLUMNS, force=force):
        written.append("07_shots/shot_list.csv")
    else:
        skipped.append("07_shots/shot_list.csv")

    if write_csv(
        project / "06_previs" / "camera_manifests" / "coin_slot_sample_camera_manifest.csv",
        camera_rows,
        ["shot_id", "camera", "shot_size", "whitebox_reference_path", "spatial_lock", "blocking", "movement"],
        force=force,
    ):
        written.append("06_previs/camera_manifests/coin_slot_sample_camera_manifest.csv")
    else:
        skipped.append("06_previs/camera_manifests/coin_slot_sample_camera_manifest.csv")

    docs = {
        "00_admin/director_brief.md": """# Director Brief

## 核心点子

- 三个孩子在潮湿旧居民楼里发现隐藏街机厅，投币行为像一次进入童年记忆和危险空间的仪式。

## 必须保留

- 1990s 中国小城旧居民楼、潮湿墙面、CRT 蓝绿光、街机厅、孩子之间的保护/犹豫/好奇。

## 可以探索

- 投币口作为神秘入口、游戏声与现实空间互相污染、离开街机厅后的巷道对峙。

## 禁止方向

- 现代商业街、明亮潮流店、成人英雄化暴力、过度血腥、现代手机和现代车辆。
""",
        "01_intake/analysis/linked_resource_summary.md": """# Linked Resource Summary

The standardized project links to `resources/examples/coin-slot`, which contains the historical Coin Slot production archive: 188 micro-storyboard rows, whitebox manifests, prompt tables, audio manifests, contact sheets, videos, WAV assets, Blender files, and delivery packages.

This sample seed imports a 12-shot representative batch into the standard project folder while keeping large media in the LFS resource archive.
""",
        "01_intake/source_inputs/coin_slot_source_inputs_index.md": """# Source Inputs Index

- Original project root: `E:\\视觉\\投币口`
- Curated archive: `resources/examples/coin-slot`
- Primary production tables: `resources/examples/coin-slot/csv/`
- Historical documents: `resources/examples/coin-slot/docs/`
""",
        "01_intake/references/coin_slot_reference_index.md": """# Reference Index

- Final contact sheets: `resources/examples/coin-slot/media/01_AIGC/final_storyboard_contact_sheets/`
- Final storyboard video: `resources/examples/coin-slot/media/01_AIGC/exports/final_video/`
- Whitebox manifests: `resources/examples/coin-slot/blender/`
- Audio cues and WAV assets: `resources/examples/coin-slot/media/01_AIGC/audio/`
""",
        "02_direction/creative_brief.md": """# Creative Brief

## 最终方向

- 中国 90 年代旧居民楼里的儿童惊奇/悬疑短片，视觉核心是潮湿夜景、街机蓝绿光、窄巷空间和孩子之间的保护关系。

## 故事大纲

- 旧小区建立。
- 三个孩子被街机厅的 CRT 光吸引。
- 进入街机厅，投币和游戏声唤起危险感。
- 离开街机厅，巷道空间转为对峙和心理压力。

## 美术风格

- Photoreal Chinese dreamcore realism, restrained VHS grain, worn 1990s clothes, damp concrete, low-key practical light.

## 角色 / 场景 / 道具优先级

- 三兄弟角色状态锁。
- 旧居民楼入口、街机厅、窄巷。
- 街机按钮、投币口、CRT 屏幕光、破自行车、潮湿地面。

## 确认记录

- Sample direction seeded from the archived Coin Slot AIGC production resources; director confirmation still required before new full-batch generation.
""",
        "02_direction/options/coin_slot_direction_options.md": """# Direction Options

## Option A - Damp Childhood Mystery

The current seeded direction. Emphasize old residential texture, CRT temptation, child curiosity, and low-key suspense.

## Option B - Arcade Dream Logic

Lean further into subjective memory, stronger game-screen contamination, and more stylized sound/image transitions.

## Option C - Realist Coming-Of-Age Tension

Reduce supernatural feeling and focus on children, hierarchy, fear, and the alley confrontation.

Recommended sample path: Option A, with controlled traces of Option B only inside the arcade.
""",
        "02_direction/approvals/provisional_direction_lock.md": """# Provisional Direction Lock

Status: sample lock for toolkit testing.

Locked for this sample batch:

- Location: old residential compound, hidden arcade, wet exit alley.
- Look: photoreal Chinese dreamcore realism, damp concrete, CRT blue-green practicals, restrained VHS grain.
- Characters: three child brothers in stage-specific states.
- Production method: AIGC-first with whitebox/control-layer support.

Requires human director confirmation before full production expansion.
""",
        "03_story/beats/coin_slot_sample_beat_sheet.md": "\n".join(
            ["# Coin Slot Sample Beat Sheet", ""]
            + [
                f"- {row['panel_id']} / Clip {row.get('clip')} / {row.get('clip_title')}: {row.get('beat')}"
                for row in selected
            ]
        ),
        "03_story/outlines/coin_slot_outline.md": """# Coin Slot Outline

Three brothers drift through an old residential compound at night and notice a hidden arcade glowing from a ground-floor doorway. The arcade feels ordinary at first, then strangely ritualistic: buttons, coins, CRT light, and game sounds pull the children deeper into the room. When they leave, the exterior alley no longer feels neutral; the space tightens into a standoff where the older brother's protective role becomes visible.
""",
        "03_story/scripts/coin_slot_sample_script.md": """# Sample Script Notes

This seeded batch is designed as a low-dialogue visual sequence.

- Exterior: silence, wet footsteps, distant room tone.
- Threshold: CRT hum leaks through the doorway.
- Arcade: coin, button taps, cabinet drones, children's breath and small reactions.
- Exit: sound thins out; footsteps and street ambience become threatening.

Dialogue should be sparse and childlike. Avoid exposition.
""",
        "04_lookdev/palettes/coin_slot_color_script.md": """# Coin Slot Color Script

- Exterior compound: wet yellowed concrete, low sodium warmth, black-green shadows.
- Arcade threshold: CRT blue-green spill leaks through doors and glass.
- Interior arcade: saturated cyan, green, red machine accents against old brown walls.
- Exit/standoff: warm street spill returns, but cyan memory remains in windows and reflections.

Forbidden drift: clean mall lighting, glossy neon cyberpunk, pure blue monochrome, modern LED signage.
""",
        "04_lookdev/styleframes/coin_slot_styleframe_index.md": """# Styleframe Index

Representative linked styleframes:

- `resources/examples/coin-slot/media/01_AIGC/final_storyboard_contact_sheets/B01_final_storyboard_contact_sheet_v002.jpg`
- `resources/examples/coin-slot/media/01_AIGC/final_storyboard_contact_sheets/B03_final_storyboard_contact_sheet_v002.jpg`

Use these as review sheets, not direct generation inputs. Individual pure frames remain in the linked LFS archive.
""",
        "04_lookdev/lighting/coin_slot_lighting_rules.md": """# Coin Slot Lighting Rules

- Light must be motivated by practical sources: CRT screens, arcade cabinets, corridor bulbs, street lamps, window spill.
- Keep contrast low-key but preserve child silhouettes and face readability.
- Wet ground reflections are a continuity anchor.
- Blue-green CRT light marks temptation and memory; warm street light marks the real exterior world.
""",
        "04_lookdev/references/coin_slot_visual_references.md": """# Visual References

Internal references are drawn from the completed Coin Slot sample archive:

- Wet exterior compound.
- Hidden ground-floor game room.
- CRT-lit arcade cabinets.
- Long exit alley with warm practical lamps.
- Child group silhouettes and stage-specific body tension.
""",
        "05_asset_bible/characters/coin_slot_character_bible.md": """# Character Bible

## Older Brother

Tall, thin metal-frame glasses, blue worn tracksuit, protective posture, often leads the group.

## Middle Boy

Round eyes, red scarf, blue school jacket, green schoolbag, alert and emotionally readable.

## Youngest Boy

Smaller, rounder body, timid eyes, pale shirt or warm vest, close to the others when afraid.

The three must remain readable as children and distinct at thumbnail size.
""",
        "05_asset_bible/character_stage_locks/coin_slot_character_stage_locks.md": """# Character Stage Locks

- S0_START_CLEAN: three brothers are clean, curious, cautious; no mud, injury, or fight damage.
- S1_ARCADE_PLAY: faces lit by CRT blue-green light; attention pulled toward machines and buttons.
- S2_EXIT_TO_STANDOFF: body tension rises; older brother becomes protective, younger children cluster behind or beside him.

Identity locks:

- Older brother: tall, thin metal-frame glasses, blue worn tracksuit, protective posture.
- Middle boy: round eyes, red scarf, blue school jacket, green schoolbag, often gripping straps.
- Youngest boy: smaller round body, timid eyes, pale shirt or warm vest, inward toes.
""",
        "05_asset_bible/locations/coin_slot_location_bible.md": """# Location Bible

- Old residential compound: yellowed concrete, damp ground, weeds, hidden ground-floor door, broken bicycle.
- Arcade room: cramped, old cabinets, CRT glow, worn controls, dusty air, low ceiling.
- Exit alley: long wet corridor, walls close in, sparse warm lamps, strong screen direction and silhouettes.
""",
        "05_asset_bible/props/coin_slot_prop_bible.md": """# Prop Bible

- Coin slot: ritual object and story trigger; should feel worn, tactile, slightly mysterious.
- Arcade buttons: colored, scratched, oily, close-up friendly.
- CRT cabinets: blue-green/red glow, old casing, imperfect reflections.
- Broken bicycle and damp ground: exterior continuity anchors.
""",
        "05_asset_bible/continuity/coin_slot_continuity_locks.md": """# Continuity Locks

- Wet ground reflections persist across compound and alley.
- CRT blue-green light marks arcade proximity.
- Older brother remains the tallest silhouette and protective anchor.
- Middle boy's red scarf and green schoolbag remain visible unless blocked by staging.
- Screen direction from compound entrance to arcade and exit alley must remain deliberate.
- No modern phones, cars, clean malls, or LED shop signage.
""",
        "06_previs/blender/coin_slot_blender_index.md": """# Blender Index

Linked source:

- `resources/examples/coin-slot/blender/coin_slot_whitebox.blend`
- `resources/examples/coin-slot/blender/whitebox_v2_manifest.csv`

Next refinement: create or copy the 12-shot whitebox scene/control set into this standard project folder when the sample batch becomes production-active.
""",
        "06_previs/qa/coin_slot_previs_notes.md": """# Previs Notes

The seed batch references archived whitebox paths from `resources/examples/coin-slot`. Next previs pass should copy or regenerate a 12-shot control layer set under `06_previs/control_layers/` and verify:

- screen direction from compound to arcade and alley,
- child scale against doors, cabinets, and walls,
- foreground occlusion in narrow corridors,
- consistent camera height and lens logic.
""",
        "06_previs/renders/coin_slot_whitebox_render_index.md": """# Whitebox Render Index

Whitebox render paths are referenced by `06_previs/camera_manifests/coin_slot_sample_camera_manifest.csv` and the seeded `07_shots/shot_list.csv`.

Current linked root: `resources/examples/coin-slot/media/01_AIGC/whitebox_renders_v2/`
""",
        "06_previs/control_layers/coin_slot_control_layer_index.md": """# Control Layer Index

For this sample batch, whitebox references are registered as the active spatial control source. Future production passes should add generated depth, line, normal, and segmentation layers here per `shot_id`.
""",
        "07_shots/keyframes/coin_slot_keyframe_index.md": """# Keyframe Index

The seeded 12-shot batch points to linked pure frame paths in `07_shots/shot_list.csv`.

Representative review contact sheets:

- `resources/examples/coin-slot/media/01_AIGC/final_storyboard_contact_sheets/B01_final_storyboard_contact_sheet_v002.jpg`
- `resources/examples/coin-slot/media/01_AIGC/final_storyboard_contact_sheets/B03_final_storyboard_contact_sheet_v002.jpg`
""",
        "10_qa/fix_queue/coin_slot_next_batch_fix_queue.md": """# Next Batch Fix Queue

| Priority | Stage | Task |
| --- | --- | --- |
| P0 | 06_previs | Regenerate/refine 12-shot whitebox control layers inside the standard project folder. |
| P0 | 07_shots | Review the seeded 12 shot rows and confirm director-approved shot purpose. |
| P1 | 04_lookdev | Create 3 styleframes from the linked contact sheets and lock color/lighting rules. |
| P1 | 09_edit | Build a 12-shot audio cue sheet covering CRT hum, coin, buttons, footsteps, ambience, and silence. |
""",
        "08_generation/jobs/coin_slot_12shot_generation_plan.md": """# 12-Shot Generation Plan

Scope: seeded 12-shot sample batch from `07_shots/shot_list.csv`.

Inputs:

- image prompts: `07_shots/prompts/`
- video prompts: `07_shots/video_prompts/`
- camera manifest: `06_previs/camera_manifests/coin_slot_sample_camera_manifest.csv`
- linked historical outputs: `resources/examples/coin-slot/media/01_AIGC/`

Policy:

- keep pure outputs separate from annotated review copies,
- record model, seed, reference paths, control paths, and failure reasons per shot,
- do not overwrite linked archive media.
""",
        "08_generation/outputs/images/coin_slot_image_outputs_index.md": """# Image Outputs Index

The sample batch uses linked historical pure/annotated image outputs from:

- `resources/examples/coin-slot/media/01_AIGC/visual_assets/`
- `resources/examples/coin-slot/media/01_AIGC/final_storyboard_contact_sheets/`

Future regenerated outputs should be written here or indexed here by `shot_id`.
""",
        "08_generation/outputs/video/coin_slot_video_outputs_index.md": """# Video Outputs Index

Linked review videos:

- `resources/examples/coin-slot/media/01_AIGC/exports/animatic/coin_slot_storyboard_animatic_v001.mp4`
- `resources/examples/coin-slot/media/01_AIGC/exports/final_video/coin_slot_final_storyboard_video_v002.mp4`

Future AIGC clip outputs should be indexed here by `shot_id` and generation job.
""",
        "08_generation/rejects/coin_slot_reject_log.md": """# Reject Log

| Shot | Issue | Cause | Fix |
| --- | --- | --- | --- |
| TBD | No active rejects in the seeded sample. | Historical outputs are linked for review. | Add rows during regenerated batches. |
""",
        "09_edit/rough_cut/coin_slot_12shot_timing_plan.md": """# 12-Shot Timing Plan

The seeded sample uses 12 representative shots at roughly 2 seconds each. Timing should be revised after director review:

- establish exterior silence,
- let CRT hum pull attention at the threshold,
- compress arcade detail into tactile inserts,
- slow down exit/standoff shots for tension.
""",
        "09_edit/audio/coin_slot_12shot_audio_cue_sheet.csv": """shot_id,cue_type,cue,notes
MSB001,ambience,compound night bed,wet exterior silence
MSB003,sound_design,CRT leak,blue-green doorway pull
MSB006,sound_design,arcade light flicker,small colored reflections
MSB019,ambience,arcade room tone,interior cabinet drone
MSB020,sound_design,CRT cabinet hum,threshold silhouette
MSB025,foley,arcade buttons,worn tactile close-up
MSB058,ambience,exit exterior bed,warm street spill
MSB066,foley,wet footsteps,long alley scale
MSB074,performance,breath and pause,child reaction close-up
MSB085,sound_design,distant arcade memory,offscreen tension
""",
        "09_edit/subtitles/coin_slot_subtitle_notes.md": """# Subtitle Notes

The seeded sample is designed as a low-dialogue sequence. Use subtitles only for essential child speech or system/game text if the director later adds it. Avoid explanatory captions inside generated frames.
""",
        "09_edit/color/coin_slot_color_pass_notes.md": """# Color Pass Notes

Preserve the exterior warm/cool split and CRT blue-green memory color. Avoid pushing the sample toward clean cyberpunk neon or flat monochrome blue.
""",
        "11_delivery/exports/coin_slot_delivery_exports_index.md": """# Delivery Exports Index

Linked final review exports:

- `resources/examples/coin-slot/media/01_AIGC/exports/final_video/coin_slot_final_storyboard_video_v002.mp4`
- `resources/examples/coin-slot/media/01_AIGC/exports/final_video/coin_slot_final_storyboard_video_v002_silent.mp4`
""",
        "11_delivery/packages/coin_slot_package_index.md": """# Delivery Package Index

Linked packages:

- `resources/examples/coin-slot/media/01_AIGC/exports/coin_slot_final_storyboard_audio_video_v002_review_package.zip`
- `resources/examples/coin-slot/media/01_AIGC/exports/coin_slot_aigc_overnight_package.zip`
""",
        "11_delivery/manifests/coin_slot_sample_delivery_manifest.md": """# Sample Delivery Manifest

This standardized project folder does not duplicate heavy media. Final review video, contact sheets, WAV assets, Blender files, and zip packages remain in the linked Git LFS resource archive.

Use `assets_link_map.md` and the delivery index files in this folder to locate source assets.
""",
    }

    for rel_path, text in docs.items():
        if write_text(project / rel_path, text, force=force):
            written.append(rel_path)
        else:
            skipped.append(rel_path)

    log = project / "00_admin" / "project_log.md"
    log_entry = f"| {datetime.now().strftime('%Y-%m-%d')} | sample_seed | Seeded 12-shot Coin Slot representative batch. | AI | scripts/seed_coin_slot_sample_project.py |\n"
    if log.exists():
        current = log.read_text(encoding="utf-8")
        if "sample_seed" not in current or force:
            log.write_text(current.rstrip() + "\n" + log_entry, encoding="utf-8", newline="\n")
            written.append("00_admin/project_log.md")

    return {"project": str(project), "written": written, "skipped": skipped, "sample_rows": len(shot_rows)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Seed the Coin Slot standardized sample project.")
    parser.add_argument("--project", default="projects/coin-slot")
    parser.add_argument("--resources", default="resources/examples/coin-slot")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    result = seed_project(Path(args.project), Path(args.resources), force=args.force)
    print(f"project={result['project']}")
    print(f"sample_rows={result['sample_rows']}")
    print(f"written={len(result['written'])}")
    print(f"skipped={len(result['skipped'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
