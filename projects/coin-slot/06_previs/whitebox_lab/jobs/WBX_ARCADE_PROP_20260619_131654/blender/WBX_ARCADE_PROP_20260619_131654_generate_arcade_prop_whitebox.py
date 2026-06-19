import math
from pathlib import Path

import bpy


PROJECT_ROOT = Path("/Users/jaychoupp/Desktop/Story/Film/projects/coin-slot")
JOB_DIR = PROJECT_ROOT / "06_previs/whitebox_lab/jobs/WBX_ARCADE_PROP_20260619_131654"
RENDER_PATH = JOB_DIR / "renders/WBX_ARCADE_PROP_20260619_131654_arcade_cabinet_whitebox.png"
BLEND_PATH = JOB_DIR / "blender/WBX_ARCADE_PROP_20260619_131654.blend"


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def material(name, color):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = color
    return mat


def cube(name, loc, scale, mat):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    return obj


def cyl(name, loc, radius, depth, mat, vertices=48):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    return obj


def sphere(name, loc, radius, mat):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=radius, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    return obj


clear_scene()

mat_body = material("WBX_arcade_body_matte_gray", (0.56, 0.57, 0.55, 1))
mat_panel = material("WBX_control_panel_mid_gray", (0.43, 0.44, 0.43, 1))
mat_dark = material("WBX_screen_dark_glass", (0.04, 0.055, 0.06, 1))
mat_glow = material("WBX_screen_glow_teal", (0.12, 0.65, 0.78, 1))
mat_button = material("WBX_button_light_markers", (0.86, 0.82, 0.70, 1))
mat_coin = material("WBX_coin_slot_marker", (0.92, 0.78, 0.32, 1))
mat_stool = material("WBX_player_stool_gray", (0.48, 0.49, 0.47, 1))
mat_axis = material("WBX_spatial_axis_markers", (0.95, 0.36, 0.22, 1))

# Cabinet measured in simple production units: X width, Y depth, Z height.
cabinet = cube("fixed_two_player_arcade_cabinet_body", (0, 0, 1.18), (2.15, 0.92, 2.36), mat_body)
base = cube("recessed_lower_base", (0, -0.03, 0.22), (2.05, 0.82, 0.38), mat_panel)
screen_housing = cube("single_shared_crt_screen_housing", (0, -0.48, 1.68), (1.72, 0.10, 0.92), mat_dark)
screen_glow = cube("single_shared_crt_visible_screen_plane", (0, -0.535, 1.68), (1.42, 0.035, 0.64), mat_glow)
bezel_top = cube("thick_crt_top_bezel", (0, -0.525, 2.05), (1.64, 0.06, 0.08), mat_panel)
bezel_bottom = cube("thick_crt_bottom_bezel", (0, -0.525, 1.31), (1.64, 0.06, 0.08), mat_panel)
bezel_left = cube("thick_crt_left_bezel", (-0.86, -0.525, 1.68), (0.08, 0.06, 0.82), mat_panel)
bezel_right = cube("thick_crt_right_bezel", (0.86, -0.525, 1.68), (0.08, 0.06, 0.82), mat_panel)

control_deck = cube("wide_two_player_control_panel", (0, -0.74, 0.92), (2.18, 0.55, 0.18), mat_panel)
control_deck.rotation_euler[0] = math.radians(-8)
control_deck["whitebox_note"] = "Players sit side-by-side facing this deck and the single shared CRT screen."

front_coin_panel = cube("front_coin_slot_access_panel", (0, -0.94, 0.64), (0.58, 0.045, 0.44), mat_panel)
coin_slot = cube("center_coin_slot_marker", (0, -0.975, 0.72), (0.34, 0.025, 0.06), mat_coin)

player_x = [-0.55, 0.55]
for side, x in zip(["left_player_A_Lei", "right_player_yellow_hair"], player_x):
    joystick_stem = cyl(f"{side}_joystick_stem", (x - 0.22, -0.80, 1.05), 0.035, 0.22, mat_dark)
    joystick_stem.rotation_euler[0] = math.radians(90)
    sphere(f"{side}_joystick_ball", (x - 0.22, -0.92, 1.09), 0.07, mat_axis)
    for row in range(2):
        for col in range(3):
            button_x = x + 0.03 + col * 0.12
            button_y = -0.91 - row * 0.10
            button_z = 1.045 + row * 0.004
            cyl(f"{side}_button_{row}_{col}", (button_x, button_y, button_z), 0.036, 0.022, mat_button, vertices=32)

for side, x in zip(["A_Lei_stool_left", "yellow_hair_stool_right"], player_x):
    cyl(f"{side}_seat", (x, -1.42, 0.45), 0.23, 0.08, mat_stool)
    cyl(f"{side}_stool_post", (x, -1.42, 0.24), 0.055, 0.36, mat_stool)
    cube(f"{side}_stool_foot", (x, -1.42, 0.045), (0.42, 0.42, 0.05), mat_stool)

# Head-position markers for rear-camera duel shots.
for label, x in [("A_Lei_head_position_when_seated", -0.55), ("yellow_hair_head_position_when_seated", 0.55)]:
    sphere(label, (x, -1.42, 1.36), 0.13, mat_axis)
    cube(label + "_shoulder_axis", (x, -1.42, 1.13), (0.42, 0.08, 0.08), mat_axis)

floor = cube("floor_plane_for_scale", (0, -0.55, -0.015), (3.4, 2.7, 0.03), mat_body)

bpy.ops.object.light_add(type="AREA", location=(0, -3.2, 4.0))
key = bpy.context.object
key.name = "large_soft_arcade_whitebox_key"
key.data.energy = 520
key.data.size = 4.0

bpy.ops.object.light_add(type="POINT", location=(0, -0.8, 1.68))
screen_light = bpy.context.object
screen_light.name = "single_crt_screen_glow_source"
screen_light.data.energy = 80
screen_light.data.color = (0.35, 0.9, 1.0)

bpy.ops.object.camera_add(location=(3.4, -5.4, 2.55), rotation=(math.radians(62), 0, math.radians(34)))
camera = bpy.context.object
bpy.context.scene.camera = camera
camera.name = "camera_three_quarter_prop_lock"
camera.data.lens = 26

for obj in bpy.context.scene.objects:
    obj["whitebox_tag"] = "arcade_cabinet_prop_lock"
    obj["source_asset"] = "BIBLE_PROP_ARCADE_CABINET_LOCK_v001_c03"

scene = bpy.context.scene
scene.render.engine = "BLENDER_EEVEE"
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
if hasattr(scene, "eevee"):
    scene.eevee.taa_render_samples = 64
scene.view_settings.view_transform = "Filmic"
scene.view_settings.look = "Medium High Contrast"
scene.render.filepath = str(RENDER_PATH)

bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
bpy.ops.render.render(write_still=True)
