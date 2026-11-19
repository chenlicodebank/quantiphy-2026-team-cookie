# simulation_0185 — measurement record (pixels, seconds)

2D simulation (Blender), 1920x1080, 24 fps, 40 frames (t = frame/24, 0–1.625 s). Static camera.
Scene: a warehouse corner. A small **white gift box with a yellow ribbon and bow** starts at rest at
about (497, 386) px, falls straight down, lands on a **dark-blue inclined conveyor/ramp** between
frames 8 and 9, then slides down-right along the ramp, speeding up, until the clip ends. The box is the only moving object.

## Files
- `scene.json`: inventory (moving and static objects with pixel boxes), sizes, events, camera, artefacts.
- `tracks/gift_box.csv`: the main track, one row per frame (0–39):
  - `ref_x, ref_y`: centroid of the box-body mask with the bow excluded. Use this as the object origin.
  - `ref_x_dupfix, ref_y_dupfix`: the same values, except at frame 38 (see below).
  - `bbox_*`: full mask including the bow.
  - `body_len_main_axis`, `body_width_across`: min-area rectangle of the body.
  - `body_tilt_deg`, `height_incl_bow_px`, `area_px`, `phase`, `occluded`, `duplicate_frame`.
- `tracks/gift_box_v2.csv`: full output of the refined segmentation. It also has `body_rect_cx/cy`, the
  centre of the min-area rectangle, a second reference-point estimate that agrees with the centroid to within 1–2 px.
- `tracks/gift_box_raw.csv`: first-pass colour-based mask (white+yellow). Kept only for cross-checking.
- `scripts/`: `track_box.py` (background median and colour mask), `track_box2.py` (background-difference mask, body without bow, overlays),
  `check_camera_dup.py` (camera shift and duplicate-frame test), `finalize.py` (builds gift_box.csv).

## Method
- Background = median of every 4th frame. The mask is |frame − bg| > 28 inside a window around the box, cleaned with
  morphology and hole-filled. The body is that mask minus the yellow bow blob at the top.
- I checked overlays at frames 0, 4, …, 36–39. The mask covers the box and bow well.

## Key numbers (pixels)
- Box size, measured on the unoccluded falling frames 0–8: body edges ≈ 111 × 109 px (≈110 px cube face,
  ±3 px), height including the bow ≈ 130 px along the box's own up axis, image bbox including the bow ≈ 137 × 145 px.
  The box stays tilted ~29° (bottom face parallel to the ramp) and does not rotate.
- Fall (frames 0–8): x stays at 496 ± 0.5. ref_y = 385.7, 387.8, 394.0, 404.1, 418.2, 436.3, 458.8, 485.2, 513.9.
  The steps grow almost linearly (about 4 px/frame² apparent), which is free fall from rest starting at frame 0.
- Impact on the ramp falls between frames 8 and 9 (t ≈ 0.34–0.37 s). From frame 9 the box slides along a direction
  ≈ 28.6° below horizontal (ramp slope in the image) and accelerates. The per-frame step grows from ≈12.9 px
  (9→10) to ≈47 px (36→37). There is no bounce.
- Ramp slope in the image is 28.6°, taken from the box path over frames 10–37.

## Reliability and caveats
- **Frame 38 is a duplicate of frame 37** (the encoded video repeats it; mean abs diff 0.013). Frame 39 contains two
  steps of motion. For backward-difference speeds at t ≈ 1.583 s or 1.625 s, use the `_dupfix` midpoint for frame 38,
  or the 37→39 difference divided by 2.
- Occlusion: from frame 9 on, the near rail of the ramp hides the lower edge of the box. The body width across the
  ramp drops from ~109 to ~89–96 px, so the centroid during the slide may sit a few px (≲8 px) up-slope/high
  of the true centre. The bias is roughly constant, so differences between frames are hardly affected.
  At frame 39 the grey lower-right face blends into the floor, so the mask is slightly short there.
- The apparent size changes during the slide (body length 111 → 101 → 119 px). This comes from occlusion plus perspective
  side-face visibility near the image edges. It is not a clear depth change; the motion is treated as planar (2D scene).
  Use the frames 0–8 sizes for the scale.
- Reference-point accuracy is ±1 px while falling and ±2–3 px while sliding. Sizes are ±3 px. There is little motion blur.
- Static objects (approximate pixel boxes, frame 0): warning sign "TAKE CARE WHEN STACKING CRATES" 187×188 px at
  (1295–1482, 575–763); wall vent 185×88 px at (1670–1855, 857–945); large cardboard box "PIZZA TOPPING" (cut by the
  frame) 0–290 × 0–530; small "SEEDLESS JAFFAS" box 285–405 × 325–535; blue shelf top y≈535–600, x 0–335; orange
  hand-truck frame bottom-left 0–222 × 620–1080; wooden floor below y≈950 on the right; grey block wall
  (block courses ~95–100 px). These boxes come from gridded zoom views and are good to ±5 px.
- No metric scale is assumed. A question's prior (for example the box size, a speed or g) sets the single m/px scale.
