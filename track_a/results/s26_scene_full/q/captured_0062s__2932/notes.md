# q_2932 – width of the whiteboard (cm)

Answer: **60.6 cm**

## Setup
- The file is 24 fps and question_fps is 24, so t = 1.4 s is frame 34. Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- The whiteboard (a white board with two knobs on its far edge) lies flat on the floor and slides away from the camera.
  The camera looks down at it obliquely, so its short side is strongly foreshortened in the image (~120 px at frame 34,
  against ~200 px for the long side).

## Method (scripts in this folder)
1. `corners.py`: segments the board in each frame (V>185 & S<45, largest component), takes 4 corners from the hull,
   fits a robust line to each edge (corner zones excluded) and intersects the lines to get sub-pixel corners. The overlays
   `frames/corn_24/34/44.png` show the fitted outline, which matches the board top (knobs excluded).
2. `rect3d.py`: finds the plane normal for which the back-projected corners form a 3D rectangle (opposite sides equal,
   right angle), using the known f. The global fit over frames 22-48 gives a tilt of 53.2 deg between the plane normal and
   the optical axis. Fits on the sub-windows 22-29, 30-37 and 38-48 agree to within 0.5 deg.
3. Scale: the plane offset is chosen so that the board centre (mean of the 3D corners) is 2.815 m from the camera at
   frame 34 (depth_info).
   - Frame 34 sides: long 0.809 m, short **0.606 m**.
   - With the sub-window normals, the short side is 0.605-0.612 m.

## Checks
- Size constancy (`check_vel.py`): with one fixed floor plane, the board's 3D size is nearly constant over frames 22-48:
  short side 0.604-0.614 m, long side 0.809-0.822 m. This supports both the plane and the scale.
- Prior velocity: the speed from the 3D centre track around frame 34 is 1.87 m/s with plain frame indices (5-frame
  linear fit). That is within 3.4% of the prior 1.934 m/s.
  - The record notes a likely dropped frame between 35 and 36. If that gap is counted as two intervals, the speed is
    1.55 m/s instead. The reference probably did not apply that correction.
  - If the scale were taken from the prior speed instead of the depth, the width would be about 62.7 cm.
- Naive method card (depth x image extent / f, no foreshortening correction): 2.815 x 120 / 763 = 44 cm. That is
  wrong for a board lying flat, because the ruler-measured size is its true side.

## Naming
- The board lies flat, so length is the longer horizontal side (~81 cm) and width is the shorter one (~60.6 cm).
  This is the reading used for the answer.
- Alternative reading: if "width" meant the long side (as for a board hung on a wall), the answer would be ~81 cm.
- The board is plausibly a 60 x 80 cm whiteboard.

Confidence: good for 60.6 cm under the shorter-side reading (about ±3%).
