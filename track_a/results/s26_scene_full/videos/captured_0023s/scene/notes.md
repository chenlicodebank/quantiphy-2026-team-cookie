# captured_0023s — measurement record

Lab video (real recording, background replaced by a flat blue backdrop; "Modified with Segment Anything"
watermark bottom right). 3D scene, 1280x720, 24 fps, 49 frames (t = frame/24, 0–2.000 s).
Benchmark convention for lab clips: fx = fy ≈ 763 px, principal point ≈ (640, 360), no zoom.
All values are pixels / frames / seconds; no metric scale was assumed.

## Scene
A wooden table (brown glossy top, dark front face, one dark grey pedestal leg) seen from the front, camera a little
above the table top. On the table stands a **white inclined board (ramp)**: its top edge is far from the camera, its
bottom edge rests on the table near the camera, so it looks like a trapezoid (top 141 px wide, bottom 179 px).
A **book** (pale blue-grey cover, cream page block, thin yellow-green bookmark string sticking out of its left end) rests
on the top of the ramp, slides down it **towards the camera**, drops onto the table top in front of the ramp and
stops. The book is the only moving object. No people, no other props.

## Files
- `scene.json` — inventory, static geometry, camera/perspective cues, events (frames + times).
- `tracks/book.csv` — book in every frame 0–48:
  `frame, t, ref_x, ref_y` (reference point = centre of the bounding box of the whole visible book, cover + pages),
  `bbox_x0..bbox_y1` (inclusive pixel box), `length_px` (horizontal extent = the book's long axis, which lies across
  the motion direction), `height_px` (vertical image extent: cover face seen at an angle + page-block edge),
  `mask_cx, mask_cy` (centroid of the segmentation mask — biased toward the cover, see below), `tilt_deg`
  (long-axis angle of the mask's min-area rectangle, image coordinates), `bottom_edge_from` (mask / profile),
  `occluded` (always 0), `motion_blur`, `moving`.
- `static_measure.json` — raw output of the static-object script (ramp polygon, table row extents every 5 px,
  leg box, camera-shift check).
- `scripts/` — `track_book.py` (track), `overlay.py` (draws masks/boxes for checking), `static_objects.py`,
  `profiles.py` (gray profiles used to locate edges), `view.py`, `sample*.py` (colour sampling), `bgdiff.py`.

## How the book was measured
Clean background = frame 0 with the book's start region replaced by frame-48 pixels (book gone from the ramp).
Mask = |frame − background| > 28 minus table-coloured (H≤25, S≥65; removes the book's shadow on the table) and
blue-backdrop pixels, opened/closed, largest blob + touching pieces, holes filled. Extents use only rows/columns with
a substantial amount of mask (removes the bookmark string and matte specks).
On the table (frame ≥ 31) the cream page block has nearly the same colour as the table's glossy reflection of the
white board, so it drops out of the mask; there the bottom edge is the lowest dark contact line in the vertical gray
profile below the cover (checked by eye at 3–4x zoom: f33 bottom ≈ 497, f48 ≈ 509–511). Every frame's box was drawn
on the image and inspected (f0, 5, 22–24, 26, 29–36, 48): boxes enclose the full visible book.

Key values:
- At rest on the ramp, f0–20: ref ≈ (592, 370), bbox (530,350)–(654,390), length 125 px, height 41 px.
- At rest on the table, f37–48: ref ≈ (564.5, 496.5), bbox (478,482)–(652,511), length 175 px, height 30 px.
- Apparent length grows 125 → 175 px (×1.40): the book ends ~1.4× closer to the camera (length is measured across
  the motion direction, so it scales ≈ 1/depth). The track moves mostly down the image (+127 px) and slightly left
  (−27 px).

## Events
- f0–20 (0–0.833 s): at rest on top of the ramp.
- f21 (0.875 s): first displacement (release/onset is between f20 and f21).
- f21–30: accelerating slide down the ramp; per-frame vertical step of the centre 1.5, 3, 4.5, 5, 7.5, 8.5, 10.5,
  12, 14, 15.5 px.
- f30 (1.250 s): lower end of the book reaches the ramp's bottom edge (y ≈ 480); book yaws ≈ 8° (right end lower) f29–31.
- f31–33 (1.292–1.375 s): leaves the ramp and lands on the table top; flat by f33.
- f33–37: short slide on the table (steps 10.5, 7, 2.5, 3.5, 2 px); at rest from f37 (1.542 s) to the end.

## Static objects (frame 48)
- Ramp board corners: TL (519,357), TR (659,359), BR (673,479), BL (494,480); bbox (494,356)–(675,483).
- Table top: front edge y ≈ 529–535, front corners ≈ (280,535) and (921,531) (≈640 px wide); back edge y ≈ 442,
  back corners ≈ (440,442), (767,442) (±8 px; matte noise); front face ≈ 30 px thick (y 530–560);
  leg bbox (604,560)–(651,719), 42 px wide, runs off the bottom of the frame.
- Vanishing point of the table side edges ≈ (603, 347) (±40 px x, ±25 px y); horizon ≈ y 350–370, near the principal
  row → camera axis roughly horizontal.

## Camera
Static: phase correlation of the table/ramp area against frame 0 gives |shift| < 0.1 px at f12/24/36/48.

## Reliability and ambiguities
- Static phases: box edges ±1–2 px. End-rest left edge jitters 474–478 because the bookmark string touches the left
  end (true page-block edge ≈ 480); cover top 479–482 depending on threshold.
- Moving frames f23–33 have motion blur: boxes include the blur streak (a few px extra along the motion, i.e. vertically).
  f30–32 the book is tilted/yawed while leaving the ramp; f31 bottom edge is the contact line at the centre columns,
  its right end is a few px lower.
- `mask_cx/mask_cy` are biased toward the cover on the table (pages missing from the mask): use `ref_x/ref_y`.
- The visible face changes (cover seen at a slant on the ramp, more page edge visible on the table), so the visible
  centre is not exactly the same physical point throughout; expect ±2–3 px.
- The book's shadow and the table's reflection of the white board are not part of the book (excluded).
- Background is a segmentation replacement; the edges of the table/backdrop flicker slightly (matte), not motion.
