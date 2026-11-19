# captured_0023x — measurement notes

Lab video (real recording, background blacked out by Segment Anything 2), 3D scene, 24 fps, 49 frames (t = 0 … 2.0 s), 1280×720.
Lab camera per benchmark: f ≈ 763 px, principal point ≈ (640, 360). All values here are in pixels/frames. No metric scale is assumed.

## Scene
A light-blue flat rectangular object (**blue_book**: pale-teal cover, cream page-edge side; it looks like a book or a flat box) rests on the top edge of a
**white_board**. The board stands on a wooden **table**, leaning back so its front face is a ramp facing the camera. At about frame 21 the book slides
down the board face toward the camera. At frames 30–32 it tips off the bottom of the board, lands flat on the table at about frame 33, slides a little
forward and to the left, and stops at frame 37. A thin whitish string or stick (**thin_string**) shows at the book's left end from about frame 35
(x ≈ 455–478, y ≈ 488–500). It seems attached to the book. It is the only other thing in view; there are no people and no other moving objects.

## Files
- `scene.json`: inventory (names, aliases, how to tell objects apart, visible frames), static extents, phases, events, camera.
- `tracks/blue_book.csv`: one row per frame (0–48):
  - mask centroid `cx, cy` (the reference point, i.e. the visible centre);
  - bbox centre `bbox_cx, bbox_cy` and bbox `x0, y0, x1, y1, w, h`;
  - minAreaRect `len_main_axis` and `width_across` (on-screen height of the object), plus `axis_angle_deg`;
  - `area_px`, `occluded` (always 0), `phase` and `quality`.
- `static_raw.json`: white-board rows at frame 48 and table-top row extents at frame 0. `camcheck_raw.json`: per-frame camera shift and board rows at frame 0.
- `scripts/`: `track_box.py` (track), `static.py`, `camcheck.py`, `cropsheet.py` (viewer), `probe.py` (colour probe).

## Method
- **Book mask:** I compared each frame with a clean background made of frame 48 above y = 470 (the book has left the board) and frame 0 below y = 470
  (the table before the book lands). A pixel counts as book if it changed and has book colour: blue (H 70–115, S > 15), or unsaturated, or cream
  (H 20–35, S < 55), with V > 110. This colour test leaves out the brown shadow on the wood. The cream side has almost the same BGR as the wood, so
  book-coloured pixels also count where the background is not book-coloured. The script then cleans the mask with a morphological open and close and
  keeps the largest component. I checked overlays of every frame (red mask, green bbox, magenta centroid): they cover the whole book in every phase.
- **Camera:** static. Phase correlation of the table front edge and the pedestal against frame 0 gives shifts below 0.25 px in every frame.

## Key numbers (px)
- **Rest on the board (frames 0–20):** centroid ≈ (591.1, 368.4); bbox ≈ 525–655 × 350–388. Length ≈ 129 and on-screen height ≈ 37, because the
  cover is seen foreshortened on the inclined board.
- **Sliding down the board (frames 21–30):** the centroid's y goes 369.7, 374.0, 378.8, 384.0, 391.4, 400.1, 410.1, 421.6, 435.3, 450.3, with x drifting
  591 → 583. The per-frame step grows steadily (about 1.4 → 15 px).
- **Tipping and landing (frames 31–33):** about 458, 467, 480. **Sliding on the table (frames 34–36):** centroid (568.5, 486.9) → (563.1, 494.5).
- **Rest on the table (frames 37–48):** centroid ≈ (562, 494.9); bbox ≈ 477–655 × 479–512. Length ≈ 176–179 and on-screen height ≈ 28–33. The blue top
  strip is at about y 479–495 and the cream side at about 495–511.
- **Apparent size:** the book's apparent length grows from about 129 to 150 (frame 30) to about 177 px. This is because it moves toward the camera:
  the board top is farther away than the table front.
- **White board:**
  - top edge y ≈ 356, x 517–659 (142 px);
  - bottom edge y ≈ 481, x 494–675 (181 px);
  - vertical extent 125 px.
  - The top is narrower than the bottom, so the top is farther from the camera (the board leans back).
- **Table:**
  - front top edge y ≈ 530, x 285–923 (638 px);
  - front face thickness y 530–558 (28 px);
  - visible back edge y ≈ 440, x 452–759;
  - the side edges converge upward;
  - pedestal leg x 608–649, from y 560 down to the bottom of the frame.

## Events (frame / t)
- At rest: frames 0–20 (t 0–0.833 s).
- Motion starts at frame 21 (t 0.875 s); release is between frames 20 and 21.
- Reaches the bottom of the board and tips: frame 30 (1.25 s).
- Lands on the table: frame 33 (1.375 s).
- Slides on the table: frames 33–36.
- Motion ends: frame 37 (1.542 s).

## Reliability and ambiguities
- **Frames 0–28 and 37–48:** centroid good to about ±1 px. Frames 0–2 have slightly noisier bbox edges (±5 px in x0).
- **Frames 29–33 (`quality = blur_tilt`):** strong motion blur and the book rotating as it tips off the ramp (angle up to about 9°). The mask
  includes blur, so the extents are inflated (width 50–58 px), and the centroid is good to only about ±3–5 px.
- **Frame 36:** the bbox's left edge (470) includes the thin string. Use x0 ≈ 477 for the book itself.
- **Reference point:** the centroid is of the visible faces. On the board that is the cover, and on the table it is the cover strip plus the page side.
  The 3D centre lies a little behind the visible faces. An annotator clicking the "object centre" would pick roughly the bbox centre, which is within
  about 1–3 px of the centroid outside the blur frames.
- **Black speckles** along the book's outline in some frames are matting artefacts of the background removal. The board's lower-left corner merges
  with the book at frame 48, so the board's bottom edge was measured at frame 0.
- **Object identity:** the object's real identity (book or flat box) is uncertain; both names are listed as aliases in `scene.json`.
