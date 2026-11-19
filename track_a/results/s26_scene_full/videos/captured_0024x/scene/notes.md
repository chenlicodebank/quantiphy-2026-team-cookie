# captured_0024x — measurement notes

Lab video (Orbbec, 24 fps, 49 frames, 1280x720, 3D). Background is segmented to black; only the
table, a white ramp board, a support stack of two books and the moving light-blue book are visible.
Benchmark intrinsics: f = 763 px, principal point ~ (640, 360). All values are pixels / seconds; t = frame/24.

## Files
- `scene.json` — inventory, static extents, camera, events.
- `tracks/book.csv` — book track, every frame 0–48: `cx, cy` (centroid of full book mask = visible centre,
  the reference point), bbox, `bbox_w/h`, `mask_len_main_axis` / `mask_wid_across` (minAreaRect of mask),
  `mask_height_px` (vertical image extent), area, `cover_*` (light-blue cover-only mask centroid/extent, an
  alternative centre), `occluded` (0 everywhere), `phase`.
- `scripts/` — `track_book.py` (masks + raw track, overlays), `static.py` (ramp/table polygons, camera
  shift), `write_record.py` (builds record), `probe.py`; `_raw_book.csv`, `_static.json` intermediates.

## Scene / motion
- **book** (only moving object): light-blue cover, cream page block. At rest on the upper ramp frames 0–18
  (centre ~(783.5, 373.0), mask 131 x 44 px). Starts moving at frame 19 (t = 0.792 s), slides down-left along
  the ramp, accelerating (centre step per frame 19→29 roughly 1, 3, 6, 10, 7, 15, 16, 18, 20, 23, 24 px; noisy). Reaches the ramp bottom and
  tips onto the table frames 28–31 (t 1.17–1.29 s; orientation change, ~frame 30 main contact), slides on the
  table decelerating frames 31–35, at rest from frame 36 (t = 1.5 s) at centre ~(569.5, 477.4), mask 151 x 29.5 px
  (edge-on view, width foreshortened).
- **ramp_board**: white board, corners at frame 48: top (750,360)–(858,361), bottom on table (610,468)–(709,489);
  left-edge slope length 177 px. Static.
- **support_books**: two stacked books under the ramp's high end, bbox ~[745,428,853,488]; bottom book dark
  green-grey hardcover (gold spine title) 106 x 35 px. Static.
- **table**: square wooden top on a dark pedestal; top corners left (414,469), front (634,607), right (1103,497),
  back (868,450, partly hidden). Static.
- **Camera**: static (background shift ≤ 0.11 px over all frames). Looks slightly down onto the table from its
  front-left corner; no horizon. The book moves down-left and toward the camera, so its apparent length grows
  from ~131 px (on ramp) to ~151 px (flat on table) partly from orientation change.

## Reliability / ambiguities
- Masks (background difference vs a clean background composite + cover colour) were checked on overlays
  (frames 0, 28, 30, 32, 48): they cover the whole book. Centre uncertainty ~1 px at rest, ~2–4 px in frames
  23–32 (motion blur, mask includes blur streak; frames 28–31 also mix ramp/table phases, mask length/width
  there reflect rotation, not size).
- Start frame 19 is ±1 frame (motion is sub-pixel at 19). Table-contact frame ±1.
- A thin white ribbon/bookmark sticks out of the book at rest on the table (~x 525, y 455); it is excluded
  from the bbox mostly. Static object extents of the support books are read by eye (±3 px).
- No depth is recorded here; questions with depth_info should back-project `cx, cy` with f = 763 px.
