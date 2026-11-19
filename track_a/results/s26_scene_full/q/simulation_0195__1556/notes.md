# q1556 — Jupiter model diameter

File fps = question_fps = 30 (no conversion issue). The depth_info names "big_europa" at 16.549 m. The scene has only two
objects, so this is read as the central big planet (Jupiter). The small moon is Callisto (13.004 m at frame 0, 13.856 m at frame 90).

## Method (orbit.py)
- Moon track: circle-fit centres from scene/tracks/moon.csv, smoothed with a quartic in frame (residual rms 0.08 px). Planet centre (941.26, 489.60) px,
  circle-fit diameter 282.66 px (bbox 284 px). The zoomed frame t=1.5 s (frames/planet.png) confirms the disc spans x 800–1083 and y 348–632.
- Model: the moon moves on a sphere of radius R around the planet origin. The planet sits at 16.549 m along its pixel ray. The principal point is the image centre.
  Two unknowns (f, R) were solved from the two given Callisto depths (frames 0 and 90): **f = 2668 px, R = 4.258 m**.
- Check against the prior: with this f, the per-frame speeds come out at 0.6275, 0.6266, 0.6269, 0.6265, 0.6255 m/s across the clip (mean 0.6268).
  That reproduces the prior of 0.627 m/s and shows it is uniform. This confirms f independently.
- Second route (solve.py): depth linearly interpolated, f chosen so the mean speed over frames 0–90 = 0.627 gives f = 2650 px (Jupiter 1.765 m).
  The orbit radius in that solution is nearly constant (4.27/4.20/4.27 m), which agrees.

## Answer
D = 282.66 × 16.549 / 2668 = 1.753 m. The exact sphere-projection correction (tan(asin(r/Z))) is −0.14 %, giving ≈1.751 m.
**Answer: 1.75 m.** Confidence: high (the routes agree within 1 %).
