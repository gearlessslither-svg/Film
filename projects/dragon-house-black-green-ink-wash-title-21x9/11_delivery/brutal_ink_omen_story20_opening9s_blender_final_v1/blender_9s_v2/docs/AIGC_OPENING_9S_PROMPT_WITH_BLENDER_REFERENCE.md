# AIGC Opening 9s Prompt With Blender Reference

Project: `dragon-house-black-green-ink-wash-title-21x9`
Shot: `brutal_ink_opening_one_take_9s_v2`
Duration: 9 seconds
Aspect: 21:9

## Inputs

1. Start frame, hard visual lock:
   `inputs/start_frame.png`
2. End frame, loose final-reveal reference only:
   `inputs/end_frame.png`
3. Blender motion reference:
   `outputs/brutal_ink_opening_one_take_9s_v2_motion_reference.mp4`
4. Sole style reference:
   `04_lookdev/style_references/brutal_ink_omen_v1/director_reference_only_style.png`

## Input Roles

- Use the start frame as the exact first-frame target. Lock its composition, palette, old-paper ground, foreground black ink canal, near throne-gear/crown-wheel scale, and brutal ink texture.
- Use the Blender video as the primary motion reference: camera path, parallax, one-take continuity, timing, map-node order, castle/gear/rib rise timing, crane-up, and final aerial reveal.
- Use the end frame only as a loose final-reveal reference for scale, mood, and destination. Do not force an exact pixel match to the end frame if that causes jitter, morphing, or unstable geometry. The AIGC model's final frame may differ as long as it preserves the same broad idea: high oblique power map, raised nodes, black dragon eclipse, mineral-green channels, cinnabar nodes, brutal ink atmosphere.
- Use the style reference only for brutal ink look. Do not copy its composition or bottom filename/text.

## Generate In The Final Video

- Old rice-paper mechanical bloodline map.
- Black ink bloodline canal that pulls the camera forward.
- Foreground throne-gear / crown-wheel at the start.
- Raised castle nodes, bridge ribs, crown gears, sea channels, dragon-bone arcs.
- Sparse mineral-green poison stains inside selected grooves and waterways.
- Sparse cinnabar seal-like nodes with no readable characters.
- Faint antique-gold cracks on gears, route edges, raised castles, and map cuts.
- Huge abstract black dry-brush dragon omen / eclipse over the final aerial view.
- Ink splatter, dry-brush fiber, flying-white gaps, paper grain, smoke pressure.

## Use Only As Reference, Do Not Visibly Generate

- Blender's plain preview materials.
- Blender's simplified cube/cylinder geometry as literal final shapes.
- Any debug/control interpretation of the camera path.
- Any colored guide logic if present; transform guide-like colors into subtle in-world ink, mineral-green stain, cinnabar node, or antique-gold crack only.

## Main AIGC Video Prompt

Create a 9-second 21:9 one-take cinematic image-to-video shot in brutal Chinese splashed-ink xieyi.

Use the uploaded start frame as the exact first frame. Lock the first-frame composition: extreme low macro camera skimming just above old rice paper, huge black throne-gear/crown-wheel cropped in the foreground, black ink bloodline canal leading forward, sparse mineral-green side stains, distant cinnabar nodes, old paper grain, brutal dry-brush ink.

Use the uploaded Blender motion reference video for camera movement, spatial continuity, parallax, map-node order, object rise timing, crane-up timing, and one-take continuity. Do not copy Blender preview materials literally.

Use the uploaded end frame only as a loose final-reveal reference. The final image should broadly arrive at a high oblique aerial reveal of a brutal ink dynasty power map under a black dragon eclipse, but do not force exact end-frame matching if it causes jitter, morphing, rubbery geometry, or unstable camera motion.

Camera and motion:
- No cuts. No scene jumps.
- Begin at a very low travelling macro angle beside the huge throne-gear.
- Glide forward along the black ink bloodline canal.
- Pass raised castle nodes, bridge ribs, crown gears, sea channels, mineral-green stains, cinnabar nodes, and dragon-bone arcs in a continuous route.
- Gradually crane upward during the final third.
- End in a broad high oblique aerial reveal of the activated map, with a huge black dry-brush dragon omen sweeping overhead like an ink eclipse.
- Keep camera motion smooth and deliberate. No random shake, no sudden zooms, no wobble, no unstable handheld movement.

Motion beats:
- 0.0-1.2s: exact start-frame lock. Old paper breathes; black canal pulls forward; foreground throne-gear is massive and close.
- 1.2-2.8s: camera glides along the canal. The foreground gear rotates slightly and falls behind. Black ink flows ahead through the route.
- 2.8-4.4s: pass the first raised castle and bridge-rib cluster. Castle blocks rise from paper as dry ink relief, not glossy metal.
- 4.4-6.0s: sea channels open as pale flying-white gaps. Mineral-green stains bleed through selected grooves and waterways.
- 6.0-7.6s: camera cranes upward while still travelling forward. Crown gears turn; dragon-bone arcs unfold along the path.
- 7.6-9.0s: high oblique aerial reveal. The full power map is visible. A vast black dry-brush dragon eclipse sweeps over the map and presses down. Settle without a hard stop or shake.

Visual style:
Brutal Chinese splashed-ink xieyi, old rice-paper ground, violent black dry-brush strokes, flying-white brush gaps, smoky gray wash, sparse mineral green, sparse cinnabar seal-like blocks with no readable characters, faint antique-gold cracks, controlled paper grain, severe negative space, cold imperial omen mood.

Character and expression:
No human characters or faces in this opening. Power is expressed through map mechanisms, castle nodes, crown gears, bloodline canals, and dragon shadow.

Audio:
Sound effects and ambience only. No music, no BGM, no soundtrack. Suggested sounds: dry brush scrape, paper fiber rumble, low gear grind, ink flow hiss, distant dragon breath, stone rising, soft seal-stamp thud at the final reveal, designed silence between mechanical beats.

Negative prompt:
No title text, no readable text, no readable map labels, no logo, no watermark, no actor likeness, no exact official costume, no official sigils, no photoreal metal, no glossy 3D title-copy look, no literal Game of Thrones title design, no shadow puppet, no cut-paper theatre, no leather puppet, no ornate card, no black-gold card, no soft scenic ink wash, no photoreal dragon flesh, no anime, no western fantasy realism, no hard cut, no scene jump, no random camera shake, no jitter, no wobble, no rubbery geometry, no melting gears, no unstable castle morphing, no thick visible camera path line, no debug arrows, no labels, no proxy geometry copied from Blender.

## Short Upload Prompt

Use start frame as exact first-frame lock. Use Blender video only for smooth one-take camera path, parallax, node-rise timing, and crane-up. Use end frame only as loose final-reveal reference, not a strict pixel match. Create a 9s 21:9 brutal Chinese splashed-ink opening: low macro camera starts beside a huge black throne-gear on old rice paper, glides along a black ink bloodline canal, passes rising castle nodes, bridge ribs, crown gears, mineral-green waterways and cinnabar nodes, then cranes up to a high oblique aerial power-map reveal under a vast black dry-brush dragon eclipse. No cuts, no jitter, no random shake, no rubbery geometry. Sound effects and ambience only; no music, no BGM, no soundtrack.
