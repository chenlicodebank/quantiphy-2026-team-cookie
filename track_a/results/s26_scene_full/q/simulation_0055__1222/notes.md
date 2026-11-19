# Q1222 – length of the orange car (m)

Prior: car acceleration = -2.86 m/s². depth_info: car 16.059 m (t=0), 11.671 m (t=1, frame 30); man 8.313 / 8.189 m;
hydrant 9.207, lamp 8.901. File fps = question_fps = 30.

## Pixel length
From scene/tracks/car.csv: L_px = 739.7 px (front − rear silhouette edge, frames 49–50, the only frames with both
edges clear; 740.2 / 739.2). Checked against the sheet: the car (a Kia Stinger-like fastback) is fully in view at
frame 49–50 only.

## Route A – pixel acceleration + prior (scale at the car's depth, the car moves parallel to the image)
- fit.py: rear edge, frames 49–77, quadratic: a = −438 px/s² (rms 0.16 px) → L = 4.83 m. The record's front-edge track
  (frames 28–50) gives −324 px/s², but it is biased by motion blur on the nose (its steps are 2–3 px smaller than the
  patch steps), so I rejected it.
- steps.py: consecutive-frame matching of a car-body gradient patch: steps fall linearly, −427 px/s² for frames 26–77
  (−416 for 26–50, −436 for 50–77) → L = 4.95 (5.08 / 4.85).
- wheels.py: front-wheel window, frames 28–51: −425 → 4.98. Rear-wheel window, frames 50–77: −445 → 4.75. Rear-end window: −440 → 4.81.
  The pixel deceleration grows slightly over time (about 5 %). A small yaw of the path (the car approaching about 1–2°;
  the roof row in roof.py drifts down about 1.7 px, though noisily) would do this.

## Route B – depth_info (pinhole)
- Man (moves laterally at constant depth): (d0²−d1²) / (Δ of (u−cx)²) gives 0.004836 m/px. Then f = 1621 px and Z = 7.84 m.
  Sanity check: man 370 px → 1.79 m tall.
- Car with f = 1621: d1 at frame 30 (u ≈ −83…−109, root row 865 or 756) → 0.00657–0.00663 m/px → L = 4.86–4.91.
  The predicted d0 is 15.87–15.94 against the given 16.06.
- Car only, solving f and scale from d0 and d1 (joint.py, positions from patch steps, extrapolated to frame 0):
  f ≈ 1573–1591, 0.00674 m/px → L = 4.985. The implied acceleration of 2.88 m/s² matches the prior's 2.86, so the
  routes agree. The silhouette ends are probably at the car's near side, which is closer than the root. That makes this
  depth-based route read slightly high, by up to a few percent.

## Answer
The routes span 4.75–5.0 m and cluster at 4.83–4.95. Answer: **4.88 m**, which is close to the real length of a Kia Stinger (4.83 m).
Confidence: moderate-good (about ±4 %).
