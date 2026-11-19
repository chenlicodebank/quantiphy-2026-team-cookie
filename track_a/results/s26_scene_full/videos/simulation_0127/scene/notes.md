# simulation_0127 — measurement record

The video is a 2D Blender render, 1920x1080, 24 fps, 57 frames (t = frame/24, so 0 to 2.333 s). The camera looks
straight down on a horizontal street and **does not move**: the background shift is under 0.002 px across the clip.
Everything here is in pixels and seconds. Image x points right and y points down. No metric scale is assumed.

## Files
- `scene.json`: the inventory (moving and static objects with pixel sizes and positions), the events, the
  camera, and the per-frame x-steps of each moving object.
- `tracks/blue_car.csv`, `tracks/cyclist.csv`: one row per frame. Columns: `ref_x, ref_y` (reference point),
  `bbox_*` (full object box, which may extend past the image edge), `visible_x0/x1` (the part inside the image),
  `length_px` (along x, the motion axis), `width_px` (along y), `height_px` (empty because the view is top-down,
  so height cannot be seen), `visible`, `occluded` (1 = partly hidden by canopy or the image edge), `source`
  (how the x-offset was obtained) and `note`.
- `scripts/`: every script used. Order: `bgfull.py` (median background, written to the scratch file
  `../frames/bg_full.png`), then `track_car_chain.py`, `track_cyclist.py`, `build_tracks.py`, `write_scene.py`.
  The others are diagnostics or earlier attempts: `track.py` and `track_car.py` (global template matching,
  outputs `raw_*.csv`), `profile.py`, `diag.py`, `viewcrop.py`, `overlay.py` (draws the tracks for checking),
  `static_view.py`, `framediff.py`, `bg.py`, `sizes.py`.

## Moving objects (only these two; nothing else moves, and the trees are still)
1. **blue_car**: a blue sedan in the upper lane, driving **right (+x)**. Its box top is at y=277, just below
   the upper curb.
   - Size (read at frame 12, ±2 px): **length 236 px** (rear x=1254 to front x=1490), **width 80 px**
     (y 277–357). The reference point is the box centre: (1372, 317) at frame 12, with y constant.
   - Visible in frames 0–38. Frames 0–10: the rear half is under the tree canopy, but the front edge is clear
     (front x=1214 at frame 0). The front crosses the right image edge between frames 28 and 29. The last
     sliver shows at frame 38, and the car is gone from frame 39.
   - Steps: about **+25.3 px/frame** (mean of frames 2–38: 25.27), uniform. Frame-to-frame scatter is ±0.4 px
     (up to ±0.7 px under the canopy).
2. **cyclist**: a person on a bicycle in the middle of the road (y≈596), riding **left (−x)**. Dark clothing
   and a helmet; a long shadow falls to the lower right.
   - Reference point: the **rider's pelvis/saddle** (rear end of the dark torso), (631, 597) at frame 36.
   - Other points at frame 36: bike front tip (574, 596), rear tip (659, 596), helmet (609, 594),
     handlebar x≈600.
   - Bike length front tip to rear tip: **85 px** (85–87 px over the clip, ±3). Width across the
     handlebar/shoulders: **26 px** (y 583–609).
   - Visible in frames 0–56. The front tip reaches the left edge at frame 54. The pelvis is at x≈29 at
     frame 55 and x≈−3 at frame 56, when only the rear ~25 px of the bike are visible.
   - Steps: about **−31.6 px/frame** (mean of frames 2–53: 31.64). Scatter is ±0.3 px; frames 2–13, in the tree
     shadow, scatter up to ±0.6 px.

## How the tracks were measured
- **Rigid translation along x.** Neither object rotates or moves in y (y drift < 1 px), so each track is one box
  read visually at an anchor frame (car at 12, cyclist at 36) plus a per-frame x-shift.
- **How the x-shift was found.** Chained frame-to-frame NCC template matching on grayscale with sub-pixel peaks:
  - Car: the whole body, or the hood alone in frames 0–7 (outside the canopy).
  - Cyclist: bike + rider, rows 580–612, which is above most of the shadow.
- **Cross-check for the car.** Independent global matching on a chromaticity image (`track_car.py`) agrees
  within 1–3 px.
- **Car, frames 35–38 (`source=rear_edge`).** The car's front is out of the image, so the shift comes from the
  measured rear edge (background difference) plus a 5.5 px bias calibrated on frames 30–34. Accuracy is ±1 px.
- **Cyclist, frames 54–56 (`source=extrapolated`).** Matching fails at the left edge, so these frames are
  extrapolated linearly with the mean step.
- **Check.** I drew the tracks and boxes on frames 0, 2, 12, 30, 34, 36, 38 (car) and 0, 10, 20, 36, 47, 53,
  55, 56 (cyclist) and looked at them (`overlay.py`). They sit on the right objects and cover their full extent.

## Events
- **Frames 0 and 1 are identical renders** (no motion at all). Both objects move from frame 1→2 onward at their
  full, constant step, with no visible acceleration phase. The frame-2 step is slightly low (car 24.2, cyclist
  31.0 px), which is probably match noise.
  - Note on the convention: backward-difference speed at frame 1 is 0 and at frame 2 is the full value.
- They pass each other (car centre x equals cyclist pelvis x) between frames 12 and 13. They are in different
  lanes and never touch.
- Car front leaves the image at frame ≈28.6; the car is fully gone after frame 38.
- Cyclist front tip reaches the left edge at frame 54; the pelvis leaves at frame ≈56.
- No bounces, impacts, stops or direction changes.

## Static objects (pixel boxes [x0, y0, x1, y1], read on frames 0 and 40, ±3 px)
- **red_car**: parked at the lower curb on the left, nose to the left. Box [13, 713, 257, 807]; length 244,
  body width 86 (95 with mirrors); centre (135, 760).
- **dark_sports_car**: dark grey coupe parked at the lower curb on the right. Box [1687, 718, 1913, 815];
  length 226, body width 90 (97 with mirrors); centre (1800, 767).
- **white_van**: roof only, bottom of the frame, in a driveway, cut off by the image edge.
  Box [638, 920, 745, 1080+]; width 107.
- **orange_object**: orange elongated prop lying diagonally on the lower sidewalk, box [1295, 847, 1370, 917],
  with a thin red post at x≈1370.
- **Road**:
  - Upper curb y≈272, lower curb y≈820, so the road is about 548 px wide.
  - Faint lane lines at y≈478 and y≈655 (±5).
  - Lanes: blue car in the upper lane (275–478), cyclist in the middle (478–655), parked cars in the lower lane.
- **Sidewalks**: upper at y 135–262, lower at y 830–950.
- **Trees**: canopies above the upper sidewalk (x≈330–1560, down to y≈360 around x 900–1100) and at the bottom
  corners.

## Reliability and ambiguities
- **Steps and positions.** Car and cyclist steps are good to about ±0.5 px/frame per frame and about ±0.1 px/frame
  on average. Absolute reference positions are ±2 px (car) and ±3 px (cyclist pelvis, which was judged from the
  top view).
- **Perspective.** The camera is perspective, not orthographic. Seen from above, the cyclist's body (rider height)
  is pushed outward from the image centre by a few px relative to the bike's ground-level parts. The bike line
  shifts up to ~8 px relative to the rider-anchored box between x≈1720 (frame 0) and x≈100 (frame 53).
  - The pixel scale at rider height and at ground level therefore differs by less than 1%.
  - The cyclist box follows the rider, so the bike tips can stick out of it by up to ~8 px near the image edges.
- **Shadows.** Both objects cast long shadows toward the lower right, and they cross tree shadows. I excluded
  the shadows from all extents: the car box is the body only, and the cyclist rows are 583–609.
- **Occlusion.** The tree canopy hides the car's rear in frames 0–10, but its position comes from the clear hood
  and front edge.
- **Motion blur.** Negligible.
- **Prior scales.** Car length 236 px and cyclist bike length 85 px are the most likely size priors. For a 2D
  question, one metres-per-pixel scale from the prior object applies to everything in the ground plane.
