# q_2639: soccer ball velocity at 0.9 s (cm/s)

t = 0.9 s -> frame round(21.6) = 22 (question_fps = file fps = 24).
Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## depth_info
- soccer f22 = 2.477 m, basketball f22 = 2.7777 m.
- At 1.4 s (frame 34) both lines are labelled "soccer"; one must be the basketball. Size check: soccer 54.1 px x 2.373/763 = 16.8 cm
  (matches 17.3 cm at f22), basketball 67 px x 2.602/763 = 23.0 cm (matches prior 23.2). So soccer f34 = 2.373, basketball f34 = 2.602.
- Soccer ball true diameter from depth: about 17.0 cm.

## Method (measure.py, centroid.py)
- The ball centres come from scene/tracks/soccer_ball.csv (circle fit). I checked them against my own white-blob convex-hull
  centroids (centroid.py). Those have a constant offset of about 3 px upward (the shadowed bottom is missed), and the steps
  between frames agree within about 4 %.
- Per-frame depth model A (ground plane): I fitted a floor plane to the 4 depth_info centres plus the resting basketball
  (depth from the 23.2 cm prior, 53.1 px). Each centre sits one radius above the floor. Residuals are 0.1-2 cm. The soccer
  centre in each frame is the ray intersected with the plane raised by r = 8.5 cm. This reproduces 2.481 m at f22
  (given 2.477) and 2.374 m at f34 (given 2.373).
- Per-frame depth model B: depth = f x 0.170 / diameter_px, with a polynomial fit of 1/D over frames 15-24 (noisier).
- The ball rolls away from the camera and slows down. Impact with the basketball is at frame 25, so windows stop at frame 24.

## Results (cm/s)
- Plane model, forward differences: 19->20 121, 20->21 112, 21->22 93, 22->23 106, 23->24 122. Chords: 18-23 110,
  19-24 110, 20-24 108.
- Size-depth model: fwd22 117, mean 19..23 125.
- Fixed depth (2.477 m, lateral only): about 97 (lower bound; it ignores the depth motion of about 0.02 m/frame).
- Hull centroids give about 4 % smaller pixel steps -> about 105.

Answer: about 107 cm/s, from the plane-model 5-frame smoothed value before impact. Confidence: moderate (±10 %). The
reference smoothing window could include the slow impact step 24->25, which would lower the value to about 98.
