# internet_0056 – measurement record

Internet video, 2D, 30 fps, 58 frames (0–57, t = frame/30, 0–1.90 s), 1920×1080. All values are pixels and seconds;
no metric scale is assumed anywhere.

## Scene
A sunny campus plaza filmed handheld from a nearly fixed position. A person (cream cap, white long-sleeve top,
khaki cargo trousers) rides a dark grey/black electric kick scooter **left → right**, side-on to the camera, across
the whole clip. They go from sunlit pavement (left) into the building's shadow (right). Behind them is a row of
wooden bollards with red bands. A small background pedestrian (dark clothes, backpack) walks slowly right beside
the sandstone building and goes behind a pillar. Two parked utility/golf carts, palms, lamp posts, a bike rack and
the building are static.

## Files
- `scene.json`: inventory (moving and static objects with pixel positions and extents), events, camera,
  recommended scooter length, rider height.
- `tracks/scooter_rider.csv`: one row per frame (0–57). Raw image coordinates. Columns:
  - `cx,cy`: centre of the clean bounding box (the reference point "visible centre").
  - `bbox_*`: box from the scooter's rear tyre edge to the front tyre edge (or handlebar if further right), and from
    the cap top to the bottom of the wheels.
  - `body_centroid_*`: centroid of the body mask above the wheels.
  - `scooter_rear_x`, `scooter_front_x`: outer tyre edges. `scooter_len_px` = wheel to wheel, which is the scooter's
    length along the motion. This is the "bumper-to-bumper" quantity.
  - `rear_axle_*`, `front_axle_*`: wheel centres. `axle_dist_px` = distance between them.
  - `head_top_y`, `ground_y` (wheel bottoms) and `height_top_to_ground_px`.
  - `bbox_w_px`; `mask_area_px` (body mask area above the wheels); `occluded` (0 throughout).
  - `bg_dx,bg_dy`: camera shift of this frame.
- `tracks/pedestrian_backpack.csv`: the background walker. Columns are the mask centroid, bbox, visible height and
  width, and an occlusion code: 0 = fully visible (frames 0–15), 1 = legs hidden by bushes (16–49), 2 = going behind
  a dark pillar at x≈1440, only a sliver visible (50–57; position meaningless).
- `tracks/camera_shift.csv`: per-frame background displacement relative to frame 0.
- `scripts/`: in order:
  - `camera_shift.py`
  - `build_bg.py`: median background, `bg_roi.npz`.
  - `track.py`: first segmentation pass, exploratory.
  - `track_wheels.py`: chained template tracking of both wheels, `wheels.json`.
  - `wheel_edges.py`: refines the tyre edges from grey-level profile steps, `wheels_refined.json`.
  - `assemble.py`: final CSVs and check overlays.
  - `static_objects.py`: zoom sheets used to read the bollards.
  - `inspect_bottom.py`, `zoom_wheels.py`: inspection helpers.

## Methods and reliability
- **Camera.** Handheld with a slow, smooth drift. The shift is the median template-match displacement of 8 static
  patches (bollards, white post, windows, arch, palm trunk, lamp post, ground marks). It reaches dx = −7.4 px and
  dy = −2.8…+1.0 px by frame 57. The patches disagree by up to ~1.7 px at the end (slight rotation or parallax). For
  motion against the scenery, subtract `bg_dx` from x. The drift is about 1 % of the rider's ~614 px travel.
- **Rider segmentation.** Difference against a shift-compensated median background (threshold 40). The rider casts
  a ground shadow behind them (to the left) while in sun, and this inflates a raw mask by up to ~80 px. The shadow
  is therefore excluded:
  - The box's horizontal extent comes from the tracked tyre edges plus the body mask above the wheels.
  - The bottom is the wheels' ground contact.

  Overlays checked at frames 0, 8, 15, 22, 30, 38, 45, 52 and 57: the box hugs cap to wheels and rear tyre to front
  tyre.
- **Scooter length (wheel to wheel).** Checked by eye on 6× zooms:

  | frame | 0 | 8 | 15 | 22 | 30 | 38 | 45 | 57 |
  |---|---|---|---|---|---|---|---|---|
  | length (px) | 119 | 122 | 122 | 127 | 127 | 127.5 | 127 | 128 |

  The per-frame file agrees within ~2 px; the uncertainty is ±2 px per frame. **Recommended value: 127 px** (stable
  126–128 px from frame ~20 on). Early frames are smaller, ~120 px for frames 0–7. The apparent growth while the
  rider moves from the left edge toward the centre is probably a slight change in viewing angle or distance; the
  rider's height grows too (205 → 215 px, about 5 %). If a question's prior is the scooter's length, a reader would
  most likely measure ~127 px, at mid-clip or later. The axle-to-axle distance is ~99 px (frames 20–57). Wheel
  diameters are ~26 px (rear) and ~29 px (front).
- **Rider height.** Cap top to ground is 205 px at frame 0 and 213–215 px from frame 30 on (±3 px). The person stands
  on the deck, about 10–12 px above ground, so the person alone is ≈ 195–203 px.
- **Rider motion.** Moving right in every frame. There is no start, stop, release, bounce, contact or direction
  change. The ground line stays at y ≈ 758 and the vertical motion of `cy` is only a few px (perspective/drift). Good
  points for position-versus-time are `scooter_front_x`, `scooter_rear_x`, `rear_axle_x`, `front_axle_x` and `cx`;
  all are consistent with one another within ~1–2 px per frame.
- **Weaker columns.** `body_centroid_*` is less reliable in frames ~51–57: in the shade the dark trousers blend into
  the dark background, so the mask loses part of the legs and the centroid moves up/down by ~5–15 px. Prefer `cx` or
  the wheel points.
- **Front tyre edge in sun–shade transition frames** (0–20, 42–57): this comes from the template tracker corrected
  by −2 px where the edge step was weak, so it carries ±2 px.
- **Pedestrian.** Mask centroid. Fully visible ~103 px tall (frames 0–15) while walking right at a slow image pace.
  Afterwards the box only covers the upper body, so the centroid drifts upward. Low priority, small object.
- **Static objects.** Read on 4× zooms of the median background (frame-0 coordinates, ±1.5 px); see `scene.json`.
  - Bollards 1–6 stand roughly on one line at about the rider's depth, each ~96–100 px tall and ~22–25 px wide.
  - Bollard 7 (122 px), the white post (98 px tall, 38 px wide) and bollard 8 (177 px) are nearer the camera on the
    right. They are not at the rider's depth, so they are not usable as same-plane references.

## Ambiguities
- "Length of the scooter" could be read as wheel to wheel (~127 px) or axle to axle (~99 px); the wheel-to-wheel value
  is the natural bumper-to-bumper analogue.
- "Rider" can mean person or person + scooter. The box covers both, and the person-only height is about 10–12 px less
  than `height_top_to_ground_px`.
- Shadows: the rider's ground shadow in the sunlit part, and the moving palm-leaf shadows on the pavement left of
  bollard 2, were excluded.
- No motion blur problems; the tyre edges are sharp enough at 30 fps.
