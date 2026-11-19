# q_765: acceleration of the basketball at t = 0.5 s (m/s^2)

Prior: basketball diameter = 0.282 m. 2D video, static camera, 24 fps (the file fps and question_fps are the same). t = 0.5 s -> frame 12, which is in the free-fall descent
(release at frame 0, bounce at frame 24).

## Method (measure.py -> my_track.csv, frames/ov12.png)
- Ball mask: HSV crimson threshold, closing, largest component, filled. Centre from a least-squares circle fit to the contour,
  for every frame. The overlay at frame 12 matches the edge.
- Diameter (frames 0-22): circle fit 74.8 px, mask bbox 74 x 76, area-equivalent 75.7. I use **75.0 px**, so the scale is
  0.282/75.0 = 3.76e-3 m/px.
- SAM 3 check ("basketball", frames 2 and 12): box 75.0-75.7 wide x 77.0-77.1 tall, centroid (986.7, 806.9). My mask gives
  (986.6, 806.8). The box width agrees with mine within 1%, and the height (77) is within 3% of 75. SAM's horiz_px of 80 and its
  area come from a ragged mask outline (see frames/seg_00_f12.jpg), so I did not use them. My circle fit follows the
  edge on the zoomed overlay.
- Acceleration: the descent is a constant-acceleration parabola. Quadratic fits of y(frame):
  frames 0-22: 544.3 px/s^2; 4-20: 541.2; 8-16 (around frame 12): 543.4; 0-12: 541.4. So a is about 543 px/s^2,
  which gives 543 x 0.282/75.0 = **2.04 m/s^2**.
- Second route: raw one-frame backward differences (speed(12) - speed(11)) x fps = 2.21 m/s^2 (noisy, ±0.3 px centre
  noise amplified by 576). The mean of the raw per-frame accelerations over frames 2-22 is 2.06 m/s^2. Both agree with the fit.
- The ascent (frames 26-49) has a curvature about 8% lower (1.89 m/s^2). It does not apply here, because t = 0.5 s is on the descent.
- The value is far below 9.81 because the render is not at real-world scale. The prior sets the scale.

Answer: 2.04 m/s^2. Confidence: good (about ±2%, mainly from the diameter's ±1 px).
