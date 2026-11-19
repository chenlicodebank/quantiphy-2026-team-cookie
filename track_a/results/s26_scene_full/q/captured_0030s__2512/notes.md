# q2512: speed of the red ball at t = 0.2 s (cm/s)

- The file and the question both run at 24 fps, so t = 0.2 s is frame round(4.8) = 5. depth_info gives the distance to the ball at f5 = 0.8715 m (the "s" in the record is a typo for m), f10 = 1.166, f14 = 1.372 and f19 = 1.315 m.
- Camera: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360). The 2D centres come from scene/tracks/red_ball.csv (circle-fit cx, cy_corr). These are sharp at f5-10, and the sheet confirms they are on the right object.
- Back-projection: P = unit ray(u, v) × the camera distance at that frame.
- Depth between the given times: the ball moves mostly away from the camera here, so the result depends on how fast its depth changes.
  - The given values average 0.0589 m/frame between f5 and f10.
  - The 7 cm ball's pixel diameter (60 px at f5 down to 46 px at f10) gives a nearly linear 0.055-0.057 m/frame. This independently confirms a steady depth rate around f5.
- Main route (vel3.py), with distance = 0.8715 + 0.0589·(i−5):
  - forward differences at f4, f5 and f6: 170, 161 and 147 cm/s;
  - 5-frame smoothed estimates: (p7−p3)/4 = 165, (p8−p3)/5 = 159, (p7−p2)/5 = 172, and the mean speed over f3-7 = 162 cm/s.
- Second route (vel2.py), with depth taken from smooth fits to the diameter-derived distance, rescaled to the given depths, or from a spline through the given depths: 155-168 cm/s for most models. The outliers are poorly constrained quadratics, at 145 and 215.
- Breakdown: about 87 cm/s across the image and about 140 cm/s in depth.
- Answer: **162 cm/s**. Confidence is moderate (about ±10%), because the depth rate at f5 dominates the result.
