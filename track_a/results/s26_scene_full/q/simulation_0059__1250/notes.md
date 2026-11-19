# Q1250: bicycle wheel diameter (m)

The prior: the white car (the white cargo van in scene/) accelerates at 4 m/s^2. The depths are given at t=0.58 s and 1.58 s (frames 14 and 38).
question_fps = file fps = 24.

## Focal length from the prior (fit_acc.py)
- For each trial f (principal point at the image centre), the van origin's 3D points at f14 and f38 = depth x unit ray of the bbox
  centre (cx, cy from scene/tracks/van.csv). These two points define the van's straight path.
- The sub-pixel panel track (patch_cx, plus a constant offset to the bbox centre) is intersected with that line for every
  frame. A quadratic s(t) is fitted over f2-71 (and over f20-71, and as a linear fit of per-frame speeds). All three agree.
- The acceleration equals 4.00 m/s^2 at f ≈ 2210 px. If I allow for the tracked side panel sitting about 1 m nearer the camera than the
  origin (zshift=0.8-1.0), f comes out at about 2190. I use **f ≈ 2200 px** (horizontal FOV ≈ 52 deg).
- Pixel acceleration of the van: 0.372 px/frame^2 over the whole clip and 0.387 late. The speed rises linearly, so the acceleration is uniform.

## Wheel pixel size (wheel2.py, wheel3.py)
- The tyres are white rings. A RANSAC circle fit on the foreground white pixels at clean frames f28-38 and f53-58 gives a
  ring-centre diameter of 33.5-34.0 px. The rows span 772-806.
- The outer edge was measured as the half-max crossing along the vertical through the fitted centre, on 14 wheel instances: 34.6-35.3 px
  (two outliers caused by the frame/legs were dropped). **Outer diameter ≈ 34.95 px.** I use the vertical extent because it is not
  foreshortened.
- Bike depth at about t=1.33 s (the middle of those frames), linearly interpolated from the given values: D ≈ 40.52 m. Optical-axis depth Z = D·cos(off-axis angle)
  ≈ 40.25 m.
- Diameter = 34.95 × 40.25 / 2200 ≈ **0.64 m** (0.636 at f=2210, 0.642 at f=2190). The ring-centre diameter would give 0.615.

## Second route and disagreement
- Second route: the van and the cyclist both ride along the cross street. If their 3D displacement directions (from the depth pairs) are made
  parallel, f ≈ 2440, which would give 0.58 m. This constraint is weak, though: 1 deg of non-parallelism moves f by about 150 px.
  At f=2200 the two paths differ by only 1.2 deg, which is entirely plausible, so I trust the direct prior route.
- Sanity check at f=2200: van height 2.1 m, bike wheelbase extent 1.7 m, cyclist speed 5.2 m/s. All are plausible.

Confidence: moderate-good. f is uncertain by about ±3% from the prior route, and the pixel diameter by about ±2%.
