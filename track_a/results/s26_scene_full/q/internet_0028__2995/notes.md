# Q2995 – length of the blue and grey bag (deuter backpack), prior: belt velocity 0.5 m/s

Object: the blue/grey backpack lying lengthwise along the motion (x), fully in view f0–~9.

## Pixel length
- f0: body x ≈ 510 → 3100 (≈2590–2600 px); f5: ≈ 860 → 3440 (≈2580 px). Strap tip adds ~200 px (not counted).
- Used L = 2590 px (±40).

## Pixel speed (speeds.py, NCC template tracking frame to frame, full res)
- backpack logo 70.5, hip-strap buckle 76, left strap 73.5 px/frame (f0–12; slowly decreasing).
- belt rubber panels at the same image height 60–68, upper-band plates ~50 px/frame (strong perspective).
- The bag rides the belt, so its own speed is the belt speed at the bag's depth: used 73 px/frame (mean of the bag points).

## Time base
File fps 20.53, question_fps 24. Used 24 (rate stated with the question = original footage). Both give plausible sizes
(0.74 m vs 0.87 m for a large hiking pack), so this is the main uncertainty.

## Result
scale = 0.5 m/s / (73 px/frame × 24 fps) = 2.854e-4 m/px → L = 2590 × 2.854e-4 = **0.74 m**.
Check: same ratio via edges by eye (both ends move ~68–70 px/frame f0→f5) gives 2590/69 → 0.78 m; buckle-only speed 76 → 0.71 m.
Alternatives: with fps 20.53 → 0.865 m; with belt-panel speed 64 px/frame → 0.84 m.
Confidence: moderate (fps choice and which belt reference the annotators used).
