# simulation_0057 – measurement record

Video: Blender render, 2D scene, 1080x1080, 91 frames at 30.003297 fps (t = frame / fps; frame 90 = 3.000 s).
The camera looks straight down at a street (top view). Image axes: x to the right, y downwards. Everything here is in pixels and seconds. No metric scale is assumed.

## Scene content
- **orange_car** (the only moving object): an orange sports car seen from above, with its headlights at the bottom. It drives straight down the image in the left lane, next to the left curb. Its front is already in view at frame 0. Frames 0–16 are clipped by the top edge of the image; from frame 17 to 90 the whole car is in view. It slows down smoothly the whole time: the per-frame step falls from about 18.6 px (frame 8) to about 3.5 px (frame 90). It never stops inside the clip. It also drifts slightly left (x about 356 → 348). There are no collisions or contacts.
- Static objects (scene.json → static_objects):
  - Left curb strip at x 281–292 and right curb at x 850–855 (road about 563 px wide).
  - Worn white lane lines: solid left line at x 336–341, dashed centre line at x 567–573, right line at x 799–804. Lane width between line centres is about 231.5 px.
  - Two black lamp posts on the left sidewalk. The hexagonal heads are about 41x38 px, centred at (195.5, 450.1) and (195.3, 979.8), so they are 529.7 px apart. Each has an arm to a post base at x about 251.
  - A small white/rust fire hydrant at about x 227–265, y 939–979, next to the lower lamp.
  - Paved sidewalks, a grass strip at the far left, and dark road patches/potholes (static texture).

## Files
- `scene.json`: inventory, static extents, events, camera, car size, example positions.
- `tracks/orange_car.csv`: one row per frame (0–90):
  - `cx_best_px, cy_best_px`: **use these as the car's reference point (its origin)**.
    - Frames 7–90 come from template matching with sub-pixel peaks. The template is the front 136 px of the car taken from frame 60, and the position is anchored to the centre of the frame-60 bounding box.
    - Frames 0–6 are estimated as front edge (y1) minus half the median length (288 px), then corrected by the mean bias seen in frames 7–12 (−10.1 px in y; the blurred front edge sticks out ahead of the car). In frame 0 only y is given.
  - `x0,y0,x1,y1`: bounding box of the orange colour mask, from an HSV threshold plus a 41 px morphological closing, with x < 272 masked off to exclude the hydrant.
  - `length_px_vertical`: length along the motion (vertical). `width_px`: width across it. Height cannot be seen from the top view.
  - `occluded_or_clipped`: 1 for frames 0–16 (clipped by the top edge). Nothing occludes the car.
  - Raw columns: `cx/cy_bbox`, `cx/cy_centroid`, `cy_est_full_car_px`, `cx/cy_tm_px`, `tm_score`.
- `scripts/`, run in this order: `track_car.py` (mask, bounding box, camera check) → `refine_template.py` → `finalize.py` (best columns, scene.json). Also: `static_features.py`, `static_objects.py`, `overlay.py` (draws a visual check to frames/overlay.png), `check_template.py` (cross-check). Small JSON outputs: `bg_shift.json`, `static_objects.json`.

## Reliability
- **Camera:** static. Phase correlation of the right sidewalk gives at most 0.5 px x and 0.01 px y shift over the clip.
- **Car size:** 288 px long (median of frames 17–90, range 286–293; the larger values are early frames lengthened by motion blur) and about 110 px wide (108–112). Mirrors are dark and not included. A size prior for the car should be matched to the 288 px length (bumper to bumper, along the motion) or the 110 px width.
- **Car positions:**
  - Frames 7–90: displacements are good to about 0.3 px. Front, rear and whole-car templates agree within about 1 px over 30 frames. For example, 60→90 measures 186.6 (front), 187.3 (rear) and 186.9 (whole) px.
  - The bounding-box centres from the colour mask are less accurate: about 2–4 px error, from motion blur and shading at the mask edges. Use the best columns.
  - The absolute origin carries a constant offset uncertainty of about ±3 px. Distances to static objects therefore have an error of about ±3 px.
  - Frames 0–6 are only good to about ±3 px; the step from frame 6 to 7 shows a visible 14 px vs 18.6 px glitch. Prefer frames ≥ 7 for speeds.
- **Motion blur:** noticeable in the early, fast frames.
- **Shadows:** no strong shadows of the car.
- **Ambiguity:** the hydrant is the only other orange-ish object and was excluded. The lane-line dashes are worn and irregular, so no reliable dash length was measured.
- **2D scale:** one metres-per-pixel scale for the whole frame. The view is top-down, and the car moves on the road plane.

## Events
- Frame 0: the car is already moving and partly in view (front 22 px).
- Frame 17 (0.567 s): the car is fully inside the frame.
- Throughout: steady deceleration. There is no stop, turn, contact or collision; the car is still moving at frame 90.
