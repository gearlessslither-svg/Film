# Environment Setup

Use this reference before starting a Blender video job or when encoding/rendering fails.

## Check The Machine

Run:

```bash
python3 ~/.codex/skills/blender-video-pipeline/scripts/check_env.py
```

The checker reports:

- Blender binary candidates and version.
- Current Python executable and key packages.
- System `ffmpeg`, `imageio-ffmpeg`, and macOS `avconvert`.
- Basic recommended next steps.

On macOS, Blender is often available at:

```bash
/Applications/Blender.app/Contents/MacOS/Blender
```

Use `BLENDER_BIN=/path/to/blender` when a project needs a specific Blender version.

## Bootstrap A Local Video Environment

Use a project-local venv when Python packages for video work are missing:

```bash
python3 ~/.codex/skills/blender-video-pipeline/scripts/bootstrap_video_env.py \
  --venv /path/to/project/.venv-video
```

This installs practical post-production packages:

- `pillow` for image inspection/contact sheets.
- `numpy` for frame analysis.
- `imageio` and `imageio-ffmpeg` for portable FFmpeg access.
- `moviepy` for simple editorial assembly when useful.

After setup, run scripts with:

```bash
/path/to/project/.venv-video/bin/python ~/.codex/skills/blender-video-pipeline/scripts/encode_frames.py ...
```

## Encoding Preference

Preferred path:

1. Render PNG or EXR frames from Blender.
2. Encode with `encode_frames.py`.
3. Keep the original frames until QA passes.

Use H.264 MP4 for AIGC upload. Use a higher-quality intermediate such as ProRes only when an editing workflow needs it and a suitable encoder is available.

## Common Fixes

- If `blender` is not on PATH, call `/Applications/Blender.app/Contents/MacOS/Blender` directly.
- If Blender direct MP4 output changes across versions, render frames and encode externally.
- If FFmpeg is missing, bootstrap the venv and let `imageio-ffmpeg` provide the executable.
- If a render is too slow, render a motion-reference pass first using Eevee, simpler materials, lower samples, and frame-step previews before final quality.
