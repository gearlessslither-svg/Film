# R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_016000ms_01

- Priority: `P1_generate_next_small_batch`
- Parent video unit: `VU_REF003_004_AIRCRAFT_BRIEF_REVEAL`
- Source timecode: `00:16.00`
- Reference frame: `01_intake/analysis/video_reference_packages/reference-003-full-op-2160p/frames_sampled/reference-003-full-op-2160p_0033.jpg`
- Reference board: `08_generation/jobs/REFERENCE003_ADAPTIVE_FRAME_PROMOTION_R5_20260630/refs/r5_reference_boards/R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_016000ms_01_board.jpg`
- Required locks: `jean_aircraft, opening_sky_clouds`
- Lock paths: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH02/outputs/OP_SHOT_007.png, 08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630/outputs/OP_SHOT_002.png`
- Planned output: `08_generation/jobs/REFERENCE003_ADAPTIVE_FRAME_PROMOTION_R5_20260630/outputs/R5_VU_REF003_004_AIRCRAFT_BRIEF_REVEAL_016000ms_01.png`

Generate one pure photorealistic 16:9 image asset, not a collage. The reference board left panel is timing/composition/motion reference only and may contain original anime credits, lyrics, subtitles, broadcaster marks, or title text; do not copy any readable text. The right-side panel(s) are identity/prop/scene locks.

Generate a clean Jean-aircraft reveal keyframe. Preserve the handmade retro monoplane design lock; keep sky/cloud motion and remove all text.

Difference reason: Brief aircraft reveal is a fast prop/camera state change; current single anchor does not cover entry and exit/reveal phase.

Hard negatives: no readable text, no logo, no watermark, no subtitles, no Japanese credits, no random glyphs, no split screen, no reference-board border, no anime screenshot style, no changed identity/prop design.
