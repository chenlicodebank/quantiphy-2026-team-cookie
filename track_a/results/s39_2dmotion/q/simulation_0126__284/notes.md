# q_284: speed of the puck at t = 2.0 s (m/s)

The prior says the puck's diameter is 0.074 m. This is a 2D top-down air-hockey render at 24 fps, and question_fps is also 24, so t = 2.0 s is frame 48.

## Method
- `measure.py`: an HSV orange mask of the puck in frames 36-60. It gives the centroid, the bbox and the equal-area diameter.
  - The puck moves straight up at constant velocity after its bounce on the bottom rail (between frames 40 and 41).
  - Steps in frames 42-60 are 9.19-9.57 px/frame (pixel noise). The mean of frames 43-60 is 9.337. The end-to-end value over frames 42→60 is (1653.97 − 1485.91)/18 = 9.337 px/frame.
  - The scene record agrees: 9.34 mean over frames 42-71.
  - The single-frame step at frame 48 is 9.47 px. It is noisy, and the motion is uniform, so I used the constant 9.34 px/frame.
- `profile.py`: the half-maximum edge diameter from (R−B) profiles through the centre in frames 44, 48, 52 and 56.
  - Horizontal: 64.20-64.26 px. This is perpendicular to the motion, so there is no blur.
  - Vertical: 64.2-65.6 px, slightly widened by motion.
  - Other measures: mask bbox 64 px, equal-area diameter 64.3 px.
  - I used D = 64.25 px, which gives a scale of 0.074 / 64.25 = 1.152e-3 m/px.
- Speed = 9.34 px/frame × 24 fps × 1.152e-3 m/px = **0.258 m/s**.

## SAM 3 check
- On frames 47 and 48, the phrase "orange puck" also picked up the two red mallets (k0 and k1). The puck is k2.
- Frame 48: SAM's centroid is (537.7, 1597.3), against my (537.8, 1598.0) and my profile centre (537.7, 1597.7). Its horiz/vert extents are 64/63 px, against my 64/64.
- SAM's minAreaRect length is 69 px and its area-equivalent diameter is 65.7 px (+2 pct). Both include the soft anti-aliased edge.
- The bbox extents agree within 1.6 pct, so they are within 3 pct. The half-max profile (64.2 px) is the sharper estimate.
- The SAM centroid step from frame 47 to 48 is 9.9 px, which is noisier but consistent with the 9.34 constant.

## Second route
- The slope of a straight-line fit to the centre positions over frames 42-60 is 9.337 px/frame. The scene record gives 9.34 over frames 42-71. Both give the same speed.
- If the diameter were 63.5 px (the scene record's value), the speed would be 0.261 m/s, a +1 pct difference.

Confidence: high, within about 2 pct.
