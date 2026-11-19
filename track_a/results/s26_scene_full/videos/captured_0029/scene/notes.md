# captured_0029 — measurement record

Lab video (Orbbec, 24 fps, 49 frames, 1280x720, 3D scene). A person at the right edge holds a yellow-green
tennis ball at the front-right corner of a wooden table (frames 0-16), releases/pushes it at frame ~17, and the
ball travels across the table away from the camera and to the left, reaches the white board at the back edge of
the table at frame ~30, and comes back toward the camera while still moving left until the end (frame 48).
The video went through a "Segment Anything 2 Demo" (watermark bottom-right); the ball has a faint pale halo.

## Files
- `scene.json` — inventory (ball, hand/person, table, white board, tripod, TV, walls...), static pixel extents,
  camera info, events.
- `tracks/ball.csv` — ball, every frame 0-48. Columns: `x,y` = reference point (visible centre, from a circle fit
  to the mask contour); `diam_px` = recommended apparent diameter; `bbox_*` = mask bounding box; `ellipse_major/minor`
  = fitted-ellipse axes; `circfit_d` = circle-fit diameter; `mask_cx/cy` = ellipse centre of the mask;
  `occluded` (1 = fingers cover the lower part, frames 0-18); `blurred` (1 = strong motion blur, frames 17-23);
  `phase` (held / release / away_to_board / rebound).
- `overlays/` — zoomed mask/circle checks (`ball_XX.png`) and the full path on frame 48 (`path_on_f48.jpg`); kept checks: frames 0, 17, 20, 30, 48.
- `scripts/` — `track_ball.py` (HSV segmentation H 25-42, S>=60, V>=60, largest blob; writes `_raw_ball.json`),
  `write_record.py` (makes ball.csv), `static_objects.py` (camera stability + board/table masks),
  `check_pts.py` (timestamps / frame differences), `draw_path.py`, `probe_hsv.py`.

## How measured / reliability
- Ball centre: least-squares circle fit to the mask contour. While held (0-18) only the upper ~45 % of the contour
  is used, because fingers hide the bottom; centre there is ±3 px. Frames 24-48: ±1 px.
- Apparent diameter (`diam_px`): frames 0-16 the horizontal width (bbox_w, ~110-116 px; fully visible); frames 17-23
  the ellipse minor axis (across the blur streak; ±5 px); frames 24-48 the vertical extent bbox_h (motion there is
  mostly horizontal, so bbox_w is inflated by ~5-10 px of blur). Values: 112 px at frame 0, ~48 px at 24, minimum ~40
  px at 28-30 (farthest point), then growing again to 48 px at frame 48 (coming back toward camera). circfit_d
  includes the pale SAM halo and is ~3-6 px larger. Depth ratios from apparent size (Z ∝ 1/diam) are ±5-10 %.
- With fx = 763 px (benchmark camera, cx,cy ≈ 640,360) a given depth converts pixel offsets to metres; e.g. depth
  from size: Z = fx·D_real/diam_px.
- Camera: static (background phase-correlation shift ≤ 0.1 px over the whole clip).
- Timestamps are regular (pts step 512), but the image step 35→36 is double (21 px vs ~10 px), so one capture frame
  was probably dropped there; treat frame 36+ as possibly 1 frame "later" in true time if it matters.

## Events (frame / t)
- held 0-16 (0-0.667 s), hand wobble ≤ 6 px/frame;
- release / start of motion 17 (0.708 s) ±1; ball clearly free by 18-19; largest image step at 19 (77 px);
- reaches the back white board / direction change 30 (1.25 s): minimum image y and minimum apparent size (28-30);
- rebound toward camera 31-48, ~10 px/frame leftwards, size 42 → 48 px; still moving at the last frame 48 (2.0 s).

## Static objects (frame 48, ±5 px)
Table top corners: front-left (210,539), front-right (1138,588), back-left (420,455), back-right (918,462);
front edge 929 px long, front edge thickness ~30 px; pedestal leg x 628-690 below y 600. White board bbox
(423,333)-(917,457), ~495 x 125 px. Tripod with cyan-lit sensor top at (688,70), legs to y 333. TV top-right.

## Ambiguities
- Whether the ball rolls on the table from release or is briefly airborne in frames 17-20 is unclear (blur and
  hand); from frame ~21 a contact shadow under the ball shows it on the table.
- A second small yellow-green patch under the ball at frames 0-2 (between the fingers, ~(1190-1230, 600-635))
  is merged into the mask bbox while held; bbox_h for frames 0-17 is therefore not the ball height.
- The bounce at frame 30 is inferred from the reversal of the depth trend (size) and image y; the board base is
  partly hidden so actual contact is not directly visible.
