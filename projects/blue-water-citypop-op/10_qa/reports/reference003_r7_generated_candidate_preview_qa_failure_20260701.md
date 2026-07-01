# Reference-003 R7 Generated Candidate Preview QA Failure

- Created: 2026-07-01
- Status: `quarantined_do_not_use_for_production`
- Affected MP4: `09_edit/rough_cut/reference003_r7_generated_candidate_animatic_1080p_with_music_20260701.mp4`
- Affected production index: `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_PROMPT_INDEX/AIGC_VIDEO_PRODUCTION_PACKAGE_INDEX.md`

## Director Reported Issues

1. Timeline/frame placement is wrong in places. Example: Nadia entrance feels early and is interrupted by opening blue-sky/cloud imagery.
2. Faces flicker or mutate, likely worsened by excessive inserted generated frames.
3. Mid/late sections drift into a different hyper-real style, indicating a workflow-level consistency failure.

## Confirmed Root Cause

The R7 generated-candidate preview script promoted every generated candidate frame into the animatic timeline:

- 42 official keyframes
- 21 R5 adaptive generated images
- 98 R7 generated candidate images
- total: 161 still frames

That behavior is invalid for production QA. R7 candidates were not all director-approved story anchors. Many were boundary, middle, or reference-video audit candidates. The script only checked file existence and decode success, then labeled the preview `decode_ok`. It did not check:

- whether a generated candidate should enter the final timeline
- whether near-duplicate boundary frames create face flicker
- whether character identity stays stable across adjacent frames
- whether style remains consistent across official/R5/R7 sources
- whether a frame's composition still serves the original shot function

## Visual Evidence

- Nadia/problem window contact sheet: `10_qa/reports/r7_preview_audit_nadia_23_29.jpg`
- Late-style/problem window contact sheet: `10_qa/reports/r7_preview_audit_late_129_161.jpg`

Nadia segment evidence shows dense frame insertion around `23.00s-29.46s`, including multiple 0.06s boundary frames and bridge frames. This makes the sequence jump among sky, Nadia closeups, and Jean bridge frames instead of preserving the intended shot rhythm.

Late segment evidence shows official/R5/R7 frames mixed with visibly different lighting, lens treatment, and realism level. The Blue Water and sky/water transition sequence especially demonstrates style discontinuity.

## Invalidated Assumptions

- `decode_ok` is not a QA pass.
- `all_generated_assets_ready` is not a director approval state.
- R7 generated candidate images are not automatically final timeline anchors.
- More frames do not mean a better video handoff; over-dense still anchors can make external video generation less stable.
- A production prompt pack must not include every generated candidate as a required upload input unless the candidate has passed visual and timeline QA.

## Immediate Production Hold

Do not use the current production-ready prompt pack for external AIGC video generation:

- `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_PROMPT_INDEX/PRODUCTION_READY_PROMPT_ONLY/`
- `08_generation/jobs/REFERENCE003_R7_HIGH_PRECISION_VIDEO_UNITS_20260701/_PROMPT_INDEX/AIGC_VIDEO_PRODUCTION_PACKAGE_INDEX.md`

These files currently include all 98 R7 candidates as image inputs. They should be treated as a material inventory, not as an approved production package.

## Recovery Plan

1. Revert to the last stable baseline for timing and style:
   - official 42 keyframes
   - R5 21 generated assets that already passed the earlier expanded-preview stage
2. Re-audit R7 generated candidates as a pool, not as mandatory anchors.
3. Add explicit candidate statuses:
   - `approved_timeline_anchor`
   - `reference_only`
   - `reject_identity`
   - `reject_style`
   - `reject_timing`
4. Build a lean R8 preview using only approved anchors:
   - cap normal units at 2-3 image anchors unless a flash/transition truly needs more
   - exclude 0.06s boundary frames unless they are a real intentional cut
   - preserve original reference-video timing as the master timeline
5. Add QA gates before any file can be called production-ready:
   - timeline alignment check
   - adjacent-frame identity/style check
   - per-unit contact sheet review
   - full animatic director review
6. Only after the lean preview passes, regenerate the per-unit AIGC video production prompt pack.
