# Q752 – acceleration of the paper airplane at t = 1 s

- fps 24 (file and question agree); t = 1 s → frame 24. The acceleration is (speed(24) − speed(23)) × fps.
- The "arrow" in scene/ is the paper airplane, seen edge-on (checked on frame 24: thin white shape near (1096, 343)).
- 2D scene, so one scale. Prior: the cat's speed is 0.714 m/s. The cat's torso centroid moves at 8.96 px/frame
  (linear fit over frames 0–49; mask centroid gives 8.95, front edge 9.02), i.e. 215 px/s, so the scale is
  0.00332 m/px.
- Airplane speed (ref = midpoint, per-frame |Δp|): about 72–77 px/frame up to frame 21, then it falls steadily
  (75 → 63.5 by frame 29 → 38 by frame 41). Raw differences are too noisy (±3 px), so I smoothed them. The slope of
  speed at frame 23.5, in px/frame²:
  - quadratic fits of speed over frames 17–31 / 18–30: −1.27 / −1.38
  - linear fit over 19–29: −1.55; cubic fits over 15–33 / 14–34: −1.56 / −1.42
  - second route, polynomial fits of position (cubic over 17–31, quartic over 15–33, quintic over 12–36), then the
    exact speed difference between frames 24 and 23: −1.42 / −1.61 / −1.42
  - the fletching-end point (tail) gives the same within 0.05 px/frame².
- Taking −1.43 px/frame² × 24² × 0.00332 m/px gives −2.73 m/s². The spread across methods is 2.4–3.1. The speed is
  falling, so the airplane is decelerating; I answer with the magnitude, 2.75 m/s².
- Confidence: moderate (±10%). The main uncertainties are the smoothing window and the cat's gait-averaged
  pixel speed (±1%).
