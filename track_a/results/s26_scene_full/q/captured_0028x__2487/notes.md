# Q2487: ping pong ball velocity at t = 1.3 s (cm/s)

- The file and the question are both 24 fps. t = 1.3 s is frame round(31.2) = 31, which is just before the
  first post-bounce apex (the pixel apex is about frame 32.1). depth_info calls t = 1.3 "max height".
- Lab camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- I re-measured the ball centroid in frames 20–44 with an intensity-weighted centroid and a subpixel width
  (`measure.py`). The values match scene/tracks/ball.csv to within about 1–2 px.
- Depth: the given distances are f26 = 1.557 m and f31 = 1.4115 m. Their ratio means the distance shrinks about 2.0 % per frame.
  The apparent ball width alone gives 1.8 % per frame over frames 27–35. That is an independent check that the ball moves
  toward the camera at roughly 0.6–0.7 m/s, and this depth motion makes up most of the speed. (The f24 value of 1.805 m
  is not consistent with the size trend; it lies before the bounce, so I did not use it.)
- 3D positions = unit ray x distance. Velocity at frame 31 (`velocity.py`), with depth taken linearly through the given values:
  - forward difference 31→32: 71.9 cm/s; 5-frame smoothed forward difference: 71.7
  - central or regression slope over frames 29–33: 76.5–77.1 (more vertical component)
  - Depth from the size trend instead of the given values: 63–69 cm/s.
- Components: about 71 cm/s toward the camera, about 10–27 cm/s vertical (still rising slightly), and about 2 cm/s horizontal.
- Answer: **73 cm/s**. It follows the reference convention (forward difference with smoothing, given depths) and sits between
  the forward and central estimates. Confidence: moderate, about ±8 %. The main uncertainty is the depth rate, which
  depends on depth values we only have at two frames near the question time.
