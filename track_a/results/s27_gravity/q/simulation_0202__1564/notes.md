# Q1564 – speed of the magnifying glass at t = 0.25 s

- t = 0.25 s -> frame 6 (question_fps = file fps = 24). Speed = |p6 - p5| x 24.
- The glass falls freely from frame 0 to impact between f10 and f11 (scene record checked: bbox-centre track
  y = 19.5, 25.5, 42.5, 70.5, 109.5, 159, 218.5 ...), so frame 6 is in the prior's free-fall phase (g = 9.8 m/s^2).
- fit.py: 3D pinhole model — f0 point back-projected with the given depth 4.2401 m, vertical drop
  with g = 9.8, unknown focal f, camera pitch and release time t0, fitted to the image-y track f0-f10.
  * Analytic free fall: f = 2644 px, t0 = -0.047 frame, rms 0.17 px -> speed f6 = 2.265 m/s.
  * Bullet semi-implicit Euler (10 substeps/frame, release exactly at f0): f = 2640 px, rms 0.17 px -> 2.266 m/s.
  Both fit the track to 0.2 px; the first-frame drop (6 px vs 17, 28 px) confirms release from rest at ~frame 0.
- Checks: predicted range at f10 = 4.37 m, consistent with given 4.41 m at t = 0.5 s (glass on desk, slightly lower).
  Glass length 187 px x 4.24 / 2640 = 0.30 m (plausible magnifying glass). Horizontal drift (~2 px/frame)
  is negligible.
- Sensitivity: t0 in [-0.1, +0.05] frame gives 2.23-2.29 m/s.
- Answer: 2.266 m/s. Confidence high (±1-2 %).
