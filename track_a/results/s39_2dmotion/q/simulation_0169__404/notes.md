# Q404: acceleration of the astronaut at t = 1 s (m/s^2)

Prior: the astronaut's height is 2.2 m. This is a 2D video. The file fps and question_fps are both 24, so t = 1 s is frame 24.

## Scale
- The astronaut is upright at frame 0. Their pixel height is 90 px from the SAM 3 mask (box 477.5-566.7, vert_px 90,
  length 90.8 px) and 91 px from the scene record's bbox. On the zoomed crop (frames/f0.png) the helmet top is at y≈477
  and the feet are at y≈567. These agree within about 1 %, so I used 90.5 px → 2.2 / 90.5 = 0.02431 m/px.
- The size stays steady at about 90-92 px along the body axis through the clip, so the depth does not change.

## Motion (fit.py, samcheck.py)
- The path is almost straight, about 3° off vertical (perpendicular deviation under 1.5 px), so I projected the
  positions onto the path direction.
- The position follows Blender's ease-in/out curve almost exactly: s = s0 + D(3τ² - 2τ³) with τ = (f - t0)/T.
  - Fit to the scene-track centroid (all 80 frames): t0 = -0.25, T = 78.4 frames, D = 274.7 px, rms 0.27 px.
- I applied the benchmark's convention to the fitted curve: acceleration = (speed(24) - speed(23)) × 24, where speed is the one-frame
  backward difference × 24. This gives **62.8 px/s²**.
- The raw one-frame difference gives 168 px/s². That is centroid noise, not motion, so I did not use it.
- Local quadratic or cubic fits around frame 24 (windows of ±8 to ±12 frames) give 56.5-60.7 px/s².

## Second route: SAM 3
- I ran SAM 3 segment on 14 frames (0 to 79). Its centroids agree with the scene track within about 1 px in x and
  2-5 px in y. SAM's centroid sits slightly higher because it includes the dark visor, but the offset is nearly
  constant, so it barely affects the acceleration.
- The same curve fitted to the SAM centroids (rms 0.55 px) gives **59.3 px/s²** (6 % lower than the scene track).
- SAM's own video tracker locked onto the wrong object (net displacement 1216 px), so I did not use it.

## Answer
- The two routes give 59.3 and 62.8 px/s², a mean of about 61.5 px/s².
- 61.5 × 0.02431 = **1.50 m/s²**. The individual routes give 1.44 and 1.53.
- Confidence: moderate to good. The uncertainty is about ±5 %, mostly from the centroid standing in for the true origin
  (the body tilts about 25° during the move).
