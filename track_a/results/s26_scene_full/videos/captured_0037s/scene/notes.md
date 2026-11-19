# captured_0037s – measurement record

Lab video (Orbbec RGB, 1280x720, 24 fps, 49 frames, t = frame/24) with the background replaced by flat green
(Segment Anything 2 watermark bottom right). 3D scene. Camera is **static** (median-background difference shows
nothing but the ball in every frame). Benchmark intrinsics: f = 0.5959*1280 = 763 px, principal point ~ (640,360).

## Scene
A wooden table (single black pedestal) seen obliquely from slightly above. On it, left to right: clear glass jar
with metal lid, flat translucent tape roll, two playing cards in an A-frame (card pyramid) with cards lying flat in
front, tall white cup. Dark blue card with yellow sticker lies flat near the front edge. The only moving object is a
small **white ball** (table-tennis-ball like). It sits on the right rim of the white cup (frames 0-6), sinks a few px
behind the rim (7-11), is launched up-left between frames 11 and 12, and then bounces leftward along the table four
times (behind the card pyramid ~19-20, at the tape roll 28, in front of the jar 36, open table 43), coming toward
the camera; the clip ends with the ball in the air (frame 48).

## Files
- `scene.json` – inventory, static object pixel boxes, ball apparent-size summary, events, camera.
- `tracks/ball.csv` – ball in every frame 0-48: `cx,cy` = centroid of the white mask (the visible centre, the lab
  reference point); `x0..y1` mask box; `w_px,h_px`; `len_main_px` / `width_across_px` = min-area-rectangle long/short
  sides (long side = motion-blur direction, angle `main_axis_deg`); `diam_est_px` = blur-free diameter estimate
  (w_px for rest frames 0-11, width_across for flight frames); `diam_px` = equal-area circle diameter (inflated by
  blur); `diff_*` = box of the raw background-difference blob (includes faint blur/shadow); `occluded` flag + comment.
- `tracks/ball_raw.csv` – same before flags. `statics_raw.json` – automatic static segmentation (tape-roll bottom
  wrong there; corrected value in scene.json).
- `scripts/` – `track.py` (median background, diff blob, white/low-saturation refinement, check images),
  `finalize.py`, `statics.py`, `montage.py`/`strip.py`/`strips_bounce.py`/`views.py` (visual checks).

## Reliability
- Ball centre: +-1 px at rest; +-2-3 px in flight (heavy motion blur, 15-25 px/frame streaks; the blur is symmetric so
  the centroid is near the mid-exposure centre). Overlays (montage) confirmed the mask covers the ball every frame.
- Occluded/biased frames: 9-11 (left part behind cup edge, centroid biased right/down by a few px), 19-20 (behind card
  pyramid, centroid biased upward – bounce-1 lowest point not observed), 28 and 35-36 (overlapping tape roll / jar,
  edges merge). Treat these frames as lower confidence.
- Apparent diameter: ~23 px at rest (frames 0-8) growing to ~39-40 px at frames 44-48 (+-2 px; blur widens the box
  along motion, use `diam_est_px`). Since size ~ 1/depth, the ball ends ~1.7x closer to the camera than at the start.
  Its image y combines height above the table and depth, so bounce image y grows (441, 442, 459) as it approaches.
- Static boxes: +-2 px; cup and jar edges are clean; the tape roll and transparent jar blend with the table at the
  bottom; card boxes include both cards.
- Events: rest end ~6, launch between 11 and 12 (frame 12 is the first clear flight frame), apexes at frames 15, 24,
  32, 40, 47 (image-y minima), bounces at 19/20 (occluded), 28, 36, 43 (image-y maxima; +-0.5 frame).
- No metric scale was assumed; use the question's prior (ball size, depth_info) with f = 763 px.
