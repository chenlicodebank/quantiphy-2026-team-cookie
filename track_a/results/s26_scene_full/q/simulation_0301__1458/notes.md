# q1458 — forklift speed at t = 1.0 s (frame 24), file fps = question fps = 24

Prior: forklift acceleration = 2 m/s^2. depth_info: forklift 16.7953 m (t=1, f24), 19.0980 m (t=2, f48).

Method (recon.py, recon2.py):
- Forklift image position = amodal bbox centre from scene/tracks/forklift.csv (checked: track smooth, frames 0-1 at rest).
- Pinhole camera, principal point at image centre, unknown f. P(24), P(48) = depth x unit ray. Assume a straight
  3D path through them; every frame's position = closest point on that line to the frame's ray -> s(t).
- Quadratic fit of s(t) over frames 3-71; f picked so that the fitted acceleration = 2 m/s^2 (prior):
  f = 3474 px (hfov 40.5 deg). Fits early (f4-39) and late (f40-71) separately give about the same acceleration
  at any f, so the motion really is uniformly accelerated. RMS residual 8 mm.
- Fitted vertex (start of motion) at frame 0.39 ≈ t = 0 -> starts from rest at t = 0.
- Speed at frame 24, backward difference: a x (24 - 0.5)/24 = 1.958 m/s (exact model); fitted-curve values 1.93-1.97;
  measured per-frame steps averaged over frames 21-27: 1.959 m/s.

Second route: displacement f24->f48 = 2.95 m, matching a(1.5 - t0) = 2.97 for t0 ≈ 0.016 s — consistent.
Answer 1.96 m/s (a·t = 2.0 under the instantaneous reading, 2% away). Confidence: high.
