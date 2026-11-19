# Q54: speed of the white car (van) at 1.0 s

- 2D top-down scene with a static camera. fps = question_fps = 24, so t = 1.0 s is frame 24. Both the van and the cyclist move straight up the vertical road.
- `measure.py` template-matches each object (van template from frame 24, cyclist template from frame 36) in every frame,
  with sub-pixel parabolic peak refinement in y. This gives much cleaner steps than the centroids in scene/ (van residual 0.08 px).
- Scale comes from the prior (bicycle speed 5.33 m/s). The cyclist moves at a constant velocity from frame 1 onward:
  (y1 − y71)/70 = 8.964 px/frame, and a linear fit gives 8.973. So 5.33 / (8.964 × 24) = 0.02477 m/px.
- Van: the per-frame step grows linearly (uniform acceleration from rest, 0.287 px/frame²).
  - Backward step from frame 23 to 24: raw 6.966 px, linear step fit 6.972, global quadratic fit 6.965, 5-step mean 6.97.
  - Speed = 6.97 × 24 × 0.02477 = **4.14 m/s**.
- Second route: three independent estimates of the step (raw step, linear step fit, quadratic position fit) agree within 0.1%.
  The scene/ centroid track gives a similar but noisier step of about 7 ± 0.7 px.
  The scene/ cyclist net motion of 623 px over 70 frames gives a scale within 1% of the template value.
- Confidence: high, about ±2%.
