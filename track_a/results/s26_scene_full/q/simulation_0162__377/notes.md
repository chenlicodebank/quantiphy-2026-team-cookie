# Q377: ball speed at t = 1 s

- 2D side-view render, static camera, 24 fps (file and question rates agree). t = 1 s → frame 24; speed = |x24 − x23| × 24.
- Scale from prior: ball diameter 0.21 m. Pixel diameter is about 81.5 px: the scene record's circle-fit median is 81.6 and frames 40–80 give 80.2–81.8; the vertical extent (top y≈607 to contact y≈688) is ≈81 px and is free of horizontal motion blur; diam.py gives a mean equatorial mask width of 81.7 px. Scale = 0.21/81.5 = 2.577e-3 m/px.
- Displacement from frame 23 to 24: the scene track gives 133.74→150.29 = 16.55 px. My own tracking (measure.py, the midpoint of the mask edges in the upper half) gives 133.5→150.0 = 16.5 px. Neighbouring steps are 16.0, 16.5, 17.0 and 17.5, a smooth trend, so 16.5 px/frame is a consistent value.
- Speed = 16.5 × 24 × 2.577e-3 = 1.02 m/s. If the blur-inflated diameter of 83.9 px is used, the speed is 0.99 m/s.
- Confidence: about ±3 %.
