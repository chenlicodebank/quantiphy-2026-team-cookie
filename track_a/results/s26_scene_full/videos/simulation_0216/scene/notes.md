# simulation_0216 — measurement record

Video: Blender render, flagged **2D**, 1920x1080, 24 fps, 50 frames (t = 0 … 2.0417 s; frame = round(t·24)).
Everything is in **pixels / frames**; no metric scale is assumed.

## Scene
A living room seen straight on (wall facing the camera). **One moving object: a black cat** (white socks/paws,
white-grey face and chest, tail held upright) that walks **left → right** across the whole clip, in front of the
furniture and parallel to the image plane. Static items, left to right: a wooden slatted bench/side table, a
white-and-blue vase on the left end of a long dark-wood TV stand (black curved metal legs), a black TV on the stand,
a table lamp (white pleated cone shade, copper base) on the right end, and a tall floor mirror in a light wooden
frame leaning on the wall at far right. There are also sunlit patches and window-frame shadows on the wall, and a
tan floor.

**Camera: static.** Phase correlation of the upper image against frame 0 gives a shift of ≤ 0.04 px in every frame.
**Perspective:** none to speak of for the motion. The cat keeps one depth: its paws touch at y ≈ 1020 in every
frame and its apparent body length stays at ~245 px from start to end. So one px→m scale applies to all cat motion.
The furniture stands farther back, against the wall (wall/floor junction y ≈ 950–968), so a scale taken from a
furniture prior is only approximately valid for the cat.

## Files
- `scene.json`: inventory, static-object pixel boxes and extents, camera, events, the cat's manual key-frame
  readings and typical extents.
- `tracks/cat.csv`: one row per frame, 0–49 (the cat is visible and never occluded):
  - `torso_cx, torso_cy`: centroid of the body blob. The blob is the fur mask opened with a 31 px ellipse, i.e.
    body + head without legs, tail or ears. This is the proxy for the rig origin.
  - `body_x_matched, body_y_matched`: **recommended for speeds.** Anchored at frame 0's torso centroid, then the
    frame-to-frame shift of the upper body (back + head, rows 840–935) is added up. The shift comes from matching
    the dark-fur mask, with sub-pixel x. The per-frame steps are in `upperbody_dx_from_prev` /
    `upperbody_dy_from_prev`.
  - `bbox_*`: full-mask box (tail tip, hind paw/leg, nose, lowest detected leg pixel). `length_px` and
    `height_px` come from this box.
  - `notail_*`: the box without the tail. `torso_*`: the box of the body blob (body + head length ≈ nose-to-rump).
  - `mask_cx, mask_cy, area_px`: centroid and area of the full mask. `occluded`: always 0.
- `scripts/`:
  - `bg.py`: camera-shift check.
  - `track_cat.py`: segmentation and track. Background = per-pixel 85th percentile over all frames. Black fur =
    V < 35, or a background difference that is not a "cool" shadow; plus white parts; plus the opened body blob.
  - `body_shift.py`: the matched shifts.
  - `zoom_keyframes.py`, `zoom_static.py`: gridded crops used for the manual readings.
  - `finalize.py`: writes scene.json and the path overlay.
  - Run order: track_cat → body_shift → finalize.

## Key numbers (px)
- **Cat horizontal motion**, roughly steady walk the whole clip:
  - matched upper body: mean 17.73 px/frame, per-frame steps 13.9–20.0 (most 16.7–19.7);
  - total over frames 0→49: 869 px;
  - torso centroid: 863 px;
  - nose, read by eye: 529 → 1399 = 870 px.
  - Vertical motion: only gait bob of ~±5 px. Stride period ≈ 9.3 frames (centroid y minima near frames 6, 15,
    24, 34, 43).
- **Cat size** (manual readings at frames 0/20/40/49, ±3 px):

  | Measure | Pixels |
  |---|---|
  | Nose to rump (body length, no legs/tail) | 248 / 238 / 245 / 248 → ≈ 245 |
  | Full horizontal extent, hind paw/tail to nose (= bbox length) | ≈ 285–310; changes with stride |
  | Paw bottom (y ≈ 1020) to ear tip (y ≈ 850) | ≈ 170 |
  | Paw bottom to tail tip (y ≈ 797–805) | ≈ 215–223 |
  | Body depth, back to belly | ≈ 100–110 |

  The world AABB of the cat would probably span hind paw to nose in length, and paw to tail tip in height
  (the tail is upright).
- **Static objects** (x0, y0, x1, y1):

  | Object | Box | Size |
  |---|---|---|
  | Bench | 25, 780, 492, 992 | 467 wide × 212 high |
  | TV stand | 650, 780, 1423, 990 | 773 × 210 incl. metal legs; cabinet body y 780–915 |
  | TV screen | 814, 528, 1213, 758 | 399 × 230; feet reach y 790 |
  | Vase | 681, 573, 781, 792 | 100 × 219 |
  | Lamp | 1239, 501, 1451, 789 | 288 high; shade 212 wide (y 501–609); base ≈ 50 wide |
  | Mirror | 1578, 390, 1845, 968 | 578 high; 237 wide at top, 247 at bottom (leaning) |

## Events
- No start, stop, turn, jump or contact events: the cat walks the whole time.
- The cat is in front of the bench legs from frame 0 to about 12, and in front of the TV stand from about frame 15.

## Reliability and caveats
- Rig origin: the cat's actual rig origin is unknown. It could sit at the hips or on the ground under the body.
  Horizontal displacement and speed are the same for any body point, to within gait jitter. Absolute positions or
  distances to other objects carry ±~30 px of uncertainty about where the origin sits.
- Centroid noise: `torso_cx` has 3–5 px of per-frame noise because the neck and leg shapes change. Use
  `body_x_matched` for one-frame differences. Path lengths that add up per-frame 2D steps are slightly inflated
  by the centroid's vertical jitter. The matched track gives a path of about 869 px.
- Shadows: the cat throws a long shadow to the right (low sun) onto the floor and the stand. The mask rules exclude
  most of it.
- Paws and face are under-segmented:
  - The grey socks and paws are partly missed, so `bbox_y1` (≈ 990–1008) sits above the true paw contact. Use
    y ≈ 1020 for the ground, read by eye.
  - The grey face is sometimes missed against the dark stand, so `bbox_x1` can be up to ~20 px short (frame 49:
    1380 vs. 1399 by eye). Frames 0–40 agree within 3 px.
- Motion blur on the legs is a few px.
- Static boxes were read by eye on 1.5–3× gridded crops, ±3 px.
