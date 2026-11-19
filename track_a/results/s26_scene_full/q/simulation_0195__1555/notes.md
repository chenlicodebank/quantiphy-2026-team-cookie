# q1555 — diameter of the orbiting Callisto model (simulation_0195)

File fps = question_fps = 30. Moon = the small cratered sphere (scene/ "moon"); "big europa" = the large banded planet.

## Method
- Moon track: scene/tracks/moon.csv circle-fit centres (checked: smooth cubic residual 0.08–0.10 px).
- Focal length from the speed prior (0.627 m/s) + depth_info:
  1. Depth interpolated between 13.004 m (t=0) and 13.856 m (t=3), back-projected 3D path, f solved so the mean
     per-frame speed = 0.627 -> f = 2612 (linear Z) / 2616 (Z ∝ 1/d) px, but the speed then varies 0.68 -> 0.55.
  2. Better (measure.py / orbitfit.py): 3D circular orbit with constant angular speed around the planet origin
     (planet centre (941.26, 489.6) px at 16.549 m), free f, plane, radius, phase, ω, fitted to all 100 pixel
     positions plus both given depths. Fit rms 0.09 px, depths reproduced to 0.2 mm, f = 2669 px (HFOV 39.6°),
     R = 4.257 m, and the resulting speed = 0.6265 m/s — reproduces the prior independently of it (prior not used in the fit).
- Pixel diameter (diam.py): circle-fit silhouette 28.04 − 0.453 t px; lit-limb half-max 27.85 − 0.41 t px
  (dark-side half-max is smaller due to shading, ignored).
- D = d_px · Z / f: t=0 ≈ 27.9·13.004/2669 = 0.136 m; t=3 ≈ 26.65·13.856/2669 = 0.138 m; mean over clip
  (orbit-fit depths, circle-fit size) 0.1372 m.
- Route 1 f (2612–2616) would give 0.1405; rejected because it implies a non-constant orbital speed.

## Answer
0.137 m. Confidence: good (~±3%); residual inconsistency is the diameter ratio (1.051) vs depth ratio (1.065).
