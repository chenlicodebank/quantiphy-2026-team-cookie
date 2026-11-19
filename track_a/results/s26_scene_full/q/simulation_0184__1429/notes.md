# Q1429 – acceleration of the box at 0.2 s (simulation_0184)

The file and the question both run at 24 fps, so t = 0.2 s is frame 5. Over frames 0–8 the box is in free fall: it is released from rest at frame 0, first touches the ramp at frame 8, and lands on the conveyor at about frames 12–13.

## Measurement
- `fall_track.py`: I tracked the box over frames 0–8 by sub-pixel template matching (the box does not rotate while it falls).
  - x stays constant to within 0.01 px. Successive y steps are 2.22, 6.68, 10.73, 14.95, 19.15, 23.33 and 27.67 px.
  - The second differences are 4.46, 4.06, 4.21, 4.21, 4.17 and 4.34 px/frame². A quadratic fit gives a = 4.21 px/frame² = 2424 px/s². This is constant, so it is free fall.
  - A vertical fall at x = 584 shows no slant, so the camera is level (pitch under about 1.5°). That makes Z constant during the fall, and g = a_px · Z0 / f.
- `scale_check.py` estimates the focal length from the prior and depth_info:
  - Z0 and Z12 come from the given distances (9.194 m at frame 0, 9.096 m at frame 12) and the pixel rays.
  - On the ramp (frames 18–44), the box's depth comes from the change in its apparent length: 1/L fitted linearly against u, anchored to Z12.
  - The 3D positions are then fitted with a quadratic to get the acceleration along the ramp at 1.25 s.
  - Matching the prior of 1.58 m/s² needs f ≈ 2225 px (horizontal FOV ≈ 47°). That gives a ramp slope of about 30.5°, which looks right.
  - With that focal length, the free-fall acceleration is 2424 × 9.03 / 2225 ≈ 9.84 m/s².
- The ratio of fall to ramp acceleration hardly depends on f (6.17–6.28 for f from 1600 to 2600 px), so g ≈ 1.58 × 6.22 ≈ 9.83 m/s².

## Answer
For a uniformly accelerated object, the acceleration at frame 5 is the constant itself. The measurement gives 9.83 ± 0.2 m/s², which matches Blender's default gravity, so the answer is **9.81 m/s²**.

## Notes on the scene record
- The `scene/` track (centroid steps of about 4.1 px/frame²) agrees with the template track.
- My first ramp template-matching attempt (`ramp_track.py`) produced a poor mask and noisy scale values, so I did not use it. The scale check uses `minrect_len` from the scene track instead.

Confidence: high.
