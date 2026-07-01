# R5_VU_REF003_019_WATER_SPLASH_TRANSITION_078500ms_01

- Priority: `P1_generate_next_small_batch`
- Parent video unit: `VU_REF003_019_WATER_SPLASH_TRANSITION`
- Source timecode: `01:18.50`
- Reference frame: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0158.jpg`
- Reference board: `08_generation/jobs/REFERENCE003_ADAPTIVE_FRAME_PROMOTION_R5_20260630/refs/r5_reference_boards/R5_VU_REF003_019_WATER_SPLASH_TRANSITION_078500ms_01_board.jpg`
- Required locks: `water_burst_transition`
- Lock paths: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_038.png`
- Planned output: `08_generation/jobs/REFERENCE003_ADAPTIVE_FRAME_PROMOTION_R5_20260630/outputs/R5_VU_REF003_019_WATER_SPLASH_TRANSITION_078500ms_01.png`

Generate one pure photorealistic 16:9 image asset, not a collage. The reference board left panel is timing/composition/motion reference only and may contain original anime credits, lyrics, subtitles, broadcaster marks, or title text; do not copy any readable text. The right-side panel(s) are identity/prop/scene locks.

Generate a clean water-splash transition keyframe. Preserve the blue-white burst state and transition function; no text or symbols.

Difference reason: Water burst transition has materially different splash/sky states; extra anchor helps preserve transition logic.

Hard negatives: no readable text, no logo, no watermark, no subtitles, no Japanese credits, no random glyphs, no split screen, no reference-board border, no anime screenshot style, no changed identity/prop design.
