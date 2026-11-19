# q_2775 — yoga ball displacement 1.0 s → 1.5 s

The question rate and the file rate are both 24 fps, so t = 1.0 s is frame 24 and t = 1.5 s is frame 36.
depth_info: the yoga ball is at 2.4985 m at t = 1.0 s. The t = 1.5 s entry reads "soccer_ball", but the only ball in the clip is the yoga ball, so I took 1.4972 m as the yoga ball's distance (this is a label slip in the question). The apparent-size check below confirms it.

## Method (lab card)
- I used f = 0.5959 × 1280 = 762.8 px with the principal point at (640, 360).
- Ball centres come from scene/tracks/ball.csv (circle fit). I checked them against gridded frames 24 and 36 (frames/f24.png, frames/f36.png):
  - f24: (523.0, 544.2), diameter 155 px.
  - f36: (360.9, 668.8). The bottom of the ball is cut off at y ≈ 711; the fixed-radius fit gives (361.9, 675.5).
- Each centre is back-projected along its unit ray × the given Euclidean distance.
  - P24 = (-0.368, 0.580, 2.402) m.
  - P36 = (-0.481, 0.532, 1.314) m.
- **Displacement = 1.095 m.** The fixed-radius centres give 1.096 m.

## Checks
- **Depth from apparent size.** Taking depth ∝ 1/diameter (diam_trend), calibrated at f24, predicts 1.487 m at f36. The given value is 1.497 m, so the two agree within 0.7%. The implied ball diameter is about 0.50 m.
- **Prior.** On the same depth model, a linear fit of the 3D centre over frames 21–27 gives a velocity at 1.0 s of 2.144 m/s. The prior is 2.1464 m/s, so the geometry is consistent.
- **Second route.** The per-frame speeds are steady at about 2.1–2.3 m/s, and the path length from f24 to f36 is 1.11 m. The motion is almost straight, so this is consistent with the 1.095 m net displacement.

Confidence: high. The error is about ±3%, mostly from where the centre of the cut-off ball sits at f36.
