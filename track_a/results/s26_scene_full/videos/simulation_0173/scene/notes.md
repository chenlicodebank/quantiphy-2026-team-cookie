# simulation_0173 – measurement record

2D simulation clip, 24 fps, 40 frames (t = frame/24), 1920x1080. Static camera. Scene: a white regional jet
flies level from right to left across the top of the frame (y ≈ 138), over a rock island with trees, a sand
beach and a turquoise sea. The plane is the only moving object. Its faint shadow also moves across the sea.

## Files
- `scene.json`: inventory, static extents, camera, events, plane size in px.
- `tracks/airplane.csv`: one row per frame (1-39). Columns: `cx, cy` = centre of the full bounding box
  (the reference point); `bbox_*` = full predicted box (can go outside the image when the plane is cut off by
  the frame edge); `visible_x0/x1` = the part inside the frame; `diffmask_*` = extents of the raw
  difference-to-background mask (shows noise from clouds); `length_px` = 459, `height_px` = 95 (rigid
  template); `visible_fraction`; `occluded_or_clipped`; `match_rms`; `cx_linefit`
  (= 2177.55 − 61.5216·frame); `reliability`.
- `tracks/plane_shadow.csv`: rough centroid/box of the dark shadow on the water.
- `scripts/`: diffscan.py (finds the moving regions), template.py (median background + plane mask),
  track_plane.py (masked template matching), check_track.py, static.py, finalize.py.

## Method
Each pixel's median over all 40 frames gives the background, which works because the plane covers any pixel
for only about 8 frames. The plane mask comes from frame 18 (|diff| > 15, closed, holes filled). It runs from
x 841 to 1299 and y 91 to 185, so it is 459 px long (nose to tail-fin tip) and 95 px tall (tail-fin top to the
bottom of the landing-gear wheels). I checked it visually and it covers the whole aircraft. Each frame was
located by masked SSD template matching with sub-pixel parabola refinement. In edge frames only the part of
the template inside the image is compared. I drew boxes on frames 2, 8, 18, 31 and 36 and they fit the plane.

## Results and reliability
- Motion: straight and level, constant velocity. dx ≈ −61.5 px/frame (61.0–62.5 in fully visible frames),
  cy = 138.0 ± 0.3 px. No acceleration was detected (quadratic term 0.0015 px/frame²). Fully visible frames
  8–31 are accurate to ±1 px. Partly visible frames 2–7 and 32–38 are ±3 px. Frames 1 and 39 (nose only /
  tail-fin tip only) use the line-fit position and are low reliability.
- Apparent size is constant (pure side view, parallel to the image plane), so one metres-per-pixel scale
  applies. Size options for a prior: full bbox length 459 px (nose to tail-fin tip) and height 95 px (the
  landing gear is down and included). The fuselage alone is about 415 px (nose to tail cone) and about 33 px
  deep; both are approximate (±5 px). The wingspan is not visible because the plane is seen side-on.
- Origin: Blender's origin for the aircraft is unknown. The bbox centre (1070, 138 at frame 18) is the best
  proxy. The mask centroid sits 4 px lower (142). Only the vertical offset differs, so speeds are unaffected.
- Shadow: a faint dark blob on the sea at y ≈ 970. Frames 16–28 are usable (±5 px), moving ≈ 56–58 px/frame
  to the left. From frame 29 it reaches the island's shadow and the beach and breaks into fragments. The
  frame 39 row is spurious. The shadow is on the sea, not at the plane's depth, so don't use it for the
  plane's scale.
- Static scenery (frame 0): rock island with trees x 627–1222, y 522 (treetops) to 1015, 595 × 493 px. Sand
  beach x 462–1400, y 970–1079. Horizon at y ≈ 895. These are far from the plane's depth, so the plane's
  scale doesn't apply to them unless a question says otherwise.
- Events: nose enters at frame 1 (t 0.042 s); fully in view frames 8–31 (0.333–1.292 s); bbox centre crosses
  x = 960 at frame 19.8 (0.825 s); last visible at frame 39 (1.625 s). There are no starts, stops, bounces or
  turns.
- Camera: static (inter-frame shift < 0.01 px). Clouds and water show no detectable motion.
