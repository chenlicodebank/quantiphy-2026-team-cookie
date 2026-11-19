# q_1949 — acceleration of the red general chess piece at t = 1.5 s

- Object: the cream disc (the record calls it a "block") sliding down the ramp trough. It is the Chinese chess piece
  lying flat; its long image axis, about 81.3 px along the motion direction, is the diameter (0.097 m, from the prior).
  Its apparent length stays the same along the ramp (81.5 / 81.4 / 80.9 / 81.7 px in successive 10-frame bins, slope
  -0.009 px/frame), so there is no measurable perspective. I used one scale: 0.097 / 81.3 = 1.193e-3 m/px.
- fps 24 = question_fps.
- Track: scene/tracks/block.csv s_along_path (template centre, ±1 px). In fit.py I checked the repeated frames
  myself with frame differences: 6, 13, 25, 28, 35 and 38 are duplicates. The frames before duplicates take double
  steps, so I mapped each frame to its true render index (as in the scene notes). The resulting per-frame steps grow
  smoothly; the quadratic fit residual is 0.5–0.7 px (it is 10 px without the remapping).
- Acceleration along the path in px/s², from quadratic fits over different windows: 3–36: 582; 10–36: 577; 15–39: 566;
  20–39: 556; 24–39: 543. A cubic fit gives a(t) = 595 / 572 / 548 at t = 0.5 / 1.0 / 1.5 s. The acceleration
  falls slightly over time, which fits Blender's rigid-body linear damping. The late-window fits and the cubic both
  give about 550 px/s² at t = 1.5 s (frame 36).
- Answer: 550 px/s² × 1.193e-3 m/px ≈ 0.66 m/s². The range across methods is 0.65–0.69.
- Confidence: moderate-high. The main uncertainties are the pixel size of the diameter (±2 %) and whether the
  reference used a constant fit (0.69) or the local value (0.65).
