# simulation_0182 — measurement record

3D Blender render, 1920x1080, 24 fps, 40 frames (t = frame/24, 0 – 1.625 s). Camera is **static**: outside the box, frames 0 and 39 are identical, so there's no per-frame background shift.

## Scene
A single brown cardboard box (loose top flaps) starts **at rest in the air** at upper-left, just right of two stacked crates on a shelf. It falls, lands on the top of a blue inclined roller-conveyor ramp, tips onto the slope and slides down-right toward the camera. The video ends with the box at the bottom end of the ramp, next to a wooden floor/pallet. Static scenery: brick/breeze-block wall, orange crate "PRODUCT OF ITALY" and tan crate "SEEDLESS JAFFAS" (top-left), wooden shelf board, blue support post, orange wall sign "TAKE CARE WHEN STACKING CRATES" and the wooden floor at bottom-right. Image positions and pixel sizes are in scene.json. The box is the only moving object, so nothing else could be confused with it.

## Files
- `scene.json`: inventory, static-object image boxes, box pixel dimensions at frame 0, events, camera/perspective cues.
- `tracks/box.csv`: one row per frame (0–39) with these columns:
  - `cx,cy`: mask centroid (the reference point, a proxy for the box origin/centre)
  - `bbox_cx,bbox_cy`: centre of the bounding box
  - `x0..y1`, `bbox_w/h`: bounding box
  - `area_px`, `sqrt_area`: mask area (apparent-size indicator)
  - `rect_len/rect_wid/rect_angle_deg`: min-area rectangle, i.e. length along the main axis, width across it, and tilt
  - `occluded`: 1 when the mask touches the image border
- `scripts/track_box.py`: segmentation and tracking. The background is frame 39, with its bottom-right patch replaced by frame 0. The mask comes from a |difference| > 30 threshold, then morphology, then the largest component with holes filled. The script also writes overlays to `frames/ov_XX.png`.

## Reliability
- I checked the masks visually at frames 0, 9, 12, 21, 30 and 39. They cover the whole box, including the flaps, with no shadow leakage worth noting. I estimate the centroid is good to about 2–3 px.
- The centroid is the centre of the visible silhouette, not the projected 3D centre. Because the box is seen corner-on, the two differ by a few px. While the box tilts (frames 8–13), the centroid also moves partly because of the rotation.
- **Frames 36–39:** the bottom of the box is cut off by the image edge (`occluded=1`). This pulls the centroid up and to the right, and the area values are too small. For these frames `x0`, `x1` and `y0` are still usable (for example, track the top/left edges).
- Box pixel sizes at frame 0 (upright, corner-on view, nearest vertical edge at x≈605):
  - total width 397 px; left face 227 px; right face 170 px
  - nearest vertical edge 205 px tall
  - mask height including flaps 222 px

  The faces are foreshortened, so which face matches the box's true length or width is ambiguous.
- Apparent size: `sqrt_area` stays at about 271 px while falling (frames 0–8), then grows to about 282 px (frames 12–20) and about 289 px (frames 28–35). The box gets closer to the camera as it slides, and its rotation adds to the change.

## Events
| Frame(s) | t (s) | Event |
|---|---|---|
| 0 | 0 | Release from rest. `cy` moves 1.3, 6.3, 10.0, 12.3, 19.2, 21.4, 26.2 px per frame (free fall). |
| 8 | 0.333 | First contact with the ramp. The box's lower-left corner touches between frames 7 and 8. |
| 8–13 | 0.333–0.542 | The box pivots onto the slope; its image tilt goes from 0° to about 26–33°. |
| 13–39 | 0.542–1.625 | The box slides down the ramp at roughly constant orientation, speeding up. Image direction is about 31.5° below horizontal, matching the ramp's far edge (720,540)→(1460,990). The centroid step grows from about 17 px to about 43 px per frame. |
| 36 | 1.5 | The box reaches the bottom edge of the image. |
| 39 | 1.625 | The video ends before the box stops. |

## Ambiguities
- No metric scale is known. Use the question's prior and depth_info, and estimate the focal length from them.
- The motion has a depth component: the ramp descends toward the camera, so the image displacement understates the true 3D displacement on the ramp. Use the depths when they are given.
