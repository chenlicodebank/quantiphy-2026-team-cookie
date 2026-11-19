# q_1534 – height of the 'B1' lettering on the back wall (simulation_0150)

Prior: tyre diameter 0.764 m. depth_info at t = 0.5 s (frame 12 at question_fps 24 = file fps):
camera→left-front-tyre origin 11.38 m, camera→B1 sign 23.44 m. Static camera, level, principal point
assumed at the image centre (960, 540) (vanishing point of the ceiling tubes, per scene/).

## Measurements (scripts in this folder)
- `b1.py`: yellowness mask (R+G)/2−B, frames 12 and 41. Letters "B" and "1" both span y 429.2–596.5,
  centre (971, 513). Half-level edges: height 166.8 ± 1 px. (scene.json's 170 px was read by eye.)
- Tyre (frame 12, left front tyre, rim-centre (1656.8–1658.7, 791.3) from a white-rim ellipse fit):
  - bottom silhouette edge (half level of the column profile) y ≈ 884.5–885.5 → radius 93 px;
  - `overlay.py`: circles of r = 86/90/94/98 drawn on gamma-boosted crops. On side-on frame 24 the tyre
    outline sits at r ≈ 92–93 all round (sides, bottom, top under the wheel arch); frame 12 has the same
    axle y and bottom y (so the same depth) and fits r ≈ 93 vertically. The yaw (~17°) does not change the
    vertical diameter.
  - The scene/ note "tyre ≈ 175 px (approx.)" was an eyeball value and does not hold up: r = 88 circles
    fall clearly inside the tyre outline. The upper dark band above r ≈ 93 is the wheel-arch interior.
  - Adopted D_tyre = 185 ± 3 px (vertical).
- `solve.py`: focal length from the tyre, f = D_px · Z_t / 0.764, where Z_t is the axial depth
  = 11.38 / sqrt(1 + (u²+v²)/f²) and the tyre sits at (u, v) = (699, 251) px from the centre. Solved
  iteratively: f ≈ 2655 px (hfov ≈ 40°), Z_t ≈ 10.96 m. The sign is almost on-axis, so Z_s ≈ 23.44 m.
  H = 166.8 · 23.44 / 2655 ≈ 1.473 m.
  Sensitivity: D = 182 px → 1.50 m; D = 186.4 px → 1.46 m; D = 176 px (scene/ value) → 1.555 m.

## Checks
- Second route for the tyre size: the same r ≈ 92–93 px shows up on the side-on frames 22–28 (overlay and
  column profiles, bottom edge ≈ 884–885 with the axle at 791.7). Rim-lip diameter is about 122 px in every
  frame, so the tyre/rim ratio holds steady.
- Consistency of the given depths: camera height from the tyre contact point (344.5 px below the horizon at
  Z ≈ 10.9 m) is 1.41 m. From the back-wall/floor line (y 705, 165 px below the horizon at Z ≈ 23.4 m) it is
  1.46 m. These agree within about 3%, so the depths and the focal length fit together.
- Sanity check on scale: wheelbase 711 px at about 10.95 m gives 2.9 m, a plausible coupe size given that this
  tyre (0.764 m) is oversized.

Answer: **1.47 m**. Confidence moderate. The answer depends mainly on the tyre's pixel diameter (±2%) and the
letter edges (±0.6%); total about ±3%.
