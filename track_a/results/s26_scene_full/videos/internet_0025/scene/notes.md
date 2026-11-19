# internet_0025 — measurement record (pixels, seconds)

Video: 1920x1080, 29.970032 fps, 473 frames (0..472), 15.78 s, internet footage, 2D. t = frame / fps.

## Scene
Alpine lake, mountains and cliffs behind, a village shoreline at y≈564. One long traditional wooden boat
(orange-brown varnish, high upturned pointed bow on the RIGHT, square dark stern post on the LEFT) moves
left→right side-on to the camera during the entire clip, poled/rowed by one standing boatman at the stern
(black clothes, face pixelated). Nothing else moves (water ripples, wake lines only).

## Files
- `scene.json` – inventory, key numbers, static objects, events, camera summary.
- `tracks/camera_shift.csv` – per frame: `bg_shift_x/y_px` (where the image centre point of frame 0 moved to),
  `roll_deg`, `scale`, and the inverse similarity `inv_a,inv_b,inv_tx,inv_c,inv_d,inv_ty` that maps frame-i pixels to
  frame-0 pixels: x0 = a·x + b·y + tx, y0 = c·x + d·y + ty.
- `tracks/boat.csv` – every frame 0..472. Columns: `x_img,y_img` reference point (centre of the above-water box:
  midpoint of orange stern and bow tip in x; midway between bow-tip top and waterline in y); `x_stab,y_stab` the same
  point in frame-0 (background-fixed) coordinates; `stern_x,stern_y` (left end of orange hull), `bow_tip_x,bow_tip_y`
  (right-most tip of the upturned bow), `stern_x_stab`, `bow_tip_x_stab`; `mask_cx,mask_cy` centroid of the
  above-water mask; bbox `bbox_x0..y1` (stern x, bow-tip top y, bow x, waterline y); `length_px` (orange only),
  `axis_length_px` (stern point → bow tip, slanted), `stern_post_x` and `length_incl_stern_post_px` (full
  bow-to-stern length including the dark stern post — USE THIS for "boat length"); `hull_top_y`, `waterline_y`,
  `waterline_y_stab`, `hull_height_mid_px` (gunwale to waterline amidships), `height_px` (bow-tip top to waterline),
  `mask_bottom_incl_reflection`, `area_above_waterline`, `occluded` (always 0).
- `tracks/boatman.csv` – every frame: `x_img` (torso column), `y_img`, `head_top_y`, `feet_visible_y` (lowest visible
  dark pixel ≈ deck/gunwale; feet hidden), bbox, `height_px` (visible head-top → gunwale), `width_px` (includes arms
  and the near part of the pole), `torso_x0/x1`, `area_px`, `window_clip`. Not stabilised: map with camera_shift.csv
  if needed.
- `scripts/`: `stabilize.py` (camera), `track.py` (boat + boatman + overlays), `check_ends.py` (zoomed end-point
  check), `summary.py` (numbers quoted here), `pan_check.py` (template-match cross-check of the pan), `pan.py`
  (first, superseded phase-correlation version — it drifted; its output was overwritten), `probe_hsv.py`.

## Camera
Not static: slow pan RIGHT (background moves left) plus slight tilt and ~1° roll, no zoom (scale 0.9992–1.0000).
Image-centre background shift: f150 (−28.8, −9.8), f300 (−44.3, −5.5), f390 (−50.4, +0.6), f472 ≈ (−45, +1) px.
Pan is fastest in the first ~5 s, almost stops 12–13 s, slightly reverses at the end. Residual of the fit ≈0.2 px;
template matching of 4 background patches agrees within ~2 px. Measure boat motion with the `_stab` columns
(motion relative to the background). Over frames 0→472 the boat centre moves +428.3 px stabilised (+386.0 px in raw
image coordinates). Mean stabilised step ≈0.91 px/frame; per-frame steps are noisy (±1 px from mask
quantisation), so smooth over several frames before differencing. Motion is almost purely horizontal
(y_stab 651.5–657.3).

## Sizes (pixels)
- Boat bow-to-stern length (`length_incl_stern_post_px`): 351.9 (mean frames 0–29), 346.0 (221–250), 340.9
  (443–472); ±2 px. The ~3 % decrease over the clip comes from slight yaw or receding (stabilised waterline stays at
  y 672–676) and the bow tip blurring at the end. If a single length is needed for the scale, take the length
  at the question's frame, or ≈352 px at frame 0. Orange-only length is 2–4 px shorter (stern post is dark).
- Boat height: bow-tip top to waterline 34–37 px; hull gunwale to waterline amidships ≈24 px.
- Boatman visible height (head top to gunwale, legs hidden): median 51 px (5–95 %: 47–55) — he bends and
  straightens with each stroke; head is pixelated, so head top is ±3 px. Torso stays 34–57 px right of the
  stern (sways with strokes).
- Static (frame 0, far shore, NOT on the boat's scale): shoreline y≈564; large house with purple roof bbox
  (271,534)-(319,556); small house (360,541)-(386,557); white house right (1700,527)-(1735,557); blue-roof house
  (1794,532)-(1849,556); left wooded headland (0,370)-(205,566); small radio mast at x≈772, y 455–485.

## Events
Boat is moving at frame 0 and still moving at frame 472 (no start/stop in the clip). No bounce, impact or
direction change; heading stays +x. Poling strokes produce surges; smoothed-step minima (slow phases) near
frames 8, 31, 60, 80, 108, 144, 180, 220, 248, 280, 304, 328, 348, 384, 404, 426, 448, 468 — noisy, approximate.

## Reliability / ambiguities
- Boat mask (HSV orange) checked on overlays at frames 0, 47, …, 470: covers the hull fully; orange reflection
  below the waterline is excluded from the box by the detected waterline (shadow line). Stern post and bow tip
  checked at 8× zoom (frames 0, 236, 440): within ~1 px.
- Boatman: dark-clothes blob + head scan; overlays OK, but width includes pole/arms at times and the head is
  pixelated. Feet are never visible.
- Wake (white line at the stern waterline) and an older faint wake line at y≈632 are not objects of the boat.
- Planar convention: the annotators use one scale (prior / its pixel measure); measure the prior's pixel value
  the same way (e.g. bow-to-stern length along the motion direction for the boat).
