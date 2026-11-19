# q_2005 — acceleration of the tennis ball at t = 1.5 s

Setup: a 2D segmentation video at 1920x1080, 24 fps (question_fps is also 24, so no re-timing). There are 41 frames, and t = 1.5 s is frame 36. The only object is one ball, which rolls horizontally to the right at constant y and slows steadily. The camera is static.

## Measurements (my own code: measure.py, diam.py)
- Position: I re-tracked the ball every frame (darkness mask, then a weighted centroid). The per-frame speed falls from about 1062 px/s to about 804 px/s.
- Pixel acceleration: I fitted x(t) with a polynomial.
  - Quadratic over all 41 frames: −153.6 px/s². The residual std is 0.19 px, so the deceleration is uniform.
  - Quadratic over frames 26–40, around t = 1.5 s: −155.0 px/s².
  - Quadratic over frames 0–19: −155.7 px/s².
  - Cubic evaluated at t = 1.5 s: −150.8 px/s².
  - I used −153.6 px/s² (the windows spread about ±1.5%).
- Ball diameter in pixels: I measured along the vertical, where motion blur does not stretch it.
  - Vertical half-max width: median 24.73 px.
  - Area-equivalent diameter from the soft mask: 24.88 px.
  - Bounding-box height: 25 px.
  - Partial-pixel count of the vertical profile: about 25.0 px.
  - I used D = 25.0 px, which agrees with the scene record.
  - The horizontal extent (26 px) and the hard-threshold equivalent diameter (26.6 px) are inflated by motion blur, so I did not use them.

## Scale and answer
- Scale = 0.17 m / 25.0 px = 0.0068 m/px.
- Acceleration = 153.6 × 0.0068 = 1.044 m/s² (a deceleration; I report the magnitude).
- Second route: the local fit around t = 1.5 s gives 155.0 px/s², which converts to 1.054 m/s², within 1%.
- Sanity check: the speed is about 7.2 m/s, slowing at about 1 m/s², which is plausible for a ball rolling with friction.

## Confidence
The main uncertainty is the pixel diameter, ±0.3 px (about ±1.5%), plus about ±1.5% from the fit. Overall I expect the answer to be within about 3%.
