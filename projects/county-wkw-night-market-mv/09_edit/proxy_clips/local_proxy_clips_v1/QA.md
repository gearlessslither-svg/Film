# Local Proxy Clips V1 QA

Project: `county-wkw-night-market-mv`  
QA date: 2026-07-08  
Folder: `09_edit/proxy_clips/local_proxy_clips_v1/`

## Result

Status: pass as local proxy clips.

All 14 VP/KF segments have a corresponding local proxy MP4 clip and ambience-only audio source. These clips can be used for local editing and replacement planning while waiting for external AIGC image-to-video outputs.

## Technical Check

- Proxy MP4 clips: 14
- Ambience WAV files: 14
- Clip audio rule: ambience/SFX only, no music/BGM/soundtrack
- Final proxy MV assembly source: `ffmpeg_concat_clips.txt`

## Creative Check

- Motion is intentionally subtle and based on keyframe pan/zoom.
- Each clip preserves the intended shot function from `video_prompts_v1`.
- The clips should be replaced by external AIGC video before final delivery.

## Known Limits

- No true model-generated motion.
- No character performance beyond local camera movement.
- Ambience is procedural placeholder audio, not final sound design.
