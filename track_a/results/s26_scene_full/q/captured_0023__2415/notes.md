# q_2415: displacement of the book between 1.0 s and 1.6 s (cm)

- question_fps = file fps = 24. t=1.0 -> frame 24 (sliding on ramp), t=1.6 -> frame 38 (at rest on table).
- Centres from scene/tracks/book.csv (checked on frames/f24.png, frames/f38.png): f24 (590.3, 383.1), f38 (562.5, 495.3).
- f = 0.5959*1280 = 762.8 px, principal point (640, 360). Depth = Euclidean distance along the ray.
- Depth at f38 given (0.851 m). Depth at f24 not given, estimated three ways:
  1. Book long-axis pixel length: L from given depths = 0.197/0.184/0.192 m (mean 0.191) -> d24 = 1.131 m.
  2. Ramp 3D line from slope far 1.201 m (top edge y 356) / near 0.9555 m (bottom y 482); the point projecting to
     row 383 -> 1.135 m (check: the same line gives 1.030 at f29 vs the given 1.02).
  3. Line through the f29 book centre (given 1.02 m) parallel to the ramp -> 1.124 m.
- Displacements: 31.5 / 31.9 / 30.9 cm; mean depth 1.130 -> 31.5 cm (z-depth convention gives 30.3).
- Answer 31.5 cm. Confidence: moderate-good (±5%); the main uncertainty is the depth at 1.0 s.
- The prior (acceleration 2.8 m/s^2 at 1.4 s) was not needed.
