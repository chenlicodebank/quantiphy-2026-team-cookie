# q3261 – speedboat displacement 1.00 s → 4.00 s

Prior: velocity at 1.00 s = 11 m/s. Internet video, single planar scale = 11 m/s / pixel speed at 1.00 s.

Time base: file 29.97 fps vs question 30 fps – the same to 0.1 %; t=1.00 → frame 30, t=4.00 → frame 120 under either.

Measurement (reference point = canopy centre, background-compensated because the camera pans ~0.3-0.5 px/frame):
- scene record (`canopy_tm_x_bg`): x(f30) = 283.5, x(f120) = 1599.7 → D = 1316.2 px.
- independent re-check (`check.py`: own canopy template from f61 + own 9-patch bank shift): D = 1314.5 px.
- pixel speed at f30: one-frame forward difference 15.3-15.7 px/frame (noisy); smoothed over f25-35 15.8 px/frame
  (record: (f35-f26)/9 = 15.8). Used 15.8 px/frame = 474 px/s.
- scale = 11 / 474 = 0.0232 m/px → displacement = 1316 × 0.0232 ≈ 30.5 m.

Second route: the raw (uncompensated) image track gives 1266.5 px and 15.3 px/frame → 30.4 m; the unsmoothed forward
difference from my check gives 31.5 m. Answer 30.5 m; confidence moderate-high (±3 %, mainly from the speed at 1 s).
