# Reference-003 Video Unit QA Checklist

Use this after the remaining keyframes are generated and before assembling the full OP.

## Required Gates

- [ ] All 42 `OP_SHOT_*` rows are `generated_reference003_qa_pass`.
- [ ] No official unit uses superseded reference-002 images, old remake-v3 placeholders, readable titles, NHK marks, credits, lyrics, subtitles, or watermarks.
- [ ] Each generated segment uses the matching `VU_REF003_*` unit prompt and QA-passed keyframes from `manifest.json`.
- [ ] Timing and motion function match `reference-003-full-op-2160p` for the unit time range.
- [ ] Incoming, outgoing, and intra-unit transition edges are preserved.
- [ ] Nadia and all minor characters remain age-appropriate, modestly clothed, and non-sexualized.
- [ ] Pure sky, water, black-tail, and symbol shots remain clean and do not invent text-like marks.
- [ ] Each segment MP4 decodes fully before roughcut assembly.

## Full Roughcut Gates

- [ ] 21 segments are assembled in `video_units.json` order.
- [ ] Final roughcut duration is close to 84.437333 seconds, allowing only deliberate editorial tolerance.
- [ ] Full roughcut MP4 complete-decodes with no corrupt frames.
- [ ] Final QA compares against the reference-003 2fps contact sheet and section contact sheets.
- [ ] Handoff and validation reports are refreshed after review.
