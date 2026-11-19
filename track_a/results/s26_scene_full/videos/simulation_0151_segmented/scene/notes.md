# simulation_0151_segmented: measurement notes

**Video:** 1920x1080 px, 24 fps, 42 frames (0–41), 1.75 s. It is a 3D Blender scene with the background segmented out to white. Time is t = frame/24.

## Scene
- There are two moving vehicles and nothing else. No ground, road, markings or furniture survive the segmentation.
  - **car**: a yellow sports coupe. It is nearer the camera and bigger.
  - **cart**: a small light-blue utility/golf cart with a roof on posts and a slanted rod rising above its rear. It is farther away, behind the car.
- Both drive from right to left (−x) and only horizontally. Image rows stay constant: car y 528–882, cart y 490–818.
- Both start from (near) rest at frame 0 and speed up. Their image speed peaks around frames 25–33 and then eases off slightly, which looks like a keyframed ease-in/ease-out. Neither changes direction.
- The car overtakes the cart by passing in front of it (nearer the camera). They never touch.
- **Visible window:** object pixels only ever appear in x = 94..1833. Anything outside that band is cut to white. An edge sitting at 94 or 1833 is clipped, not a real end of the object.
- **Camera:** assumed static, as the benchmark's Blender clips use a fixed camera. This cannot be checked against a background because none is left. Both objects keep a constant size and image row, which is consistent with a static camera.
  - It is a side view. In the right part of the image (x > ~1400) the vehicles are also seen a little from the front, because of off-axis perspective.
  - Perspective cues: the car's tyres touch y = 882 and the cart's touch y = 818. The farther cart therefore stands higher in the image, so the camera is above the ground. The horizon is not visible.
  - Apparent size over time is constant for both objects, so each moves at a roughly constant depth.

## Files
- `scene.json`: the inventory, pixel sizes, wheel measurements, camera and perspective cues, and events.
- `tracks/car.csv` and `tracks/cart.csv`: one row per frame in which the object is present. Columns:
  - `cx, cy`: the reference point, an estimate of the side-view bounding-box centre used as a proxy for the origin.
  - `front_x` / `rear_x` (car) and `front_x` / `roof_front_x` / `rear_post_tip_x` (cart): the measured feature positions, left blank when hidden or clipped.
  - `vis_*`: the visible-mask bbox.
  - `est_*`: the estimated full bbox, computed as cx ± L/2.
  - `vis_length`, `vis_height`.
  - `clipped_by_window`: L or R.
  - `occluded`: for the cart only, set while the car hides part of it.
  - `cx_source`: how cx was obtained.
  - `reliability`.
- `raw/features.json`: per-frame mask extents and feature positions. `raw/build_constants.json`: the lengths and offsets used.
- `scripts/`:
  - `masks.py`: colour segmentation, which also writes the overlay sheets.
  - `features.py`: per-frame edges.
  - `build.py`: writes the tracks.
  - `check_overlay.py`: draws the tracks on frames for checking.
  - `wheels.py`: wheel spans.
  - `view.py` and `probe.py`: viewing helpers.

## Method
**Masks**
- Foreground means any channel < 225.
- **Car:** the convex hull of the large yellow components (HSV hue 8–32, sat > 70), plus the non-blue foreground just below the body (tyres). Only the largest component is kept. The car is never occluded because it is in front.
- **Cart:** foreground components that don't touch the dilated car mask and contain blue pixels (hue 85–125).
- I checked the masks and boxes visually (`frames/mask_sheet_*.png`, `frames/check_tracks.png`). They cover the right object and its full visible extent.

**Car reference point**
- Car length L = 1153.5 px, the median over frames 22–27, the only frames where both ends are inside the window. The spread is 1151–1160 px.
- Frames 22–27: cx = (front + rear)/2.
- Frames 0–21: cx = front (nose) + L/2.
- Frames 28–39: cx = rear − L/2.
- cy = 705 is fixed: the midpoint of the roof (528) and the tyre bottom (882).

**Cart reference point**
- Frames 32–41 (fully visible): cx = (x0 + x1)/2, with length 374 px.
- Frames 15–31: the average of two estimates calibrated on frames 32–41:
  - rear-post tip x − 186.5;
  - roof front tip x + 118.75.
  
  Both features stay visible above the car's roof.
- Frames 0–14: the post is outside the window, so only the roof front tip (frames 0–1 and 10–14) or the cart's front edge (frames 2–9) is available.
  - On the right side the cart looks ~22 px longer in these features (oblique view), so single-feature estimates read low.
  - To compensate I added +11 px, half the post-vs-roof spread measured in frames 15–19.
- cy = 654 is the bbox midpoint including the post (490..818). The body-only midpoint would be 665.

**Sizes (side view, px)**
- Car: length 1153.5, height 354. Wheelbase ≈ 700 (hubs at x 633.5 and 1333.5 in frame 24). Tyre diameter ≈ 175–186.
- Cart: length 374 including the rear post (370–375), height 328 to the post tip or 305 to the roof top. Wheelbase ≈ 226.5. Tyre diameter ≈ 80.
- The vehicles' widths (depth axis) cannot be measured.

## Reliability
- **Car**
  - Frames 22–27: high, ±2 px.
  - Frames 9–21 and 28–37: medium. They rely on a constant L, which held to within ~8 px; expect ±5–10 px.
  - Frames 0–8: low. Only the nose is visible at the right window edge and is seen obliquely, so the nose silhouette shifts; expect ±10–15 px. The 0→1 step is only ~4 px.
  - Frames 38–39: a blurred brown segmentation blob of the car's rear (artefact), low reliability. The car is absent in 40–41 although its rear should still be just inside the window, so the segmentation lost it.
- **Cart**
  - Frames 32–41: high, ±1–2 px.
  - Frames 15–31: medium, ±3 px. The spread between the two feature estimates shrinks from 25 px at the right side to under 4 px from frame 27 on.
  - Frames 0–14: low–medium, ±8–12 px, because of a single feature and the obliquity correction. The step between frames 9 and 10, where the source switches from front edge to roof tip, is noisy.
- Per-frame differences of cx inherit these errors. When fitting speed or acceleration, prefer fits over many frames, or a single feature such as `front_x`, `rear_x` or `rear_post_tip_x` over a stretch where it is continuously visible.

## Ambiguities
- **Similar objects:** none. The two vehicles differ clearly in colour and size.
- **Shadows:** none, since the background has been removed.
- **Motion blur:** slight on the car at high speed.
- **Segmentation artefacts:** a beige streak on the car roof (frames 29–30), the car blob in frames 38–39, and the hard window clip at x = 94/1833.
- **Origin vs bbox centre:** the true origin of each vehicle rig may not sit at its side-view bbox centre. The car's wheel midpoint is 31 px left of the bbox centre (in frame 24). Positions differ by a constant offset either way, which doesn't affect speeds.
