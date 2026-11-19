# simulation_0043 — measurement record

Blender render, 3D scene, 24 fps, 72 frames (t = 0 … 2.958 s), 1080×1080 px. Pixel coords: x right, y down.
Nothing here is in metres: every value is in pixels and frames/seconds.

## Scene
High aerial view looking steeply down (slightly oblique: you can see the boat's side and the islet's slopes) over a
coast. A large white/grey **rock islet** sits on a beige **sand spit** in the upper half. Dark green **water** fills
the lower and right parts. A small **fishing boat** (white hull, red stripe, red-roofed wheelhouse, mast, teal hatch)
is the only moving object. It sails left (slightly up), bow first, in the water below the sand tip. Its dark
**shadow** is up and to the right of it. There are no other vehicles, people or animals.

## Files
- `scene.json`: inventory, static extents, boat summary, events, camera.
- `tracks/boat.csv`: one row for each frame 0–71. The columns are:
  - `cx,cy`: the reference point, which is the centroid of the boat-body mask (convex hull of the hull and
    wheelhouse with the mast removed). Use it as the proxy for the object origin.
  - `bbox_*`: the body box. `full_x0..full_y1`: the box including the mast.
  - `length_px`: bow-to-stern extent along the mask's main axis. `width_px`: the extent across that axis.
  - `axis_angle_deg`, `area_px`.
  - `bow_x,bow_y,stern_x,stern_y`: the main-axis end points.
  - `occluded`: 0 in every frame.
- `tracks/camera_shift.csv`: per-frame phase-correlation shift of the top 700 rows against frame 0.
- `scripts/track_boat.py`: segmentation and tracking (white, red and teal colour mask, then the largest component
  near the previous box, then opening to drop the mast, then convex hull). It also writes the overlays
  `frames/ov_*.png`.
- `scripts/summarize.py`: step and size checks. `scripts/framediff.py`: frame-difference checks.
  `scripts/static_rock.py`: the islet outline.

## Findings
- **Camera is static.** The shift is ≤0.002 px in every frame. The water texture is static too.
- **Boat motion:**
  - Frames 0 and 1 are pixel-identical (the boat-region diff is 0.06 grey levels, against ~12 between later
    frames). The boat moves from frame 2 on.
  - This could be a real start from rest or just a duplicated first render frame, so it is ambiguous.
  - From frame 2 it moves in a straight line at a nearly constant image speed of ~3.70 px/frame. Per-frame
    steps range from 2.9 to 4.3 px; that spread is segmentation jitter.
  - A quadratic fit gives x″ ≈ 0.0007 px/frame² and y″ ≈ 0.0006 px/frame², which is negligible.
  - The centroid goes from (440.1, 948.6) to (192.3, 876.3). The net displacement is 258.1 px and the path is
    259.2 px. The image direction is −163.7°, about 16° above due left, along the boat's own axis (heading forwards).
  - There is no bounce, turn, contact or stop.
- **Apparent size:**
  - Body length (bow to stern, mast excluded) is 216.9 px at frame 0 and 213.4 px at frame 71, a steady
    −0.055 px/frame (−1.6%). So the boat's camera distance grows by about 1.6% over the clip.
  - Width across the hull is ~87 px, constant within ±2 px.
  - The body box is about 200×108 px. With the mast the box is 209×142 px at frame 0.
  - Seen from above, the length is the hull length plus a little foreshortening. The visible "width" includes some
    of the hull side, because the view is oblique.
- **Rock islet (static):**
  - Centroid (626, 204), bbox x 398–885, y 12–450.
  - Main-axis length ≈ 538 px (axis 144.5°, running upper-right to lower-left); width across ≈ 390 px.
  - The outline was hand-clicked, ±10–15 px.
- **Sand spit:** the lowest tip is at about (370, 775). It is about 120 px above the boat's mast at the end.

## Reliability and ambiguity
- **Centroid:** ±1 px per frame. It is the centroid of the visible body, which can sit a few px from the true
  object origin, so use differences, or fits over many frames, for motion.
- **Bow tip:** it is very thin, so length can be ~2–5 px short.
- **Shadow:** excluded from the mask, which was checked on the overlays at frames 0, 24, 48 and 71.
- **Mast:** excluded from the body metrics, but included in the `full_*` box.
- **Perspective:** there is no horizon or vanishing point.
- **Focal length:** unknown. It needs depth_info plus a known size to estimate.
