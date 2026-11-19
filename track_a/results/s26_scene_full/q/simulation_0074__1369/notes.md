# Q1369 – height of the purple car (simulation_0074)

Answer: **1.43 m**. The purple car is the parked Mercedes-style sedan on the left, which stays still the whole clip. File fps = question fps = 24.

## Camera (bg.py, kerbs.py, cam.py, poles.py, geom.py)
- Background = median of every 10th frame. Kerb edges were found as sidewalk/road colour transitions (R-B channel) and fitted
  with sub-pixel lines, rms 0.3-0.5 px. Some kerb segments turned out to lie on the same image line, which leaves 2 lines per road direction.
- Vanishing points: A (-1315,-264) and B (2688,-258). The horizon is level (roll 0.09 deg). Orthogonal VPs give f = 1791 px.
- Vertical VP from 8 poles: (1078, 4595). This confirms the principal point x = centre, and with the horizon gives f = 1802 px.
  Each pole's lean matches the model within 0.005.
- I used f = 1797 px (hfov 62 deg) and pitch = 24.03 deg.
- Camera height H comes from the depth_info (hcam.py, hscan.py). Each object origin was placed at the ground centre (wheel-contact midpoint
  plus half-track) for the vehicles, or at the pelvis (~0.95 m) for the pedestrian and cyclist:
  van14 9.45, van38 9.61, taxi38 9.24, ped14 9.70, cyc38 9.54, cyc14 9.46. Median **H = 9.5 m** (spread ±2.5 %).
  Changing f does not reduce the spread, so it comes from where each origin really sits.
- Check against the prior (white van length 6 m), which is independent of the depths:
  - A 6.0 m box on the van's wheel line at H = 9.5 fits the van in frame 14 (vanbox.py).
  - The silhouette length is 6.0 m for an assumed van width of 2.0 m (vanmask.py). This check is sensitive to the width.
  - The van wheelbase is 3.83 m (a Chevrolet Express 155" is 3.94 m), and the taxi wheelbase is 2.88 m (a real Crown Vic is 2.91 m).

## Purple car (purple.py, rails.py, railsolve.py, crown.py)
- Near-side tyre contacts are at (451,365.5) and (558,403), giving a wheelbase of 2.92 m at 30.9 m from the camera.
  The car axis's vanishing point (-1337,-261) is the road's, so the car is parallel to the road.
- Roof: the far rail is the top silhouette (x 528-572) and the near rail is the roof/window boundary (x 496-511).
  Both run toward the axis VP (sd 0.4 / 0.2 px). They are treated as two parallel 3D lines at the same height,
  symmetric about the car centreline.
- Centreline offset from the near tyre-contact line: c = 0.80 ± 0.05 m. This comes from the midpoint of the front-bumper ends
  at bumper height 0.45-0.5 m (0.75-0.83), consistent with a typical half-track.
- Result: rail height 1.407 m (c 0.75 → 1.432, c 0.85 → 1.382), roof width 1.24 m. Each 1 px of edge error changes it by 0.009 m.
- Roof crown above the rails, from the rear roof-edge profile (crown.py): max height 1.42-1.44 m → bbox height ≈ **1.43 m**.
- Dependence on H: H = 9.24 gives rail 1.36; H = 9.7 gives 1.445.

## Second route / sanity
- The van box fit and van length agree with H = 9.5 independently of the depths.
- The wheelbase (2.92 m) and height (1.43 m) suit a Mercedes W123 (real 2.795 / 1.438), so the scale is close to real.

Confidence: moderate. Likely error about ±4 % (from H, the centreline offset and the roof crown).
