# Q901 — width (long side) of the AC, simulation_0259

The file rate and question_fps are both 30. I treated the scene as 2D: one metres-per-pixel scale, taken from the prior that the red cup falls at 9.8 m/s² before 0.5 s.

## Scale (measure.py)
- I fitted a quadratic to the cup's vertical position over the free-fall frames 0–14. I used the frame column from scene/tracks/cup.csv, which matches my own checks: the cup is released at frame 0 and hits the table at frame 15.
- Acceleration from the lid top edge (the cleanest point): 6322–6330 px/s², which gives 1.549e-3 m/px.
- Acceleration from the bbox centre or centroid: 6255–6310 px/s², which gives 1.553–1.567e-3 m/px.
- From the bottom edge: 1.558–1.586e-3 m/px. This edge is affected by the underside ellipse seen in perspective.
- I adopted 1.556e-3 m/px ±0.6%.

## AC width (edges.py)
- I took horizontal intensity gradients on frame 0 for rows y = 770–1050. The left edge of the unit is at x≈132 and the right edge at x≈638 in nearly every row, so the width is 506 px.
- Width = 506 × 1.556e-3 = **0.787 m**. Across the different scale choices the range is 0.784–0.794 m.

## Checks
- The cup comes out about 6.6 cm wide (42 px) and 10 cm tall (65 px), which is plausible for a small paper cup.
- An LG outdoor AC unit is typically about 0.77–0.87 m wide, so 0.79 m is realistic. The prior is realistic and the resulting scale is consistent.
- Caveat: the AC stands in front of the table, so it may be slightly closer to the camera than the plane the cup falls in. Under the 2D single-scale convention this is ignored.

Confidence: good, within about 3%.
