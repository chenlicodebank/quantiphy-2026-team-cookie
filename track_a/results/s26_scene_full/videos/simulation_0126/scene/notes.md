# simulation_0126 – measurement record

2D Blender render, 1080x1790 px, 24 fps, 72 frames (t = frame/24). It shows an air-hockey table from straight above. The camera is static (the background differs by <0.05 grey levels between the first and last frames, and the shift is 0.000 px).

## Files
- `scene.json`: inventory (objects, pixel sizes and positions of the static features), events, per-frame step summary.
- `tracks/puck.csv`, `tracks/mallet_top.csv`, `tracks/mallet_bottom.csv`: every frame 0-71. Columns: frame, time_s, ref_x, ref_y (centroid of the filled colour mask = the disk centre ≈ the object origin), bbox, mask_area_px, length_px / width_px (minAreaRect of the mask), height_px (vertical image extent), enclosing_circle_diam_px, occluded (always 0).
- `static_measure.json`: raw output of `scripts/static.py` (lines, circles, goals, dots, camera check).
- `scripts/`: `track.py` (HSV segmentation: orange puck h 9-22; red mallets h ≤7, s>110), `overlay.py` (draws the checks into frames/), `static.py`, `probe.py`.

## Objects
- **puck**: orange disk, 63-64 px diameter (stable in every frame, no visible blur). x stays at 537.8. It moves straight down the image at a constant 24.41 px/frame (frames 2-40), bounces on the bottom rail in front of the bottom goal between frames 40 and 41 (estimated at frame ≈40.55, t ≈ 1.690 s, centre y ≈ 1686), then moves straight up at a constant 9.34 px/frame (frames 42-71). Speed ratio after/before is ≈0.38. Frames 0-1 are still.
- **mallet_top**: red striker in the upper half. Diameter 113-115 px. It sits at (531.5, 534.5) in frames 0-1, moves down with steps of 53.1, 58.3, 53.2, 39.2 and 15.1 px (frames 2-6), and then stays still at (531.6, 753.3) until the end. It reaches the puck at frames 5-6 (centre gap 80.5 px and then 89.2 px, against a radius sum of ≈88.5). The puck already moved at constant speed before this contact and its speed does not change, so this "hit" does not set the puck's speed.
- **mallet_bottom**: red mallet that never moves, at (713.3, 1434.3) over the lower-right face-off circle. Its mask is 106-110 px, which is probably a few px small because of the lighter rim. It is probably the same size as mallet_top.
- **Static table features** (px): the playing surface spans x 102-979 (878 wide) and y ≈113-1701 (≈1588 long, top edge ±2). Blue lines are at y 630 and 1183 (11 px thick, 553 apart). The red dashed centre line is at y ≈906.5. The centre circle has an outer diameter of ≈267 and is centred near (531.5, 912.5). The four red face-off circles have an outer diameter of 282 and are centred at (313/749, 298/1515). There are four red dots, 18 px across, at (314/749, 684/1129). Each light-blue goal semicircle is 124 px wide, centred at x 531.5, at the top (y 115-153) and bottom (y 1660-1700). There is also a partial blue circle at the left edge and a scoreboard on the right rail.

## Reliability and ambiguities
- Puck and mallet centres are accurate to about ±0.3 px, and the overlays (frames/ov.png) were checked by eye. The mallet's reference point is the centre of the disk outline seen from above; the handle knob looks slightly off-centre because of shading, and I ignored it.
- Two red mallets look alike: top = the one that moves, bottom = the one that never moves.
- The scale has to come from the given prior. Likely candidates are the puck diameter (63.5 px), the mallet diameter (113.5 px), the puck's speed (24.41 px/frame before the bounce, 9.34 after) or the mallet's motion. The mallet's motion is not uniform, so a prior on it needs the per-frame steps.
- Bounce timing: the puck's lowest recorded frame is 40, and the frame 40→41 backward difference (9.19 px) spans the impact.
