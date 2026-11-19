# q_2638 – basketball velocity at 1.6 s (cm/s)

- The question rate (24 fps) is the same as the file rate. t = 1.6 s is frame round(38.4) = 38.
- In depth_info the second "t=1.6s, distance_soccer_ball_camera = 2.4120 m" is clearly the basketball: it is a duplicate label, and 2.27 m at t=0.6 s
  → 2.412 m at t=1.6 s fits the ball's diameter shrinking from 74 px to 69 px (ratio 1.074 vs 1.063). So I use Z_bb(38) = 2.412 m.
- Lab camera: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).
- Positions: the scene/ RANSAC circle centres (I checked frame 38 visually: the centre is at ≈(562, 474)) back-projected with depth.
  The depth for each frame comes from Z ∝ 1/diam (a linear fit of diam over frames 21–48), anchored at 2.412 m at frame 38.
  The same model gives 2.24 m at frame 14 against the given 2.27 m (1 % off).
- Velocity: 3D forward differences around frame 38. The 35→36 step is doubled (a dropped capture frame), so it is kept out of the window.
  - RANSAC centres: forward difference at 38 = 37.9; mean over 36–40 = 37.1; centred 5-frame vector = 37.0; mean over 37–41 = 36.2 cm/s.
  - Route 2, my own orange-mask centroids: 36.9 / 37.1 / 37.0 / 35.8 cm/s.
  - With constant depth (ignoring the slow recession): 36.2–37.3 cm/s.
- The image speed is about 4.8 px/frame, and the depth rate adds about 4 cm/s along the line of sight.
- Answer: **37.0 cm/s**. Confidence is good, about ±4 %.
