# q_1857: acceleration of the blue car at t = 1.5 s

Time base: the file and the question both use 24 fps. t = 1.5 s is frame 36. a(36) = v(36) - v(35) in px/frame²,
which is x36 - 2·x35 + x34.

Scene: a 2D side view of a light-blue cart on a white background, with a static camera. The hub and ground-contact
y-values stay constant (±0.3 px) and the tyre's pixel diameter does not change across frames 30–41, so the cart moves
at constant depth. I used one planar scale.

## Scale (prior: tyre diameter = 0.369 m)
I fitted circles to the tyre/background boundary seen from the hub (`tyre_fit.py`):
- Frames 30–39, both tyres: D = 108.8–110.6 px.
- Rear tyre at frame 36: 110.0 px. This holds for mask thresholds 200, 230 and 245.
- At threshold 128 the front-tyre fit picks up the dark tread side and grows to about 113 px (sd 1.3), so I rejected it.

I used D = 110 px, so the scale is 0.369 / 110 = 3.355e-3 m/px. The record gave ≈112 px. That came from a cruder
extent measure, and my fits supersede it.

## Acceleration
I used the drift-free template tracks in scene/tracks/cart.csv: marker, front hub, rear hub and wheel midpoint.
- Raw second differences are noisy (±0.1–0.2 px). At frame 36 they read −0.53 to −0.63.
- Route 1 (`accel.py`, `global_fit.py`): global polynomial fits (degree 3–5) over frames 11/17/20–41. They reach
  0.04–0.17 px rms and give a(36) = −0.614 to −0.635 px/f² for all four tracks.
- Route 2: Blender's default Bezier ease between two keys, x = x0 + Δ(3s² − 2s³) with s = (t − t0)/T, fitted to the
  marker track. The best fit has t0 = 0.0 and T = 59 frames, with 0.05 px rms error. It gives a(36) = −0.634 px/f².
  - The same model matches the early chained shifts: v(1) ≈ 1.5 px/f and an initial acceleration of about 3.4 px/f².
  - Peak speed is at frame 29.5. After that the cart decelerates with a linearly growing deceleration.
- Local quadratic fits (constant-acceleration models) give −0.73 to −0.77 px/f². I rejected them because the
  acceleration changes linearly in time (constant jerk), so a quadratic fit reads it at the wrong frame.

a = 0.634 px/f² × 24² × 3.355e-3 m/px = 1.225 m/s². This is a deceleration; the answer is reported as its magnitude.

Confidence: medium-high. The pixel acceleration is consistent across all tracks to within ±2 %. The scale is
uncertain by about ±1 % from the tyre-edge definition.
