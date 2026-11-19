# simulation_0062 – measurement record

Blender render, 3D scene, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s), 2160×1080. All values are in **original-image pixels** (x to the right, y down) and seconds. There is no metric scale here: answering sessions take it from their own prior and depth_info.

## Scene
A city intersection seen from a **static, level camera** looking straight down a street. The street's vanishing point is at about (1078, 539), i.e. the image centre, and the horizon is at y ≈ 540. The camera never moves: background phase correlation between frames 0, 35 and 71 shifts by less than 0.01 px. Four objects move:

| name | what tells it apart | motion | visible |
|---|---|---|---|
| pedestrian | man in a white T-shirt and blue jeans with a white mannequin face, on the near-left sidewalk | walks toward the camera and to the left the whole clip | 0–71 |
| taxi | yellow NYC-style sedan with a roof "TAXI" sign | drives right (side view) at the start, turns left toward the camera, then comes head-on (front view from ~f44); still approaching at f71 | 0–71 |
| van | white cargo van with brown rear-side windows | starts from rest at f1 and speeds up steadily, driving left→right on the cross street, behind the taxi and the cyclist | 0–71 (partly hidden f0–56) |
| cyclist | rider in dark clothes on a bike with white rims | rides left→right on the cross street at a steady speed, nearer to the camera than the van | 0–71 (hidden behind the taxi f0–~22) |

Static objects (`scene.json → static_objects`): double-lantern lamp post (near left), green litter bin, four traffic lights (near-left, far-left, far-right, near-right with a red triangular crossing sign), rows of small street lamps along the receding street, sidewalks with red brick planters. The bounding boxes are measured on the clean background. Where the box only covers the signal head, the top including the sign and the pole base y were read by eye (±5 px).

**Important: frames 0 and 1 are identical.** The first frame is a duplicate, so every object is stationary between f0 and f1. Motion begins at f1→f2.

## Files
- `scene.json`: metadata, camera and perspective cues, object inventory (descriptions, reference-point definitions, apparent-size summary), static objects, and events with frame numbers.
- `tracks/<object>.csv`: one row for each of the 72 frames. Common columns are `frame, t, ref_x, ref_y, ground_y, bbox_x0, bbox_y0, bbox_x1, bbox_y1`, plus size columns and occlusion flags.
  - `van.csv`: `ref` = centre of the full van box. `length_px` = 453 is rear bumper to front bumper; `height_px` = 162.5 is roof (y 452.5) to tyre bottom (y 615). Also `n_subtemplates`, `match_score` and `occluded`.
  - `cyclist.csv`: `ref` = centre of the rider+bike box. `pelvis_x/y` = saddle/pelvis estimate (box x0+43, y0+65). Bike length 134 px (rear rim to front rim), height 138 px (head top to tyre bottom). Also `match_score` and `occluded`.
  - `taxi.csv`: `ref` = centre of the cleaned box. `ground_y` = tyre bottoms. The `raw_*` columns are what the mask gave before cleaning. `mask_cx/cy` = centroid of the visible mask. `axis_length/width/angle` come from a principal-axis fit to the mask. `sign_top_y` = top of the roof sign when detected. `occlusion_flags` gives the reason for each corrected frame.
  - `pedestrian.csv`: `ref` = pelvis estimate (x = mask mean in a ±10-row band at 47% of the box height from the top; y = that row). `height_px` = head top to the lowest foot. `bbox_w` includes arm swing. `legs_cx` = centre of the legs. Also `occlusion_flags`.
- `scripts/`: every script used. The order is `bg.py`/`bg2.py` (clean background), `van_tm2.py`, `cyc_tm.py`, `composite.py`, `seg_taxi_ped.py`, `post.py`, `static.py`, `vanish.py`, `events_scene.py`, and `check_overlay.py` (visual check). Scratch images go to `../frames/`, which is not part of the record.

## How each object was measured, and how reliable it is
- **Background**: frame 0 everywhere except x 200–778, where frame 71 was used (the moving objects are elsewhere in each frame). It is clean except for compression noise. The white van against the white sky differs by only about 7 grey levels, so a low threshold was used in sky areas.
- **Van**: the van is rigid. A multi-scale template search over all frames gave scale 0.99–1.01 and a top-edge y that stayed fixed at 444–446, so the van translates horizontally at constant image size. That means it moves at constant depth, parallel to the image plane. It was tracked with 1-D NCC of several sub-templates taken from frame 57 (full, rear, roof, rear-roof, front, rear-end). The result is the median of the agreeing sub-templates, with sub-pixel refinement. The full box comes from fixed offsets: rear bumper and roof measured at f58, front bumper at f54. **Reliability: about ±1 px per frame from f22 on. f0–21 is about ±1–2 px** because the pedestrian, the taxi and the poles occlude it; in those frames only the rear end and the roof are visible. Per-frame steps rise smoothly: 0 (f0→1), 1.4, 1.8, 2.4, … about 38 px/frame at the end (steady acceleration). Small jitter appears at f20–22.
- **Cyclist**: tracked with NCC of a frame-40 template (full, upper body, bike), again at constant scale and constant y (box top at 482 ±0.5). The box geometry was measured on a zoomed view of f40. **Reliability: ±1 px from about f8 on.** In f0–7 most of the cyclist is behind the taxi, so the match score is only 0.56–0.7, but the positions still follow the steady 17.8 px/frame line. The pedalling legs change shape; the box and reference come from the rigid template, not from the leg pixels.
- **Taxi**: segmented as the residual against a composite made of the background plus the van sprite plus the cyclist sprite, each placed at its tracked position. Static occluders (lamp post, bin, near-left traffic pole) are kept in front. Pieces split by the pole were merged, and the box top comes from the roof sign when that is higher. The taxi **turns**, so its 2-D box changes shape and the box centre is only a proxy for the vehicle root. In the side view the box width ≈ car length (about 470–480 px at f8–f19). In the front view the box width ≈ car width plus mirrors (about 250–260 px at f48–56, 311 px at f71). Corrections, each marked in `occlusion_flags`:
  - Rear edge hidden behind the bin and lamp post at f0–5: extrapolated. The true rear is hidden, so treat these values as uncertain by ±20 px.
  - Rear edge hidden behind the traffic pole at f20–23, plus a one-frame glitch at f36: interpolated.
  - Right edge inflated by the cyclist at f24–26 and by a van-wheel ghost at f44: interpolated.
  - Roof sign partly lost at f41–42: top interpolated.
  - At f12–26 the cyclist overlaps the taxi front, so the right edge may still be up to about 10–15 px too wide there.

  **Reliability: edges ±3–5 px otherwise.**
- **Pedestrian**: legs were found as a residual cluster below the vehicles. The mask is the residual inside a window around the legs. **f0–14**: the pedestrian is in front of the van rear and near the taxi rear. The white shirt has almost no contrast against the white van, so the width comes only from head and leg rows (arms may be clipped). The height (head top to feet) is still reliable, ±2 px. f13 (head lost) and the widths at f0–3, f13, f14 and f17 were interpolated. **From f15 on: ±2 px.** The pelvis is a body-proportion estimate, not a joint detection. Its y stays at about 545, close to the horizon, so the camera height is roughly the pedestrian's pelvis height. Apparent height grows from 242 px to 306 px as he walks closer, with gait oscillation in the width (60–103 px).

## Perspective / 3D notes
- Level camera with the principal point near the image centre (1080, 540); the horizon is at y ≈ 540.
- Image ground-contact rows show the depth order: van 615 (constant) < cyclist 626 (constant) < taxi 633→712 (approaching) < pedestrian 672→707 (approaching). Larger ground_y means nearer.
- Van and cyclist keep constant image size, so their depth is constant: they move parallel to the image plane. Taxi and pedestrian grow over the clip. Their per-frame sizes (taxi bbox h; pedestrian height) are in the tracks.

## Ambiguities
- Taxi "root": unknown point on the car; only the box centre, the mask centroid and the tyre line are given.
- Cyclist reference: a question may mean the rider's pelvis (`pelvis_x/y`) or the bike/rig origin (box centre). The two differ by a fixed offset, so speeds are the same.
- Shadows: the cars' soft contact shadows are outside the boxes (tyre bottoms were used). Motion blur is negligible.
- Similar objects: the four traffic lights and the many identical small street lamps — use the position descriptions in `scene.json`.
