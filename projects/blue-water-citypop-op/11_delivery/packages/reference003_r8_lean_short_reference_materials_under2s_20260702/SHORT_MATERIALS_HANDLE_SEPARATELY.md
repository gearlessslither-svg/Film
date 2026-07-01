# Short Reference Materials, Handle Separately

This package contains source-independent reference clips shorter than 2 seconds.

Do not merge these shots with neighboring shots to satisfy a platform duration rule.

Each unit keeps two reference files:

1. `00_original_independent_reference_clip/`
   Original-duration independent clip, re-encoded as H.264/AAC for review.

2. `01_reference_clip_same_shot_hold_min2s_optional/`
   Optional upload workaround. This only holds the same shot's final frame to reach the 2-second floor. It does not splice adjacent shots.

Use the optional version only when a platform strictly rejects the original independent clip. Keep the prompt's original time range and shot intent.
