# Q959 — speed of the phoenix at 0.5 s (m/s)

Prior: acceleration at 2.0 s = 2 m/s^2. 2D simulation, 24 fps (file fps = question_fps, no retiming). t=0.5 s -> frame 12.

## Method
- Used the scene record's beak-tip track (tracks/phoenix.csv ref_x; leftmost mask pixel, rigid with the head), plus
  body-template and mask-centroid tracks as cross-checks. Checked the contact sheet: a single phoenix flying left, static camera.
- Per-frame dx shows a strong ripple with the 25-frame flap cycle, so I fitted
  x(f) = x0 + v0 f + a f^2/2 + 2-harmonic sinusoid (period scanned 22-28 frames), frames 0-69 (fit.py, fit2.py).
- Beak fit: period 25.0 frames, RMS residual 1.2 px (= pixel quantisation), a = 0.657 px/frame^2, v0 = 0.012 px/frame,
  i.e. at rest at frame 0.02. Centroid fit: a = 0.653, rest at frame 0.03 (RMS 6 px). Body template (cumulative,
  drifts): a = 0.642, rest at frame -1.1.
- So the origin moves with constant acceleration from rest at t = 0; the ripple is the flap animation surge of the mesh.
  The round prior (2 m/s^2 at 2.0 s) is that constant acceleration. Scale = 2 / (0.657*576) ≈ 0.0053 m/px (bird length
  ~715 px ≈ 3.8 m, final speed ≈ 5 m/s: plausible for a large phoenix).
- Speed at frame 12 (backward difference of p = a t^2/2, rest at t=0): a*(12^2-11^2)/(2*24) = 2*23/48 = 0.958 m/s.
  (Instantaneous a*t would be 1.000 m/s; the benchmark convention is the backward difference.)

## Second route
- Pixel route: trend speed at frame 12 = (v0 + 11.5 a) px/frame = 7.57 px/frame -> x 24 x 0.00528 m/px = 0.958 m/s
  (beak), 0.956 (centroid), 1.05 (body template, which drifts).
- Raw per-frame beak dx around frame 12 is ~10 px/frame because of the flap surge of the mesh; the origin trend is used.

Answer: 0.958 m/s. Confidence: fairly high (relies on the origin following the uniform-acceleration trend).
