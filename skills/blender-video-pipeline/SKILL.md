---
name: blender-video-pipeline
description: End-to-end Blender video production pipeline for Codex. Use when Codex needs to install or check a Blender/video environment, create procedural Blender scenes, build models/materials/animation/camera moves, render frame sequences, encode frames to video, QA outputs, or package Blender motion-reference videos for AIGC video generation from keyframes and prompts.
---

# Blender Video Pipeline

Use this skill for complete Blender video workflows, from environment setup through final video packaging. It is especially useful for AIGC film work where Blender supplies motion, space, timing, and camera reference while image keyframes supply the final art style.

## Core Workflow

1. Define the deliverable: aspect ratio, duration, fps, visual purpose, final audience, and whether the output is final render, previs, motion reference, or AIGC control video.
2. Create a project package:
   - `inputs/` for reference images, keyframes, sketches, audio, source videos.
   - `blender/` for `.blend` files and Blender Python scripts.
   - `renders/frames/` for PNG or EXR frame sequences.
   - `outputs/` for encoded MP4/ProRes/WebM/GIF deliverables.
   - `docs/` for prompts, shot notes, render notes, QA notes.
3. Check or bootstrap the environment. Read `references/env-setup.md`, then run `scripts/check_env.py`. If video encoding packages are missing, use `scripts/bootstrap_video_env.py` in a project-local virtual environment.
4. Build a Blender automation script. Read `references/blender-automation.md` before writing scene-generation code.
5. Render a small sample first: start, midpoint, and final frame, or a 24-48 frame motion slice. Inspect framing, scale, blank frames, camera target, and major motion before full render.
6. Render the full shot as a frame sequence first. Prefer image frames over direct video output because they are resumable, inspectable, and easy to re-encode.
7. Encode the frame sequence with `scripts/encode_frames.py`. Use H.264 MP4 for AIGC upload, ProRes or high-quality H.264 for editing masters when needed.
8. QA the output: frame count, duration, aspect ratio, codec, visible motion, no accidental text/logos, no blank frames, no incoherent overlaps, and no camera clipping.
9. For AIGC usage, read `references/aigc-reference-packaging.md` and write prompts that explicitly separate style inputs from Blender motion/reference inputs.

## Environment Rules

- Prefer the installed Blender binary if present. On macOS, check `/Applications/Blender.app/Contents/MacOS/Blender` before assuming `blender` is on PATH.
- Use project-local dependencies for video tools. Do not pollute the system Python when a `.venv-video` environment will do.
- If system `ffmpeg` is unavailable, use `imageio-ffmpeg` from the project venv and point `scripts/encode_frames.py` at that executable automatically.
- Keep Blender renders deterministic: fixed fps, fixed frame range, fixed random seed, absolute output paths, and saved `.blend` before rendering.

## Blender Build Rules

- Model enough geometry for the task's purpose. A motion-reference video needs clear spatial relationships, silhouettes, scale, occlusion, and mechanical beats more than final surfacing.
- Animate named control objects, not many raw meshes, when pieces must rise, fold, rotate, or track together.
- Use a camera target object and a tracking constraint for one-take shots. Keyframe both camera and target.
- Use frame-accurate timing notes. For a 10s 24fps shot, speak in frames as well as seconds: `1-72`, `73-144`, `145-240`.
- Save the `.blend`, the Blender script, the frame sequence, and the encoded video. AIGC failures are easier to repair when the control source is reproducible.

## AIGC Motion-Reference Pattern

When using Blender video plus keyframes for AIGC video:

- Treat keyframes/reference images as style, composition, materials, palette, and final visual target.
- Treat the Blender video as camera path, object movement, spatial continuity, timing, parallax, and construction logic.
- Tell the AIGC model not to copy Blender's plain preview materials unless those materials are intentional.
- Use negative prompts against hard cuts, scene jumps, rubbery geometry, melting mechanics, random camera shake, and style drift.
- If the motion is complex, generate a second Blender pass with simpler high-contrast materials or labeled color groups for control, while keeping the final aesthetic keyframes separate.

## Useful Scripts

- `scripts/check_env.py`: report Blender, Python video libraries, FFmpeg, and macOS video tool availability.
- `scripts/scaffold_project.py`: create the standard Blender video package folders and a render brief.
- `scripts/run_blender_script.py`: run a Blender Python scene script with the correct Blender binary.
- `scripts/bootstrap_video_env.py`: create a local `.venv-video` and install common video/post libraries.
- `scripts/encode_frames.py`: encode a PNG/JPG frame sequence to MP4 using system FFmpeg or `imageio-ffmpeg`.
- `scripts/make_contact_sheet.py`: create a visual QA sheet from key frames in a rendered sequence.

## Safety And Scope

- Do not delete prior renders or user source assets unless explicitly asked. Write versioned outputs instead.
- If a render is long, render samples first and keep the user updated.
- If working inside an AIGC Film/Story project, run the session-size guard first and keep image/video payloads on disk rather than re-embedding them in chat.
