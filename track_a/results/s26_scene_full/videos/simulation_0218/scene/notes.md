# simulation_0218 – measurement record

Blender render, labelled 2D, 1920x1080, 24 fps, 50 frames (t = 0 … 2.042 s). The camera is static. One moving object:
a blue tracked drilling robot driving left to right in front of a grey industrial wall at **constant velocity**.
It is already moving and partly in view at frame 0, is fully in frame for frames 9–32, and has left by frame 49. All
values are in pixels and seconds; no metric scale is assumed.

## Files
- `scene.json`: inventory (robot plus static scene features), sizes, per-point pixel rates, events, camera and
  perspective notes.
- `tracks/robot.csv`: one row per frame (0–49). Columns:
  - `frame`, `time_s` (= frame/24)
  - `origin_est_x, origin_est_y`: **recommended reference point**. It is the midpoint of the near-side rear corner
    and the drill tip, taken from the two linear fits, so it is exact and uniform for every frame, including frames
    where the robot is partly or wholly off-screen. y is fixed at 582 (the bbox centre). `ground_y` = 894 (bottom of
    the tracks).
  - `bbox_centre_x`: midpoint of the measured silhouette `rear_x` and `tip_x`. It is not uniform, because the rear
    silhouette changes with perspective (see below).
  - `rear_x`: leftmost silhouette point, where the rear of the tracks crosses the white floor line at row 843.
    `rear_measured` = 1 if measured, 0 if taken from the piecewise-linear fit (off-screen frames and frame 36).
  - `barrel_back_x`: back end of the black head barrel (rows 405–430), measured frames 9–47.
  - `tip_x`: drill tip (rightmost point, row ~655). `tip_measured` = 0 means extrapolated (tip off-screen).
  - `bbox_x0, bbox_y0, bbox_x1, bbox_y1`: silhouette box clipped to the image. y is fixed at 270–894.
  - `length_px`: `tip_x - rear_x` (unclipped). `height_px` = 624.
  - `visible_frac`: fraction of the length inside the image. `truncated_by_border`: 1 if the robot is partly outside
    the frame. There are no occluders in this scene.
  - `plate_*`, `head_*`, `arm_*`: template-matched rigid features (chassis nameplate on the near track frame, the
    stripes on the head side, the blue arm box), with sub-pixel x/y. `*_measured` = 0 means the value is
    extrapolated from the linear fit.
- `scripts/`:
  - `bg_and_camera.py`: camera stability check.
  - `lightprobe.py`: the lighting problem and the coloured-mask extents.
  - `features.py`: template matching → `features_out.json`.
  - `extremes20.py`, `profiles20.py`, `floorprobe.py`, `reardebug.py`: silhouette edges at frame 20.
  - `track_robot.py`: final track and fits → `robot.csv`, `track_summary.json`.
  - `overlay.py`: verification drawing.
  - `static.py`: static features.
  - Other probes (`probe.py`, `satprobe.py`, `satview.py`, `measure.py`) are earlier exploration.

## Method
- **Camera:** phase correlation of the ceiling strip against frame 0 gives shifts ≤ 0.66 px (static).
- **Lighting:** a bright light patch moves along the back wall ahead of the robot. Wall brightness changes by up to
  ±60 grey levels, so background subtraction is unreliable on the wall.
- **Points that move rigidly:** I tracked these with `TM_CCOEFF_NORMED` templates taken from frame 20, with parabolic
  sub-pixel refinement, plus the drill tip edge on its own. Every linear fit has residuals ≤ 0.4 px (plate 1.2 px).
  The y values are constant to within 0.6 px. Overlays of the bbox, edges, features and origin on frames 4, 12, 20,
  28, 36 and 44 hit the robot correctly.
- **Silhouette edges:** I measured these from grey profiles where the background is fixed: the rear of the tracks
  against the white floor line, the barrel against the window, the drill tip against the wall. Top (handle, y 270) and
  bottom (tracks, y 894) were checked by profiles at frame 20; with no vertical motion they do not change.

## Motion (pixels per frame, constant)

| point | px/frame | px/s |
|---|---|---|
| origin_est | 52.46 | 1259 |
| chassis plate | 50.75 | 1218 |
| head stripes | 51.87 | 1245 |
| arm box | 54.52 | 1309 |
| drill tip | 54.02 | 1297 |
| rear corner, frames 9–27 | 50.90 | — |
| rear corner, frames 30–47 | 45.80 | — |

There is no acceleration, start, stop, contact or direction change. The motion is purely horizontal.

## Perspective (main ambiguity)
The image is labelled 2D, but the robot is close to the camera. Parts at different depths move at 45.8–54.5 px per
frame. The silhouette outline also changes:
- Left of the image centre, the robot's front face is visible and the rear silhouette is the near-side rear corner
  (50.9 px/frame).
- Right of the centre, its back face shows and the rear silhouette is the far-side corner (45.8 px/frame). The switch
  happens at frames 28–29, when the rear passes x ≈ 1000.

So the apparent length grows from about 600 px (frame 8) to 637 px (frame 20) and 690 px (frame 32).

**For a single 2D scale:**
- Use the length at the frame where the robot is centred on the image: frame 21, **640.5 px** (frame 20: 637.4 px).
- Use the `origin_est` rate, 52.46 px/frame, which comes from the same near-side outline.
- The ratio of length to per-frame displacement is then about 12.2 frames per body length. Using the plate rate
  instead changes this by about 3%.
- Height is 624 px (handle top to track bottom), constant.

The floor marks give a depth vanishing point of about (951, 561), so the horizon is at y ≈ 561, near the image centre.
The focal length cannot be recovered from a single vanishing point.

## Reliability
- **High:** camera static; uniform motion; per-frame displacement of each feature (±0.1 px); tip and plate positions
  (±0.5 px); height (±2 px); frame-20 length (±2 px).
- **Medium:** which pixel plane corresponds to the hidden Blender origin (±3% in rate); sub-part extents in
  `scene.json` (read from a gridded frame, ±5 px); pillar edges (±4 px).
- Frame 48 shows only a ~10 px coloured sliver at x ≥ 1909. The CSV's fit gives visible_frac 0 there, but a few pixels
  are still visible. Frame 0 shows only the front 26% of the robot.
- Small effects: the wheels and tracks rotate, so the wheel-hub template locks onto neighbouring wheels (~95 px
  apart); this is not used. There is mild motion blur, and the robot reflects faintly in the window band and casts a
  soft floor shadow. I found no other moving objects.
