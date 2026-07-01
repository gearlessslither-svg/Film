#!/usr/bin/env python3
"""Build a 24s Blender previs for the script-first opening one-take.

This is a director-camera playblast, not a final render. It locks the first
24 seconds as one continuous camera unit: blue sky and clouds -> track the
white bird -> reveal Jean's retro flying machine -> return to blue sky,
clouds, and the bird. AIGC rendering should use this animation/playblast as
the spatial and camera truth.
"""

from __future__ import annotations

import math
import os
from pathlib import Path

import bpy
from mathutils import Vector


PROJECT_ROOT = Path("/Users/jaychoupp/Story/Film/projects/blue-water-citypop-op")
BLEND_PATH = PROJECT_ROOT / "06_previs/blender/opening_24s_onetake_previs.blend"
VIDEO_PATH = PROJECT_ROOT / "06_previs/playblasts/opening_24s_onetake_previs.mp4"
STILL_DIR = PROJECT_ROOT / "06_previs/renders/opening_24s_onetake_frames"
ANIM_FRAME_DIR = PROJECT_ROOT / "06_previs/renders/opening_24s_onetake_animation_frames"

FPS = 24
START = 1
END = FPS * 24
RES_X = 1280
RES_Y = 548


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def mat(name: str, color: tuple[float, float, float, float], roughness: float = 0.55):
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = roughness
        if "Metallic" in bsdf.inputs:
            bsdf.inputs["Metallic"].default_value = 0.0
    material.diffuse_color = color
    return material


MAT_DOVE = None
MAT_DOVE_WING = None
MAT_EYE = None
MAT_CLOUD = None
MAT_WOOD = None
MAT_CANVAS = None
MAT_METAL = None
MAT_RED = None
MAT_SKY = None


def create_materials() -> None:
    global MAT_DOVE, MAT_DOVE_WING, MAT_EYE, MAT_CLOUD, MAT_WOOD, MAT_CANVAS, MAT_METAL, MAT_RED, MAT_SKY
    MAT_DOVE = mat("dove warm white", (0.96, 0.95, 0.9, 1.0), 0.78)
    MAT_DOVE_WING = mat("dove feather white", (1.0, 0.985, 0.94, 1.0), 0.85)
    MAT_EYE = mat("small dark eye", (0.02, 0.016, 0.012, 1.0), 0.35)
    MAT_CLOUD = mat("soft cloud white", (1.0, 0.98, 0.92, 1.0), 0.9)
    MAT_WOOD = mat("warm varnished wood", (0.38, 0.19, 0.07, 1.0), 0.5)
    MAT_CANVAS = mat("cream wing canvas", (0.82, 0.72, 0.52, 1.0), 0.88)
    MAT_METAL = mat("aged brass metal", (0.56, 0.43, 0.24, 1.0), 0.35)
    MAT_RED = mat("small red scarf accent", (0.8, 0.04, 0.025, 1.0), 0.55)
    MAT_SKY = mat("clear blue sky background", (0.36, 0.66, 1.0, 1.0), 0.95)
    bsdf = MAT_SKY.node_tree.nodes.get("Principled BSDF")
    if bsdf and "Emission Color" in bsdf.inputs:
        bsdf.inputs["Emission Color"].default_value = (0.36, 0.66, 1.0, 1.0)
        bsdf.inputs["Emission Strength"].default_value = 0.45


def add_uv_sphere(
    name: str,
    loc: tuple[float, float, float],
    scale: tuple[float, float, float],
    material,
    segments: int = 32,
    rings: int = 16,
):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.data.materials.append(material)
    return obj


def add_cube_scaled(name: str, loc, scale, material):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.data.materials.append(material)
    return obj


def add_cylinder(name: str, loc, radius: float, depth: float, material, vertices: int = 32, rotation=(0, 0, 0)):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    return obj


def set_key(obj, frame: int, loc=None, rot=None, scale=None) -> None:
    bpy.context.scene.frame_set(frame)
    if loc is not None:
        obj.location = loc
        obj.keyframe_insert(data_path="location", frame=frame)
    if rot is not None:
        obj.rotation_euler = rot
        obj.keyframe_insert(data_path="rotation_euler", frame=frame)
    if scale is not None:
        obj.scale = scale
        obj.keyframe_insert(data_path="scale", frame=frame)


def linearize_animation(obj) -> None:
    if not obj.animation_data or not obj.animation_data.action:
        return
    action = obj.animation_data.action
    curves = getattr(action, "fcurves", None)
    if curves is None:
        return
    for curve in curves:
        for key in curve.keyframe_points:
            key.interpolation = "SINE" if False else "LINEAR"


def create_world() -> None:
    scene = bpy.context.scene
    scene.frame_start = START
    scene.frame_end = END
    scene.frame_set(START)
    scene.render.fps = FPS
    scene.render.resolution_x = RES_X
    scene.render.resolution_y = RES_Y
    scene.render.resolution_percentage = 100
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    except Exception:
        scene.render.engine = "BLENDER_EEVEE"
    try:
        scene.view_settings.view_transform = "Standard"
        scene.view_settings.look = "Medium High Contrast"
        scene.view_settings.exposure = 0
        scene.view_settings.gamma = 1
    except Exception:
        pass
    scene.eevee.taa_render_samples = 32
    scene.eevee.use_raytracing = False
    world = scene.world or bpy.data.worlds.new("World")
    scene.world = world
    world.color = (0.36, 0.66, 1.0)

    bpy.ops.object.light_add(type="SUN", location=(0, 0, 12))
    sun = bpy.context.object
    sun.name = "OP sun - warm sky key"
    sun.rotation_euler = (math.radians(42), 0, math.radians(-35))
    sun.data.energy = 3.0
    sun.data.angle = math.radians(3.5)

    bpy.ops.object.light_add(type="AREA", location=(0, -5, 8))
    area = bpy.context.object
    area.name = "soft sky fill"
    area.data.energy = 230
    area.data.size = 9


def create_sky_backdrop():
    bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 24, 5.2), rotation=(math.radians(90), 0, 0))
    sky = bpy.context.object
    sky.name = "bright blue sky backdrop for previs readability"
    sky.scale = (90, 36, 1)
    sky.data.materials.append(MAT_SKY)
    return sky


def create_cloud_cluster(name: str, center: tuple[float, float, float], spread: float, count: int):
    parent = bpy.data.objects.new(name, None)
    bpy.context.collection.objects.link(parent)
    for i in range(count):
        angle = (i / max(1, count)) * math.tau
        r = spread * (0.25 + 0.75 * ((i * 37) % 100) / 100)
        x = center[0] + math.cos(angle) * r
        y = center[1] + math.sin(angle * 1.7) * r * 0.18
        z = center[2] + math.sin(angle * 0.9) * spread * 0.08
        sx = 0.6 + ((i * 13) % 7) * 0.12
        sy = 0.32 + ((i * 17) % 5) * 0.08
        sz = 0.18 + ((i * 19) % 4) * 0.04
        puff = add_uv_sphere(f"{name}_puff_{i:02d}", (x, y, z), (sx, sy, sz), MAT_CLOUD, 16, 8)
        puff.parent = parent
    return parent


def create_clouds():
    clusters = [
        ("cloud foreground left", (-8, 7.0, 4.1), 3.8, 18),
        ("cloud high sweep", (0, 11.5, 6.6), 5.2, 22),
        ("cloud right bank", (9, 8.6, 4.9), 4.4, 20),
        ("cloud far horizon", (0, 15.2, 3.0), 7.2, 26),
    ]
    objs = [create_cloud_cluster(*args) for args in clusters]
    for obj in objs:
        set_key(obj, START, loc=obj.location)
        set_key(obj, END, loc=obj.location + Vector((0.5, 0.1, 0.0)))
        linearize_animation(obj)
    return objs


def make_wing_mesh(name: str, side: float, material):
    mesh = bpy.data.meshes.new(name)
    verts = [
        (0.0, 0.0, 0.0),
        (side * 1.4, -0.05, 0.12),
        (side * 2.35, -0.02, 0.02),
        (side * 1.65, 0.06, -0.26),
        (side * 0.38, 0.04, -0.14),
    ]
    faces = [(0, 1, 2, 3, 4)]
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    return obj


def create_dove():
    bird = bpy.data.objects.new("WHITE_BIRD_RIG one-take path", None)
    bpy.context.collection.objects.link(bird)
    body = add_uv_sphere("dove body", (0, 0, 0), (0.45, 0.18, 0.22), MAT_DOVE, 32, 16)
    head = add_uv_sphere("dove head", (0.44, 0, 0.16), (0.18, 0.14, 0.14), MAT_DOVE, 24, 12)
    beak = add_cylinder("dove beak", (0.63, 0, 0.15), 0.025, 0.2, MAT_METAL, 12, rotation=(0, math.radians(90), 0))
    tail = make_wing_mesh("dove tail fan", -1, MAT_DOVE_WING)
    tail.location = (-0.43, 0, -0.02)
    tail.rotation_euler = (0, math.radians(4), math.radians(180))
    left_wing = make_wing_mesh("dove left wing animated", 1, MAT_DOVE_WING)
    right_wing = make_wing_mesh("dove right wing animated", -1, MAT_DOVE_WING)
    left_wing.location = (0.04, 0.08, 0.04)
    right_wing.location = (0.04, -0.08, 0.04)
    eye_l = add_uv_sphere("dove eye L", (0.57, -0.08, 0.21), (0.025, 0.018, 0.018), MAT_EYE, 12, 6)
    eye_r = add_uv_sphere("dove eye R", (0.57, 0.08, 0.21), (0.025, 0.018, 0.018), MAT_EYE, 12, 6)
    for part in [body, head, beak, tail, left_wing, right_wing, eye_l, eye_r]:
        part.parent = bird

    path_keys = [
        (1, Vector((-8.8, -2.2, 2.6)), (math.radians(6), 0, math.radians(-12)), (1.0, 1.0, 1.0)),
        (96, Vector((-2.5, -0.8, 3.1)), (math.radians(4), math.radians(2), math.radians(3)), (0.92, 0.92, 0.92)),
        (192, Vector((3.6, 0.4, 3.6)), (math.radians(0), math.radians(5), math.radians(10)), (0.78, 0.78, 0.78)),
        (312, Vector((8.2, 1.2, 4.4)), (math.radians(-3), math.radians(8), math.radians(18)), (0.58, 0.58, 0.58)),
        (430, Vector((3.0, 1.6, 4.8)), (math.radians(-1), math.radians(-6), math.radians(-155)), (0.45, 0.45, 0.45)),
        (576, Vector((-4.5, 2.0, 5.2)), (math.radians(0), math.radians(-8), math.radians(-172)), (0.38, 0.38, 0.38)),
    ]
    for frame, loc, rot, scale in path_keys:
        set_key(bird, frame, loc=loc, rot=rot, scale=scale)
    linearize_animation(bird)

    for frame in range(1, END + 1, 8):
        flap = math.sin(frame * 0.24) * math.radians(34)
        set_key(left_wing, frame, rot=(flap, 0, math.radians(8)))
        set_key(right_wing, frame, rot=(-flap, 0, math.radians(-8)))
    return bird


def create_flying_machine():
    rig = bpy.data.objects.new("JEAN_RETRO_FLYING_MACHINE_RIG", None)
    bpy.context.collection.objects.link(rig)
    fuselage = add_cylinder("wood fuselage", (0, 0, 0), 0.12, 1.8, MAT_WOOD, 24, rotation=(0, math.radians(90), 0))
    nose = add_uv_sphere("brass nose", (0.92, 0, 0), (0.18, 0.16, 0.16), MAT_METAL, 24, 12)
    tail = add_cube_scaled("tail rudder", (-0.92, 0, 0.18), (0.04, 0.42, 0.16), MAT_CANVAS)
    upper_wing = add_cube_scaled("canvas main wing", (0.04, 0, 0.28), (0.72, 2.55, 0.035), MAT_CANVAS)
    lower_wing = add_cube_scaled("lower canvas wing", (0.0, 0, -0.12), (0.56, 2.05, 0.025), MAT_CANVAS)
    strut1 = add_cube_scaled("left wing strut", (0.15, -0.9, 0.06), (0.025, 0.025, 0.42), MAT_WOOD)
    strut2 = add_cube_scaled("right wing strut", (0.15, 0.9, 0.06), (0.025, 0.025, 0.42), MAT_WOOD)
    prop = add_cube_scaled("propeller blur proxy", (1.12, 0, 0), (0.025, 0.9, 0.035), MAT_METAL)
    prop.parent = rig
    for part in [fuselage, nose, tail, upper_wing, lower_wing, strut1, strut2]:
        part.parent = rig
    for frame in range(1, END + 1, 6):
        set_key(prop, frame, rot=(0, math.radians(90), frame * 0.9))

    path = [
        (1, Vector((13, 5.2, 5.3)), (math.radians(1), math.radians(0), math.radians(185)), (0.7, 0.7, 0.7)),
        (160, Vector((9.0, 3.8, 5.0)), (math.radians(1), math.radians(-2), math.radians(190)), (0.82, 0.82, 0.82)),
        (245, Vector((2.8, 2.0, 4.2)), (math.radians(3), math.radians(-5), math.radians(198)), (1.0, 1.0, 1.0)),
        (335, Vector((-4.5, 1.0, 4.1)), (math.radians(4), math.radians(-8), math.radians(206)), (0.82, 0.82, 0.82)),
        (430, Vector((-10.0, 0.5, 4.7)), (math.radians(4), math.radians(-12), math.radians(214)), (0.55, 0.55, 0.55)),
        (576, Vector((-15.0, 0.0, 5.6)), (math.radians(4), math.radians(-14), math.radians(220)), (0.38, 0.38, 0.38)),
    ]
    for frame, loc, rot, scale in path:
        set_key(rig, frame, loc=loc, rot=rot, scale=scale)
    linearize_animation(rig)
    return rig


def create_camera():
    target = bpy.data.objects.new("CAMERA_TARGET_opening_bird_follow", None)
    bpy.context.collection.objects.link(target)

    bpy.ops.object.camera_add(location=(-7.0, -7.5, 3.2))
    cam = bpy.context.object
    cam.name = "CAMERA_opening_24s_one_take"
    cam.data.lens = 22
    cam.data.dof.use_dof = True
    cam.data.dof.aperture_fstop = 7.5
    cam.data.dof.focus_object = target
    constraint = cam.constraints.new(type="TRACK_TO")
    constraint.name = "look at opening action"
    constraint.target = target
    constraint.track_axis = "TRACK_NEGATIVE_Z"
    constraint.up_axis = "UP_Y"
    bpy.context.scene.camera = cam

    keys = [
        (1, Vector((-8.4, -7.8, 3.15)), Vector((-7.0, 0.0, 3.1)), 24),
        (80, Vector((-6.2, -7.1, 3.35)), Vector((-4.3, 0.1, 3.3)), 22),
        (155, Vector((-2.7, -6.9, 3.6)), Vector((-1.1, 0.55, 3.45)), 23),
        (245, Vector((0.7, -7.1, 3.9)), Vector((2.3, 1.15, 3.9)), 28),
        (345, Vector((3.2, -7.4, 4.2)), Vector((4.5, 1.45, 4.2)), 31),
        (450, Vector((0.6, -8.2, 4.55)), Vector((1.0, 1.0, 4.65)), 27),
        (576, Vector((-3.6, -8.9, 4.95)), Vector((-3.5, 1.2, 5.05)), 25),
    ]
    for frame, loc, target_loc, lens in keys:
        bpy.context.scene.frame_set(frame)
        cam.location = loc
        target.location = target_loc
        cam.data.lens = lens
        cam.keyframe_insert(data_path="location", frame=frame)
        target.keyframe_insert(data_path="location", frame=frame)
        cam.data.keyframe_insert(data_path="lens", frame=frame)
    linearize_animation(cam)
    linearize_animation(target)
    return cam


def add_timing_markers() -> None:
    markers = [
        (1, "00:00 blue sky cloud hold"),
        (49, "00:02 white bird enters"),
        (145, "00:06 tracking bird"),
        (217, "00:09 retro flying machine revealed"),
        (313, "00:13 flying machine crosses behind bird"),
        (433, "00:18 camera returns to sky and bird"),
        (576, "00:24 final blue sky cloud bird state"),
    ]
    scene = bpy.context.scene
    for frame, name in markers:
        marker = scene.timeline_markers.new(name, frame=frame)
        marker.camera = scene.camera


def set_origin_metadata() -> None:
    bpy.context.scene["script_first_unit_id"] = "VU_001_024_OPENING_SKY_BIRD_PLANE_ONETAKE"
    bpy.context.scene["director_intent"] = (
        "24s one-take previs: blue sky and clouds, track white bird, reveal Jean-style retro flying machine, "
        "return to blue sky, clouds, and bird."
    )
    bpy.context.scene["aigc_policy"] = (
        "Use this Blender camera animation/playblast as the motion and spatial truth before AIGC rendering."
    )


def render_animation() -> None:
    scene = bpy.context.scene
    ANIM_FRAME_DIR.mkdir(parents=True, exist_ok=True)
    scene.render.filepath = str(ANIM_FRAME_DIR / "opening_24s_")
    scene.render.image_settings.file_format = "PNG"
    if hasattr(scene.render, "use_motion_blur"):
        scene.render.use_motion_blur = True
    if hasattr(scene.eevee, "use_motion_blur"):
        scene.eevee.use_motion_blur = True
    if hasattr(scene.eevee, "motion_blur_shutter"):
        scene.eevee.motion_blur_shutter = 0.35
    bpy.ops.render.render(animation=True, write_still=False)


def save_key_stills() -> None:
    STILL_DIR.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    old_format = scene.render.image_settings.file_format
    old_filepath = scene.render.filepath
    scene.render.image_settings.file_format = "PNG"
    for frame in [1, 49, 145, 217, 313, 433, 576]:
        scene.frame_set(frame)
        scene.render.filepath = str(STILL_DIR / f"opening_24s_frame_{frame:04d}.png")
        bpy.ops.render.render(write_still=True)
    scene.render.image_settings.file_format = old_format
    scene.render.filepath = old_filepath


def main() -> None:
    clear_scene()
    create_materials()
    create_world()
    create_sky_backdrop()
    create_clouds()
    create_dove()
    create_flying_machine()
    create_camera()
    add_timing_markers()
    set_origin_metadata()
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    save_key_stills()
    if os.environ.get("OPENING_PREVIS_STILLS_ONLY") != "1":
        render_animation()
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))


if __name__ == "__main__":
    main()
