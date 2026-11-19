# q935 — speed of the spacecraft at 0.5 s (prior: acceleration at 1.0 s = 4 m/s^2)

- 2D top-down render, 24 fps (file fps = question_fps; no retiming). The only moving object (the record calls it a
  "vehicle") is the spacecraft. It moves straight in -x from rest.
- fit.py: quadratic fits of x(frame) over frames 7–50 for three points:
  - bbox centre: a = 1.205 px/frame², rest at frame 0.015, max residual 0.7 px
  - nose: a = 1.228, rest at frame -0.002
  - tail: a = 1.181, rest at frame 0.026
  The cubic terms are negligible, so the acceleration is constant and the motion starts at frame 0.
- Scale: 4 m/s² = a_px·24² · s, so s ≈ 4/694 m/px. Speed at frame 12 (backward difference) = step(12)·24·s.
  - Centre: 1.914 m/s. Nose: 1.917 m/s. Tail: 1.912 m/s.
  - Analytic: constant a starting at rest at frame 0 gives v_bd(12) = a·11.5/24 = 4·11.5/24 = 1.917 m/s.
- This result does not depend on the scale: it is the ratio of the step to the acceleration.
- The instantaneous speed a·t would be 2.0 m/s (4 % higher). The paper's convention is the backward difference, so the
  answer is **1.917 m/s**.
- Confidence: high.
