# Q1539 – speed of the blue car (light-blue canopy cart) at t = 1 s

File fps = question fps = 24 -> t = 1 s is frame 24; speed = |p(24) - p(23)| x 24.

## Motion is parallel to the image plane
The cart keeps the same image row and size (scene record and my own checks), so every rigid point has the same 3D
velocity. Speed = (pixel step in some depth plane) x (m/px in that same plane). I use the cart's **near-side plane**
(tyre face / side sill).

## Pixel speed at frame 24 (motion24.py, fitmodel.py)
- At frame 24 the cart's lower body is hidden behind the yellow car. Only the roof, handle and rear light box show.
  The record's roof track switches method at frame 24/25, which gives a fake 30.0 px step there, so I did not use its raw steps.
- Near-side templates (sill, lower body; frames 32-41) give smooth steps of 33.56 down to 29.31 px/frame.
- Per-frame speed fits a Blender Bezier ease (smoothstep) well: v = V(1-((t-c)/h)^2), with start ~ frame 0, c ~ 29.3,
  h ~ 30, and residuals of 0.04-0.12 px. The value at t = 23.5 (the backward step into frame 24):
  sill 32.76; light box 32.30 (x1.005-1.007 near/lightbox ratio = 32.5); whole record 0-41 32.15 (x1.011 = 32.5);
  handle raw 31.35 (x1.004 = 31.5; the handle drifts systematically against the light box, a perspective/appearance change).
  -> near-plane step at frame 24 = **32.6 px/frame** (+-0.3).

## Scale (scale.py, tyre3.py, crops)
- Route A (prior, cart tyre 0.369 m): the near-face tyre diameter is about 73-74 px. Sources: a left-silhouette circle fit
  (72-74 px in frames 37-41) and the zoomed crop (top 743.6 to bottom 816.4 = 72.8 px; width 75). Gives 0.00499-0.00505 m/px.
- Route B (prior, yellow car tyre 0.764 m = 189-192 px vertical, plus depth_info 11.38 m to the yellow front-left tyre at
  frame 12): f is about 2716-2762 px (HFOV about 38 deg), car near-side Z = 10.99 m and camera height 1.38 m. The cart's
  ground contact row 817 vs the car's 884 (horizon 539.3) gives cart near-side Z = 13.64 m and 0.00494-0.00502 m/px. This
  predicts a cart tyre of 73.5-74.7 px, which matches route A.
- Adopted: 0.00500 m/px (+-1.5 %).

## Answer
v = 32.6 px/frame x 24 fps x 0.00500 m/px = **3.91 m/s**.
Second route: the record-based smoothstep (32.5 near-plane) with the route-B scale (0.00494-0.00502) gives 3.85-3.92 m/s.
Confidence: about +-3 %.
