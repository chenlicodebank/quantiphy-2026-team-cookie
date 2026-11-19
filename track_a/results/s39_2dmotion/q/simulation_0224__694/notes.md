# q_694 — speed of the moving chess piece at t = 1.5 s

Video 1920x1080, file fps 24 = question_fps 24. t = 1.5 s -> frame 36; speed = |p(36) - p(35)| x 24.
2D scene, one m/px scale from the prior (piece diameter 0.097 m).

## Object
The only moving object is the cream piece (the record calls it a "block"/soap bar): a Chinese chess piece lying flat on the
inclined chess board, seen edge-on. Its extent along the slope is the diameter; the ~33 px across is its thickness.

## Diameter in pixels
- Own (measure_bg.py): |frame - background frame 0| > 30, largest blob, extent along the 27.3 deg slope axis.
  Median over frames 14-38: 82.1 px full extent, 80.2 px trimmed (0.5-99.5 pct). Frame 36 mask overlay
  (frames/own_bgmask36.png) fits the piece, plus a thin shadow sliver at the lower left.
- Record: 81.5 px (80.2-82.7).
- SAM 3 ("white soap bar", frames 35 and 36; sam_check.py, same axis): 85.0 / 83.6 px full, 81.3 / 80.0 px trimmed.
  This is within about 2-3 pct of mine. The first box-prompted SAM masks ("white block" + box) gave 97-109 px because
  they bled into the background (overlay checked; the visible piece bbox is about 74x57 px), so I rejected them.
- Adopted D = 81.5 px -> scale = 0.097 / 81.5 = 1.190e-3 m/px.

## Displacement from frame 35 to frame 36 (px/frame)
- Record centroids: 34.67. Own centroids: 35.19. SAM centroids (690.55, 792.91) -> (658.46, 808.37): 35.62.
- Duplicate/skip check: video frame 34 already shows source frame 35, frame 35 duplicates it, and frame 36 is source
  frame 36. So the step from 35 to 36 is a true single-frame step.
- Smooth check: quadratic of the record position against source_frame_est gives 35.40 (whole slide, rms 0.8 px) and
  34.88 (local fit over source frames 28-38); own data with a local fit gives 34.91. Acceleration is about 1.0 px/frame^2.
- Adopted 35.1 px/frame (middle of the 34.7-35.6 spread).

## Answer
v = 35.1 x 24 x 1.190e-3 = 1.00 m/s. The routes range from 0.99 to 1.02 m/s across the scale and step choices.
Confidence: good (about +/-3 pct). The main uncertainty is the pixel diameter: soft lower-left edge, shadow.
