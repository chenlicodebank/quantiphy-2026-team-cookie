# Q1493 – speed of the car at t = 1.0 s (frame 24), m/s → **6.1**

File fps = question fps = 24, so t = 1.0 s is frame 24 and t = 2.0 s is frame 48. The camera is static (LK flow on about 380
background corners: no shift, scale 1.000000).

## Tracking (scene/ record only used as a starting point)
The silhouette centroid in scene/ is noisy (about 3 px rms, and partly hidden by the pole up to frame 28), so I tracked rigid
features instead (`track_feat.py`, `track_tl.py`, `rims.py`): the white ring on the engine cover (NCC > 0.92 from frame 18,
visible at frame 24), the rear-left hub, a body point behind the front wheel, both tail lights, and ellipse-fitted centres of
both left rims.

## Camera / motion model
- Vertical VP from the edges of the two utility poles (`vp.py`): (1270, 12180).
- Pure translation: all 5 tracks are straight lines (0.1–0.25 px) meeting at one focus of expansion, FOE = (-1169, -898)
  (`foe2.py`, rms 0.22 px). The Z-translation per frame is constant (0.00772 vs 0.00769, first vs second half), so the speed
  is constant and the speed at frame 24 equals the mean. A fit that allows yaw gives yaw ≈ 0 (`yawfit.py`).
- Focal length, two independent routes: motion direction perpendicular to the pole vertical → f = 4303 px; tail-light
  vector perpendicular to the motion → f = 4369 px. I use f ≈ 4330 (hfov ≈ 33°). Checks: the reconstructed wheelbase is
  constant (0.0995–0.1004 units over frames 40–71), horizontal, and parallel to the motion.

## Scale – conflict with depth_info
For any point on the body, the image gives Z24/Z48 = 0.815 (independent of f). The given distances need about 0.76
(17.83/23.20, after converting to Z). No point on the body can satisfy both. The flat-road reconstruction that matches the
depths (f ≈ 3600) makes the car non-rigid: its wheelbase grows 24% from frame 22 to 71. So the given depths cannot both
belong to a point fixed on the car body. Speed of any point rigidly attached to the car = body speed = 0.2233·σ m/s, where
σ is the ring depth at frame 48 in metres.
Candidate scales (speed):
- body centre at d48 → 5.21; body centre at d24 → 4.87. Both violate |d48−d24| = 5.37 m in 1 s, the hard lower bound.
- Origin as close to the body as both exact depths allow (`origin_fit.py`): σ = 27.7 → **6.19**.
- Height prior 1.15 m (≈ LaFerrari 1.116 m, ×1.03) via the car's proportions (`dims.py`, `width2.py`): wheelbase 2.73 m →
  σ = 27.3 → **6.11**; rear rim → 5.9–6.0; body width ≤ 2.05 m → speed ≤ 6.36.
Answer **6.1 m/s** (the scale chosen from the height prior and the car's proportions, which agrees with the minimum-offset
depth solution, 6.19).

## Confidence
Moderate. The image geometry is solid. The metric scale is uncertain by about ±5–8%, because the given depths conflict with
the image and the height has to be converted through the car's proportions.
