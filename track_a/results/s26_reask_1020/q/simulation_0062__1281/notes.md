# q1281 – width of the lane (road surface, curb to curb)

File fps = question fps = 24. t=0.58 s -> f14, t=1.58 s -> f38.

## Scale
- White van (prior: a = 4 m/s^2) moves at constant depth parallel to the image plane. A quadratic fit to its x track
  gives 0.534 px/frame^2 (fits f2-71, f22-71 and f10-60 all agree within 0.5 %), i.e. 307.6 px/s^2.
  So s = 0.01300 m/px at the van's depth (`van_acc.py`).
- depth_info for the van: Z = sqrt(d^2 - s^2 r^2) gives 29.158 m (f14) and 29.167 m (f38). The two agree, which checks s.
  That gives f = Z/s ≈ 2243 px (HFOV ≈ 51°).
- Checks: van 5.9 m long and 2.1 m tall (Chevy Express); pedestrian 1.83 m tall at both depth times; cyclist 5.1 m/s.
- Horizon / vanishing point from the two receding curb lines: (1078.7, 538.5).
- Camera height H from ground contacts and depths: cyclist tyres at y=620, Z=27.0 -> 0.98 m; van near tyres at y=615.5
  (Z ≈ 29.16 minus about 0.6–0.85 m) -> 0.96–0.97 m; pedestrian lowest foot -> 1.01 m (biased high because the front
  foot is nearer than the pelvis). Adopted H = 0.975 ± 0.015 m.

## Road widths (`curbs.py`, `cross.py`, `curbface.py`, on frame 0)
- Receding street (the camera looks down it; the taxi ends on it): road-level curb edges lie on lines through the
  vanishing point. The ground lateral offsets X/H = (u-cx)/(v-cy) are -3.85 (left) and +7.57 (right), so
  width = 11.42 H ≈ **11.1 m**. This route does not depend on f.
- Cross street (the van and cyclist ride on it; the taxi starts on it): the far curb's road edge is at y=603.5. The
  near sidewalk's curb top is at y=633. The curb is about 0.05 m high, measured from the curb-face pixel heights.
  Z_far = fH/65 = 33.6 m and Z_near = f(H-0.05)/94.5 = 21.95 m, so width ≈ **11.7 m**.
- The two routes differ by 5 %, which is within the horizon and H uncertainty, so this is probably the same road
  width. Answer: the mean, **11.4 m**, which is within 3 % of both.

Confidence: moderate (±5 %). The main uncertainties are which road is meant, and H.
