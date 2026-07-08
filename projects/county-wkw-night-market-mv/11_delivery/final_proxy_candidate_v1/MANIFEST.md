# Final Proxy Candidate V1 Manifest

Project: `county-wkw-night-market-mv`  
Candidate date: 2026-07-08  
Candidate type: proxy-style final candidate, pending director acceptance

## Main Files

- Proxy candidate with scratch music: `../final_proxy_mv_v1/county_wkw_proxy_mv_v1_with_scratch_music.mp4`
- Ambience-only proxy candidate: `../final_proxy_mv_v1/county_wkw_proxy_mv_v1_ambience_only.mp4`
- Poster frame: `poster_frame_v1.png`
- Checksums: `checksums_sha256.csv`
- QA: `QA.md`
- Director decision note: `DIRECTOR_ACCEPTANCE_NOTE.md`

## Status

Ready for director review as a proxy-style final candidate.

This is not automatically the final external-AIGC MV. It becomes final only if the director explicitly accepts the proxy style as the delivery style. Otherwise, continue with external image-to-video replacement using `11_delivery/packages/external_i2v_upload_v1/county_wkw_external_i2v_upload_v1.zip`.

## Technical Summary

- Duration: about 74.73 seconds
- Resolution: 1920 x 824
- Frame rate: 24 fps
- Video codec: H.264 / yuv420p
- Audio codec: AAC LC, 44.1 kHz stereo

## Deliverable Logic

1. Review the proxy candidate.
2. If accepted, update `DIRECTOR_ACCEPTANCE_NOTE.md` and `10_qa/PROJECT_COMPLETION_AUDIT_V1.md`.
3. If not accepted, use the external I2V upload package and replace local proxy clips.
