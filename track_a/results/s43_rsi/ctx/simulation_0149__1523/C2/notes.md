# Q1523: acceleration of the car at t = 0.5 s (frame 12, question_fps = file fps = 24)

Answer: **10.1 m/s²**

## Method
- **Wheel tracking.** I tracked the right front wheel (the near-side "front" rim; at t=0 it is the white rim at x≈68)
  over frames 0-28, and the rear rim over frames 16-32. For each image column I found the bright, low-saturation rim
  run through the hub row, with half-level subpixel ends (`rims2.py`, `tracks.py`). This gave the rim's vertical
  extent h and its centre u.
  - The record is wrong for frames 10-16: its rim heights (54→107 px, "partly hidden") are not right. The rim is
    fully visible there. Measured h: 87.8 (f0) → 99.9 (f12) → 167.8 (f28).
- **Camera.** The hubs sit on the horizon (v≈829). The big-pillar edges are exactly vertical (dx/dy ≈ 0), so
  there is no pitch: the principal point is at y≈829 through lens shift, and cx is taken as 960.
- **Focal length from orthogonal vanishing points** (`vp_fit.py`):
  - Ceiling tubes and pipes: VP1 at u≈4050 (record: 4050; my B1 pipe fit: 4046).
  - The perpendicular red pipes: A1 at -912, A3 at -895, A2 at -1036 (short line).
  - f² = (4050-960)(960+920) → **f ≈ 2410 px** (range 2400-2480).
- **Scale.**
  - The depth_info distance (14.244 m to the right front tyre at t=0, Euclidean) converts to an axial depth of
    13.357 m, so the rim diameter is 13.357 × 87.8 / 2410 = 0.487 m.
  - Check against the prior: tyre/rim = 0.764 / 0.487 = 1.570. Measured from tyre edges in frames 0-12 it is
    1.57-1.60 (`tire_prof.py`), so the prior, depth_info and f agree.
- **Trajectory.**
  - Depth z = z0·h0/h and X = (u-cx)·z/f. The hub paths are straight lines (perpendicular RMS 1.7 cm front,
    0.9 cm rear; heading about 54°). The front-to-rear rim vector stays constant in 3D, so the car translates
    with no yaw: every point, including the origin, has the same speed.
  - Position along the line comes from intersecting each frame's rim-centre viewing ray with the fitted line
    (`traj_line.py`). This is far less noisy than the size-based depth.
- **Speeds** (backward differences, m/s): f8 4.84, f9 5.20, f10 5.75, f11 6.18, f12 6.47, f13 6.92, f14 7.48,
  f15 7.61, f16 8.13. The motion is an ease-in from rest at f0 to a plateau of about 9.85 m/s by f26-32.
  Acceleration falls steadily over time; it is not constant.

## Acceleration at frame 12
- Cubic and quartic fits of s(t) over frames 0-24, 4-20 and 6-18 give a(0.5 s) = 9.6-9.8 instantaneous.
- The reference convention, (speed12 - speed11) × fps on the fitted curve (centred at frame 11), gives 10.0-10.4.
- Quadratic fits over short windows give 9.6-9.7.
- f from 2330 to 2490 changes the result by about ±1%.
- The raw one-frame difference is noisy (7.1), so I didn't use it.

## Second route
- A linear fit of the measured speeds over frames 8-16 gives 0.41 m/s per frame = 9.9 m/s².
- The rear-wheel speeds over frames 16-20 match the front wheel's (8.6-8.9 m/s).

## Confidence
Moderate to good, about ±6%. The main uncertainties are the convention (frame 11 vs 12 centring, 9.7 vs 10.3)
and the vanishing-point f, which the tyre/rim ratio confirms.
