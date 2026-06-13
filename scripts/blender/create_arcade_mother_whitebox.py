from pathlib import Path
import math

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "environment_lookdev" / "SCN_ARCADE" / "whitebox"
BLEND_OUT = ROOT / "blender" / "arcade_mother_whitebox_v001.blend"
RENDER_OUT = OUT_DIR / "SCN_ARCADE_blender_whitebox_mother_camera_v001.png"


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def mat(name, color):
    material = bpy.data.materials.new(name)
    material.diffuse_color = color
    return material


MAT_FLOOR = mat("MAT_floor_wet_gray", (0.22, 0.22, 0.20, 1.0))
MAT_WALL = mat("MAT_peeling_wall_gray", (0.47, 0.46, 0.42, 1.0))
MAT_CEILING = mat("MAT_low_ceiling_gray", (0.34, 0.34, 0.31, 1.0))
MAT_CAB = mat("MAT_black_arcade_cabinet", (0.035, 0.038, 0.040, 1.0))
MAT_CAB_FACE = mat("MAT_worn_cabinet_face", (0.13, 0.12, 0.10, 1.0))
MAT_CURTAIN = mat("MAT_dirty_plastic_curtain", (0.30, 0.29, 0.26, 0.72))
MAT_STOOL = mat("MAT_old_wood_stool", (0.22, 0.17, 0.12, 1.0))
MAT_METAL = mat("MAT_dark_wire_metal", (0.025, 0.025, 0.024, 1.0))
MAT_LIGHT = mat("MAT_warm_bulb", (1.0, 0.80, 0.36, 1.0))
MAT_BLUE = mat("MAT_screen_blue", (0.05, 0.42, 0.75, 1.0))
MAT_GREEN = mat("MAT_screen_green", (0.05, 0.55, 0.33, 1.0))
MAT_RED = mat("MAT_screen_red", (0.75, 0.14, 0.10, 1.0))
MAT_GOLD = mat("MAT_screen_gold", (0.80, 0.55, 0.10, 1.0))
MAT_PURPLE = mat("MAT_screen_purple", (0.40, 0.15, 0.75, 1.0))
MAT_CONTROL = mat("MAT_control_panel", (0.18, 0.16, 0.13, 1.0))


def look_at(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def cube(name, loc, scale, material, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)
    return obj


def plane_box(name, loc, scale, material, rot=(0, 0, 0)):
    return cube(name, loc, scale, material, rot)


def add_cylinder(name, loc, radius, depth, material, rot=(0, 0, 0), vertices=24):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc, rotation=rot)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    return obj


def add_line(name, points, bevel, material):
    curve = bpy.data.curves.new(name, "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 2
    curve.bevel_depth = bevel
    curve.bevel_resolution = 2
    poly = curve.splines.new("POLY")
    poly.points.add(len(points) - 1)
    for p, co in zip(poly.points, points):
        p.co = (co[0], co[1], co[2], 1)
    obj = bpy.data.objects.new(name, curve)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    return obj


def add_screen_detail(prefix, loc, width, height, material):
    x, y, z = loc
    screen = cube(prefix + "_screen", (x, y, z), (width, 0.018, height), material)
    for i in range(4):
        zline = z - height * 0.32 + i * height * 0.21
        cube(prefix + f"_scanline_{i}", (x, y - 0.012, zline), (width * 0.86, 0.012, height * 0.018), MAT_LIGHT)
    return screen


def add_buttons(prefix, x, y, z, side=1, scale=1.0):
    add_cylinder(prefix + "_stick", (x - side * 0.18 * scale, y, z + 0.045 * scale), 0.035 * scale, 0.09 * scale, MAT_RED, vertices=16)
    for i, material in enumerate((MAT_RED, MAT_GOLD, MAT_BLUE, MAT_GREEN)):
        add_cylinder(
            prefix + f"_button_{i}",
            (x + side * (0.03 + 0.08 * i) * scale, y, z + 0.030 * scale),
            0.028 * scale,
            0.030 * scale,
            material,
            vertices=16,
        )


def add_arcade_cabinet(prefix, x, y, yaw, screen_mat, scale=1.0):
    rot = (0, 0, yaw)
    # Cabinet is built in local-ish chunks; yaw only needs to read correctly from mother camera.
    body = cube(prefix + "_body", (x, y, 0.98 * scale), (0.78 * scale, 0.62 * scale, 1.72 * scale), MAT_CAB, rot)
    cube(prefix + "_base", (x, y + 0.03 * scale, 0.28 * scale), (0.86 * scale, 0.68 * scale, 0.56 * scale), MAT_CAB_FACE, rot)
    cube(prefix + "_marquee", (x, y - 0.22 * scale, 1.78 * scale), (0.82 * scale, 0.10 * scale, 0.18 * scale), screen_mat, rot)
    cube(prefix + "_bezel", (x, y - 0.31 * scale, 1.28 * scale), (0.66 * scale, 0.06 * scale, 0.52 * scale), MAT_CAB_FACE, rot)
    add_screen_detail(prefix, (x, y - 0.35 * scale, 1.30 * scale), 0.54 * scale, 0.36 * scale, screen_mat)
    cube(prefix + "_control_panel", (x, y - 0.38 * scale, 0.88 * scale), (0.72 * scale, 0.22 * scale, 0.10 * scale), MAT_CONTROL, rot)
    add_buttons(prefix, x, y - 0.50 * scale, 0.95 * scale, 1 if x < 0 else -1, scale)
    return body


def add_double_cabinet():
    cube("BACK_double_fighting_cabinet_body", (0.0, 3.72, 0.98), (1.65, 0.58, 1.58), MAT_CAB)
    cube("BACK_double_fighting_cabinet_marquee", (0.0, 3.42, 1.78), (1.72, 0.10, 0.18), MAT_CAB_FACE)
    add_screen_detail("BACK_left_fictional_fighter", (-0.42, 3.34, 1.28), 0.62, 0.42, MAT_BLUE)
    add_screen_detail("BACK_right_fictional_fighter", (0.42, 3.34, 1.28), 0.62, 0.42, MAT_RED)
    cube("BACK_double_control_panel", (0.0, 3.22, 0.83), (1.56, 0.28, 0.10), MAT_CONTROL)
    add_buttons("BACK_left_controls", -0.38, 3.06, 0.91, 1, 0.85)
    add_buttons("BACK_right_controls", 0.38, 3.06, 0.91, -1, 0.85)
    for x in (-0.56, -0.30, 0.30, 0.56):
        add_cylinder("BACK_screen_fighter_proxy", (x, 3.00, 1.28), 0.045, 0.16, MAT_LIGHT, vertices=12)


def add_stool(prefix, x, y, scale=1.0):
    add_cylinder(prefix + "_seat", (x, y, 0.46 * scale), 0.16 * scale, 0.065 * scale, MAT_STOOL, vertices=18)
    for dx, dy in ((-0.10, -0.07), (0.10, -0.07), (-0.10, 0.07), (0.10, 0.07)):
        cube(prefix + f"_leg_{dx}_{dy}", (x + dx * scale, y + dy * scale, 0.23 * scale), (0.035 * scale, 0.035 * scale, 0.44 * scale), MAT_STOOL)


def add_plastic_curtain():
    # Foreground dirty plastic strips, intentionally very close to camera.
    for i, x in enumerate([-2.58, -2.28, -2.02, 2.05, 2.34, 2.62]):
        strip = cube(f"FG_dirty_plastic_strip_{i}", (x, -4.76, 1.25), (0.18, 0.035, 2.65), MAT_CURTAIN, (0, 0, math.radians(2 if x < 0 else -2)))
        strip.show_transparent = True


def add_room_shell():
    cube("FLOOR_wet_narrow_aisle", (0, 0.0, -0.025), (5.2, 9.4, 0.05), MAT_FLOOR)
    cube("CEILING_low_stained", (0, 0.0, 2.23), (5.2, 9.4, 0.06), MAT_CEILING)
    cube("LEFT_peeling_wall", (-2.62, 0.0, 1.08), (0.08, 9.4, 2.20), MAT_WALL)
    cube("RIGHT_peeling_wall", (2.62, 0.0, 1.08), (0.08, 9.4, 2.20), MAT_WALL)
    cube("BACK_dirty_wall", (0.0, 4.62, 1.08), (5.2, 0.08, 2.20), MAT_WALL)
    cube("BACK_small_window", (0.0, 4.56, 1.55), (0.58, 0.04, 0.32), MAT_GREEN)
    cube("BACK_poster_cluster_left", (-1.55, 4.54, 1.36), (0.58, 0.035, 0.75), MAT_CAB_FACE)
    cube("BACK_poster_cluster_right", (1.45, 4.54, 1.30), (0.65, 0.035, 0.86), MAT_CAB_FACE)
    # Patchy wall scars.
    for i, (x, y, z, sx, sz) in enumerate([
        (-2.57, -2.2, 1.25, 0.03, 0.54),
        (2.57, -1.6, 1.32, 0.03, 0.48),
        (-2.57, 1.9, 1.05, 0.03, 0.70),
        (2.57, 2.2, 1.08, 0.03, 0.62),
        (-0.9, 4.55, 1.06, 0.55, 0.34),
        (0.95, 4.55, 0.90, 0.62, 0.28),
    ]):
        cube(f"WALL_peeling_patch_{i}", (x, y, z), (sx, 0.02 if abs(x) < 1 else 0.42, sz), MAT_CEILING)


def add_lights_and_wires():
    bpy.ops.object.light_add(type="POINT", location=(0.0, -0.85, 2.02))
    bulb = bpy.context.object
    bulb.name = "LIGHT_dirty_warm_bulb"
    bulb.data.energy = 450
    bulb.data.color = (1.0, 0.78, 0.42)
    add_cylinder("BULB_visible", (0.0, -0.85, 1.92), 0.06, 0.10, MAT_LIGHT, vertices=18)

    for x, y, color in [(-1.7, 0.7, (0.2, 0.5, 1.0)), (1.65, 0.5, (1.0, 0.28, 0.18)), (0.0, 3.25, (0.2, 0.55, 1.0))]:
        bpy.ops.object.light_add(type="POINT", location=(x, y, 1.25))
        l = bpy.context.object
        l.name = f"LIGHT_CRT_spill_{x}_{y}"
        l.data.energy = 85
        l.data.color = color

    for pts in [
        [(-2.40, -4.0, 2.08), (-1.2, -1.2, 2.05), (0.4, 0.1, 2.12), (2.35, 1.1, 2.00)],
        [(-2.35, -2.0, 1.95), (-0.6, -0.7, 1.92), (1.1, 0.2, 1.98), (2.35, 2.4, 1.90)],
        [(-1.8, 4.54, 1.95), (-0.2, 4.40, 2.05), (1.8, 4.54, 1.90)],
    ]:
        add_line("CEILING_sagging_wire", pts, 0.012, MAT_METAL)

    add_cylinder("CEILING_fan_hub", (0.0, 0.30, 2.14), 0.08, 0.06, MAT_METAL, vertices=18)
    for i, angle in enumerate((0, 120, 240)):
        cube(f"CEILING_fan_blade_{i}", (0.0, 0.30, 2.14), (0.70, 0.06, 0.018), MAT_METAL, (0, 0, math.radians(angle)))


def build_scene():
    clear_scene()
    add_room_shell()
    add_plastic_curtain()

    # Rows are laid out to match the mother image: two compressed banks and a target cabinet at the end.
    left_positions = [(-1.95, -2.55, 0.88, MAT_GREEN), (-1.72, -1.52, 0.80, MAT_RED), (-1.48, -0.55, 0.70, MAT_BLUE), (-1.25, 0.34, 0.60, MAT_GOLD), (-1.06, 1.12, 0.52, MAT_GREEN)]
    right_positions = [(1.95, -2.40, 0.88, MAT_BLUE), (1.72, -1.34, 0.78, MAT_PURPLE), (1.48, -0.44, 0.68, MAT_RED), (1.25, 0.40, 0.58, MAT_GOLD), (1.06, 1.18, 0.50, MAT_GREEN)]
    for idx, (x, y, s, material) in enumerate(left_positions):
        add_arcade_cabinet(f"LEFT_cabinet_{idx}", x, y, math.radians(-8), material, s)
    for idx, (x, y, s, material) in enumerate(right_positions):
        add_arcade_cabinet(f"RIGHT_cabinet_{idx}", x, y, math.radians(8), material, s)

    add_double_cabinet()

    for idx, (x, y, s) in enumerate([
        (-1.38, -2.78, 0.95),
        (1.33, -2.55, 0.95),
        (-0.85, -0.90, 0.78),
        (0.86, -0.70, 0.78),
        (-0.40, 1.15, 0.62),
        (0.42, 1.18, 0.62),
        (0.0, 2.75, 0.55),
    ]):
        add_stool(f"STOOL_{idx}", x, y, s)

    add_lights_and_wires()

    # Camera-matched mother view: centered in the plastic curtain, low enough to preserve wet floor wedge.
    bpy.ops.object.camera_add(location=(0.0, -5.18, 1.32), rotation=(math.radians(77), 0, 0))
    camera = bpy.context.object
    camera.name = "CAM_SCN_ARCADE_MOTHER_MATCH"
    camera.data.lens = 20
    camera.data.sensor_width = 32
    look_at(camera, (0.0, 0.10, 1.12))
    bpy.context.scene.camera = camera

    bpy.context.scene.render.engine = "BLENDER_EEVEE_NEXT"
    bpy.context.scene.eevee.taa_render_samples = 64
    bpy.context.scene.render.resolution_x = 1672
    bpy.context.scene.render.resolution_y = 941
    bpy.context.scene.view_settings.view_transform = "Filmic"
    bpy.context.scene.view_settings.look = "Medium High Contrast"
    bpy.context.scene.world.color = (0.015, 0.015, 0.014)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_scene()
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_OUT))
    bpy.context.scene.render.filepath = str(RENDER_OUT)
    bpy.ops.render.render(write_still=True)
    print(f"blend={BLEND_OUT}")
    print(f"render={RENDER_OUT}")


if __name__ == "__main__":
    main()
