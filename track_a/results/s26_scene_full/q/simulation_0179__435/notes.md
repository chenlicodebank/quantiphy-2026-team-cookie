# Q435 — trolley speed at t = 2 s (frame 48, 24 fps; file fps = question fps)

Prior: trolley (shopping cart) acceleration = 1.507 m/s^2 (2D video, horizontal motion at constant depth).

Method (fit.py): quadratic fit x(t) to the scene record's per-frame cart position (tracks/shopping_cart.csv),
which covers the cart in every frame 0-59 with no occlusion or bounce. The fit gives the pixel acceleration, so
the scale is 1.507 / a_px m/px. Speed at frame 48 = one-frame backward difference of the fitted x, times 24 fps, times the scale.

- bbox_cx: a_px = 296.1 px/s^2, rms residual 0.5 px, start time t0 ≈ -0.017 s (from rest at about frame 0). v48 = 591.0 px/s, which gives **3.008 m/s**
- wheels_cx: 3.004 m/s; fits starting from frame 5 or 10: 3.009-3.018 m/s
- bbox x0 and x1 edges: 3.04 and 2.98 m/s (the apparent length grows slightly, which biases the edges in opposite directions)

Second-route check: constant acceleration from rest gives v = a·t = 1.507 × 2 = 3.014 m/s, and the
backward-difference midpoint gives 1.507 × 47.5/24 = 2.983 m/s. All routes give 2.98–3.02 m/s.

Answer: 3.01 m/s. Confidence: high (within about 1 %).
