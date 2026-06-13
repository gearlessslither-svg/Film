import csv
import math
import re
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[1]
BLEND_PATH = ROOT / "blender" / "coin_slot_whitebox.blend"
PLAN_PATH = ROOT / "exports" / "whitebox_expansion_plan.csv"
OUT_ROOT = ROOT / "whitebox_renders_v2"
MANIFEST_PATH = ROOT / "blender" / "whitebox_v2_manifest.csv"


SHOT_LENS = {
    "远景": 24,
    "全景": 26,
    "广角": 24,
    "中远景": 30,
    "中景": 35,
    "反打中景": 35,
    "低机位中景": 32,
    "中近景": 42,
    "近景": 50,
    "特写": 65,
    "极近景": 75,
    "横版远景": 35,
    "横版全景": 35,
    "横版中景": 45,
}


SCENE_TARGETS = {
    "SCN_COMPOUND": (-15.4, 2.5, 1.25),
    "SCN_ARCADE": (0.0, -0.8, 1.1),
    "SCN_EXIT": (15.0, 0.8, 1.1),
    "SCN_ALLEY": (32.0, -1.5, 1.0),
    "SCN_CORRIDOR": (0.0, 22.0, 1.25),
    "SCN_PHONE": (0.45, 31.2, 1.25),
    "SCN_8BIT": (15.0, 36.0, 1.25),
}


SOURCE_CAMERA_TARGETS = {
    "CAM_COMPOUND_01_ESTABLISH": (-15.4, 3.2, 1.5),
    "CAM_COMPOUND_02_BROTHERS_APPROACH": (-14.3, 2.9, 1.2),
    "CAM_ARCADE_01_ENTRANCE_WIDE": (0, 0.7, 1.25),
    "CAM_ARCADE_02_CHILD_POV": (0, 1.8, 1.05),
    "CAM_ARCADE_02_STREET_FIGHTER_CABINET": (0, -0.65, 1.05),
    "CAM_ARCADE_03_DUEL_OVER_SHOULDER": (0.45, -1.12, 1.05),
    "CAM_ARCADE_04_BOSS_LOSES_REACTION": (0.55, -1.32, 0.98),
    "CAM_ARCADE_EXIT_01_LEAVING": (15, 1.2, 1.2),
    "CAM_ARCADE_EXIT_02_TO_ALLEY": (17.0, 0.4, 1.15),
    "CAM_ALLEY_01_WALK_HOME": (32.0, -1.0, 1.15),
    "CAM_ALLEY_02_BLOCKED": (32.0, 0.35, 1.0),
    "CAM_ALLEY_03_BROTHER_BEATEN": (32.0, -0.7, 1.0),
    "CAM_ALLEY_04_STONE_HIT": (31.8, -0.6, 0.85),
    "CAM_ALLEY_05_ESCAPE_VECTOR": (32.0, -2.0, 1.05),
    "CAM_CORRIDOR_01_ENTRY_LONG": (0, 21, 1.35),
    "CAM_CORRIDOR_02_LOW_TRACK": (0.15, 24.5, 1.2),
    "CAM_PHONE_01_DISTANT_GLOW": (0.45, 31.2, 1.35),
    "CAM_PHONE_02_APPROACH_CLOSE": (0.45, 31.7, 1.3),
    "CAM_PHONE_03_RECEIVER_INSERT": (0.13, 31.38, 1.35),
    "CAM_8BIT_01_STAGE_WIDE": (15, 36.0, 1.15),
    "CAM_8BIT_02_WIN_SCREEN": (15, 36.0, 2.35),
}


def look_at(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def panel_material(name, color):
    mat = bpy.data.materials.get(name)
    if mat:
        return mat
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = color
    return mat


CHARACTER_SPECS = {
    "alei": {
        "height": 1.35,
        "width": 0.42,
        "depth": 0.28,
        "body": (0.18, 0.34, 0.82, 1.0),
        "accent": (0.85, 0.08, 0.04, 1.0),
    },
    "xiaochuan": {
        "height": 1.08,
        "width": 0.32,
        "depth": 0.22,
        "body": (0.20, 0.46, 0.86, 1.0),
        "accent": (0.85, 0.08, 0.04, 1.0),
        "bag": (0.20, 0.55, 0.30, 1.0),
    },
    "xiaoman": {
        "height": 0.95,
        "width": 0.28,
        "depth": 0.20,
        "body": (0.62, 0.72, 0.88, 1.0),
        "accent": (0.85, 0.08, 0.04, 1.0),
    },
    "binzi": {
        "height": 1.25,
        "width": 0.46,
        "depth": 0.34,
        "body": (0.035, 0.035, 0.04, 1.0),
        "accent": (0.92, 0.68, 0.18, 1.0),
    },
    "gaogan": {
        "height": 1.75,
        "width": 0.38,
        "depth": 0.30,
        "body": (0.10, 0.10, 0.12, 1.0),
        "accent": (0.55, 0.58, 0.62, 1.0),
    },
    "dahai": {
        "height": 1.45,
        "width": 0.68,
        "depth": 0.42,
        "body": (0.09, 0.09, 0.10, 1.0),
        "accent": (0.42, 0.42, 0.36, 1.0),
    },
    "xiaoqi": {
        "height": 1.25,
        "width": 0.36,
        "depth": 0.25,
        "body": (0.06, 0.06, 0.07, 1.0),
        "accent": (0.45, 0.45, 0.50, 1.0),
    },
}


def proxy_cube(name, loc, scale, color, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(panel_material(f"MAT_{name}", color))
    return obj


def delete_objects(objects):
    for obj in objects:
        if obj and obj.name in bpy.data.objects:
            bpy.data.objects.remove(obj, do_unlink=True)


def text_has(text, *needles):
    return any(needle in text for needle in needles)


def hide_base_character_anchors():
    """Use the base blend as environment only; panel characters are rebuilt per render."""
    for obj in bpy.data.objects:
        if obj.name.startswith("CHAR_") or obj.name.startswith("PIXEL_enemy_") or obj.name.startswith("PIXEL_boy_"):
            obj.hide_render = True
            obj.hide_viewport = True


def clamp(value, low, high):
    return max(low, min(high, value))


def progress(n, start, end):
    if end <= start:
        return 0.0
    return clamp((n - start) / (end - start), 0.0, 1.0)


def add_character_proxy(prefix, spec_key, foot_loc, yaw=0.0, lean=0.0):
    spec = CHARACTER_SPECS[spec_key]
    x, y, z = foot_loc
    height = spec["height"]
    width = spec["width"]
    depth = spec["depth"]
    body_h = height * 0.58
    leg_h = height * 0.28
    head_h = height * 0.16
    rot = (0, lean, yaw)
    objs = []

    objs.append(proxy_cube(
        f"{prefix}_legs",
        (x, y, z + leg_h * 0.5),
        (width * 0.65, depth * 0.72, leg_h),
        spec["body"],
        rot,
    ))
    objs.append(proxy_cube(
        f"{prefix}_body",
        (x, y, z + leg_h + body_h * 0.5),
        (width, depth, body_h),
        spec["body"],
        rot,
    ))
    objs.append(proxy_cube(
        f"{prefix}_head",
        (x, y, z + height - head_h * 0.45),
        (width * 0.72, depth * 0.72, head_h),
        spec.get("accent", spec["body"]),
        rot,
    ))
    objs.append(proxy_cube(
        f"{prefix}_shoulder_line",
        (x, y, z + leg_h + body_h * 0.80),
        (width * 1.25, depth * 0.45, height * 0.055),
        spec["body"],
        rot,
    ))

    if spec_key == "xiaochuan":
        objs.append(proxy_cube(
            f"{prefix}_green_schoolbag",
            (x - 0.18, y - 0.12, z + height * 0.48),
            (0.26, 0.12, 0.38),
            spec["bag"],
            rot,
        ))
        objs.append(proxy_cube(
            f"{prefix}_red_scarf",
            (x, y - 0.08, z + height * 0.64),
            (width * 1.05, 0.055, 0.055),
            spec["accent"],
            rot,
        ))
    elif spec_key in {"alei", "xiaoman"}:
        objs.append(proxy_cube(
            f"{prefix}_red_scarf",
            (x, y - 0.08, z + height * 0.62),
            (width * 0.90, 0.05, 0.05),
            spec["accent"],
            rot,
        ))
    elif spec_key == "binzi":
        objs.append(proxy_cube(
            f"{prefix}_yellow_hair",
            (x, y - 0.02, z + height + 0.035),
            (width * 0.82, depth * 0.75, 0.07),
            spec["accent"],
            rot,
        ))
    elif spec_key in {"gaogan", "dahai", "xiaoqi"}:
        objs.append(proxy_cube(
            f"{prefix}_jacket_edge",
            (x, y - 0.09, z + height * 0.58),
            (width * 0.95, 0.045, 0.08),
            spec["accent"],
            rot,
        ))

    return objs


def add_group_three_brothers(prefix, base_x, base_y, z=0.0, spread=1.0, advance=0.0):
    objs = []
    objs.extend(add_character_proxy(f"{prefix}_alei", "alei", (base_x, base_y + 0.42 + advance, z), yaw=0.0))
    objs.extend(add_character_proxy(f"{prefix}_xiaochuan", "xiaochuan", (base_x - 0.62 * spread, base_y - 0.18 + advance, z), yaw=0.0))
    objs.extend(add_character_proxy(f"{prefix}_xiaoman", "xiaoman", (base_x + 0.56 * spread, base_y - 0.42 + advance, z), yaw=0.0))
    return objs


def add_bully_group(prefix, base_x, base_y, z=0.0, spread=1.0, advance=0.0):
    objs = []
    objs.extend(add_character_proxy(f"{prefix}_binzi", "binzi", (base_x, base_y - 0.18 + advance, z), yaw=math.radians(180)))
    objs.extend(add_character_proxy(f"{prefix}_gaogan", "gaogan", (base_x - 0.85 * spread, base_y + 0.36 + advance, z), yaw=math.radians(180)))
    objs.extend(add_character_proxy(f"{prefix}_dahai", "dahai", (base_x + 0.95 * spread, base_y + 0.30 + advance, z), yaw=math.radians(180)))
    objs.extend(add_character_proxy(f"{prefix}_xiaoqi", "xiaoqi", (base_x + 1.45 * spread, base_y - 0.45 + advance, z), yaw=math.radians(180)))
    return objs


def add_panel_character_blocking(row):
    n = panel_number(row["panel_id"])
    scene = row["scene_id"]
    subject = row.get("character_blocking", "")
    focus = row.get("layout_focus", "")
    pose = row.get("pose_or_path", "")
    text = f"{subject} {focus} {pose}"
    prefix = f"WB_CHAR_{n}"
    objs = []

    if scene == "SCN_COMPOUND":
        if text_has(text, "三兄弟", "阿磊", "小川", "小满", "弟弟"):
            p = progress(n, 7, 18)
            objs.extend(add_group_three_brothers(prefix, -18.4 + p * 3.2, -3.25 + p * 1.1, spread=0.82, advance=p * 0.45))
            if text_has(text, "半回头", "回头"):
                objs.append(proxy_cube(f"{prefix}_turn_bead", (-16.0, -2.55, 1.35), (0.16, 0.08, 0.08), (1.0, 0.82, 0.05, 1.0)))
        return objs

    if scene == "SCN_ARCADE":
        if n <= 28:
            p = progress(n, 19, 28)
            if text_has(text, "三兄弟", "阿磊", "小川", "小满", "弟弟"):
                objs.extend(add_group_three_brothers(prefix, -0.35, -3.0 + p * 1.35, spread=0.76, advance=p * 0.15))
            return objs

        if text_has(text, "阿磊", "小川", "小满", "三兄弟", "弟弟"):
            if text_has(text, "小川") and not text_has(text, "阿磊"):
                objs.extend(add_character_proxy(f"{prefix}_xiaochuan", "xiaochuan", (-1.18, -1.88, 0.0)))
            elif text_has(text, "小满") and not text_has(text, "阿磊"):
                objs.extend(add_character_proxy(f"{prefix}_xiaoman", "xiaoman", (-1.66, -2.25, 0.0)))
            else:
                lean = math.radians(5) if text_has(text, "前倾", "操作", "按钮") else 0.0
                objs.extend(add_character_proxy(f"{prefix}_alei", "alei", (-0.48, -1.35, 0.0), lean=lean))
                if text_has(text, "三兄弟", "弟弟"):
                    objs.extend(add_character_proxy(f"{prefix}_xiaochuan", "xiaochuan", (-1.15, -1.88, 0.0)))
                    objs.extend(add_character_proxy(f"{prefix}_xiaoman", "xiaoman", (-1.66, -2.25, 0.0)))

        if text_has(text, "彬子", "高杆", "大海", "小齐", "混混", "四人"):
            if text_has(text, "高杆") and not text_has(text, "四人", "混混"):
                objs.extend(add_character_proxy(f"{prefix}_gaogan", "gaogan", (1.28, -1.12, 0.0), yaw=math.radians(180)))
            elif text_has(text, "大海") and not text_has(text, "四人", "混混"):
                objs.extend(add_character_proxy(f"{prefix}_dahai", "dahai", (1.48, -1.95, 0.0), yaw=math.radians(180)))
            elif text_has(text, "小齐") and not text_has(text, "四人", "混混"):
                objs.extend(add_character_proxy(f"{prefix}_xiaoqi", "xiaoqi", (0.22, -2.30, 0.0), yaw=math.radians(180)))
            elif text_has(text, "四人", "混混"):
                objs.extend(add_bully_group(prefix, 0.72, -1.28, spread=0.78))
            else:
                objs.extend(add_character_proxy(f"{prefix}_binzi", "binzi", (0.66, -1.35, 0.0), yaw=math.radians(180)))
        return objs

    if scene == "SCN_EXIT":
        if text_has(text, "三兄弟", "阿磊", "小川", "小满", "队形", "门口"):
            p = progress(n, 58, 65)
            objs.extend(add_group_three_brothers(prefix, 14.45 - p * 0.9, 0.48 - p * 1.55, spread=0.78, advance=-p * 0.25))
        return objs

    if scene == "SCN_ALLEY":
        if n <= 75:
            p = progress(n, 66, 75)
            if text_has(text, "三兄弟", "阿磊", "小川", "小满"):
                objs.extend(add_group_three_brothers(prefix, 31.8, -6.15 + p * 1.75, spread=0.85, advance=p * 0.22))
            if n >= 72 or text_has(text, "混混远影", "人影"):
                objs.extend(add_bully_group(prefix, 32.2, 1.35, spread=0.62))
            return objs

        if 76 <= n <= 85:
            if text_has(text, "高杆") and not text_has(text, "四人", "混混", "全体"):
                objs.extend(add_character_proxy(f"{prefix}_gaogan", "gaogan", (30.95, 0.82, 0.0), yaw=math.radians(180)))
                objs.append(proxy_cube(f"{prefix}_gaogan_blocking_arm", (30.95, 0.46, 1.28), (1.30, 0.08, 0.10), (0.55, 0.58, 0.62, 1.0)))
            elif text_has(text, "大海") and not text_has(text, "四人", "混混", "全体"):
                objs.extend(add_character_proxy(f"{prefix}_dahai", "dahai", (32.95, 0.55, 0.0), yaw=math.radians(180)))
                objs.append(proxy_cube(f"{prefix}_dahai_width_wall", (32.95, 0.22, 0.85), (0.95, 0.12, 1.15), (0.42, 0.42, 0.36, 1.0)))
            elif text_has(text, "小齐") and not text_has(text, "四人", "混混", "全体"):
                objs.extend(add_character_proxy(f"{prefix}_xiaoqi", "xiaoqi", (33.25, -0.25, 0.0), yaw=math.radians(180), lean=math.radians(-6)))
            elif text_has(text, "彬子") and not text_has(text, "阿磊", "四人", "混混", "全体"):
                adv = 0.22 if text_has(text, "向前", "半步") else 0.0
                objs.extend(add_character_proxy(f"{prefix}_binzi", "binzi", (31.92, 0.32 - adv, 0.0), yaw=math.radians(180), lean=math.radians(5)))
            elif text_has(text, "彬子", "高杆", "大海", "小齐", "混混", "四人", "全体"):
                adv = 0.22 if text_has(text, "向前", "半步") else 0.0
                objs.extend(add_bully_group(prefix, 32.05, 0.45, spread=0.88, advance=-adv))
            if text_has(text, "阿磊", "小川", "小满", "三兄弟", "全体"):
                front = 0.35 if text_has(text, "挡前", "前面") else 0.0
                objs.extend(add_group_three_brothers(prefix, 31.75, -4.75 + front, spread=0.82))
            return objs

        if 86 <= n <= 97:
            if text_has(text, "阿磊", "混混", "彬子", "高杆", "大海", "小齐", "全体"):
                objs.extend(add_character_proxy(f"{prefix}_alei", "alei", (31.85, -0.65, 0.0), yaw=math.radians(180), lean=math.radians(8 if text_has(text, "失衡", "歪") else 0)))
                objs.extend(add_bully_group(prefix, 32.0, 0.05, spread=0.70, advance=-0.25))
            if text_has(text, "小川"):
                objs.extend(add_character_proxy(f"{prefix}_xiaochuan", "xiaochuan", (31.05, -2.25, 0.0), yaw=math.radians(180)))
            if text_has(text, "小满"):
                objs.extend(add_character_proxy(f"{prefix}_xiaoman", "xiaoman", (33.15, -2.45, 0.0), yaw=math.radians(180)))
            return objs

        if 98 <= n <= 107:
            if text_has(text, "小川", "石块", "手"):
                crouch = 0.18 if text_has(text, "向下", "弯身", "抓住") else 0.0
                objs.extend(add_character_proxy(f"{prefix}_xiaochuan", "xiaochuan", (30.95, -2.85, 0.0), yaw=math.radians(30), lean=math.radians(12 + crouch * 40)))
            if text_has(text, "彬子", "阿磊", "全体", "混混"):
                objs.extend(add_character_proxy(f"{prefix}_alei", "alei", (31.78, -0.52, 0.0), yaw=math.radians(180), lean=math.radians(9)))
                objs.extend(add_bully_group(prefix, 32.0, 0.10, spread=0.70, advance=-0.20))
            return objs

        if 108 <= n <= 119:
            p = progress(n, 108, 119)
            if text_has(text, "小川", "环境", "入口"):
                objs.extend(add_character_proxy(f"{prefix}_xiaochuan", "xiaochuan", (31.15 - p * 0.45, -4.75 - p * 3.55, 0.0), yaw=math.radians(-25), lean=math.radians(-8)))
            if text_has(text, "阿磊", "小满", "混混", "追兵", "后方"):
                objs.extend(add_character_proxy(f"{prefix}_alei", "alei", (31.75, -1.15, 0.0), yaw=math.radians(180), lean=math.radians(8)))
                objs.extend(add_character_proxy(f"{prefix}_xiaoman", "xiaoman", (33.10, -2.05, 0.0), yaw=math.radians(180)))
                if text_has(text, "混混", "追兵"):
                    objs.extend(add_bully_group(prefix, 32.1, -0.05, spread=0.68, advance=-0.40))
            return objs

    if scene == "SCN_CORRIDOR":
        if text_has(text, "小川") or 120 <= n <= 138:
            p = progress(n, 120, 138)
            objs.extend(add_character_proxy(f"{prefix}_xiaochuan", "xiaochuan", (0.0 + ((n % 3) - 1) * 0.12, 5.0 + p * 23.5, 0.0), yaw=0.0, lean=math.radians(-6 if text_has(text, "跑") else 0)))
        return objs

    if scene == "SCN_PHONE":
        if text_has(text, "小川", "红领巾", "书包", "脸", "眼", "手") or 140 <= n <= 169:
            if n <= 146:
                p = progress(n, 140, 146)
                y = 20.8 + p * 8.5
                x = -0.20 + p * 0.08
            elif n <= 154:
                p = progress(n, 147, 154)
                y = 30.40 + p * 0.72
                x = -0.45 + p * 0.30
            else:
                y = 31.05
                x = -0.15
            lean = math.radians(5 if text_has(text, "靠近", "前进", "伸手") else 0)
            objs.extend(add_character_proxy(f"{prefix}_xiaochuan", "xiaochuan", (x, y, 0.0), yaw=0.0, lean=lean))
        return objs

    if scene == "SCN_8BIT":
        p = progress(n, 170, 188)
        objs.extend(add_character_proxy(f"{prefix}_player", "xiaochuan", (10.2 + p * 4.7, 35.72, 0.0), yaw=0.0))
        if text_has(text, "敌人", "高杆", "大海", "小齐", "彬子", "混混"):
            objs.extend(add_bully_group(prefix, 15.2 + ((n % 4) - 1.5) * 0.45, 35.72, spread=0.55))
        return objs

    return objs


def semantic_target(row):
    scene = row["scene_id"]
    subject = row.get("character_blocking", "")
    focus = row.get("layout_focus", "")
    pose = row.get("pose_or_path", "")
    text = f"{subject} {focus} {pose}"
    n = panel_number(row["panel_id"])
    phase = (n % 5) - 2
    fine = (n % 3) - 1

    if scene == "SCN_COMPOUND":
        if text_has(text, "阿磊"):
            return Vector((-16.1, -2.3, 0.9))
        if text_has(text, "小川"):
            return Vector((-16.8, -2.95, 0.75))
        if text_has(text, "小满"):
            return Vector((-15.45, -3.05, 0.7))
        if text_has(text, "门", "CRT", "入口", "游戏机房"):
            return Vector((-11.8, 2.86, 1.2))
        return Vector((-15.4 + phase * 0.8, 0.6 + fine * 0.8, 1.1))

    if scene == "SCN_ARCADE":
        if text_has(text, "按钮", "手指", "操作台"):
            return Vector((0.0, -0.86, 0.75))
        if text_has(text, "街机", "屏幕", "CRT", "胜利"):
            return Vector((0.0, -0.82, 1.25))
        if text_has(text, "阿磊"):
            return Vector((-0.45, -1.35, 1.0))
        if text_has(text, "小川"):
            return Vector((-1.15, -1.85, 0.85))
        if text_has(text, "小满"):
            return Vector((-1.65, -2.25, 0.75))
        if text_has(text, "彬子"):
            return Vector((0.65, -1.35, 0.9))
        if text_has(text, "高杆"):
            return Vector((1.55, -1.0, 1.2))
        if text_has(text, "大海"):
            return Vector((1.55, -2.0, 1.05))
        if text_has(text, "小齐"):
            return Vector((0.25, -2.35, 0.9))
        if text_has(text, "混混", "四人"):
            return Vector((1.05, -1.6, 1.05))
        return Vector((0.0 + phase * 0.45, -1.2 + fine * 0.35, 1.05))

    if scene == "SCN_EXIT":
        if text_has(text, "门", "游戏机房"):
            return Vector((15.0, 2.45, 1.2))
        if text_has(text, "三兄弟", "小川", "阿磊", "小满"):
            return Vector((14.25 + phase * 0.18, 0.2 + fine * 0.22, 0.9))
        return Vector((15.0 + phase * 0.35, 0.4 + fine * 0.3, 1.1))

    if scene == "SCN_ALLEY":
        if text_has(text, "石块", "碎砖"):
            return Vector((30.85, -2.6, 0.18))
        if text_has(text, "阿磊"):
            return Vector((31.75, -4.2, 1.0))
        if text_has(text, "小川"):
            if row["source_camera"] == "CAM_ALLEY_05_ESCAPE_VECTOR":
                return Vector((31.1 + phase * 0.10, -4.8 - max(0, n - 108) * 0.28, 0.85))
            return Vector((31.05, -4.85, 0.85))
        if text_has(text, "小满"):
            return Vector((32.55, -5.05, 0.75))
        if text_has(text, "彬子"):
            return Vector((31.85, 0.5, 0.9))
        if text_has(text, "高杆"):
            return Vector((30.95, 0.9, 1.2))
        if text_has(text, "大海"):
            return Vector((33.05, 0.85, 1.05))
        if text_has(text, "小齐"):
            return Vector((33.55, -0.05, 0.9))
        if text_has(text, "混混", "追兵", "四人"):
            return Vector((32.6 + phase * 0.25, 0.4 + fine * 0.25, 1.05))
        if text_has(text, "入口", "废楼"):
            return Vector((31.2, -8.5, 1.0))
        return Vector((32.0 + phase * 0.25, -2.2 + fine * 0.8, 1.0))

    if scene == "SCN_CORRIDOR":
        if text_has(text, "消防箱"):
            return Vector((1.54, 26.5, 1.15))
        if text_has(text, "电话亭", "铃声", "暖光"):
            return Vector((0.45, 31.8, 1.25))
        if text_has(text, "小川"):
            y = 5.0 + max(0, n - 120) * 1.25
            return Vector((0.0 + fine * 0.12, min(y, 29.8), 0.85))
        return Vector((0.0 + phase * 0.08, 12.0 + max(0, n - 120) * 0.95, 1.2))

    if scene == "SCN_PHONE":
        if text_has(text, "电话线", "扫描线"):
            return Vector((0.05, 31.35, 1.55))
        if text_has(text, "听筒", "电话"):
            return Vector((0.15, 31.38, 1.35))
        if text_has(text, "手", "指尖"):
            return Vector((-0.15, 31.15, 1.05))
        if text_has(text, "书包"):
            return Vector((-0.25, 30.95, 0.8))
        if text_has(text, "脸", "眼", "红领巾", "小川"):
            return Vector((-0.15 + phase * 0.04, 30.85 + fine * 0.08, 1.15))
        return Vector((0.45, 31.45, 1.25))

    if scene == "SCN_8BIT":
        if text_has(text, "WIN", "INSERT", "UI"):
            return Vector((15.0, 36.0, 2.45))
        if text_has(text, "敌人", "高杆", "大海", "小齐", "彬子", "混混"):
            return Vector((15.2 + phase * 0.55, 36.0, 0.95))
        if text_has(text, "小川", "玩家"):
            return Vector((10.5 + max(0, n - 170) * 0.25, 35.9, 0.9))
        return Vector((15.0 + phase * 0.35, 36.0, 1.15))

    return Vector(SCENE_TARGETS.get(scene, (0, 0, 1.2)))


def add_panel_proxies(row):
    n = panel_number(row["panel_id"])
    scene = row["scene_id"]
    target = semantic_target(row)
    subject = row.get("character_blocking", "")
    focus = row.get("layout_focus", "")
    pose = row.get("pose_or_path", "")
    text = f"{subject} {focus} {pose}"
    color_focus = (1.0, 0.85, 0.05, 1.0)
    color_action = (0.05, 0.6, 1.0, 1.0)
    color_danger = (1.0, 0.08, 0.05, 1.0)
    color_player = (0.15, 0.8, 0.35, 1.0)
    objs = add_panel_character_blocking(row)

    if scene == "SCN_8BIT":
        progress = max(0, n - 170)
        player_x = 10.2 + min(progress, 15) * 0.28
        enemy_x = 15.8 + ((n % 4) - 1.5) * 0.65
        objs.append(proxy_cube(f"WB_PANEL_PLAYER_{n}", (player_x, 35.72, 0.88), (0.42, 0.18, 1.05), color_player))
        if text_has(text, "敌人", "高杆", "大海", "小齐", "彬子", "混混"):
            objs.append(proxy_cube(f"WB_PANEL_ENEMY_{n}", (enemy_x, 35.72, 0.95), (0.55 + (n % 3) * 0.15, 0.18, 1.0 + (n % 2) * 0.35), color_danger))
        if text_has(text, "WIN", "INSERT", "UI"):
            objs.append(proxy_cube(f"WB_PANEL_UI_{n}", (15.0, 35.65, 2.55), (2.4 + (n % 4) * 0.45, 0.10, 0.42), color_focus))
            if n == 187:
                objs.append(proxy_cube(f"WB_PANEL_UI_HOLD_{n}", (12.1, 35.65, 1.85), (0.7, 0.10, 0.18), color_action))
            if n == 188:
                objs.append(proxy_cube(f"WB_PANEL_INSERT_{n}", (18.8, 35.65, 1.65), (1.45, 0.10, 0.28), color_action))
        return objs

    if scene == "SCN_PHONE":
        if text_has(text, "电话线", "扫描线"):
            objs.append(proxy_cube(f"WB_PANEL_PHONE_LINE_{n}", target, (0.08, 0.08, 1.25), color_action))
            objs.append(proxy_cube(f"WB_PANEL_PHONE_SCAN_{n}", (target.x + 0.28, target.y, target.z + 0.32), (0.62, 0.06, 0.08), color_focus))
        elif text_has(text, "听筒", "电话"):
            objs.append(proxy_cube(f"WB_PANEL_RECEIVER_{n}", target, (0.20, 0.10, 0.62), color_focus))
        elif text_has(text, "手", "指尖"):
            objs.append(proxy_cube(f"WB_PANEL_HAND_{n}", target, (0.34, 0.12, 0.20), color_focus))
        elif text_has(text, "书包"):
            objs.append(proxy_cube(f"WB_PANEL_BAG_{n}", target, (0.42, 0.16, 0.42), color_player))
        elif text_has(text, "脸", "眼", "红领巾", "小川"):
            objs.append(proxy_cube(f"WB_PANEL_BOY_{n}", target, (0.30, 0.20, 1.05), color_player))
            objs.append(proxy_cube(f"WB_PANEL_SCARF_{n}", (target.x, target.y - 0.03, target.z - 0.18), (0.38, 0.06, 0.08), color_danger))
        else:
            objs.append(proxy_cube(f"WB_PANEL_PHONE_BOOTH_{n}", target, (0.42, 0.20, 1.15), color_focus))
        return objs

    if text_has(text, "石块", "听筒", "电话线", "按钮", "手", "指尖", "屏幕", "CRT", "书包"):
        scale = (0.32, 0.18, 0.32)
    elif text_has(text, "环境", "入口", "门", "走廊", "小路"):
        scale = (0.42, 0.22, 0.65)
    else:
        scale = (0.34, 0.24, 1.05)

    proxy_color = color_danger if text_has(text, "混混", "彬子", "高杆", "大海", "小齐", "敌人") else color_focus
    if text_has(text, "石块", "听筒", "电话线", "按钮", "手", "指尖", "屏幕", "CRT", "书包", "入口", "门框", "墙面"):
        objs.append(proxy_cube(f"WB_PANEL_FOCUS_{n}", target, scale, proxy_color))

    if text_has(text, "跑", "奔", "靠近", "走", "进入", "追", "回头", "逃", "左到右", "右到左"):
        if scene == "SCN_ALLEY":
            path_loc = (target.x, target.y + 0.6, 0.08)
            path_scale = (0.12, 1.2, 0.08)
        elif scene in {"SCN_CORRIDOR", "SCN_PHONE"}:
            path_loc = (target.x, target.y - 0.75, 0.08)
            path_scale = (0.12, 1.5, 0.08)
        else:
            path_loc = (target.x, target.y - 0.35, 0.08)
            path_scale = (0.85, 0.12, 0.08)
        objs.append(proxy_cube(f"WB_PANEL_ACTION_{n}", path_loc, path_scale, color_action))

    if text_has(text, "遮挡", "擦镜", "门框", "墙面", "前景"):
        fg = target + Vector((-0.55, -0.35, 0.35))
        objs.append(proxy_cube(f"WB_PANEL_FOREGROUND_{n}", fg, (0.18, 0.18, 1.3), (0.08, 0.08, 0.08, 1.0)))

    return objs


def semantic_camera_override(row, base_cam):
    n = panel_number(row["panel_id"])
    scene = row["scene_id"]
    source = row["source_camera"]
    target = semantic_target(row)
    subject = row.get("character_blocking", "")
    focus = row.get("layout_focus", "")
    pose = row.get("pose_or_path", "")
    text = f"{subject} {focus} {pose}"
    phase = (n % 5) - 2
    fine = (n % 3) - 1
    close = text_has(text, "特写", "手", "按钮", "指尖", "听筒", "电话线", "石块", "嘴角", "眼", "屏幕", "CRT")

    if scene in {"SCN_ARCADE", "SCN_ALLEY", "SCN_PHONE"}:
        return None

    if scene == "SCN_COMPOUND":
        if source == "CAM_COMPOUND_01_ESTABLISH":
            return Vector((-18.0 + phase * 0.75, -8.5 + fine * 0.55, 1.35 + fine * 0.08)), target, 22 + (n % 3) * 3
        return Vector((-20.2 + phase * 0.65, -4.8 + fine * 0.55, 1.05 + (n % 2) * 0.15)), target, 28 + (n % 4) * 4

    if scene == "SCN_ARCADE":
        if source == "CAM_ARCADE_01_ENTRANCE_WIDE":
            return Vector((0.0 + phase * 0.35, -5.65, 1.22 + fine * 0.05)), target, 22 + (n % 3) * 3
        if source == "CAM_ARCADE_02_STREET_FIGHTER_CABINET":
            loc = Vector((-2.75 + phase * 0.18, -3.75 + fine * 0.18, 1.32 + (n % 2) * 0.08))
            return loc, target, 28 + (n % 4) * 4
        if source == "CAM_ARCADE_03_DUEL_OVER_SHOULDER":
            loc = Vector((-2.35 + phase * 0.18, -3.35 + fine * 0.20, 1.22 + (n % 2) * 0.08))
            return loc, target, 32 + (n % 4) * 4
        if close:
            loc = target + Vector((-1.8 + phase * 0.16, -2.05 + fine * 0.18, 0.70 + (n % 2) * 0.10))
            return loc, target, 38 + (n % 4) * 4
        if text_has(text, "彬子", "高杆", "大海", "小齐", "混混", "四人"):
            loc = Vector((3.05 + phase * 0.25, -3.45 + fine * 0.20, 1.25 + (n % 2) * 0.10))
            return loc, target, 30 + (n % 3) * 5
        if text_has(text, "小川"):
            loc = Vector((-2.35 + phase * 0.18, -3.25 + fine * 0.18, 0.98))
            return loc, target, 38
        return Vector((-2.2 + phase * 0.35, -3.2 + fine * 0.25, 1.16)), target, 26 + (n % 5) * 3

    if scene == "SCN_EXIT":
        return Vector((12.6 + phase * 0.55, -5.6 + fine * 0.20, 1.35)), target, 24 + (n % 4) * 4

    if scene == "SCN_ALLEY":
        if source == "CAM_ALLEY_05_ESCAPE_VECTOR":
            loc = target + Vector((-1.8 + phase * 0.16, -3.0 + fine * 0.18, 0.75 + (n % 2) * 0.10))
            return loc, target + Vector((0.25, 0.9, 0.1)), 26 + (n % 5) * 4
        if source == "CAM_ALLEY_04_STONE_HIT":
            loc = target + Vector((-1.7 + phase * 0.12, -2.2 + fine * 0.12, 0.82))
            return loc, target, 34 + (n % 4) * 4
        if close:
            loc = target + Vector((-1.65 + phase * 0.12, -2.1 + fine * 0.15, 0.70))
            return loc, target, 38 + (n % 4) * 5
        if text_has(text, "混混", "彬子", "高杆", "大海", "小齐"):
            loc = Vector((33.8 + phase * 0.20, -5.2 + fine * 0.35, 1.35))
            return loc, target, 32 + (n % 4) * 4
        return Vector((31.2 + phase * 0.35, -9.3 + fine * 0.45, 1.45 + (n % 2) * 0.12)), target, 24 + (n % 4) * 4

    if scene == "SCN_CORRIDOR":
        if text_has(text, "消防箱", "墙", "标语", "细节"):
            return Vector((-1.25 + phase * 0.10, target.y - 3.8, 1.05)), target, 42
        loc = Vector((-1.0 + phase * 0.16, max(3.5, target.y - 6.5 + fine * 0.35), 0.95 + (n % 2) * 0.08))
        return loc, target + Vector((0.0, 1.1, 0.2)), 24 + (n % 5) * 3

    if scene == "SCN_PHONE":
        if close:
            loc = target + Vector((-1.35 + phase * 0.14, -1.75 + fine * 0.12, 0.55 + (n % 2) * 0.08))
            return loc, target, 34 + (n % 5) * 4
        loc = Vector((-2.20 + phase * 0.18, 27.65 + fine * 0.22, 1.30 + (n % 3) * 0.06))
        return loc, target + Vector((0.08, 0.35, 0.05)), 28 + (n % 4) * 4

    if scene == "SCN_8BIT":
        loc = Vector((15.0 + phase * 0.22, 26.5 + (n % 4) * 0.45, 2.0 + fine * 0.06))
        if source == "CAM_8BIT_02_WIN_SCREEN":
            loc = Vector((15.0 + phase * 0.18, 28.6 + (n % 3) * 0.35, 2.35 + fine * 0.05))
        return loc, target, None

    return None


def stable_seed(row):
    text = f"{row.get('panel_id', '')}|{row.get('character_blocking', '')}|{row.get('layout_focus', '')}|{row.get('pose_or_path', '')}"
    return sum(ord(ch) for ch in text)


def camera_space_point(cam, local):
    return cam.location + cam.rotation_euler.to_matrix() @ Vector(local)


def add_camera_space_guides(row, cam):
    n = panel_number(row["panel_id"])
    seed = stable_seed(row)
    depth = -3.0 if cam.data.type == "ORTHO" else -2.2
    x = ((seed % 7) - 3) * 0.10
    y = (((seed // 7) % 5) - 2) * 0.08
    color_bank = [
        (1.0, 0.82, 0.05, 1.0),
        (0.10, 0.65, 1.0, 1.0),
        (0.18, 0.85, 0.38, 1.0),
        (1.0, 0.16, 0.12, 1.0),
        (0.92, 0.45, 1.0, 1.0),
    ]
    focus_color = color_bank[seed % len(color_bank)]
    action_color = color_bank[(seed // 5 + 2) % len(color_bank)]
    objs = []

    # A small in-camera focus proxy makes the per-panel beat visible even when
    # the 3D set remains intentionally continuous across adjacent storyboard panels.
    focus_loc = camera_space_point(cam, (x, y, depth))
    focus_scale = (
        0.11 + (n % 3) * 0.025,
        0.11 + ((n // 3) % 3) * 0.025,
        0.11,
    )
    objs.append(proxy_cube(f"WB_CAMERA_FOCUS_{n}", focus_loc, focus_scale, focus_color))

    # Action bar: horizontal/vertical/diagonal-ish variants distinguish still,
    # reach, run, hold, and transition beats without putting text into the frame.
    mode = seed % 4
    if mode == 0:
        bar_local = (x + 0.22, y, depth)
        bar_scale = (0.28, 0.045, 0.045)
    elif mode == 1:
        bar_local = (x, y + 0.20, depth)
        bar_scale = (0.045, 0.28, 0.045)
    elif mode == 2:
        bar_local = (x - 0.20, y - 0.15, depth)
        bar_scale = (0.20, 0.06, 0.12)
    else:
        bar_local = (x + 0.18, y + 0.14, depth)
        bar_scale = (0.12, 0.20, 0.06)
    objs.append(proxy_cube(f"WB_CAMERA_ACTION_{n}", camera_space_point(cam, bar_local), bar_scale, action_color))

    if row["scene_id"] in {"SCN_PHONE", "SCN_8BIT"}:
        pulse_local = (x - 0.24, y + 0.18, depth)
        pulse_scale = (0.07 + (n % 2) * 0.05, 0.07 + ((n + 1) % 2) * 0.05, 0.07)
        objs.append(proxy_cube(f"WB_CAMERA_PULSE_{n}", camera_space_point(cam, pulse_local), pulse_scale, (0.95, 0.95, 0.95, 1.0)))

    return objs


def read_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def panel_number(panel_id):
    match = re.search(r"(\d+)", panel_id or "")
    return int(match.group(1)) if match else 0


def shot_lens_from_focus(layout_focus, pose_or_path):
    text = f"{layout_focus} {pose_or_path}"
    for key, lens in SHOT_LENS.items():
        if key in text:
            return lens
    return None


def row_adjustment(row):
    n = panel_number(row["panel_id"])
    clip = row["clip"]
    scene = row["scene_id"]
    # Small deterministic offsets make each panel specific without violating the base scene axis.
    phase = (n % 5) - 2
    fine = (n % 3) - 1
    loc_offset = Vector((0.0, 0.0, 0.0))
    target_offset = Vector((0.0, 0.0, 0.0))
    lens_delta = 0
    ortho_delta = 0.0

    if scene == "SCN_COMPOUND":
        loc_offset = Vector((phase * 0.22, fine * 0.18, 0.02 * fine))
        target_offset = Vector((phase * 0.12, 0.10 * fine, 0.04 * fine))
    elif scene == "SCN_ARCADE":
        loc_offset = Vector((phase * 0.16, fine * 0.18, 0.04 * fine))
        target_offset = Vector((phase * 0.10, 0.08 * fine, 0.04 * fine))
        if clip in {"04", "05"}:
            lens_delta = 6
    elif scene == "SCN_EXIT":
        loc_offset = Vector((phase * 0.20, fine * 0.15, 0.0))
        target_offset = Vector((phase * 0.12, fine * 0.18, 0.0))
    elif scene == "SCN_ALLEY":
        loc_offset = Vector((phase * 0.18, fine * 0.28, 0.02 * fine))
        target_offset = Vector((phase * 0.12, fine * 0.22, 0.03 * fine))
        if clip == "10":
            lens_delta = 4
        if clip == "11":
            lens_delta = 8
            loc_offset += Vector((-0.25, -0.2, -0.05))
        if clip == "12":
            loc_offset += Vector((-0.15, -0.45, -0.08))
            target_offset += Vector((0.05, 0.65, 0.0))
    elif scene == "SCN_CORRIDOR":
        loc_offset = Vector((phase * 0.08, fine * 0.35, 0.0))
        target_offset = Vector((phase * 0.05, fine * 0.50, 0.0))
    elif scene == "SCN_PHONE":
        loc_offset = Vector((phase * 0.08, fine * 0.22, 0.03 * fine))
        target_offset = Vector((phase * 0.04, fine * 0.16, 0.02 * fine))
        if clip == "17":
            lens_delta = 12
    elif scene == "SCN_8BIT":
        loc_offset = Vector((phase * 0.05, 0.0, fine * 0.04))
        target_offset = Vector((phase * 0.05, 0.0, fine * 0.04))
        ortho_delta = phase * 0.08

    return loc_offset, target_offset, lens_delta, ortho_delta


def duplicate_camera_for_row(row, base_cam):
    n = panel_number(row["panel_id"])
    loc_offset, target_offset, lens_delta, ortho_delta = row_adjustment(row)
    cam_data = base_cam.data.copy()
    cam = base_cam.copy()
    cam.data = cam_data
    cam.name = row["whitebox_id"]
    cam.location = base_cam.location + loc_offset
    forced_target = None
    forced_lens = None
    forced_ortho_scale = None

    if row["source_camera"] == "CAM_ARCADE_02_STREET_FIGHTER_CABINET" and n == 29:
        cam.location = Vector((-2.55, -3.25, 1.18))
        forced_target = Vector((0.0, -0.72, 0.98))
        forced_lens = 24
    elif row["source_camera"] == "CAM_ARCADE_02_STREET_FIGHTER_CABINET" and n == 34:
        cam.location = Vector((1.95, -2.70, 1.18))
        forced_target = Vector((0.62, -1.34, 1.08))
        forced_lens = 42
    elif row["source_camera"] == "CAM_ARCADE_04_BOSS_LOSES_REACTION" and 51 <= n <= 57:
        cam.location = Vector((2.85 + ((n % 3) - 1) * 0.08, -3.15, 1.22))
        forced_target = Vector((0.68, -1.38, 1.0))
        forced_lens = 30
    elif row["source_camera"] == "CAM_ALLEY_02_BLOCKED" and n == 78:
        cam.location = Vector((30.55, -4.95, 1.20))
        forced_target = Vector((30.95, 0.65, 1.22))
        forced_lens = 40
    elif row["source_camera"] == "CAM_ALLEY_02_BLOCKED" and n == 79:
        cam.location = Vector((33.20, -4.70, 1.08))
        forced_target = Vector((32.95, 0.42, 0.98))
        forced_lens = 42
    elif row["source_camera"] == "CAM_ALLEY_05_ESCAPE_VECTOR" and n == 108:
        cam.location = Vector((29.95, -7.35, 1.05))
        forced_target = Vector((31.05, -4.80, 0.95))
        forced_lens = 34
    elif row["source_camera"] == "CAM_ALLEY_05_ESCAPE_VECTOR" and n == 109:
        cam.location = Vector((30.05, -6.95, 0.78))
        forced_target = Vector((31.02, -5.20, 0.82))
        forced_lens = 42
    elif row["source_camera"] == "CAM_PHONE_01_DISTANT_GLOW" and n == 143:
        cam.location = Vector((-0.35, 17.65, 1.18))
        forced_target = Vector((-0.08, 25.05, 1.05))
        forced_lens = 32
    elif row["source_camera"] == "CAM_PHONE_01_DISTANT_GLOW" and n == 144:
        cam.location = Vector((-0.45, 19.20, 1.12))
        forced_target = Vector((-0.10, 26.50, 1.02))
        forced_lens = 38
    elif row["source_camera"] == "CAM_PHONE_02_APPROACH_CLOSE" and n == 153:
        cam.location = Vector((-1.35, 28.85, 1.35))
        forced_target = Vector((0.26, 31.32, 1.28))
        forced_lens = 32
    elif row["source_camera"] == "CAM_PHONE_03_RECEIVER_INSERT" and n in {156, 159}:
        cam.location = Vector((-1.22 + (0.08 if n == 159 else 0.0), 30.12, 1.43))
        forced_target = Vector((0.12, 31.38, 1.34))
        forced_lens = 42

    semantic_override = semantic_camera_override(row, base_cam)
    if semantic_override:
        cam.location, forced_target, forced_lens = semantic_override
        if cam.data.type == "ORTHO" and row["scene_id"] == "SCN_8BIT":
            forced_ortho_scale = 7.4 - min(max(n - 170, 0), 8) * 0.10
            if row["source_camera"] == "CAM_8BIT_02_WIN_SCREEN":
                forced_ortho_scale = 5.7 - min(max(n - 178, 0), 8) * 0.08

    if row["source_camera"] == "CAM_ALLEY_04_STONE_HIT":
        cam.location.x = max(cam.location.x, 29.9)
    if row["source_camera"] == "CAM_CORRIDOR_01_ENTRY_LONG":
        cam.location.y = max(cam.location.y, 3.5)

    base_target = SOURCE_CAMERA_TARGETS.get(
        row["source_camera"],
        SCENE_TARGETS.get(row["scene_id"], (0, 0, 1.2)),
    )
    scene_target = forced_target if forced_target is not None else Vector(base_target) + target_offset
    look_at(cam, scene_target)

    focus_lens = shot_lens_from_focus(row.get("layout_focus", ""), row.get("pose_or_path", ""))
    if cam.data.type == "ORTHO":
        cam.data.ortho_scale = max(4.0, cam.data.ortho_scale + ortho_delta)
        if forced_ortho_scale:
            cam.data.ortho_scale = max(4.0, forced_ortho_scale)
    else:
        if focus_lens:
            cam.data.lens = focus_lens
        cam.data.lens = max(18, min(85, cam.data.lens + lens_delta))
        if forced_lens:
            cam.data.lens = forced_lens

    bpy.context.scene.collection.objects.link(cam)
    return cam


def setup_render():
    bpy.context.scene.render.engine = "BLENDER_WORKBENCH"
    bpy.context.scene.display.shading.light = "STUDIO"
    bpy.context.scene.display.shading.color_type = "MATERIAL"
    bpy.context.scene.render.resolution_x = 1280
    bpy.context.scene.render.resolution_y = 720
    bpy.context.scene.render.film_transparent = False
    bpy.context.scene.view_settings.view_transform = "Standard"


def main():
    if not BLEND_PATH.exists():
        raise FileNotFoundError(BLEND_PATH)
    if not PLAN_PATH.exists():
        raise FileNotFoundError(PLAN_PATH)

    bpy.ops.wm.open_mainfile(filepath=str(BLEND_PATH))
    hide_base_character_anchors()
    setup_render()
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    plan = [row for row in read_csv(PLAN_PATH) if row.get("whitebox_required") == "yes"]
    manifest = []
    skipped = []
    for row in plan:
        base_name = row["source_camera"]
        base_cam = bpy.data.objects.get(base_name)
        if not base_cam or base_cam.type != "CAMERA":
            skipped.append({**row, "status": "missing_source_camera"})
            continue

        batch = row["batch"]
        out_dir = OUT_ROOT / batch
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = ROOT / row["planned_whitebox_path"]
        out_path.parent.mkdir(parents=True, exist_ok=True)

        cam = duplicate_camera_for_row(row, base_cam)
        proxies = add_panel_proxies(row)
        bpy.context.scene.camera = cam
        bpy.context.scene.render.filepath = str(out_path)
        bpy.ops.render.render(write_still=True)
        delete_objects(proxies)
        manifest.append({
            "whitebox_id": row["whitebox_id"],
            "panel_id": row["panel_id"],
            "batch": batch,
            "clip": row["clip"],
            "scene_id": row["scene_id"],
            "source_camera": base_name,
            "render_path": str(out_path),
            "location": tuple(round(v, 3) for v in cam.location),
            "lens_or_ortho": f"ortho {cam.data.ortho_scale:.2f}" if cam.data.type == "ORTHO" else f"{cam.data.lens:.1f}mm",
            "layout_focus": row["layout_focus"],
            "pose_or_path": row["pose_or_path"],
            "status": "rendered",
        })

    fields = [
        "whitebox_id", "panel_id", "batch", "clip", "scene_id", "source_camera",
        "render_path", "location", "lens_or_ortho", "layout_focus", "pose_or_path", "status",
    ]
    write_csv(MANIFEST_PATH, manifest, fields)
    if skipped:
        write_csv(ROOT / "blender" / "whitebox_v2_skipped.csv", skipped, list(skipped[0].keys()))
    print(f"RENDERED={len(manifest)}")
    print(f"SKIPPED={len(skipped)}")
    print(f"MANIFEST={MANIFEST_PATH}")


if __name__ == "__main__":
    main()
