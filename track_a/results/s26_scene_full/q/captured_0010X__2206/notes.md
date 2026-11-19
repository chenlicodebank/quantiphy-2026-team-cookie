# q_2206 — ball (pendulum bob) speed at t = 0.6 s (frame 14 at 24 fps; file fps is also 24)

**Setup.** Lab clip, f = 0.5959·1280 = 763 px, principal point (640, 360). The ball is a pendulum bob swinging mostly
along the line of sight. The given depths are at frames 7, 14, 22, 29, 36, 43. Ball centroids come from
scene/tracks/ball.csv. I checked frame 14 visually: the centroid is at about (680, 386) and sits on the ball.

**Why not use the per-frame data directly.**
- Solving the ray–sphere intersection (pivot plus string length, fitted to the given depths; `measure.py`) gives two
  solutions per frame. Near the bottom of the swing these come close together, so the depth jumps between branches.
- Depth from the apparent diameter (`route2.py`) is too noisy: the mask changes from red to pale at frame 12, and
  the diameter jumps from 35 to 40 px. This route gives 1.4–1.5 m/s, which is unphysical. I rejected it.

**Main route (`fit_pend.py`).** I fitted a damped 3D pendulum to all 49 image centroids, the 6 given depths and a weak
diameter-depth term. The model has pivot position, string length L, swing azimuth, camera pitch and roll, amplitude,
ω, phase and damping. Fit variants:
- pivot fixed or free;
- with or without the constraint ω = √(g/L)·(1 + A²/16), with g = 9.8;
- given depths soft (σ = 1 cm) or hard (σ = 2 mm).

Across the variants: period ≈ 29 frames, amplitude ≈ 0.68–0.83 rad, L ≈ 0.32–0.43 m. The near turning point is at
frame ≈ 17.2, and image residuals are about 3 px rms. The given depths are reproduced to within 0.5–4 cm.

Speed near frame 14 (m/s), over all variants:

| Measure | Speed (m/s) |
|---|---|
| Instantaneous at frame 14 | 0.91–1.02 |
| Forward difference, frames 14→15 | 0.79–0.89 |
| Positions smoothed over 5 frames, then forward difference | 0.74–0.84 |
| Mean of forward speeds over frames 12–16 | 0.75–0.84 |

**Second check (energy with the g prior).** v = √(2gL(cos θ14 − cos θturn)) gives 0.92 m/s for both the free-g
and g-constrained fits. This agrees with the instantaneous model speed.

**Answer: 0.84 m/s.** The reference convention is a forward difference smoothed over at least 5 frames, which gives
0.75–0.87. The instantaneous speed is about 0.92. I chose 0.84 between the two. Confidence: moderate, about ±10%.
The ball is only 3 frames before its turning point, so the result depends strongly on the smoothing and difference
convention.
