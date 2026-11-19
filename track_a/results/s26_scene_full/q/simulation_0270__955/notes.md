# Q955 — speed of the phoenix at 0.5 s (prior: acceleration at 2.0 s = 2 m/s^2)

The video is a 2D render at 24 fps (the file and the question both say 24). The phoenix flies right to left, speeding up.
The prior is an acceleration, so the answer only needs the ratio speed/acceleration, which can be read in pixels. No metric scale is needed.

Method (fit.py): I fitted a quadratic x(frame) to scene/tracks/phoenix.csv over several frame windows, using several
reference points: body_s_x (smoothed torso), head_x (NCC head track, ok frames only), the mask centroid and the bbox left edge.
- Acceleration is close to constant: about -0.49 to -0.53 px/frame^2 for every point and window.
  The residuals are 10-18 px and come from the wing-beat bob. A cubic term is negligible.
- The vertex (where the bird is at rest) falls at frame about 0 (range -0.7 to +1.2 for the reliable fits). The track also shows frames 0→1 almost unchanged.
  So the phoenix starts from rest at t = 0 and accelerates uniformly at a = 2 m/s^2.
- Speed at frame 12 (t = 0.5 s) under the backward-difference convention: v = a·(12 − 0.5)/24 = 0.958 m/s.
  Under the continuous form v = a·t it is 1.0 m/s. The fitted speed12/acc ratios, 0.43-0.51 s (most near 0.47-0.49), agree with this.
- The vertical bob (±30 px per wingbeat) is taken to be the flapping animation, not motion of the rig root, so it is left out.

Answer: 0.98 m/s, between 0.958 (frame-difference convention) and 1.0 (a·t). It is within about 2.5% of either.
Confidence: fairly high. The constant acceleration from rest is clear from every reference point tracked.
