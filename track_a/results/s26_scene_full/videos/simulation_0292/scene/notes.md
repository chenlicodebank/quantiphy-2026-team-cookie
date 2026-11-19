# simulation_0292 – measurement record

2D simulation render, 24 fps, 72 frames (0-71, t = frame/24), 2560x1440. Pixel coordinates: x right, y down.
The camera is static; there is no pan or shake. The cart's pixels are unchanged between frames 0 and 71 except where the lid moves.

## Scene
A static black delivery cart (robot box on two visible wheels) stands on a grey studio floor with no markings.
- **drone**: the only object that moves through space. A black drone with a wide top plate, 4 arms with spinning props, and a
  cylindrical body below. It starts docked in the cart: in frames 0-1 only its plate shows above the roof. It then flies
  **straight up** at a **constant pixel speed** until the end of the clip.
- **lid**: the cart's hinged hatch/handle frame. At the start it is open and tilted up-left. It rotates about a hinge at about (1187, 995)
  over the top and down to the right, and is nearly closed at frame 71, where it is still moving.
- **cart**, **left_wheel**, **right_wheel**, **floor_backdrop**: static.

## Files
- `scene.json`: inventory, static extents, drone sizes, events, camera.
- `tracks/drone.csv`: one row per frame (0-71):
  - `ref_x, ref_y`: drone bounding-box centre (the reference point / origin). `ref_y = top_y + 194.14/2`, and `ref_x = 1333.5 +` the template x-shift.
  - `top_y`: sub-pixel top of the dark plate rim, from normalised cross-correlation with a frame-71 template of the plate. Accuracy is ~0.3 px.
  - `body_bottom_y_measured`: integer row of the body's bottom. Empty while the body is hidden inside the cart (frames 0-25).
  - `bottom_y_from_height`: top_y + 194.1.
  - Body, plate and prop x extents and widths.
  - `height_px_const` (194.1) and `height_px_measured`.
  - `occluded_bottom`: 1 means the lower part of the drone is hidden by the cart.
- `tracks/drone_raw.csv`: the integer threshold measurements (gray < 80) behind the track.
- `tracks/lid.csv`:
  - `tip_x, tip_y`: lid tip, the dark pixel farthest from the hinge.
  - `angle_deg_from_left_horizontal`: lid angle about the fitted hinge (1187, 995). 0 = pointing left, 90 = straight up, 180 = pointing right.
  - Visible bbox of the lid above the roof.
- `scripts/`:
  - `track_drone.py`: threshold track and overlays.
  - `subpix_drone.py`: sub-pixel template track.
  - `build_record.py`: merges both into drone.csv and runs the linear-fit check.
  - `track_lid.py`, `measure_static*.py`, `true_top.py`, `check_lid.py`: lid tracking, static extents, rim offset and overlay check.
  - `views.py`, `probe.py`: viewing and probing helpers.

## Key numbers (pixels)
- **Drone motion**: frames 0 and 1 are identical (at rest, top_y 956.44). From frame 1→2 to frame 70→71 the drone rises
  7.14 px/frame (171.4 px/s), the same every frame. A linear fit leaves 0.27 px rms residual, and the quadratic term is about 0, so there is no
  measurable acceleration after take-off. Per-frame steps range from 6.7 to 7.8 px, which is noise. Horizontal drift is under 1 px.
  The total rise is 499.4 px (top_y 956.44 → 457.0, frame 1 → 71). The path is straight, so path length equals displacement.
  Take-off: frame 2 (t = 0.083 s) is the first moved frame. Speed jumps from 0 to the full value in one frame.
- **Drone size**:
  - Height (dark plate top → body bottom): 194.1 px (sd 1.2).
  - The visible bright top rim adds ~6 px while the drone is low (plate seen from above) and ~1 px when high, so the full height is 195-201 px.
  - Top plate (dark rim, with motor arms): 231 px wide.
  - Body cylinder: ~88 px wide (83-88).
  - Prop-tip span: up to ~353 px (x 1159-1512). It changes every frame because the props spin.
  - The world bbox "length/width" of the drone is most likely the plate or prop span.
- **Cart** (static, measured at frames 30 and 71):
  - Roof at y ≈ 983. The wheel bottoms / ground contact are at y ≈ 1434, so roof to ground is ≈ 451 px.
  - Body box x 1074-1439 (366 px). With the sloped front this widens to 1066. With wheels the overall span is x 1030-1459 (430 px).
  - Wheels are about 110-130 px across (x 1030-1140 and 1330-1459, y 1305-1434). These are approximate.
- **Lid**:
  - Hinge (1187, 995); hinge to tip ≈ 197 px.
  - At rest at 40.5° (up-left) for frames 0-21. Starts rotating at frame ≈ 22.
  - Reaches 90° at frame ≈ 45 and 163.8° at frame 71, still rotating at about 1.5-3.5°/frame.

## Events
| event | frame | time (s) |
|---|---|---|
| drone at rest | 0-1 | 0-0.042 |
| drone take-off (first moved frame) | 2 | 0.083 |
| lid starts rotating | ~22 | ~0.92 |
| drone body fully clear of the roof | 26 | 1.083 |
| lid vertical | ~45 | ~1.875 |
| clip ends (drone and lid still moving) | 71 | 2.958 |

There are no bounces or impacts.

## Reliability and ambiguities
- **Drone vertical track**: very reliable, ~0.3 px. Its origin is taken as the bbox centre, which is a constant offset from the top,
  so speeds and displacements do not depend on that choice.
- **Bottom of the drone**: hidden in frames 0-25. Use `bottom_y_from_height` there.
- **Plate-left and prop-left extents**:
  - In frames 0-8 the plate's left edge merged with the lid, so it was reconstructed from symmetry (1220).
  - In frames ≤ 25 the left prop extent is clipped to 1150 because the open lid lies in the same rows.
  - Prop extents are motion-blurred, semi-transparent streaks, accurate to ±5 px.
- **Lid**: tip is accurate to ±3 px and angle to ±1.5°. Around frames 46-49 the tip passes near the drone exclusion box and is slightly less reliable.
- **Cart and wheel extents**: ±3 px. The wheel outlines blend with the chassis.
- **Scale**: no metric scale is assumed. With a size prior (e.g. drone height or cart size), use a single m/px scale. The drone and cart are in
  the same plane, and the drone's apparent width is constant, so its depth does not change.
