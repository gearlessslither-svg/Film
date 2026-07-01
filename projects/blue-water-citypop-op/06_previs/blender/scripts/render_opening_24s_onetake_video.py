#!/usr/bin/env python3
"""Render the saved opening one-take Blender scene to an MP4 playblast."""

from pathlib import Path

import bpy


PROJECT_ROOT = Path("/Users/jaychoupp/Story/Film/projects/blue-water-citypop-op")
VIDEO_PATH = PROJECT_ROOT / "06_previs/playblasts/opening_24s_onetake_previs.mp4"

FPS = 24
START = 1
END = FPS * 24
RES_X = 1280
RES_Y = 548


def main() -> None:
    scene = bpy.context.scene
    VIDEO_PATH.parent.mkdir(parents=True, exist_ok=True)
    scene.frame_start = START
    scene.frame_end = END
    scene.render.fps = FPS
    scene.render.resolution_x = RES_X
    scene.render.resolution_y = RES_Y
    scene.render.resolution_percentage = 100
    scene.render.filepath = str(VIDEO_PATH)
    if hasattr(scene.render.image_settings, "media_type"):
        scene.render.image_settings.media_type = "VIDEO"
    else:
        scene.render.image_settings.file_format = "FFMPEG"
    scene.render.ffmpeg.format = "MPEG4"
    scene.render.ffmpeg.codec = "H264"
    scene.render.ffmpeg.audio_codec = "NONE"
    scene.render.ffmpeg.video_bitrate = 12000
    scene.render.ffmpeg.maxrate = 14000
    scene.render.ffmpeg.minrate = 4000
    scene.render.ffmpeg.buffersize = 224 * 8
    if hasattr(scene.render.ffmpeg, "constant_rate_factor"):
        scene.render.ffmpeg.constant_rate_factor = "HIGH"
    bpy.ops.render.render(animation=True)


if __name__ == "__main__":
    main()
