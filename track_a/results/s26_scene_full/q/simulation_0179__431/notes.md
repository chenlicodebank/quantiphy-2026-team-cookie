# Q431 — height of the trolley (shopping cart)

2D side-view render, 24 fps (file fps = question_fps, no re-timing). Prior: cart acceleration = 1.507 m/s².

## Method
- fit.py: quadratic fit x(t) to the record's track (scene/tracks/shopping_cart.csv, frames 0-59; cart rolls
  from rest along +x at constant depth, no impacts).
  - bbox_cx: a = 296.1 / 295.4 / 294.8 px/s² (fit from frame 0 / 5 / 10), rms 0.5 px
  - wheels_cx (independent reference point): a = 295.1 / 294.4 / 294.0 px/s²
  - Edges: x0 is about 288 and x1 about 302. They differ because the apparent length grows a little, while the centre stays near 295.
  - Adopted a = 295 px/s² ± 1 px/s².
- Scale = 1.507 / 295 = 0.005108 m/px.
- Pixel height: handle top → wheel bottom = 248 px (median of all frames, range 246–250, constant), checked
  on a zoomed frame at t = 1.0 s (bottom of castors at y ≈ 884).
- Height = 248 × 0.005108 = 1.267 m.

## Check / confidence
- The two reference points (bbox centre, wheels) agree on the acceleration to within 0.5%.
- The camera looks slightly down: the basket rim is seen almost edge-on, and the near and far castors are offset by a few px.
  So up to about 5 px of the 248 px may come from depth rather than true height (that would give about 1.24 m).
- Answer 1.265 m. Confidence: good (±3%).
