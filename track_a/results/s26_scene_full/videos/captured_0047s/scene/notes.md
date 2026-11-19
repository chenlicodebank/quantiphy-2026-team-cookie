# captured_0047s — measurement record (lab, 3D, 24 fps, 49 frames, 1280x720)

## Scene
The background has been replaced by a smooth blue gradient (SAM-style; there is a "Modified with Segment Anything 2 Demo"
watermark at the bottom right). There is no floor, horizon or other static scene feature. Objects:
- **ball**: a large dark-grey exercise ball with white highlights, the only moving object. The person holds it still in
  frames 0-12. It is pushed toward the camera and rolls down-left in the image, growing from 118 px to about 280 px. It is
  cut by the bottom edge from frame 33 and has left the frame from frame 47.
- **person**: one crouching person (black hoodie and trousers, white shoes, face blurred) behind the ball. The feet stay
  fixed (shoe bottom y≈543) and only the arms and torso move. The person pushes the ball, throws the arms up at frame 17,
  then lowers them by about frames 40-46.
- **Camera**: static. The pinhole model f = 0.5959·W = 762.75 px with principal point (640,360) comes from the lab
  convention and is used in the ball fit.

## Files
- `scene.json`: inventory, static extents, events, camera.
- `tracks/ball.csv`: one row per frame (0-48). Columns:
  - `center_proj_x/y`: the image projection of the 3D sphere centre. **This is the recommended reference point.**
  - `ray_x/y/z`: unit viewing ray to the centre. 3D centre = depth × ray, where depth is the distance to the centre.
  - `alpha_deg`, `sin_alpha`: the angular radius of the ball. R_world / distance = sin_alpha, so with a known ball
    diameter, distance = (D/2)/sin_alpha. Equivalently, `equiv_diam_px` = 2f·tan(alpha) is the diameter in pixels if
    the ball sat on the optical axis.
  - `ell_*`: the projected silhouette ellipse (centre, major and minor axes, angle). It is elongated off-axis.
  - `sil_bbox_*`: bbox of the full predicted silhouette. It can extend outside the image.
  - `vis_*`: bbox, centroid and area of the visible mask inside the silhouette.
  - Fit diagnostics: `arc_inliers`, `arc_coverage_deg`, `fit_rms_px`.
  - Flags: `cut_by_frame_edge`, `occluded_or_partial`, `visible`.
  - `alpha_smooth_deg` and `equiv_diam_smooth_px`: median-3 plus Savitzky-Golay(7,2) smoothing for frames 13-45, and
    the mean for static frames 0-12.
  - `reliability`: good (0-32), good_cut (33-35), fair (36-41), poor (42-45), invalid_fit (46), not_visible (47-48).
- `tracks/person.csv`: centroid, bbox, height and width of the person mask (foreground minus the ball silhouette),
  plus a flag for overlap with the ball.
- `scripts/`:
  - `track.py`: segmentation and fits.
  - `postprocess.py`: reliability and smoothing.
  - `write_scene.py`: builds scene.json.
  - `check_overlay.py`: draws the visual check.
  - `explore*.py`: scratch scripts.

## Method
1. **Foreground**: fit a robust quadratic per channel to the background gradient, keep pixels whose colour differs by
   more than 35, then fill holes.
2. **Ball fit**: the outer contour points (excluding image-border points) are turned into viewing rays. RANSAC finds a
   cone: a centre direction plus an angular radius. Points where the ball meets the person are not foreground boundary,
   and RANSAC rejects them. The result is refined by least squares, with residuals of about 0.6-1.1 px.
3. **Checks**: I drew overlays at frames 0, 12, 14, 17, 20, 26, 30, 33, 36, 38, 39, 42, 44 and 46. The silhouette
   follows the visible left, top and bottom edges well, and the centre path is a smooth, nearly straight line down-left.

## Reliability and ambiguities
- **Segmentation clips the shaded right side of the ball.** From about frame 25 on, the SAM mask cuts off the dark
  right-hand side with a near-straight edge. As a result:
  - `vis_x1`, `vis_area` and `vis_cx` are biased left and small.
  - The cone fit uses the true left and top arcs, so `center_proj` and `ell_*` are the better values.
  - An annotator clicking the "visible centre" would probably land near `ell_cx/cy` (within a few px of
    `center_proj` early on, up to about 10-25 px apart in frames 36-45).
- **Fit quality by frame range**:
  - Frames 0-35: good. Centre ±1 px; diameter ±1-2 px, with a dip at frame 17 where the release happens and the arc is
    partly hidden by the person.
  - Frames 36-41: only a 130-210° arc is visible and the ball is cut, so diameter is about ±5% (frame 36 is a high
    outlier: 226 raw against 212 smoothed).
  - Frames 42-45: only a short arc is visible and the centre lies below the image; ±10%.
  - Frame 46: invalid.
- **Static size** (frames 0-12): equivalent diameter 118.0 px; silhouette 122.5 × 120.2 px; bbox x 511-632, y 431-553;
  centre (571.6, 491.7).
- **Events**:
  - Motion starts at frame 13 (1 px) and is clear at frame 14.
  - Release is at frame 17 ±1, when the arms fly up.
  - No bounce is visible; the ball appears to roll toward the camera.
  - Exit: last visible frame 46, gone at frame 47.
- **Person height**: in frames 0-16 the person bbox excludes the legs, which are hidden behind the ball. From frame 20
  on, the crouched head-to-shoe height is about 196 px, with bbox x 512-638, y 348-543 (medians). The person never
  stands up.
- **Scale**: I did not estimate any metric scale. Use the given depth or size prior together with `sin_alpha` and the
  rays.
