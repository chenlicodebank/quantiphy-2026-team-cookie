# Q365 — turtle speed at t = 1 s (m/s)

Prior: turtle acceleration = 2.639 m/s^2 (exact). 2D video, static camera, fps 24 = question_fps (no re-timing).
Speed at 1 s = backward difference at frame 24. Only the ratio v_px / a_px matters, so no metre-per-pixel scale is needed:
v(1 s) = 2.639 m/s^2 x (v24 [px/s] / a [px/s^2]).

## Measurements
- Record (scene/tracks/turtle.csv ref_x) checked with quadratic fits (fit.py): v24 ≈ 22.1 px/frame, a 0.84-1.01 px/frame^2
  depending on window (the chained templates make the record a bit inconsistent across the frame-25/26 join).
- Re-measured independently (track_steps.py): frame-to-frame carapace template matching (high-pass grey, subpixel),
  giving per-frame steps for frames 7-47 (steps.csv). Steps are very linear (rms 0.3-0.5 px):
  frames 7-47: a = 0.931 px/frame^2, step reaches zero at frame 0.48, v24 = 21.89 px/frame.
- Zero-step at frame ≈ 0.5 means uniform acceleration from rest at t = 0: step(i) = a (i - 0.5).
  Hence v(1 s) = a (24 - 0.5)/24 = 2.639 x 0.97917 = 2.584 m/s.

## Second route / check
Linear fits of the steps over different windows (fit_steps.py): 7-47 -> 2.586, 13-47 -> 2.599, 22-47 -> 2.560,
7-30 -> 2.603, 30-47 -> 2.710 (short window, less leverage). Quadratic fits of the record: 2.54-2.64 for most windows.
All consistent with the from-rest model 2.584.

Answer: 2.584 m/s. Confidence high (~±2 %).
