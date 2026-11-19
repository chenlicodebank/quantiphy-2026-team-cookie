# q_2529 — tennis ball velocity at t=1.6 s (cm/s)

- Tennis ball = yellow_ball in scene/. t=1.6 s at question_fps 24 -> frame 38 (file fps is also 24). The ball is still rolling
  on the table (it drops off at frame 42), so the fit window 28–41 contains no impact.
- Re-measured the centre and diameter for frames 20–42 (`measure.py`): HSV mask, then a circle fit to the contour without the
  bottom 90° wedge, which has reflections. The results agree with scene/tracks/yellow_ball.csv to about 1 px.
  Frame 38: centre (739.8, 452.9), diameter 53.3 px (the record gives 55).
- Lab method: f = 0.5959*1280 = 763 px, principal point (640,360). Depth at frame 38 = 1.19 m (depth_info). The depth in other
  frames is taken from the apparent-size ratio: Z(i) = 1.19 * d(38)/d(i), using a smoothed fit of 1/d. Back-projection:
  ((u-cx)/f, (v-cy)/f, 1)*Z.
- Velocity = |P(39)-P(38)|*24, with u, v and 1/d smoothed by a linear or quadratic polynomial fit over 28–41, 30–41, 33–41 or 34–41
  (`velocity.py`). I computed it from my measurements, from the record's measurements and from their average.
  Results: 74–78 cm/s with the wide windows, and 67–79 with the short quadratic windows (noisier).
  Forward, backward and central differences agree to within about 1 cm/s for the wide windows. Most of the speed comes
  from motion in depth.
- Note: the size prior gives a different depth. 763*0.067/53.3 = 0.96 m, against the given 1.19 m. If the size depth were
  used, every component would scale by 0.81 and the speed would be about 61 cm/s. The reference positions use the measured
  depth, so I scaled by depth_info.
- Answer: 75.5 cm/s. Confidence: moderate (±5–8%). The depth rate depends on the diameter growth and is the main uncertainty.
