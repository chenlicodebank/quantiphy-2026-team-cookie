# q_2106 – displacement of the airplane, 0 s → 2.00 s

Prior: airplane length = 40 m. Internet convention: one scale = 40 m / airplane pixel length.

## Time base
File fps 29.554, question_fps 25. Plane = B737-800 (winglets, gear down, approach; real length 39.5 m, matching the prior).
Its speed at the start is ~18.5 px/frame against the background, and 0.122 m/px gives 2.26 m/frame:
- at 29.55 fps: ~67 m/s (~130 kt), a typical 737-800 approach speed;
- at 25 fps: ~56 m/s (~110 kt), too slow for a 737 on approach.
So I use the file rate: t = 2.00 s → frame round(2 × 29.554) = 59.

## Measurements (measure.py, my own script; matches scene/tracks/airplane.csv)
- Frame 0: bbox x 1594–1921 → length 328 px (stabiliser tip to nose), centre (1757.5, 865.5).
- Frame 59: centre (2920.5, 858.5); background shift by phase correlation (−45.9, +25.4) px → compensated (2966.4, 833.1).
- Displacement against the background = 1209.3 px. Scale 40/328 = 0.1220 m/px → **147.5 m**.

## Checks and alternatives
- The scene record's bgcomp columns give 1208.5 px in x (same result).
- Raw image displacement without pan compensation is 1163 px → 141.8 m.
- The plane's pixel length grows 328 → 378 px over the window because it gets closer. Using the window's mean length
  (~353 px) gives ~137 m; using the frame-59 length gives 128 m. I use the frame-0 length, the most likely annotator choice.
- If question_fps 25 were used (frame 50): 1007 px → 122.8 m.

Confidence: moderate. The main risks are which frame rate and which frame's length the annotators used.
