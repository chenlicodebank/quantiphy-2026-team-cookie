# q 3214 – ball velocity at 3.0 s (prior: g = 9.8 m/s^2)

- Time base: file fps = question_fps = 30, so t = 3.0 s means frame 90. The ball is in free flight (released at frames 80–81,
  apex at frame 93, bounce at frame 114).
- Track: scene/tracks/ball.csv circle-fit centre. Checked visually at frame 90 (frames/f90.png): centre ≈ (674, 206). Correct.
- Scale from the prior: I fitted a quadratic to cy(t) for flight 1 (frames 81–113), which gives a_y = 3539 px/s^2 (raw)
  and 3546 px/s^2 (camera drift removed). The core frames 82–111 give 3545 and flight 2 (116–143) gives 3531/3558, so the
  results agree to within 0.5%.
  Scale = 9.8 / 3540 = 0.00277 m/px.
  Sanity check: ball diameter 85 px × 0.00277 = 0.235 m, close to a real basketball (0.24 m).
- Velocity, using the annotators' forward difference |p(91) − p(90)| × 30 = 968 px/s, so v = 2.68 m/s (raw and drift-removed
  give the same value).
- Second route: the parabola/linear fit at t = 3.0 s gives 2.67–2.70 m/s. The central difference gives 2.76 and the backward
  difference 2.85. The ball is slowing near the apex, so the difference schemes give different values.
- Answer: 2.68 m/s (forward-difference convention). Confidence: good. The main uncertainty is the difference convention
  (about ±3%).
