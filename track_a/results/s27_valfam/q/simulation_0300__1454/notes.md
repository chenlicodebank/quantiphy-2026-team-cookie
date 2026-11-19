# q_1454 — speed of the car at t = 2.0 s (frame 48 at question_fps 24 = file fps)

Prior: car acceleration = 5 m/s^2. depth_info: 17.8278 m at t=1 s (frame 24), 23.1989 m at t=2 s (frame 48).

## Method (recon.py)
- Track: scene/tracks/car.csv est_cx/est_cy (whole-car centroid, checked smooth for frames 21-71).
- For a trial focal length f (principal point = image centre), back-project frames 24 and 48 with the given depths,
  take the 3D line through them (straight drive), and intersect every frame's ray with that line (ray-line
  residual <= 2 cm -> straight-line motion is consistent). This gives the arc position s(t) per frame.
- Fit s = c0 + c1 t + c2 t^2 over frames 21-71 for each f.
  - Without using the prior, the quadratic fit is best (rms ~1.6 mm) at f ~ 3400-3500 px, giving acc ~ 4.9-5.0 m/s^2
    and start-from-rest time t0 ~ -0.01 to -0.03 s, i.e. uniform acceleration from rest at t ~ 0. This independently confirms the prior.
  - Using the prior (acc = 5.00) gives f ~ 3400 px, t0 = -0.01 s, displacement 1->2 s = 7.57 m (theory 7.5 m).
- Speed at frame 48 (one-frame backward difference of the reconstructed positions) at f = 3400: 9.95 m/s.
- Analytic check: a=5 from rest at t=0 -> |s(48)-s(47)| x 24 = 5 x 47.5/24 = 9.90 m/s (5 x 2.0 = 10.0 instantaneous).

Answer: 9.9 m/s. Confidence high (routes agree within ~1 %).
