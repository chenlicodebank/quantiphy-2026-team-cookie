# q_2201: ball acceleration at t = 0.3 s (frame 7 at 24 fps; the file is also 24 fps)

The object is a pendulum: a red ball swinging mostly toward and away from the camera. At f7 it is about halfway
between the far turning point (f3) and the bottom of the swing.

## Method
- Track: scene/tracks/ball.csv (centroid u,v and equivalent diameter). I checked it against the residuals.
  There is a glitch or dropped frame at f35/36, which is far from f7.
- Direct route (m.py): back-project with depth from the ball size (d = K/diam, K = 51.1 calibrated on depth_info),
  f = 763. The size-based depth is too noisy (±5 %) for a second difference. Smoothed estimates of |a| at f7 range
  from 1.5 to 6, so this route is unreliable and I did not use it for the answer.
- Model route (fit.py): a 3D pendulum (pivot, length L, swing-plane yaw, camera pitch, amplitude, phase, light damping;
  exact nonlinear ODE). It is fit jointly to u, v, the 6 depth_info distances and the ball diameter.
  - Free L: L = 0.250 m, implied g = 7.5. Fixing g = 9.8 (the prior): L = 0.335 m, with a similar fit quality
    (rms u 2.5 px, v 1.1 px on f0–30; depth residuals ≤ 0.06 m). The fitted ball diameter is 6.7 cm.
  - At f7 with g = 9.8 (fit on f0–30): θ = 0.49 rad, speed 1.05 m/s, tangential a = 4.5, centripetal a = 3.3,
    |a| = 5.6 m/s². The full-clip fit gives |a| = 5.77 m/s², and the free-L fit gives 5.42 m/s².
  - Reference-style discrete second difference of the model positions: unsmoothed |A| = 5.6–5.7; with a
    3/5/7-frame moving average, 5.4 / 4.95 / 4.3. The change of scalar speed (tangential only) is ≈ 4.1–4.6.

## Answer
|a| ≈ 5.4 m/s². This is the magnitude of the acceleration vector. I chose a value between the instantaneous model
value (5.6) and the value after the 5-frame smoothing the reference uses (≈ 4.9).
Confidence: moderate. The main uncertainty is the reference's smoothing and whether it takes the vector magnitude
or the tangential (speed-change) component (≈ 4.5).
