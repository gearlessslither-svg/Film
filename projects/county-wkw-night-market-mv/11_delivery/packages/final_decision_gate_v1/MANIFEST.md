# Final Decision Gate Package V1

Project: `county-wkw-night-market-mv`  
Archive: `county_wkw_final_decision_gate_v1.zip`

## Purpose

This package is a compact handoff for the final gate. It lets the director or a new Codex window choose the final path without searching across the whole project:

- accept proxy style as final;
- or return and assemble external image-to-video clips.

## Source Folder

`11_delivery/final_decision_gate_v1/`

## Proxy Finalizer

After explicit director acceptance, run:

```bash
python3 11_delivery/final_decision_gate_v1/finalize_proxy_acceptance.py --confirm-director-accepts-proxy-final --audio-choice with_scratch_music
```
