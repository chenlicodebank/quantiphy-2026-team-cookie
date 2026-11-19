# simulation_0056: measurement record

3D Blender render, 2048x2048, 62 frames at 29.993562 fps (t = frame/fps). The camera is **static**. It sits at street
level and looks down a wet city street. Three objects move:

- **orange_car**: orange sports sedan, front-on, driving toward the camera in the near lane next to the left curb.
- **dark_car**: dark green vintage coupe with lit headlights in the far lane. It moves right and toward the camera and
  leaves the frame through the right edge.
- **man**: man in a navy jacket and grey trousers, walking away from the camera on the left sidewalk.

Everything is in full-resolution pixels (x right, y down). No metric scale is assumed.

## Files
- `scene.json`: inventory (moving and static objects, with pixel extents), camera, vanishing point, events.
- `tracks/orange_car.csv`: every frame 0-61. Columns:
  - `ref_x, ref_y`: bbox centre, used as the proxy for the car origin.
  - `bottom_center_x, bottom_y`: bottom of the front bumper, about the ground contact.
  - `x0 y0 x1 y1`, `bbox_w`, `bbox_h`.
  - PCA extents of the paint mask (`mask_axis_len`, `mask_axis_wid`, `mask_axis_angle_deg`).
  - `orange_paint_top_y`.
  - `edge_fixed`: names any box edge that was repaired.
- `tracks/dark_car.csv`: frames 0-50. Columns:
  - `x0, y0, x1`: from the automatic mask.
  - `y1`: lowest wheel bottom, linearly interpolated from manual keyframes.
  - `ref_x, ref_y`: bbox centre. `ref_x` and `bbox_w` are left empty when the car is cut by the right edge
    (`truncated=1`, f35 on).
  - `visible_w`: always filled.
  - `manual_left_x / manual_top_y / manual_right_x`: interpolated keyframe readings.
  - `mask_cx, mask_cy`: centroid of the difference mask.
- `tracks/man.csv`: frames 0-61, linearly interpolated between 14 manual keyframes (`keyframe=1`):
  - `head_top_y`, `lowest_foot_y`, left and right extents (arms included).
  - `ref_x`: hip midpoint x.
  - `ref_y`: estimated pelvis, = lowest_foot_y - 0.51 x (lowest_foot_y - head_top_y).
- `tracks/*_raw.csv`: the automatic per-frame masks before any correction. `man_jacket_raw.csv` is the navy-jacket
  mask; it is unreliable, see below.
- `manual_keyframes.json`: the hand readings used for the man and the dark car.
- `scripts/`:
  - `bg.py` / `bg_full.py`: camera-shift check and median background.
  - `track.py`: automatic segmentation.
  - `zoom.py`, `man_zooms.py`, `orange_zooms.py`: gridded zooms for the manual readings.
  - `static_view.py`: static-object measurements.
  - `assemble.py`: final CSVs.
  - `check_overlay.py`: visual check.
  - `bg_man.py`, `man_try.py`, `diffview.py`, `darkview.py`: experiments.

## Methods and reliability
- **Camera**: phase correlation between frames shows less than 0.003 px shift, so the camera is fixed. No background
  correction is needed.
- **orange_car**: an HSV orange mask, made by joining the nearby orange parts and filling their convex hull. The top
  edge is then extended over the dark windshield and roof using the difference from the median background.
  - The box was checked on zoomed crops at f0, 10, 20, 30, 40, 46, 52 and 61. It is good to about ±3 px; at f0 that
    covers mirror to mirror and roof to bumper bottom.
  - The shaded left side panel drops out of the mask at f19-20 and f43-51. In those frames x0 was replaced by linear
    interpolation (marked in `edge_fixed`); those values are good to about ±5 px.
  - The bottom is the front bumper. The tyres are only a few px lower, and the wet-road reflection is excluded.
  - The box is the visible silhouette of a car seen nearly head-on, so `bbox_w` is about the car's width, not its
    length. The car's length is not observable.
  - The box centre lies above the true 3D centre of the car, because we see the front face and the top. Treat it as an
    approximation of the origin.
- **dark_car**: background-difference mask with threshold 40.
  - Left, right and roof edges agree with the manual readings to about ±5 px (f0-30).
  - The automatic bottom edge includes the car's dark shadow and reflection on the wet road, about 50 px too low. It
    was therefore replaced by manual wheel-bottom readings (f0, 5, ..., 45, 48), good to about ±8 px.
  - Headlight glare and motion blur after f25 widen the edges by up to about 10 px.
  - From f35 the car is cut by the right image edge: only the visible part is recorded, the centre is unknown, and
    after f45 only the rear wheel and tail are visible.
  - The car turns as it crosses, so its visible side changes: the front and left side early, more of the left side
    later.
- **man**: automatic masks failed. He moves slowly, so the median background contains him, and his grey trousers
  match the grey sidewalk; puddles and reflections also leak in. Extents were instead read by hand at f0, 5, 10, ...,
  55, 58 and 61 on zoomed crops with a 25-px grid.
  - Head top and side extents: about ±5 px.
  - Lowest foot: about ±8 px. It changes with gait: the near foot is lowest at heel strike, which is why the apparent
    height wobbles (858, 780, 811, 791 px at f0-15).
  - Between keyframes the values are linear interpolations, so gait detail within each 5-frame gap is lost.
  - The pelvis point is an anatomical estimate (about 51% of the height above the lowest foot, at the hip midpoint).
    It sits near the jacket hem, uncertain by about ±25 px.
  - For rest standing height, use frames where both feet are close together. Max and min apparent height can be read
    from `bbox_h`, but it shrinks with distance.
- **Static objects** (in `scene.json`): measured on the median background with gridded zooms.
  - Hydrant: ±4 px.
  - Near lamp post: its base is hidden behind the hydrant cap, so the bottom is ±15 px.
  - Far lamp post: ±10 px.
  - Road vanishing point (923, 1050): ±30 px. It comes from the solid road-edge line and the dashed centre line.
    Points on both lines are in `scene.json`.

## 3D and perspective cues
- The ground plane is the road and sidewalk; the horizon is at about y = 1050.
- The orange car's apparent width grows from 185 to 785 px (about 4.2x), so its depth falls by roughly that factor,
  assuming a constant view angle.
- The man's apparent height falls from about 858 to 650 px; he is moving away.
- The dark car grows from 170 to 371 px wide between f0 and f30; it gets nearer while crossing to the right.
- The focal length is unknown. Estimate it from the given depth_info together with a known size, e.g.
  f = pixel_size x depth / real_size for an object seen roughly face-on, then back-project positions with the
  principal point at (1024, 1024).

## Events
- All three objects are already moving at f0 and keep moving.
- The orange car never stops before the clip ends (f61).
- The dark car reaches the right edge at f34-35, is partly out of frame afterwards, and its last sliver is gone by
  about f52.
- No contacts or collisions. The man and the cars never overlap in the image.

## Ambiguities
- The wet road gives strong reflections and shadows under both cars. They are excluded from the boxes, but the raw
  dark-car `y1` still includes them.
- The car "origin" is taken as the bbox centre, and the human origin as the estimated pelvis. These are proxies for
  the true 3D origins.
- There are two lamp posts: "near" is the tall one behind the hydrant, "far" the smaller one farther down the
  sidewalk.
