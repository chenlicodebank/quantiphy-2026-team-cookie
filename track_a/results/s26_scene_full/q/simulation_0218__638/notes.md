# Q638: height of the big robot (m)

Prior: robot speed = 5.924 m/s. fps = question_fps = 24, so the robot moves 0.24683 m per frame. No depth_info.
The robot is the only moving object. It translates rigidly, horizontally and at constant speed. Every tracked feature
has a constant pixel rate, so its depth does not change and the motion is parallel to the image plane.

## Why a single 2D scale is not enough
The robot is close to the camera, and parts at different depths move at different pixel rates (45.8 to 54.5 px/frame,
see scene/notes.md). For any point, metres per pixel at that point's depth = 0.24683 m / (its own px/frame rate),
because every point of a rigid body moves at the same world speed. So I convert each pixel span with the rate of the
part that forms that edge.

## Measurements (scripts: measure.py, handle2.py, edges.py, edges2.py)
- Top of the AABB is the top of the near-side handle on the red box. Two handles are visible; the near one appears
  higher. Its top edge is at row 270.3 (grey drop and red-chroma onset, frames 12 and 21).
  - Rate from template tracking of the near handle top bar, frames 9-29: 49.62 px/frame on grey values, 49.60 on the
    gradient image (max residual 0.85 px).
- Bottom of the AABB is the bottom of the near track (the ground contact edge). It is at row 893.5 ± 1.
  - Rate of the track-bottom template: 50.775 px/frame, matching the near chassis plate at 50.757.
- Horizon (ground-plane vanishing line) is at y = 561, from the floor-mark vanishing point in scene.json. The result
  hardly depends on it: 10 px of horizon error changes H by only 0.04%.

## Result
H = 0.24683 x [(893.5 - 561)/50.775 + (561 - 270.3)/49.60] = 0.24683 x (6.549 + 5.861) = **3.06 m**.
That splits into a camera height of about 1.62 m and 1.43 m from camera level to the top of the handle.

## Checks
- The two rate measurements (grey and gradient templates) agree within 0.04%.
- Bottom edge ±1 px and top edge ±0.5 px change H by less than 0.2%.
- A naive single scale from the full 624 px height gives a range around this value: 2.94 m with the record's
  origin_est rate (52.46 px/frame, near-side outline), 3.20 m with the robot's mid-depth rate (about 48.2 px/frame).
  The per-depth computation above (3.06 m) is the one that is geometrically consistent.

Confidence: moderate to high, roughly ±3%. The main remaining uncertainty is whether the reference AABB includes
exactly the handle top and the track bottom.
