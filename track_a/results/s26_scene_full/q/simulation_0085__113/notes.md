# Q113: distance between car and bike at t = 1.0 s (frame 24, fps 24, question_fps 24, no re-timing)

2D top-down scene. I take the scale from the prior: car acceleration = 4.03 m/s².

## Scale
- `track_tm.py`: sub-pixel template matching of the car body (and the cyclist) between consecutive frames, giving per-frame dx (`tm.csv`).
  The cyclist moves at a constant 27.2 px/frame.
- Car speed is linear in frame number over frames 10–49: acc = 0.906 px/frame² (sub-windows give 0.888–0.934),
  and v = 0 at frame ~0.8. Around frames 50–60 there is a bump (the car crosses the image centre, a perspective/parallax effect),
  and the speed levels off at ~63 px/frame by frame 67. I excluded that window.
- scale = 4.03 / (0.906 × 576) = 0.00773 m/px. Sanity checks: car length 726 px → 5.6 m (Cybertruck-like, real one is about 5.7 m),
  and cyclist speed 5.0 m/s. Both are plausible.
- Front-edge quadratic fit (frames 2–40, from the integer bbox edges): 0.883 px/f² → 0.00792 m/px. The front-edge silhouette
  moves ~2.3% slower than the roof texture, a parallax effect of the tall truck under a perspective camera.

## Positions at frame 24
- Cyclist: bbox centre x = 1270.5, y ≈ 381.5.
- Car: rear edge is still off-screen, so centre = front edge 1588 + (727−1)/2 = 1951 (route 1),
  or bbox centre at frame 40 (1504.5) minus the template displacements over frames 25..40 = 1961.4 (route 2). y = 727.5.
- Lane gap dy = 346 px.

## Result (each route uses one tracked feature for both the scale and the position)
- Route 1 (front edge): 763.4 px × 0.00792 = 6.05 m.
- Route 2 (template/roof texture): 772.7 px × 0.00773 = 5.97 m.
- Answer: 6.0 m. The two routes differ by 1.3%. The main uncertainty is which part of the speed profile defines the
  prior's acceleration (the full-clip average of 0.95 px/f² would give ~5.7 m). Confidence: moderate–good (±5%).
