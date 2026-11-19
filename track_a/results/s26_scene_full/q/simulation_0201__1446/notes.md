# Q1446 — speed of the droplet at t = 0.05 s (m/s)

Prior: droplet acceleration = 9.7 m/s². depth_info: |cam→drop| = 0.156 m at t=0 (frame 0), 0.186 m at t=0.1 s (frame 6).
question_fps = file fps = 60 → t = 0.05 s is frame 3; speed = |p3 − p2| × 60.

## Measurements
- `measure.py`: re-segmented the drop (difference to frame 13, drop absent; thresholds 10/15/25) — centroids agree
  with scene/tracks/drop.csv to <1 px for frames 0–7 (threshold-sensitive only in frames 8–9). Used threshold 15.
- `fit3d.py`: 3D free-fall model P(t) = P0 + v0 t + ½ a t², |a| = 9.7 (direction free), pinhole camera with unknown f,
  principal point at image centre; fitted to the pixel centroids (σ 2 px) and the two given distances.
  Results: f ≈ 3900 px (hfov ≈ 36°), both given distances reproduced exactly, pixel residuals < 1 px,
  fitted v0 ≈ 0.02 m/s (≈ at rest at frame 0, consistent with pinch-off at frame 0); drop width ≈ 4.8 mm (plausible).
- Speed at frame 3 (backward difference): 0.397–0.404 (frames 0–9, 1–9, 1–7, with and without v0=0); 0.416 for frames 0–6 only.

## Second route
Release from rest at frame 0 with constant a = 9.7: p3 − p2 = ½a(3² − 2²)/60² → speed = 9.7 × 2.5/60 = 0.404 m/s,
matching the geometric fit. (A width-based depth route was tried in fit.py but the drop's apparent width shrinks faster
than free fall permits in late frames — low contrast — so it was not used.)

## Answer
0.402 m/s (confidence high; ±3%).
