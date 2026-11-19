# internet_0058 measurement record

Video: 1920x1080, 30 fps, 113 frames (t = frame/30). Internet footage marked as 2D. An indoor basketball court with the
camera facing the end wall. A woman (white cap, beige tank top, olive cargo pants, white sneakers, face blurred) holds a
basketball. She dips (frames 6-14), then tosses it nearly straight up with a small jump (release about frame 22). The ball
reaches its apex near the top of the frame (frame 42), falls back, and she catches it (about frame 64). She then pushes it
down (about frame 72). It bounces on the floor (frame 77), arcs to the left (peak frame 89), bounces again (frame 102) and
keeps moving left. She walks right (frames 44-80), pauses, then walks back left (frames 92-112).
All values are pixels and seconds. No metric scale is assumed.

## Files
- `scene.json`: inventory (moving and static objects with frame-0 pixel boxes and sizes), events, camera and perspective summary.
- `tracks/ball.csv`: one row per frame (0-112).
  - `cx_px, cy_px`: ball centre in raw image coordinates (y points down).
  - `cx_stab_px, cy_stab_px`: the same centre in frame-0 (camera-drift-compensated) coordinates.
  - `diameter_fit_px`: fitted circle diameter.
  - `bbox_*`: the fitted circle's box.
  - `edge_width_px / edge_height_px`: spread of the accepted edge points.
  - `edge_coverage`: fraction of the 90 rays that gave a valid edge.
  - `held_or_touching`: 1 in frames 0-21 and 64-72.
  - `occluded`: 1 if held, or if edge coverage < 0.6.
  - `method`: `edge_circle_fit`, or `colour_mask_centroid` as a fallback (frames 10, 11, 13).
- `tracks/ball_raw.csv`: coarse colour-blob tracker used to seed the fit. Superseded by `ball.csv`; its extents are inflated.
- `tracks/person.csv`: one row per frame.
  - `bbox_x0..y1`, `center_*`, `height_px`, `width_px`: person box and size.
  - `head_top_y_px`: top of the cap. `feet_bottom_y_px`: lowest shoe point. Both are raw coordinates. `feet_bottom_y_stab_px` is the feet value in frame-0 coordinates.
  - `pants_x_px` (`_stab`): horizontal centroid of the olive pants. This is the most robust body position for walking.
  - `top_bottom_interp`: 1 where head top and feet were linearly interpolated between manual readings.
- `tracks/camera.csv`: per-frame shift of the image centre to frame 0 (`dx_to_f0_px, dy_to_f0_px`), scale, rotation, inlier count, and the full 2x3 affine (`m00..m12`) that maps a raw frame-i pixel to frame-0 coordinates.
- `scripts/`:
  - `camera.py`: camera drift.
  - `track_ball.py` + `track_ball_lib.py`: coarse ball tracker.
  - `refine_ball.py`: ball circle fit, writes `ball.csv`.
  - `track_person.py`: background-subtraction mask. Writes `frames/person_rows.npy` and `frames/person_xc.npy` outside `scene/`.
  - `build_person.py`: merges the mask with manual head and feet readings, writes `person.csv`.
  - `zoom.py`, `zoomstrip.py`, `strips.py`, `montage.py`, `viewmask.py`, `overlay.py`, `probe*.py`, `stats.py`: viewers and probes.
  - Run order: `camera.py`, `track_ball.py`, `refine_ball.py`, `track_person.py`, `build_person.py`.

## Camera
The camera is handheld and drifts slowly; it does not pan around. Background content moves **up** in the image by
35.7 px in total, and by less than 4.4 px horizontally:
- Frames 10-60: about 0.45-0.6 px/frame.
- After frame 80: about 0.1-0.2 px/frame.

Scale stays within 0.6 % and rotation within 0.1°. Drift was measured from ORB features on the wall plane (wall,
backboard, scoreboard) with a RANSAC similarity fit. The floor, the player and the ball path were masked out.

This drift matters for vertical motion: over the free flight it adds about +0.5 px/frame to raw vertical velocity, but
almost nothing to acceleration (the drift's second difference is about 0.02 px/frame²). Use the `*_stab` columns to
measure against the background. Drift accuracy is about ±0.5 px.

## Ball
How the centre and size were measured:
1. A coarse colour tracker followed the ball. Ball pixels are very dark and reddish (OpenCV Lab L ≤ 58, a ≥ 139).
2. From that centre, 90 rays were cast. On each ray, the edge is the halfway crossing in Lab-L between the dark ball
   (L about 20) and the local background. Rays whose background is also dark (pants, black wall trim, hands, hair) were
   rejected.
3. A least-squares circle was fitted to the edges, with outlier rejection, iterated twice.

Overlays (`frames/ov1.png`) confirm that the circle sits on the ball in every phase.

Reliability:
- Centre: about ±0.5 px in free flight (frames 23-63) and in the bounce phase (frames 73-112). About ±2-3 px while held
  (frames 0-21 and 64-72). Frames 9-14 are the worst: the ball is low against the dark pants and hands cover it.
- Diameter: the best value is **50.4 px** (median of frames 35-50, the slow, sharp part near the apex).
  - In the fast parts of the flight, motion blur makes the fit read 46.6-49 px.
  - While held: about 49 px.
  - After the first bounce: about 51 px. After the second bounce: about 53-55 px. The ball is rolling toward the camera,
    so its apparent size grows. This is real perspective, not error.
  - For a "pixel length of the ball" prior, about 50 px is the natural value in the toss phase.
- The apex is at frame 42: raw cy = 30.3 px; stabilised cy = 44.35 px. The ball stays fully in frame; its top edge is at
  y ≈ 5.
- Horizontal motion in flight: cx rises steadily from 1067 (frame 22) to 1122 (frame 63), about +1.3 px/frame, i.e.
  slightly to the right.

Ambiguities:
- The glossy floor shows a mirror reflection of the ball (and the player) below the contact point. The tracker uses the
  real ball, not the reflection.
- Release at frame 22 and catch at frame 64 are ±1 frame (hands touch the ball).
- The bounce frames are the frames of maximum cy: 77 and 102.

## Person
**Head top and feet: manual readings, ±3 px.** The cap (beige) does not separate from the tan wall pads, and the floor
reflection merges with the shoes. So the cap top and lowest shoe point were read by eye on 2x zoom strips every 4th frame
and linearly interpolated between them.

**Left/right extent: automatic.** It comes from background subtraction in stabilised coordinates. The background is a
per-pixel median over frames where the person was more than 170 px away. The extent includes the arms. It is sometimes
widened by artefacts: the left edge jumps to about 1050 in frames 50, 74 and 76, and the right edge to about 1337 in
frames 81-111. Treat `width_px` as approximate; for horizontal body position use `pants_x_px`.

Height from cap top to shoe bottom, raw pixels:

| Pose | Frames | Height (px) |
|---|---|---|
| Standing upright (best "person height" pixel value) | 36-60 | ≈ 344 (range 343-348) |
| Head tilted | 0 | 330 |
| Crouched dip | 8-12 | 291-297 |
| Jump peak, arm overhead not counted | 24 | 351 |
| Walking, bent forward looking down | 80-112 | 323-336 |

- The jump: feet are about 15-19 px above standing level at frame 24 (feet bottom 882 against ≈ 900 when standing).
- Walking: pants_x goes 1095 → 1217 px (frames 44-80), stays about 1220 (frames 80-92), then 1219 → 1094 (frames 92-112).
  Her stabilised feet_y rises from ≈ 901 to ≈ 908-922, so she also moves slightly toward the camera.

## Static objects
Frame-0 pixel boxes are in `scene.json`; they are ±2 px from 2x zooms unless noted:
- Backboard glass: 345 × 198 px (with padding 365 × 214).
- Rim: outer width 95.5 px, centre (883, 297).
- Net bottom: y 392.
- Scoreboard panel: 318 × 155 px.
- Wall pads: 646 × 239 px, 8 panels of about 81 px each.
- Notice boards, fire-extinguisher cabinet, small wall box: ±3 px.

These sit on the wall plane, which is farther from the camera than the player and ball. Pixel ratios between wall
objects and the ball or player are **not** equal-depth ratios. The rim and backboard are about the same depth as the wall.

## Perspective
- The view is roughly frontal to the end wall.
- The wall-floor junction is at y ≈ 795 at frame 0.
- The maroon lane lines (perpendicular to the wall) converge at about (903, 595). This gives the horizon height at frame
  0 (it moves up with the camera drift, about 35 px by the end).
- The scene is otherwise treated as planar, as the benchmark's internet convention does: one scale factor, no perspective
  correction.

## Annotator convention reminder
Internet answers use a single scale = prior value / prior pixel value, positions per frame, forward differences for
velocity and second differences for acceleration. For the ball, use the centre track (raw or `_stab`; prefer `_stab`
when the camera drift matters, mainly for vertical velocity).
