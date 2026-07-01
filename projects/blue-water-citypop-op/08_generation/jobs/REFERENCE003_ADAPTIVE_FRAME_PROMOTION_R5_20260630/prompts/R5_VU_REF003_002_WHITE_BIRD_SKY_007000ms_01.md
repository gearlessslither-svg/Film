# R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01

- Priority: `P1_generate_next_small_batch`
- Parent video unit: `VU_REF003_002_WHITE_BIRD_SKY`
- Source timecode: `00:07.00`
- Reference frame: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0015.jpg`
- Reference board: `08_generation/jobs/REFERENCE003_ADAPTIVE_FRAME_PROMOTION_R5_20260630/refs/r5_reference_boards/R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01_board.jpg`
- Required locks: `white_bird, opening_sky_clouds`
- Lock paths: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630/outputs/OP_SHOT_003.png, 08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630/outputs/OP_SHOT_002.png`
- Planned output: `08_generation/jobs/REFERENCE003_ADAPTIVE_FRAME_PROMOTION_R5_20260630/outputs/R5_VU_REF003_002_WHITE_BIRD_SKY_007000ms_01.png`

Generate one pure photorealistic 16:9 image asset, not a collage. The reference board left panel is timing/composition/motion reference only and may contain original anime credits, lyrics, subtitles, broadcaster marks, or title text; do not copy any readable text. The right-side panel(s) are identity/prop/scene locks.

Generate a clean white-bird sky motion keyframe. Preserve the same white bird design and saturated blue sky; remove all lyrics/credits/text from the original reference frame.

Difference reason: White bird glide changes screen position/scale within a long sky movement; useful middle/final action anchor without generating every frame.

Hard negatives: no readable text, no logo, no watermark, no subtitles, no Japanese credits, no random glyphs, no split screen, no reference-board border, no anime screenshot style, no changed identity/prop design.
