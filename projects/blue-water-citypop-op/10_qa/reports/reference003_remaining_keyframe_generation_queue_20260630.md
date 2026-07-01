# Reference-003 Remaining Keyframe Generation Queue

- Created: `2026-06-30T06:44:08+08:00`
- Scope: 18 remaining official Reference-003 keyframes, Batch05 to Batch07.
- Status: ready for fresh-window generation queue. Do not generate in a WARN handoff window.

## Summary

- Queue items: 18
- Current official keyframes done: 24/42
- Current remaining prompt-ready: 18/42

## Operating Rules

- Use this queue only in a fresh Codex window/session; do not generate in the current WARN handoff window.
- Generate in queue_order, Batch05 then Batch06 then Batch07.
- For each item, use reference_frame as visual reference and generation_prompt_text as the prompt source.
- Save/copy the generated output to expected_output_path before applying status updates.
- After visual QA passes, run the post_generation_apply_command for that batch; never paste base64 or POST the whole board.

## Queue Table

| # | Batch | Item | Time | Unit | Reference | Prompt file | Output |
|---:|---|---|---:|---|---|---|---|
| 1 | 05 | `OP_SHOT_025` | 00:51.50 | `VU_REF003_012_GRANDIS_VEHICLE_ACTION` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_025_ref_005150.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/prompts/OP_SHOT_025_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_025.png` |
| 2 | 05 | `OP_SHOT_026` | 00:52.50 | `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_026_ref_005250.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/prompts/OP_SHOT_026_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_026.png` |
| 3 | 05 | `OP_SHOT_027` | 00:55.00 | `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_027_ref_005500.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/prompts/OP_SHOT_027_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_027.png` |
| 4 | 05 | `OP_SHOT_028` | 00:58.50 | `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_028_ref_005850.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/prompts/OP_SHOT_028_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_028.png` |
| 5 | 05 | `OP_SHOT_029` | 01:01.50 | `VU_REF003_014_NIGHT_CITY_BLUE_GRID` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_029_ref_010150.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/prompts/OP_SHOT_029_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_029.png` |
| 6 | 05 | `OP_SHOT_030` | 01:03.50 | `VU_REF003_014_NIGHT_CITY_BLUE_GRID` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_030_ref_010350.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/prompts/OP_SHOT_030_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_030.png` |
| 7 | 06 | `OP_SHOT_031` | 01:05.50 | `VU_REF003_015_NIGHT_AIRCRAFT_PASS` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_031_ref_010550.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/prompts/OP_SHOT_031_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_031.png` |
| 8 | 06 | `OP_SHOT_032` | 01:06.50 | `VU_REF003_016_NEMO_SUNSET_PROFILE` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_032_ref_010650.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/prompts/OP_SHOT_032_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_032.png` |
| 9 | 06 | `OP_SHOT_033` | 01:09.50 | `VU_REF003_016_NEMO_SUNSET_PROFILE` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_033_ref_010950.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/prompts/OP_SHOT_033_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_033.png` |
| 10 | 06 | `OP_SHOT_034` | 01:12.00 | `VU_REF003_017_NADIA_SOLEMN_CLOSE` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_034_ref_011200.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/prompts/OP_SHOT_034_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_034.png` |
| 11 | 06 | `OP_SHOT_035` | 01:13.50 | `VU_REF003_018_BLUE_WATER_SYMBOL` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_035_ref_011350.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/prompts/OP_SHOT_035_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_035.png` |
| 12 | 06 | `OP_SHOT_036` | 01:15.00 | `VU_REF003_018_BLUE_WATER_SYMBOL` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_036_ref_011500.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/prompts/OP_SHOT_036_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_036.png` |
| 13 | 07 | `OP_SHOT_037` | 01:16.50 | `VU_REF003_018_BLUE_WATER_SYMBOL` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_037_ref_011650.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/prompts/OP_SHOT_037_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_037.png` |
| 14 | 07 | `OP_SHOT_038` | 01:18.00 | `VU_REF003_019_WATER_SPLASH_TRANSITION` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_038_ref_011800.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/prompts/OP_SHOT_038_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_038.png` |
| 15 | 07 | `OP_SHOT_039` | 01:19.00 | `VU_REF003_019_WATER_SPLASH_TRANSITION` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_039_ref_011900.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/prompts/OP_SHOT_039_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_039.png` |
| 16 | 07 | `OP_SHOT_040` | 01:20.00 | `VU_REF003_020_FINAL_SKY_SAFE_HOLD` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_040_ref_012000.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/prompts/OP_SHOT_040_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_040.png` |
| 17 | 07 | `OP_SHOT_041` | 01:22.00 | `VU_REF003_020_FINAL_SKY_SAFE_HOLD` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_041_ref_012200.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/prompts/OP_SHOT_041_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_041.png` |
| 18 | 07 | `OP_SHOT_042` | 01:23.50 | `VU_REF003_021_BLACK_TAIL` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_042_ref_012350.jpg` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/prompts/OP_SHOT_042_generation_prompt.md` | `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_042.png` |

## Per-Item Prompt Text

### 01. `OP_SHOT_025` Batch05

- Timecode: `00:51.50`
- Unit: `VU_REF003_012_GRANDIS_VEHICLE_ACTION`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_025_ref_005150.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_025.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 05 --apply`

```text
# OP_SHOT_025 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_025
Reference: use BATCH05 OP_SHOT_025 reference frame for composition only.
Primary request: 21:9 live-action group lineup/tableau in bright daylight, matching 00:51.50 composition; main group together, no text overlay.
Subjects: Nadia 14-year-old age-safe in conservative red-orange/white outfit with Blue Water pendant; Jean 14-year-old inventor in blue cap/glasses/blue jacket/red bow tie; Marie child in modest dress; King friendly small lion cub with red scarf; Grandis adult red-haired woman in red period uniform; Sanson and Hanson adult companions.
Constraints: pure image only; no readable text, credits, lyrics, subtitles, logo, watermark, random symbols; minors age-appropriate and non-sexualized.
```

### 02. `OP_SHOT_026` Batch05

- Timecode: `00:52.50`
- Unit: `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_026_ref_005250.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_026.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 05 --apply`

```text
# OP_SHOT_026 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_026
Reference: use BATCH05 OP_SHOT_026 reference frame for composition only.
Primary request: deep blue underwater light shafts with Nautilus submarine silhouette entering, no credits.
Scene: vast underwater blue with surface light rays, cinematic scale.
Subject: retro-futurist Nautilus submarine silhouette, elegant and readable, no markings/text.
Constraints: pure image only; no readable text, credits, subtitles, logo, watermark, random symbols.
```

### 03. `OP_SHOT_027` Batch05

- Timecode: `00:55.00`
- Unit: `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_027_ref_005500.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_027.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 05 --apply`

```text
# OP_SHOT_027 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_027
Reference: use BATCH05 OP_SHOT_027 reference frame for composition only.
Primary request: Nautilus passes under shimmering surface light, large but graceful, clean underwater blue.
Scene: underwater light caustics and surface shimmer, rich blue depth.
Subject: large retro-futurist submarine crossing frame, readable silhouette, no markings/text.
Constraints: pure image only; no readable text, credits, subtitles, logo, watermark, random symbols.
```

### 04. `OP_SHOT_028` Batch05

- Timecode: `00:58.50`
- Unit: `VU_REF003_013_NAUTILUS_UNDERSEA_CREDITS`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_028_ref_005850.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_028.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 05 --apply`

```text
# OP_SHOT_028 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_028
Reference: use BATCH05 OP_SHOT_028 reference frame for composition only.
Primary request: submarine silhouette deepens into darker blue water with moving light bands, no text.
Scene: darker underwater blue, light rays fading into depth.
Subject: Nautilus shadow/silhouette receding, mysterious and graceful.
Constraints: pure image only; no readable text, credits, subtitles, logo, watermark, random symbols.
```

### 05. `OP_SHOT_029` Batch05

- Timecode: `01:01.50`
- Unit: `VU_REF003_014_NIGHT_CITY_BLUE_GRID`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_029_ref_010150.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_029.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 05 --apply`

```text
# OP_SHOT_029 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_029
Reference: use BATCH05 OP_SHOT_029 reference frame for composition only.
Primary request: dark night city reveal under hovering craft lights, blue tones and mysterious scale.
Scene: night city or industrial skyline, deep blue, small glowing craft lights overhead.
Composition: wide 21:9, city scale and darkness, no text.
Constraints: pure image only; no readable text, signs, logos, subtitles, credits, watermark, random symbols.
```

### 06. `OP_SHOT_030` Batch05

- Timecode: `01:03.50`
- Unit: `VU_REF003_014_NIGHT_CITY_BLUE_GRID`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/refs/OP_SHOT_030_ref_010350.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH05_READY/outputs/OP_SHOT_030.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 05 --apply`

```text
# OP_SHOT_030 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_030
Reference: use BATCH05 OP_SHOT_030 reference frame for composition only.
Primary request: glowing blue geometric grid or diagram across the ground with city lights beyond, no readable symbols.
Scene: night city, luminous blue ground pattern, mysterious technology.
Composition: wide 21:9, grid dominates foreground, city lights beyond.
Constraints: pure image only; no readable letters, numbers, symbols, signs, logos, subtitles, credits, watermark; abstract non-readable geometry only.
```

### 07. `OP_SHOT_031` Batch06

- Timecode: `01:05.50`
- Unit: `VU_REF003_015_NIGHT_AIRCRAFT_PASS`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_031_ref_010550.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_031.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 06 --apply`

```text
# OP_SHOT_031 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_031
Reference: use the OP_SHOT_031 reference frame for composition only; do not copy anime art or source text.
Primary request: 21:9 anamorphic live-action keyframe matching reference-003 at 01:05.50: night aircraft pass.
Scene/subject: Dark night sky/city atmosphere with a retro aircraft or craft passing through, small colored lights readable, mysterious blue-black tones.
Original frame description: Dark retro aircraft passes at night with small colored lights, no text.
Constraints: pure image only; no readable text, subtitles, lyrics, credits, title letters, logos, watermarks, random symbols, or direct anime screenshot copying. Preserve full reference-003 timing/composition function while replacing all source text with clean live-action remake imagery.
```

### 08. `OP_SHOT_032` Batch06

- Timecode: `01:06.50`
- Unit: `VU_REF003_016_NEMO_SUNSET_PROFILE`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_032_ref_010650.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_032.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 06 --apply`

```text
# OP_SHOT_032 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_032
Reference: use the OP_SHOT_032 reference frame for composition only; do not copy anime art or source text.
Primary request: 21:9 anamorphic live-action keyframe matching reference-003 at 01:06.50: Nemo profile start.
Scene/subject: Stern adult submarine captain Nemo in dark naval uniform and white cap, dignified profile against sunset sky, wind/coat silhouette clear, no text.
Original frame description: Stern adult submarine captain in dark uniform and white cap against sunset sky, no text.
Constraints: pure image only; no readable text, subtitles, lyrics, credits, title letters, logos, watermarks, random symbols, or direct anime screenshot copying. Preserve full reference-003 timing/composition function while replacing all source text with clean live-action remake imagery.
```

### 09. `OP_SHOT_033` Batch06

- Timecode: `01:09.50`
- Unit: `VU_REF003_016_NEMO_SUNSET_PROFILE`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_033_ref_010950.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_033.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 06 --apply`

```text
# OP_SHOT_033 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_033
Reference: use the OP_SHOT_033 reference frame for composition only; do not copy anime art or source text.
Primary request: 21:9 anamorphic live-action keyframe matching reference-003 at 01:09.50: Nemo profile hold.
Scene/subject: Stern adult submarine captain Nemo in dark naval uniform and white cap, dignified profile against sunset sky, wind/coat silhouette clear, no text.
Original frame description: Nemo holds a dignified profile at sunset, wind and coat shape clear.
Constraints: pure image only; no readable text, subtitles, lyrics, credits, title letters, logos, watermarks, random symbols, or direct anime screenshot copying. Preserve full reference-003 timing/composition function while replacing all source text with clean live-action remake imagery.
```

### 10. `OP_SHOT_034` Batch06

- Timecode: `01:12.00`
- Unit: `VU_REF003_017_NADIA_SOLEMN_CLOSE`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_034_ref_011200.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_034.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 06 --apply`

```text
# OP_SHOT_034 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_034
Reference: use the OP_SHOT_034 reference frame for composition only; do not copy anime art or source text.
Primary request: 21:9 anamorphic live-action keyframe matching reference-003 at 01:12.00: Nadia solemn front.
Scene/subject: Nadia, age-appropriate 14-year-old adventure girl with honey-tan complexion, short navy-black bob, gold earrings/bangles, conservative red-orange/white outfit and Blue Water pendant, solemn front close-up in cool symbolic light; non-sexualized.
Original frame description: Nadia C-version front close-up in cool symbolic light, serious and age-safe.
Constraints: pure image only; no readable text, subtitles, lyrics, credits, title letters, logos, watermarks, random symbols, or direct anime screenshot copying. Preserve full reference-003 timing/composition function while replacing all source text with clean live-action remake imagery.
```

### 11. `OP_SHOT_035` Batch06

- Timecode: `01:13.50`
- Unit: `VU_REF003_018_BLUE_WATER_SYMBOL`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_035_ref_011350.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_035.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 06 --apply`

```text
# OP_SHOT_035 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_035
Reference: use the OP_SHOT_035 reference frame for composition only; do not copy anime art or source text.
Primary request: 21:9 anamorphic live-action keyframe matching reference-003 at 01:13.50: Blue Water symbol.
Scene/subject: Blue Water sapphire jewel/symbol over a clean blue field, luminous and centered, abstract enough to avoid readable marks.
Original frame description: Blue Water jewel/sapphire symbol over clean blue field, no text or marks.
Constraints: pure image only; no readable text, subtitles, lyrics, credits, title letters, logos, watermarks, random symbols, or direct anime screenshot copying. Preserve full reference-003 timing/composition function while replacing all source text with clean live-action remake imagery.
```

### 12. `OP_SHOT_036` Batch06

- Timecode: `01:15.00`
- Unit: `VU_REF003_018_BLUE_WATER_SYMBOL`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/refs/OP_SHOT_036_ref_011500.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH06_READY/outputs/OP_SHOT_036.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 06 --apply`

```text
# OP_SHOT_036 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_036
Reference: use the OP_SHOT_036 reference frame for composition only; do not copy anime art or source text.
Primary request: 21:9 anamorphic live-action keyframe matching reference-003 at 01:15.00: blue symbol bloom.
Scene/subject: Cyan-blue bloom/energy texture with jewel feeling preserved, clean abstract light, replacing source text overlay.
Original frame description: Cyan-blue bloom or energy texture replaces original text overlay, jewel feeling preserved.
Constraints: pure image only; no readable text, subtitles, lyrics, credits, title letters, logos, watermarks, random symbols, or direct anime screenshot copying. Preserve full reference-003 timing/composition function while replacing all source text with clean live-action remake imagery.
```

### 13. `OP_SHOT_037` Batch07

- Timecode: `01:16.50`
- Unit: `VU_REF003_018_BLUE_WATER_SYMBOL`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_037_ref_011650.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_037.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 07 --apply`

```text
# OP_SHOT_037 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_037
Reference: use the OP_SHOT_037 reference frame for composition only; do not copy anime art or source text.
Primary request: 21:9 anamorphic live-action keyframe matching reference-003 at 01:16.50: underwater blue texture.
Scene/subject: Underwater blue texture and light pattern, text-free, mysterious jewel/sea mood.
Original frame description: Underwater blue texture and light pattern, clean and text-free.
Constraints: pure image only; no readable text, subtitles, lyrics, credits, title letters, logos, watermarks, random symbols, or direct anime screenshot copying. Preserve full reference-003 timing/composition function while replacing all source text with clean live-action remake imagery.
```

### 14. `OP_SHOT_038` Batch07

- Timecode: `01:18.00`
- Unit: `VU_REF003_019_WATER_SPLASH_TRANSITION`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_038_ref_011800.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_038.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 07 --apply`

```text
# OP_SHOT_038 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_038
Reference: use the OP_SHOT_038 reference frame for composition only; do not copy anime art or source text.
Primary request: 21:9 anamorphic live-action keyframe matching reference-003 at 01:18.00: water burst.
Scene/subject: Bright water or ice-like burst fills the wide frame with blue-white motion, no text.
Original frame description: Bright water/ice-like burst fills frame with blue-white motion, no text.
Constraints: pure image only; no readable text, subtitles, lyrics, credits, title letters, logos, watermarks, random symbols, or direct anime screenshot copying. Preserve full reference-003 timing/composition function while replacing all source text with clean live-action remake imagery.
```

### 15. `OP_SHOT_039` Batch07

- Timecode: `01:19.00`
- Unit: `VU_REF003_019_WATER_SPLASH_TRANSITION`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_039_ref_011900.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_039.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 07 --apply`

```text
# OP_SHOT_039 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_039
Reference: use the OP_SHOT_039 reference frame for composition only; do not copy anime art or source text.
Primary request: 21:9 anamorphic live-action keyframe matching reference-003 at 01:19.00: splash to sky.
Scene/subject: Water streaks clear into blue sky and white cloud fragments, transitional splash-to-sky composition, no text.
Original frame description: Water streaks clear into blue sky and white cloud fragments.
Constraints: pure image only; no readable text, subtitles, lyrics, credits, title letters, logos, watermarks, random symbols, or direct anime screenshot copying. Preserve full reference-003 timing/composition function while replacing all source text with clean live-action remake imagery.
```

### 16. `OP_SHOT_040` Batch07

- Timecode: `01:20.00`
- Unit: `VU_REF003_020_FINAL_SKY_SAFE_HOLD`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_040_ref_012000.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_040.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 07 --apply`

```text
# OP_SHOT_040 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_040
Reference: use the OP_SHOT_040 reference frame for composition only; do not copy anime art or source text.
Primary request: 21:9 anamorphic live-action keyframe matching reference-003 at 01:20.00: final sky safe.
Scene/subject: Clean final blue sky card with soft cloud and open negative space, replacing the broadcaster end card with no text/logo.
Original frame description: Clean final blue sky card with soft cloud and no text, replacing the broadcaster end card.
Constraints: pure image only; no readable text, subtitles, lyrics, credits, title letters, logos, watermarks, random symbols, or direct anime screenshot copying. Preserve full reference-003 timing/composition function while replacing all source text with clean live-action remake imagery.
```

### 17. `OP_SHOT_041` Batch07

- Timecode: `01:22.00`
- Unit: `VU_REF003_020_FINAL_SKY_SAFE_HOLD`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_041_ref_012200.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_041.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 07 --apply`

```text
# OP_SHOT_041 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_041
Reference: use the OP_SHOT_041 reference frame for composition only; do not copy anime art or source text.
Primary request: 21:9 anamorphic live-action keyframe matching reference-003 at 01:22.00: final sun hold.
Scene/subject: Blue sky with bright sun glow and clear negative space, final hold, no logo or text.
Original frame description: Blue sky with bright sun glow and clear negative space, no logo or text.
Constraints: pure image only; no readable text, subtitles, lyrics, credits, title letters, logos, watermarks, random symbols, or direct anime screenshot copying. Preserve full reference-003 timing/composition function while replacing all source text with clean live-action remake imagery.
```

### 18. `OP_SHOT_042` Batch07

- Timecode: `01:23.50`
- Unit: `VU_REF003_021_BLACK_TAIL`
- Reference frame: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/refs/OP_SHOT_042_ref_012350.jpg`
- Expected output: `08_generation/jobs/REFERENCE003_OFFICIAL_KEYFRAMES_QA_20260630_BATCH07_READY/outputs/OP_SHOT_042.png`
- Apply command after QA: `python3 00_admin/ai_bridge/packets/apply_reference003_batch05_07_keyframes.py --batch 07 --apply`

```text
# OP_SHOT_042 generation prompt

Use case: photorealistic-natural
Asset type: official keyframe for REFERENCE003 full OP remake, OP_SHOT_042
Reference: use the OP_SHOT_042 reference frame for composition only; do not copy anime art or source text.
Primary request: 21:9 anamorphic live-action keyframe matching reference-003 at 01:23.50: black tail.
Scene/subject: Clean black tail frame after final sky hold, very dark and textureless, no text.
Original frame description: Clean black tail frame after the final sky hold.
Constraints: pure image only; no readable text, subtitles, lyrics, credits, title letters, logos, watermarks, random symbols, or direct anime screenshot copying. Preserve full reference-003 timing/composition function while replacing all source text with clean live-action remake imagery.
```
