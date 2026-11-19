# captured_0015s — measurement record (pixels, seconds)

Lab video, 2D, 24 fps, 73 frames (t = frame/24, 0–3.000 s), 1280x720. Real recording whose background
was replaced (SAM2 demo) by a smooth synthetic colour gradient. One person stands still and tosses a small
brown plush toy (red-panda/bear, white face, striped tail) upward with both hands twice, catching it each time.
Image coords: x right, y DOWN (smaller y = higher). No metric scale is assumed anywhere.

## Files
- `scene.json` – inventory, static person extents, camera, events (frames/times), size summaries.
- `tracks/teddy.csv` – toy, all 73 frames: `state` (held / throw_in_hand / release / flight / catch_contact),
  `source` (auto_mask, manual, interp_A_B), `occluded` (1 = partly behind hands), `cx,cy` = bbox centre
  (visible centre, the primary reference point), bbox `x0,y0,x1,y1`, `width_px,height_px`; in flight frames also
  mask centroid `mask_cx,mask_cy`, PCA main-axis length/width/angle and area.
- `tracks/person.csv` – person mask per frame: bbox, height, centroid, `upper_x0/x1` (x extent for rows y<440).
- `bg.png` reconstructed background; `static_body.png` = pixels foreground in >=95% of frames (intermediate).
- `scripts/`: `bg.py` (background), `segment.py` (fg mask helpers + early colour classifier, superseded),
  `flight.py` (in-flight component test), `gridsheet.py`/`cropsheet.py`/`tile.py`/`montage.py` (viewing sheets used for
  manual reading), `build_tracks.py` (final tracks; contains the manual boxes), `probe*.py` (colour probes).

## Method and reliability
- Camera: static (background pixel-identical apart from compression, no shake). Person's feet never move.
- Toy in flight (frames 17–21 and 53–58): foreground = |frame − background| > 45, the toy is the foreground
  component detached from the person; full extent incl. tail, checked on overlays. Reliable to ~±2 px
  (some motion blur). Toy upright in both flights: vertical extent 92–98 px, PCA length 93.5–98 px (≈96 px is the
  best toy height/length in pixels), width 40 px for the body, up to ~60 px with the tail out.
- Toy while held / during the throw and catch (all other frames): the toy's colour overlaps the skin, so
  boxes were read by hand from 2x zoomed grid sheets for 49 key frames and linearly interpolated for the
  rest (frames 1,2,4,5,7,8,32,34,37,39,42,65,67,68,70,71 — slow phases only). Uncertainty ~±4 px on edges,
  larger (±6–8 px) in the motion-blurred throw/catch frames 12–15, 23–29, 46–51, 60–63, where the toy is
  smeared together with the hand. Centre = bbox centre (visible centre, as the lab annotators click).
- Person: top of hair y=132 (134 when head tilts), shoe soles y=640–641 → standing height ≈508 px (509–510 by
  mask rows). Body centre x≈349. The mask's left edge (x0≈278) and lower part are contaminated by
  background-reconstruction artefacts beside the legs — do not use person.csv x0/width for body width; use
  scene.json static extents (chest 293–400, trousers 297–405). Person bbox y0=120 at frame 52 is the toy touching
  the mask, not the head.

## Motion summary (pixels; for orientation only)
- Toss 1: lift starts f10; release f16 (±1); apex f19, cy≈178 (mask cy 179.4); catch f22; back at waist ≈f30.
  Toy rose from cy≈363–375 (waist hold) to 178 ⇒ ~190 px total, but only ~20 px of free rise after release.
- Toss 2: lift starts f45; release f52 (±1); apex f54–55, cy≈150.5 (mask 149.1); catch f59; at waist ≈f64.
- x stays within 425–452 px: motion is essentially vertical.

## Ambiguities
- Release/catch frames are ±1 frame (contact hidden by blur). Free-flight segments are short (≈6–7 frames),
  so per-frame accelerations will be noisy.
- A static background seam (x416–440, y145–216, next to the face blur) was suppressed with a stricter threshold;
  it could slightly clip the toy's left edge in frames 53–56.
- Toy depth is close to the person's (held at her right side); no perspective cues, single planar scale applies.
- The face is blurred (green-grey oval); hair top used as head top.
