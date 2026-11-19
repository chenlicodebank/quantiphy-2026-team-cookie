# simulation_0162: measurement record

This is a 2D simulation (Blender render) at 1920x1080, 24 fps, 100 frames (t = frame/24, 0 to 4.125 s). All values are in
image pixels (x to the right, y down) and seconds. No metric scale is recorded, so get it from the question's prior.

## Scene
A side view of a bowling-lane-like track. A **dark-blue marbled ball** is the only moving object. It rolls left to right
along a white lane at a constant image row. The camera is **static**: phase correlation of rows 200–560 against frame 0
gives |shift| < 0.01 px in every frame (columns cam_dx and cam_dy in the track). There are no people, animals, vehicles
or other props.

## Files
- `scene.json`: inventory, ball summary (diameter, row, visibility), static bands, events and camera.
- `tracks/ball.csv`: one row per frame, 0–99.
  - Frames 0–8 and 97–99 have visible=0.
  - `cx, cy`: centre of the fitted circle, which is the sphere centre and therefore the object origin.
  - `radius_px` and `diameter_px`.
  - `circle_x0..y1`: box of the fitted circle, clipped to the image in x.
  - `mask_x0..y1`: raw box of the difference mask. It includes the shadow, so it can run wider or lower than the ball.
  - `visible_fraction`: the share of the disc that lies inside the image.
  - `cut_by_frame_edge`: set when the mask touches the image edge.
  - `occluded`: always 0.
  - `cam_dx, cam_dy`: per-frame camera shift.
- `scripts/`:
  - `track_ball.py`: the tracker.
  - `static_bands.py`: row profile of the static scene.
  - `summarize.py`: writes scene.json and frames/track_check.png.
  - `diff_probe.py`: a diagnostic script.

## How the ball was measured
1. Frame 0 has no ball, so it serves as a clean background.
2. Mask = per-pixel |frame − background| summed over BGR > 40, limited to rows 560–720, then cleaned with a morphological open and close.
3. The ball's contact shadow lies on the lane below and to the right of the ball. To keep it out of the fit, the circle is
   fitted (least squares, one outlier-rejection pass) only to the left and right mask boundaries in rows ≤ 672 and
   the top row. Boundary points on the image border are dropped.
4. Frames where the ball is cut by the image edge (9–18 and 93–96) are refitted with the radius fixed at 40.6 px.
5. I checked the fits by eye on overlays (frames 12, 48, 80 and 95, plus the whole track): the circles sit on the ball rim.

## Reliability
- **Ball centre x:** ±1 px per frame in full view, ±1.5–2 px in the edge frames 9–13 and 95–96 (only a small arc is visible there).
- **Ball centre y:** 647.4 ± 1.5 px. The wobble repeats about every 10 frames. It comes from the rim texture of the rolling ball, not from real
  vertical motion, so the motion is purely horizontal.
- **Ball diameter:** **≈ 81.5 ± 1 px** (median of the fits 81.6). Frames 40–80 give 80.2–81.8. Some early and late frames fit up to 84.7,
  probably because of rim texture or motion blur. At frame 48 the mask runs from y 607 to 688.
- **Apparent size over time:** there is no real size change, so all objects are at one depth. Use a single metres-per-pixel scale.
- **Motion:** the ball enters from the left already moving and speeds up the whole time. Its per-frame step grows from about
  8 px (frames 9→10) to 15 (20→21), 25 (50→51) and 28.4 (90→91), up to about 29 px/frame at the end. The acceleration is largest early and shrinks
  later. Fit only the window your question needs, and smooth over several frames because of the ±1 px noise.

## Events
- Frame 9 (0.375 s): ball first visible at the left edge.
- Frame 17 (0.708 s): ball fully in view.
- Frame 94 (3.917 s): ball starts leaving at the right edge.
- Frame 96 (4.000 s): ball last visible.
- No bounce, impact, contact with another object or direction change. The start and end of the motion are outside the video.

## Static objects
Every static structure is a horizontal band that spans the full width (x 0–1919) and has no visible perspective. The lane
top edge is at y = 639 in every column. Band rows in y, top to bottom:

| Rows (y) | Object |
|---|---|
| 0–238 | Grey-blue wall |
| 238–490 | Pinkish wall |
| 490–516 | Upper rail (26 px) |
| 517–527 | Black gap |
| 528–619 | Back ledge (92 px) |
| 620–639 | Black back gutter (20 px) |
| **640–737** | **White lane** (98 px band; the ball rolls on it; both ends are off-screen, so its length is ≥ 1920 px) |
| 738–817 | Front ledge or bumper (80 px) |
| 818–863 | Black band (46 px) |
| 864–869 | Bright edge line |
| 870–1079 | Light wooden plank floor |

The camera looks slightly down, so the ball's contact point (y ≈ 688) lies inside the lane band.

## Ambiguities
- The ball's shadow (grey, lower right) is part of the raw difference mask (`mask_*` columns) but is excluded from the circle fit.
- Frames 17–18 and 93 are flagged `cut_by_frame_edge` only because the shadow or blur touches the border. The ball itself is inside (visible_fraction = 1).
