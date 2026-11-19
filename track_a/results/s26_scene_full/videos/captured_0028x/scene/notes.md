# captured_0028x – measurement record

Lab recording (24 fps, 1280x720, 49 frames, 0–2.0 s) shown with its background replaced by black (SAM2 segmentation; there is a watermark in the bottom-right corner). It is a 3D scene. Lab camera convention: f ≈ 763 px, principal point ≈ (640, 360).

## Content
- **ball**: a small white ball, the only moving object. In frames 0–11 it is held almost still at about (720, 312). The hand has been segmented out, but the ball's top looks flattened, probably because the fingers were removed. In frames 11–20 it is lifted slowly, 2–4 px/frame upward. It is released at about frame 20 (apex cy ≈ 292, fit apex 20.7) and falls. It then bounces on the table top at frames **26, 36 and 47**, with apexes at **frames 32 (cy 302) and 42 (cy 314)**. It is rising again at frame 48.
- **ball path**: cx drifts right, 720 → 767 px. Its apparent diameter grows from about 20 px (held) to about 23 (f32), about 27 (f42) and about 28 (f48), so the ball moves toward the camera. Each bounce point appears lower on the table: ball bottom y ≈ 427 (at the table's back edge), then 436, then 453.
- **table_top**: a light-wood slab in a perspective trapezoid. The back edge runs x ≈ 572–855 at y ≈ 426 (≈283 px). The front top edge runs from (463, 487) to (962, 498) (≈500 px). The slab is about 12–18 px thick at the front. The front edge drops about 13 px from left to right, so there is a slight roll or tilt.
- **table_post**: a dark grey pedestal, x 708–748 (40 px wide), visible from y 518 down to the bottom of the frame (201 px visible).
- **Camera**: static. The table mask bbox is identical in every frame and its centroid std is < 0.3 px. There is no floor or horizon; the only perspective cue is the table trapezoid.

## Files
- `scene.json`: inventory, static extents, events, camera.
- `tracks/ball.csv`: one row per frame (0–48) with frame, t_s, centroid (cx, cy), bbox, bbox w/h, mask major/minor extent (PCA axes), mask area, occluded flag and phase label.
- `scripts/track_ball.py`: builds a ball-free background as the per-pixel median of a crop (x 600–900, y 200–560) over all frames. The ball mask is the pixels where |frame − bg| > 40 and brightness > 70, taking the component nearest the previous position. It also writes overlay crops to `frames/`.
- `scripts/measure_static.py`: measures table and post extents and checks camera stability.
- `scripts/events.py`: prints dy and d²y per frame, quadratic fits of the flight arcs, apexes and bounce estimates.

## Reliability and ambiguities
- I checked the overlays visually at frames 0, 20, 26, 36 and 47; the mask covers the whole ball.
- **Motion blur is strong** whenever the ball moves fast (frames 23–26, 35–37, 44–48). In those frames the mask is a vertical streak up to about 50 px long, and the centroid is the centre of the streak (mid-exposure), not a sharp position.
  - In blurred frames, use `mask_wid_minor_px` as the ball diameter, not the length.
  - Bounce frames (26, 36, 47) contain the descent and the rebound in one streak, so their centroids are biased. Exact contact times are sub-frame: the fit gives ≈ 26.2 for the first bounce; the second bounce lies between frames 35 and 37.
- Pixel accelerations on the free-flight arcs are about 7.5–9 px/frame² (2 × the quadratic coefficient). This is only for checking; the depth changes slightly as the ball approaches the camera.
- In frames 0–20 the ball is partly hidden by the removed hand: the mask is about 20 wide × 17 tall instead of round. The width (≈20 px) is the better diameter estimate there. The `occluded` flag is 0 throughout, because nothing visible covers the ball; the `phase` column marks held, blurred and bounce frames.
- Release time is uncertain by ±1 frame: upward motion stops at frames 20–21, and free-fall curvature is clear from frame 21–22 on.
- Table extents are read from mask rows. The rounded corners and segmentation edges give about ±3 px. The bottom of the post is cut off by the frame.
