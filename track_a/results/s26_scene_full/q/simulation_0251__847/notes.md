# Q847 — speed of soccer ball at t = 0.5 s (m/s)

- 2D sim, static camera, fps = question_fps = 24 → t = 0.5 s is frame 12; speed = |p12 - p11| x 24.
- Scale from prior (diameter 0.344 m). Ball pixel diameter re-measured (diam.py, measure.py) with subpixel
  half-threshold edges on the |frame - median background| profile: horizontal width 49.2-49.9 px in clean late
  frames (30-50, where contrast is good); vertical extent ~49. Scene record says 50. Used 49.5 px →
  0.006949 m/px.
- Displacement: scene track cx11 = 338.75, cx12 = 370.75 → 32.0 px/frame. Quadratic fit of the whole track
  (record's fit, 0.47 px rms) gives a step of 31.8 px at frame 12. My own edge midpoints (frames 10 → 14:
  306.5 → 433.5) give 31.75 px/frame. Used 31.85 px/frame.
- Speed = 31.85 x 24 x 0.344 / 49.5 = 5.31 m/s (range 5.27-5.36 for a 49-50 px diameter).
- Confidence: good (about ±2 %), limited mainly by the pixel diameter.
