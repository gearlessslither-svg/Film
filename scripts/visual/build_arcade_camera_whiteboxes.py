from __future__ import annotations

import csv
import importlib.util
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / "tools" / "build_arcade_obj_whitebox.py"
BASE_DIR = ROOT / "environment_lookdev" / "SCN_ARCADE"
OBJ_DIR = BASE_DIR / "whitebox_obj"
OUT_DIR = BASE_DIR / "camera_whiteboxes_v001"
MOTHER = BASE_DIR / "SCN_ARCADE_lookdev_A_entrance_wide_v002_game_screens.png"

W, H = 1672, 941
BG = (28, 28, 27)
SENSOR_WIDTH_MM = 36.0


@dataclass(frozen=True)
class CameraSpec:
    camera_id: str
    location: tuple[float, float, float]
    target: tuple[float, float, float]
    focal_mm: float
    coverage: str
    note: str


CAMERAS = [
    CameraSpec(
        "CAM_ARCADE_01_ENTRANCE_WIDE",
        (0.0, -5.18, 1.32),
        (0.0, 0.10, 1.12),
        20.0,
        "MSB019-MSB028",
        "Mother-image entrance axis: plastic curtain foreground, narrow cabinet aisle, low ceiling.",
    ),
    CameraSpec(
        "CAM_ARCADE_01_CHILD_POV_CENTER",
        (0.04, -3.45, 0.96),
        (0.0, 1.65, 1.08),
        24.0,
        "alternate for MSB020-MSB024",
        "Child-height view inside the aisle; keeps cabinet rows and rear fighting cabinet aligned.",
    ),
    CameraSpec(
        "CAM_ARCADE_02_STREET_FIGHTER_CABINET",
        (-0.70, -3.45, 1.10),
        (-1.72, -2.78, 1.08),
        26.0,
        "MSB029-MSB037",
        "Left-front hero cabinet zone for the first duel setup; fictional screens only.",
    ),
    CameraSpec(
        "CAM_ARCADE_03_DUEL_OVER_SHOULDER",
        (-0.86, -2.08, 1.28),
        (0.0, 3.28, 1.24),
        38.0,
        "MSB038-MSB049",
        "Compressed aisle view toward the rear two-player machine, useful for duel coverage.",
    ),
    CameraSpec(
        "CAM_ARCADE_04_BOSS_LOSES_REACTION",
        (1.42, -2.18, 1.16),
        (0.32, 2.15, 1.18),
        42.0,
        "MSB050-MSB057",
        "Right-side reaction angle; preserves cabinet-row geography while turning away from the entrance.",
    ),
    CameraSpec(
        "CAM_ARCADE_DETAIL_CONTROL_PANEL",
        (-1.12, -3.20, 0.95),
        (-1.88, -3.03, 0.92),
        44.0,
        "detail inserts including MSB025/MSB033/MSB037/MSB039",
        "Close spatial lock for joystick, buttons, coin slot, and child-hand scale inserts.",
    ),
    CameraSpec(
        "CAM_ARCADE_CEILING_PRESSURE",
        (0.0, -2.52, 1.78),
        (0.0, 0.30, 2.02),
        30.0,
        "atmosphere inserts including MSB026",
        "Low ceiling, dirty bulb, fan, wires, smoke-pressure layout.",
    ),
]


def load_base_scene():
    spec = importlib.util.spec_from_file_location("arcade_whitebox_base", BASE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {BASE_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.faces.clear()
    module.asset_rows.clear()
    module.build_geometry()
    return module


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def norm(v):
    length = math.sqrt(max(dot(v, v), 1e-12))
    return (v[0] / length, v[1] / length, v[2] / length)


def camera_basis(cam: CameraSpec):
    forward = norm(sub(cam.target, cam.location))
    world_up = (0.0, 0.0, 1.0)
    right = norm(cross(forward, world_up))
    up = norm(cross(right, forward))
    return right, up, forward


def project(point, cam: CameraSpec):
    right, up, forward = camera_basis(cam)
    rel = sub(point, cam.location)
    cx = dot(rel, right)
    cy = dot(rel, up)
    cz = dot(rel, forward)
    if cz <= 0.06:
        return None
    fov_x = 2.0 * math.atan(SENSOR_WIDTH_MM / (2.0 * cam.focal_mm))
    aspect = W / H
    fov_y = 2.0 * math.atan(math.tan(fov_x / 2.0) / aspect)
    px = W * 0.5 + (cx / (cz * math.tan(fov_x / 2.0))) * W * 0.5
    py = H * 0.5 - (cy / (cz * math.tan(fov_y / 2.0))) * H * 0.5
    return px, py, cz


def material_color(material: str, materials, depth: float):
    rgb = materials.get(material, (0.30, 0.30, 0.30))
    base = tuple(int(max(0, min(1, c)) * 255) for c in rgb)
    if material.startswith("screen_") or material == "warm_bulb":
        glow = 1.15
        return tuple(min(255, int(c * glow + 16)) for c in base)
    haze = max(0.0, min(0.55, (depth - 1.0) / 12.0))
    return tuple(int(c * (1.0 - haze) + BG[i] * haze) for i, c in enumerate(base))


def draw_grid(draw: ImageDraw.ImageDraw, cam: CameraSpec) -> None:
    line_color = (120, 120, 112, 70)
    for x in [i * 0.5 for i in range(-5, 6)]:
        pts = [project((x, y, 0.005), cam) for y in [i * 0.25 - 4.5 for i in range(37)]]
        draw_polyline(draw, pts, line_color, 1)
    for y in [i * 0.5 - 4.5 for i in range(19)]:
        pts = [project((x, y, 0.006), cam) for x in [i * 0.25 - 2.5 for i in range(21)]]
        draw_polyline(draw, pts, line_color, 1)


def draw_polyline(draw: ImageDraw.ImageDraw, pts, fill, width):
    clean = [(p[0], p[1]) for p in pts if p is not None]
    if len(clean) >= 2:
        draw.line(clean, fill=fill, width=width)


def render_camera(cam: CameraSpec, base) -> tuple[Path, dict[str, int]]:
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image, "RGBA")
    draw_grid(draw, cam)

    projected = []
    for face in base.faces:
        pts = [project(vertex, cam) for vertex in face.verts]
        if any(p is None for p in pts):
            continue
        coords = [(p[0], p[1]) for p in pts if p is not None]
        min_x = min(x for x, _ in coords)
        max_x = max(x for x, _ in coords)
        min_y = min(y for _, y in coords)
        max_y = max(y for _, y in coords)
        if max_x < -W or min_x > W * 2 or max_y < -H or min_y > H * 2:
            continue
        avg_depth = sum(p[2] for p in pts if p is not None) / len(pts)
        projected.append((avg_depth, face.material, face.name, coords))

    projected.sort(key=lambda item: item[0], reverse=True)

    visible_faces = 0
    screen_faces = 0
    for avg_depth, material, _name, coords in projected:
        fill = material_color(material, base.MATERIALS, avg_depth)
        alpha = 238 if material.startswith("screen_") else 220
        outline = (9, 9, 9, 205)
        draw.polygon(coords, fill=fill + (alpha,), outline=outline)
        visible_faces += 1
        if material.startswith("screen_"):
            screen_faces += 1
            centroid = (
                sum(x for x, _ in coords) / len(coords),
                sum(y for _, y in coords) / len(coords),
            )
            r = max(2, min(18, int(160 / max(avg_depth, 1.0))))
            draw.ellipse(
                [centroid[0] - r, centroid[1] - r, centroid[0] + r, centroid[1] + r],
                fill=fill + (60,),
            )

    out_path = OUT_DIR / f"{cam.camera_id}_constraint_whitebox_v001.png"
    image.save(out_path)
    return out_path, {"visible_faces": visible_faces, "screen_faces": screen_faces}


def write_manifest(rows: list[dict[str, str]]) -> None:
    csv_path = OUT_DIR / "SCN_ARCADE_camera_constraint_manifest_v001.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "camera_id",
                "coverage",
                "whitebox_path",
                "location_xyz",
                "target_xyz",
                "focal_mm",
                "visible_faces",
                "screen_faces",
                "note",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    json_path = OUT_DIR / "SCN_ARCADE_camera_constraint_manifest_v001.json"
    json_path.write_text(
        json.dumps(
            {
                "scene_id": "SCN_ARCADE",
                "mother_image": str(MOTHER.relative_to(ROOT)),
                "geometry_source": str((OBJ_DIR / "SCN_ARCADE_mother_visual_constraint_whitebox_v001.obj").relative_to(ROOT)),
                "style_reference": str(MOTHER.relative_to(ROOT)),
                "camera_constraints": rows,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def write_panel_map(rows: list[dict[str, str]]) -> None:
    source_manifest = ROOT / "blender" / "whitebox_v2_manifest.csv"
    camera_to_path = {row["camera_id"]: row["whitebox_path"] for row in rows}
    detail_panels = {"MSB025", "MSB033", "MSB037", "MSB039"}
    ceiling_panels = {"MSB026"}
    mapped_rows = []

    with source_manifest.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if row.get("scene_id") != "SCN_ARCADE":
                continue
            panel_id = row["panel_id"]
            selected = row["source_camera"]
            note = "uses source camera constraint"
            if panel_id in detail_panels:
                selected = "CAM_ARCADE_DETAIL_CONTROL_PANEL"
                note = "detail insert uses dedicated control-panel constraint"
            elif panel_id in ceiling_panels:
                selected = "CAM_ARCADE_CEILING_PRESSURE"
                note = "atmosphere insert uses dedicated low-ceiling constraint"

            mapped_rows.append(
                {
                    "panel_id": panel_id,
                    "batch": row["batch"],
                    "clip": row["clip"],
                    "source_camera": row["source_camera"],
                    "selected_constraint_camera": selected,
                    "constraint_whitebox_path": camera_to_path[selected],
                    "mother_style_reference": str(MOTHER.relative_to(ROOT)),
                    "layout_focus": row["layout_focus"],
                    "pose_or_path": row["pose_or_path"],
                    "mapping_note": note,
                }
            )

    map_path = OUT_DIR / "SCN_ARCADE_panel_camera_constraint_map_v001.csv"
    with map_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "panel_id",
                "batch",
                "clip",
                "source_camera",
                "selected_constraint_camera",
                "constraint_whitebox_path",
                "mother_style_reference",
                "layout_focus",
                "pose_or_path",
                "mapping_note",
            ],
        )
        writer.writeheader()
        writer.writerows(mapped_rows)


def make_contact_sheet(rows: list[dict[str, str]]) -> Path:
    thumbs = []
    thumb_w = 480
    for row in rows:
        img = Image.open(OUT_DIR / Path(row["whitebox_path"]).name).convert("RGB")
        thumb = img.resize((thumb_w, int(img.height * thumb_w / img.width)), Image.Resampling.LANCZOS)
        thumbs.append((row["camera_id"], row["coverage"], thumb))

    cols = 2
    thumb_h = max(t.height for _, _, t in thumbs)
    label_h = 64
    pad = 18
    sheet_w = cols * thumb_w + (cols + 1) * pad
    rows_count = math.ceil(len(thumbs) / cols)
    sheet_h = rows_count * (thumb_h + label_h) + (rows_count + 1) * pad
    sheet = Image.new("RGB", (sheet_w, sheet_h), (242, 242, 240))
    draw = ImageDraw.Draw(sheet)
    try:
        title_font = ImageFont.truetype("Arial.ttf", 20)
        small_font = ImageFont.truetype("Arial.ttf", 16)
    except OSError:
        title_font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    for idx, (camera_id, coverage, thumb) in enumerate(thumbs):
        col = idx % cols
        row = idx // cols
        x = pad + col * (thumb_w + pad)
        y = pad + row * (thumb_h + label_h + pad)
        sheet.paste(thumb, (x, y))
        draw.text((x + 4, y + thumb_h + 8), camera_id, fill=(22, 22, 22), font=title_font)
        draw.text((x + 4, y + thumb_h + 34), coverage, fill=(72, 72, 72), font=small_font)

    path = OUT_DIR / "SCN_ARCADE_camera_constraints_contact_sheet_v001.jpg"
    sheet.save(path, quality=92)
    return path


def validate_outputs(rows: list[dict[str, str]]) -> dict[str, object]:
    result = {
        "image_count": len(rows),
        "expected_resolution": [W, H],
        "all_resolution_ok": True,
        "all_nonblank": True,
        "minimum_visible_faces": None,
    }
    minimum_faces = None
    for row in rows:
        path = OUT_DIR / Path(row["whitebox_path"]).name
        img = Image.open(path).convert("RGB")
        if img.size != (W, H):
            result["all_resolution_ok"] = False
        extrema = img.getextrema()
        if all(lo == hi for lo, hi in extrema):
            result["all_nonblank"] = False
        visible = int(row["visible_faces"])
        minimum_faces = visible if minimum_faces is None else min(minimum_faces, visible)
    result["minimum_visible_faces"] = minimum_faces
    return result


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    base = load_base_scene()
    rows: list[dict[str, str]] = []
    for cam in CAMERAS:
        path, stats = render_camera(cam, base)
        rows.append(
            {
                "camera_id": cam.camera_id,
                "coverage": cam.coverage,
                "whitebox_path": str(path.relative_to(ROOT)),
                "location_xyz": json.dumps(cam.location),
                "target_xyz": json.dumps(cam.target),
                "focal_mm": f"{cam.focal_mm:.1f}",
                "visible_faces": str(stats["visible_faces"]),
                "screen_faces": str(stats["screen_faces"]),
                "note": cam.note,
            }
        )
    write_manifest(rows)
    write_panel_map(rows)
    contact_sheet = make_contact_sheet(rows)
    validation = validate_outputs(rows)
    validation_path = OUT_DIR / "SCN_ARCADE_camera_constraints_validation_v001.json"
    validation_path.write_text(json.dumps(validation, indent=2), encoding="utf-8")
    print(contact_sheet)
    print(validation_path)
    print(json.dumps(validation, indent=2))


if __name__ == "__main__":
    main()
