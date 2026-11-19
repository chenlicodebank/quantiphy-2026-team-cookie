# simulation_0234 – measurement record (pixels, seconds)

2D simulation (Blender render), 1920x1080, 24 fps, 50 frames (t = frame/24, frame 0 = t 0, last frame 49 = 2.042 s).
Scene: a gym wall seen from the front, with a white basketball backboard, an orange rim and a net at the top centre. There is a
light-grey upper wall, a teal lower wall band and an orange wooden floor at the bottom. A single crimson basketball
is dropped from rest, falls straight down, bounces once on the floor and rises back to almost its starting height.
**Camera is static** (background shift < 0.03 px in every frame).

## Files
- `scene.json`: inventory (ball plus the static objects with pixel bboxes and extents), camera, events.
- `tracks/ball.csv`: one row per frame (0-49). Columns: `cx, cy` = least-squares circle fit to the silhouette contour
  (**reference point = ball origin/centre**); `centroid_x/y` = mask centroid (agrees within ~0.3 px); bbox (`bbox_x0..y1`,
  `bbox_w/h`); `circle_diam` (circle-fit diameter), `encl_diam` (min enclosing circle), `equiv_diam` (from mask area),
  `len_major/width_minor` (mask extents along/across the principal axis; for a sphere these are only noisy diameters);
  `area_px`; `bg_dx/bg_dy` = background shift vs frame 0; `occluded` (always 0).
- `scripts/track_ball.py` (tracking), `track_ball_lib.py` (mask function), `overlay.py` (check images),
  `events_static.py` (bounce timing and static extents), `probe.py` (colour probing).

## Method
Ball mask: HSV hue >= 150 or <= 4, saturation > 80, then a 9x9 closing, the largest component and hole filling. The orange floor
(hue ~12) and the grey shadow are excluded. I drew the overlays (contours, bbox, fitted circle) for frames 0, 12, 22-25, 36 and 49 and checked them by eye. The
fit follows the ball edge closely in every one of them, including the bounce frames over the floor.

## Ball (only moving object)
- Diameter: circle fit 74.75 px mean (range 74.2-76.0); bbox about 74.7 (w) x 76.0 (h); area-equivalent 75.7.
  **Best ball diameter ≈ 75 px (±1).** The ball keeps the same apparent size in every frame (2D, constant depth).
- x is constant at 986.66 ± 0.2 px, so the ball does not move horizontally. Motion is purely vertical.
- y (down positive): 738.84 at frame 0 → lowest 1004.24 at frame 24 → 738.96 at frame 49.
  The drop is 265.4 px and the rebound 265.3 px. The bottom of the ball at its lowest point is at y ≈ 1042, on the floor below the baseline.
- Per-frame centre noise is about 0.15 px (residual of a smooth fit).

## Events
- Frame 0 (t = 0): release from rest. The descent parabola has its apex at frame 0.01.
- Frame 24 (t = 1.000 s): bounce, floor impact, lowest point and the change from falling to rising. The two parabola branches
  intersect at frame 23.995, so contact falls essentially on frame 24. There is no visible squash.
- Frame 49 (t = 2.042 s): apex after the bounce (the ascent fit puts the apex at frame 49.00, y = 738.7). This is the last frame.
- Caution for answering sessions: the fitted curvature of the descent (frames 0-22) is about 8 % larger than that of the ascent
  (frames 26-49). If a question gives an acceleration prior, check which part of the motion it refers to. Frames 23-25 are
  the impact frames, where the one-frame differences change sign.

## Static objects (frame 0, pixels)
- Backboard (white): x 794.5-1152.5, y 71.5-280.5, which is **358 x 209 px**, centre (973.5, 176).
- Orange square on the backboard: x 916-1031, y 158-231 (116 x 74 px).
- Rim (orange ring, seen nearly edge-on): x 916-1031, y ~236-259. **Width 116 px**, centre about (973.5, 246).
- Net: x 933-1018, y 242-297 (86 x 56 px). Black support bracket: x 809-1137, y 280-317.
- Upper wall / teal band boundary: y ≈ 679. Teal band / floor junction: y ≈ 981. White baseline: y ≈ 989-991.
  The white court lines on the floor slant towards the bottom edge (near x 100, 590, 1390 and 1850).
- The orange blurry patches (lower right floor near x ~1480 and the upper right wall) are light reflections, not objects.

## Reliability / ambiguities
- Ball centre and diameter: high reliability (±0.3 px centre, ±1 px diameter). There is no occlusion and little motion blur.
- Static extents: ±1-2 px. The rim and net are 3D parts seen almost edge-on, so their heights are only apparent.
  The backboard probably sits in a slightly different depth plane from the ball (it is mounted on the wall, while the ball falls in front of it). In a 2D question,
  the convention is a single scale from the prior object.
- The ball's shadow appears on the wall and floor near the bounce. It is excluded from the mask.
