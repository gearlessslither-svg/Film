import bpy
import math
from pathlib import Path
from mathutils import Vector

ROOT = Path('/Users/jaychoupp/Story/Film/projects/all-came-last-show/08_generation/jobs/environment_whiteboxes_v1')
RENDERS = ROOT / 'renders_attempt_003'
BLENDS = ROOT / 'blender'
RENDERS.mkdir(parents=True, exist_ok=True)
BLENDS.mkdir(parents=True, exist_ok=True)


def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for datablocks in (bpy.data.meshes, bpy.data.curves, bpy.data.materials, bpy.data.cameras, bpy.data.lights):
        pass


def mat(name, color):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.diffuse_color = (*color, 1.0)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get('Principled BSDF')
    bsdf.inputs['Base Color'].default_value = (*color, 1.0)
    bsdf.inputs['Roughness'].default_value = 0.92
    return m


WHITE = None
TEAL = None
OCHRE = None
BRICK = None
CHARCOAL = None
WINDOW = None


def setup_materials():
    global WHITE, TEAL, OCHRE, BRICK, CHARCOAL, WINDOW
    WHITE = mat('proxy_offwhite', (0.72, 0.70, 0.62))
    TEAL = mat('continuity_teal', (0.08, 0.20, 0.20))
    OCHRE = mat('blocking_ochre', (0.52, 0.34, 0.10))
    BRICK = mat('building_brick', (0.34, 0.16, 0.10))
    CHARCOAL = mat('edge_charcoal', (0.045, 0.055, 0.055))
    WINDOW = mat('window_cold', (0.24, 0.42, 0.46))


def cube(name, loc, scale, material, bevel=0.06):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if material:
        obj.data.materials.append(material)
    if bevel:
        mod = obj.modifiers.new('small_bevel', 'BEVEL')
        mod.width = bevel
        mod.segments = 2
    return obj


def cylinder(name, loc, radius, depth, material):
    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=radius, depth=depth, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    return obj


def target_camera(name, loc, target, lens=32):
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.object
    cam.name = name
    cam.data.lens = lens
    direction = Vector(target) - cam.location
    cam.rotation_euler = direction.to_track_quat('-Z', 'Y').to_euler()
    return cam


def setup_render():
    scene = bpy.context.scene
    scene.render.engine = 'BLENDER_EEVEE'
    scene.render.resolution_x = 960
    scene.render.resolution_y = 540
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = 'PNG'
    scene.render.film_transparent = False
    scene.world.color = (0.025, 0.035, 0.04)
    bpy.ops.object.light_add(type='AREA', location=(-6, -7, 14))
    key = bpy.context.object
    key.name = 'large_soft_key'
    key.data.energy = 1300
    key.data.shape = 'DISK'
    key.data.size = 10
    key.rotation_euler = (math.radians(22), 0, math.radians(-25))
    bpy.ops.object.light_add(type='AREA', location=(8, 6, 10))
    fill = bpy.context.object
    fill.name = 'warm_fill'
    fill.data.energy = 700
    fill.data.color = (1.0, 0.58, 0.25)
    fill.data.size = 8


def render_views(scene_id, cameras):
    scene = bpy.context.scene
    bpy.ops.wm.save_as_mainfile(filepath=str(BLENDS / f'{scene_id}_whitebox_attempt_003.blend'))
    for idx, cam in enumerate(cameras, start=1):
        scene.camera = cam
        scene.render.filepath = str(RENDERS / f'{scene_id}_view_{idx:02d}.png')
        bpy.ops.render.render(write_still=True)


def build_locker_room():
    clear_scene()
    setup_materials()
    setup_render()
    cube('floor', (0, 1, -0.25), (7.5, 6.5, 0.25), WHITE)
    cube('back_wall', (0, 7.25, 2.8), (7.5, 0.18, 3.05), WHITE)
    cube('left_wall', (-7.35, 1, 2.8), (0.18, 6.25, 3.05), WHITE)
    cube('right_wall_front', (7.35, -2.0, 2.8), (0.18, 3.2, 3.05), WHITE)
    cube('right_wall_back', (7.35, 6.0, 2.8), (0.18, 1.2, 3.05), WHITE)
    for i, x in enumerate([-5.7, -4.1, -2.5, -0.9, 0.7, 2.3, 3.9, 5.5]):
        cube(f'locker_{i+1:02d}', (x, 6.75, 2.15), (0.7, 0.35, 2.15), TEAL, 0.03)
    for y in (-1.2, 2.3):
        cube(f'bench_top_{y}', (0, y, 0.58), (4.8, 0.48, 0.18), OCHRE)
        for x in (-4.1, 0, 4.1):
            cube(f'bench_leg_{x}_{y}', (x, y, 0.26), (0.18, 0.38, 0.26), CHARCOAL, 0.02)
    cube('left_high_window_01', (-7.12, -0.8, 3.8), (0.08, 1.2, 1.25), WINDOW, 0)
    cube('left_high_window_02', (-7.12, 3.2, 3.8), (0.08, 1.2, 1.25), WINDOW, 0)
    cube('exit_threshold', (7.15, 2.0, 0.08), (0.3, 1.35, 0.08), OCHRE, 0)
    cams = [
        target_camera('cam_master', (12.5, -13.5, 8.2), (0, 2.1, 1.5), 33),
        target_camera('cam_high', (0, -0.5, 18.5), (0, 1.5, 0), 24),
        target_camera('cam_reverse', (-5.2, 5.0, 3.3), (4.8, 0.0, 1.4), 28),
    ]
    render_views('ENV-01', cams)


def build_square_hall():
    clear_scene()
    setup_materials()
    setup_render()
    cube('square_floor', (0, 0, -0.25), (11, 9, 0.25), WHITE)
    cube('hall_floor', (0, 11.5, -0.20), (6.2, 5.0, 0.20), OCHRE)
    cube('hall_left_wall', (-6.1, 11.5, 3.2), (0.3, 5.0, 3.2), BRICK)
    cube('hall_right_wall', (6.1, 11.5, 3.2), (0.3, 5.0, 3.2), BRICK)
    cube('hall_back_wall', (0, 16.35, 3.2), (6.2, 0.25, 3.2), BRICK)
    cube('hall_front_left', (-4.7, 6.65, 3.2), (1.4, 0.25, 3.2), BRICK)
    cube('hall_front_right', (4.7, 6.65, 3.2), (1.4, 0.25, 3.2), BRICK)
    cube('hall_front_header', (0, 6.65, 5.4), (3.35, 0.25, 1.0), BRICK)
    cube('balcony', (0, 14.1, 3.8), (4.8, 1.05, 0.18), TEAL)
    cube('balcony_rail', (0, 13.1, 4.35), (4.8, 0.08, 0.55), CHARCOAL, 0.02)
    cube('stage', (-5.2, -1.2, 0.42), (3.2, 2.1, 0.42), OCHRE)
    cube('long_table', (5.3, -1.0, 0.72), (2.9, 0.62, 0.12), TEAL)
    for x in (3.0, 7.6):
        cube(f'table_leg_{x}', (x, -1.0, 0.35), (0.14, 0.48, 0.35), CHARCOAL, 0.02)
    for side in (-1, 1):
        for idx, y in enumerate((-5.2, 0.0, 4.3)):
            cube(f'hostel_{side}_{idx}', (side * 10.2, y, 2.2), (1.1, 2.0, 2.2), BRICK)
    cylinder('factory_chimney', (-8.1, 14.2, 5.5), 0.55, 11.0, CHARCOAL)
    for x in (-7.2, -2.4, 2.4, 7.2):
        cylinder(f'light_pole_{x}', (x, 1.7, 2.2), 0.06, 4.4, CHARCOAL)
    cams = [
        target_camera('cam_master', (16.5, -18.0, 11.0), (0, 6.5, 1.6), 36),
        target_camera('cam_high', (0, -4.0, 34.0), (0, 5.5, 0), 28),
        target_camera('cam_hall_reverse', (0, 10.5, 3.5), (0, 0.0, 1.0), 30),
    ]
    render_views('ENV-02', cams)


build_square_hall()
