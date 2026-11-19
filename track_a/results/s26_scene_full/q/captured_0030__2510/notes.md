# q_2510 — velocity of red ball at 0.6 s (cm/s)

- t=0.6 s -> frame round(0.6*24)=14 (file fps = question_fps = 24).
- Track: scene/tracks/ball.csv (mask centroid), checked visually at frame 14 (centre ≈ (563,428), matches CSV 562.9,425.6).
- Lab intrinsics: f = 0.5959*1280 = 762.8 px, principal point (640,360).
- Depth: depth_info anchors at frames 5,10,14,19 (0.8715, 1.166, 1.372, 1.315 m), interpolated over frames (PCHIP / cubic / quadratic).
  Size check: 7 cm ball at f14 is ~37.6 px -> 1.42 m (given 1.372, consistent within ~3%).
- Positions = unit ray * distance; velocity = forward difference of 3D centres x 24.
- Results (measure.py): raw forward v at f14: 159.5 (pchip/quad) – 172 (cubic) cm/s; 5-frame-smoothed forward
  152–160, backward 163–178; mean raw over frames 12–16: 157–173.
  Pixel speed at f14 ≈ 35–37 px/frame ≈ 1.5–1.6 m/s from the lateral motion alone; the depth change near the far point is small.
- Size-scaled depth model rejected (diameter noise makes the depth jump around).
- Answer: ~162 cm/s. Confidence: moderate (±8%), most of the spread comes from how depth is interpolated between anchors and from the irregular 11->12 step.
