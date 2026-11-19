# q_670 — diameter of the vase (m)

Prior: diameter of the robot vacuum = 0.438 m. No depth_info. fps = question_fps = 24 (only static sizes matter here).

## Pixel sizes (frame 77; both objects are static or stopped)
- Vase (white round pot on the left end of the TV console): I cast 360 radial rays and placed the edge where each ray
  crosses 50% of the local vase-to-console contrast, then fitted a circle (rms 0.5 px). Diameter = **72.5 px**
  (73.3 px at 35% contrast). `vase.py`, `edges50.py`, overlay in `frames/vase_overlay.png`.
  **The scene record is wrong here:** its 60 px box (725–784) cuts inside the silhouette. The overlay shows the
  72.5 px circle sitting on the outer rim.
- Robot: same 50%-contrast circle fit, leaving out the inward-facing sector where the side wall shows.
  Diameter = **119.8–120.0 px** (frames 50 and 77; 120.4–120.6 at 35%). The record's 117.8 px comes from a
  threshold near the top of the edge (gray > 185), so it is not on the same edge definition as the vase.
- Pixel ratio vase/robot = 0.606 (0.6045 at 50%, 0.6085 at 35%). With no perspective correction:
  0.606 × 0.438 = 0.265 m.

## Perspective correction (the vase stands on the console, above the floor)
The camera is overhead and pinhole, with the principal point taken as the image centre (960, 540). If an object's
top is at height h and the camera is at height H, its image scale is H/(H−h) times the floor scale, and its top
appears shifted away from the centre by a fraction h/H of its image radius.
- Robot top: the side wall appears on the inward side of the disc, and its width grows linearly with image radius.
  The regression gives a slope of 0.0062–0.0075, so h_robot/H ≈ 0.007 (`robot_side2.py`).
- Console top: the front face is visible. The left front corner shifts diagonally from (710.5, 282) to (719, 291),
  i.e. 12.4 px at radius 359, so h_console/H ≈ 0.0345 (`console_face.py`).
- Vase: the centre of the dark opening is 9.2 px further out than the silhouette centre (radius 367), which puts the
  rim about 0.025 H above the widest section. I assume the widest section sits about 40% of the way up the vase,
  so it is about 0.0165 H above the console top (plausible range 0.008–0.025 H).
- Correction C = (1 − 0.007) / (1 − 0.0345 − 0.0165) = 1.046 (range about 1.037–1.056).

Vase diameter = 0.606 × 0.438 / 1.046 = **0.254 m**.

## Checks and confidence
- Second route, using the 35% contrast edges for both objects: 0.6085 × 0.438 / 1.046 = 0.255 m.
- Without any perspective correction the answer would be 0.265 m (+4.5%). With the correction at the ends of its
  range: 0.251–0.256 m.
- The height ratios hang together: console/robot height ≈ 5, which would be about a 0.6 m console for a 0.12 m
  robot in scene units.
- Main uncertainty: how high the vase's widest section sits (±1% on C), plus about ±1% from edge definition.
  Overall about ±3%.
