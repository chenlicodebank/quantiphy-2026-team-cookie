# internet_0016 – measurement record (pixels / seconds only)

Video: 2160x3840 portrait, 29.901099 fps, 91 frames (0-90), t = frame/fps. 2D, internet source.
Grayscale and strongly contrast-boosted: cast shadows are clipped to pure black (gray 0-6), which is
what makes them separable from people (a black shirt is ~10-20).

## Scene
Near-top-down drone view of a whole outdoor basketball court (long axis vertical in the image).
Sun from upper-left, long hard shadows to lower-right. Bottom half: rebound play under the bottom
basket. Ball leaves the bottom rim at frame 0, bounces once (frame 13), is caught by player B (black
shirt) at frame 26 and carried/dribbled to the right. Player A (white shirt) walks up-left. Player C
stands almost still near the top basket with arms over the head. No other people, no vehicles.

## Files
- `scene.json` – inventory, static measurements (court lines, hoops), events, camera.
- `tracks/ball.csv` – frame, t_s, cx/cy (visible centre), cx/cy_bgref (minus camera shift), bbox,
  diameter_px (frames 0-26 only: mean of the bright blob's w and h – the bright blob's width
  under-reads because the right side of the ball is shaded; use bbox height ≈ 33 px, 31-35),
  occluded flag, NCC score, state (free / held visible / hidden). Rows with empty cx = ball hidden.
- `tracks/ball_shadow.csv` – ball's cast shadow, frames 0-26 (dark blob ~37x32 px).
- `tracks/player_A_white.csv`, `tracks/player_B_dark.csv` – every frame 0-90: mask centroid
  (visible centre of the person, shadow excluded), bgref centre, bbox, mask length along main axis
  (PCA), width across it, axis angle, mask area, occluded flag.
- `tracks/player_C_top.csv` – near-static person: template-tracked centre, bbox measured by eye at
  frame 30 (93 x 153 px incl. raised arms) shifted with the track.
- `tracks/camera_shift.csv` – per-frame global image shift vs frame 0 (cam_dx, cam_dy, px);
  `camera_shift.json` holds the same plus the per-landmark template checks.
- `tracks/*_mask_raw.csv` – intermediate output of track_masks.py (same data without bgref columns); ignore.
- `scripts/` – all code: camera.py (shift), background.py (median background, two windows),
  track_ball.py + ball_late.py + ball_check.py (ball), track_masks.py (player masks),
  track_players.py + track_C.py (template tracks, C), assemble.py (final CSVs), court_lines.py,
  summary.py, peek.py / cropsheet.py / dbg_frame.py (viewers). The background image bg.png was
  deleted to keep the record small; rerun background.py first (needs scene/camera_shift.json from
  camera.py) to recreate it. Run order: camera, background, track_ball, track_players, track_masks
  (needs tracks/ball raw json), ball_late, assemble, track_C.

## How measured / reliability
- Camera: phase correlation vs frame 0 (half res) checked against 5 static line-corner templates –
  agree within ~1 px. Drift is small and slow (dy reaches -6..-8 px around frames 75-85, dx up to
  +5 px). For motion questions use the *_bgref_px columns (or subtract camera_shift); the difference
  is at most ~8 px over the clip.
- Ball, frames 0-26 (free flight / bounce): NCC template tracking with sub-pixel peak, ±0.5 px.
  Frame 0 overlaps the rim (score 0.63, ±2 px). Frames 27-39, 41-43 the ball is visible at B's right
  hand (±2 px); 64-68 and 86-90 visible at B's lower body/hand (±3 px). All other frames hidden
  (empty). Checked visually on crop sheets.
- Ball size: vertical extent 33 px median (35 at frame 0 high in the air, 31-32 near the bounce –
  the ball looks slightly larger when higher, i.e. closer to the drone). By eye at frame 6: 35 px.
- Players A and B: background subtraction (|frame - shifted median background| > 30), person =
  foreground with gray > 6 minus the grey rim of shadows, closed with a 25 px ellipse, pieces within
  110 px merged. Overlays checked every 6 frames (masks hit the person, not the shadow).
  * A (white shirt): good; centroid jitter ~±5 px from swinging arms. Stands on the left lane line
    at the start (paint pixels are excluded and bridged).
  * B (black shirt): the black shirt touching its black shadow cannot always be separated, so B's
    mask sometimes loses part of the torso (frames ~10-14, 44-50, 60-64: smaller area) and from
    frame 27 includes the ball and arms; centroid jitter ~±10 px (jumps up to ~23 px at 22-27, when
    the ball joins the mask). Smooth over ~5 frames before differencing.
  * Mask length/width are of the top-down silhouette (arms included), NOT standing height: a person
    seen from above has no measurable height in this view. Typical A silhouette ~100-130 px, B ~110-150 px.
- Player C: tracked with an NCC template (score >0.96); moves only a few px (arms/torso sway).
- Court lines: profiles on the median background; line centres ±1-2 px. Lines are ~10-12 px wide.
  The court is slightly wider at the bottom (camera tilt): bottom lane 639.5 px vs top lane 615 px;
  court width 1879 px at y=300 vs 1963 px at y=3600. Baseline to baseline 3572 px.

## Ambiguities
- Ball 3D motion: the ball's image track mixes horizontal motion and height (top-down view). Its
  shadow shows height: ball-shadow image distance shrinks 247 px (frame 0) -> 22.5 px (frame 13,
  bounce) -> 179 px (frame 26). An annotator likely measured the ball's image position directly.
- Bounce frame 13 (t = 0.435 s) is clear (±1 frame). Catch/contact frame 26 (t = 0.870 s) ±1.
- Player height is not measurable; only top-down silhouette sizes are given.
- The shadows of people/poles/tree are not objects but could be confused with them; the rim and
  backboard are elevated, so their image positions are parallax-shifted relative to the floor lines.
