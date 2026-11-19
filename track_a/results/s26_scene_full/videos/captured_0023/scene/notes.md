# captured_0023: measurement record

Lab recording (24 fps, 49 frames, 1280x720, 3D scene). Someone has edited the video with "Segment Anything 2 Demo"
(watermark bottom-right): everything except the table, ramp and book is blurred. The camera is static.
A person crouches behind a wooden table and holds a light-blue book at the top of a white board that leans back as
a ramp. At frame ~21 they let go. The book slides down the ramp toward the camera, drops off the ramp foot onto the
table and lies flat there from frame ~37.
Pixel coordinates: x to the right, y down, origin at top-left. Time t = frame/24.

## Files
- `scene.json`: inventory (book, ramp, table, person, tripod, TV screen, walls), static pixel extents, events,
  camera and perspective cues.
- `tracks/book.csv`: the only tracked object, one row per frame for all 49 frames. Columns:
  frame, t, cx, cy (mask centroid = reference point "visible centre"), bbox_x0/y0/x1/y1 (inclusive), bbox_cx/cy,
  bbox_w/h, len_main_px / width_across_px (minAreaRect of the mask: length along the book's long axis, which stays
  nearly horizontal in the image, and visible extent across it), main_axis_angle_deg, area_px, occluded (always 0),
  motion_blur (1 for f23-35), method.
- `scripts/`: `make_track.py` (final track and overlays), `track_book.py` / `track_book2.py` (earlier mask
  versions), `static_objs.py` (ramp and table extents), `camera_check.py` (camera motion), `diffscan.py`
  (frame-difference scan used to find when motion happens), `view.py` / `probe*.py` (viewing and pixel probes).

## Method
- Book mask: per pixel |frame − book-free background| > 25 (max over BGR), AND not wood- or skin-coloured
  (R−B < 18), largest connected component inside x 440-760, y 320-540. The background is a composite: frame 48 above
  y = 440 and frame 0 below it.
  - Frames 0-21: the mask is also limited to the light-blue cover's colour box, grown 8 px downward to take in
    the page edge. Without this limit it picks up the blurred arms and the edit artifact above the ramp.
  - Frames ≥ 33: the book's warm-white page block looks like the table reflection in the background, so each
    column is filled down to the dark contact line.
- I drew masks, boxes and centroids on every frame and checked them by eye. They sit on the book and cover its
  visible extent.

## Key numbers (px)
- Book on the ramp top (f0-20): bbox x 528-656, y 345-391, centroid ≈ (592.5, 368). Long axis about 127 px.
- Book at rest on the table (f37-48): bbox x 478-651, y 478-513, centroid ≈ (562.4, 495.2). Long axis about 173 px,
  visible height about 30 px (cover top plus page block, seen almost edge-on). Zooming in by hand gives x 477-654.
- How the centroid moves (frame: cx, cy): 20: 592.4, 368.3 | 21: 593.0, 369.3 | 22: 591.6, 374.3 | 23: 589.9, 377.1 |
  24: 590.3, 383.1 | 25: 588.7, 391.5 | 26: 588.0, 399.8 | 27: 587.3, 409.9 | 28: 586.4, 421.7 | 29: 585.4, 435.4 |
  30: 582.7, 450.1 | 31: 579.2, 457.1 | 32: 579.3, 466.4 | 33: 583.8, 476.9 | 34: 574.5, 483.8 | 35: 574.6, 488.4 |
  36: 564.5, 494.2 | 37+: ≈562, 495. All of the motion is down the ramp toward the camera. Image y is foreshortened
  by the ramp's tilt. The apparent length grows from 125 to 173 px as the book comes closer.
- Ramp (white board, static): top edge y ≈ 356 (x 517-660, 145 px wide), bottom edge y ≈ 482 (x 494-676, 183 px
  wide), 126 px tall in the image, corners rounded.
- Table top: front edge y ≈ 532 (x 282-922, 640 px). The dark front band runs y 532-562. The back edge is ≈ y 440,
  roughly x 410-800, and partly hidden.

## Events
- f0-20: the book is held still at the ramp top. The person's hands are on its two ends.
- f21 (t = 0.875 s): release and start of motion. The centroid moves 1 px at f21 and 5 px at f22. The last fully
  static frame is f20. Uncertainty ±1 frame.
- f21-30: the book slides down the ramp, speeding up.
- f30 (1.25 s): the lower edge reaches the ramp foot / table (bbox bottom 481 ≈ ramp bottom edge 482).
- f31-35: the book leaves the ramp, tips forward and lands flat on the table in front of the ramp.
- f37 (1.54 s): the book is at rest. From here on the centroid stays within about 1 px.

## Camera and 3D cues
- Static. Phase correlation of background patches shows less than 0.4 px of shift over the whole clip.
- Lab intrinsics: f ≈ 763 px, principal point ≈ (640, 360).
- The table's left and right edges converge at about (609, 338). The camera is a little above the table top and
  looks almost level.
- The ramp's side edges converge at about (603, −21). Combining this with f = 763 gives a rough ramp inclination of
  about 25° (±5°). This is derived from blurred edges, so use it only as a sanity check.
- The ramp's top edge appears 145 px wide and its bottom edge 183 px. If the board is rectangular, its foot is about
  1.26× closer to the camera than its top.
- If a question gives camera distances for the book, back-project the centroid (cx, cy) using the depth given at
  that time.

## Reliability and ambiguities
- Centroid: about ±1 px while static. About ±3 px during f23-35, because of motion blur and the moment the
  book tips over.
  - Mask jumps: at f33-35 the page-edge fill is patchy. At f31-32 part of the page edge under the cover is missed
    (about 5 px), so cy may sit about 2-3 px high there.
- The reference point is the centre of the visible mask: the oblique cover face plus the front page edge. It is not
  the book's 3D centre. On the ramp the visible face is the cover; on the table the book is seen edge-on.
- The book's long-axis pixel length is the most reliable size cue: about 127 px at the top and about 173 px at rest.
  Its visible height and width depend strongly on viewing angle.
- The person is blurred and was not tracked. The grey-white blob above the ramp top after f21 is an artifact of the
  edit. A thin pale cord or bookmark sticks out of the book's left end on the table (x ≈ 440-478, y ≈ 485-500). It
  is not counted as part of the book.
- No shadows are significant on the ramp. On the glossy table the book hides the ramp's reflection; that was
  removed from the mask by the colour test.
