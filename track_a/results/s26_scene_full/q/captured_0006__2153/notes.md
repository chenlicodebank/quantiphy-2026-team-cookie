# q2153 — speed of the toy at t = 1.2 s (frame 29 at 24 fps; the file is also 24 fps)

Data: scene/tracks/toy.csv full-mask centres for flight frames f23–f31 (release ≈ f22, table impact f32).
I checked the track: the toy is in free flight from f23 to f31, with motion blur in f28–f31.
Camera: f = 0.5959·1280 = 762.8 px, principal point (640, 360).
depth_info: f24 is 1.402 m away, f29 is 1.065 m away.

## Method (fit.py, tilt.py)
I fit a 3D ballistic model, P(t) = P0 + V0·t + ½·g·t² with |g| = 9.8 (the prior), to the pixel centres
of f23–f31 and to the two given camera distances.
- If the camera tilt is a free parameter, the best fit is −18° (rms 1.9 px). That gives an instantaneous
  speed of 2.63 m/s, a forward difference f29→30 of 2.82 m/s, and a mean over f27–31 of 2.64 m/s.
- The table's side edges meet at a vanishing point near (650, 357), which is about the principal point.
  So the camera pitch is about 0° and gravity runs along the camera's y axis. With tilt = 0 the fit has
  rms 2.7 px, depth residuals under 1 cm, an instantaneous speed of 2.43 m/s, a forward difference
  f29→30 of 2.60 m/s, and a mean over f27–31 of 2.45 m/s.
- Back-projecting the tracked centres with the fitted distance gives frame-to-frame speeds of
  2.14, 2.40, 2.76 and 3.30 m/s for f27→31 (free-tilt fit).

## Answer
2.5 m/s. This is the tilt-0 fit, with the instantaneous and smoothed values (2.43–2.60) taken together.
Sensitivity: tilt between −18° and +10° gives 2.3–2.8 m/s.
Check: going down, the vertical speed is about 9.8·(4/24) ≈ 1.6 m/s after the apex at f25. The speed
toward the camera is about 1.1–1.6 m/s. Together that is about 2.2–2.4 m/s, which is consistent.
Confidence: moderate, about ±10%.
