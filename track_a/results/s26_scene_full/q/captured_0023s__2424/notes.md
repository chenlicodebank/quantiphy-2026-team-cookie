# q_2424 — displacement of the book between 1.0 s and 1.6 s (cm)

File fps = question_fps = 24 -> t=1.0 s is frame 24, t=1.6 s is frame 38.
Camera: f = 0.5959*1280 = 762.8 px, principal point (640,360).

Book centre (scene/tracks/book.csv ref point, bbox centre): f24 (589.5, 383.5) (sliding on the ramp, slight
vertical blur), f38 (564.5, 496.5) (at rest on the table since f37).
Depth at f38: given 0.851 m (t=1.6). Depth at f24 is NOT given, so it was estimated:

- Route A (apparent size, depth ~ 1/horizontal length of the book, which is across the motion): length 128 px at f24;
  K = depth*length = 0.851*176 = 149.8 (f38) or 1.02*144 = 146.9 (f29, t=1.2) -> d24 = 1.170 / 1.148 m
  -> displacement 35.2 / 33.1 cm (mean 34.2).
- Route B (straight ramp path): 3D line from start point (f0, depth from size 1.198 m, ~= slope_far 1.201 m) to
  f29 (depth 1.02 m given); intersect with f24 ray (gap 1 mm) -> d24 = 1.156 m -> displacement 33.9 cm
  (34.05 with d0 = 1.201).

Answer 34.0 cm (routes agree within ~±1 cm). Script: calc.py. Confidence: moderate-good (depth at 1.0 s inferred).
