# Q1571 — speed of magnifying glass at t = 0.125 s (frame 3 at 24 fps; file fps also 24)

Method (fit.py): pinhole camera, principal point at image centre. The glass falls freely (|a| = 9.8 m/s^2, prior) over frames 0–11.
Model P(t) = P0 + V0 t + 0.5 g t^2 ĝ, where P0 is the back-projection of the frame-0 pixel at depth 4.2401 m, and ĝ = (0, cos θ, sin θ) in camera coordinates.
Fitted parameters: f, θ, V0. The fit uses pixel tracks of frames 0–11 plus the constraint depth(0.5 s) = 4.4097 m.
- bbox-centre track: f ≈ 2597 px (hFOV ≈ 44°), θ ≈ 15°, rms 0.3 px, depth at 0.5 s reproduced. |P3 − P2|·24 = 1.049 m/s.
- When V0 is forced parallel to gravity: 1.052 m/s.
- With the lens-centre track: 1.052–1.056. With the mask-centroid track: 1.058–1.061.

Second route: v ≈ g·(2.5/24 s) + V0 (≈0.03–0.06 m/s) ≈ 1.05–1.08 m/s, which agrees.
Plausibility: the glass is ~174 px long at ~4.4 m, so ~0.29 m, which is reasonable.

Answer: 1.05 m/s. Confidence high (±3 %).
