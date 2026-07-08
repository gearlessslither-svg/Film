# External I2V Upload Package V1

Project: `county-wkw-night-market-mv`  
Package date: 2026-07-08  
Package type: upload packet for external image-to-video tools  
Archive: `county_wkw_external_i2v_upload_v1.zip`

## Purpose

Prepare the final missing external-AIGC step as 14 clear upload units. Each unit contains:

- source keyframe image;
- bilingual image-to-video prompt;
- hard audio rule;
- expected returned clip filename.

## Hard Rule

Each external clip must be generated with ambience / sound effects only. No music, no BGM, no soundtrack. Final music is added later in editing.

## Upload Units

Upload folders live in `units/`.

Expected returned clips should be saved to:

`09_edit/external_clips/external_i2v_clips_v1/`

Then run:

```bash
python3 09_edit/tools/assemble_external_mv_v1.py --check-only
python3 09_edit/tools/assemble_external_mv_v1.py
```

## Tracking

- CSV tracker: `external_i2v_tracker.csv`
- JSON tracker: `external_i2v_tracker.json`

## Status

Ready for external upload. No external clips have been returned yet.
