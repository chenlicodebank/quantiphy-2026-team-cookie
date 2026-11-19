# q966 — speed of the phoenix at 0.5 s (m/s)

Prior: acceleration at 2.0 s = 2 m/s^2. 2D video, no depth_info. fps = question_fps = 24, so no re-timing.

## Method
- I re-tracked the head with half-resolution template matching (rolling template, sub-pixel peak). Scripts are
  `tm.py` (writes head_tm.csv) and `seg.py`. `fit.py` checks the head_x track from scene/.
- The per-frame head speed comes in plateaus, with a wing-beat ripple on top: about 6.2 px/frame over frames 2-21,
  18.4 over frames 29-47 and 30.8 over frames 55-71. The steps fall at about 1 s and 2 s, which looks like the root
  is keyed once per second with linear interpolation. The step size of about 12.3 px/frame per second matches a
  constant acceleration from rest of about 0.5 px/frame^2 (288 px/s^2), and each plateau is the mean speed over
  its second.
- Scale: 2 m/s^2 equals the pixel acceleration, so the answer is the ratio v(0.5 s)/a in seconds × 2 m/s^2.

## Results
- Plateau route: v1/a = 0.507 s, giving 1.01 m/s.
- Per-second displacement route (frames 0→24→48→71): 0.534 s, giving 1.07 m/s. The head bobs with the wing phase at
  the window ends, which biases this route.
- Global quadratic fit (with a poor fit, rms 12-16 px): about 1.06 m/s.
- Ideal model (uniform 2 m/s^2 from rest at t = 0): v(0.5) = 1.0 m/s. This is also the speed of segment 1 under
  piecewise-linear keys.

Answer: 1.0 m/s. Confidence: good (routes agree within about 7 %).
