# q21: length of the green car (m)

The "green car" is the record's `black_car`, a very dark green roadster with white bumpers in the right lane. The video is a 2D top-down view at 30 fps (file rate = question_fps). The camera is static.

## Scale from the prior (orange car acceleration = -2.86 m/s^2)
- `accel.py` uses the orange-car template track (`scene/tracks/orange_car.csv`, reliable frames). The per-frame speed is linear in time:
  - speed slope = -0.3475 px/frame^2 (f25-90, residual 0.11 px), which gives **-312.7 px/s^2**
  - from f17: -309.4
  - quadratic position fits: -303.7 (f20-50), -309.7 (f50-90), -313.0 (f20-90)
- Adopted -312.7 px/s^2, so the scale is 2.86 / 312.7 = **0.009146 m/px**.

## Green car pixel length
- The record's bbox length depends on y: it is 574 px near the top and bottom of the image and has a minimum of about 560 px near y ≈ 1150. The speed is constant, so this is perspective or a slight tilt, not blur. A fit of L = L0 + c·y + b·y² (`blurfit2.py`) gives a minimum of **559.6 px** (bbox_h minimum is 562).
- Motion blur check (`ramps.py`, `ends.py`):
  - The rear (white bumper) edge is sharp: a 2-5 px ramp at 43 px/frame. So there is no significant motion blur in the length.
  - The front edge has a ~20 px low-contrast ramp: the dark nose against the dark road.
  - A diff-profile length at the 10 % level on the centre column is 566-571 px (f60/65/70), and at the 50 % level 550-554 px.
  - An earlier joint fit that attributed the length change to blur (`blurfit.py`, a = 0.54) is rejected. The black car alone, at constant speed, shows the same linear trend in y, and its rear edge is sharp.
- Adopted **≈ 561 px** (range 556-568).

## Result
561 px × 0.009146 = **5.13 m** (range 5.08-5.20 m).

Second route: the orange car's own minimum length (561 px) gives 5.13 m with the same scale, which is consistent with two similar-sized cars. Lane width is 440 px = 4.0 m and car width is 241 px = 2.2 m, which is plausible for a slightly enlarged render.

Confidence: about ±3 %. The main uncertainties are the bumper-height versus origin-plane scale and the soft front edge.
