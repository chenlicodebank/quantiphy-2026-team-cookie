# q_3244 – velocity of the acorn at 2.00 s

Prior: acceleration 2.00–2.30 s = 0.77 m/s^2. 2D internet clip at 30 fps (file and question agree). t=2.00 s is frame 60 and t=2.30 s is frame 69.

## Method
- Reference point: the acorn's stem knob x. It is the sharpest horizontal marker; the bbox centre jitters by tens of px because of motion blur. Motion is horizontal (y constant).
- Velocity is the forward difference v(i) = (x(i+1) - x(i)) x 30. Acceleration over the window is (v(69) - v(60)) / 0.3 s, which equals the mean of the second differences.
- Scale: one metres-per-pixel factor = 0.77 / pixel acceleration, so the answer = 0.77 x v_px(60) / a_px.

## Measurements (calc.py, stem.py)
- Record, ref-stabilised stem x: v60 = 2712 px/s, a = 3660 px/s^2, giving 0.571 m/s (scale 2.10e-4 m/px).
- Record, raw stem x: 2727 px/s and 3840 px/s^2, giving 0.547 m/s.
- Second route: my own stem tracking (dark-pixel centroid in the stem band, stem.py, raw frames): 2758 px/s and 3699 px/s^2, giving 0.574 m/s. Agrees with the record within 1–6 px.
- Fits for comparison: a linear fit of v over frames 60–69 gives 0.59. A quadratic fit of position over 59–71 gives 0.51–0.55. The bbox centre gives 0.37–0.45 (blur-noisy, rejected).
- The camera drift over the passage is about 2 px in x, so it is negligible.

Answer: 0.57 m/s. Confidence: moderate, about ±5–8 %, because the result depends on the noisy per-frame second difference.
