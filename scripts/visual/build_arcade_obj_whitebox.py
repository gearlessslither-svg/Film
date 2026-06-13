from __future__ import annotations

import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "environment_lookdev" / "SCN_ARCADE" / "whitebox_obj"
MOTHER = ROOT / "environment_lookdev" / "SCN_ARCADE" / "SCN_ARCADE_lookdev_A_entrance_wide_v002_game_screens.png"


@dataclass
class Face:
    verts: list[tuple[float, float, float]]
    material: str
    name: str


faces: list[Face] = []


MATERIALS = {
    "floor_wet_gray": (0.22, 0.22, 0.20),
    "ceiling_dirty_gray": (0.34, 0.34, 0.31),
    "wall_peeling_gray": (0.48, 0.47, 0.43),
    "wall_patch": (0.30, 0.30, 0.28),
    "cabinet_black": (0.035, 0.038, 0.040),
    "cabinet_face": (0.13, 0.12, 0.10),
    "screen_blue": (0.05, 0.42, 0.75),
    "screen_green": (0.05, 0.55, 0.33),
    "screen_red": (0.75, 0.14, 0.10),
    "screen_gold": (0.80, 0.55, 0.10),
    "screen_purple": (0.40, 0.15, 0.75),
    "plastic_curtain": (0.30, 0.29, 0.26),
    "stool_wood": (0.22, 0.17, 0.12),
    "wire_dark": (0.025, 0.025, 0.024),
    "warm_bulb": (1.0, 0.80, 0.36),
    "control_panel": (0.18, 0.16, 0.13),
}


asset_rows: list[dict[str, str]] = []


def add_asset(asset_id: str, category: str, description: str, role: str, lock_note: str) -> None:
    asset_rows.append(
        {
            "asset_id": asset_id,
            "category": category,
            "description": description,
            "role": role,
            "lock_note": lock_note,
        }
    )


def rot_xy(x: float, y: float, yaw: float) -> tuple[float, float]:
    c = math.cos(yaw)
    s = math.sin(yaw)
    return x * c - y * s, x * s + y * c


def add_box(
    name: str,
    loc: tuple[float, float, float],
    size: tuple[float, float, float],
    material: str,
    yaw: float = 0.0,
) -> None:
    cx, cy, cz = loc
    sx, sy, sz = size[0] / 2, size[1] / 2, size[2] / 2
    corners = []
    for x, y, z in [
        (-sx, -sy, -sz),
        (sx, -sy, -sz),
        (sx, sy, -sz),
        (-sx, sy, -sz),
        (-sx, -sy, sz),
        (sx, -sy, sz),
        (sx, sy, sz),
        (-sx, sy, sz),
    ]:
        rx, ry = rot_xy(x, y, yaw)
        corners.append((cx + rx, cy + ry, cz + z))
    quads = [
        [0, 1, 2, 3],
        [4, 7, 6, 5],
        [0, 4, 5, 1],
        [1, 5, 6, 2],
        [2, 6, 7, 3],
        [3, 7, 4, 0],
    ]
    for quad in quads:
        faces.append(Face([corners[i] for i in quad], material, name))


def add_arcade_cabinet(prefix: str, x: float, y: float, yaw: float, scale: float, screen: str) -> None:
    add_box(prefix + "_body", (x, y, 0.96 * scale), (0.78 * scale, 0.62 * scale, 1.72 * scale), "cabinet_black", yaw)
    add_box(prefix + "_base", (x, y + 0.03 * scale, 0.28 * scale), (0.86 * scale, 0.68 * scale, 0.56 * scale), "cabinet_face", yaw)
    add_box(prefix + "_marquee", (x, y - 0.23 * scale, 1.78 * scale), (0.82 * scale, 0.10 * scale, 0.18 * scale), screen, yaw)
    add_box(prefix + "_bezel", (x, y - 0.31 * scale, 1.28 * scale), (0.66 * scale, 0.06 * scale, 0.52 * scale), "cabinet_face", yaw)
    add_box(prefix + "_screen", (x, y - 0.35 * scale, 1.30 * scale), (0.54 * scale, 0.018 * scale, 0.36 * scale), screen, yaw)
    add_box(prefix + "_control_panel", (x, y - 0.39 * scale, 0.88 * scale), (0.72 * scale, 0.22 * scale, 0.10 * scale), "control_panel", yaw)
    add_box(prefix + "_joystick", (x - 0.15 * scale if x < 0 else x + 0.15 * scale, y - 0.52 * scale, 0.98 * scale), (0.06 * scale, 0.06 * scale, 0.12 * scale), "screen_red", yaw)
    for idx, mat in enumerate(["screen_red", "screen_gold", "screen_blue", "screen_green"]):
        direction = 1 if x < 0 else -1
        add_box(
            prefix + f"_button_{idx}",
            (x + direction * (0.03 + 0.075 * idx) * scale, y - 0.52 * scale, 0.955 * scale),
            (0.045 * scale, 0.045 * scale, 0.025 * scale),
            mat,
            yaw,
        )


def add_double_cabinet() -> None:
    add_box("BACK_double_fighting_cabinet_body", (0.0, 3.72, 0.98), (1.65, 0.58, 1.58), "cabinet_black")
    add_box("BACK_double_fighting_cabinet_marquee", (0.0, 3.42, 1.78), (1.72, 0.10, 0.18), "cabinet_face")
    add_box("BACK_left_screen_fictional_fighter", (-0.42, 3.34, 1.28), (0.62, 0.018, 0.42), "screen_blue")
    add_box("BACK_right_screen_fictional_fighter", (0.42, 3.34, 1.28), (0.62, 0.018, 0.42), "screen_red")
    add_box("BACK_double_control_panel", (0.0, 3.22, 0.83), (1.56, 0.28, 0.10), "control_panel")
    for x in [-0.62, -0.48, -0.34, 0.34, 0.48, 0.62]:
        add_box("BACK_control_buttons", (x, 3.04, 0.91), (0.045, 0.045, 0.03), "screen_gold")


def add_stool(prefix: str, x: float, y: float, scale: float) -> None:
    add_box(prefix + "_seat", (x, y, 0.45 * scale), (0.36 * scale, 0.36 * scale, 0.06 * scale), "stool_wood")
    for dx in [-0.13, 0.13]:
        for dy in [-0.13, 0.13]:
            add_box(prefix + f"_leg_{dx}_{dy}", (x + dx * scale, y + dy * scale, 0.22 * scale), (0.035 * scale, 0.035 * scale, 0.42 * scale), "stool_wood")


def build_geometry() -> None:
    add_box("FLOOR_wet_narrow_aisle", (0, 0, -0.03), (5.20, 9.40, 0.06), "floor_wet_gray")
    add_box("CEILING_low_stained", (0, 0, 2.23), (5.20, 9.40, 0.06), "ceiling_dirty_gray")
    add_box("LEFT_peeling_wall", (-2.62, 0, 1.08), (0.08, 9.40, 2.20), "wall_peeling_gray")
    add_box("RIGHT_peeling_wall", (2.62, 0, 1.08), (0.08, 9.40, 2.20), "wall_peeling_gray")
    add_box("BACK_dirty_wall", (0, 4.62, 1.08), (5.20, 0.08, 2.20), "wall_peeling_gray")
    add_box("BACK_small_window", (0, 4.56, 1.55), (0.58, 0.04, 0.32), "screen_green")
    add_asset("ROOM_SHELL", "architecture", "low rectangular residential storage-room shell", "global space lock", "floor/ceiling/walls define the arcade room volume")

    # Foreground plastic curtains, critical mother-image anchor.
    for idx, x in enumerate([-2.58, -2.30, -2.05, 2.05, 2.34, 2.62]):
        add_box(f"FG_dirty_plastic_curtain_strip_{idx}", (x, -4.76, 1.24), (0.18, 0.035, 2.65), "plastic_curtain", math.radians(2 if x < 0 else -2))
    add_asset("FG_PLASTIC_CURTAIN", "foreground", "dirty hanging plastic entrance strips", "mother camera framing", "must remain at entrance, framing both sides of the shot")

    # Cabinet banks.
    left = [
        (-1.95, -2.55, 0.88, "screen_green"),
        (-1.72, -1.52, 0.80, "screen_red"),
        (-1.48, -0.55, 0.70, "screen_blue"),
        (-1.25, 0.34, 0.60, "screen_gold"),
        (-1.06, 1.12, 0.52, "screen_green"),
    ]
    right = [
        (1.95, -2.40, 0.88, "screen_blue"),
        (1.72, -1.34, 0.78, "screen_purple"),
        (1.48, -0.44, 0.68, "screen_red"),
        (1.25, 0.40, 0.58, "screen_gold"),
        (1.06, 1.18, 0.50, "screen_green"),
    ]
    for idx, (x, y, scale, screen) in enumerate(left):
        add_arcade_cabinet(f"LEFT_CAB_{idx}", x, y, math.radians(-8), scale, screen)
    for idx, (x, y, scale, screen) in enumerate(right):
        add_arcade_cabinet(f"RIGHT_CAB_{idx}", x, y, math.radians(8), scale, screen)
    add_asset("CABINET_ROWS", "architecture/props", "two rows of bulky CRT arcade cabinets forming a narrow aisle", "spatial DNA", "left/right cabinet banks must stay parallel and cramped")

    add_double_cabinet()
    add_asset("BACK_DOUBLE_FIGHTING_CAB", "hero prop", "rear two-player fictional fighting-game cabinet", "visual destination", "screen content stays fictional, no real titles/logos/characters")

    for idx, (x, y, scale) in enumerate([
        (-1.38, -2.78, 0.95),
        (1.33, -2.55, 0.95),
        (-0.85, -0.90, 0.78),
        (0.86, -0.70, 0.78),
        (-0.40, 1.15, 0.62),
        (0.42, 1.18, 0.62),
        (0.0, 2.75, 0.55),
    ]):
        add_stool(f"STOOL_{idx}", x, y, scale)
    add_asset("STOOL_SET", "props", "old wooden stools scattered along cabinet rows", "scale and blockage reference", "use as child-height/standing-space anchors")

    # Ceiling fixtures and wiring.
    add_box("LIGHT_dirty_warm_bulb", (0, -0.85, 1.95), (0.16, 0.16, 0.16), "warm_bulb")
    add_box("CEILING_FAN_hub", (0, 0.28, 2.13), (0.16, 0.16, 0.08), "wire_dark")
    for idx, angle in enumerate([0, 120, 240]):
        add_box(f"CEILING_FAN_blade_{idx}", (0, 0.28, 2.13), (0.72, 0.055, 0.018), "wire_dark", math.radians(angle))
    for idx, (x, y, z, sx, sy, sz) in enumerate([
        (0.0, -1.65, 2.05, 4.3, 0.025, 0.025),
        (-0.6, -0.15, 2.02, 3.7, 0.025, 0.025),
        (0.25, 1.55, 1.96, 3.8, 0.025, 0.025),
    ]):
        add_box(f"CEILING_sagging_wire_{idx}", (x, y, z), (sx, sy, sz), "wire_dark", math.radians(7 * (idx - 1)))
    add_asset("CEILING_FIXTURES", "lighting/props", "single dirty warm bulb, fan, sagging wires", "lighting and ceiling-height lock", "must preserve low ceiling pressure and central bulb")

    # Wall patches and poster scraps, intentionally unreadable.
    for idx, (x, y, z, sx, sy, sz) in enumerate([
        (-2.57, -2.2, 1.25, 0.035, 0.45, 0.54),
        (2.57, -1.6, 1.32, 0.035, 0.42, 0.48),
        (-2.57, 1.9, 1.05, 0.035, 0.55, 0.70),
        (2.57, 2.2, 1.08, 0.035, 0.45, 0.62),
        (-1.55, 4.54, 1.36, 0.58, 0.035, 0.75),
        (1.45, 4.54, 1.30, 0.65, 0.035, 0.86),
    ]):
        add_box(f"WALL_patch_or_poster_{idx}", (x, y, z), (sx, sy, sz), "wall_patch")
    add_asset("WALL_SCARS", "surface detail", "peeling patches and non-readable poster masses", "visual texture lock", "no readable text or real game IP")


def write_obj() -> tuple[Path, Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    obj_path = OUT_DIR / "SCN_ARCADE_mother_visual_constraint_whitebox_v001.obj"
    mtl_path = OUT_DIR / "SCN_ARCADE_mother_visual_constraint_whitebox_v001.mtl"
    with mtl_path.open("w", encoding="utf-8") as f:
        for name, rgb in MATERIALS.items():
            f.write(f"newmtl {name}\n")
            f.write(f"Kd {rgb[0]:.4f} {rgb[1]:.4f} {rgb[2]:.4f}\n")
            f.write("Ka 0.0000 0.0000 0.0000\n")
            f.write("Ks 0.0500 0.0500 0.0500\n")
            f.write("Ns 16\n\n")

    verts: list[tuple[float, float, float]] = []
    with obj_path.open("w", encoding="utf-8") as f:
        f.write("# SCN_ARCADE mother-image visual constraint whitebox v001\n")
        f.write(f"mtllib {mtl_path.name}\n")
        for face in faces:
            f.write(f"o {face.name}\n")
            f.write(f"usemtl {face.material}\n")
            start = len(verts) + 1
            for vertex in face.verts:
                verts.append(vertex)
                f.write(f"v {vertex[0]:.4f} {vertex[1]:.4f} {vertex[2]:.4f}\n")
            indices = " ".join(str(start + i) for i in range(len(face.verts)))
            f.write(f"f {indices}\n")
    return obj_path, mtl_path


def write_metadata() -> None:
    camera = {
        "camera_id": "CAM_SCN_ARCADE_MOTHER_MATCH",
        "source_mother_image": str(MOTHER.relative_to(ROOT)),
        "intent": "match the selected arcade mother image A v002 as closely as possible with proxy geometry",
        "coordinate_notes": "Y axis runs down the arcade aisle; camera looks from y=-5.18 toward y=0.10; floor is z=0.",
        "suggested_camera": {
            "location_xyz": [0.0, -5.18, 1.32],
            "look_at_xyz": [0.0, 0.10, 1.12],
            "focal_length_mm": 20,
            "resolution": [1672, 941],
        },
        "known_limits": [
            "OBJ has proxy geometry and material colors, not final projection textures.",
            "Blender 5.1.2 macOS CLI is currently crashing before Python execution on this machine.",
            "Import OBJ through Blender GUI until a stable CLI path is available.",
        ],
    }
    (OUT_DIR / "SCN_ARCADE_mother_camera_lock_v001.json").write_text(json.dumps(camera, ensure_ascii=False, indent=2), encoding="utf-8")

    with (OUT_DIR / "SCN_ARCADE_scene_asset_design_list_v001.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["asset_id", "category", "description", "role", "lock_note"])
        writer.writeheader()
        writer.writerows(asset_rows)


def make_visual_png() -> None:
    mother = Image.open(MOTHER).convert("RGB")
    w, h = mother.size
    whitebox = Image.new("RGB", (w, h), (30, 30, 30))
    draw = ImageDraw.Draw(whitebox, "RGBA")

    # Hand-placed mother-camera 2D projection guide. This is the visual QA plate for the OBJ.
    draw.polygon([(190, 0), (1485, 0), (1238, 326), (455, 318)], fill=(96, 96, 92, 255), outline=(12, 12, 12, 190))
    draw.polygon([(470, 300), (1248, 300), (1112, 584), (560, 584)], fill=(112, 112, 108, 255), outline=(12, 12, 12, 190))
    draw.polygon([(210, 54), (486, 307), (559, 900), (115, 941), (0, 941), (0, 0)], fill=(128, 128, 122, 255), outline=(12, 12, 12, 170))
    draw.polygon([(1236, 300), (1495, 60), (1672, 0), (1672, 941), (1160, 900), (1118, 585)], fill=(128, 128, 122, 255), outline=(12, 12, 12, 170))
    draw.polygon([(555, 584), (1118, 584), (1320, 941), (350, 941)], fill=(76, 76, 72, 255), outline=(12, 12, 12, 190))

    # Curtains.
    for poly in [
        [(0, 0), (155, 0), (210, 941), (0, 941)],
        [(1510, 0), (1672, 0), (1672, 941), (1398, 941)],
    ]:
        draw.polygon(poly, fill=(58, 58, 56, 235), outline=(8, 8, 8, 220))
    for x in [35, 72, 115, 150, 1512, 1550, 1594, 1636]:
        draw.line([(x, 0), (x - 22 if x < 800 else x + 28, 941)], fill=(120, 120, 115, 120), width=5)

    # Cabinets as projected blocks.
    def cab_left(x, y, s, color):
        body = [(x, y), (x + s * 86, y + s * 10), (x + s * 98, y + s * 218), (x + s * 18, y + s * 246), (x - s * 8, y + s * 70)]
        scr = [(x + s * 18, y + s * 42), (x + s * 82, y + s * 50), (x + s * 82, y + s * 122), (x + s * 10, y + s * 115)]
        panel = [(x + s * 18, y + s * 170), (x + s * 96, y + s * 155), (x + s * 105, y + s * 205), (x + s * 22, y + s * 228)]
        draw.polygon(body, fill=(44, 46, 48, 255), outline=(8, 8, 8, 220))
        draw.polygon(panel, fill=(82, 82, 78, 255), outline=(8, 8, 8, 160))
        draw.polygon(scr, fill=color + (230,), outline=(8, 8, 8, 220))

    def cab_right(x, y, s, color):
        body = [(x, y), (x - s * 86, y + s * 10), (x - s * 98, y + s * 218), (x - s * 18, y + s * 246), (x + s * 8, y + s * 70)]
        scr = [(x - s * 18, y + s * 42), (x - s * 82, y + s * 50), (x - s * 82, y + s * 122), (x - s * 10, y + s * 115)]
        panel = [(x - s * 18, y + s * 170), (x - s * 96, y + s * 155), (x - s * 105, y + s * 205), (x - s * 22, y + s * 228)]
        draw.polygon(body, fill=(44, 46, 48, 255), outline=(8, 8, 8, 220))
        draw.polygon(panel, fill=(82, 82, 78, 255), outline=(8, 8, 8, 160))
        draw.polygon(scr, fill=color + (230,), outline=(8, 8, 8, 220))

    for args in [(605, 330, .55, (184, 154, 82)), (512, 325, .68, (68, 160, 120)), (415, 330, .83, (74, 150, 190)), (305, 350, 1.02, (170, 82, 65)), (185, 380, 1.23, (68, 160, 120))]:
        cab_left(*args)
    for args in [(1062, 330, .55, (170, 82, 65)), (1152, 330, .68, (74, 150, 190)), (1255, 342, .83, (184, 154, 82)), (1382, 366, 1.02, (68, 160, 120))]:
        cab_right(*args)

    draw.rounded_rectangle([684, 343, 990, 570], radius=8, fill=(46, 47, 46, 255), outline=(8, 8, 8, 230), width=4)
    draw.rectangle([705, 380, 830, 477], fill=(74, 150, 190, 230), outline=(8, 8, 8, 200), width=3)
    draw.rectangle([844, 380, 970, 477], fill=(170, 82, 65, 230), outline=(8, 8, 8, 200), width=3)
    draw.rectangle([705, 492, 970, 528], fill=(82, 82, 78, 255), outline=(8, 8, 8, 160), width=2)

    # Stools and bulb.
    for cx, cy, s in [(735, 582, .55), (955, 588, .55), (580, 690, .75), (1112, 700, .8), (480, 812, 1.05), (1190, 820, 1.05), (838, 552, .48)]:
        draw.ellipse([cx - 22*s, cy - 10*s, cx + 22*s, cy + 10*s], fill=(70, 67, 61, 255), outline=(8, 8, 8, 180))
    draw.ellipse([815, 162, 858, 205], fill=(235, 213, 150, 220), outline=(250, 230, 170, 220), width=2)

    out_png = OUT_DIR / "SCN_ARCADE_visual_constraint_whitebox_2d_v001.png"
    whitebox.save(out_png)

    overlay = Image.blend(mother, whitebox, 0.62)
    overlay.save(OUT_DIR / "SCN_ARCADE_visual_constraint_overlay_v001.png")

    tw = 520
    items = [("mother", mother), ("2D whitebox", whitebox), ("overlay", overlay)]
    thumbs = []
    for label, img in items:
        thumbs.append((label, img.resize((tw, int(img.height * tw / img.width)), Image.Resampling.LANCZOS)))
    th = max(img.height for _, img in thumbs)
    sheet = Image.new("RGB", (tw * 3 + 64, th + 76), (245, 245, 245))
    d = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("Arial.ttf", 22)
    except OSError:
        font = ImageFont.load_default()
    for idx, (label, img) in enumerate(thumbs):
        x = 16 + idx * (tw + 16)
        sheet.paste(img, (x, 16))
        d.text((x + 6, 16 + th + 10), label, fill=(20, 20, 20), font=font)
    sheet.save(OUT_DIR / "SCN_ARCADE_visual_constraint_compare_v001.jpg", quality=92)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_geometry()
    obj_path, mtl_path = write_obj()
    write_metadata()
    make_visual_png()
    print(obj_path)
    print(mtl_path)
    print(OUT_DIR / "SCN_ARCADE_visual_constraint_compare_v001.jpg")


if __name__ == "__main__":
    main()
