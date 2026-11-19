# q1346 – height of the purple car (simulation_0066)

The answer is **1.39 m**, the world-AABB height of the parked purple sedan, from the ground to the top of the roof.
The file fps and question_fps are both 24, so t=0.58 s is frame 14 and t=1.58 s is frame 38.

## Camera model (static camera, pinhole, principal point at the image centre)
- **Vanishing points** (`curbs2.py`, `curbs3.py`): curb lines were fitted with RANSAC on the background.
  - Road B: three lines meet at VB = (3122, 78), with residuals under 0.6 px.
  - So the horizon is at y ≈ 78. VB and the two road-A lines give a roll of about 0.
  - VA is where the A right-curb line crosses y = 78: (622, 78).
  - If the two roads are perpendicular, f = 850 px (HFOV about 104°) and the pitch is 28.5° down.
- **Check of f from depth + prior:** the van's 3D displacement f14→f38, from the depths and pixel centroids, is
  4.25 m at f=850. The kinematics with a=4 from rest at t=0 give 4.33 m (`calib1.py`). This route is weaker
  because of the centroid/origin offset.
- **Camera height H** (everything scales with H). Four routes:
  1. Pedestrian at f38 (`pedH.py`): pelvis depth 21.35 m, feet at v≈485 px → H = 7.03 ± 0.07 m.
     This barely depends on the pelvis pixel or the origin height, because the ray is shallow.
     The implied stature is 1.96 m.
  2. Van at f38 (`vanH.py`): depth 19.99 m and the left-wheel ground contacts plus half a track width → H = 7.07–7.20 m.
     Its wheelbase comes out at 3.85 m, about the size of a real extended van.
  3. Taxi at f38: depth 16.55 m and its near-wheel contacts → H = 6.90–7.06 m.
  4. Van kinematics, using the prior a = 4 (`hubtrack.py`, `wheelfit2.py`):
     - The rear-left wheel rim was tracked automatically over f56–70. A fit of s = 2t² has mm residuals and puts the hub plane 6.42 m below the camera.
     - The wheel radius measured in the image is 0.41 m, so H = 6.83 m.
     - This is about 3% below the depth routes. A start time about 2 frames before t=0 would close the gap.
     - Over all frames, the bbox-bottom fits put the start time at t0 ≈ 0 ± 0.4 frames.
  - Adopted H ≈ 6.95–7.0 m (± 2%).

## Purple car (`purple_h.py`, `purple_final.py`)
- **Ground line:** the near-side tyre bottoms, from column profiles, are rear (164, 896) and front (515, 799.5).
  They back-project to a wheelbase of 2.94–2.97 m, and their line passes through VB, so the car is parallel to road B.
- **Roof edges:** both are lines through VB, measured automatically on bg.png (`roofedges2.py`):
  - Far roof edge = the silhouette against the road. Taking its highest part, it crosses x=250 at y ≈ 675.5.
  - Near roof edge = the dark window seal above the side windows, at y ≈ 743 at x=250.
- **Solving for roof height:** the two edges are taken as horizontal lines parallel to the car axis, symmetric
  about the car's centreline.
  - Centreline = 0.86 m from the near tyre face. The bumper-corner width measured 1.71–1.76 m, which matches W116-like proportions.
  - The seal sits about 0.045 m below the roof top, and the silhouette tangent about 0.015 m below it.
  - This gives h_top = 1.383 m at f=850, H=6.95, and 1.394 m at H=6.99.
- **Sensitivity:**
  - centreline ±0.03 m → ±0.017 m
  - H ±0.1 m → ±0.027 m
  - f 800/900 → +0.026 / −0.020 m
  - Full grid range: 1.33–1.44 m.
- **Sanity check:** the car looks like a Mercedes W116 (real wheelbase 2.87–2.97 m, height about 1.41–1.43 m).
  The measured wheelbase of 2.95 m fits a real-scale model, and the measured height of 1.38–1.40 m matches.

## Answer
1.39 m. Confidence is moderate: the estimated error is about ±3–4%, mostly from H and the roof-centreline assumption.

The scene record was correct as far as it was used (static purple car, wheel centres, van/pedestrian tracks).
Its rough f ≈ 830 matches my 850.
