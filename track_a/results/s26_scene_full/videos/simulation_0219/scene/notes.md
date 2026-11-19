# simulation_0219: measurement record (pixels and seconds only)

Video: 1920x1080, 24 fps, 50 frames (t = frame/24). Blender render labelled **2D**. Static camera (the ceiling
strip moves at most 0.16 px). The back-wall lighting and shadows change strongly over the clip, so plain
background subtraction does not work here.

Scene: a factory hall with a back wall parallel to the image (concrete pillars, slatted windows, plain grey lower
panel) and a dark floor with white lane lines. There are two moving objects:

1. **tank_drill_robot**: the large blue tracked robot with the drill and claws. It is the only coloured object.
   It moves **right** at constant pixel speed for the whole clip.
2. **small_grey_robot**: the small grey humanoid toy robot with a big dome head. It walks **left** at a steady
   speed. It is nearer the camera than the tank, and the tank passes *behind* it (frames 22-36). They never touch.

There are no starts, stops, bounces or contacts. Both are already moving at frame 0 and still moving at frame 49.

## Files
- `scene.json`: inventory, static objects (pixel positions), events, camera, summary speeds and sizes.
- `tracks/tank_drill_robot.csv`, one row per frame:
  - `ref_x, ref_y`: recommended origin proxy. ref_x = main-body point + 30 px (about the chassis mid-x), ref_y = middle of the box.
  - `body_x` (fit) and `body_x_meas` (template measurement).
  - `tip_x` (fit) and `tip_x_meas` (row scan) for the drill tip, at y = 655.
  - `rear_plate_x_meas`: rear sloped plate of the track frame.
  - `left_x` (quadratic fit) and `left_x_meas`: leftmost point.
  - `box_center_x`, the bbox clipped to the image, `length_px` (left_x to tip_x, *unclipped*), `height_px`.
  - `visible`, `fully_in_frame`, `occluded`.
- `tracks/small_grey_robot.csv`, one row per frame:
  - `ref_x`: body axis, the centre of the dark cup under the dome head.
  - `ref_y`: estimated pelvis/hip height = cup top + 154 px.
  - `cup_top_y`, `head_top_y` (dome top), `feet_bottom_y`, `height_px`.
  - bbox and `width_px` from the segmentation, filled only where it is reliable.
  - `cup_interpolated` flag.
- `scripts/`: every measurement script. `build_record.py` assembles the CSVs from the intermediate JSON files in `../frames/`.

## How it was measured
**Tank** (rigid). Sub-templates were cut from frame 12, where the tank is fully visible: drill tip, claws, drill
arm, main body and rear plate. They were matched with NCC to sub-pixel accuracy in every frame (`track_tank.py`).
The drill tip was also found by a dark-pixel row scan (`tip_scan.py`), and the leftmost point from a
colour-saturation mask (`sat_extents.py`).
- Linear fits (robust):
  - tip: 54.02 px/frame (max residual 1.6 px)
  - main body: 51.80 px/frame (1.5)
  - rear plate: 50.89 px/frame (1.8)
- The leftmost point slows from about 50 to about 46 px/frame, so it uses a quadratic fit (residual < 5 px).
- Vertical motion is under 1.5 px. Top y = 271 (handle) and bottom y = 894 (tracks) are constant.
- Frame 12 extents: x 181-799 (618 px), y 271-894 (623 px). The tracks run about 181-690. The body cylinder spans about 195-625 by 335-495.

**Small robot** (articulated). Its reference is the dark cup under the dome head (`neck_track.py`, `robot_points.py`):
- The cup centre is the centre of its widest dark row, which marks the vertical body axis.
- It moves at -8.40 px/frame (linear-fit residual <= 1.5 px).
- In frames 27-33 the dark tank behind it merges with the cup, so the cup x and top are **linearly interpolated** between frames 26 and 34 (`cup_interpolated = 1`).
- The dome top is the strongest gradient edge about 77 px above the cup top. Where that edge is weak it is set to cup top - 76.5.
- Feet bottom, x extents and width come from a gain-corrected background-difference mask (`seg_robot.py`). They are given only for frames 0-23 and 37-49.

## Reliability
- **Tank positions:** about 1-2 px for each part. **Origin choice is ambiguous:** under perspective the parts move
  at different pixel speeds (tip 54.0, body 51.8, rear plate 50.9, far-side rear about 46, claws about 44 px/frame;
  the claws are animated or on the far side). For a single "tank speed" in 2D, `ref_x` (51.8 px/frame) is the
  central estimate. The spread between parts is about ±4%.
- **Tank apparent length** grows from 614 px (frame 9) to 705 px (frame 32) because of perspective. In
  frames 33-49 the tip is beyond the image edge, so `length_px` there is extrapolated. Frame 12 gives 618 px.
  Height is always 623 px.
- **Robot axis x:** about 1.5 px (frames 27-33 interpolated, about 3 px).
- **Robot pelvis y:** the +154 px offset was read by eye at frames 0-4 (±5 px). Its frame-to-frame change follows the head bob, which may not match the true hip motion.
- **Robot height** (dome top to lowest foot): 300-317 px, changing with gait and head bob; 302.5 px at frame 0.
  The dome is semi-transparent and faint in frames 9-16 and 36-49, so the dome top is ±3 px there.
- **Robot bbox x0/x1:** from the mask, which may miss grey parts that match the wall, so the width can be slightly
  too small (±10 px). Not given during the tank overlap.
- **Static objects:** read by eye from gridded frames, ±5 px.
- **Ambiguity, depth:** the robot's feet are lower in the image (y about 965) than the tank's tracks (894), so the
  robot is nearer the camera. A single m/px scale for both objects is therefore approximate. The tank's own
  parts also span depth.
- **Other:** no motion blur of note. The tank's shadow darkens the wall as it passes.
