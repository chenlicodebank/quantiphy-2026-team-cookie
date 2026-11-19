# captured_0034bs – measurement record

Lab video (captured, Orbbec, 24 fps, 49 frames, 1280x720, 3D). The background has been replaced with a blue
gradient (watermark "Modified with Segment Anything 2 Demo"), so only the table and the objects on it are real
footage. t = frame / 24. All values are in pixels and frames; no metric scale has been assumed.
Lab convention: fx ≈ 763 px (0.5959 x 1280), principal point ≈ (640, 360).

## Scene
A wooden table top seen from the front and above, with one dark central leg. On it:
- **tennis_ball_left** (A): a yellow-green tennis ball at the LEFT corner of the table (≈468, 287).
- **tennis_ball_right** (B): a yellow-green tennis ball at the BACK-RIGHT corner (≈819, 257).
- **soccer_ball**: a black/white football, static, centre (601.2, 318.6), diameter ≈105 px.
- **pencil_case**: an orange-yellow elongated case, static, centre ≈(694, 356), ≈99 x 26 px (visible top), axis ≈23° rising to the right.
- **table**: top corners ≈ BL(496,244) BR(833,247) FL(434,415) FR(853,432). Back edge ≈337 px, front edge ≈419 px,
  front-edge thickness ≈20 px. **table_leg**: bbox (634,445)-(657,527), ≈22 px wide.
The two tennis balls look the same. Tell them apart by where they start (left corner vs back-right corner).

## Motion / events
- Frames 0–23: everything is at rest. Both balls start moving at frame 24 (first clear step at 25). The push is not visible.
- A rolls right at ≈11–12 px/frame and goes behind the top of the soccer ball from frame 31. B rolls left and slightly down
  at ≈10–17 px/frame.
- Frame 35→36: both balls move about twice as far as in neighbouring frames, although the timestamps are uniform. This is
  probably a dropped capture frame; treat it with care when computing speeds.
- **Collision at frame 38 (t = 1.583 s)**: the centre separation drops from 50 px (frame 37) to ≈30.5 px, which equals the
  sum of the radii. Afterwards A moves slowly back left/up (≈1.8 px/frame) and stays mostly hidden behind the soccer ball.
  B moves down-right, toward the camera (≈2.9 px/frame). Both are still moving at frame 48.
- The camera is static: frame differences are ≈0 while nothing moves.

## Files
- `scene.json`: inventory, static extents, events, camera notes, and the per-frame A–B centre separation for frames 30–48.
- `tracks/tennis_ball_left.csv`, `tracks/tennis_ball_right.csv`: frames 0–48. Columns: centre (cx, cy) from a circle fit,
  fitted radius and diameter, visible-mask bbox, mask area, occlusion flag, and notes.
- `scripts/`: `track.py` (tracker; it writes track_raw.json), `static.py` (static objects), `write_record.py` (builds the
  record), `overlay.py` / `view.py` (check images), `probe*.py` and `pts.py` (exploration and timestamp check).

## Method and reliability
- Ball mask: difference from a ball-free background (frame 0 with the start regions taken from frame 48), AND hue 22–45,
  which excludes wood and shadows. Before motion (frames 0–23) a hue mask inside the start windows is used instead.
  The centre comes from a least-squares circle fit to the mask boundary, leaving out boundary points next to the soccer
  ball or the other ball. I checked the overlays (frames 0, 25, 30, 33, 35–39, 41, 44, 48) and the circles sit on the balls.
- Expected error: ±1 px for unoccluded B and for A in frames 25–30. For A in frames 31–48 (lower part hidden) it is
  ±2 px, and ±3 px in frames 35–37 (only the top cap is visible). The A centre in frames 0–24 comes from the upper arc,
  because the segmentation removed the ball's lower part at the table corner.
- The bbox and mask area are for the *visible* mask only. While a ball is occluded, use the fitted diameter, not the bbox.
- Apparent diameter: A ≈32 px (frames 25–30, unoccluded), B ≈30.4 px (mean). Neither shows a clear trend, so depth
  changes are small. They are probably equal-sized balls at slightly different depths, plus fit noise. Motion blur in
  frames 26–37 stretches the masks by ≈1–3 px along the motion.
- Perspective: the table top narrows toward the back. Larger image y on the table means closer to the camera.
  Converting to 3D needs the depth_info given with each question (back-project with fx = 763).
