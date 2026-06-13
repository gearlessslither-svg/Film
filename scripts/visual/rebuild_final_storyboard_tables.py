#!/usr/bin/env python3
"""Rebuild clean final storyboard generation tables.

The previous stage/prompt CSVs can become unusable if a shell/codepage step
turns Chinese continuity text into long runs of question marks. This script
keeps the 188-panel plan as the source of truth, rebuilds compact stage locks,
and refreshes the pure-image prompt and real-image queue tables.
"""

from __future__ import annotations

import csv
import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class StageRule:
    start: int
    end: int
    stage_id: str
    stage_name: str
    character: str
    wardrobe: str
    emotion: str
    environment: str


STAGES = [
    StageRule(
        1,
        18,
        "S0_START_CLEAN",
        "opening clean state",
        "The three brothers are ordinary children, curious and only slightly tense; no fight damage yet.",
        "Old 1990s school clothes, worn but clean; red scarf, green schoolbag, old shoes, no mud or injury.",
        "Curious, cautious, attracted by the hidden arcade light.",
        "Damp old residential compound, yellowed concrete, hidden ground-floor game room, children still clean.",
    ),
    StageRule(
        19,
        57,
        "S1_ARCADE_PLAY",
        "arcade play and humiliation",
        "The brothers are absorbed by the arcade; Binzi shifts from swagger to humiliation.",
        "Children remain clean; CRT light changes color on clothes; bully clothes can be sweaty, not muddy.",
        "Excited play turning into status pressure and embarrassment.",
        "Low-ceiling hidden arcade, CRT glow, smoke haze, plastic curtain, cramped machine rows.",
    ),
    StageRule(
        58,
        85,
        "S2_EXIT_TO_STANDOFF",
        "exit and danger premonition",
        "Happy afterglow drains away; the brothers sense danger before the alley blockade.",
        "The brothers are still mostly clean; clothes can wrinkle and bags can swing, but no fight dirt.",
        "The mood shifts from pride to alertness and unease.",
        "Arcade exit to damp secluded path; warm door light falls behind them, shadows begin to appear.",
    ),
    StageRule(
        86,
        97,
        "S3_ALLEY_PRESSURE",
        "alley pressure",
        "A Lei tries to hold himself together; Xiao Chuan shrinks back; Xiao Man freezes.",
        "Clothes start to wrinkle and catch a little wall dust; still not fully dirty.",
        "Pressure, shame, fear, and trapped breathing.",
        "Secluded alley compresses the group; wet ground, wall, weeds, broken brick and old streetlight.",
    ),
    StageRule(
        98,
        107,
        "S4_STONE_ACCIDENT",
        "stone accident",
        "Xiao Chuan panics and acts without heroism; A Lei is being squeezed by the group.",
        "Xiao Chuan's hand, knee, shoe edge, scarf, and bag start to become wet or muddy.",
        "Panic, loss of control, shock after impact.",
        "Wet ground and roadside stone become the visual center; violence is hidden and de-glorified.",
    ),
    StageRule(
        108,
        119,
        "S5_ESCAPE_DIRTY",
        "escape dirty state",
        "Xiao Chuan runs in panic with broken breath; he is not brave, only frightened.",
        "Xiao Chuan is visibly dirtier: knees, shoes, bag edge and sleeves muddy; clothes crooked.",
        "Breathless fear, tunnel vision, guilt, and flight.",
        "The alley streaks past toward an abandoned building entrance.",
    ),
    StageRule(
        120,
        154,
        "S6_CORRIDOR_PHONE_SHOCK",
        "corridor phone shock",
        "Xiao Chuan enters the abandoned corridor and slows under the phone booth pull.",
        "Carry over the escape dirt: wet gray on face, hands, bag strap and sleeves.",
        "Shock, dissociation, listening, moving as if pulled by the ring.",
        "Cold green corridor, long perspective, fluorescent flicker, warm white phone booth glow.",
    ),
    StageRule(
        155,
        169,
        "S7_PHONE_ELECTRONICIZATION",
        "phone electronicization",
        "Xiao Chuan is pulled into electronicization and pixel slicing.",
        "Keep S6 dirt while adding scanline edges, pixel blocks, and color-channel separation.",
        "Fear becomes blank focus, as if the world is parsing him.",
        "The phone booth stays fixed while the real space flattens into electronic layers.",
    ),
    StageRule(
        170,
        188,
        "S8_8BIT_TRANSLATED",
        "8-bit translated stage",
        "The real characters are translated into side-scrolling arcade rules while identity anchors remain.",
        "Pixel versions retain red scarf, green bag, yellow hair, body-size differences and earlier dirt logic.",
        "Game-rule intensity, mechanical resolve, then empty win-state stillness.",
        "Low-resolution 1990s side-scrolling beat-em-up stage with the phone booth as background anchor.",
    ),
]


IDENTITY_LOCK = (
    "Identity locks: A Lei is the tall older brother with old thin metal-frame glasses, a blue worn tracksuit, "
    "protective posture, and a habit of pushing his glasses. Xiao Chuan is the middle/protagonist boy with round "
    "eyes, a slightly protruding right ear, half-open mouth, red scarf, blue school jacket and green schoolbag, "
    "often gripping the bag straps. Xiao Man is the smallest younger brother with a round head, rounder body, "
    "timid downcast eyes, warm old vest or pale shirt, hands gripping his hem, toes turned inward. Binzi is the "
    "short bully boss with dyed yellow hair and a compact aggressive body. The other three bullies must have "
    "distinct tall-thin, heavy, and errand-runner silhouettes."
)


NEGATIVE_BASE = (
    "No text, no captions, no Chinese characters, no English letters, no labels, no arrows, no diagrams, "
    "no storyboard frame, no contact sheet, no sketch lines, no watermark. Avoid modern phones, modern cars, "
    "LED shop signs, polished mall interiors, fashionable contemporary clothes, glossy advertisement lighting, "
    "heroic violence, gore, blood focus, glamorized fighting, or characters looking like adults."
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def maybe_backup(path: Path) -> None:
    if not path.exists():
        return
    backup = path.with_suffix(path.suffix + ".bak_pre_clean_rebuild")
    if not backup.exists():
        shutil.copy2(path, backup)


def panel_number(panel_id: str) -> int:
    return int(panel_id.replace("MSB", ""))


def stage_for(panel_id: str) -> StageRule:
    number = panel_number(panel_id)
    for stage in STAGES:
        if stage.start <= number <= stage.end:
            return stage
    raise ValueError(f"No stage rule for {panel_id}")


def scene_id(camera: str) -> str:
    camera = camera.upper()
    if "COMPOUND" in camera:
        return "SCN_COMPOUND"
    if "ARCADE_EXIT" in camera:
        return "SCN_ARCADE_EXIT"
    if "ARCADE" in camera:
        return "SCN_ARCADE"
    if "ALLEY" in camera:
        return "SCN_ALLEY"
    if "CORRIDOR" in camera:
        return "SCN_CORRIDOR"
    if "PHONE" in camera:
        return "SCN_PHONE"
    if "8BIT" in camera:
        return "SCN_8BIT"
    return "SCN_UNKNOWN"


def find_whitebox(root: Path, panel_id: str) -> str:
    matches = sorted((root / "whitebox_renders_v2").glob(f"*/WB2_*_{panel_id}.png"))
    if not matches:
        return ""
    return matches[0].relative_to(root).as_posix()


def make_prompt(row: dict[str, str], stage: StageRule, whitebox: str) -> str:
    return " ".join(
        [
            "Create a pure cinematic film still for AIGC video generation, 16:9 landscape, high-resolution,",
            "photoreal Chinese dreamcore realism, 1990s small-town China, humid yellowed childhood memory,",
            "low light, restrained VHS grain, real old clothes, lived-in surfaces, no visible text or annotations.",
            f"Use the whitebox reference for composition and spatial relationship: {whitebox}.",
            f"Panel {row['panel_id']}, Clip {row['clip']} {row['clip_title']}, time {row['approx_time']}.",
            f"Scene lock: {scene_id(row['camera'])}. Camera reference: {row['camera']}. Shot size: {row['shot_size']}.",
            f"Beat: {row['beat']}. Visual focus: {row['image_prompt_focus']}.",
            f"Character focus: {row['character_focus']}. Expression: {row['expression_note']}.",
            f"Blocking and motion: {row['pose_motion_note']}.",
            f"Continuity anchors: {row['continuity_anchor']}.",
            f"Story stage: {stage.stage_id} / {stage.stage_name}.",
            f"Character stage lock: {stage.character}. Wardrobe state: {stage.wardrobe}.",
            f"Emotion state: {stage.emotion}. Environment stage lock: {stage.environment}.",
            IDENTITY_LOCK,
            "The image must look like a final movie frame or clean keyframe, not a storyboard drawing.",
        ]
    )


def make_negative(row: dict[str, str], stage: StageRule) -> str:
    leaks = {
        "S0_START_CLEAN": "Do not show dirty, muddy, injured, post-fight, post-escape, phone-booth, or 8-bit states.",
        "S1_ARCADE_PLAY": "Do not add alley mud, fight injury, corridor lighting, phone booth glow, or 8-bit pixels.",
        "S2_EXIT_TO_STANDOFF": "Do not make the brothers already beaten, muddy, heroic, or inside the abandoned corridor.",
        "S3_ALLEY_PRESSURE": "Do not show the stone impact yet; do not overplay blood, gore, or triumphant violence.",
        "S4_STONE_ACCIDENT": "Keep the impact obscured and panic-based; no gore, no heroic pose, no explicit wound detail.",
        "S5_ESCAPE_DIRTY": "Do not restore Xiao Chuan to clean clothes; do not make the escape look brave or action-heroic.",
        "S6_CORRIDOR_PHONE_SHOCK": "Do not lose the escape dirt; do not return to arcade lighting or show modern phone hardware.",
        "S7_PHONE_ELECTRONICIZATION": "Do not replace identity anchors with generic sci-fi; keep it 1990s arcade-electronic.",
        "S8_8BIT_TRANSLATED": "Do not use modern mobile-game polish, 3D cartoon style, neon cyberpunk, or high-res fantasy UI.",
    }
    return " ".join([NEGATIVE_BASE, f"Avoid panel-specific problems: {row['avoid']}.", leaks[stage.stage_id]])


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    panels = read_csv(root / "19_micro_storyboard_188_panels.csv")
    queue_path = root / "exports/real_image_generation_queue.csv"
    existing_queue = {r["panel_id"]: r for r in read_csv(queue_path)} if queue_path.exists() else {}

    for target in [
        root / "exports/panel_stage_state_map.csv",
        root / "exports/micro_storyboard_pure_image_prompts.csv",
        queue_path,
    ]:
        maybe_backup(target)

    stage_rows: list[dict[str, str]] = []
    prompt_rows: list[dict[str, str]] = []
    queue_rows: list[dict[str, str]] = []

    for row in panels:
        panel_id = row["panel_id"]
        number = panel_number(panel_id)
        stage = stage_for(panel_id)
        batch = existing_queue.get(panel_id, {}).get("batch") or f"B{((number - 1) // 32) + 1:02d}"
        pure_path = existing_queue.get(panel_id, {}).get("pure_path") or f"visual_assets/pure/micro_storyboard/{batch}/{panel_id}_v001.png"
        annotated_path = existing_queue.get(panel_id, {}).get("annotated_path") or f"visual_assets/annotated/micro_storyboard/{batch}/{panel_id}_v001_annotated.png"
        whitebox = find_whitebox(root, panel_id)

        stage_rows.append(
            {
                "panel_id": panel_id,
                "clip": row["clip"],
                "clip_title": row["clip_title"],
                "story_stage": stage.stage_id,
                "stage_name": stage.stage_name,
                "character_stage_lock": stage.character,
                "wardrobe_state": stage.wardrobe,
                "emotion_state": stage.emotion,
                "environment_stage_lock": stage.environment,
                "whitebox_reference_path": whitebox,
            }
        )
        prompt_rows.append(
            {
                "panel_id": panel_id,
                "batch": batch,
                "clip": row["clip"],
                "clip_title": row["clip_title"],
                "scene_id": scene_id(row["camera"]),
                "camera": row["camera"],
                "asset_type": row["asset_type"],
                "priority": row["priority"],
                "pure_path": pure_path,
                "annotated_path": annotated_path,
                "pure_prompt": make_prompt(row, stage, whitebox),
                "negative_prompt": make_negative(row, stage),
                "spatial_lock": f"Follow {whitebox}; preserve axis, scale, foreground/midground/background, and subject blocking.",
                "story_stage": stage.stage_id,
                "stage_name": stage.stage_name,
                "character_stage_lock": stage.character,
                "wardrobe_state": stage.wardrobe,
                "emotion_state": stage.emotion,
                "environment_stage_lock": stage.environment,
                "whitebox_reference_path": whitebox,
            }
        )
        previous = existing_queue.get(panel_id, {})
        pure_exists = (root / pure_path).exists()
        status = "generated_needs_qa" if pure_exists else previous.get("status", "queued")
        if "outdated" in previous.get("status", ""):
            status = "existing_draft_needs_review_or_regeneration" if pure_exists else "queued"
        queue_rows.append(
            {
                "panel_id": panel_id,
                "batch": batch,
                "clip": row["clip"],
                "clip_title": row["clip_title"],
                "priority": row["priority"],
                "story_stage": stage.stage_id,
                "pure_path": pure_path,
                "annotated_path": annotated_path,
                "whitebox_reference_path": whitebox,
                "status": status,
                "production_order": previous.get("production_order", str(number)),
                "notes": "generate pure first; annotate only after QA pass; clean prompt table rebuilt 2026-05-22",
            }
        )

    queue_rows.sort(key=lambda r: int(r["production_order"]))

    write_csv(
        root / "exports/panel_stage_state_map.csv",
        [
            "panel_id",
            "clip",
            "clip_title",
            "story_stage",
            "stage_name",
            "character_stage_lock",
            "wardrobe_state",
            "emotion_state",
            "environment_stage_lock",
            "whitebox_reference_path",
        ],
        stage_rows,
    )
    write_csv(
        root / "exports/micro_storyboard_pure_image_prompts.csv",
        [
            "panel_id",
            "batch",
            "clip",
            "clip_title",
            "scene_id",
            "camera",
            "asset_type",
            "priority",
            "pure_path",
            "annotated_path",
            "pure_prompt",
            "negative_prompt",
            "spatial_lock",
            "story_stage",
            "stage_name",
            "character_stage_lock",
            "wardrobe_state",
            "emotion_state",
            "environment_stage_lock",
            "whitebox_reference_path",
        ],
        prompt_rows,
    )
    write_csv(
        queue_path,
        [
            "panel_id",
            "batch",
            "clip",
            "clip_title",
            "priority",
            "story_stage",
            "pure_path",
            "annotated_path",
            "whitebox_reference_path",
            "status",
            "production_order",
            "notes",
        ],
        queue_rows,
    )

    max_q = max(r["pure_prompt"].count("?") for r in prompt_rows)
    missing_whitebox = sum(1 for r in stage_rows if not r["whitebox_reference_path"])
    existing_pure = sum(1 for r in queue_rows if (root / r["pure_path"]).exists())
    print(f"panel_stage_rows={len(stage_rows)}")
    print(f"pure_prompt_rows={len(prompt_rows)}")
    print(f"queue_rows={len(queue_rows)}")
    print(f"missing_whitebox={missing_whitebox}")
    print(f"existing_pure_images={existing_pure}")
    print(f"max_question_marks_in_prompt={max_q}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
