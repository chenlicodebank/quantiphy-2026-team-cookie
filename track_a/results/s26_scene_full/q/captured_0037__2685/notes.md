# q2685: ping pong ball velocity at t = 1.0 s (cm/s)

File fps = question fps = 24, so t = 1.0 s is frame 24. At that point the ball is at the apex of its 2nd arc (between the bounce
behind the card tent at f19-20 and the bounce in front of the tape roll at f28). Frames 21-27 are clean free flight.
f = 0.5959 x 1280 = 763 px, principal point (640, 360). Given range at t = 1.0 is 1.055 m. The ball is at (638.9, 347.6) px, so Z = 1.0549 m.

## Measurements (measure.py -> meas.json, velocity.py)
- I re-measured the centroids as brightness-weighted centroids of the background-difference mask (they agree with scene/ within about 1-2 px).
- A quadratic fit of u(t) and v(t) over frames 21-27 at t = 1.0 gives u' = -304 px/s and v' of about +40 px/s. That is a lateral speed of
  vx = -0.417 m/s and vy = +0.057 m/s.
- Depth rate Z' (this dominates the answer):
  (a) Perspective: near the image centre u'' = -2 u' Z'/Z. With u'' = -316 px/s², Z' = -0.548 m/s. Arcs 1 and 3 give the same
      ratio (Z'/Z of about -0.52 to -0.75 per s).
  (b) Apparent size: the mean mask width per arc is 22.1, 26.1 and 30.8 px for arcs 1-3. Scaling to Z = 1.055 at arc 2 gives Z of about
      1.24, 1.055 and 0.89 m, so Z' = -0.540 m/s.
  (c) Occlusion check: at f19-20 the ball passes behind the card tent (0.905 m), so it is farther away. At f28 it is drawn in front
      of the tape roll (1.038 m) and at f36 in front of the glass jar (1.008 m). This agrees with the ball approaching the camera.
- The 3D velocity at t = 1.0 is about (-0.417, 0.057, -0.544) m/s, so |v| = 0.688 m/s. The 5-frame smoothed slope gives 68.8 cm/s and the
  central difference gives 68.9 cm/s. The raw one-frame forward difference is 71.4 cm/s.
- Without the depth change, |v| would be only 42.3 cm/s. The answer therefore depends on Z', which two independent methods put at -0.54 to -0.55 m/s.
- Scale check: the mask width at f24 (24.4 px) x 1.055 / 763 = 3.4 cm, against a 4 cm prior. The mask runs about 10-15 % small
  (half-intensity edge). This affects only the size ratios, not the scale.

The gravity-curvature depth estimate (f·g/v'') is not usable here: it gives inconsistent values between arcs, probably because of spin/Magnus effects on the light ball.

Answer: 69 cm/s. Confidence: moderate. The main uncertainty is the depth rate, about ±15 %, which maps to about ±8 % in the answer.
