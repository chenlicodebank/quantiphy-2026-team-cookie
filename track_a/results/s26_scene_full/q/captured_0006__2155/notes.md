# q 2155 — toy speed at first desk impact (captured_0006)

File fps = question fps = 24. f = 0.5959*1280 = 762.8 px, principal point (640,360).

- Track: scene/tracks/toy.csv, verified visually (frames/flight.png, view.py): the toy is in flight f23–f31, first touches the desk at f32 (squashed on the front edge), then bounces.
- Depth: depth_info gives Euclidean distances 1.402 m at f24 and 1.065 m at f29. Converted to Z (1.346, 1.046) along each pixel ray; Z assumed linear in time (ballistic, so constant velocity toward the camera, -1.44 m/s), extrapolated to f32 (Z≈0.866).
- 3D centres = back-projection of (cx,cy) with that Z (fit.py).
- Check: a quadratic fit to vertical Y over f24–f31 gives a = 8.85–9.0 m/s² (prior 9.8), so the depth model is consistent to within about 10%.
- Impact speed from the ballistic fit at contact (≈f31.8–32): 3.29–3.36 m/s (free fit), 3.35–3.53 m/s (with g forced to 9.8).
  Components: vy≈3.0, vz≈-1.44, vx≈-0.11 m/s.
- Finite differences (reference style): 29→30 2.50, 30→31 3.10, 31→32 2.72 m/s (the last one includes contact/deceleration and blur).
- Answer: 3.2 m/s, between the physical ballistic value (~3.3) and the last finite differences (2.7–3.1).
- Confidence: moderate (±10%). Depth past f29 is extrapolated, and the reference's smoothing near impact is unknown.
