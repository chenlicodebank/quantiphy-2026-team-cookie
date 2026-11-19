# q_1548 — speed of the turtle at t = 1.5 s (simulation_0159)

File fps = question_fps = 24, so t = 1.5 s is frame 36.

## Data used
- Prior: the turtle's acceleration is 2.639 m/s² (exact).
- depth_info for the turtle: 15.232 m at t = 0 and 14.968 m at t = 0.5 s. The turtle comes slightly toward the camera.
- Pixel tracks, with the turtle swimming right to left:
  - scene/ core centroid and full-mask centroid (re-checked against the frames);
  - my own chained, scale-aware template track of a fixed point on the shell (`chain.py`, saved as `chain_shell.json`). Its fit residual is about 1.7 px. Overlay: `frames/pts_shell.png`.

## Method (`fit3d.py`)
I modelled the turtle as moving in a straight line with constant acceleration:
- P(t) = P0 + d·s(t), with s(t) = v0·t + a·t²/2 and a = 2.639.
- P0 is the back-projected pixel position at the t = 0 depth (15.232 m).

The free parameters are the focal length f, the start pixel, the direction d and v0. They were fitted to the full 41-frame pixel track, with the constraint |P(0.5)| = 14.968.

| Track | f (px) | v0 (m/s) | depth at f40 (m) |
|---|---|---|---|
| core centroid | 2071 | 0.000 (at the bound) | 12.97 |
| mask centroid | 2348 | 0.000 (at the bound) | 12.57 |
| shell chain | 2505 | 0.092 | 12.40 |

When v0 is fixed at 0, the shell-chain fit's residual rises only slightly, from 1.67 to 1.87 px. Plain quadratic fits of the pixel x track give the same picture: the image velocity is close to zero at t ≈ 0–0.1 s. So the turtle starts from (nearly) rest at t = 0, and its speed is v(t) = v0 + a·t.

The fitted f values give a horizontal field of view of about 42–50°, which is plausible.

## Answer
- The analytic speed at 1.5 s is 3.958 m/s with v0 = 0, or 4.05 m/s with v0 = 0.09.
- The benchmark convention is a one-frame backward difference at frame 36: |p36 − p35|·24 = a·35.5/24 + v0 = 3.904 m/s with v0 = 0.
- I answer **3.93 m/s**, between these values: within 1.5% of both v0 = 0 readings and within 3% of the v0 = 0.09 reading.

## Second-route check
The three pixel tracks are independent, and they give the same picture: v0 is between 0 and 0.09 m/s. The pixel-only quadratic fits agree with this.

## Confidence
High. The answer depends mainly on the prior and on the start-from-rest finding; the focal length cancels out.
