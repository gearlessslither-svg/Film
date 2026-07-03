# Brutal Ink Omen Story20 + Opening 9s + Blender Final V1

Project: `dragon-house-black-green-ink-wash-title-21x9`

## Contents

- `images/story20/`: 20 final story/event/person images.
- `images/opening_9s/`: opening 9s v2 start/end frames.
- `prompts/AIGC_VIDEO_PROMPT_INDEX.md`: AIGC prompts for opening + story20.
- `blender_9s_v2/inputs/`: Blender/AIGC start and end frames.
- `blender_9s_v2/outputs/brutal_ink_opening_one_take_9s_v2_motion_reference.mp4`: 9s Blender motion-reference video.
- `blender_9s_v2/outputs/blender_motion_reference_contact_sheet.jpg`: Blender motion contact sheet.
- `blender_9s_v2/docs/AIGC_OPENING_9S_PROMPT_WITH_BLENDER_REFERENCE.md`: detailed AIGC prompt for the 9s opening using start frame + Blender reference + loose end-frame reference.
- `blender_9s_v2/docs/RENDER_NOTES_AND_QA.md`: render specs and QA notes.
- `blender_9s_v2/blender/`: reproducible Blender script and `.blend` scene.
- `contact_sheets/`: story20 and opening image contact sheets.

## Important AIGC Opening Rule

For the 9s opening, use the start frame as the hard first-frame visual lock. Use the Blender video as the primary reference for camera movement, spatial continuity, parallax, object timing, and one-take stability. Use the end frame only as a loose final-reveal reference; do not force exact end-frame matching if it causes jitter, morphing, or unstable geometry.

## Audio Rule

Every AIGC video prompt uses: sound effects and ambience only; no music, no BGM, no soundtrack.

## Style Rule

Use only `Brutal Ink Dragon Omen`: splashed black ink, old rice paper, dry brush, flying-white gaps, sparse mineral green, sparse cinnabar, faint antique-gold cracks, severe negative space.

Do not use shadow-puppet, cut-paper, leather-puppet, ornate-card, black-gold card, soft scenic ink wash, old Blender proxy style, readable text, logos, actor likeness, exact official costume, or readable sigils.
