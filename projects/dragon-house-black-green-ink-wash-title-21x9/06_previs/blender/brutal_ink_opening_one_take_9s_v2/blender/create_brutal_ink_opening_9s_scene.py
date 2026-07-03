import argparse
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector


PROJECT = Path("/Users/jaychoupp/Desktop/Story/Film/projects/dragon-house-black-green-ink-wash-title-21x9/06_previs/blender/brutal_ink_opening_one_take_9s_v2")
BLEND_PATH = PROJECT / "blender" / "brutal_ink_opening_one_take_9s_v2.blend"
FRAMES_DIR = PROJECT / "renders" / "frames"
SAMPLES_DIR = PROJECT / "renders" / "samples"
FPS = 24
FRAME_START = 1
FRAME_END = 216
RES_X = 1344
RES_Y = 576


def ensure_dirs():
    for path in [PROJECT / "blender", FRAMES_DIR, SAMPLES_DIR, PROJECT / "outputs", PROJECT / "docs"]:
        path.mkdir(parents=True, exist_ok=True)


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def make_mat(name, color, roughness=0.85, metallic=0.0):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic
    return mat


def add_cube(name, loc, scale, mat):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if mat:
        obj.data.materials.append(mat)
    bevel = obj.modifiers.new(name="soft_bevel", type="BEVEL")
    bevel.width = min(scale) * 0.08
    bevel.segments = 2
    obj.modifiers.new(name="weighted_normals", type="WEIGHTED_NORMAL")
    return obj


def add_cylinder(name, loc, radius, depth, mat, vertices=48):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc)
    obj = bpy.context.object
    obj.name = name
    if mat:
        obj.data.materials.append(mat)
    obj.modifiers.new(name="weighted_normals", type="WEIGHTED_NORMAL")
    return obj


def add_curve(name, points, mat, bevel=0.08, resolution=3):
    curve = bpy.data.curves.new(name=name, type="CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = resolution
    curve.bevel_depth = bevel
    curve.bevel_resolution = 3
    spline = curve.splines.new("POLY")
    spline.points.add(len(points) - 1)
    for point, co in zip(spline.points, points):
        point.co = (co[0], co[1], co[2], 1.0)
    obj = bpy.data.objects.new(name, curve)
    bpy.context.collection.objects.link(obj)
    if mat:
        curve.materials.append(mat)
    return obj


def keyframe(obj, frame, loc=None, scale=None, rot=None):
    if loc is not None:
        obj.location = loc
        obj.keyframe_insert(data_path="location", frame=frame)
    if scale is not None:
        obj.scale = scale
        obj.keyframe_insert(data_path="scale", frame=frame)
    if rot is not None:
        obj.rotation_euler = rot
        obj.keyframe_insert(data_path="rotation_euler", frame=frame)


def rising_block(name, x, y, h, w, d, start, end, mat):
    obj = add_cube(name, (x, y, h / 2.0), (w, d, h), mat)
    keyframe(obj, start, loc=(x, y, 0.03), scale=(1, 1, 0.02))
    keyframe(obj, end, loc=(x, y, h / 2.0), scale=(1, 1, 1))
    return obj


def make_gear(name, x, y, radius, mat_black, mat_gold, rise_start, rise_end):
    ring = None
    bpy.ops.mesh.primitive_torus_add(major_radius=radius, minor_radius=0.08, major_segments=96, minor_segments=12, location=(x, y, 0.13))
    ring = bpy.context.object
    ring.name = f"{name}_ink_crown_ring"
    ring.data.materials.append(mat_black)
    for i in range(18):
        a = i * math.tau / 18.0
        tx = x + math.cos(a) * (radius + 0.18)
        ty = y + math.sin(a) * (radius + 0.18)
        tooth = add_cube(f"{name}_tooth_{i:02d}", (tx, ty, 0.13), (0.18, 0.42, 0.16), mat_black if i % 3 else mat_gold)
        tooth.rotation_euler[2] = a
    keyframe(ring, rise_start, loc=(x, y, 0.03), rot=(0, 0, -0.15))
    keyframe(ring, rise_end, loc=(x, y, 0.13), rot=(0, 0, 0.8))
    return ring


def make_castle_cluster(prefix, x, y, rise_start, mat_black, mat_gray, mat_gold):
    offsets = [(-0.35, -0.2, 0.9, 0.26), (0.0, 0.1, 1.35, 0.34), (0.35, -0.1, 0.75, 0.22)]
    blocks = []
    for idx, (ox, oy, h, w) in enumerate(offsets):
        mat = mat_black if idx == 1 else mat_gray
        blocks.append(rising_block(f"{prefix}_tower_{idx}", x + ox, y + oy, h, w, w, rise_start, rise_start + 32, mat))
    base = rising_block(f"{prefix}_base", x, y - 0.28, 0.32, 1.1, 0.42, rise_start + 8, rise_start + 38, mat_gold)
    blocks.append(base)
    for i, block in enumerate(blocks):
        block.rotation_euler[2] = (i - 1) * 0.08
    return blocks


def set_interpolation_linear():
    for obj in bpy.data.objects:
        if obj.animation_data and obj.animation_data.action:
            fcurves = getattr(obj.animation_data.action, "fcurves", None)
            if fcurves is None:
                continue
            for fc in fcurves:
                for kp in fc.keyframe_points:
                    kp.interpolation = "BEZIER"


def create_scene():
    ensure_dirs()
    clear_scene()

    scene = bpy.context.scene
    scene.frame_start = FRAME_START
    scene.frame_end = FRAME_END
    scene.render.fps = FPS
    scene.render.resolution_x = RES_X
    scene.render.resolution_y = RES_Y
    scene.render.film_transparent = False
    scene.render.image_settings.file_format = "PNG"
    scene.render.filepath = str(FRAMES_DIR / "frame_")
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
        scene.eevee.taa_render_samples = 48
    except Exception:
        scene.render.engine = "BLENDER_EEVEE"

    mat_paper = make_mat("old_rice_paper_matte", (0.74, 0.68, 0.55, 1))
    mat_ink = make_mat("brutal_black_ink", (0.006, 0.005, 0.004, 1))
    mat_ink_soft = make_mat("smoky_gray_ink", (0.12, 0.115, 0.10, 1))
    mat_green = make_mat("mineral_green_poison", (0.05, 0.28, 0.22, 1))
    mat_cinnabar = make_mat("cinnabar_node", (0.58, 0.06, 0.025, 1))
    mat_gold = make_mat("faint_antique_gold", (0.53, 0.39, 0.18, 1), metallic=0.15)
    mat_bone = make_mat("dragon_bone_shadow", (0.04, 0.037, 0.03, 1))

    # Old paper map plane.
    add_cube("old_rice_paper_world_plate", (1.2, 0.2, -0.04), (26.0, 13.0, 0.08), mat_paper)

    # Main bloodline route, built to create strong parallax under the travelling camera.
    main_route = [
        (-9.5, -2.25, 0.04), (-7.6, -1.55, 0.05), (-5.3, -1.1, 0.06),
        (-3.0, -0.35, 0.07), (-0.8, 0.05, 0.08), (1.6, 0.75, 0.08),
        (3.6, 1.25, 0.08), (6.2, 2.0, 0.08), (8.8, 2.65, 0.08)
    ]
    add_curve("main_black_bloodline_camera_route", main_route, mat_ink, bevel=0.11)
    add_curve("thin_antique_gold_crack_along_route", [(x, y + 0.18, z + 0.015) for x, y, z in main_route], mat_gold, bevel=0.018)
    add_curve("mineral_green_side_channel_left", [(-5.8, -2.4, 0.055), (-3.0, -1.7, 0.065), (0.5, -1.35, 0.07), (3.2, -0.65, 0.08)], mat_green, bevel=0.055)
    add_curve("mineral_green_side_channel_right", [(-1.0, 1.15, 0.06), (1.8, 1.95, 0.07), (4.8, 3.45, 0.075), (7.2, 4.4, 0.08)], mat_green, bevel=0.045)

    # Foreground throne gear and smaller route gears.
    make_gear("foreground_throne", -8.4, -2.25, 0.78, mat_ink, mat_gold, 1, 52)
    make_gear("mid_crown", -1.0, 0.0, 0.48, mat_ink, mat_gold, 42, 88)
    make_gear("distant_crown", 5.9, 2.0, 0.55, mat_ink, mat_gold, 128, 170)

    # Raised castle nodes that wake as the camera passes them.
    make_castle_cluster("node_dragonstone", -4.7, -1.0, 36, mat_ink, mat_ink_soft, mat_gold)
    make_castle_cluster("node_kings_landing", -0.6, 0.2, 78, mat_ink, mat_ink_soft, mat_gold)
    make_castle_cluster("node_harrenhal", 2.6, 1.25, 116, mat_ink, mat_ink_soft, mat_gold)
    make_castle_cluster("node_final_throne_city", 6.8, 2.55, 150, mat_ink, mat_ink_soft, mat_gold)

    # Bridge ribs and sea-channel blockers for the title-sequence traversal feeling.
    for i in range(9):
        x = -2.8 + i * 0.34
        rib = add_cube(f"bridge_rib_{i:02d}", (x, 0.92 + math.sin(i) * 0.05, 0.26), (0.08, 0.9, 0.42), mat_ink)
        keyframe(rib, 56 + i * 2, loc=(x, rib.location.y, 0.04), scale=(1, 1, 0.04))
        keyframe(rib, 88 + i * 2, loc=(x, rib.location.y, 0.26), scale=(1, 1, 1))

    for i, (x, y) in enumerate([(-6.0, 1.9), (-3.4, 2.55), (1.2, 3.2), (4.7, -1.8), (8.3, -0.9)]):
        node = add_cube(f"cinnabar_seal_node_{i}", (x, y, 0.09), (0.35, 0.35, 0.08), mat_cinnabar)
        keyframe(node, 1 + i * 24, scale=(0.65, 0.65, 1))
        keyframe(node, 16 + i * 24, scale=(1.25, 1.25, 1.2))
        keyframe(node, 34 + i * 24, scale=(0.75, 0.75, 1))

    # Dragon-bone arcs near final reveal, kept abstract and non-fleshy.
    for i in range(4):
        pts = []
        for j in range(12):
            t = j / 11
            x = 2.0 + t * 7.2
            y = 4.8 - i * 0.38 - math.sin(t * math.pi) * (1.1 + i * 0.13)
            z = 0.25 + math.sin(t * math.pi) * (0.5 + i * 0.06)
            pts.append((x, y, z))
        arc = add_curve(f"dragon_bone_arc_{i}", pts, mat_bone, bevel=0.045 + i * 0.012)
        keyframe(arc, 130 + i * 8, scale=(0.2, 0.2, 0.2))
        keyframe(arc, 188 + i * 6, scale=(1, 1, 1))

    # Huge flat black brush shadow that sweeps over final aerial view.
    shadow = add_cube("final_black_dragon_eclipse_brush_shadow", (5.6, 3.9, 1.05), (8.5, 0.42, 0.06), mat_ink)
    shadow.rotation_euler[2] = -0.35
    keyframe(shadow, 150, loc=(8.8, 5.8, 1.05), scale=(0.4, 0.4, 1))
    keyframe(shadow, 216, loc=(5.6, 3.9, 1.05), scale=(1.0, 1.0, 1))

    # Paper-grain flecks and ink splatters as small fixed cylinders.
    for i in range(80):
        x = -10.5 + (i * 1.713 % 21.0)
        y = -5.2 + (i * 2.371 % 10.5)
        r = 0.025 + (i % 5) * 0.008
        mat = mat_ink_soft if i % 7 else mat_ink
        add_cylinder(f"ink_splatter_{i:02d}", (x, y, 0.035), r, 0.018, mat, vertices=12)

    # Camera and target.
    target = bpy.data.objects.new("camera_look_target", None)
    bpy.context.collection.objects.link(target)
    cam_data = bpy.data.cameras.new("one_take_camera")
    cam = bpy.data.objects.new("one_take_camera", cam_data)
    bpy.context.collection.objects.link(cam)
    bpy.context.scene.camera = cam
    constraint = cam.constraints.new(type="TRACK_TO")
    constraint.track_axis = "TRACK_NEGATIVE_Z"
    constraint.up_axis = "UP_Y"
    constraint.target = target
    cam.data.lens = 24
    cam.data.dof.use_dof = False

    camera_beats = [
        (1, (-9.4, -3.18, 0.78), (-7.25, -1.65, 0.16), 22),
        (34, (-7.05, -2.35, 0.98), (-4.9, -1.0, 0.34), 24),
        (76, (-3.35, -1.25, 1.18), (-0.8, 0.12, 0.55), 27),
        (118, (0.25, 0.15, 1.95), (2.6, 1.2, 0.8), 30),
        (166, (3.85, 1.55, 4.25), (5.75, 2.25, 0.8), 34),
        (216, (7.15, 4.35, 7.8), (3.2, 0.6, 0.45), 38),
    ]
    for frame, loc, tar, lens in camera_beats:
        cam.location = loc
        target.location = tar
        cam.data.lens = lens
        cam.keyframe_insert(data_path="location", frame=frame)
        cam.data.keyframe_insert(data_path="lens", frame=frame)
        target.keyframe_insert(data_path="location", frame=frame)

    # Lighting.
    bpy.ops.object.light_add(type="AREA", location=(-4.5, -4.5, 6.0))
    key = bpy.context.object
    key.name = "large_pale_rice_paper_softbox"
    key.data.energy = 560
    key.data.size = 8.0
    bpy.ops.object.light_add(type="POINT", location=(4.8, 3.4, 3.0))
    green_light = bpy.context.object
    green_light.name = "mineral_green_channel_glow"
    green_light.data.color = (0.15, 0.62, 0.48)
    green_light.data.energy = 60
    bpy.ops.object.light_add(type="POINT", location=(-4.8, 1.2, 2.3))
    red_light = bpy.context.object
    red_light.name = "cinnabar_node_pulse"
    red_light.data.color = (0.95, 0.12, 0.05)
    red_light.data.energy = 35

    set_interpolation_linear()
    scene.frame_set(1)
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))


def render_frames(frames):
    scene = bpy.context.scene
    for frame in frames:
        scene.frame_set(frame)
        scene.render.filepath = str((SAMPLES_DIR if len(frames) < 10 else FRAMES_DIR) / f"frame_{frame:04d}.png")
        bpy.ops.render.render(write_still=True)


def render_full():
    scene = bpy.context.scene
    scene.render.filepath = str(FRAMES_DIR / "frame_")
    bpy.ops.render.render(animation=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["scene", "samples", "full"], default="scene")
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    args = parser.parse_args(argv)
    create_scene()
    if args.mode == "samples":
        render_frames([1, 72, 144, 216])
    elif args.mode == "full":
        render_full()


if __name__ == "__main__":
    main()
