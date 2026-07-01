# Unit Method Recommendations - reference-002-opening

Updated: 2026-06-30 02:38 Asia/Shanghai

This table applies the three-layer remake strategy to the current reference opening.

## Principle

Start cheap and local:

1. Build a frame-stack roughcut from stills to test rhythm.
2. Use AIGC video only for units where motion smoothness matters.
3. Use Blender/previs first when spatial continuity or camera/object relations are risky.

## Reference 002 Opening

| Time | Content | First-pass method | Upgrade path | Reason |
|---:|---|---|---|---|
| 00.0-04.5 | White bird over blue sky | image keyframes + frame-stack roughcut | AIGC video for wingbeats and smooth glide | Simple sky/bird motion; no aircraft scale problem yet. |
| 05.0-08.0 | Bird with credit/title overlay in reference | no-text title-safe keyframes + roughcut | AIGC video only for subtle drift | We must not reproduce readable text/logo; timing and negative space matter most. |
| 08.5-12.0 | Cloud bank expands/fills frame | keyframes + AIGC video | Blender only if camera path becomes important | Cloud evolution needs smooth motion, but spatial geometry is low risk. |
| 12.5-14.0 | Brief flying machine/aircraft reveal | Blender/simple previs + keyframes | AIGC video after scale/axis is locked | Aircraft relation and scale need proof; duration should remain short. |
| 14.5-19.5 | Main title/logo card in reference | no-text title-safe frame-stack roughcut | AIGC video for sky drift if needed | This is mainly timing/hold. Pure output must be clean no-text composition. |
| 20.0-21.0 | Sun/light flare transition | keyframes + AIGC video | compositing/Blender light pass optional | Flare needs smooth bloom; can be handled by video model or compositing. |
| 21.5-23.0 | Heroine close-up begins | keyframes + AIGC video | no Blender unless camera path changes | Character performance motion matters more than 3D space. |

## Current Roughcut

- Frame-stack roughcut: `roughcuts/reference-002-opening_frame_stack_2fps.mp4`
- Purpose: local timing/composition review, not final output.

## Important Warning

The previous `opening_24s_onetake_previs.mp4` should not be used as the accepted remake timing. It is too continuous and gives the aircraft too much screen importance compared with the reference.
