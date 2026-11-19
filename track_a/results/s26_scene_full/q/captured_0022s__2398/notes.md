# q_2398 – ping pong ball displacement 0.6 s → 1.6 s (cm)

- question_fps = file fps = 24 → frames 14 and 38. Lab camera: f = 0.5959·1280 = 762.8 px, principal point (640, 360).
- Ball centre pixels (scene track, checked on 8x crops, measure.py / frames/f14.png, f38.png):
  f14 (435.3, 395.0), f38 (408.0, 511.3). Also used f19 (431.5, 413.5), f29 (422, 455) from the track.
- Depths given at f14 (1.751), f19 (1.687), f29 (1.526); none at 1.6 s.
- Main route (solve.py): back-project f14/f19/f29 with their depths → 3 points nearly collinear (residual 5 mm; the ball
  rolls straight down the board). Intersect the f38 pixel ray with that 3D line: gap 2.4 mm, range 1.371 m.
  Displacement |P38 − P14| = 44.27 cm.
- Check routes: depth vs frame extrapolation linear 1.392 m → 42.6 cm; quadratic 1.343 m → 46.6 cm (bracket the
  line-intersection result). Apparent diameter at f38 ≈ 23 px (core read, biased +1–2 px as seen at f14/f19/f29 vs
  depth-predicted size) → 21.5–22.5 px ↔ Z ≈ 1.36–1.42 m, consistent with 1.371 m.
- Answer: 44.3 cm. Confidence: moderate-good (±5 %), driven by the extrapolated depth at 1.6 s.
