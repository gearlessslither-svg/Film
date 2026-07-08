# Director Acceptance Note

Project: `county-wkw-night-market-mv`  
Candidate: `11_delivery/final_proxy_mv_v1/county_wkw_proxy_mv_v1_with_scratch_music.mp4`

## Current Decision

Status: pending.

The proxy-style candidate is ready for review, but it has not been explicitly accepted as the final delivery.

## Acceptance Options

### Option A - Accept Proxy Style As Final

Use this only if the director explicitly accepts local pan/zoom proxy motion as the final visual style for this MV.

If accepted, update:

- `10_qa/PROJECT_COMPLETION_AUDIT_V1.md`
- `00_admin/handoff/HANDOFF_LATEST.md`

and mark the final delivery path as proxy-style final.

### Option B - Continue External I2V

Use this if the director wants true image-to-video motion.

Next steps:

1. Upload `11_delivery/packages/external_i2v_upload_v1/county_wkw_external_i2v_upload_v1.zip`.
2. Save returned files to `09_edit/external_clips/external_i2v_clips_v1/`.
3. Run `python3 09_edit/tools/assemble_external_mv_v1.py --check-only`.
4. Run `python3 09_edit/tools/assemble_external_mv_v1.py`.
