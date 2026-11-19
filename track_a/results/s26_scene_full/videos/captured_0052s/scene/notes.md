# captured_0052s — measurement record (pixels, seconds)

Lab video (real recording), 3D scene, 24 fps, 49 frames (t = frame/24, 0 … 2.000 s), 1280×720.
The original background was removed and replaced by a blue-white sky-like gradient ("Modified with Segment
Anything 2 Demo" watermark, bottom right). So there is **no floor, horizon or wall texture** to give perspective cues.
Camera intrinsics follow the benchmark convention: f = 0.5959×1280 ≈ 762.8 px, principal point ≈ (640, 360), HFOV 80°.
No metric scale is assumed anywhere.

## Scene in one line
A person in a black hoodie (face masked white) crouches behind a large **dark-grey exercise ball**, next to a **blue
recycling bin**. They hold the ball (frames 0–20), push it off and let go (~frame 21), and the ball rolls toward the
camera and to the left (down-left in the image), growing from 128 px to >300 px wide, and leaves the bottom-left
of the frame after frame 45. A **basketball** (bottom centre-right) and a **white sneaker/shoe** (bottom left) lie still
on the floor. The ball passes in front of the shoe (frames 35–43).

## Files
- `scene.json`: inventory, camera, events, summary sizes. Start here.
- `tracks/exercise_ball.csv`: one row per frame (0–48; `visible`=0 for 46–48).
  - `ref_x, ref_y`: **primary visible-centre point**. `ref_method`:
    - `chord` (frames 0–38): x = middle of the widest horizontal chord of the ball mask, y = top row + chord/2,
      i.e. the centre of a round outline. This ignores the dark contact-shadow "tail" that the segmentation adds
      under the ball in frames ~24–31, which makes the plain bbox taller than wide.
    - `top+extrap_diam` (frames 39–45): ball centre below the image. x = middle of the topmost rows,
      y = top + extrapolated diameter/2 (1/diameter fitted linearly against frame over frames 31–38). This is an
      **extrapolation; low reliability**.
  - `max_row_width`: apparent diameter (widest chord). This is the best size measure while `equator_visible`=1.
  - `bbox_*`, `cx_vis, cy_vis` (bbox centre), `mask_cx, mask_cy` (centroid), `vis_width, vis_height`, `area`: visible mask.
  - `circ_cx, circ_cy, circle_r, circle_diam`: RANSAC + least-squares circle fitted on the free outline.
    `cx_fit, cy_fit, ell_*`: ellipse fit (`ell_ok`=0 means the ellipse was rejected and the circle was used).
    Reliable to frame ~31. After that only a short arc is free and the fit overshoots.
  - `top_x, top_y`: topmost point of the ball. It stays clean in every visible frame (useful as a fallback point).
  - `cut_by_frame_edge` (1 from frame 32), `outline_free_frac`, `occluded` flag.
- `tracks/person.csv`: person mask = foreground − ball − static objects. bbox, bbox centre (`cx_vis, cy_vis`),
  centroid, PCA main-axis length/width/angle, `touches_ball`, `touches_bin`, `occluded`.
- `tracks/static_check.csv`: per-frame centroid of the bin, basketball and shoe, plus `<obj>_visible_frac`.
  This is the camera-stability and occlusion check.
- `static_objects.json`: static object extents (bbox, width/height, PCA length/width along the object's own axis,
  centroid).
- `scripts/`: `common.py` (decoding, foreground mask), `track.py` (ball), `ball_ref.py` (reference columns),
  `person_static.py`, `shoe_vis.py`, `build_scene.py`, `run_all.py` (runs all), viewers `look_*.py`.

## Method
Foreground = pixels whose max BGR difference to the per-row background colour is >40. The background colour is the
per-row median of columns 880–1020, which are always empty, because the background is a vertical gradient. Small
morphological open/close follows. The ball is not colour-separable from the black clothes, so it is found
geometrically: contours of the foreground near the position predicted from the previous two frames, a RANSAC
circle constrained to stay close to the predicted radius and centre, a least-squares refinement, and ball mask =
foreground ∩ fitted disc. The masks and points were drawn on frames and checked visually (frames/ scratch images,
not part of the record).

## Key numbers (px)
- Exercise ball at rest (frames 0–17): centre ≈ (612–617, 505–508); apparent diameter 128 px (124–133);
  top at y≈442. Moving: frame 19 (614,515) d137 → 23 (586,536) d151 → 27 (542,558) d163 → 31 (491,591) d190 →
  35 (422,642) d228. Frames 36–38: chord 253/262/283 px, but the silhouette is no longer round.
- Person (crouched, full figure, frames 36–48): bbox ≈ x 556–703 → 559–680, y 344–354 to 535–551, height ≈ 192–204 px.
  In frames 0–22 the lower body is hidden behind the ball, so bbox height there (111–130 px) is only the visible upper body.
- Recycling bin (static): bbox x 681–775, y 485–591 → 95 px wide (at the top rim), 107 px tall. It tapers slightly
  toward the bottom. Centre ≈ (728, 538).
- Basketball (static): bbox x 756–847, y 623–719 → 92 px wide. The bottom touches the image edge, so use the width
  as its diameter. Centre ≈ (801.5, 671).
- Shoe (static): bbox x 250–318, y 627–687. Diagonal (toe up-right, ~141° axis), length along its axis ≈ 85 px,
  width ≈ 36 px. Centroid (286, 657).

## Events
Ball held at rest frames 0–17 (t 0–0.708). Motion starts at frame 18 (t 0.750, ±1 frame). The person releases at
~frame 21 (t 0.875, ±1). Arms are raised frames 22–33. The ball first touches the bottom image edge at frame 32
(t 1.333). It hides the shoe frames 35–43 (t 1.458–1.792). It is last visible at frame 45 (t 1.875); a sliver
remains at bottom-left. No bounce and no collisions; the ball rolls continuously toward the camera.

## Camera
Static. The basketball and shoe centroids are constant to ±0.3 px over all frames, and there is no per-frame
shift. The camera looks down at the floor: nearer floor objects appear lower in the image. Apparent-size change of
the moving ball: diameter 128 → 228 px between frames 18 and 35 (depth ratio ≈ 0.56 if the size is inversely
proportional to depth). The person and static objects keep a constant apparent size.

## Reliability and ambiguities
- Ball centre is good (±2 px) in frames 0–31. It is fair (±5 px) in frames 32–35, where it is cut at the bottom and
  the equator is still visible. It is poor in frames 36–38: near the image bottom-left corner, wide-angle
  perspective widens and flattens the silhouette, so the chord overstates the diameter and the centre is uncertain
  by about 10–20 px. Frames 39–45 are extrapolated: use them only for coarse statements.
- In frames 0–20 the person's hands rest on the ball top and the ball touches the bin. The ball outline there is
  fitted on its free left and bottom arc and agrees with the bbox to within 2 px.
- Segmentation (SAM) artefacts: a dark contact-shadow tail under the ball in frames ~24–31 (bbox taller than wide by
  up to 10%). Ragged edges on the person's arms and hair. Motion blur on the person's arms in frames 20–24.
- The "exercise ball" vs "basketball": the dark-grey large ball moves; the orange basketball never moves.
  The only moving objects are the exercise ball and the person (no locomotion; arm and torso motion only).
- Annotator convention (lab): centres clicked in the image and back-projected with the measured depth. Use
  `ref_x, ref_y` plus the given depth_info with f ≈ 762.8 px, (cx, cy) ≈ (640, 360).
