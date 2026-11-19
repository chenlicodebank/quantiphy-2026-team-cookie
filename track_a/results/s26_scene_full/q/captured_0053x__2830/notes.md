# q2830: trashbin displacement 0.4 s -> 1.4 s

The trashbin is the record's "blue_box". It is a blue patterned cylinder lying on its side and rolling away from the camera (up-left in the image).
question_fps = file fps = 24. So t = 0.4 s is frame 10 and t = 1.4 s is frame round(33.6) = 34.
Camera (lab card): f = 0.5959*1280 = 763 px, principal point (640, 360).

## Method (disp.py, sizes.py)
- Centres: mask centroids from scene/tracks/blue_box.csv. I checked them on frames 10 and 34 (frames/full10.png, full34.png, z10.png).
  Frame 10 is at (797.8, 379.7) and frame 34 at (614.0, 268.2).
- Depth at frame 10 = 2.73 m (depth_info, Euclidean). Depth at frame 34 is not given, so I took it from the apparent-size ratio (depth ∝ 1/size).
  I fitted the size locally with a linear fit over ±3 or ±5 frames:
  - minor axis 1.146–1.152, sqrt(area) 1.154–1.155, bbox width 1.150, bbox height 1.157–1.166.
  - The major axis gives 1.085. I treat it as the outlier: the cylinder yaws as it rolls, and motion blur at the faster frame 10 inflates it.
  - The minor axis (the cylinder's diameter) is the most viewpoint-invariant measure.
  - Adopted ratio ≈ 1.152, so D34 ≈ 3.145 m.
- Back-projected 3D points (unit ray × Euclidean depth). The displacement is |P34 − P10| = 0.90–0.92 m. Answer: **0.912 m**.

## Other routes / checks
- With constant depth (a lower bound) the displacement would be 0.757 m.
- Floor-plane route (floor.py): I fitted a plane through the four objects' 3D centres (cup, book, ball, bin) with assumed centre heights, then intersected ray 34 with the bin's plane parallel to the floor.
  This gives D34 = 3.32–3.47 and a displacement of 1.03–1.13 m. The plane is poorly conditioned (only 4 points, guessed heights, residuals up to 6 cm), so I used it only as an upper-side check.
- Prior velocity 0.9962 m/s at 0.4 s (vcheck.py):
  - The unsmoothed one-frame forward difference matches it with a smaller depth change (k ≈ 0.6–0.7 of the size model), which gives a displacement of about 0.85 m.
  - Every 5-frame smoothed scheme already gives more than 1.02 m/s at constant depth.
  - The track also has a probable dropped frame at 11→12, which inflates smoothed speeds near frame 10.
  - So the prior does not pin down the depth change cleanly.
- The size route sits between the velocity route (~0.85) and the floor route (~1.05).

Confidence: moderate, about ±8%.
