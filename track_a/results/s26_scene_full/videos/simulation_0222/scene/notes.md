# simulation_0222 — measurement record

Video: 2D Blender render, 1920x1080, 24 fps, 80 frames (t = frame/24, 0–3.29 s). Static overhead camera looking
down into a living room. **The only moving object is a white round robot vacuum.** All units are pixels (x right,
y down) and seconds; no metric scale has been assumed.

## Files
- `scene.json`: inventory (moving and static objects with pixel boxes), events, camera notes.
- `tracks/robot_vacuum.csv`: one row per frame (0–79). Columns:
  - `x, y`: **reference point** = centre of a robust least-squares circle fitted to the mask contour (outlier contour
    points >2 px from the circle are dropped). This is the disc's origin. Use these for positions and speeds.
  - `circle_diam`: diameter of the fitted circle (≈117.3–118.3 px; median ≈117.8).
  - `cx, cy`: mask centroid; `ell_cx, ell_cy`: ellipse-fit centre. Both are biased where the mask is clipped.
  - `bbox_*`: mask bounding box; `length_major`/`width_minor`: ellipse axes; `equiv_diam`: diameter from mask area.
  - `occluded`: 1 where the mask edge is partly lost. That happens at frames 0–7 (the robot overlaps the white dock
    block at x≈1700–1735, which matches the background) and at frames 37–41 (the top edge runs along the console
    shadow and lamp). `mask_clipped` is an automatic flag and is always 0.
- `static_auto.json`: automatic threshold boxes at frame 79. Only `wood_slat_bench` and `vase_on_console` are
  valid; the others failed (the shadow got included or the threshold picked the wrong region). Use `scene.json`
  instead.
- `scripts/`: `diff.py` (frame differencing to find moving regions and check the camera), `track.py` (robot
  mask, circle fit and overlays), `events.py` (per-frame steps and headings for events), `static.py`.

## Measurement and reliability
- Robot mask: |frame − background| > 25 and gray > 185, then the largest component with holes filled. Background
  = frame 0 with the robot's start area taken from frame 79. Overlays at frames 0, 10, …, 79 were checked: the
  contour and circle sit on the robot's rim. The circle-fit centre is good to about ±0.3 px, even at the clipped
  frames. Frame-to-frame step noise is about 0.05 px while the robot stands still (frames 69–79).
- Frames 0–1: the robot sits in the dock and the 0→1 step (0.5 px) is noise. The real motion starts at frame 1
  (±1). Frame 0 position is (1674.1, 423.9).
- Robot size: a disc about 118 px across (circle fit 117.8; bbox 119). Length and width are equal. Height cannot be
  seen from above.
- Path, measured on (x, y): it starts at (1674, 424) and moves left with a slight upward drift. Its topmost point,
  y = 355.9, is at frame 39 (t = 1.625 s), just below the lamp and console (closest approach in frames 35–41, no
  contact visible). It then moves left-down and stops at (650.1, 500.2) by frame 69/70 (t ≈ 2.88–2.92 s), just above
  the left arm of the sofa. Path length over frames 0–79 is 1054.7 px; net displacement is 1026.9 px.
- Per-frame step (px/frame), for orientation only: it rises from about 0 to about 20.5 at frame 25, dips to about
  15.3 at frame 39 during the heading change, peaks at about 23.1 at frame 51, then falls smoothly to 0 at frame 69/70.
- Static objects: the pixel boxes in `scene.json` were read from zoomed, gridded frames, with threshold boxes where
  those worked. The dock, bench and vase are good to ±2 px. The lamp shade (Ø≈145 px), console, sofa, cushions and
  rug are good to ±5 px. The glass side table is seen at an angle and its box is rough.

## Ambiguities
- The camera is static (no global shift). There is mild perspective near the image edges: the inner faces of the
  walls are visible and the glass table is seen obliquely. Tall objects (lamp shade, table top, sofa back) are
  closer to the camera and look slightly larger. The robot and dock are both on the floor, so one px scale holds for
  the robot's motion and size.
- The robot shows up as a faint reflection in the glass side table (top right, y≈100–135) around frames 13–26. This
  is not a second object.
- Similar-looking objects: the white lamp shade, the white vase and the white dock are all static. Only the plain
  white disc moves. The robot casts a faint soft shadow, which the mask excludes.
- Motion blur is negligible.
