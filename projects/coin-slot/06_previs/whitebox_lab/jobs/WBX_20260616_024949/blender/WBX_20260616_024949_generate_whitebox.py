import json
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector


def arg_after(flag, default=""):
    if flag in sys.argv:
        index = sys.argv.index(flag)
        if index + 1 < len(sys.argv):
            return sys.argv[index + 1]
    return default


spec_path = Path(arg_after("--spec")).resolve()
spec = json.loads(spec_path.read_text(encoding="utf-8"))
project_root = Path(spec["project_root"]).resolve()
render_path = project_root / spec["suggested_render_path"]
blend_path = project_root / spec["suggested_blend_path"]
source_asset = spec.get("source_asset", {})
source_path = project_root / source_asset.get("path", "")
render_path.parent.mkdir(parents=True, exist_ok=True)
blend_path.parent.mkdir(parents=True, exist_ok=True)

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

scene = bpy.context.scene
try:
    scene.render.engine = "BLENDER_EEVEE_NEXT"
except Exception:
    scene.render.engine = "BLENDER_EEVEE"
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.eevee.taa_render_samples = 64 if hasattr(scene, "eevee") else 16
scene.view_settings.view_transform = "Standard"
scene.view_settings.look = "Medium High Contrast"
scene.world = bpy.data.worlds.new("WBX_gray_world") if not scene.world else scene.world
scene.world.color = (0.78, 0.80, 0.78)


def material(name, color, roughness=0.82):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = color
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = roughness
    return mat


mat_wall = material("WBX_plaster_wall_mid_gray", (0.62, 0.63, 0.60, 1))
mat_wall_dark = material("WBX_recess_shadow_gray", (0.31, 0.33, 0.32, 1))
mat_door = material("WBX_dark_metal_door", (0.23, 0.22, 0.19, 1))
mat_edge = material("WBX_chipped_edge_light", (0.78, 0.78, 0.72, 1))
mat_floor = material("WBX_old_concrete_floor", (0.45, 0.47, 0.45, 1))
mat_proxy = material("WBX_character_proxy_warm_white", (0.82, 0.80, 0.74, 1))
mat_proxy_mid = material("WBX_character_proxy_mid_gray", (0.68, 0.69, 0.64, 1))
mat_proxy_vest = material("WBX_character_proxy_front_vest", (0.58, 0.52, 0.40, 1))
mat_proxy_dark = material("WBX_character_proxy_dark", (0.40, 0.43, 0.42, 1))
mat_black = material("WBX_black_detail", (0.08, 0.08, 0.075, 1))
mat_mark = material("WBX_camera_match_markers", (0.95, 0.86, 0.55, 1))


def cube(name, loc, scale, mat, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    return obj


def cyl(name, loc, radius, depth, mat, rot=(0, 0, 0), vertices=48):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc, rotation=rot)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    return obj


def sphere(name, loc, radius, mat, scale=(1, 1, 1)):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=radius, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.data.materials.append(mat)
    return obj


def look_at(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def add_crack(name, x, z, length=0.55, angle=0.0):
    return cube(name, (x, 0.018, z), (0.018, 0.018, length), mat_black, rot=(0, 0, angle))


def add_child_proxy(name, x, zbase, height, depth_offset, head_turn=0.0, backpack=False, glasses=False, width=0.34, body_mat=None):
    y = depth_offset
    body_mat = body_mat or mat_proxy
    torso_h = height * 0.44
    leg_h = height * 0.34
    head_r = height * 0.095
    cube(f"{name}_torso", (x, y, zbase + leg_h + torso_h * 0.5), (width, 0.18, torso_h), body_mat)
    cube(f"{name}_left_leg", (x - width * 0.18, y, zbase + leg_h * 0.5), (width * 0.22, 0.15, leg_h), mat_proxy_dark)
    cube(f"{name}_right_leg", (x + width * 0.18, y, zbase + leg_h * 0.5), (width * 0.22, 0.15, leg_h), mat_proxy_dark)
    cube(f"{name}_neck", (x, y, zbase + leg_h + torso_h + 0.035), (width * 0.16, 0.12, 0.07), mat_proxy)
    head = sphere(f"{name}_head_turned_to_door", (x + math.sin(head_turn) * 0.04, y, zbase + leg_h + torso_h + head_r + 0.08), head_r, mat_proxy, scale=(0.92, 0.78, 1.08))
    head.rotation_euler[2] = head_turn
    cube(f"{name}_nose_direction_marker", (x + 0.04 + math.sin(head_turn) * 0.05, y - 0.08, zbase + leg_h + torso_h + head_r + 0.08), (0.05, 0.04, 0.025), mat_black)
    cube(f"{name}_left_arm", (x - width * 0.56, y, zbase + leg_h + torso_h * 0.48), (width * 0.16, 0.13, torso_h * 0.72), mat_proxy_dark, rot=(0.0, math.radians(0), math.radians(-8)))
    cube(f"{name}_right_arm", (x + width * 0.56, y, zbase + leg_h + torso_h * 0.48), (width * 0.16, 0.13, torso_h * 0.72), mat_proxy_dark, rot=(0.0, math.radians(0), math.radians(8)))
    if backpack:
        cube(f"{name}_backpack_block", (x - width * 0.42, y + 0.12, zbase + leg_h + torso_h * 0.52), (width * 0.28, 0.18, torso_h * 0.62), mat_wall_dark)
        cube(f"{name}_backpack_strap", (x - width * 0.18, y - 0.095, zbase + leg_h + torso_h * 0.58), (0.035, 0.03, torso_h * 0.78), mat_black)
    if glasses:
        cyl(f"{name}_glasses_left_ring", (x + 0.025, y - 0.087, zbase + leg_h + torso_h + head_r + 0.09), head_r * 0.35, 0.012, mat_black, rot=(math.radians(90), 0, 0), vertices=24)
        cyl(f"{name}_glasses_right_ring", (x + 0.092, y - 0.087, zbase + leg_h + torso_h + head_r + 0.09), head_r * 0.35, 0.012, mat_black, rot=(math.radians(90), 0, 0), vertices=24)
        cube(f"{name}_glasses_bridge", (x + 0.058, y - 0.095, zbase + leg_h + torso_h + head_r + 0.09), (0.045, 0.012, 0.01), mat_black)


# 16:9 camera-matched stage. The source image is kept as a non-rendering camera
# background in the .blend so the whitebox can be refined against it by hand.
cube("source_frame_floor_slab_left_to_door", (-0.1, -0.12, -0.04), (7.7, 4.7, 0.08), mat_floor, rot=(0, 0, math.radians(-1.2)))
cube("rear_plaster_wall_full_width", (0.45, 0.06, 1.55), (7.8, 0.12, 3.1), mat_wall)
cube("deep_black_passage_left_behind_boys", (-1.78, -0.02, 1.45), (0.48, 0.16, 2.9), mat_wall_dark)
cube("left_wall_plane_fading_to_edge", (-2.35, 0.0, 1.35), (0.45, 0.13, 2.7), mat_wall_dark)
cube("door_recess_vertical_light_pillar_left", (0.28, -0.035, 1.53), (0.21, 0.18, 3.05), mat_edge)
cube("right_cracked_plaster_plane", (1.86, 0.02, 1.52), (0.62, 0.14, 3.04), mat_wall)
door = cube("large_closed_dark_metal_door_matches_right_half", (0.92, -0.07, 1.48), (1.22, 0.18, 2.96), mat_door)
cube("thin_shadow_gap_between_wall_and_door", (0.46, -0.18, 1.48), (0.055, 0.08, 2.96), mat_black)
cube("door_bottom_darker_wear_band", (0.92, -0.175, 0.21), (1.22, 0.045, 0.34), mat_black)
cube("door_right_jamb_chipped_vertical", (1.56, -0.16, 1.42), (0.09, 0.18, 2.84), mat_edge)
cube("door_lock_plate", (1.42, -0.19, 0.98), (0.10, 0.035, 0.52), mat_black)
cyl("round_peephole_exact_upper_door_position", (0.84, -0.205, 1.97), 0.055, 0.028, mat_black, rot=(math.radians(90), 0, 0), vertices=48)
cyl("peephole_outer_ring", (0.84, -0.214, 1.97), 0.085, 0.014, mat_mark, rot=(math.radians(90), 0, 0), vertices=48)
cyl("door_handle_curved_proxy", (1.45, -0.225, 0.82), 0.035, 0.42, mat_black, rot=(math.radians(90), 0, math.radians(78)), vertices=24)
cube("small_lock_below_handle", (1.42, -0.22, 0.72), (0.08, 0.04, 0.1), mat_black)
cube("small_wall_hole_left_of_door", (-0.15, -0.07, 1.35), (0.13, 0.035, 0.09), mat_black)

add_crack("right_wall_primary_crack_vertical", 2.08, 2.05, 0.72, math.radians(-11))
add_crack("right_wall_secondary_crack", 1.9, 1.68, 0.45, math.radians(21))
add_crack("rear_wall_center_stain_line", -0.08, 2.02, 0.8, math.radians(-3))
add_crack("door_surface_vertical_stain_01", 0.72, 1.52, 0.9, math.radians(0))
add_crack("door_surface_vertical_stain_02", 1.18, 1.15, 0.7, math.radians(2))

add_child_proxy("older_brother_left_glasses_tall", -1.23, 0.0, 1.78, -0.55, head_turn=math.radians(-8), backpack=False, glasses=True, width=0.42, body_mat=mat_proxy)
add_child_proxy("middle_brother_center_backpack", -0.58, 0.0, 1.52, -0.57, head_turn=math.radians(-13), backpack=True, glasses=False, width=0.36, body_mat=mat_proxy_mid)
add_child_proxy("younger_brother_front_short_near_door", -0.08, 0.0, 1.24, -0.59, head_turn=math.radians(-17), backpack=False, glasses=False, width=0.34, body_mat=mat_proxy_vest)

# Camera and light match the source: eye-height, slight telephoto compression,
# boys occupy left third; door dominates right half.
bpy.ops.object.camera_add(location=(0.05, -6.35, 1.48))
camera = bpy.context.object
camera.name = "CAM_1to1_source_match_ACT1_SHOT_003"
camera.data.type = "ORTHO"
camera.data.ortho_scale = 3.28
camera.data.shift_x = 0.0
camera.data.shift_y = -0.005
look_at(camera, (0.03, -0.06, 1.34))
scene.camera = camera

if source_path.exists():
    try:
        image = bpy.data.images.load(str(source_path))
        bg = camera.data.background_images.new()
        bg.image = image
        bg.alpha = 0.22
        bg.display_depth = "BACK"
        bg.frame_method = "FIT"
    except Exception as exc:
        print(f"Could not load camera background: {exc}")

bpy.ops.object.empty_add(type="PLAIN_AXES", location=(0.35, -0.06, 1.34))
center = bpy.context.object
center.name = "source_image_composition_center"
for label, loc in {
    "source_left_boy_eye_line": (-1.23, -0.22, 1.55),
    "source_middle_boy_eye_line": (-0.58, -0.25, 1.38),
    "source_younger_boy_eye_line": (-0.08, -0.32, 1.14),
    "source_peephole_anchor": (0.84, -0.24, 1.97),
    "source_handle_anchor": (1.45, -0.24, 0.82),
}.items():
    sphere(f"match_marker_{label}", loc, 0.035, mat_mark)

bpy.ops.object.light_add(type="AREA", location=(-2.7, -3.4, 3.2))
key = bpy.context.object
key.name = "soft_overcast_left_key_from_source"
key.data.energy = 360
key.data.size = 4.8
bpy.ops.object.light_add(type="AREA", location=(1.6, -2.3, 2.2))
fill = bpy.context.object
fill.name = "very_soft_door_fill"
fill.data.energy = 45
fill.data.size = 3.2

for obj in bpy.context.scene.objects:
    obj["whitebox_tag"] = "replica_from_source_image"
    obj["source_asset"] = source_asset.get("asset_id", source_asset.get("path", ""))

scene.render.filepath = str(render_path)
bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
bpy.ops.render.render(write_still=True)
