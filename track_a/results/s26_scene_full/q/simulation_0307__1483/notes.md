# Q1483 – displacement of the plane, 0.5 s → 1.0 s (frames 12 → 24 at question_fps 24; file fps also 24)

Prior: plane speed 22.16 m/s. depth_info: 102.6664 m at t=1 s, 121.8263 m at t=2 s.

## Method (fit.py)
- Track: scene/tracks/aircraft.csv hull centroid (origin proxy); camera static; plane flies a straight line
  away from the camera, no turns or stops (motion starts after frame 1).
- Pinhole camera with the principal point at the image centre, focal length f free. 3D path P(t) = P0 + V t, fitted to
  pixel positions for frames 2–71 and to the two given depths.
  - Free fit: f ≈ 3200 px, rms 2.3 px, speed = 22.53 m/s. This matches the prior 22.16 (1.7 % off) without using it,
    so the speed is constant.
  - Speed fixed at 22.16: f ≈ 3380 px, rms still 2.27 px, and the given depths come out as 102.69 / 121.80 (match).
  - A constant-acceleration model is not constrained by the data (it drifts to f = 303 px with no real gain in fit),
    so it was rejected. Fitting sub-windows gives 27.0 m/s (frames 4–40) and 19.2 m/s (30–71); these windows are
    poorly conditioned, and the full-clip fit is the reliable one.
- Constant velocity → displacement = 22.16 × 0.5 = 11.08 m. The free fit gives 11.26 m directly (second route, 1.6 % apart).

Answer: 11.08 m. Confidence: high.
