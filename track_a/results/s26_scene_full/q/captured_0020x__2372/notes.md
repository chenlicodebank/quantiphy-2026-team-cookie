# q_2372: displacement of the yellow toy from 0.60 s to 0.80 s (cm)

- Frames: question_fps = file fps = 24, so the interval is f14 (round 14.4) to f19 (round 19.2).
- Yellow toy = the pale-yellow mango/carrot-like toy the far person throws (scene/ "yellow_fruit"). The depth entry
  "carrot 2.63 m at 0.60 s" fits it: it was just released near the far person (3.237 m). The "jar" (1.9735 m) is
  the white object the near person throws.
- Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).
- Depth is given only at f14, so the f19 depth comes from physics. I fit a 3D projectile with |g| = 9.8 m/s^2 (the
  prior), with its direction in camera coordinates left free, to the tracked centroids (scene/ tracks; spot-checked
  on crops in frames/crops.png). The toy's start point is anchored at the f14 back-projection with depth 2.63 m.
  The white jar's trajectory is fitted at the same time (same g; start point anchored at f14 depth 1.9735 m) to
  constrain the direction of g. Script: fit.py, variants in check.py.
  - Joint fit: rms 1.5 px, camera tilted 57.5 deg down. Toy depth 2.63 -> 2.035 m. Displacement **68.0 cm**.
  - Joint fit with the jar's start point free: rms 1.26 px, tilt 59.4 deg. Displacement **70.3 cm**.
  - Toy-only fit: rms 1.0 px, tilt 61.9 deg. Displacement **74.1 cm**. Least constrained of the three.
- Check: from the far person's pelvis (~(707, 95), 3.237 m), I dropped 0.95 m along the fitted g direction and
  projected. This lands at y ≈ 251 for tilt 57.5 and y ≈ 240 for tilt 61.9; the feet are at y ≈ 255-270. That
  favours the smaller tilt of the joint fits.
- An apparent-size route was not usable: the toy tumbles, and its visible width/length changes with orientation.
- f19 is partly overlapped by the white jar, so its centroid has a ~2 px residual (under 1 cm).
- Answer: 69 cm, between the two joint fits. Confidence: moderate, about ±7%.
