# Q1211 – height of the fire hydrant (m)

File fps 30.003, question_fps 30 (used for t->frame: t=1 s -> f30, t=2 s -> f60).

## Hydrant pixel height (hydrant.py)
Frame 0 (unoccluded; later the orange car covers it). Colour mask (warm white vs bluish wall) + column
profiles: cap top y≈663.5, base bottom y≈758 -> 94.5 px (record said 94). The front edge of the base sits ~1 px
low because it is closer to the camera, so the effective extent is ~94 px. Origin taken at the centre (135, 710).

## Scale (fit.py, solve.py)
- Orange car pixel acceleration: quadratic fit of hub-tracked ref_x (no extrapolated/interpolated frames),
  f6-80: 0.3346 px/frame² = 301.1 px/s² (f6-34: 0.3307, f46-80: 0.3375). Prior -2.86 m/s² ->
  s = Z_o/f = 0.009497 m/px at the car's depth (the motion is parallel to the image plane; the hub separation stays
  at 323 px throughout).
- Orange depths: D(f0)=17.26 at u=1343.7 (extrapolated), D(f30)=15.436 at u=621.3 -> Z_o ≈ 15.3 m. That gives
  f ≈ 1610 px (HFOV ≈ 37°). Solving cx from the two depths plus s gives cx = 525 (close to the centre, so consistent).
  Route B (two depths only, cx=540) gives s=0.009658, which agrees with the acceleration route to within 1.7%.
- Hydrant: D=17.737 at pixel offset (-405,+170) -> Z_h ≈ 17.12-17.15 m (lamps 17.33 / 17.18 -> hydrant slightly in
  front of the wall line, plausible).
- H = 94.5 * Z_h / f: route A (acc + depths) 1.005-1.011; A2 (acc, cx=540) 1.000-1.006; B (depths only) 1.018-1.025,
  for an origin row of 718-794.

## Second-route check: green car (green.py)
Using the two green-car depths (10.25 at f30, 12.768 at f60, with f60 extrapolated at -69.84 px/frame,
far off-screen) gives f ≈ 1750-1800 -> H ≈ 0.91-0.93. This disagrees with the orange car. If the green car's origin
sat ~90 px behind its wheelbase centre, it would match f≈1610. This check depends on extrapolating 11 frames
beyond the last measured hub and on where the root is, so I give it less weight. The orange-car value rests on the
exact prior and on D at f30, where the car is near the image centre. Two orange-car routes agree.

## Answer
H ≈ 1.005 m. Confidence moderate: ±2% within the orange-car routes; the green-car route would give ~0.92.
