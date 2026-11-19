# q_241 – diameter of the ball (m)

The scene is a 2D render: a tennis-like ball falls straight down in front of a door, and the camera is static. The prior is g = 9.8 m/s². The file runs at 24.020228 fps. All times use question_fps = 24.0, so t = frame / 24.

## Scale from the prior (measure.py)
- I subtracted a median background, thresholded the difference at 15, 30 and 45, and took the largest component's centroid.
- I fitted a quadratic to y(t) over frames 2–18. Frames 0–1 are clipped by the top edge, so I left them out. The fall is free all the way: there is no bounce.
  - thr30: a = 6290 px/s², rms 0.19 px
  - thr15: 6283 px/s²
  - thr45: 6302 px/s²
  - Fits on the top edge and bottom edge give 6265–6332 px/s².
- I used a = 6290 px/s², so the scale is 9.8 / 6290 = 1.558e-3 m/px.

## Ball diameter in pixels
- Bounding-box width and height at thr30: median 45 / 44 px. The area-equivalent diameter is 44.7 px.
- At thr45 the area-equivalent diameter is 43.0 px. At thr15 it is 47.5 px, but that threshold is inflated by noise and blur.
- Second route (edges.py): subpixel edges at the gradient maximum of horizontal difference profiles through the centre, over 10 frames. The median is 43.2 px (range 41.8–44.3).
- I adopted 44 px, which sits between the two routes (43–45).

## Answer
- 44 × 1.558e-3 = 0.0686 m.
- Range from the pixel uncertainty: 0.067–0.070 m.
- This is consistent with a real tennis ball (about 0.067 m), so the scale is plausible.

Confidence: good, about ±3%.
