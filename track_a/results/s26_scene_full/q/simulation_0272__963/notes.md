# Q963 – speed of the phoenix at 0.5 s (prior: acceleration at 2.0 s = 2 m/s^2)

2D sim, 24 fps (question_fps = file fps = 24, no re-timing). Static camera. t = 0.5 s -> frame 12.

## Measurements
- scene/tracks/bird.csv (body_cx, beak_x) plus my own sub-pixel template tracking of the head and neck
  between consecutive frames (track_head.py -> head_steps.npy; neck track is the cleanest, corr > 0.9 up to f57).
- Per-frame steps pulse with the 25-frame flap cycle (about 6 px/f at f2-12, 3-4 at f13-20, 15-18 at f27-47, 25-28 at f53+).
- fit2.py: x(f) = x0 + v0 f + a f^2/2 + 2 harmonics of a free period. Best period is 25.0 frames, exactly the flap
  cycle (wing-spread maxima alternate 522/616 px at frames 10, 21, 35, 46, 60, 71). Residual rms: 0.7 px (neck),
  1.3 px (body, beak). v0 is about 0 (from -0.08 to +0.04 px/f), and starting from rest at frame 0 fits best.
  a = 0.4132-0.4141 px/f^2 across the three tracks (pure quadratic: 0.415-0.417).
- So the origin (rig root) moves with uniform acceleration from rest at t = 0. The pulsing is the flap action
  moving the body back and forth by about 15-18 px (a cosine with the 25-frame cycle) relative to the root.

## Answer
Scale: a_px = 0.4135 px/f^2 = 238.2 px/s^2, which corresponds to 2 m/s^2, so 0.00840 m/px.
Backward-difference speed at frame 12 = a*(12 - 0.5)/24 = 2 * 11.5/24 = 0.958 m/s.
Check in pixels: 0.4135*11.5 = 4.755 px/f, times 24, times 0.00840 = 0.958 m/s.
(The analytic v = a t would give 1.00 m/s.)

## Alternative reading (not used)
If the reference origin followed the pulsing body motion: local speed at f12 is about 6.5-7 px/f and the local
acceleration at f48 is about 1.25 px/f^2, giving about 0.45-0.5 m/s. This is rejected because the clean
quadratic-plus-flap-cycle fit (sub-pixel residuals, v0 = 0) shows the root itself accelerates uniformly.

Confidence: fairly high in 0.958. The main risk is the convention: 1.0 if the reference used a*t.
