# Q20: length of the orange car (m)

The scene is 2D: a top-down static camera and a road plane facing it, at 30 fps (the file fps and question_fps agree).
The prior is the orange car's acceleration, −2.86 m/s².

## Scale from the prior (fit.py)
- The orange car's track in scene/tracks/orange_car.csv (template-matched centre, reliable frames only) fits a quadratic y(f):
  - f50–90: a = −0.3441 px/frame² (rms 0.15 px)
  - f25–90: −0.3486
  - f30–80: −0.3496
- Check from the per-frame displacements: 25.72 px at f50 and 11.80 px at f90 give 0.348 px/frame². 33.58 px at f26 to 11.80 px at f90 gives 0.340.
- Adopted value: a = 0.345 ± 0.004 px/frame² = 310.5 px/s².
- Scale = 2.86 / 310.5 = 0.00921 m/px.

## Pixel length (length2.py, length.py)
Frames 48–64 sit near the image centre, where perspective and motion blur are smallest.
- Difference mask against the empty-road frame 0 (threshold 60): 552–556 px. Centre column: 551–556 px.
- Orange paint only: 537–540 px. This misses the dark bumper trim, so it underestimates the length.
- Record bbox: about 556 px.
- Adopted length: 550 ± 6 px.

## Answer
550 px × 0.00921 m/px = **5.06 m**. Across the acceleration fits (0.340–0.350 px/frame²) the result runs from 5.0 to 5.15 m.
The width is about 205 px across the body (about 1.9 m), so the proportions are plausible.
Confidence: good, roughly ±3 %.
