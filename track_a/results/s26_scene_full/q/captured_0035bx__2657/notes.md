# q_2657 — soccer ball velocity at t = 0.9 s (cm/s)

- t = 0.9 s → frame round(0.9·24) = 22 (file fps = question fps = 24). Soccer ball rolls freely in frames 14–24;
  it hits the basketball around frames 24–26, so the smoothing window stops at frame 24.
- Camera: f = 0.5959·1280 = 762.8 px, principal point (640, 360).
- depth_info lists "soccer" twice at 1.4 s. I took 2.602 m as the soccer ball (it moves away from the camera) and
  2.373 m as the basketball (it approaches). This is confirmed below.
- Centres: the `circle_cx/cy` columns from scene/tracks (I checked frame 22 on a 2x crop; the fit is good).
- Method (measure.py): I back-projected the 4 depth anchors (soccer f22 and f34, basketball f22 and f34) to 3D. Both
  ball centres sit about 11–11.6 cm above the floor, so they lie on one plane parallel to it. Fitting a plane to the
  4 points leaves residuals ≤ 3.4 mm, which confirms the labelling. Every soccer frame was then placed in 3D as the
  intersection of its pixel ray with that plane. At frame 22 this gives a distance of 2.4726 m, against 2.477 m given.
- Checks: basketball diameter from bbox × depth / f is 24.9 / 21.3 cm, against the 23.2 cm prior (the bbox has a
  ~2 px halo). Soccer ball diameter comes out at 20–22 cm, which is plausible.
- Velocity: a linear fit of the 3D centres around frame 22 (smoothed over at least 5 frames) gives
  18–24: 123.2, 19–24: 120.8, 20–24: 122.1, 17–23: 125.6, 18–23: 124.7 cm/s.
  The raw one-frame steps are noisy (107–144).
- Second route: taking depth from the apparent bbox size (scaled to 2.477 m at f22) instead of the plane gives
  125.9 cm/s. Taking constant depth (lateral motion only) gives 101 cm/s, a lower bound because it ignores the
  receding motion.
- Answer: **123 cm/s**. Confidence: moderate-high (±5 %).
