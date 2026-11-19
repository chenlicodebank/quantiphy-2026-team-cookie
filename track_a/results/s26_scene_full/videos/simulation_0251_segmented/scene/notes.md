# simulation_0251_segmented — measurement record

2D scene, 24 fps, 51 frames (t = 0 … 2.0833 s), 1920x1080. Segmentation video: the background is plain white,
and the only object is a single light-grey ball (mask RGB about 234). There is no ground, no markings and no other
object. The camera is static: there is nothing in the background, and the ball's y position stays constant.

## Files
- `scene.json`: inventory (one object, "ball"), diameter, key positions, events, camera.
- `tracks/ball.csv`: one row per frame (0–50). Columns:
  - `cx, cy`: reference point. This is the bbox midpoint, i.e. the disc centre, which is the object origin.
  - `cx_centroid, cy_centroid`: mask centroid.
  - `bbox_x0..y1`: inclusive pixel bounding box.
  - `width_x, height_y`: mask extents.
  - `area`, `eq_diam`: mask area and area-equivalent diameter.
  - `clipped` / `occluded`: 1 when the ball is cut by the image border (frames 0 and 1).
- `scripts/`:
  - `probe.py`: grey-level survey.
  - `track.py`: makes the track. It thresholds grey < 245, applies a 3x3 opening and keeps the largest component.
  - `check.py`: quadratic consistency check plus overlay images. Overlays were viewed and the boxes fit the ball in every checked frame.

## Measurements and reliability
- **Ball diameter**: median bbox size is 49 px. Per-frame bbox width is 48–55 px and height is 46–51 px. The mask
  edges are soft and low-contrast, so per-frame extents jitter by ±2–3 px. Use ~49 px (±2) as the size for a size prior.
  Because this is a ball, length, width and height are all the same diameter.
- **Centre positions**: about ±0.7 px. That is the rms residual of a smooth quadratic fit over frames 2–50.
  Bbox midpoint and centroid agree within about 1 px.
  - Frames 0 and 1 are clipped by the left border. Their cx is estimated as right edge − 24 px, giving −15 and 19.
  - The quadratic extrapolation gives −17.9 and 15.6, so frames 0–1 carry roughly ±3 px uncertainty.
  - Frame 0 shows only a ~10 px darker sliver.
- **Motion**: purely horizontal, moving right. y stays at 555–557 px.
  - Per-frame steps fall smoothly from ~33 px/frame (frames 2–10) to ~26 px/frame (frames 45–50).
  - The ball decelerates at an approximately steady rate. Fit your own model for your question.
  - Single-frame differences are noisy (±1.5 px/frame), so use fits or averages over several frames.
- **Events**:
  - The ball enters from the left edge already moving (frame 0) and is fully visible from frame 2 (t = 0.083 s).
  - There is no bounce, contact, stop or direction change.
  - At the last frame (50, t = 2.083 s) the ball is at cx = 1451 px and still moving.
- **Scale**: a single metres-per-pixel factor applies (2D, no perspective). Derive it from whatever prior the question gives:
  - size → 49 px diameter;
  - speed → pixel speed from the track (px/frame × 24);
  - acceleration → pixel acceleration from your own fit to the track (px/frame² × 576).

## Ambiguities
- The mask colour is very close to white, and compression adds faint halos and a few dark speck pixels near the
  ball. The opening step plus the largest-component rule removes them.
- No other objects exist, so there is no possible confusion between objects.
