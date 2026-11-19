# internet_0014: measurement notes

**Scene.** A drone looks straight down on a full-size artificial-turf football pitch at sunset, with long tree
shadows running diagonally. Video: 1920x1080, 29.764032 fps, 287 frames (9.64 s). It is a 2D scene: the ground
is essentially parallel to the image, the scale is uniform (the centre circle is round, 117.0 vs 117.5 px radii)
and the lines are axis-aligned to within about 0.25°. The only action takes place in and around the RIGHT
penalty area: two people and one yellow ball. Everything else is static.

## Files
- `scene.json`: inventory, static pixel measurements, events, camera, file index.
- `tracks/player_A_light.csv`, `tracks/player_B_dark.csv` (frames 0-286), `tracks/ball.csv` (frames 150-286;
  286 is not detected). Columns: `frame,time_s,x,y,x_stab,y_stab,bbox_x0,bbox_y0,bbox_x1,bbox_y1,length_px,width_px,area_px,detected,occluded`.
  `x,y` are raw image pixels. `x_stab,y_stab` are the same point in frame-0 coordinates, corrected for camera
  drift. Use the stabilised values for displacements and velocities. Bboxes and extents are in frame-0
  coordinates. length/width come from the minimum-area rectangle of the object's mask.
- `camera_affine.csv` (ECC affine registration of every frame to frame 0), `camera_shift.csv` (phase correlation).
- `bg_region.png`: temporal-median background of the action region. `track_paths.png`: the three paths drawn on
  frame 0, with a dot every 30 frames.
- `scripts/`: `camera_motion.py`, `camera_affine.py`, `bgmodel.py`, `track.py` (produces the tracks),
  `overlay.py`/`cropsheet.py` (visual checks), `events.py` (smoothed step and heading used to find events),
  `static_lines.py`, `static_goals.py`, `summary.py`, `probe_color.py`, `detect.py` (an early attempt, not used).

## Camera
Static to within measurement. Over the whole clip the background drifts by at most ~2.2 px relative to frame 0,
with rotation ≤0.076° and scale change ≤0.025%. Per-frame changes are below 0.1 px. The tracks are corrected
anyway (`x_stab`). No pan, no zoom.

## How the tracks were measured
Each frame's action region (x 1300-1650, y 400-820) is warped into frame-0 coordinates and differenced against
a temporal-median background. Cast shadows are removed: pixels uniformly darkened by a factor of 0.55-0.97 are
treated as shadow, while black clothing, which is darker than that, is kept.
- **Ball**: the very bright yellow core (R>205, G>185), grown to the bright blob within 2.5 px. The reference
  point is the blob centre, roughly ±0.5 px.
- **Players**: foreground pixels within 9 px of the predicted position. The reference point is the
  difference-weighted centroid of the body blob, i.e. the visible body centre seen from above, roughly ±1 px.
  In frames 115-117 and 174-180 the two players touch. There the shared pixels are split by 2-means and
  `occluded=1`; centres in those frames are less reliable (±2-3 px).

All tracks were checked visually on zoomed overlays (frames 0-286) and stay on the correct object.

## Objects and sizes (pixels)
- **player_A_light**: light/whitish clothing with an orange top. Starts at (1407, 521), left of the right
  penalty spot, and kicks the ball. Top-down body blob: length about 12 px (10-16), width about 9.5, area about
  57 px².
- **player_B_dark**: black clothing with light limbs and shoes. Starts at (1462, 531), just right of and below
  the spot. Blob length about 14 px (12-16), width about 10, area about 60 px². They chase the ball and take it
  at the end.
- The people are seen from directly above, so a standing height cannot be measured; blob sizes change with
  posture. Their long shadows point toward the lower right (roughly +65° in image coordinates) and are not part
  of the masks.
- **ball**: yellow, diameter 4-5 px (bbox median 4x4, area about 14 px²). That is only 4-5 px, so a ball-size
  prior gives a coarse scale (about ±15%). The pitch markings are a much more precise pixel reference.
- **Static markings** (frame 0, line centres; details in scene.json):
  - Goal line to goal line: about 1309 px (x 286 to 1594-1596.5). Touchline to touchline: about 836 px
    (y 104 to 940-942).
  - Penalty areas: about 217-218 px deep and about 525-527 px wide.
  - Goal areas: about 71.5-72 px deep and about 239 px wide.
  - Centre circle: radius 116.9 px.
  - Penalty spots: (1451.4, 522.2) on the right and (431.8, 522.0) on the left, about 143-146 px from their
    goal lines.
  - Goals: about 101 px between the outer edges of the posts, frame depth about 25 px.
  - A static dark round object (bag?) of about 11 px sits at (1601, 465), beside the right goal's upper post.
  - Positions of the small training goals around the pitch are approximate (read off by eye).

## Events (frame / time)
- 0-18: both players nearly still.
- 19-90: A drifts slowly right (0.3-0.7 px/frame).
- 91-155: A moves down-right (about 1 px/frame).
- 101: B starts moving, downward and then down-right.
- 150: the ball first appears separately, in front of A. Before that it is not visible (with/under A).
- 153-172: the ball is at rest at about (1451.5, 564).
- 172 (5.779 s): kick. A's foot touches the ball; the ball moves from frame 173.
- 173-262: the ball rolls down-left (heading 117-124°). Its smoothed step slows from about 1.4-1.7 px/frame just
  after the kick to about 0.8 px/frame by frame 260.
- 174-180: A and B touch. A then goes back up and is nearly still at about (1455, 555) during frames 193-213,
  then drifts right and down.
- B runs down-left after the ball (up to about 1.5-1.9 px/frame) and reaches it at frames 262-264. The ball's
  direction changes to leftward (heading about -165°). B dribbles left to the end.
- 285: last ball detection, at (1380.5, 645.8). At frame 286 the ball sits on the white penalty-area line
  (x ≈ 1379) at B's feet and is not detected.

## Ambiguities
- The bright white glow at the right penalty spot is a static marking. It is not the ball.
- Identities are kept through the frames 174-180 contact: the light player goes up and the dark player goes
  down-left.
- Motion blur is small. The ball blob grows to 5-6 px on contact frames (172, 177, 262).
- Speeds quoted above are only for describing events. Answering sessions should fit their own motion from the
  per-frame stabilised positions. For the internet-video convention, use one scale = prior / prior pixel value,
  measured the same way (for example the ball's pixel diameter, or a player's pixel length along the motion).
