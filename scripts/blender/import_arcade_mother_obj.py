from __future__ import annotations

import json
import math
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[1]
OBJ_DIR = ROOT / "environment_lookdev" / "SCN_ARCADE" / "whitebox_obj"
OBJ_PATH = OBJ_DIR / "SCN_ARCADE_mother_visual_constraint_whitebox_v001.obj"
CAMERA_LOCK_PATH = OBJ_DIR / "SCN_ARCADE_mother_camera_lock_v001.json"
BLEND_OUT = ROOT / "blender" / "SCN_ARCADE_mother_visual_constraint_whitebox_v001.blend"
PREVIEW_OUT = OBJ_DIR / "SCN_ARCADE_blender_import_preview_v001.png"


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def look_at(obj, target_xyz) -> None:
    direction = Vector(target_xyz) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def import_obj() -> list[bpy.types.Object]:
    before = set(bpy.data.objects)
    if hasattr(bpy.ops.wm, "obj_import"):
        bpy.ops.wm.obj_import(filepath=str(OBJ_PATH), forward_axis="Y", up_axis="Z")
    else:
        bpy.ops.import_scene.obj(filepath=str(OBJ_PATH), axis_forward="Y", axis_up="Z")
    imported = [obj for obj in bpy.data.objects if obj not in before]
    for obj in imported:
        obj.select_set(True)
    return imported


def add_camera(camera_lock: dict) -> bpy.types.Object:
    suggested = camera_lock["suggested_camera"]
    location = suggested["location_xyz"]
    target = suggested["look_at_xyz"]
    lens = suggested["focal_length_mm"]
    resolution_x, resolution_y = suggested["resolution"]

    bpy.ops.object.camera_add(location=location)
    camera = bpy.context.object
    camera.name = camera_lock["camera_id"]
    camera.data.lens = lens
    camera.data.sensor_width = 32
    look_at(camera, target)

    bpy.context.scene.camera = camera
    bpy.context.scene.render.resolution_x = resolution_x
    bpy.context.scene.render.resolution_y = resolution_y
    return camera


def add_review_lighting() -> None:
    bpy.ops.object.light_add(type="AREA", location=(0.0, -2.8, 2.7))
    key = bpy.context.object
    key.name = "LIGHT_review_softbox_front"
    key.data.energy = 450
    key.data.size = 4.0

    bpy.ops.object.light_add(type="POINT", location=(0.0, -0.85, 2.02))
    bulb = bpy.context.object
    bulb.name = "LIGHT_review_arcade_warm_bulb"
    bulb.data.energy = 250
    bulb.data.color = (1.0, 0.78, 0.42)

    bpy.context.scene.world.color = (0.015, 0.015, 0.014)


def configure_scene() -> None:
    engines = {item.identifier for item in bpy.context.scene.render.bl_rna.properties["engine"].enum_items}
    if "BLENDER_EEVEE_NEXT" in engines:
        bpy.context.scene.render.engine = "BLENDER_EEVEE_NEXT"
    elif "BLENDER_EEVEE" in engines:
        bpy.context.scene.render.engine = "BLENDER_EEVEE"
    else:
        bpy.context.scene.render.engine = "BLENDER_WORKBENCH"

    bpy.context.scene.view_settings.view_transform = "Filmic"
    bpy.context.scene.view_settings.look = "Medium High Contrast"
    bpy.context.scene.frame_set(1)


def main() -> None:
    if not OBJ_PATH.exists():
        raise FileNotFoundError(OBJ_PATH)
    if not CAMERA_LOCK_PATH.exists():
        raise FileNotFoundError(CAMERA_LOCK_PATH)

    camera_lock = json.loads(CAMERA_LOCK_PATH.read_text(encoding="utf-8"))
    clear_scene()
    imported = import_obj()
    add_review_lighting()
    add_camera(camera_lock)
    configure_scene()

    BLEND_OUT.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_OUT))

    bpy.context.scene.render.filepath = str(PREVIEW_OUT)
    bpy.ops.render.render(write_still=True)

    print(f"imported_objects={len(imported)}")
    print(f"blend={BLEND_OUT}")
    print(f"preview={PREVIEW_OUT}")


if __name__ == "__main__":
    main()
