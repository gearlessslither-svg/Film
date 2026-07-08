# Hardlocks V1 QA

Project: `county-wkw-night-market-mv`  
QA date: 2026-07-08  
Batch: `08_generation/jobs/hardlocks_v1/`  
Contact sheet: `hardlocks_v1_contact_sheet.png`

## Summary

Status: pass as V1 candidate locks.

The batch generated four candidate lock sheets for boy, girl, motorcycle, and two-character distance/reflection grammar. These are good enough to support a small `keyframes_v1` test batch, but they should remain `candidate` until the director confirms the faces and styling.

## File Check

- Expected images: 4
- Actual images: 4
- Missing outputs: none

## Visual Checks

| Item | Result | Notes |
|---|---|---|
| HL001 | pass | Boy reads as early-20s county-town motorcycle youth; dark wet jacket and quiet expression are stable. |
| HL002 | conditional pass | Girl reads as adult and grounded; styling is acceptable, but if the director wants less leg/shorts, regenerate with trousers or longer skirt. |
| HL003 | pass | Motorcycle reads as ordinary used local bike, not luxury or sci-fi. |
| HL004 | pass | Relationship grammar works: separated by rain curtain, mirror, wet market ground, and field-road distance. |

## Use Notes

- Use `HL001`, `HL002`, and `HL003` as candidate references for the first `keyframes_v1` test.
- Keep `HL004` as a composition/relationship reference, not a strict face lock.
- Do not use these as final official locks if the director rejects the character faces.
