# q 939 – speed of the spacecraft (the black snowmobile-like vehicle) at 0.5 s

2D top-down render, 24 fps (file fps = question fps, so no re-timing). Only one moving object; prior: acceleration at 1.0 s = 4 m/s^2.

## Method (fit.py)
- Used scene/tracks/snowmobile.csv (bbox centre, rear edge and front edge; frames 2-60 have the whole vehicle in view).
- Quadratic fits x(t) for several windows (2-60, 2-30, 30-60, 5-45, 2-20) and three reference points:
  pixel acceleration -502 to -537 px/s^2 (centre: -513, residual 0.5 px); the acceleration is constant, so a(1.0 s) = a everywhere.
  Rest time t0 ≈ 0.004 s, i.e. it starts from rest at t ≈ 0.
- Scale: 4 m/s^2 / 513 px/s^2 = 0.0078 m/px. The scale cancels: v = a·(time since start).

## Result
- Analytic speed at 0.5 s: 4·(0.5 − 0.004) ≈ 1.98 m/s.
- Benchmark convention (backward difference, frames 11→12): 4·(0.5 − 1/48 − 0.004) ≈ 1.90–1.92 m/s.
  Raw step 11→12 = 10 px → 240 px/s → 1.87 m/s (±0.5 px noise per step).
- Answer 1.95 m/s, between the two readings (each within about 3 %).

## Check
- Rear-edge and front-edge fits give the same t0 and pixel acceleration to within ±2 %, so the speed is the same.
Confidence: high (±3 %).
