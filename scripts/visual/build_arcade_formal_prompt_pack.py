from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCENE_DIR = ROOT / "environment_lookdev" / "SCN_ARCADE"
CAMERA_DIR = SCENE_DIR / "camera_whiteboxes_v001"
PANEL_MAP = CAMERA_DIR / "SCN_ARCADE_panel_camera_constraint_map_v001.csv"
OUT_CSV = CAMERA_DIR / "SCN_ARCADE_formal_storyboard_prompt_pack_v001.csv"
OUT_MD = CAMERA_DIR / "SCN_ARCADE_formal_storyboard_prompt_pack_v001.md"


BASE_STYLE = (
    "Pure cinematic storyboard frame for AIGC video generation, 16:9 landscape, "
    "high-resolution film still quality, no annotations, no captions, no visible readable text. "
    "1990s small-town China hidden arcade room, Chinese dreamcore realism, humid yellowed childhood memory, "
    "dim gray-yellow light, CRT blue-green-red screen glow, subtle VHS grain, lived-in dirty surfaces."
)

SCENE_DNA = (
    "Keep SCN_ARCADE design DNA consistent: dirty plastic entrance strips, low stained ceiling, narrow wet aisle, "
    "left and right rows of bulky black CRT arcade cabinets, rear two-player fictional fighting cabinet, old wooden stools, "
    "single warm dirty bulb, ceiling fan, sagging wires, peeling gray walls, unreadable poster scraps."
)

GAME_SCREEN_RULE = (
    "Arcade screen content must be fictional and non-infringing: genre-level 1990s fighting-game, beat-em-up, "
    "side-scrolling action, and vertical shooter energy only; no real game title, no logo, no copyrighted UI, "
    "no recognizable character from existing games."
)

NEGATIVE = (
    "Do not show modern arcade cabinets, LCD screens, smartphones, LED esports room, cyberpunk neon club, clean mall game center, "
    "readable game names, real Street Fighter, real Mortal Kombat, real Cadillacs and Dinosaurs, real Dynasty Wars, real Captain Commando, "
    "real Psikyo logos, copyrighted characters, gore, adult gangsters, anime style, toy-like 3D, poster text, watermark, subtitle, annotation."
)


def build_prompt(row: dict[str, str]) -> str:
    return " ".join(
        [
            BASE_STYLE,
            f"Panel {row['panel_id']} / clip {row['clip']}.",
            f"Use mother style reference path: {row['mother_style_reference']}.",
            f"Use spatial constraint whitebox path: {row['constraint_whitebox_path']}.",
            f"Camera constraint: {row['selected_constraint_camera']}.",
            f"Layout/action focus: {row['layout_focus']}.",
            f"Blocking or motion: {row['pose_or_path']}.",
            SCENE_DNA,
            GAME_SCREEN_RULE,
            "Preserve the same room proportions and cabinet positions from the whitebox; only add final cinematic texture, light, haze, characters, and period detail.",
        ]
    )


def main() -> None:
    with PANEL_MAP.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    out_rows = []
    for row in rows:
        out_rows.append(
            {
                "panel_id": row["panel_id"],
                "batch": row["batch"],
                "clip": row["clip"],
                "scene_id": "SCN_ARCADE",
                "selected_constraint_camera": row["selected_constraint_camera"],
                "mother_style_reference": row["mother_style_reference"],
                "constraint_whitebox_path": row["constraint_whitebox_path"],
                "pure_prompt": build_prompt(row),
                "negative_prompt": NEGATIVE,
                "status": "ready_for_formal_generation_with_mother_style_and_whitebox_space",
            }
        )

    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "panel_id",
                "batch",
                "clip",
                "scene_id",
                "selected_constraint_camera",
                "mother_style_reference",
                "constraint_whitebox_path",
                "pure_prompt",
                "negative_prompt",
                "status",
            ],
        )
        writer.writeheader()
        writer.writerows(out_rows)

    camera_counts: dict[str, int] = {}
    for row in out_rows:
        camera_counts[row["selected_constraint_camera"]] = camera_counts.get(row["selected_constraint_camera"], 0) + 1

    lines = [
        "# SCN_ARCADE Formal Storyboard Prompt Pack v001",
        "",
        f"Rows: {len(out_rows)}",
        f"Panel range: {out_rows[0]['panel_id']} through {out_rows[-1]['panel_id']}",
        "",
        "Source references:",
        "",
        f"- Mother style image: `{out_rows[0]['mother_style_reference']}`",
        "- Panel-to-whitebox map: `SCN_ARCADE_panel_camera_constraint_map_v001.csv`",
        "",
        "Camera distribution:",
        "",
    ]
    for camera_id, count in sorted(camera_counts.items()):
        lines.append(f"- `{camera_id}`: {count}")
    lines.extend(
        [
            "",
            "Usage:",
            "",
            "Use each row's `mother_style_reference` as the style anchor and `constraint_whitebox_path` as the spatial anchor. Keep all arcade game screen content fictional and non-infringing.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(OUT_CSV)
    print(OUT_MD)
    print(f"rows={len(out_rows)}")


if __name__ == "__main__":
    main()
