# q_2860 – velocity of the green ball at 1.0 s (frame 24, question_fps = file fps = 24)

## Identification
- green ball = the small yellow-green (tennis) ball, `yellow_ball` in scene/. At f24 it is just leaving the standing
  person's right hand at (600, 292) px. The "white ball" (3.0735 m) is the pale small ball (`pink_ball`, (569, 271)),
  not the soccer ball, which sits next to the crouching person (~2.4 m) and doesn't fit 3.07 m.
- orange ball = basketball (prior object).

## Measurements (seg2.py, ufit.py, ballistic2.py, orange_check.py)
- I re-segmented both small balls as the full non-green blob (seg2.py; masks in frames/yellow_fg.png and pink_fg.png),
  frames 24-36. Free flight lasts until the bounce at about f37.
- Camera: f = 762.8 px, principal point (640, 360). Z0 at f24 = 3.039 m along the ray (Z = 3.023).
- Route A (no gravity, ufit.py): I assume no camera roll, so motion along camera x has no acceleration and
  u(t) = cx + f(X0 + Vx t)/(Z0 + Vz t). Fitting u over f25-35 gives Vz/Z0 = -0.567 ± 0.015 and Vx/Z0. The given
  distance sets the scale. The vertical motion comes from v(t)·Z(t)/f with a quadratic fit.
  Result: V24 = (-1.09, -0.60, -1.71) m/s, |V| = 2.12 m/s. The forward difference |P25-P24|·24 = 2.07 and the
  backward difference = 2.18. With other frame windows, |V| = 1.96-2.11.
- Route B (3D ballistic fit, ballistic2.py): the start point is fixed by the given distance, the pitch is fixed at
  2.5° (from the plane the basketball rolls on) and effective g is left free. The fit gives |V24| = 2.20 and a
  forward difference of 2.15 (rms 0.37 px, g_eff = 8.75).
  With g fixed at 9.81, the fit puts both small balls 15-20 % farther away than the given distances. The same
  mismatch shows up for the white ball, so I trust the given depths and the gravity-free route.
- Check on the white ball (Route A): |V| is 2.08-2.33, and its fitted X0/Z0 matches the measured f24 position.
  The model is consistent.
- Prior check (orange_check.py): a basketball depth model from apparent size reproduces the given 1.81 m at
  t = 1.0 to within 2 % (I get 1.85). Its smooth 3D speed is about 1.55-1.7 m/s. Only the jump from f11 to f12
  (2.3 m/s, probably a dropped frame or the release) reaches the prior's 2.21. So the reference's
  differencing/smoothing is noisy and can't be reproduced exactly. I did not rescale anything.

## Answer
Over the routes and windows, the green ball's speed at f24 is 2.0-2.2 m/s, with a central value of **2.1 m/s**.
The 5-frame mean of the model speeds over f24-28 is also about 2.1.
Confidence: moderate, about ±8 %. Most of the uncertainty is in the depth-rate component (about 1.7 m/s toward the camera).
