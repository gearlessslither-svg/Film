import csv
import math
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[1]
BLENDER_DIR = ROOT / "blender"
RENDER_DIR = ROOT / "whitebox_renders"
BLEND_PATH = BLENDER_DIR / "coin_slot_whitebox.blend"
MANIFEST_PATH = BLENDER_DIR / "camera_manifest.csv"


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def make_mat(name, color, roughness=0.55, emission=None, strength=0.0):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = roughness
        if emission:
            bsdf.inputs["Emission Color"].default_value = emission
            bsdf.inputs["Emission Strength"].default_value = strength
    return mat


def cube(name, loc, scale, mat, collection=None, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if mat:
        obj.data.materials.append(mat)
    if collection:
        link_to_collection(obj, collection)
    return obj


def link_to_collection(obj, collection):
    if obj.name not in collection.objects:
        collection.objects.link(obj)
    for col in list(obj.users_collection):
        if col != collection:
            col.objects.unlink(obj)


def text_label(name, text, loc, size, mat, collection=None, rot=(math.radians(90), 0, 0)):
    # Keep whitebox renders clean for image-to-image references; camera_manifest.csv stores labels.
    return None


def look_at(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def add_area_light(name, loc, target, power, size, color):
    bpy.ops.object.light_add(type="AREA", location=loc)
    light = bpy.context.object
    light.name = name
    light.data.energy = power
    light.data.size = size
    light.data.color = color
    look_at(light, target)
    return light


def add_camera(name, loc, target, lens=28, ortho=False, ortho_scale=6.0):
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.object
    cam.name = name
    look_at(cam, target)
    cam.data.lens = lens
    if ortho:
        cam.data.type = "ORTHO"
        cam.data.ortho_scale = ortho_scale
    return cam


def arcade_cabinet(name, x, y, face, col, mats):
    base = cube(f"{name}_body", (x, y, 0.85), (0.75, 0.72, 1.7), mats["dark"], col, rot=(0, 0, face))
    sx = x + math.sin(face) * 0.39
    sy = y - math.cos(face) * 0.39
    screen = cube(f"{name}_screen", (sx, sy, 1.15), (0.50, 0.04, 0.38), mats["screen"], col, rot=(0, 0, face))
    panel = cube(f"{name}_buttons", (sx, sy, 0.72), (0.55, 0.04, 0.18), mats["red"], col, rot=(0, 0, face))
    return base, screen, panel


def make_collections():
    names = ["COMPOUND", "ARCADE", "EXTERIOR", "ALLEY", "CORRIDOR_PHONE", "EIGHT_BIT_STAGE", "CAMERAS_MARKERS"]
    result = {}
    for name in names:
        col = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(col)
        result[name] = col
    return result


def build_compound(cols, mats):
    col = cols["COMPOUND"]
    ox = -17
    oy = 0
    # Old residential compound corner: arcade is a ground-floor room tucked in a remote corner.
    cube("COMP_courtyard_floor", (ox, oy, -0.05), (14, 10, 0.1), mats["floor"], col)
    cube("COMP_old_apartment_back", (ox, oy + 4.8, 2.2), (13.5, 0.22, 4.4), mats["wall"], col)
    cube("COMP_old_apartment_left", (ox - 6.8, oy, 2.2), (0.22, 9.6, 4.4), mats["wall"], col)
    cube("COMP_arcade_corner_room", (ox + 3.2, oy + 3.6, 1.55), (3.6, 1.4, 3.1), mats["concrete"], col)
    cube("COMP_arcade_hidden_door_glow", (ox + 3.2, oy + 2.86, 1.15), (1.25, 0.06, 2.05), mats["screen"], col)
    cube("COMP_arcade_tiny_sign", (ox + 3.2, oy + 2.80, 2.75), (2.4, 0.06, 0.35), mats["red"], col)
    cube("COMP_stairwell_dark_opening", (ox - 4.9, oy + 4.66, 1.25), (1.4, 0.08, 2.2), mats["dark"], col)
    cube("COMP_notice_board", (ox - 1.5, oy + 4.65, 1.45), (1.8, 0.06, 1.1), mats["yellow"], col)
    for idx, x in enumerate([-5.2, -2.6, 0.0, 2.6]):
        cube(f"COMP_window_back_{idx+1}", (ox + x, oy + 4.66, 2.75), (1.1, 0.05, 0.7), mats["metal"], col)
    for idx, y in enumerate([-3.2, -1.5, 0.2, 1.9]):
        cube(f"COMP_pipe_left_{idx+1}", (ox - 6.68, oy + y, 1.9), (0.06, 0.06, 3.4), mats["metal"], col)
    cube("COMP_clothesline_1", (ox - 1.8, oy + 2.4, 2.65), (5.2, 0.04, 0.04), mats["metal"], col)
    cube("COMP_clothesline_hanging_cloth_1", (ox - 2.8, oy + 2.4, 2.2), (0.6, 0.05, 0.7), mats["translucent"], col)
    cube("COMP_clothesline_hanging_cloth_2", (ox - 0.6, oy + 2.4, 2.15), (0.7, 0.05, 0.85), mats["translucent"], col)
    cube("COMP_weeds_corner", (ox + 5.0, oy + 1.5, 0.15), (1.4, 0.7, 0.3), mats["green"], col)
    cube("COMP_bicycle_frame", (ox + 0.4, oy - 2.3, 0.45), (1.6, 0.12, 0.9), mats["metal"], col)
    # Older brother-like boy leads two younger brothers. No girls in this group.
    cube("CHAR_older_brother_anchor", (ox - 1.1, oy - 2.3, 0.9), (0.42, 0.28, 1.35), mats["boy"], col)
    cube("CHAR_younger_brother_1_anchor", (ox - 1.8, oy - 2.95, 0.72), (0.32, 0.22, 1.05), mats["boy"], col)
    cube("CHAR_younger_brother_2_anchor", (ox - 0.45, oy - 3.05, 0.72), (0.32, 0.22, 1.05), mats["boy"], col)
    cube("PATH_compound_to_arcade_corner", (ox + 0.9, oy + 0.15, 0.03), (0.14, 6.7, 0.06), mats["path"], col, rot=(0, 0, math.radians(-26)))
    text_label("LABEL_COMPOUND", "OLD RESIDENTIAL COMPOUND / remote ground-floor arcade corner", (ox, oy - 0.7, 0.06), 0.28, mats["label"], col)


def build_arcade(cols, mats):
    col = cols["ARCADE"]
    # Room shell: entrance at negative Y, machine rows on both sides.
    cube("ARCADE_floor_10x7", (0, 0, -0.05), (10, 7, 0.1), mats["floor"], col)
    cube("ARCADE_back_wall", (0, 3.5, 1.6), (10, 0.15, 3.2), mats["wall"], col)
    cube("ARCADE_left_wall", (-5, 0, 1.6), (0.15, 7, 3.2), mats["wall"], col)
    cube("ARCADE_right_wall", (5, 0, 1.6), (0.15, 7, 3.2), mats["wall"], col)
    cube("ARCADE_front_left_wall", (-3.4, -3.5, 1.6), (3.2, 0.15, 3.2), mats["wall"], col)
    cube("ARCADE_front_right_wall", (3.4, -3.5, 1.6), (3.2, 0.15, 3.2), mats["wall"], col)
    cube("ARCADE_ceiling_low", (0, 0, 3.22), (10, 7, 0.08), mats["ceiling"], col)
    cube("ARCADE_dirty_plastic_curtain_left_strip", (-0.85, -3.55, 1.45), (0.22, 0.05, 2.1), mats["translucent"], col)
    cube("ARCADE_dirty_plastic_curtain_right_strip", (0.85, -3.55, 1.45), (0.22, 0.05, 2.1), mats["translucent"], col)
    cube("ARCADE_owner_counter", (3.65, 2.25, 0.6), (2.0, 0.65, 1.2), mats["wood"], col)
    cube("ARCADE_faded_poster_wall", (-2.5, 3.42, 1.85), (2.2, 0.04, 1.0), mats["yellow"], col)
    for idx, y in enumerate([-2.2, -1.0, 0.2, 1.4]):
        arcade_cabinet(f"ARCADE_left_cab_{idx+1}", -4.35, y, math.radians(90), col, mats)
        arcade_cabinet(f"ARCADE_right_cab_{idx+1}", 4.35, y, math.radians(-90), col, mats)
    for idx, x in enumerate([-2.2, 0.0, 2.2]):
        arcade_cabinet(f"ARCADE_back_cab_{idx+1}", x, 2.75, 0, col, mats)
    # Hero Street Fighter cabinet: conflict anchor.
    cube("ARCADE_STREET_FIGHTER_body", (0, -0.35, 0.9), (1.4, 0.85, 1.8), mats["dark"], col)
    cube("ARCADE_STREET_FIGHTER_screen", (0, -0.82, 1.25), (0.95, 0.05, 0.55), mats["screen"], col)
    cube("ARCADE_STREET_FIGHTER_two_player_panel", (0, -0.86, 0.72), (1.25, 0.08, 0.24), mats["red"], col)
    # Three boys only: an older brother-like boy leads two younger brothers.
    cube("CHAR_older_brother_arcade_anchor", (-0.45, -1.35, 0.9), (0.42, 0.28, 1.35), mats["boy"], col)
    cube("CHAR_protagonist_arcade_anchor", (-1.15, -1.85, 0.72), (0.32, 0.22, 1.05), mats["boy"], col)
    cube("CHAR_younger_brother_arcade_anchor", (-1.65, -2.25, 0.64), (0.28, 0.20, 0.95), mats["boy"], col)
    cube("CHAR_green_schoolbag_anchor", (-1.15, -2.05, 0.82), (0.34, 0.10, 0.40), mats["green"], col)
    # Bully group: short boss, lanky tall, fat guy, errand runner.
    cube("CHAR_bully_short_boss", (0.65, -1.35, 0.8), (0.46, 0.34, 1.25), mats["dark"], col)
    cube("CHAR_bully_lanky_tall", (1.55, -1.0, 1.05), (0.38, 0.30, 1.75), mats["dark"], col)
    cube("CHAR_bully_fat_guy", (1.55, -2.0, 0.95), (0.68, 0.42, 1.45), mats["dark"], col)
    cube("CHAR_bully_errand_runner", (0.25, -2.35, 0.82), (0.36, 0.25, 1.25), mats["dark"], col)
    cube("PATH_arcade_entry_to_duel", (-0.1, -2.8, 0.03), (0.18, 1.9, 0.06), mats["path"], col)
    text_label("LABEL_ARCADE", "ARCADE HALL / low ceiling / entrance axis", (0, 0, 0.06), 0.35, mats["label"], col)


def build_exterior(cols, mats):
    col = cols["EXTERIOR"]
    ox = 15
    cube("EXT_sidewalk", (ox, 0, -0.05), (12, 7, 0.1), mats["floor"], col)
    cube("EXT_arcade_facade", (ox, 2.7, 1.8), (7.0, 0.2, 3.6), mats["wall"], col)
    cube("EXT_rolling_shutter_left", (ox - 2.2, 2.55, 1.4), (1.9, 0.08, 2.4), mats["metal"], col)
    cube("EXT_rolling_shutter_right", (ox + 2.2, 2.55, 1.4), (1.9, 0.08, 2.4), mats["metal"], col)
    cube("EXT_arcade_door_glow", (ox, 2.45, 1.2), (1.8, 0.06, 2.2), mats["screen"], col)
    cube("EXT_old_signboard", (ox, 2.38, 3.15), (5.5, 0.08, 0.55), mats["red"], col)
    cube("EXT_dirty_steps", (ox, 1.6, 0.15), (2.4, 1.0, 0.3), mats["concrete"], col)
    cube("EXT_streetlight_pole", (ox - 4.8, -1.8, 1.5), (0.12, 0.12, 3.0), mats["metal"], col)
    cube("EXT_streetlight_head", (ox - 4.2, -1.8, 3.1), (1.0, 0.25, 0.18), mats["yellow"], col)
    cube("CHAR_older_brother_exit", (ox - 0.45, 0.65, 0.9), (0.42, 0.28, 1.35), mats["boy"], col)
    cube("CHAR_protagonist_exit", (ox - 1.05, 0.15, 0.72), (0.32, 0.22, 1.05), mats["boy"], col)
    cube("CHAR_younger_brother_exit", (ox - 1.45, -0.25, 0.64), (0.28, 0.20, 0.95), mats["boy"], col)
    cube("CHAR_green_schoolbag_exit", (ox - 1.05, -0.05, 0.82), (0.34, 0.10, 0.40), mats["green"], col)
    cube("PATH_exit_to_alley", (ox - 1.0, -0.25, 0.03), (0.18, 3.8, 0.06), mats["path"], col, rot=(0, 0, math.radians(-55)))
    text_label("LABEL_EXTERIOR", "ARCADE EXIT / three brothers leave toward alley / no fight here", (ox, -1.2, 0.06), 0.35, mats["label"], col)


def build_alley(cols, mats):
    col = cols["ALLEY"]
    ox = 32
    oy = 0
    # Secluded alley behind the old compound: the real ambush location.
    cube("ALLEY_ground_damp_path", (ox, oy, -0.05), (5.0, 18.0, 0.1), mats["floor"], col)
    cube("ALLEY_left_wall_yellowed", (ox - 2.55, oy, 1.8), (0.16, 18.0, 3.6), mats["wall"], col)
    cube("ALLEY_right_wall_yellowed", (ox + 2.55, oy, 1.8), (0.16, 18.0, 3.6), mats["wall"], col)
    cube("ALLEY_back_apartment_hint", (ox, oy + 8.9, 2.0), (5.2, 0.16, 4.0), mats["wall"], col)
    cube("ALLEY_old_streetlight_pole", (ox - 2.05, oy - 2.5, 1.8), (0.10, 0.10, 3.6), mats["metal"], col)
    cube("ALLEY_old_streetlight_head", (ox - 1.55, oy - 2.5, 3.25), (0.9, 0.25, 0.18), mats["yellow"], col)
    cube("ALLEY_weeds_left_1", (ox - 2.2, oy + 1.8, 0.18), (0.55, 1.5, 0.35), mats["green"], col)
    cube("ALLEY_weeds_right_1", (ox + 2.1, oy - 3.0, 0.18), (0.65, 1.3, 0.35), mats["green"], col)
    for idx, y in enumerate([-3.6, -2.8, -1.9]):
        cube(f"ALLEY_broken_stone_{idx+1}", (ox - 1.35 + idx * 0.35, oy + y, 0.08), (0.28, 0.20, 0.16), mats["concrete"], col)
    cube("PROP_key_stone_near_protagonist", (ox - 1.15, oy - 2.6, 0.11), (0.34, 0.25, 0.18), mats["red"], col)
    # Three brothers walking home, then stopped.
    cube("CHAR_older_brother_alley", (ox - 0.25, oy - 4.2, 0.9), (0.42, 0.28, 1.35), mats["boy"], col)
    cube("CHAR_protagonist_alley", (ox - 0.95, oy - 4.85, 0.72), (0.32, 0.22, 1.05), mats["boy"], col)
    cube("CHAR_green_schoolbag_alley", (ox - 1.15, oy - 5.05, 0.82), (0.34, 0.10, 0.40), mats["green"], col)
    cube("CHAR_younger_brother_alley", (ox + 0.55, oy - 5.05, 0.64), (0.28, 0.20, 0.95), mats["boy"], col)
    # Bully blockade ahead.
    cube("CHAR_bully_short_boss_alley", (ox - 0.15, oy + 0.5, 0.8), (0.46, 0.34, 1.25), mats["dark"], col)
    cube("CHAR_bully_lanky_tall_alley", (ox - 1.05, oy + 0.9, 1.05), (0.38, 0.30, 1.75), mats["dark"], col)
    cube("CHAR_bully_fat_guy_alley", (ox + 1.05, oy + 0.85, 0.95), (0.68, 0.42, 1.45), mats["dark"], col)
    cube("CHAR_bully_runner_alley", (ox + 1.55, oy - 0.05, 0.82), (0.36, 0.25, 1.25), mats["dark"], col)
    cube("PATH_alley_home_to_ambush", (ox, oy - 2.4, 0.03), (0.12, 6.2, 0.06), mats["path"], col)
    cube("PATH_alley_escape_vector", (ox - 0.8, oy - 5.4, 0.03), (0.12, 4.8, 0.06), mats["path"], col, rot=(0, 0, math.radians(-35)))
    text_label("LABEL_ALLEY", "SECLUDED ALLEY / ambush after Street Fighter victory / stone on ground", (ox, oy - 1.0, 0.06), 0.25, mats["label"], col)


def build_corridor(cols, mats):
    col = cols["CORRIDOR_PHONE"]
    cy = 18
    length = 34
    cube("COR_floor_long_narrow", (0, cy, -0.05), (3.2, length, 0.1), mats["floor"], col)
    cube("COR_left_wall", (-1.65, cy, 1.55), (0.12, length, 3.1), mats["wall"], col)
    cube("COR_right_wall", (1.65, cy, 1.55), (0.12, length, 3.1), mats["wall"], col)
    cube("COR_ceiling_low", (0, cy, 3.1), (3.2, length, 0.08), mats["ceiling"], col)
    for i, y in enumerate(range(3, 32, 4)):
        yy = cy - 17 + y
        cube(f"COR_repeated_door_left_{i+1}", (-1.58, yy, 1.35), (0.08, 1.15, 2.15), mats["door"], col)
        cube(f"COR_repeated_door_right_{i+1}", (1.58, yy + 1.5, 1.35), (0.08, 1.15, 2.15), mats["door"], col)
        cube(f"COR_flicker_tube_{i+1}", (0, yy + 0.5, 2.95), (1.0, 0.08, 0.08), mats["green_light"], col)
    cube("COR_old_fire_box", (1.54, cy + 8.5, 1.15), (0.08, 0.8, 0.7), mats["red"], col)
    cube("PHONE_booth_body", (0.45, cy + 14.0, 1.1), (1.0, 0.95, 2.2), mats["phone"], col)
    cube("PHONE_glowing_panel", (0.45, cy + 13.48, 1.25), (0.75, 0.05, 1.65), mats["warm_light"], col)
    cube("PHONE_receiver", (0.15, cy + 13.38, 1.35), (0.18, 0.08, 0.55), mats["dark"], col)
    cube("CHAR_boy_corridor_anchor", (0, cy - 13.0, 0.75), (0.35, 0.25, 1.1), mats["boy"], col)
    cube("PATH_corridor_to_phone", (0, cy + 0.5, 0.03), (0.12, 28, 0.06), mats["path"], col)
    text_label("LABEL_CORRIDOR", "ABANDONED BUILDING / endless corridor / phone booth at far end", (0, cy - 7, 0.06), 0.28, mats["label"], col)


def build_eight_bit(cols, mats):
    col = cols["EIGHT_BIT_STAGE"]
    ox = 15
    oy = 36
    cube("PIXEL_stage_floor", (ox, oy, 0.05), (13.5, 0.35, 0.1), mats["pixel_floor"], col)
    for i in range(12):
        cube(f"PIXEL_wall_tile_{i+1}", (ox - 6.0 + i * 1.1, oy + 0.45, 1.2), (0.8, 0.18, 0.8), mats["pixel_wall"], col)
    cube("PIXEL_phone_booth", (ox + 4.6, oy + 0.25, 1.0), (0.8, 0.25, 2.0), mats["warm_light"], col)
    cube("PIXEL_fire_box", (ox + 2.0, oy + 0.18, 1.0), (0.55, 0.18, 0.55), mats["red"], col)
    cube("PIXEL_boy_player", (ox - 4.5, oy - 0.1, 0.75), (0.5, 0.22, 1.05), mats["boy"], col)
    cube("PIXEL_green_bag", (ox - 4.82, oy - 0.12, 0.72), (0.18, 0.15, 0.45), mats["green"], col)
    for i, x in enumerate([ox - 1.2, ox + 0.1, ox + 1.4]):
        cube(f"PIXEL_enemy_{i+1}_black_jacket", (x, oy - 0.08, 0.78), (0.55, 0.22, 1.15), mats["dark"], col)
        cube(f"PIXEL_enemy_{i+1}_healthbar", (x, oy - 0.1, 1.55), (0.7, 0.06, 0.08), mats["red"], col)
    cube("PIXEL_UI_WIN_placeholder", (ox, oy - 0.18, 2.7), (3.8, 0.08, 0.55), mats["yellow"], col)
    cube("PATH_side_scroll_left_to_right", (ox, oy - 0.25, 0.16), (10.5, 0.08, 0.08), mats["path"], col)
    text_label("LABEL_8BIT", "SIDE-SCROLLING 8-BIT STAGE / player moves left to right", (ox, oy - 0.55, 0.06), 0.26, mats["label"], col)


def add_cameras():
    camera_specs = [
        ("CAM_ARCADE_01_ENTRANCE_WIDE", (0, -5.4, 1.2), (0, 0.7, 1.25), 22, False, 0, "Arcade entrance axis: children enter toward machine rows."),
        ("CAM_ARCADE_02_CHILD_POV", (0, -2.45, 0.95), (0, 1.8, 1.05), 24, False, 0, "Child-height center-axis view inside arcade, CRT glow and machine density."),
        ("CAM_ARCADE_02_STREET_FIGHTER_CABINET", (-1.9, -3.0, 1.1), (0, -0.65, 1.05), 28, False, 0, "Three brothers find the Street Fighter cabinet."),
        ("CAM_ARCADE_03_DUEL_OVER_SHOULDER", (-1.25, -2.2, 1.25), (0.45, -1.12, 1.05), 35, False, 0, "Older brother versus short boss at Street Fighter cabinet."),
        ("CAM_ARCADE_04_BOSS_LOSES_REACTION", (1.95, -2.25, 1.15), (0.55, -1.32, 0.98), 40, False, 0, "Short boss loses and bully group gathers."),
        ("CAM_ARCADE_EXIT_01_LEAVING", (15, -5.5, 1.3), (15, 1.2, 1.2), 28, False, 0, "Three brothers leave the hidden arcade door after the Street Fighter victory; no fight here."),
        ("CAM_ARCADE_EXIT_02_TO_ALLEY", (11.4, -2.8, 1.25), (17.0, 0.4, 1.15), 30, False, 0, "Transition direction from arcade exit toward the secluded alley."),
        ("CAM_ALLEY_01_WALK_HOME", (32.0, -9.8, 1.55), (32.0, -1.0, 1.15), 24, False, 0, "Three brothers walk home through secluded alley after arcade victory."),
        ("CAM_ALLEY_02_BLOCKED", (32.0, -8.6, 1.65), (32.0, 0.35, 1.0), 24, False, 0, "Bully group blocks the alley ahead."),
        ("CAM_ALLEY_03_BROTHER_BEATEN", (34.0, -5.0, 1.4), (32.0, -0.7, 1.0), 28, False, 0, "Four bullies surround and beat the older brother."),
        ("CAM_ALLEY_04_STONE_HIT", (30.0, -5.8, 1.15), (31.8, -0.6, 0.85), 28, False, 0, "Protagonist sees roadside stone before short boss's heavy blow."),
        ("CAM_ALLEY_05_ESCAPE_VECTOR", (30.2, -8.6, 1.25), (32.0, -2.0, 1.05), 26, False, 0, "Protagonist runs from the alley toward the abandoned building."),
        ("CAM_CORRIDOR_01_ENTRY_LONG", (0, 3.5, 1.25), (0, 21, 1.35), 24, False, 0, "Entry view into abandoned endless corridor."),
        ("CAM_CORRIDOR_02_LOW_TRACK", (-1.0, 9.0, 0.95), (0.15, 24.5, 1.2), 28, False, 0, "Low tracking direction for boy running down corridor."),
        ("CAM_PHONE_01_DISTANT_GLOW", (0, 15.0, 1.35), (0.45, 31.2, 1.35), 35, False, 0, "Distant glowing phone booth at the far end."),
        ("CAM_PHONE_02_APPROACH_CLOSE", (-1.15, 29.0, 1.35), (0.45, 31.7, 1.3), 35, False, 0, "Boy approaches phone booth, booth dominates frame."),
        ("CAM_PHONE_03_RECEIVER_INSERT", (-0.65, 30.85, 1.45), (0.13, 31.38, 1.35), 55, False, 0, "Insert angle for receiver and hand before electronic transition."),
        ("CAM_8BIT_01_STAGE_WIDE", (15, 26.5, 2.0), (15, 36.0, 1.15), 35, True, 8.0, "Orthographic side-scrolling stage wide view."),
        ("CAM_8BIT_02_WIN_SCREEN", (15, 29.0, 2.45), (15, 36.0, 2.35), 35, True, 5.8, "Final WIN / INSERT COIN framing."),
    ]
    camera_specs = [
        ("CAM_COMPOUND_01_ESTABLISH", (-17, -8.2, 1.55), (-15.4, 3.2, 1.5), 24, False, 0, "Old residential compound establishing view: remote ground-floor arcade corner."),
        ("CAM_COMPOUND_02_BROTHERS_APPROACH", (-20.8, -4.2, 1.15), (-14.3, 2.9, 1.2), 28, False, 0, "Older brother-like boy leads two younger brothers toward hidden arcade door."),
    ] + camera_specs
    cameras = []
    for name, loc, target, lens, ortho, scale, note in camera_specs:
        cameras.append((add_camera(name, loc, target, lens, ortho, scale), note))
    return cameras


def setup_scene():
    bpy.context.scene.render.engine = "BLENDER_WORKBENCH"
    bpy.context.scene.display.shading.light = "STUDIO"
    bpy.context.scene.display.shading.color_type = "MATERIAL"
    bpy.context.scene.render.resolution_x = 1280
    bpy.context.scene.render.resolution_y = 720
    bpy.context.scene.render.film_transparent = False
    bpy.context.scene.view_settings.view_transform = "Standard"
    bpy.context.scene.view_settings.look = "Medium High Contrast"
    add_area_light("KEY_soft_global", (0, -6, 6), (0, 0, 1), 450, 5, (1.0, 0.92, 0.82))
    add_area_light("CORRIDOR_green_overhead", (0, 18, 3.8), (0, 23, 1), 250, 8, (0.55, 0.9, 0.65))
    add_area_light("PHONE_warm_pool", (0.45, 31.5, 2.4), (0.45, 31.5, 1), 650, 2, (1.0, 0.82, 0.55))


def render_cameras(cameras):
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for cam, note in cameras:
        bpy.context.scene.camera = cam
        out = RENDER_DIR / f"{cam.name}.png"
        bpy.context.scene.render.filepath = str(out)
        bpy.ops.render.render(write_still=True)
        rows.append({
            "camera_id": cam.name,
            "image": str(out),
            "location": tuple(round(v, 3) for v in cam.location),
            "lens_or_ortho": f"ortho {cam.data.ortho_scale}" if cam.data.type == "ORTHO" else f"{cam.data.lens}mm",
            "note": note,
        })
    return rows


def write_manifest(rows):
    with MANIFEST_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["camera_id", "image", "location", "lens_or_ortho", "note"])
        writer.writeheader()
        writer.writerows(rows)


def main():
    BLENDER_DIR.mkdir(parents=True, exist_ok=True)
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    clear_scene()
    mats = {
        "floor": make_mat("mat_floor_concrete", (0.45, 0.43, 0.38, 1)),
        "wall": make_mat("mat_moldy_wall", (0.58, 0.60, 0.52, 1)),
        "ceiling": make_mat("mat_low_ceiling", (0.50, 0.52, 0.47, 1)),
        "door": make_mat("mat_old_door", (0.32, 0.36, 0.30, 1)),
        "concrete": make_mat("mat_dirty_concrete", (0.42, 0.40, 0.36, 1)),
        "metal": make_mat("mat_dull_metal", (0.32, 0.33, 0.34, 1)),
        "wood": make_mat("mat_old_counter", (0.44, 0.27, 0.16, 1)),
        "dark": make_mat("mat_black_jacket_dark", (0.035, 0.035, 0.04, 1)),
        "screen": make_mat("mat_crt_screen_bluegreen", (0.02, 0.55, 0.65, 1), emission=(0.02, 0.75, 0.85, 1), strength=1.2),
        "red": make_mat("mat_arcade_red_blood_ui", (0.85, 0.08, 0.04, 1), emission=(0.8, 0.05, 0.03, 1), strength=0.5),
        "yellow": make_mat("mat_dirty_yellow_sign", (0.9, 0.68, 0.18, 1), emission=(0.7, 0.45, 0.08, 1), strength=0.25),
        "green": make_mat("mat_schoolbag_green", (0.20, 0.55, 0.30, 1)),
        "boy": make_mat("mat_boy_blue_white_anchor", (0.18, 0.34, 0.82, 1)),
        "path": make_mat("mat_camera_path_orange", (1.0, 0.28, 0.05, 1), emission=(1.0, 0.2, 0.04, 1), strength=0.4),
        "label": make_mat("mat_label_black", (0.01, 0.01, 0.01, 1)),
        "translucent": make_mat("mat_dirty_plastic_curtain", (0.7, 0.75, 0.62, 0.45)),
        "green_light": make_mat("mat_fluorescent_green", (0.45, 1.0, 0.55, 1), emission=(0.45, 1.0, 0.55, 1), strength=1.5),
        "warm_light": make_mat("mat_phone_warm_light", (1.0, 0.78, 0.42, 1), emission=(1.0, 0.75, 0.38, 1), strength=2.0),
        "phone": make_mat("mat_old_phone_booth", (0.25, 0.38, 0.42, 1)),
        "pixel_floor": make_mat("mat_pixel_floor", (0.16, 0.18, 0.25, 1)),
        "pixel_wall": make_mat("mat_pixel_wall_tile", (0.38, 0.42, 0.52, 1)),
    }
    cols = make_collections()
    build_compound(cols, mats)
    build_arcade(cols, mats)
    build_exterior(cols, mats)
    build_alley(cols, mats)
    build_corridor(cols, mats)
    build_eight_bit(cols, mats)
    setup_scene()
    cameras = add_cameras()
    rows = render_cameras(cameras)
    write_manifest(rows)
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    print(f"SAVED_BLEND={BLEND_PATH}")
    print(f"SAVED_MANIFEST={MANIFEST_PATH}")
    print(f"SAVED_RENDERS={RENDER_DIR}")


if __name__ == "__main__":
    main()
