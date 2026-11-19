# q_157 — height of the plane (m); prior: car length = 5.67 m

2D side-view render, fps 24 (same as question_fps, so no re-timing issue). Static camera.

Method (measure.py): threshold max|RGB − bg(80,81,88)| at 12/18/30, 3×3 opening, connected components,
on frames 0, 2, 5, 10, 15, 18 (plane fully visible).
- Car (Cybertruck-like) length: 91 px at frames 0–10, when it is near the image centre (x 854–944 at frame 0).
  Later frames read 92–93 px because the off-centre perspective shows a bit of the end face. Height 30 px.
- Plane height (fin top to engine bottom, no landing gear in the model): 181–182 px in every frame and at every threshold
  (y 369/370 to 550).
- Scale = 5.67 / 91 = 0.0623 m/px  →  plane height = 181.5 × 0.0623 ≈ 11.3 m.

Checks: the same scale gives a plane length of 608 px × 0.0623 = 37.9 m (a real A320 is 37.6 m) and a car height of
30 px → 1.87 m (a real Cybertruck is about 1.9 m). So both objects sit at a consistent scale. A real A320 is 11.8 m tall with the gear
down, and this model has no gear, so about 11.3 m is plausible. The scene/ record values (608 px, 181–182 px, 91 px) agree with my re-measurement.
Confidence: high (about ±2%, mostly from 1 px of uncertainty in the 91 px car length).
