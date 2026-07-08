# Local Proxy Clips V1 Manifest

Project: `county-wkw-night-market-mv`  
Created: 2026-07-08  
Type: local image-to-video proxy clips  
Output folder: `outputs/`

## Purpose

Provide 14 replaceable local proxy clips for VP001-VP014 before external AIGC image-to-video generation. Each clip uses the corresponding keyframe with subtle local pan/zoom motion and ambience/SFX-only audio.

These clips are not external AIGC generated video. They are temporary edit proxies.

## Audio Rule

Clip audio is ambience/SFX only. No music, no BGM, no soundtrack is embedded in the individual proxy clips.

## Files

- Timing: `local_proxy_clips_timing.csv`
- Clip concat list: `ffmpeg_concat_clips.txt`
- Ambience WAV files: `audio/`
- Proxy MP4 clips: `outputs/`

## Counts

- Expected clips: 14
- Generated clips: 14
- Expected ambience WAV files: 14

## Next

Replace each local proxy clip with the matching external AIGC image-to-video result when available.
