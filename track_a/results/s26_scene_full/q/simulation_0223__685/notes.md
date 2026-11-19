# q685: speed of red general at t=1 s
- 2D top-down scene, fps 24 (= question_fps). t=1 s -> frame 24 (frames 23 and 24 are clean, not duplicates).
- measure.py: median-background mask on column strip; centroid y: f22 412.76, f23 437.07, f24 462.48, f25 489.05 px; x constant.
- Backward diff at frame 24: 25.42 px/frame (scene record 25.46). Quadratic fit of clean frames 14-33 gives backward diff 25.35, residuals <0.3 px (route 2).
- Scale: general diameter 86.7-87.3 px (bbox 87, area-equivalent 86.8) -> 0.097/86.9 = 1.116e-3 m/px.
- Speed = 25.40 px/frame x 24 x 1.116e-3 = 0.680 m/s. (Instantaneous from fit would be 25.9 px/frame -> 0.694; convention is backward diff.)
- Confidence: high, ~2%.
