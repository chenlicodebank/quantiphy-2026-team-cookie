# Q312 — height of the table (kitchen island), m

Prior: g = 9.8 m/s^2; no depth_info. question_fps = file fps = 120.

## Scale from gravity (fit.py, fit2.py)
The apple (scene/tracks/apple.csv, circle-fit centre, checked against the frame at t=1.6 s) rolls off the
left edge of the counter at frame ~141 and falls freely to the floor (impact between 191 and 192).
I left out frames 141–147 because the apple is still pivoting over the edge there.
- Quadratic fits of y(t): 148–191 -> 6387 px/s^2; 152–191 -> 6427; 155–191 -> 6459; 160–191 -> 6435.
- Linear fit of the per-frame dy over 148–191 -> 6409 px/s^2.
- Adopted a = 6420 ± 60 px/s^2, so the scale is 9.8/6420 = 1.527e-3 m/px.
- Early and late half-windows differ (6290 vs 6920), but this is within the noise from the ±1 px per-frame
  jitter, so I used the fits over the whole fall.

## Table height in pixels
Height = drop of the apple centre from rolling on the counter top to rolling on the floor. The radius is the
same in both places, so it cancels.
- Centre on the counter just before the edge (frames 136–140): y ≈ 1104.5.
- Centre rolling on the floor (frames 205–262, median): y = 1743.2.
- Drop = 638.7 px.
- The apparent radius is 30.2 px on the counter and 30.0 px on the floor. The depth is the same, so one scale
  applies, and the gravity fit covers the same image rows as the height.

## Result
638.7 px × 1.527e-3 m/px = 0.975 m. The range across the fits is 0.969–0.980 m.

## Checks
- Plausibility: a kitchen island at 0.97 m is realistic.
- Apple diameter: 61 px × 1.527e-3 = 9.3 cm, a plausible large apple.
- Second route, the quadratic extrapolation: the fit gives y at frame 141 of 1107–1110, which is consistent with
  the counter level of 1104–1106. A different reference level would change the answer by less than 1%.

Confidence: good (about ±3%).
