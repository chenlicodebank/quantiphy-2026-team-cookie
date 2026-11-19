# simulation_0053 — measurement record

Blender render, labelled **2D**, 30 fps, 91 frames (t = frame/30, 0–3.0 s), 2048×2048 px. Units: pixels (x right,
y down) and seconds. No metric scale was assumed.

## Scene
A static, top-down camera looks at a straight two-lane road running vertically through the image, with sidewalks on both sides.
- **orange_car**: an orange sports coupe in the left lane (x ≈ 684–700). It enters at the top at f8 and drives **down** (+y), front pointing down. It **decelerates smoothly the whole time**. The per-frame displacement of its reference point is 34.1 px at f25, 30.4 at f36, 25.7 at f50, 21.9 at f60, 17.9 at f72 and 11.8 px at f90. It is still moving and still in view at the end.
- **black_car**: a very dark green/black roadster with white bumpers, in the right lane (x = 1301). It enters at the top at f33 and drives down at a **nearly constant 43 px/frame** (43.4 at f50, 43.1 at f60, 42.8 at f75–90). It starts leaving through the bottom edge at f81 and is about 190 px visible at f90. It overtakes the orange car in the adjacent lane: the two reference points have equal y at about f77.2 (t ≈ 2.57 s). There is no contact.
- **person**: a pedestrian on the left sidewalk in the bottom-left corner (x ≈ 310–395) wearing a navy jacket and grey trousers, with the face blurred. They walk slowly toward the top of the image (−y), about 1.3–2.9 px/frame. A foot first shows at the bottom edge around f14 and the jacket from f28. The torso is fully in frame from f59.
- The scene contains no collisions, stops, bounces or reversals.

## Files
- `scene.json`: inventory (moving and static objects with pixel positions and extents), events, and camera information.
- `tracks/orange_car.csv`, `tracks/black_car.csv` (one row per visible frame):
  - `ref_x, ref_y`: the reference point, i.e. the centre of the car's top-view footprint. For a top-down 2D view this is the best image proxy for the vehicle origin. It comes from sub-pixel template matching (`ref_method` = `template_match_*`). The template is the car's bbox crop at f60, where the reference equals the bbox centre.
  - `bbox_ref_x/y`: the plain bbox-centre estimate before refinement. For cut frames this is leading edge − half the median length, or trailing edge + half the median length. Positions such as y < 0 or y > 2047 are extrapolated centres of partly visible cars.
  - `bbox_*`: the visible mask bbox. `length_px` and `width_px` are the long and short sides of the mask's minAreaRect. `area_px` is the mask area.
  - `truncated_by_frame_edge`, `visible_fraction` and `occluded` (always 0: nothing occludes the cars).
  - `tm_score`: the template correlation.
  - `ref_reliable = 0` marks frames where only a sliver is visible: orange f8–14 and black f33–38. Black f89–90 are also flagged because less than 45 % of the car is visible, but their template positions look consistent (42.8 px/frame).
- `tracks/person.csv`:
  - `ref_x, ref_y`: the centroid of the navy jacket mask (upper torso).
  - `bbox_*`: the jacket bbox, including the arms.
  - `truncated_by_frame_edge` = 1 while the jacket touches the bottom edge (until about f58).
  - `tracks/person_raw.csv` holds the raw body/jacket masks for frames 5–90. Its body-mask rows before f28 are mostly noise and shadow-edge pixels.
- `camshift.json`: per-frame background shift (phase correlation on both sidewalks). It is below 0.05 px/frame, so the **camera is static**.
- `static_lines.json`: lane-line x positions, widths and painted runs, plus a column grey profile (frame 0).
- `car_size_summary.json`: median full-visibility bbox sizes.
- `scripts/`:
  - `camshift.py`: camera shift.
  - `track.py`: segmentation by difference against frame 0, which shows the empty road.
  - `refine_template.py`: sub-pixel template refinement.
  - `person.py`: pedestrian mask with shadow rejection and the jacket mask.
  - `finalize.py`: writes person.csv and the reliability flags, and prints displacements.
  - `static_measure.py`: lines and curbs.
  - `events.py`: the overtaking frame.
  - `overlay*.py`, `crops.py`: visual checks.
- Run order: track → refine_template → person → finalize.

## Sizes (px)
- **orange_car**: bbox length along the road is 554–584 px (median 564) and width is 243–248 px. The length includes motion blur along y: it is about 582 px at 33 px/frame and about 555 px at 22–24 px/frame. A blur-free footprint is about **556 × 245 px**.
- **black_car**: median 562 × 241 px (minAreaRect 559–563 × 236–250 px). Its speed is constant, so blur is too: about 559 px long at 43 px/frame.
- **Static features**:
  - Lane lines: x = 665 (left edge line, solid, worn), 1104.5 (centre line, worn and dashed) and 1545 (right line, dashed). Each is 11–12 px wide.
  - Lane widths: 439.5 px and 440.5 px line-to-line.
  - Curbs: left x ≈ 555–590, right x ≈ 1625–1665. The road is about 1042 px curb to curb (588–1630).
  - Sidewalks: left x ≈ 80–555 (grass at x < 80), right x ≈ 1665–2048.
  - Lamp post (left sidewalk, middle): hexagonal head bbox (359,1035)–(442,1109), 83 × 74 px; round pole top at (460–520, 1042–1085).
  - Lower-left lamp post: seen leaning because of perspective, with its white globe at about (475,2025).
  - Asphalt patches: centre-line potholes and right-lane repair patches, with approximate bboxes in scene.json.
  - The painted dashes are worn and irregular, so they are **not** a reliable length cue.

## Perspective / 2D scale
The road plane faces the camera. Car footprint sizes stay constant from the top to the bottom of the image (to within blur), so **one px scale works for anything on the road plane**. Both cars are on the same plane, so a scale from either car's size or speed applies to the other and to the road features.

Tall objects (lamp posts, the person) lean radially away from the image centre. The pedestrian's head therefore projects below their feet in the image. The jacket centroid is a torso point, not exactly the projected pelvis. It is offset by up to a few tens of px toward the bottom-left from the pelvis's ground position, but that offset is nearly constant over 3 s, so **displacements and speeds of the person are reliable while absolute person–car distances are only approximate (±20–30 px)**.

## Reliability
- **Cars, fully visible frames**: frame-to-frame template positions are smooth (the displacement sequence varies by less than 0.5 px). Absolute centre is within ±3 px of the visible footprint centre.
- **Cars, partly visible frames**: positions come from matching the visible part of the template and are good once more than about 45 % of the car is visible. Slivers at entry (orange f8–14, black f33–38) are unreliable and should not be used for speeds.
- **Person**: the jacket mask changes with arm swing, so per-frame displacements jitter by ±1 px (larger at f32–36 while the torso is entering the frame). Use differences over several frames.
- **Shadows**: the cars cast no visible shadows. The person casts a shadow toward the upper part of the image, and it is excluded from the jacket mask.
- **Motion blur**: present on both cars along y. It inflates bbox length but not the template-matched centre.
