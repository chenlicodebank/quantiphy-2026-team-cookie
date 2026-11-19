# Q43: speed of the bicycle at 1.0 s (m/s)

- The video is a 2D top-down orthographic street scene at 24 fps; question_fps is also 24, so no re-timing. t = 1.0 s is frame 24.
- Prior: the yellow (peach) car is 5.44 m long.
- Scale (`carlen.py`): the car body mask (background difference, peach colour, convex hull) gives a length of
  217 px (vertical, f0-1) and 218 px (horizontal, f66-71). The scene record's PCA extent is 220 px. The bumper
  edges are soft, so I use 219 ± 1.5 px, which gives 0.02484 m/px.
- Cyclist (`measure.py`): I re-tracked it with my own background-difference mask in the x 880-935 strip
  (`cyc_track.csv`). It rides straight up at constant speed:
  - centroid slope: 8.96 px/frame over frames 18-30, 8.87 over frames 12-36, 8.93 over frames 2-71 (quadratic term ≈ 0);
  - top-tip and bottom-tip slopes: 8.7-9.5 and 8.83-8.90 px/frame.
  - Single steps jitter between 8.2 and 9.3 px because of pedalling, so I use the smooth slope, 8.93 px/frame.
- Speed: 8.93 px/frame × 24 × 0.02484 = **5.32 m/s**.
- Second route: the scene record's own track (mean step 8.93 px/frame, frames 2-71) agrees. The car-length spread
  (217-220 px) gives 5.30-5.37 m/s.
- Confidence: high, about ±2 %.
