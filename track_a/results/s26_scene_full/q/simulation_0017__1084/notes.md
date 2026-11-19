# q1084 – width of the pedestal (square base) of the central sculpture

Answer: **1.49 m**

Time base: question_fps = 33. The file runs at 33.039 fps, so t = 1 s is frame 33.

## Camera / scale (solve_f.py, width.py)
- The camera is static, and the image is rolled 90° (world up = image +x). The shelf-wall vertical edges stay at a
  constant image y across x (y = 166 and y = 1027 for x = 720–1040; pitch.py), so the camera has no pitch. The
  cubby inner faces recede toward the image centre, so the principal point is (540, 540).
- Person: the prior gives 1.3 m/s, and depth_info gives d0 = 5.424 m (frame 0) and d1 = 4.886 m (frame 33).
  Solving with only the pixel positions and |P1 − P0| = 1.3 m gives a constant depth: Z = 4.66 at frame 0 and
  4.66 at frame 33. So the walk runs parallel to the image plane. Solving with the distances only, assuming a
  purely lateral walk: Y0 + Y1 = (d0² − d1²)/1.3, so Y0 = 2.783, Y1 = 1.483 and Z = 4.655 m.
- Focal length f = Z·(540 − y)/Y, using the pelvis track from scene/ (pelvis_y = 20 at frame 0 and 263.7 at
  frame 33):
  - from frame 33: 867 px (871 with the raw value)
  - from frame 0: 870 px
  - from the displacement Δy: 873 px
  - from the whole-clip pixel speed of 7.28 px/frame: 860 px
  - **I use f ≈ 868 px** (horizontal field of view 64°).
- Consistency checks:
  - The bench at 2.267 m (the foreground cushioned bench) comes out at Z ≈ 2.2 m with its centre about 0.43 m
    above the floor. The camera height is about 1.0 m, from the person's feet.
  - The person passes in front of the pedestal, which fits the pedestal's front face being at Z ≈ 5.18 m,
    behind the person.

## Pedestal
- Pedestal = the dark grey square block under the sculpture. Its front face in frame 0 (profile.py): edges at
  y = 404.5 and 654.5, so the width is **250 px**, the same at x = 400, 430 and 460. Its top is at x ≈ 478, and
  its bottom is hidden behind the bench. A lighter tapered piece sits on top of it (x 478–532, about 217–227 px
  wide), then the sculpture.
- Square base: depth = width = w, and the front face is at Z_f = Z_c − w/2. Solving
  |origin| = 5.963 m with w = 250·Z_f/f gives Z_f = 5.18 m and **w = 1.49 m**.
  - This barely changes whether the light piece counts as part of the pedestal: 1.491 vs 1.495 m.
  - It barely changes with camera height (0.95–1.03 m).
  - Over f = 860–873 px it ranges from 1.484 to 1.508 m.
- Check: the pedestal origin (5.963 m) and the sculpture origin (5.962 m) are almost the same distance from the
  camera. That puts the sculpture's centre about 0.65 m above the horizon (image x ≈ 636), which fits the
  sculpture's extent (x 532–783).
- Alternative reading: if "pedestal" meant only the light tapered piece (about 217–227 px), the width would be
  about 1.30–1.36 m. I don't favour this reading.

## Confidence
Moderate to high for the dark-block reading (about ±2% from f). The main risk is which block the question means.
