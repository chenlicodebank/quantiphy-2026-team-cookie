# q3221 – ball velocity at 0.20 s (frame 6 at 30 fps; the file is also 30 fps)

- The camera looks straight down at a gym floor, and a basketball rolls horizontally across the view. The prior is
  gravity (9.8 m/s^2), but the clip shows no vertical or free-fall motion, so the prior gives no usable scale.
- **Scale:** taken from a standard object instead, a regulation basketball with a diameter of 0.24 m. Its pixel
  diameter is 258 px, the vertical (unblurred) extent and the median over frames 5–21 in scene/tracks. That gives
  0.24/258 = 0.000930 m/px.
- **Pixel speed near frame 6:** from the stabilised centroid track (`measure.py`).
  - backward difference 5→6: 94.4 px/frame
  - forward difference 6→7: 100.4 px/frame
  - quadratic fits over frames 4–10, 5–9, 5–12 and 5–21: 95.1–98.1 px/frame
  - adopted value: 97.5 px/frame = 2925 px/s
- **Velocity:** 2925 × 0.000930 = **2.72 m/s**. The forward difference alone gives 2.80 and the backward difference
  2.63.
- **Check (court lines):** the maroon lines are about 47 px wide. If they are standard 5.08 cm lines, the floor scale is
  1.08 mm/px. The ball's widest section is about 12 cm nearer the camera than the floor, so it is magnified by roughly
  1.1. On that scale the ball comes out at about 0.25 m, consistent with a 0.24 m ball.
- **Confidence:** moderate. The main uncertainty is the scale convention, because the gravity prior is unusable here.
