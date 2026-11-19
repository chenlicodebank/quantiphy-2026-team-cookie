# q202 — speed of the shark at t = 0.0 s (prior: shark acceleration = 1 m/s^2)

fps = question_fps = 24, no re-timing issue. 2D scene, static camera.

Method (fit.py): quadratic fit x(frame) to the shark track in scene/tracks/shark.csv (frames 1–53 and 2–53;
frame 0 equals frame 1, motion starts after frame 1). Uniform acceleration in px: a ≈ 0.150 px/frame^2
(= 86.4 px/s^2). Scale from prior: 1 m/s^2 ↔ a_px, so speed in m/s = v_px / a_px (s), independent of the
absolute scale.

Results (v/a in seconds = speed in m/s):
- centroid cx: v(0)/a = 1.95, v(1)/a = 2.00 (rms resid 0.47 px)
- bbox centre: 1.99 / 2.03
- nose edge x0: 1.98 / 2.03; tail edge x1: 2.00 / 2.04
Second route: independent reference points (nose edge, tail edge, centroid, bbox centre) all give 1.95–2.04.

Answer: initial speed 2.0 m/s (consistent with a clean simulation setup v0 = 2 m/s, a = 1 m/s^2).
Confidence: high (~±3%).
