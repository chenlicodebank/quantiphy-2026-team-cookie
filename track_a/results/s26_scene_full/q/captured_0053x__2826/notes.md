# q_2826: basketball diameter (cm)

File fps 24 = question_fps 24. Basketball is static all clip; depth_info: basketball 2.925 m (t=0.4 s). f = 0.5959*1280 = 763 px, c=(640,360).

## Measurement (measure_ball.py, chroma-key mask, frames 0,5,10,20,30,47 - identical within 1 px)
- bbox 66-67 px wide x 61 px tall, centre (986, 370); area-equivalent diameter 63.9-64.3 px; circle fit 63.0 px
  (overlay frames/ov10.png: contour clean, top not clipped).
- Ellipse elongation 66/61 = 1.08 is the expected off-axis sphere stretch 1/cos(theta) = 1.098
  (theta = atan(346/763) = 24.4 deg), which also confirms f ~ 763 px.

## Sizes
- Method card (depth * px / f): 61 px -> 23.4 cm; 64 px (equal-area) -> 24.5 cm; 66 px -> 25.3 cm.
- Exact sphere perspective with 2.925 m to centre: tangential axis -> 21.3 cm, radial axis -> 21.0 cm.
  If the depth was measured to the ball's front surface (centre ~0.11 m further) -> ~22.0 cm.
- Answer: 23.4 cm (card value from the undistorted tangential/minor axis), a value between the
  perspective-exact estimate (21-22 cm) and the plain card value with the mean extent (24.5 cm, = size-7 ball).

Confidence: moderate; spread of routes is 21-25 cm, mostly from the depth/perspective convention.
