# simulation_0293 — measurement record

2D simulation scene, 2560x1440, 24 fps, 72 frames (t = frame/24). The camera is static. A black wheeled robot sits
at the bottom centre. A small black cylindrical drone (4 arms with spinning rotors on a light-grey top plate) rises
straight up out of the robot's top. The robot's hinged hatch lid, open to the upper left at the start, swings
right over the hatch from frame 22 to the end. All values are in pixels (x right, y down). No metric scale is given.

## Files
- `scene.json`: inventory, static sizes, events, camera.
- `tracks/drone.csv`, one row per frame (0-71):
  - `ref_x, ref_y`: drone reference point = centre of its full bbox (x = cylinder axis, y = midpoint of top and bottom).
  - `top_y`: top of the drone, measured.
  - `bottom_y`: bottom of the cylinder. Measured when `bottom_measured=1` (frames 26-71). Otherwise it is top_y + 194.
  - `bbox_*`: rigid arm span in x. y goes from top to the visible bottom (clipped at the robot top, y = 989).
  - `height_px`, `visible_height_px`.
  - `arm_span_px`: rigid arms, 231 px.
  - `blade_span_px`, `blade_left/right`: includes the motion-blurred blade tips, so it is noisy.
  - `cyl_top/bot/width`.
  - `occluded`: 1 = the bottom is inside the robot.
- `tracks/lid.csv`: hinge assumed at (1197, 992).
  - `tip_x, tip_y`: lid pixel farthest from the hinge.
  - `length_px`.
  - `angle_deg`: measured from image +x, counter-clockwise with y up (90 = vertical).
  - Lid mask bbox and pixel count.
- `scripts/track_drone.py`: background-difference mask (composite background from frames 0 and 48) plus a dark-pixel cylinder finder.
- `scripts/track_lid.py`: temporal-median background difference, with the drone box masked out.
- `scripts/static_robot.py`: robot extents at frame 48.
- `scratch_drone_raw.csv`: an obsolete first pass. Ignore it; use `tracks/drone.csv`.
- Overlays I checked are in `../frames/dbg/` (d*.png, lid*.png, robot48.png).

## Key measurements
- **Drone size:** height (top bar to cylinder bottom) 194 px. Cylinder 173 px tall × 81 px wide. Rigid arm span 231 px (x 1220-1451). Blade tips with blur reach up to about 280 px.
- **Drone position:**
  - x is constant at 1330.5.
  - top_y: 940 at frames 0-1, 933 at frame 2, then falls steadily (about 7 px per frame) to 457 at frame 71.
  - Centre y: 1037 at frame 0 down to 556 at frame 71.
  - It moves straight up with no sideways motion and is still rising at the end of the clip.
- **Robot (static):** bbox x 1048-1442, y 985 (top of body) to about 1392 (bottom of wheels; the wheel bottoms are partly hidden behind a ground ridge).
  - Body width 394 px.
  - Body height without wheels about 323 px; total height about 407 px.
  - Bbox centre about (1245, 1188).
- **Lid:**
  - Static at 142.4° (pointing up-left) for frames 0-21.
  - Swings clockwise from frame 22: passes vertical between frames 46 and 47, reaches 16.8° at frame 71 and is still closing.
  - Hinge to tip is about 203 px.

## Events
| Event | Frame | t (s) |
|---|---|---|
| Drone starts rising (moves between frames 1 and 2) | 1 | 0.042 |
| Lid starts swinging | 21-22 | 0.875-0.917 |
| Cylinder bottom clears the robot top | 26 | 1.083 |
| Lid passes vertical | 46-47 | 1.92-1.96 |

The clip ends at frame 71 (t = 2.958 s) with both the drone and the lid still moving. There are no bounces or impacts.

## Reliability / ambiguities
- **Drone `top_y`:** about ±1 px, since the top edge is crisp. Use it, or `ref_y`, for vertical displacement and speed. Since the body is rigid, both give the same per-frame differences, except in frames 0-25, where `ref_y` is derived from top_y.
- **Drone origin:** not visible in the image. I used the bbox centre. The real Blender origin could sit higher, near the plate or rotor level, but a constant offset does not affect speed or displacement.
- **Early frames (0-25):** the lower part of the drone is hidden inside the robot, so `bottom_y` and `ref_y` there are inferred from the rigid height of 194 px. Frames 0-2 also blend with the robot's top and lid, so arm spans there are noisier.
- **`blade_span_px`:** unreliable because the rotors spin and blur. For drone width, use `arm_span_px` (231).
- **Lid:** angle accurate to about ±2°. The apparent length shrinks from 203 to 187 px as the lid swings, probably from foreshortening or which tip feature gets picked, so treat the lid as roughly planar. The hinge position is estimated to within about ±5 px.
- **No similar objects to confuse:** there is one drone, one robot and one lid. The background is static.
