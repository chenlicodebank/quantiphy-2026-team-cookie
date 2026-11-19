# Q1025: displacement of the column below the drone, 0.5 s to 1.0 s

- The "column below the drone" is the black cylinder hanging under the drone's rotor plate. It is rigid with the drone, which rises straight up from the robot. This is a 2D scene with a static camera, 24 fps (the file and the question agree).
- I checked `scene/tracks/drone.csv` against the contact sheet. top_y falls steadily, about 6.9 px per frame, from frame 2 to frame 71, with no bounces. Linear fits (`measure.py`):
  - top edge, frames 2-71: 6.90 px/frame
  - cylinder bottom, frames 26-71: 7.06 px/frame
  - top edge, frames 2-30: 6.65 px/frame (the early frames are partly blended with the robot and lid)
- The prior is a single speed of 0.96 m/s, which implies constant velocity. So the scale is 0.96 / (6.90 × 24) m/px.
- Displacement from frame 12 to frame 24 (0.5 s to 1.0 s) = 12 frames × 6.90 px × scale = **0.48 m**. This is the same as speed × Δt = 0.96 × 0.5.
- Second route: the raw top_y difference between frames 12 and 24 (866 to 787 px, 79 px) gives 0.458 m. Using the early-window slope gives 0.475 m. Both are within 5 % of 0.48. The motion is consistent with constant velocity.
- Confidence: high.
