# Reference-003 Frame Boundary Refine R6

- Source: `01_intake/references/reference-003-full-op-2160p.mp4`
- FPS scan: 23.976; frames: 2024
- Opening sheet: `01_intake/analysis/reference003_frame_boundary_refine_r6_20260701/opening_00_25_4fps_contact_sheet.jpg`
- Boundary triplets: `01_intake/analysis/reference003_frame_boundary_refine_r6_20260701/top_boundary_candidate_triplets.jpg`
- Flash triplets: `01_intake/analysis/reference003_frame_boundary_refine_r6_20260701/single_frame_flash_candidate_triplets.jpg`
- PySceneDetect scene list: `01_intake/analysis/reference003_frame_boundary_refine_r6_20260701/pyscenedetect/reference-003-full-op-2160p-Scenes.csv`

## Opening 0-25s Candidate Boundaries

| time | frame | score | kind |
|---:|---:|---:|---|
| 00:00.67 | 16 | 0.81266 | hard_boundary_candidate |
| 00:14.72 | 353 | 0.49533 | hard_boundary_candidate |
| 00:23.44 | 562 | 0.34794 | hard_boundary_candidate |
| 00:23.90 | 573 | 0.44837 | hard_boundary_candidate |

## PySceneDetect Cross-Check

PySceneDetect `detect-content --threshold 18` detected 28 scenes. The opening cross-check boundaries are:

- `00:00:00.667`
- `00:00:01.376`
- `00:00:02.544`
- `00:00:14.723`
- `00:00:16.266`
- `00:00:23.440`
- `00:00:25.901`

This agrees with the R6 frame-diff scan on the important opening beats: aircraft flash around `00:14.72`, aircraft/sky transition around `00:16.27`, and sun/Nadia transition around `00:23.44-00:25.90`.

## Packaging Decision

The opening is repacked as three long AIGC units: 00:00-00:07, 00:07-00:16.50, and 00:16.50-00:24.80. These are generation chunks, not a claim that the reference has hard cuts at those exact times.

## Precision Upgrade

- Previous 2fps sampling can miss 1-3 frame inserts.
- R6 scans every source frame at ~23.976fps and flags hard-boundary and single-frame flash candidates.
- PySceneDetect is now installed in the project venv at `00_admin/.venv_vision/` and should be used as a cross-check, not as the sole director.
- Candidate boundaries still require director/semantic review before becoming promoted image assets.
