# Moving Preview V1 Manifest

Project: `county-wkw-night-market-mv`  
Created: 2026-07-08  
Type: local moving preview assembled from V1 keyframes  
Output: `county_wkw_moving_preview_v1_with_scratch_music.mp4`

## Purpose

Provide a playable first MV preview before external image-to-video generation. This preview uses the approved V1 keyframes with subtle local pan/zoom motion and an original scratch music bed. It is useful for reviewing rhythm, emotional flow, and edit structure.

This is not the final AIGC moving MV because the 14 image-to-video clips have not been generated yet.

## Source

- Keyframes: `08_generation/jobs/keyframes_v1/outputs/`
- Video prompt package: `08_generation/jobs/video_prompts_v1/PROMPTS.md`
- Edit guide: `09_edit/EDIT_GUIDE_V1.md`
- Build script: `09_edit/tools/build_moving_preview_v1.py`
- Timing: `moving_preview_timing.csv`
- Scratch music: `scratch_music_v1_original.wav`

## Specs

- Duration: 75.00 seconds
- Resolution: 1920 x 824
- Frame rate: 24 fps
- Video codec: H.264 / yuv420p
- Audio codec: AAC LC
- Audio: original scratch music, 44.1 kHz stereo

## Review Notes

- This preview intentionally uses subtle Ken-Burns style motion from still keyframes.
- It is meant for timing and mood review, not for judging final image-to-video motion quality.
- External AIGC video clips should still be generated from `video_prompts_v1` before final delivery.
