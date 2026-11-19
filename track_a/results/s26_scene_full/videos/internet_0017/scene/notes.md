# internet_0017 – measurement record (pixels, seconds)

Video: 4096x2160, 22.368421 fps, 28 frames (t = frame/fps, 0–1.207 s). Real footage, 2D: fixed overhead camera
looking straight down at a white desk. Someone types on an Apple keyboard with the right hand while the left hand
holds a black Visa card. No metric scale is recorded (apply one scale = prior world value / prior pixel value).

## Files
- `scene.json` – inventory, static-object pixel sizes/positions, events, camera.
- `tracks/right_hand.csv`, `tracks/left_hand.csv` – per frame (0–27): `ref_x,ref_y` = centroid of the *hand*
  part of the skin mask (skin pixels within 450 px of the fingertip extreme, measured along the arm direction);
  `hand_bbox_*`, `hand_len_px` / `hand_width_px` / `hand_axis_deg` (min-area rectangle of that hand part);
  `tip_x,tip_y` = fingertip extreme; `arm_bbox_*`, `arm_area_px` = whole skin component incl. forearm;
  `occluded=1` because the forearm is always cut by the bottom image edge.
- `tracks/visa_card.csv` – per frame: centre of the min-area rectangle of the convex hull of the dark card mask
  (`ref_x,ref_y`), bbox, `len_px` (long side ≈354–355), `width_px` (≈193–204), axis angle, areas; `occluded=1`
  because the thumb/fingers cover part of the card's left end.
- `camera_shift.json` – phase-correlation shift of 4 static patches vs frame 0 (all < 1 px).
- `static_auto.json`, `mouse_auto.json` – mask-based measurements of static objects.
- `scripts/` – common.py (decoder), camera.py, track.py (tracks + overlays), static.py, mouse.py, crops.py (zoom
  sheets used to read corners by hand), probe.py (colour sampling).

## Methods and reliability
- Camera: static. Background shift < 1 px every frame → measure motion directly in image coordinates.
- Hands: skin mask (R−B > 15, max channel > 90, x > 1400, y > 900), two largest components, left/right by
  centroid x. Overlays at frames 0, 7, 14, 20, 27 checked: masks cover hand and forearm correctly. Light-coloured
  fingernails are not in the mask, so `tip_*` is ~10–20 px short of the true nail tip. The "hand" reference point is
  a convention (450-px hand part); hand_len changes partly because fingers curl/extend. Positions ±3 px.
- Right hand motion: rest/typing frames 0–5, slides up-left frames 6–12 (ref moves from (3263,1483) to (3081,1223),
  ~315 px), holds 12–16, returns down-right 17–23 to ~(3293,1491), rests 23–27. Largest per-frame steps around
  frames 8–10 and 19–21 (~60–75 px/frame).
- Left hand: nearly static (≤ ~20 px drift, frames 8–11 up-left, 18–25 slightly back).
- Visa card: dark-pixel mask (max channel < 60) in x 2350–3000, y 1000–1430 (excludes the wallet below). Card is held
  above the desk and somewhat tilted, so its visible aspect (354 x ~198 ≈ 1.8) is not the 1.586 of a flat card; the
  short side is the less reliable dimension. Long side ±5 px. Moves ≤ 17 px in total.
- Static sizes (frame 0 unless noted): keyboard 1145 x 512 px (manual corners, ±8 px; long axis ~37° down-right);
  mouse length 487 px, width ~250 px (low contrast, shadow on its right side; ±12 px); wallet body 467 x 336 px
  (dark mask minus zipper tab, ±25 px; incl. tab bbox 2443–2940 x 1421–1975); second card (under right wrist)
  335 x 201 px (middle always hidden by forearm, edges extrapolated, ±12 px); pin tin diameter 417 px at (3674,420);
  pen 578 px long (cap end (522,1365) to tip (890,1812)); clipboard runs off the left/bottom edges, only its
  top-right edge (1221 px, corners (502,1110) and (1362,1977)) is complete; plant leaves bbox 306–1337 x 0–701
  (cut by the top edge).

## Ambiguities
- Two black cards: the held **Visa card** (moving, upper, in the left hand) vs the **second card** lying on the
  desk under the right wrist. The black wallet lies between them.
- "Hand" vs "arm": forearms run off the image; use hand_* columns for the hand, arm_* for the whole visible skin.
- No ball / vehicle / free motion; the only real motions are the right hand sliding over the keyboard and small
  movements of the left hand and card. Key-press contacts are not resolvable individually.
- Slight motion blur on the right hand during frames 8–10 and 19–21.
