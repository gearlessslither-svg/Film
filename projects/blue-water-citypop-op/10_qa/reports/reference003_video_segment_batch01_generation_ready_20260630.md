# Reference-003 Video Segment Batch01 Generation Ready

- Created: `2026-06-30T14:49:39+08:00`
- Status: `ready_for_external_aigc_video_generation`
- Orders: `[1, 2, 3]`

## Jobs

| Unit | Ready | Reference clip | Generation brief | Expected output |
|---|---:|---|---|---|
| `VU_REF003_001_BLACK_CLOUD_FADEIN` | `True` | `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_001_BLACK_CLOUD_FADEIN/reference_clip/VU_REF003_001_BLACK_CLOUD_FADEIN_reference.mp4` | `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_001_BLACK_CLOUD_FADEIN/AIGC_VIDEO_GENERATION_BRIEF.md` | `08_generation/outputs/video/reference003_segments/VU_REF003_001_BLACK_CLOUD_FADEIN.mp4` |
| `VU_REF003_002_WHITE_BIRD_SKY` | `True` | `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_002_WHITE_BIRD_SKY/reference_clip/VU_REF003_002_WHITE_BIRD_SKY_reference.mp4` | `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_002_WHITE_BIRD_SKY/AIGC_VIDEO_GENERATION_BRIEF.md` | `08_generation/outputs/video/reference003_segments/VU_REF003_002_WHITE_BIRD_SKY.mp4` |
| `VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS` | `True` | `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/reference_clip/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS_reference.mp4` | `08_generation/jobs/REFERENCE003_VIDEO_SEGMENTS_20260630/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS/AIGC_VIDEO_GENERATION_BRIEF.md` | `08_generation/outputs/video/reference003_segments/VU_REF003_003_CREDIT_SAFE_BIRD_CLOUDS.mp4` |

## Boundary

Use each job's reference clip, keyframe anchors, and generation brief in a video-capable AIGC tool; save returned MP4s to expected_video_output_path, then run roughcut/audit scripts.
