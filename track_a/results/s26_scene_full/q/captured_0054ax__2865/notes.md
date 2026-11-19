# Q2865 – distance green ball ↔ white ball at t = 1.0 s

- t = 1.0 s → frame 24 (question_fps = file fps = 24).
- Identification: the "green" ball = the small yellow-green (tennis) ball, called `yellow_ball` in scene/; the "white" ball =
  the pale small ball, called `pink_ball` in scene/. Both have just left the standing person's hands at f24. Their given depths
  (3.04 / 3.07 m) match the standing person's distance. The soccer ball sits by the crouching person, nearer the camera,
  which rules it out.
- Camera: f = 0.5959·1280 = 762.8 px, principal point (640, 360). Each position is the unit ray scaled to the given Euclidean distance.
- Centres at f24:
  - scene record (full blob): green (599.7, 291.7), white (569.1, 270.9) → 0.1499 m
  - my colour masks (`measure.py`, only the lit upper part of each ball, so biased slightly upward): green (599.1, 289.4), white (569.2, 269.2) → 0.1463 m
  - visual reading of the silhouettes on a 4× crop (frames/mask24.png): green ≈ (599, 290), white ≈ (570, 271). This agrees with the record.
- The record's full-blob centres are taken as best. Answer: 0.149 m. The ~37 px offset in the image plane gives ~0.145 m;
  the 0.035 m depth difference adds the rest.
- Sensitivity: 1 px ≈ 4 mm at 3 m, so ±2 px in the centres gives roughly ±0.006 m. The prior (orange ball velocity) is not needed,
  because the depths of both balls are given directly.
- Confidence: moderate to high. The answer is small, so the relative error is driven by the centre pixels and the depth values.
