# q_1664 — height of the freestanding art display panel (m)

File fps = question_fps = 33. 3D Blender scene (segmented), static camera, 1080x1080; principal point assumed at (540,540).

## Focal length (two routes)
- Route 1 (depth_info only): the man's pixel height stays ~constant (257-268 px) while the given Euclidean distance drops
  6.84 m (t=0, pelvis px 882.9,648.3) -> 6.49 m (t=1 = frame 33, pelvis 688.6,649.8). This means he walks at constant
  optical-axis depth Z. Setting d^2 = Z^2 (1 + r^2/f^2) equal at both times gives f = 908 px, Z = 6.36 m.
  Check: the legs-together bbox height of 266 px (frames 5-8 and 39-40) x 6.36 / 908 = 1.862 m, vs the 1.87 m prior (0.4 %).
- Route 2 (prior height): f from 266 px = 1.87 m at the interpolated depth gives f = 909 px. The two routes agree.

## Panel
- There are two near-identical panels (each 128x167 px bbox, same base y). Measured on the right one (closest to the
  image centre, so most likely the "nearest" one): column profile at x=715 (profile.py, frame 90, unobstructed).
  - Panel top is at y=520. The panel meets the stand base at about y=665. The base's top face runs 665-672 and its front face 672-680.
  - The base bottom directly under the panel plane is about 680 - 7 = 673, so the vertical extent at the panel's depth is about 154 px.
    The raw bbox (519-685) is about 166 px, but that is inflated because it includes the near, lower front corner of the base.
- Z of the panel = 11.042 / sqrt(1 + r^2/f^2) = 10.81 m with the origin at the panel centre (719,596), or 10.73 m with it at the base.
- H = 154 x 10.81 / 908 = 1.83 m (1.82 with the origin at the base).
- Other readings: the raw column extent 520-680 gives 1.91 m and the full bbox gives 1.99 m. Both overcount the base's foreshortened depth.
  The panel without its base (520-665) would be about 1.73 m.

## Answer
1.83 m. Confidence is moderate, about ±5 %. The main uncertainty is where the base bottom sits under the panel plane.
