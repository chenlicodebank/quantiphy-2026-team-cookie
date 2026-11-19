# q3167: distance person–ball at 3.00 s

Time base: file fps = question_fps = 30, so t = 3.00 s is frame 90. The ball is in free flight there (released at frame 54, first bounce at frame 97).

Scale from the prior, g = 9.8 m/s²: I fitted a quadratic to the ball's bg-fixed y (scene/tracks/ball.csv) in `fitg.py`.
- Frames 54–96 (degraded frames 73–77 excluded): 1856 px/s², rms 1.8 px. Frames 55–95: 1855. Frames 60–90: 1857.
  Frames 58–95: 1847.
- Bounce arcs as a cross-check: 1889, 1840 and 1888 px/s².
- Scale used: 9.8 / 1856 = 0.00528 m/px. Across the windows it ranges from 0.0051 to 0.0054 (±3 %).

Positions at frame 90 (frame pixels; checked on frames/f90.png):
- Ball centre (1183, 557).
- Person bbox centre (598.5, 730.5), bbox 558–639 × 561–900. That is the pelvis/torso area.
- Distance: dx = 584.5, dy = 173.5, so 609.7 px. 609.7 × 0.00528 = **3.22 m**.

Sanity checks with the same scale:
- Person height 339 px gives 1.79 m (plausible).
- Rim outer width 90 px gives 0.475 m (a real rim is about 0.46 m).

Uncertainty: about ±3 % from the scale and a few px from the person's reference point. If the hip were used instead of the bbox centre (about 30 px lower), the distance would be about 618 px, or 3.26 m.
