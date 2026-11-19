# q_2893: orange ball diameter (cm)

Orange ball = the basketball (scene/ "basketball"). The file and the question both use 24 fps, so t = 0.5 s is frame 12 and t = 1.0 s is frame 24.
f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Measurement (measure.py)
- Orange HSV mask at two value thresholds, a least-squares circle fit to the contour, and the equal-area diameter.
- f12 (t = 0.5 s; first clear frame, no hand): fit d = 78.2 / 77.1 px, avg 77.7 px. The overlay (frames/f12_fit.png) sits well on the ball.
  It has slight motion blur (about 24 px/frame); the scene record gives minor/major axes of 74.6/80.0.
- A smooth 1/d-vs-frame fit over f12-29 gives 76.2 px at f12.
- f24 (t = 1.0 s): 62.7 px.

## Size
- Method card with the t = 0.5 s depth: 2.24 x 77.7 / 762.8 = **22.8 cm** (22.4 cm with the smoothed 76.2 px).
- The t = 1.0 s depth (1.81 m) gives 1.81 x 62.7 / 762.8 = 14.8 cm. That is impossible for a basketball, and it
  contradicts the image: the ball shrinks from 78 to 63 px, so it moves away from the camera, while that depth says it comes closer.
  I treat it as a bad depth reading and do not use it.

## Second route: the velocity prior (velcheck.py)
- 3D track with Z from the t = 0.5 s depth scaled by the apparent size: forward-difference speed is about 1.79 m/s at f12-16, against the prior's 2.21.
- A linear Z between the two given depths gives 1.85-2.06 m/s.
- The reference velocity uses noisy per-frame sensor depth, and the f11->f12 step looks like a skipped frame.
  So the prior only loosely constrains the scale. If anything it points to a slightly larger ball, which is why I keep the unsmoothed 22.8 rather than 22.4.
- Sanity check: a basketball is 22-24.5 cm (sizes 5-7), which matches.

Answer: 22.8 cm. Confidence: moderate (about ±5%).
