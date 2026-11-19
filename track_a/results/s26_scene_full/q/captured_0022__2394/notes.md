# q_2394: length of the table (cm), captured_0022

The "table" is the tilted wooden board (tabletop). Its length is the long left–right edge (front and back edges in the image). The camera is the lab camera: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360). File fps and question fps are both 24.

## Board corners (edges.py → edges_v.py)
- The scene/ record's corners and my first colour-mask fit (measure.py) both followed the blurred halo from the background edit, so they were off by up to about 7 px.
- I re-fitted each side on the sharp step in the V channel, taking the maximum outward brightness drop along normals at 40 samples. Line residuals are 0.2–1.7 px. The overlay is in frames/quadV.png.
- Top-surface corners (px): BL (281.1, 416.7), BR (600.2, 361.3), FR (671.0, 513.5), FL (224.9, 613.8).

## 3D reconstruction (measure2.py, mc.py)
- **Ball points:** the centre at frames 14, 19 and 29 (t = 0.6, 0.8, 1.2 s), back-projected with depth_info (1.751, 1.687, 1.526 m). I added 1 px to v to correct the centroid bias noted in scene/.
- **Route A (main):** the plane normal comes from the two vanishing points of the rectangle edges. At f = 763 they are 88.6° apart, close to the expected 90°. The plane is placed 2 cm (one ball radius) below the mean ball centre. Corners are intersected with that plane.
  - Result: length 71.55 cm (back and front edges), width 58.3 cm.
  - Monte Carlo with ±1.5 px corner noise: length 71.6 ± 0.4 cm.
- **Route B (check):** the plane is spanned by the 3D ball-path direction and the long-edge vanishing direction.
  - Back edge 72.6 cm, front edge 69.0 cm (mean 70.8); sides 64.3 cm.
  - The length agrees with route A to about 1%. The width is less stable (58 vs 64), but the question does not ask for it.
- **Sensitivity:** without the 2 cm ball-radius offset the length would be 69.9 cm.
- The ball path sits about 3.8° off the route-A plane. That is consistent with roughly 1 cm noise in the depth values.

## Answer
Length ≈ 71.5 cm. My confidence is fairly high (±3%).
