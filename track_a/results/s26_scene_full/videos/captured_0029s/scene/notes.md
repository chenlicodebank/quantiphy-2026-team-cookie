# captured_0029s: measurement record

**Video:** lab recording (Orbbec Femto Mega, 24 fps, 49 frames, 0 to 2.000 s, 1280x720). The background was replaced with SAM2 ("Modified with Segment Anything 2 Demo" watermark at bottom right), so only the table, its leg and the ball are kept. The masks leave white halos around the ball in frames 18 to 48. Use focal length f = 763 px and principal point (640, 360), per the benchmark convention. The camera is **static**: the table mask moves less than 1 px against frame 0 in every frame (`scripts/table.py`).

## Scene
- **ball**: a yellow-green tennis ball and the only moving object.
  - Frames 0 to 16: the ball sits close to the camera, right of and in front of the table's front-right corner, centred near (1170, 563). It is probably held in a hand that the segmentation erased (there is an odd lobe under it).
  - From about frame 17 it moves up-left, crosses the front-right corner onto the table top (frames 18 to 22, heavy motion blur), then rolls diagonally toward the back of the table.
  - It shrinks to its smallest apparent size at frames 29 to 31 (diameter about 43 to 46 px; the y position is smallest at frame 30), near the back edge.
  - From there it moves left and slightly down the image while getting **larger**, so it is coming back toward the camera. This is a direction change, possibly a rebound off something erased with the background. At frame 48 it is still rolling, at (515, 454) with diameter about 54 px.
- **table**: brown wood top on one pedestal leg; static. Corners at frame 48, in px: back-left (447,453), back-right (915,469), front-left top (208,541), front-right top (1141,590). Front-edge bottom corners: (211,571) and (1138,624).
  - Image lengths: front edge 933, back edge 468, left side 255, right side 256.
  - Edge (slab) thickness: 30 px at the left, 34 px at the right.
  - The front-right corner is hidden behind the ball until about frame 19.
- **table_leg**: dark column, x 629 to 688, from y 615 to the image bottom; black bracket at x 605 to 701, y 592 to 615.

## Files
- `scene.json`: inventory, camera, static extents and events with frames and times.
- `tracks/ball.csv`: one row for each of frames 0 to 48. The ball is never occluded (`occluded` = 0), but it is motion-blurred in frames 17 to 22. Columns:
  - `cx, cy`: centroid of the colour mask, which is the reference point (visible centre).
  - `bbox_*`: bounding box.
  - `mask_len_major` / `mask_wid_minor`: extents along the mask's principal axes.
  - `diam_radial_px` / `diam_tangential_px`: extents along and across the line from the principal point.
  - `mask_area_px`, `equiv_diam_px`: mask area and the diameter of a circle with that area.
  - `encl_circle_*`: minimum enclosing circle.
- `scripts/`: `track_ball.py` (HSV mask, H 22 to 50, S ≥ 40, V ≥ 30, largest blob, filled contour), `table.py`, `dump_frames.py`, `strip.py`. I checked the overlays by eye: the mask covers the whole ball in every frame.

## Reliability and caveats
- **Ball size and depth:** the ball is about 35° off-axis while near the camera, so perspective stretches its image radially (radial about 115 px vs tangential about 95 px; the ratio matches 1/cos 35°). Use **`diam_tangential_px`** as the apparent diameter. A depth estimate for a sphere is Z ≈ f·D/d_tan, or more exactly the distance to the centre is D / (2·sin(α/2)), where α is the angular diameter.
  - Frames 0 to 16: there is a ±3 px uncertainty from the erased hand or fingers below the ball.
  - Frames 17 to 22: the size is inflated along the motion direction by blur. Prefer `diam_tangential_px` or `mask_wid_minor` there.
  - Frames 23 to 48: the size is about ±2 px.
- **Ball centre:** ±1 px in sharp frames and ±3 to 5 px in frames 17 to 22. The halo is excluded by the colour threshold.
- **Dropped frame:** the image step from frame 35 to 36 (20.5 px) is about twice its neighbours (about 10.5 px), and the size is continuous, so a capture frame was probably dropped there. The file's timestamps are uniform, so the time rule is still frame/24.
- **Motion onset:** the ball slowly creeps left from frame 13 (steps of 2, 4, 6 and 9 px), then makes a 44 px jump from frame 17 to 18. Frame 17 (0.708 s) is the start of motion; frames 13 to 17 are the onset window.
- **Direction change and farthest point:** frame 30 (1.25 s), range 29 to 31. Smallest size: about 43 px at frames 29 to 31.
- Speeds, accelerations and metric scale are not computed. Each question's depth_info or size prior sets the scale.
