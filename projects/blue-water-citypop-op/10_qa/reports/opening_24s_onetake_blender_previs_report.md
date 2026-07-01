# Opening 24s One-Take Blender Previs Report

Updated: 2026-06-30 01:11 Asia/Shanghai

## Result

PASS for director previs / camera blocking review.

This is a whitebox/previs pass, not final beauty render. It tests whether the first 24 seconds can be treated as one continuous shot: white bird already gliding in blue sky and clouds -> follow the bird -> reveal a Jean-style retro flying machine -> return to blue sky, clouds, and bird.

## Deliverables

- Playblast MP4: `06_previs/playblasts/opening_24s_onetake_previs.mp4`
- Blender file: `06_previs/blender/opening_24s_onetake_previs.blend`
- Build script: `06_previs/blender/scripts/build_opening_24s_onetake_previs.py`
- Video render script: `06_previs/blender/scripts/render_opening_24s_onetake_video.py`
- Full frame sequence: `06_previs/renders/opening_24s_onetake_animation_frames/opening_24s_0001.png` through `opening_24s_0576.png`
- Key stills: `06_previs/renders/opening_24s_onetake_frames/`
- Keyframe contact sheet: `10_qa/reports/contact_sheet_OPENING_24S_ONETAKE_PREVIS_KEYFRAMES.jpg`
- Unit prompt: `07_shots/video_prompts_by_unit/VU_001_024_OPENING_SKY_BIRD_PLANE_ONETAKE.md`

## Technical Check

- Duration: 24.00 seconds
- FPS: 24
- Frame count: 576
- Resolution: 1280 x 548
- Aspect: 21:9 close, 320:137 display aspect
- Blender: 5.1.2
- Video codec: H.264 MP4 from Blender internal video output

## Timing Map

| Frame | Time | Role |
|---:|---:|---|
| 0001 | 00:00 | White bird already gliding in blue sky |
| 0049 | 00:02 | White bird enters |
| 0145 | 00:06 | Tracking bird through sky |
| 0217 | 00:09 | Retro flying machine reveal |
| 0313 | 00:13 | Bird and flying machine share sky space |
| 0433 | 00:18 | Camera returns attention to sky and bird |
| 0576 | 00:24 | Final blue sky / cloud / bird state |

## Production Decision

This pass is registered as `VU_001_024_OPENING_SKY_BIRD_PLANE_ONETAKE` and marked `candidate_replacement_pending_user_review`.

If approved, the current first 24 seconds should be recut. This candidate supersedes the existing split opening logic for review:

- `VU_001_CLOUD_PRELUDE`
- `VU_002_BIRD_PLANE_SKY_CHAIN`
- `VU_003_SUN_FLASH_WIPE`
- `VU_004_CHARACTER_INTRO_MONTAGE:00:12-00:24`

## AIGC Use

For final AIGC video generation, use this order:

1. Blender camera/playblast as motion and spatial truth.
2. Start/end/key frames as visual anchors.
3. AIGC video prompt with explicit `图1` through `图7` continuity.
4. Reject outputs that add hard cuts, random aircraft inserts, title text, logos, or inconsistent bird/sky geography.

## Limits

- Bird and aircraft are proxy models for camera proof, not final hero assets.
- Clouds are procedural whitebox clusters, not final volumetric clouds.
- MP4 is a review encode; PNG frame sequence is the visual master for this previs.
