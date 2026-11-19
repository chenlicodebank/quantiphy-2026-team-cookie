# q_774 — speed of the basketball at t = 1.5 s

- 2D simulation. fps = question_fps = 24, so t = 1.5 s is frame 36. Speed = |p36 - p35| x 24.
- The ball moves only vertically (x stays at 907–908). Frame 36 is in the rising phase after the bounce at frame 24, so no impact falls inside the 35→36 interval or the fit window.
- Pixel displacement 35→36:
  - scene record circle-fit centre: 609.58 → 592.82, which is 16.76 px.
  - my own mask bbox centre (`measure.py`): 16.0 px raw (integer bbox). A quadratic fit over frames 30–42, 32–40 or 27–49 gives 16.70, 16.70 and 16.74 px.
  - Value used: 16.72 px/frame.
- Scale from the prior (diameter 0.282 m):
  - circle-fit diameter 106 px (range 105–107); mask bbox 108 px; sub-pixel 50 % saturation edge profile about 104 px (`diam.py`).
  - A zoomed view (frames/f36.png) shows the ball at x 853–961, about 108 px, with soft edges.
  - I used 106 px, so the scale is 0.00266 m/px.
- Speed = 16.72 x 24 x 0.282 / 106 = **1.067 m/s**.
- Second route: the raw per-frame difference of the circle-fit centres (16.76 px) gives 1.070 m/s. With the diameter anywhere from 104 to 108 px, the answer is 1.05–1.09 m/s.
- Confidence: good. The diameter definition is the main uncertainty, about ±2 %.
