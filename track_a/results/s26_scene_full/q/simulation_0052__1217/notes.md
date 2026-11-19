# q1217 – height of the green car (simulation_0052)

The green car is the dark green/black vintage coupe in the near lane, called `black_car` in scene/.
The file runs at 30.0033 fps; all times use question_fps = 30, so t=1 s is f30 and t=2 s is f60.

## Scale (prior plus depth_info)
- Orange car pixel acceleration: quadratic fit of the record's hub-based ref_x over f6-86, leaving out the
  extrapolated and occluded frames, gives 301.3 px/s^2. Fits over sub-windows give 297.6-303.0, with
  residuals under 0.7 px. The orange car keeps a constant depth (wheelbase 323.2 px everywhere), so
  k = Z_o/f = 2.86/301.3 = 0.00949 m/px.
- Orange distance at t=1 (u=621, v≈745): 15.436 = k*sqrt(f^2 + r^2), which gives **f ≈ 1611 px** and Z_o ≈ 15.3 m.
  Check: the orange distance at t=0 is reproduced as 17.2 vs the given 17.26. The orange car's two distances
  alone give f=1583, which in turn implies an acceleration of 2.91 vs the prior's 2.86, so these agree to about 2%.
- Green car depth from its distance at t=1 (f30, hub centre u=1112): Z_g ≈ 9.5 m.
- Inconsistency: the green distance at t=2 (f60, car off-screen; its u comes from extrapolating the measured
  constant speed of −69.84 px/frame) fits only with f≈1785. That disagrees with the prior by 10%: f=1785 would
  give an orange acceleration of 2.58. So I trust the orange-based f and treat the t=2 green value as an
  outlier, probably caused by motion after the car leaves the frame.

## Pixel measurements (re-measured)
- Green roof top: row 636 (half-maximum of the difference from the background, f31-35 and f47-49).
- Green tyre bottom: row ≈902. In columns through the hubs at f36/39/42 the hubcap spans 804-884 and the
  tyre is dark down to about 904, with reflections below that.
- Orange tyre contact: row 794. Orange roof: row 643.
- Vertical edges (lamp poles and window frames) converge upward, so the camera is pitched up about 3.5-4.5°.
  This puts the horizon at about 640-670 px; the pole-only estimate is about 656. The record's statement
  that the poles converge downward is wrong.

## Height
The naive estimate 263 px × Z_g/f ≈ 1.57 m is too big. The bottom of the silhouette is the near-side tyre,
which is about 0.8 m closer to the camera than the car's centre, and the roof sits almost at the horizon.
I used an exact pitched-pinhole model (height_model.py):
- Route A, green car only (tyre row 902, roof row 636, Z_g): H = 1.42-1.46.
- Route B, camera height from the orange car's contact row and depth, plus the green roof row and Z_g:
  H = 1.31-1.41, and it depends on the horizon row.
- The two routes agree when the horizon is at about 637-640 px, giving H ≈ 1.40-1.42. With the pole-based
  horizon of 656 they give 1.44 and 1.36.
- Sanity check: the same model gives the orange car a height of 1.35-1.37 m and a length of about 4.83 m,
  close to a real Kia Stinger, so the scene is roughly real scale. The green car comes out slightly larger
  than a real 300SL (1.30 m), which is consistent with its pixel length (~4.7-4.9 m).

**Answer: 1.41 m.** Confidence: moderate, within about ±4%. If the green car's t=2 distance were trusted
instead, f would be about 1785 and the height about 1.30.

Scripts: accel.py, solve.py, joint.py, poles.py, verticals.py, roof.py, bottoms.py, crops.py, height_model.py.
