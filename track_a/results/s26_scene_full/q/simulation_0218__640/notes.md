# q640: outer diameter of the robot's tires (m)

Prior: robot speed 5.924 m/s. depth_info: none. fps = question_fps = 24, so no re-timing.

## What the "tires" are
The tracked robot has three large road wheels with grey rims between two sprocket/idler wheels. Each has a
mid-grey outer tire band (r ≈ 29–33.5 px) around a bright ring (r ≈ 28.5 px). The bottom of the wheel sits on the
lower run of the track.

## Measurements (scripts are in this folder)
- `wheeltrack.py`: Hough circles plus refinement of the bright-ring centre, then the median radial profile with the
  top sector (suspension arm) excluded. The outer tire edge is the half-level crossing between the tire band and the
  dark background.
  - Outer radius 33.2–33.9 px over frames 4–42, typically 33.4 px.
  - **Outer diameter ≈ 66.8 px** (the max-gradient edge gives 33.4–33.6 px, which agrees).
- The wheel centre is tracked from frame 8 to frame 36 (`compute.py`):
  - It moves **50.76 px/frame** (residuals ≤ 0.2 px), which matches the chassis-plate rate of 50.75 in scene/.
  - So the wheel's own depth plane has this pixel rate.

## Scale
- The motion is a pure translation parallel to the image at constant depth, so every rigid part moves
  5.924/24 = 0.24683 m per frame.
- At the wheel plane the scale is 0.24683 / 50.76 = 0.004863 m/px. This is the same plane as the wheel, so
  perspective cancels.
- **D = 66.8 × 0.004863 = 0.325 m.**

## Checks
- The radius is consistent across about 30 frames and positions in the image (±0.2 px), and the left, right, down and
  diagonal profiles agree.
- The scale is the same whether it comes from the wheel's own centre track or from the plate rate in the scene record.
- If the scene record's origin_est rate (52.46 px/frame, a different depth mix) is used instead, D = 0.314 m (−3%).
  I rejected it because the wheel's own plane is the physically correct one.

Confidence: medium-high, about ±4%. The main risk is how the reference defines a "tire" (for example, whether a
sprocket or the track is meant instead).
