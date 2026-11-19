# simulation_0259 — measurement record

2D simulation, 30 fps, 40 frames (t = frame/30, 0–1.3 s), 1920×1080. Pixel y points down.
The camera is static (phase correlation of background patches gives <0.01 px drift; one patch shows a constant 0.5 px offset, which is render noise).

## Scene
There is one moving object: a **paper coffee cup** (white lid, red/pink bands, cream sleeve). It is dropped from rest at the top
of the frame (x≈856) and falls straight down in front of a blue wall onto a table. It hits the table, bounces once and comes to rest.
The static objects are a table, an LG outdoor AC unit (bottom-left), a camera bag, a mug, a potted succulent, a phone, a pen, a small wallet/notebook and a window.
Their pixel boxes are in `scene.json` (±3 px, read off grid crops of frame 0).

## Files
- `scene.json`: inventory, camera, events, static object boxes, and a summary of the cup's size.
- `tracks/cup.csv`: one row per frame (0–39). `cx,cy` = mask bbox centre (proxy for the object origin); `centroid_x/y` = mask
  pixel mean; `top_y` (lid top edge) / `bottom_y`; bbox; `width_px` (max width = lid rim); `top_rim_width_px`; `bottom_width_px`;
  `height_px` (= silhouette height = `length_px`, since the main axis is vertical); `area_px`; and `occluded` (1 only at frame 15).
- `scripts/`: `track_cup.py` (background difference: frame 39 used as background above y=500, frame 0 below; mask rows y>871 are cut
  from frame 15 on to remove the cup's glow/reflection on the glossy table), `rowprof.py` (per-row width profile used to find the
  contact line at y=871), `strip.py` (landing montage), `camera_check.py`.
- Check images (not part of the record) are in `../frames/chk/`. Masks were looked at in frames 0, 5, 10, 14, 15, 16, 18, 20, 30 and 39, and they cover the whole cup.

## Cup measurements and reliability
- **Width is the most reliable size:** 42–43 px in every frame (lid rim), bottom about 28 px. Use the width when a prior gives the cup's diameter/width.
- **Height:** 65–66 px when the cup is near camera height (frames 13–14 and 16–39). In frames 0–12 the silhouette is taller (74 px at
  the top, shrinking to 67 px) because the camera sees the cup's underside ellipse from below. This is perspective, not a size change.
  The same effect moves the bbox centre down by ≤4 px early in the fall. For vertical kinematics, `top_y` is the cleanest
  point (the lid edge is barely affected). Its frame-to-frame drops are 4, 11, 18, 24, 32, 39, 46, 53, 60, 67, 74, 81, 88, 95 px (frames 0→14),
  a steady increase of about 7 px/frame per frame. `bottom_y` increments are about 0.5 px/frame smaller (shrinking ellipse). x stays at 856–857 the whole fall.
- **Events:** release from rest at frame 0. Last free-fall frame is 14 (bottom_y 779). First impact at frame 15 (t=0.5 s). In that frame
  the cup is about 9 px lower than its rest pose, with its bottom partly hidden below the table-top line (sim penetration on impact; flagged
  as occluded). It moves up in frames 16–17, the bounce apex is at frame 18 (top_y 791, 16 px above rest), and it lands again at frame 20 (t=0.667 s).
  After that it rests at top_y 806–807 / bottom_y 871 (centre y≈838.5–839), with a slow ~3 px leftward creep or tilt of the bbox until frame 36. Frames 36–39 are identical.
- **Ambiguities:** on the table the cup has a bright blurred reflection/glow below it (y 872–895). It is excluded from the mask, but a
  naive mask would add about 24 px of height. The cup's origin is assumed to be its centre. The bbox centre at rest is (853–856, 838.5–839).
  The table's back edge is at y≈866, the cup contact line at y=871, and the table's front edge at y≈897.
- There are no metric scales here. A prior on the cup's size, speed or acceleration gives the m/px scale (2D scene, single plane).
  The cup lands near the back of the table, so the table objects are at roughly the same depth (same scale to within a few %).
