# internet_0048 – measurement record (pixels, seconds; t = frame/30)

## Scene
Indoor gym, side view. 1920x1080, 30 fps, 109 frames (0–108, 3.63 s). Background: 8 tan padded wall
panels over a dark base strip, white wall above, glossy wood floor (strong mirror reflections).
Moving things:
1. **ball**: dark red-brown basketball, the only ball. An off-screen thrower (only hands visible at the left
   edge, frames ~33–45) throws it left→right in an arc. It bounces once on the floor at the right (frame 61)
   and leaves past the right edge (partly visible 63–65, gone from 66).
2. **walker**: a woman in a light beige cap, beige tank top, olive cargo trousers and white trainers with red
   soles (face blurred). She walks in from the left (cap visor first visible ~frame 55, head fully in from 73)
   and walks right, parallel to the wall at constant depth, until the end. She is probably the thrower.

The video is 2D-like. All motion is roughly in one plane parallel to the wall, so one px→m scale is
appropriate. The ball may fly slightly in front of the wall plane: its apparent size grows from about 94 to
100 px towards the right, but most of that growth is motion blur.

## Files
- `scene.json`: inventory, static geometry, events, camera summary, key sizes.
- `tracks/ball.csv`: frames 33–64, one row per frame.
  - `ref_x_px,ref_y_px` is the reference point (visible centre); `ref_*_bg0` is the same point in frame-0
    (camera-compensated) coordinates.
  - Also: mask centroid, least-squares circle-fit centre and diameter, bbox, fitted-ellipse major/minor axes,
    mask area, equivalent-circle diameter.
  - Flags: `cut_by_border` (33, 63, 64) and `merged_or_touching` (34, 35 hands; 61 floor/reflection).
- `tracks/person.csv`: frames 55–108.
  - `head_x,head_y`: centre of a 150x140 head box (cap plus blurred face), tracked every frame 73–108.
    `head_*_bg0` is the camera-compensated version.
  - `cap_top_x,cap_top_y`: top of the cap crown.
  - `sole_red_bottom_y`: bottom row of the red trainer soles. Floor contact ≈ this + 4, which is the bbox
    bottom (`bbox_y1`).
  - `sole_x_min/max`: x extent of the red soles. Plateaus in these columns show the planted foot.
  - `bbox_x0/x1`, `hip_x` (centre of the waistband) and `waist_y`: read by hand at frames 78, 81, 84, 87,
    90, 96, 99, 102, 105 and 108 only.
  - `height_px_cap_to_ground` = floor contact − cap top.
  - `cut_by_left_border` = 1 before frame 73.
- `tracks/camera_shift.csv`: per frame, the similarity transform (m00..m12) that maps frame-0 coordinates
  to frame-i coordinates, plus the shift of the image centre, scale, rotation and number of inliers.
- `scripts/`: everything used.
  - `camera.py`: LK corner flow plus RANSAC similarity, chained over frames.
  - `ball.py`: median background of frames 0–28 warped per frame; dark-red difference blob; circle fit;
    manual overrides.
  - `head_track.py`: NCC template match on the Lab difference-to-background image, template taken from
    frame 90.
  - `soles.py`: red-sole detector.
  - `person_assemble.py`: builds person.csv; contains the manual readings.
  - `static.py`: pad geometry.
  - Viewers: `view.py`, `strip.py`, `pstrip.py`, `check_overlay.py`.
  - Debug: `dbg_*`. `person.py` is an abandoned trousers-segmentation attempt; it is not used.
  - Intermediates (`head_tm.csv`, `soles.csv`, `bg0.jpg`) are in `../frames/`.

## Camera
Not static. There is a slow, smooth hand-held drift: content moves left and up by about −24 px and −37 px
over the clip (−13.7/−23.3 px at frame 60), with roll up to 0.23° and no zoom. That is under 1 % of the
ball's per-frame motion and about 2 % of the walker's. For walker speed, use the `_bg0` columns (motion
against the background). The ball's raw and `_bg0` coordinates differ by about 0.3–0.5 px per frame.

## Ball: reliability
- **Frames 36–60 and 62**: clean mask; centroid accurate to about ±1 px. Steps are about 64–66 px per frame
  horizontally.
- **Frames 33–35**: hand-read from 3x zooms (±3 px). Frame 33 is cut by the left edge: its centre is
  extrapolated with D = 95, ±5 px.
- **Frame 61 (bounce)**: the mask merges with the floor reflection, so the centre comes from a circle fit to
  the upper contour, (1812.5, 827.6), ±5 px. The visible bottom of the ball is about y 870.
- **Frames 63–64**: cut by the right edge. Frame 64's centre = visible left edge + 47.5 px (±5).
  Frame 65 (a sliver at x > 1890) is not tracked.
- **Diameter**: best value is **94 px**.
  - Vertical bbox at frames 44–50 is 93–94 px; horizontal is 95–98 px because of blur; ellipse minor axis
    is 91–95 px.
  - The bbox is enlarged along the motion direction by blur: by 10–17 px at frames 36–39 and 56–60.
- **Events**: release between frames 34 and 35 (fingers touch at 34; free at 35). Apex at frame 45 (y min
  304.8). Floor bounce at frame 61. Exit at 63–65.

## Walker: reliability
- **Head track (frames 73–108)**: smooth, with match score 0.55–0.82. Relative position ±2–3 px; per-frame
  steps are 12–28 px, so they are noisy. Before frame 73 the head is cut by the border and there is no
  track.
- **Gait**: the head bobs (head box y 166–189 px). It leads the hip by about 25–30 px in x.
- **Mean speed**: head_x_bg0 goes 102.8 → 740.9 between frames 73 and 108, about 18.2 px per frame.
  This is a raw displacement for reference, not a fitted model.
- **Cap top** = head box + fixed offset, checked at 3x zoom at frames 78, 90 and 100 (±4 px).
- **Ground contact y**: 867–880 px.
- **Height (cap top to floor contact)**: varies with gait.
  - Minimum about 685 px (frames 77–79); maximum about 715 px (frames 91–93); 711 px at frame 90.
  - She never stands still. For "person height" use about 700 px (±15 px).
  - The cap adds a little above the head.
- **Bbox x extents, hip x and waist y**: hand-read on 1x crops, ±8–10 px. The bbox includes feet and
  swinging hands.
- **Footfalls (red-sole plateaus)**:
  - One foot is planted at x ≈ 36–51 from frame 64 to about 79.
  - The other foot lands at x ≈ 316–349 at about frame 85 and stays to about 101.
  - The first foot lands again at x ≈ 626–639 at about frame 99.
  - Step length is about 290–300 px; stride is about 590 px.

## Static objects (frame-0 coordinates; subtract about 20–35 px in y for late frames because of drift)
- **Pad block**: x from 99 to about 1814–1831 (left edge, slight tilt), y from about 182 to 812.
  - Panel seams at x = 312, 532, 748, 961, 1171, 1389 and about 1610.
  - Each panel is about 213–220 px wide and about 628 px tall.
- **Base strip**: dark, y ≈ 823–860.
- **Small grey wall box**: at the left edge, x 0–35, y ≈ 415–450.

## Ambiguities
- **Floor reflections** of the ball and walker sit just below them; they are excluded from the masks.
- **Walker's shadow** is a soft dark area on the pads, about 100 px to her right/behind. It is not part of
  her.
- **Face blur** is a privacy patch; its outline is used only for tracking.
- **Thrower's hands** (frames 33–45, x < 100) are a separate visible object. They are not tracked.
