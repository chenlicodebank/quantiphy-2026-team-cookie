# Q318: horizontal displacement of the apple during its parabolic motion (m)

2D side view, 30 fps (file and question rates are the same). Track: scene/tracks/apple.csv (I checked it; it follows the apple).
The apple rolls off the counter edge (x ≈ 578 px) at about frame 34 and lands on the floor between frames 47 and 48.

Method (fit.py):
- Fit a quadratic to the centroid y over the free-fall frames 37-47 (residual 0.17 px). It gives a = 6360 px/s²
  (6352-6369 across frame windows 36-47, 38-47 and 39-46; from the top edge, 6342-6355).
- Scale: 9.8 / 6360 = 1.541e-3 m/px.
- Horizontal speed is constant at 14.31 px/frame.
- The parabola's vertex (start of flight) is at frame 34.44, x = 575 px, which matches the counter edge at 578.
  The centre reaches floor height (y = 1525) at frame 47.88.
- Continuous horizontal displacement: 192.4 px = 0.2965 m.
- Discrete frame check: x(34) - x(48) = 581.65 - 381.07 = 200.6 px = 0.309 m.
- Answer: 0.30 m, between the two readings and within about 4 pct of each.

Sanity check: the apple's diameter is 62 px × 1.541e-3 = 0.096 m, a realistic apple. The fall height is
(1525 - 884) px × 1.541e-3 ≈ 0.99 m, consistent with a counter-height fall.

Confidence: high on the scale. The main uncertainty is where the flight starts and ends (about ±4 pct).
