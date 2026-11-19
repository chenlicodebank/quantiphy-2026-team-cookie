# captured_0006 — measurement record

Lab video (real recording), 3D scene, 24 fps, 49 frames (t = 0 … 2.000 s), 1280x720.
Static camera. A person in light-blue overalls standing behind a wooden table holds a yellow
plush pineapple-like toy, tosses it up and forward (toward the camera); it lands on the table near
the front edge, bounces once, tumbles leftward along the front edge, drops off the front-left corner
and falls out of the bottom of the frame. Everything is in pixels and seconds; no metric scale guessed.

## Files
- `scene.json` — inventory (toy, person, table, tripod, monitor, walls/floor), static extents,
  camera info, event list with frames/times, apparent-size summary.
- `tracks/toy.csv` — toy, every frame 0–48 (`visible=0` at frame 48). Columns:
  `cx, cy` reference point = centroid of the full toy mask (yellow body hull + beige face patch);
  `bbox_x0..y1, bbox_w, bbox_h` of that mask; `mask_len_major / mask_wid_minor` = sides of the
  min-area rotated rectangle; `mask_height` = bbox height; `mask_area`, `equiv_diam` = 2·sqrt(area/π);
  `yellow_cx, yellow_cy` = centroid of the yellow pixels only (alternative centre); `flag`.
- `scripts/` — `track_yellow.py` (masking), `make_tracks.py` (writes the csv and
  `frames/mask_check.jpg` overlay), `crops.py` (zoomed check montages), `table.py` (table-top
  segmentation), `camera_shift.py` (background phase correlation), `probe.py`, `print_bottom.py`.

## Method
- Toy mask: HSV yellow (H 18–38, S≥110, V≥120), largest blob + nearby blobs, convex-hull filled,
  plus flat (local std < 1.5) beige pixels adjacent to the hull (the toy's face was replaced by a flat
  beige oval by the video's face anonymiser — same as the person's face), closed and hole-filled.
  The green leaf tuft on top is NOT included (small, few px).
- Overlays of contour + centre on every frame were inspected (frames/mask_check.jpg): the contour
  follows the toy in all frames 0–47. Small protrusions (≤10 px) from the beige rule in f4, f11,
  f21–f27; in f32 the face patch below-left is included (mask extends to table surface).
- Camera: phase correlation of three static regions vs frame 0 gives |shift| < 0.15 px for all
  frames → static camera, no correction needed.
- Camera intrinsics (from the task's lab spec, not measured): fx = fy ≈ 762.8 px, principal point
  ≈ (640, 360). Back-project with `X = (cx-640)·Z/762.8`, `Y = (cy-360)·Z/762.8` given a depth.

## Toy (key numbers)
- Held still f0–f16: cx≈613, cy 221→233 (slow drift down), equiv_diam ≈ 41 px, bbox ≈ 42x38 px
  (face-on, lower edge partly behind fingers).
- Wind-up dip f18 (cy 236.9); moves up with hand f19–f22; release ≈ f22 (t 0.917 s, ±1 frame):
  hand still touching at f22, separated by f23–f24.
- Flight f23–f31; apex (min cy = 138.1) at f25 (t 1.042 s). The toy approaches the camera during
  flight: equiv_diam 39 → 53 (f25) → 61 (f28) → 80 (f31).
- First impact on the table f32 (t 1.333 s), bottom at y≈511 (table front edge y≈514), cx≈553.
- Bounce: airborne f33–f35 (cy up to 423 at f34), second contact f36 (t 1.5 s).
- Tumbles/rolls left along the front edge f36–f42 (cx 492 → 409), lying on its side: long axis
  ~114 px, short ~79 px, equiv_diam ≈ 94–97 px.
- Goes over the front-left corner (≈(392,514)) ≈ f42 (t 1.75 s); falls f43–f47 (cy 506 → 695),
  touches the image bottom at f46, out of view at f48.
- Apparent size: ~41 px while held at the person's depth vs ~95 px on the table near its front edge
  → camera distance on the table ≈ 0.43× the held distance (rough; the toy is not a sphere and
  its orientation changes: face-on in hand, on its side on the table).

## Static objects (frame 48, toy gone)
- Table top corners: back-left (528,431), back-right (805,433), front-left (392,514),
  front-right (978,518); front edge 586 px, back edge ~277 px (same real length → back edge
  ~2.1x farther), front face thickness ~30 px (y 515–545); pedestal x 670–705, y 545→below frame.
- Person: head top y≈45, head x 360–450, body x 310–500, feet below the frame (full height not
  measurable). Body stationary; only the right (image-right) arm moves.
- Tripod: light on top at (688,65), legs span x≈560–840. Monitor: top-right, ~[1000,0,1280,140].

## Reliability / ambiguities
- Centre: ±2 px held/on table; ±5–10 px in strong motion blur (f28–f31, f43–f47) where the blurred
  streak lengthens the mask along the motion (e.g. f30–f31 bbox_h 105–111 px vs ~60 px true size).
  Use equiv_diam or held/table sizes, not blurred-frame bbox, for size questions.
- f33–f35 show a translucent ghost of the toy under it (motion blur / SAM2 edit artefact); the
  mask keeps only the solid part, which is the toy in the air.
- f46–f47 are cut by the bottom frame edge (flag `cut_by_frame_edge`); centre biased upward.
- f0–f19 flag `held_in_hand_partly`: fingers cover part of the lower edge.
- Background is blurred by the SAM2 edit (watermark bottom right); only the toy is sharp.
- Yellow-only centre (`yellow_cx/cy`) differs from the full-mask centre by up to ~4 px when the
  beige face sits at the edge of the silhouette (f32, f35–f37).
