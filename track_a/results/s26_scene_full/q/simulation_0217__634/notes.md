# q_634: diameter of the white fur carpet (m)

- Scene: 2D top-down Blender render, static camera, 24 fps (file fps = question_fps, no re-timing).
- Prior: black cat speed = 0.94 m/s. The cat walks a straight line at a near-constant speed. Pixel speed from
  scene/tracks/black_animal.csv (checked in fit.py):
  front-edge net 10.98 px/frame, front-edge linear-fit slope 10.98, body-centroid mean step 11.02, whole-mask centroid
  mean step 10.92 px/frame. I used 10.96 px/frame = 263 px/s, which gives a scale of 0.94/263 = 3.575e-3 m/px.
- Rug (rug.py, fit.py): on frame 0 I cast rays from about (440, 632) and placed the edge at the steepest brightness drop.
  The right side is hidden by the sofa and the shadow/cat top-right, so I used only the clean edge points (angles 90–267°, plus 309–330°).
  - Circle fits: D = 475 px (wide arc, residual 9 px), 474 px (with the upper-right points) and 486 px (120–240°, residual 3 px).
  - Direct extents: top y 389, bottom y 873, so the vertical diameter is 483 px. The left edge x = 198 and the centre x ≈ 437–441
    give ≈ 480–486 px. scene.json lists 487 px.
  - Adopted D ≈ 482 px.
- Answer: 482 × 3.575e-3 = 1.72 m. Second route: the vertical extent of 483 px gives 1.727 m. The fit range 474–487 px
  gives 1.69–1.74 m.
- Confidence: moderate-high. The main uncertainty is the fuzzy fur edge (±2%) and whether the reference counts the hair tips.
