# Q1423 – trolley speed at t = 2 s

- File fps = question fps = 24; t = 2 s -> frame 48.
- Prior: constant acceleration a = 1.507 m/s^2 (the units in the prior read "m/s"; it is an acceleration).
- Track (scene/tracks/cart.csv, bbox_cx): fitting x = x0 + c (n - n0)^2 puts the start at n0 = 0.3-0.8 frames,
  so the cart is at rest at frame 0 and accelerates uniformly (pixel steps grow linearly; no stops or bounces).
- Convention: speed = one-frame backward difference x fps. With p(n) = a/2 (n/24)^2, the speed at frame 48 is
  a x 47.5/24 = **2.983 m/s** (a x t = 3.014 would be the instantaneous value).
- Second route (fit.py): a 3D pinhole check. Depths come from 1/bbox_h anchored to d(0) = 12.589. The focal length
  was solved from the distance travelled between frames 0 and 12, a/2 x 0.5^2 = 0.188 m (f ≈ 2670 px). That gives a
  speed of ≈ 3.06 m/s at frame 48, within 3 % of the answer. This route is rough because the depth comes from the
  bbox height and the origin's location on the cart is unknown.
- Confidence: high.
